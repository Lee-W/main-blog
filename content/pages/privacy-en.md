Title: Privacy
Date: 2026-08-16 14:11 +0800
Modified: 2026-08-16 14:11 +0800
Slug: privacy
Summary: Which third-party services see your browsing information on this site, and how to get in touch.
Lang: en

This page is also available in [臺灣華語](/pages/privacy.html) and [日本語](/ja/pages/privacy.html). The three versions say the same thing; if they differ, the Taiwanese Mandarin version governs.

### What I don't do

This site has no registration, no newsletter, no advertising, and no ad tracking. I do not actively collect, store, or sell your personal data, and there is no dashboard anywhere that tells me who a particular reader is.

That said, a few third-party services do receive some technical information when you visit. Each is described below.

### Analytics

This site uses [Umami Cloud](https://umami.is/) to count page views. According to Umami's own documentation, its tracking code uses no cookies and collects no personally identifiable information, and all collected data is anonymized; see [Umami's privacy policy](https://umami.is/privacy) for details.

What I see is aggregate: how many times each article was read, which sites referred those visits, and rough country and device type. I cannot see individual readers, nor can I tie two visits to the same person.

To be clear about one thing: the mere act of your browser requesting a file from `cloud.umami.is` means that server sees your IP address and browser information.

### Comments

Comments are powered by [utterances](https://github.com/utterance/utterances), which stores each comment as an issue comment in this site's GitHub repository (`Lee-W/main-blog`). Therefore:

* Commenting requires a GitHub account and authorizing utterances to post on your behalf
* Your comment and your GitHub username are **public**, visible to anyone, and indexed by search engines and crawlers
* The data itself lives on GitHub and is governed by the [GitHub Privacy Statement](https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement)
* To delete a comment, you can remove it yourself on GitHub, or email me and I will do it for you

### Content loaded from other sites

Some pages load resources from elsewhere:

* Map pages (such as the coworking page) fetch tiles from [OpenStreetMap](https://osmfoundation.org/wiki/Privacy_Policy), with the mapping library served from unpkg
* Some articles embed external content such as Spotify or SpeakerDeck
* The blogroll links badge images directly from the other sites that host them

Each of these requests lets the remote server see your IP address and browser information. If you would rather it didn't, a content-blocking browser extension works fine here — the written content of this site remains readable without those resources.

### Hosting and connection logs

This site is served as static assets on Cloudflare Workers, so pages reach you from Cloudflare's edge. Cloudflare processes connection logs as needed to operate that service, under the [Cloudflare Privacy Policy](https://www.cloudflare.com/privacypolicy/). I have no access to those logs and do not request them.

### Cookies and browser storage

This site sets no cookies of its own. The only thing it keeps in your browser is your dark/light theme preference (`attila_theme` in `localStorage`), which stays on your device and is never sent to me or to anyone else.

The third-party services above may set cookies of their own — for instance when you sign in to GitHub in order to comment.

### Contact

For any question or request about this page, or about data relating to you, please email [hello+blog@wei-lee.me](mailto:hello+blog@wei-lee.me?subject=Privacy).

This page describes what this site actually does today; I will update it when the services it uses change. It does not constitute legal advice.
