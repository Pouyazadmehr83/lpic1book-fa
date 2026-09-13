Title: 109.3 عیب یابی اساسی شبکه
Date: 2010-12-03 10:20
Category: LPIC1
Tags: LPIC1, 102, LPIC1-102-500
Authors: Jadi
sortorder: 420
Summary: 

_وزن: 4_

کاندیداها باید بتوانند مشکلات شبکه را در میزبان مشتری عیب یابی کنند.

### حوزه های دانش کلیدی

* رابط های شبکه را به صورت دستی پیکربندی کنید، از جمله مشاهده و تغییر پیکربندی رابط های شبکه با استفاده از iproute2.
* پیکربندی دستی مسیریابی، از جمله مشاهده و تغییر جداول مسیریابی و تنظیم مسیر پیش فرض با استفاده از iproute2.
* مشکلات اشکال زدایی مرتبط با پیکربندی شبکه.
* آگاهی از دستورات `net-tools` قدیمی.


### شرایط و امکانات

* `ip`
* `hostname`
* `ss`
* `ping`
* `ping6`
* `traceroute`
* `traceroute6`
* `tracepath`
* `tracepath6`
* `netcat`
* `ifconifg`
* `netstat`
* `route`

<iframe width="560" height="315" src="https://www.youtube.com/embed/sAzkN5P2-0E?si=P1r5KgfEvit_BMFW" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

### عیب یابی مشکلات شبکه

هنگامی که یک مشکل مرتبط با شبکه به شما گزارش می شود، باید اقدامات زیادی را انجام دهید تا بفهمید علت اصلی مشکل کجاست. برای مثال، اگر گزارش می‌گوید «نمی‌توانم صفحات وب را باز کنم»، باید از بررسی اینکه آیا رابط شبکه IP دارد یا خیر، اگر بالا است، مسیریابی درست است و اگر DNS خوب کار می‌کند و اگر همه چیز درست است، باید سعی کنید از طریق دستور `ping` به سروری در اینترنت دسترسی پیدا کنید و اگر مشکلی مشاهده کردید، باید ببینید که ترافیک شما در کجاست._IN_ در این درس، این مراحل اولیه را مرور خواهیم کرد.

#### ifconfig & ip

همانطور که می دانید، دستورات `ifconfig` و `ip` را می توان برای بررسی آدرس IP رابط های خود استفاده کرد. اگر یک کارت شبکه قرار است کار کند، به آدرس IP و ماسک شبکه صحیح نیاز دارد. اجازه دهید کامپیوتر خودم را بررسی کنم تا ببینم آدرس IP دارد:

```text
[jadi@debian ~]$ ip addr show
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host
       valid_lft forever preferred_lft forever
2: wlp3s0: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc pfifo_fast state DOWN group default qlen 1000
    link/ether f0:de:f1:62:c5:73 brd ff:ff:ff:ff:ff:ff
3: enp0s25: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP group default qlen 1000
    link/ether 8c:a9:82:7b:89:06 brd ff:ff:ff:ff:ff:ff
    inet 192.168.1.35/24 brd 192.168.1.255 scope global dynamic wlp3s0
       valid_lft 254836sec preferred_lft 254836sec
    inet6 fe80::8ea9:82ff:fe7b:8906/64 scope link
       valid_lft forever preferred_lft forever
[jadi@debian ~]$ 
[jadi@debian ~]$ 
[jadi@debian ~]$ 
[jadi@debian ~]$ ifconfig
enp0s25   Link encap:Ethernet  HWaddr f0:de:f1:62:c5:73  
          inet addr:192.168.1.35  Bcast:192.168.1.255  Mask:255.255.255.0
          inet6 addr: fe80::8ea9:82ff:fe7b:8906/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:231586 errors:0 dropped:0 overruns:0 frame:0
          TX packets:200220 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000
          RX bytes:198053888 (198.0 MB)  TX bytes:51583154 (51.5 MB)

lo        Link encap:Local Loopback  
          inet addr:127.0.0.1  Mask:255.0.0.0
          inet6 addr: ::1/128 Scope:Host
          UP LOOPBACK RUNNING  MTU:65536  Metric:1
          RX packets:221752 errors:0 dropped:0 overruns:0 frame:0
          TX packets:221752 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0
          RX bytes:150859909 (150.8 MB)  TX bytes:150859909 (150.8 MB)
```

