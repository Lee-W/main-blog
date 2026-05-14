Title: 將 Apache 討論串變成電子書的魔法
Date: 2026-05-12 12:10 +0800
Category: Tech
Tags: Airflow, Tool
Slug: apache-thread-to-ebook
Authors: Wei Lee
Lang: zh-tw

昨天剛好看完[葬送的芙莉蓮](https://anilist.co/manga/118586/)第 15 集
順著這個情緒，就取了個魔法般的標題（？？？）

<!--more-->

---

TL;DR
[apache_thread_to_ebook.py](https://gist.github.com/Lee-W/5e5798400132ac3cf0775e33a260e91a)是可以把 Apache 郵件群組討論串轉成電子書的小工具

---

最近覺得 Apache Airflow 開發者郵件群組的信件有點多
一天沒看信箱就會超過 100 封信...
但我的眼睛不好，要太長時間盯著螢幕又很累
再來就是用電腦看，很容易會分心 🙉
終於下定決心要寫個小工具，把這些討論串丟到我的 KOBO Elipsa 閱讀
（Elipsa 3 到底什麼時候要出！）

Apache 的郵件群組背後是使用 [Apache Pony Mail™](https://ponymail.apache.org/)，而這個工具本身是有 [API](https://ponymail.apache.org/docs/api.html) 的
所以其實就是簡單地呼叫 API，取得資料，再整理成 epub 就好

因為我有 Kindle 跟 KOBO，所以兩種閱讀器都有支援
實際做開發的當然也不是我自己，而是 claude.ai
但依然是需要有幾輪的來回才完成這個版本

1. CLI 不支援一次爬多個討論串
2. 輸出的 epub 包含了所有前一封信件的回覆
3. 檔名過長，導致 KOBO 將討論串標題縮減為 ... （這樣我哪知道要先看哪個）

總之，這是完成品，它應該是支援所有在 pony mail 的討論，而不只有 airflow 的

<https://gist.github.com/Lee-W/5e5798400132ac3cf0775e33a260e91a>

這才讓我想起來 uv 有支援直接跑 gist
之前看到覺得很酷，但不知道什麼時候用得到
現在就用得到了

待會準備來細看 Java SDK 跟 AERR 討論
順便來復活一下，一樣是沒人在乎的[Airflow 開發生情報](/tag/airflow-kai-fa-sheng-qing-bao)系列

```sh
uv run https://gist.github.com/Lee-W/5e5798400132ac3cf0775e33a260e91a \
    --kobo --no-epub \
    https://lists.apache.org/thread/gjot4bxj9kygj2fk76kx6tyg8s4hr057 \
    https://lists.apache.org/thread/f275xo3tjd4olsmrc8nggncs62fjnl0x
```

雖然殊難想像這個 gist 會再更動，但作為紀念（？？？）還是附上此刻的程式碼

<!-- blacken-docs:off -->
<!-- rumdl-disable -->
??? 20260512的程式碼快照

    ```python
    # /// script
    # requires-python = ">=3.10"
    # dependencies = [
    #     "httpx>=0.27",
    #     "ebooklib>=0.18",
    #     "click>=8.1",
    # ]
    # ///
    """Fetch a Pony Mail thread from lists.apache.org and produce e-reader formats.

    Dependencies:
      - kepubify (optional): if not on PATH, --kobo falls back to copying the EPUB
        with a .kepub.epub extension (Kobo can still read it).
      - Calibre ebook-convert (optional): required only for --kindle.

    Timezone note:
      On systems where Asia/Taipei is the local zone, timestamps are labelled TST
      (Taiwan Standard Time) instead of CST. CST is ambiguous — it is also used for
      China Standard Time (UTC+8) and Central Standard Time (UTC-6), so most
      operating systems return CST for Asia/Taipei even though TST is the correct
      abbreviation for Taiwan.
    """

    from __future__ import annotations

    import os
    import re
    import shutil
    import subprocess
    from dataclasses import dataclass, field
    from datetime import datetime, timezone
    from html import escape
    from pathlib import Path
    from urllib.parse import parse_qs, urlparse

    import click
    import httpx
    from ebooklib import epub

    PONY_MAIL_BASE = "https://lists.apache.org"
    THREAD_API = f"{PONY_MAIL_BASE}/api/thread.lua"
    EMAIL_API = f"{PONY_MAIL_BASE}/api/email.lua"


    def _detect_iana_zone() -> str | None:
        try:
            link = Path("/etc/localtime").resolve()
            parts = link.parts
            if "zoneinfo" in parts:
                idx = parts.index("zoneinfo")
                return "/".join(parts[idx + 1 :])
        except OSError:
            pass
        tz = os.environ.get("TZ")
        if tz and "/" in tz:
            return tz
        return None


    def tz_label(dt: datetime) -> str:
        if _detect_iana_zone() == "Asia/Taipei":
            return "TST"
        return dt.tzname() or dt.strftime("%z")


    def fmt_local(dt: datetime) -> str:
        local = dt.astimezone()
        return f"{local.strftime('%Y-%m-%d %H:%M:%S')} {tz_label(local)}".rstrip()


    _SENDER_RE = re.compile(r'^\s*"?([^"<]+?)"?\s*<[^>]+>\s*$')


    def parse_sender_name(sender: str) -> str:
        if not sender:
            return "(unknown)"
        if m := _SENDER_RE.match(sender):
            return m.group(1).strip()
        return sender.strip()


    def extract_thread_id(arg: str) -> str:
        if "://" not in arg:
            return arg.strip()

        parsed = urlparse(arg)
        parts = [p for p in parsed.path.split("/") if p]
        if "thread" in parts:
            idx = parts.index("thread")
            if idx + 1 < len(parts):
                return parts[idx + 1]

        qs = parse_qs(parsed.query)
        for key in ("threadid", "thread", "id"):
            if key in qs:
                return qs[key][0]

        if parsed.fragment:
            frag_parts = parsed.fragment.split("/")
            if "thread" in frag_parts:
                idx = frag_parts.index("thread")
                if idx + 1 < len(frag_parts):
                    return frag_parts[idx + 1]

        raise click.BadParameter(f"Could not extract thread id from: {arg}")


    def fetch_thread(client: httpx.Client, thread_id: str) -> dict:
        resp = client.get(THREAD_API, params={"id": thread_id})
        resp.raise_for_status()
        payload = resp.json()
        if not isinstance(payload, dict):
            raise click.ClickException(f"Unexpected API response shape for {thread_id}")
        return payload


    def fetch_email(client: httpx.Client, mid: str) -> dict:
        resp = client.get(EMAIL_API, params={"id": mid})
        resp.raise_for_status()
        payload = resp.json()
        if not isinstance(payload, dict) or "mid" not in payload:
            raise click.ClickException(f"email.lua returned unexpected payload for {mid}")
        return payload


    def collect_mids(node: dict) -> list[str]:
        mids: list[str] = []
        if node.get("mid"):
            mids.append(node["mid"])
        for child in node.get("children", []):
            mids.extend(collect_mids(child))
        return mids


    @dataclass
    class Email:
        mid: str
        message_id: str
        subject: str
        sender: str
        epoch: int
        body: str
        children: list["Email"] = field(default_factory=list)

        @property
        def timestamp(self) -> datetime:
            return datetime.fromtimestamp(self.epoch, tz=timezone.utc)

        @property
        def message_url(self) -> str:
            return f"{PONY_MAIL_BASE}/thread/{self.mid}"


    def build_email_tree(node: dict, emails_by_id: dict[str, dict]) -> Email:
        raw = emails_by_id.get(node.get("mid", "")) or emails_by_id.get(node.get("tid", ""))
        if raw is None:
            raise RuntimeError(
                f"Could not locate email payload for node {node.get('mid') or node.get('tid')}"
            )
        children = [build_email_tree(c, emails_by_id) for c in node.get("children", [])]
        return Email(
            mid=raw.get("mid", ""),
            message_id=raw.get("message-id", ""),
            subject=raw.get("subject", "(no subject)"),
            sender=raw.get("from", ""),
            epoch=int(raw.get("epoch", 0)),
            body=raw.get("body", "") or "",
            children=children,
        )


    def collect_emails(root: Email) -> list[Email]:
        """Collect all emails in the tree, sorted chronologically."""
        items: list[Email] = []
        stack = [root]
        while stack:
            node = stack.pop()
            items.append(node)
            stack.extend(node.children)
        items.sort(key=lambda e: e.epoch)
        return items


    _ATTRIBUTION_RE = re.compile(
        r"""^\s*(
              On\s+.*\bwrote:\s*$
            | .*\bwrote:\s*$
            | -{2,}\s*Original\s+Message\s*-{2,}.*$
            | From:\s+.*$
        )""",
        re.IGNORECASE | re.VERBOSE,
    )

    # Matches the opening line of a multi-line Outlook-style attribution such as:
    #   "On Mon, 12 May 2025 at 10:30, John Smith"  (no "wrote:" yet on this line)
    _ATTRIBUTION_OPENER_RE = re.compile(r"^\s*On\s+.+", re.IGNORECASE)


    def strip_quoted_content(body: str) -> str:
        """Remove all quoted lines (starting with '>') and their attribution lines.

        Handles both single-line attributions ("John wrote:") and multi-line
        Outlook-style attributions ("On Mon 12 May...\\n...John wrote:") that
        immediately precede a quoted block.
        """
        if not (lines := body.splitlines()):
            return ""

        remove = [False] * len(lines)

        # Mark quote lines
        for i, line in enumerate(lines):
            if line.lstrip().startswith(">"):
                remove[i] = True

        # Walk backwards over quote blocks to find and remove attribution lines
        i = len(lines) - 1
        while i >= 0:
            if not remove[i]:
                i -= 1
                continue

            # Found the top of a quote block — skip blank lines above it
            j = i - 1
            while j >= 0 and not lines[j].strip():
                j -= 1

            if j >= 0 and not remove[j]:
                if _ATTRIBUTION_RE.match(lines[j]):
                    # Single-line attribution ("... wrote:") — also look for a
                    # preceding opener line ("On Mon 12 May...\nJohn wrote:")
                    remove[j] = True
                    k = j - 1
                    while k >= 0 and not lines[k].strip():
                        k -= 1
                    # Greedily consume wrapped opener lines upward
                    while (
                        k >= 0 and not remove[k] and _ATTRIBUTION_OPENER_RE.match(lines[k])
                    ):
                        remove[k] = True
                        k -= 1
                elif _ATTRIBUTION_OPENER_RE.match(lines[j]):
                    # The "wrote:" line is missing (truncated attribution) but the
                    # opener is there — remove it and any further wrapped lines.
                    while (
                        j >= 0
                        and not remove[j]
                        and (
                            _ATTRIBUTION_RE.match(lines[j])
                            or _ATTRIBUTION_OPENER_RE.match(lines[j])
                        )
                    ):
                        remove[j] = True
                        j -= 1

            # Jump past this quote block to continue scanning upward
            while i >= 0 and remove[i]:
                i -= 1

        # Rebuild, collapsing consecutive blank lines produced by removal
        result: list[str] = []
        prev_blank = False
        for i, line in enumerate(lines):
            if remove[i]:
                continue
            is_blank = not line.strip()
            if is_blank and prev_blank:
                continue
            result.append(line)
            prev_blank = is_blank

        return "\n".join(result).rstrip()


    def body_to_html(body: str) -> str:
        """Render plain-text body to simple XHTML."""
        return "\n".join(
            [
                "<br/>" if not line.strip() else f"<p>{escape(line)}</p>"
                for line in body.splitlines()
            ]
        )


    def render_email_chapter(email: Email, index: int) -> epub.EpubHtml:
        cleaned = strip_quoted_content(email.body)
        body_html = body_to_html(cleaned)
        ts = fmt_local(email.timestamp)
        name = parse_sender_name(email.sender)
        chapter = epub.EpubHtml(
            title=name,
            file_name=f"chap_{index:03d}.xhtml",
            lang="en",
        )
        chapter.content = (
            "<html>\n"
            f"<head><title>{escape(name)}</title></head>\n"
            "<body>\n"
            f"  <h2>{escape(name)}</h2>\n"
            f"  <p><strong>From:</strong> {escape(email.sender)}<br/>\n"
            f"     <strong>Date:</strong> {ts}<br/>\n"
            f"     <strong>Original message:</strong> "
            f'<a href="{escape(email.message_url)}">{escape(email.message_url)}</a></p>\n'
            "  <hr/>\n"
            f"  {body_html}\n"
            "</body>\n"
            "</html>\n"
        )
        return chapter


    def render_title_page(
        thread_id: str, emails: list[Email], list_id: str | None
    ) -> epub.EpubHtml:
        first = emails[0]
        last = emails[-1]
        thread_url = f"{PONY_MAIL_BASE}/thread/{first.mid}"
        if list_id:
            list_url = f"{PONY_MAIL_BASE}/list.html?{list_id}"
        else:
            list_url = PONY_MAIL_BASE
        fetched = fmt_local(datetime.now(tz=timezone.utc))
        page = epub.EpubHtml(title="Thread info", file_name="title.xhtml", lang="en")
        page.content = (
            "<html>\n"
            f"<head><title>{escape(first.subject)}</title></head>\n"
            "<body>\n"
            f"  <h1>{escape(first.subject)}</h1>\n"
            f"  <p><strong>Thread id:</strong> {escape(thread_id)}</p>\n"
            f'  <p><strong>Original thread:</strong> <a href="{escape(thread_url)}">'
            f"{escape(thread_url)}</a></p>\n"
            f'  <p><strong>List archive:</strong> <a href="{escape(list_url)}">'
            f"{escape(list_url)}</a></p>\n"
            f"  <p><strong>Messages:</strong> {len(emails)}</p>\n"
            f"  <p><strong>First post:</strong> {fmt_local(first.timestamp)}</p>\n"
            f"  <p><strong>Last updated:</strong> {fmt_local(last.timestamp)}</p>\n"
            f"  <p><strong>Fetched at:</strong> {fetched}</p>\n"
            "</body>\n"
            "</html>\n"
        )
        return page


    def build_epub(
        emails: list[Email], thread_id: str, list_id: str | None, out_path: Path
    ) -> None:
        book = epub.EpubBook()
        book.set_identifier(f"lists.apache.org-{thread_id}")
        root_subject = emails[0].subject or "Apache mail thread"
        book.set_title(root_subject)
        book.set_language("en")
        senders = sorted({e.sender for e in emails if e.sender})
        for sender in senders[:5]:
            book.add_author(sender)

        title_page = render_title_page(thread_id, emails, list_id)
        book.add_item(title_page)

        chapters: list[epub.EpubHtml] = []
        for i, email in enumerate(emails, start=1):
            ch = render_email_chapter(email, i)
            book.add_item(ch)
            chapters.append(ch)

        book.toc = (title_page, *chapters)
        book.add_item(epub.EpubNcx())
        book.add_item(epub.EpubNav())
        book.spine = ["nav", title_page, *chapters]

        epub.write_epub(str(out_path), book)


    def convert_with_calibre(epub_path: Path, target: Path) -> None:
        if not shutil.which("ebook-convert"):
            raise click.ClickException(
                "ebook-convert (Calibre) is required for Kindle output. "
                "Install Calibre and ensure ebook-convert is on PATH."
            )
        subprocess.run(["ebook-convert", str(epub_path), str(target)], check=True)


    def convert_with_kepubify(epub_path: Path, target: Path) -> None:
        if not shutil.which("kepubify"):
            click.echo(
                "kepubify not found on PATH; copying EPUB with .kepub.epub extension "
                "(Kobo will still read it, but reading-progress hooks won't be added).",
                err=True,
            )
            shutil.copyfile(epub_path, target)
            return

        # Snapshot existing .kepub.epub files before running so we can identify
        # the newly produced file regardless of how kepubify names it.
        before = set(target.parent.glob("*.kepub.epub"))

        subprocess.run(
            ["kepubify", "-o", str(target.parent), str(epub_path)],
            check=True,
        )

        new_files = sorted(
            set(target.parent.glob("*.kepub.epub")) - before,
            key=lambda p: p.stat().st_mtime,
            reverse=True,
        )
        if not new_files:
            raise click.ClickException(
                f"kepubify ran successfully but no new .kepub.epub file found in {target.parent}"
            )
        produced = new_files[0]
        if produced != target:
            produced.replace(target)


    def process_thread(
        client: httpx.Client,
        thread: str,
        out_dir: Path,
        kindle: bool,
        kobo: bool,
        keep_epub: bool,
    ) -> None:
        thread_id = extract_thread_id(thread)
        click.echo(f"Fetching thread {thread_id} ...", err=True)

        data = fetch_thread(client, thread_id)

        thread_struct = data.get("thread")
        if not isinstance(thread_struct, dict):
            raise click.ClickException("Thread API returned no thread structure.")

        if thread_struct.get("in-reply-to"):
            click.echo(
                "Note: the queried message has an in-reply-to header — "
                "you appear to have started mid-thread, so only this subtree "
                "will be exported. Paste the root message URL to capture "
                "everything above it.",
                err=True,
            )

        # Extract the mailing list id from the API response (e.g. "dev@airflow.apache.org")
        list_id: str | None = data.get("list") or thread_struct.get("list") or None

        emails_raw = data.get("emails") or []
        emails_by_id: dict[str, dict] = {e["mid"]: e for e in emails_raw if "mid" in e}

        all_mids = collect_mids(thread_struct)
        missing = [m for m in all_mids if m not in emails_by_id]
        if missing:
            click.echo(f"Fetching {len(missing)} additional message(s) ...", err=True)
            for mid in missing:
                emails_by_id[mid] = fetch_email(client, mid)

        if not emails_by_id:
            raise click.ClickException("Thread API returned no emails.")

        root = build_email_tree(thread_struct, emails_by_id)
        emails = collect_emails(root)
        click.echo(f"Got {len(emails)} message(s)", err=True)

        safe_subject = (
            re.sub(r"[^A-Za-z0-9-]+", "-", emails[0].subject).strip("-")[:60] or thread_id
        )
        last_updated = emails[-1].timestamp.astimezone().strftime("%m%d")
        base = out_dir / f"{last_updated}-{safe_subject}"

        epub_path = base.with_suffix(".epub")
        build_epub(emails, thread_id, list_id, epub_path)
        click.echo(f"Wrote {epub_path}", err=True)

        conversion_ok = True
        if kindle:
            try:
                target = base.with_suffix(".azw3")
                convert_with_calibre(epub_path, target)
                click.echo(f"Wrote {target}", err=True)
            except Exception:
                conversion_ok = False
                raise

        if kobo:
            try:
                target = Path(f"{base}.kepub.epub")
                convert_with_kepubify(epub_path, target)
                click.echo(f"Wrote {target}", err=True)
            except Exception:
                conversion_ok = False
                raise

        if not keep_epub and conversion_ok:
            epub_path.unlink(missing_ok=True)


    @click.command()
    @click.argument("threads", nargs=-1, required=True)
    @click.option(
        "--out-dir",
        type=click.Path(file_okay=False, path_type=Path),
        default=Path("."),
        show_default=True,
        help="Directory to write outputs to.",
    )
    @click.option("--kindle", is_flag=True, help="Also produce a Kindle .azw3 file.")
    @click.option("--kobo", is_flag=True, help="Also produce a Kobo .kepub.epub file.")
    @click.option(
        "--epub/--no-epub",
        default=True,
        show_default=True,
        help="Keep the pure EPUB output.",
    )
    def main(
        threads: tuple[str, ...], out_dir: Path, kindle: bool, kobo: bool, epub: bool
    ) -> None:
        """Build e-books from one or more Apache mailing-list threads.

        THREADS can be bare thread IDs or full lists.apache.org URLs.
        Multiple values are accepted and processed in order.
        """
        out_dir.mkdir(parents=True, exist_ok=True)

        failed: list[str] = []
        with httpx.Client(timeout=30.0, follow_redirects=True) as client:
            for i, thread in enumerate(threads):
                if len(threads) > 1:
                    click.echo(f"\n[{i + 1}/{len(threads)}] Processing: {thread}", err=True)
                try:
                    process_thread(client, thread, out_dir, kindle, kobo, epub)
                except (click.ClickException, RuntimeError, httpx.HTTPError) as exc:
                    click.echo(f"ERROR: {exc}", err=True)
                    failed.append(thread)

        if failed:
            click.echo(
                f"\n{len(failed)} thread(s) failed:\n"
                + "\n".join(f"  {t}" for t in failed),
                err=True,
            )
            raise SystemExit(1)


    if __name__ == "__main__":
        main()
    ```
<!-- rumdl-enable -->
