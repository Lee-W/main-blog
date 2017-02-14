---
Title: [C++] 如何create thread
Date: 2013-12-11 00:56
Category: Article
Tags: thread
Slug: how-to-create-thread-in-c-plus-plus
Authors: Lee-W
Summary: 
---

之前因為作業需要使用到multi-thread，就留下了這篇紀錄
這篇會稍微介紹C++11 的`thread`函式庫，還有一點點和`pthread`

<!--more-->

要使用C++11的`thread`在編譯時要加上 `-std=c++11 -pthread` (`-std=c++ -lphread`好像也可以)
ex: `g++ -o t thread.cpp -std=c++11 -pthread`
`-std=c++11` :  是指定c++的版本
`-pthread` (或 `-lpthread`)：使用thread的liberary

下面有寫到join的部份
join是開啟這個thread的上層程式必須等待到這個thread的工作結束了，才可以繼續下面的工作
也就是join以上的程式會與thread搶CPU，join以後的程式就會等待到thread結束才開始

那就直接來看code吧
</br>
</br>
</br>

##C++ 11 thread
###在main裡面直接開啟thread
直接宣告thread型態的變數
thread的constructor的第一個參數是函數名稱，第二個以後就是原本函數的參數

```c++
#include <iostream>
#include <thread>
using namespace std;    

void fun1() {
        cout<<"This is funtion1"<<endl;
}

void fun2(int p1, int p2) {
        cout<<"This is function2"<<p1<<p2<<endl;
}

main(){
        thread t1(fun1);
        thread t2(fun2,1,2);
        t1.join();
        t2.join();
}
```

這樣就可以產生兩個thread，他們會彼此搶CPU的資源
cout似乎是每一個<<會去搶一次，所以如果想要一次印完全部，可能可以考慮使用printf或者是thread的lock功能


###在class內開啟thread
用上面的方法直接呼叫同個class的function會出現錯誤
所以就必須用下面的方法
在宣告thread的時候
第1個參數必須是這個function的完整reference
第2個用this
第3個以後才是原本function的參數
p.s.如果fun1是static，則不用this

```c++
#include <iostream>
#include <thread>
using namespace std;

class A {
public:
        void fun1(int p1) {
                cout<<"This is funtion1"<<endl;
        }

        void fun2() {
                thread t(&example::fun1, this, 1);
                t.join();
        }
};

main()
{
        A a;
        a.fun2();
}
```

最後是如何呼叫其他class的function，這裡包含兩個例子(main, class B)
想法跟上面那種很接近，只是第2個參數改成那個物件的實體
```c++
#include <iostream>
#include <thread>
using namespace std;

class A {
public:
        void fun1() {
                cout<<"This is funtion1"<<endl;
        };
};

class B {
public:
        void fun2() {
                cout<<"This is function2"<<endl;

                thread t(&A::fun1, &a);
                t.join();
        }
private:
        A a;
};

main()
{
        B b;
        b.fun2();

        A a;
        thread t1(&A::fun1, &a);
        t1.join();
}
```
</br>
</br>
##基本的pthread使用
```c++
#include <iostream>
#include <pthread.h>
using namespace std;

struct arg {
        int p1;
};

void* fun1(void* a) {
        arg* argument;
        argument = (arg*) a;
        cout<<argument->p1<<endl;
}

main()
{
        arg* argumentForFun1 = new arg;
        argumentForFun1->p1 = 1 ;

        pthread_t t1;
        pthread_create(&t1,NULL,fun1,argumentForFun1);
        pthread_join(t1,NULL);
}
```
至於pthread如何用在class的function上
可以將function加上static
同樣第3個參數也要改成&A::fun1

# Reference
- [資訊小兵的胡言亂語: [C++] Thread Function相關測試] (http://programmingpaul.blogspot.tw/2013/08/c-thread-function.html)
- [解析Linux中多線程編程並傳遞多個參數實例] (http://17089349.blog.hexun.com.tw/65836836_d.html)
- [linux下C/C++,多线程pthread] (http://www.cnblogs.com/xianghang123/archive/2011/08/11/2134927.html)