هر دو دستور نشان می دهد که آدرس IP من صحیح است. این ممکن است به مودم Wi-Fi و 192.168.1.35 به عنوان IP و 255.255.255.0 معقول به نظر می رسد.

> لطفاً توجه داشته باشید که می‌توانید با استفاده از `man ip` راهنمایی کامل در مورد `ip` دریافت کنید یا با استفاده از `man ip-address` (یا هر دستور فرعی دیگری) راهنمای بخش خاصی را دریافت کنید.

#### پینگ و پینگ6

این رایج ترین ابزار هنگام عیب یابی مشکل شبکه است. این یک بسته ICMP را به مقصدی ارسال می کند و اگر پاسخی دریافت کند، نه تنها آن، بلکه تمام آمار را به شما اطلاع می دهد. در زیر، مسیر پیش فرض خود را بررسی می کنم و سعی می کنم آن را پینگ کنم. همیشه باید بتوانید روتر پیش‌فرض خود را پینگ کنید، اگرچه گاهی اوقات سیستم‌های پارانوئید ICMP را در شبکه مسدود می‌کنند و با وجود اینکه متصل هستید، پاسخی دریافت نمی‌کنید.

```text
jadi@debian:~$ ip route show
default via 192.168.70.1 dev enp0s1
172.17.0.0/16 dev docker0 proto kernel scope link src 172.17.0.1 linkdown
192.168.70.0/24 dev enp0s1 proto kernel scope link src 192.168.70.2
jadi@debian:~$ ping 192.168.70.1
PING 192.168.70.1 (192.168.70.1) 56(84) bytes of data.
64 bytes from 192.168.70.1: icmp_seq=1 ttl=64 time=1.11 ms
64 bytes from 192.168.70.1: icmp_seq=2 ttl=64 time=0.855 ms
^C
--- 192.168.70.1 ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 1002ms
rtt min/avg/max/mdev = 0.855/0.984/1.113/0.129 msec
```

من می توانم دروازه خود را پینگ کنم، اما آیا می توان با استفاده از آدرس IP به سروری در اینترنت دسترسی پیدا کرد. برای یافتن پاسخ، 4.2.2.4 را پینگ می کنیم. این سرور در اینترنت بسیار شناخته شده است و بسیاری از افراد از آن برای بررسی اتصال IP خود استفاده می کنند.

```text
[jadi@debian ~]$ ping 4.2.2.4
PING 4.2.2.4 (4.2.2.4) 56(84) bytes of data.
64 bytes from 4.2.2.4: icmp_seq=1 ttl=50 time=108 ms
64 bytes from 4.2.2.4: icmp_seq=2 ttl=50 time=111 ms
64 bytes from 4.2.2.4: icmp_seq=3 ttl=50 time=113 ms
^C
--- 4.2.2.4 ping statistics ---
3 packets transmitted, 3 received, 0% packet loss, time 2003ms
rtt min/avg/max/mdev = 108.160/111.233/113.717/2.338 ms
```

این هم خوب کار میکنه اما آیا می توانم به google.com هم پینگ کنم؟

```text
[jadi@debian ~]$ ping google.com
ping: unknown host google.com
```

آها! ما مشکل را پیدا کردیم. در این حالت من یک آدرس IP صحیح روی دستگاه خود دارم، می توانم دروازه پیش فرض خود را پینگ کنم و می توانم 4.2.2.4 را پینگ کنم، اما نمی توانم google.com را پینگ کنم. پیام خطا "میزبان ناشناس" است. این بدان معناست که رایانه من نمی تواند google.com را به آدرس IP خود ترجمه کند. این یک مشکل DNS است:

```text
[jadi@debian ~]$ cat /etc/resolv.conf
# Dynamic resolv.conf(5) file for glibc resolver(3) generated by resolvconf(8)
#     DO NOT EDIT THIS FILE BY HAND -- YOUR CHANGES WILL BE OVERWRITTEN
```

جای تعجب نیست که ما با گشت و گذار در WWW مشکل داشتیم. هیچ DNS فعالی در رایانه من وجود ندارد، بنابراین هیچ کس نمی تواند با نام دامنه خود به سایت ها دسترسی پیدا کند! این باید با افزودن یک DNS به فایل پیکربندی من برطرف شود.

#### مشکلات مسیریابی

در برخی شرایط نمی توانید به اینترنت دسترسی پیدا کنید \(مثلاً 4.2.2.4 یا 8.8.8.8\) اما می توانید دروازه خود را پینگ کنید. نگاهی بیندازید:

```text
[jadi@debian ~]$ ping 8.8.8.8
connect: Network is unreachable
[jadi@debian ~]$ ping 192.168.1.1
PING 192.168.1.1 (192.168.1.1) 56(84) bytes of data.
64 bytes from 192.168.1.1: icmp_seq=1 ttl=254 time=3.03 ms
64 bytes from 192.168.1.1: icmp_seq=2 ttl=254 time=3.31 ms
^C
--- 192.168.1.1 ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 1001ms
rtt min/avg/max/mdev = 3.039/3.174/3.310/0.146 ms
```

اینجا چه خبر است؟ بیایید ببینیم، چه سرنخ هایی دارم:
1) می توانم به دروازه برسم.
2) هنگام درخواست اینترنت، رایانه من نمی داند چه کاری انجام دهد.
در این مورد **درگاه پیش‌فرض** وجود ندارد: کامپیوتر نمی‌داند اگر بسته‌ای خارج از ماسک شبکه خود باشد، چه کاری انجام دهد. می‌دانید که می‌توانیم دروازه پیش‌فرض را با استفاده از فایل پیکربندی `/etc/network/interfaces` تنظیم کنیم، اما یک `route` (یا دستور فرعی جدیدتر `ip route`) برای نمایش و تغییر پیکربندی‌های مسیریابی در جریان وجود دارد.

> مسیرهایی که از طریق `ip route` (یا `route`) اضافه یا تغییر کرده اند، پس از راه اندازی مجدد از بین خواهند رفت! تنظیمات دائمی باید از فایل های پیکربندی باشد.

اجازه دهید وضعیت مسیریابی فعلی خود را با استفاده از دستور `route` به عنوان ریشه بررسی کنیم.

```text
jadi@debian:~$ ip route show
default via 192.168.70.1 dev enp0s1
172.17.0.0/16 dev docker0 proto kernel scope link src 172.17.0.1 linkdown
192.168.70.0/24 dev enp0s1 proto kernel scope link src 192.168.70.2

jadi@debian:~$ sudo ip route del default
[sudo] password for jadi:

jadi@debian:~$ ip route show
172.17.0.0/16 dev docker0 proto kernel scope link src 172.17.0.1 linkdown
192.168.70.0/24 dev enp0s1 proto kernel scope link src 192.168.70.2

jadi@debian:~$ ping 4.2.2.4
ping: connect: Network is unreachable

jadi@debian:~$ ip route add default via 192.168.70.1
RTNETLINK answers: Operation not permitted

jadi@debian:~$ sudo ip route add default via 192.168.70.1

jadi@debian:~$ ping 4.2.2.4
PING 4.2.2.4 (4.2.2.4) 56(84) bytes of data.
64 bytes from 4.2.2.4: icmp_seq=1 ttl=55 time=316 ms
64 bytes from 4.2.2.4: icmp_seq=2 ttl=55 time=434 ms
^C
--- 4.2.2.4 ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 1002ms
rtt min/avg/max/mdev = 316.253/375.282/434.311/59.029 ms
```

پس از افزودن یک دروازه پیش فرض با استفاده از دستور `ip route`، توانستیم اینترنت را پینگ کنیم. مهم است بدانید که می‌توانیم حتی مسیرهای بیشتری را تعریف کنیم و دقیقاً بر اساس مقصد بسته‌هایمان را کنترل کنیم.

#### Tracepath & Traceroute


این یک ابزار عیب یابی پیشرفته تر است. مثل این است که تمام سرورهای بین شما و مقصدتان را یکی یکی پینگ کنیم و ببینیم که بسته های ما کجا اشتباه می کنند. بیایید بررسی کنیم که چگونه به google.com دسترسی پیدا کنم.

```text
jadi@debian:~$ traceroute 4.2.2.4
traceroute to 4.2.2.4 (4.2.2.4), 30 hops max, 60 byte packets
 1  192.168.70.1 (192.168.70.1)  0.619 ms *  0.673 ms
 2  10.192.0.1 (10.192.0.1)  421.898 ms  728.657 ms  728.617 ms
 3  162.221.202.253 (162.221.202.253)  728.597 ms  728.564 ms  728.552 ms
 4  * * *
 5  207.35.48.241 (207.35.48.241)  728.289 ms  728.265 ms  728.251 ms
 6  agg2-vancouverbg_5-2-0.net.bell.ca (64.230.122.250)  728.344 ms agg1-vancouverbg_5-2-0.net.bell.ca (64.230.122.248)  612.097 ms  922.055 ms
 7  * * *
 8  bx6-seattle_et-0/0/13_ae1.net.bell.ca (64.230.76.157)  921.662 ms  921.635 ms  921.566 ms
 9  ae96.edge6.Seattle1.Level3.net (4.16.2.13)  921.511 ms  921.372 ms  921.317 ms
10  * * ae6.4.edge2.SanJose1.level3.net (4.69.220.185)  920.786 ms
11  d.resolvers.level3.net (4.2.2.4)  601.295 ms  921.003 ms  920.970 ms
```

در مرحله اول \(1\) به روتر خودم می رسم. در مرحله دوم، من در شبکه محلی ISP خود هستم و سپس به 162.blah.blah.blah خواهم رسید. مشاهده می کنید که در برخی موارد traceroute قادر به انجام **بازیابی معکوس DNS** بوده و نام میزبان IP ها را پیدا کرده و آنها را نشان می دهد. بعد از 11 پرش به مقصد رسیدم. Traceroute یک ابزار بسیار مفید در عیب یابی شبکه و مشکلات مسیریابی یا بررسی وضعیت شبکه و مسیرهای شما است. 

> در برخی از روترها، ترافیک پینگ مسدود شده است، و در برخی مراحل `* * *` را خواهید دید زیرا آن سرورها ترافیک ICMP را مسدود می کنند.

دستور دیگری به نام `tracepath` وجود دارد که بسیار شبیه به `traceroute` است. برای سطح LPIC1، آنها اساسا یکسان هستند!


#### ss و netstat

<iframe width="560" height="315" src="https://www.youtube.com/embed/AvVOHQdbZDA?si=WZzCqGbaEdUDFp88" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

این دستورات می توانند طیف وسیعی از اطلاعات را در مورد شبکه ما نشان دهند. `ss` جدیدتر است و `netstat` قدیمی تر است. این دو دستور در اکثر موارد قابل تعویض هستند و کارهای مشابهی را انجام می دهند و حتی در بیشتر موارد استفاده گزینه مشابهی دارند. می توانید از `netstat` برای بررسی جدول مسیریابی خود استفاده کنید:

```text
jadi@debian:~$ netstat -nr
Kernel IP routing table
Destination     Gateway         Genmask         Flags   MSS Window  irtt Iface
0.0.0.0         192.168.70.1    0.0.0.0         UG        0 0          0 enp0s1
172.17.0.0      0.0.0.0         255.255.0.0     U         0 0          0 docker0
192.168.70.0    0.0.0.0         255.255.255.0   U         0 0          0 enp0s1
```

یا از `ss` استفاده کنید تا ببینید کدام پورت در حالت LISTENING است:

```text
jadi@debian:~$ ss -na | grep LISTEN | grep tcp
tcp   LISTEN 0      128                                       127.0.0.1:631              0.0.0.0:*
tcp   LISTEN 0      100                                         0.0.0.0:25               0.0.0.0:*
tcp   LISTEN 0      128                                         0.0.0.0:22               0.0.0.0:*
tcp   LISTEN 0      100                                            [::]:25                  [::]:*
tcp   LISTEN 0      128                                            [::]:22                  [::]:*
tcp   LISTEN 0      128                                           [::1]:631                 [::]:*
```

سوئیچ `-na` همه پورت‌های باز (از جمله سوکت‌ها) را نشان می‌دهد و در اینجا من فقط پورت‌های tcp را در وضعیت LISTEN بررسی می‌کنم.

> در این سوئیچ ها، `-n` مخفف _numeric_، `-a` مخفف _all ports_ و `-r` مخفف _routes_ است.

یک ترکیب فوق العاده رایج مجموعه گزینه `-tulpn` است:

```
jadi@debian:~$ ss -tulpn
Netid             State              Recv-Q             Send-Q                         Local Address:Port                          Peer Address:Port            Process
udp               UNCONN             0                  0                                    0.0.0.0:68                                 0.0.0.0:*
udp               UNCONN             0                  0                                    0.0.0.0:631                                0.0.0.0:*
udp               UNCONN             0                  0                                    0.0.0.0:58120                              0.0.0.0:*
udp               UNCONN             0                  0                                    0.0.0.0:5353                               0.0.0.0:*
udp               UNCONN             0                  0                                       [::]:39822                                 [::]:*
udp               UNCONN             0                  0                                       [::]:5353                                  [::]:*
tcp               LISTEN             0                  128                                127.0.0.1:631                                0.0.0.0:*
tcp               LISTEN             0                  100                                  0.0.0.0:25                                 0.0.0.0:*
tcp               LISTEN             0                  128                                  0.0.0.0:22                                 0.0.0.0:*
tcp               LISTEN             0                  100                                     [::]:25                                    [::]:*
tcp               LISTEN             0                  128                                     [::]:22                                    [::]:*
tcp               LISTEN             0                  128                                    [::1]:631                                   [::]:*
```

#### نت کت

ابزار . می تواند اتصالات TCP را باز کند، بسته های UDP ارسال کند، به پورت های دلخواه TCP و UDP گوش دهد، اسکن پورت را انجام دهد و با هر دو IPv4 و IPv6 سروکار داشته باشد. برخلاف `telnet`، `nc` را می‌توان به راحتی در اسکریپت‌ها استفاده کرد و پیام‌های خطا را به جای ارسال آن‌ها به خروجی استاندارد (Standard Output - stdout)، مانند telnet، به خطای استاندارد (Standard Error - stderr) جدا می‌کند. این دستور بسیار توانا است و کافی است با مفهوم کلی آن آشنا شوید.

در اینجا من یک شنونده tcp در پورت 1337 ایجاد می کنم:

```
jadi@debian:~$ nc -l 1337
```

و در اینجا من یک اتصال به آن پورت را باز می کنم و مقداری داده را ارسال می کنم:

```
jadi@debian:~$ nc localhost 1337
Are you enjoying the LPIC?
```

و پیام باید در گوش دادن `nc` قابل مشاهده باشد. 

#### حفاری

دستور `dig` یک ابزار جستجوی DNS است. اگر با نام دامنه مشکل دارید، می توانید بررسی کنید که چگونه آن را به IP ها حل می کنند. و توسط چه کسی

```text
[jadi@debian ~]$ dig google.com

; <<>> DiG 9.9.5-11ubuntu1.3-Ubuntu <<>> google.com
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 50032
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 0

;; QUESTION SECTION:
;google.com.            IN    A

;; ANSWER SECTION:
google.com.        293    IN    A    216.58.214.46

;; Query time: 120 msec
;; SERVER: 4.2.2.4#53(4.2.2.4)
;; WHEN: Fri Apr 01 22:00:05 IRDT 2016
;; MSG SIZE  rcvd: 44
```

می بینید که SERVER 4.2.2.4 google.com را به 216.58.214.46 تغییر می دهد.