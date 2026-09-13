Title: 108.1 زمان سیستم را حفظ کنید
Date: 2010-12-03 10:20
Category: LPIC1
Tags: LPIC1, 102, LPIC1-102-500
Authors: Jadi
sortorder: 360
Summary: 

_وزن: 3_

داوطلبان باید بتوانند به درستی زمان سیستم را حفظ کرده و ساعت را از طریق NTP همگام کنند.

### حوزه های دانش کلیدی

* تاریخ و زمان سیستم را تنظیم کنید.
* ساعت سخت افزاری را روی زمان صحیح در UTC تنظیم کنید.
* منطقه زمانی صحیح را پیکربندی کنید.
* پیکربندی اصلی NTP با استفاده از `ntpd` و `chrony`.
* دانش استفاده از سرویس `pool.ntp.org`.
* آگاهی از دستور `ntpq`.

### شرایط و امکانات

* `/usr/share/zoneinfo/`
* `/etc/timezone`
* `/etc/localtime`
* `/etc/ntp.conf`
* `/etc/chrony.conf`
* `date`
* `hwclock`
* `ntpd`
* `ntpdate`
* `chronyc`
* `pool.ntp.org`

<iframe width="560" height="315" src="https://www.youtube.com/embed/RhH-2I1dBjA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

### چگونه یک کامپیوتر زمان خود را نگه می دارد

یک ساعت در رایانه شما وجود دارد. یک ساعت سخت افزاری روی مادربرد شما! باتری مخصوص به خود را دارد و حتی زمانی که کامپیوتر خاموش است زمان را حفظ می کند. هنگامی که سیستم بوت می شود، سیستم عامل این **زمان سخت افزاری** را می خواند و **زمان سیستم** خود را بر اساس ساعت سخت افزاری تنظیم می کند و هر زمان که نیاز به دانستن زمان داشته باشد از این ساعت استفاده می کند.

ساعت سخت افزاری می تواند در زمان محلی (زمانی که در ساعت شما در هر کجا که هستید نشان داده می شود) یا زمان UTC (زمان استاندارد) تنظیم شود. `hwclock` را می توان برای نشان دادن زمان بر اساس hwtime استفاده کرد. ببینید بر اساس زمان سخت افزاری چگونه کار می کند حتی بعد از اینکه زمان سیستم را تغییر دادیم:

```
$ date
Fri Jun 23 01:47:22 PM +0330 2023
$ sudo date -s "Jan 22 22:22:22 2022"
Sat Jan 22 10:22:22 PM +0330 2022
$ date
Sat Jan 22 10:22:29 PM +0330 2022
$ sudo hwclock 
2023-06-23 13:47:41.160122+03:30
```

> حتی زمانی که ساعت سخت افزاری روی UTC تنظیم شده است، تاریخ `hwclock` تاریخ را در زمان محلی \(زمان پس از افزودن منطقه زمانی به زمان UTC\) نشان می دهد.

سیستم عامل های قدیمی برای تنظیم ساعت سخت افزاری در منطقه زمانی محلی به جای منطقه زمانی استفاده می شدند. این را می توان با:

```text
# hwclock --localtime --set --date="01/05/2023 22:04:00"
```

دستورات قبلی ساعت سخت افزاری را در آن تاریخ مشخص تنظیم می کند و به آن می گوید که این زمان محلی است. اگر می‌خواهید به زمان UTC برگردید، مسئله:

```text
# hwclock -u -w
```

در اینجا، `-w` به `hwclock` می گوید که زمان سخت افزار را بر اساس زمان فعلی سیستم تنظیم کند و `-u` به ساعت hwclock می گوید که ما از UTC استفاده می کنیم. این همچنین HWClock را با استفاده از UTC در فایل `\etc\adjtime` تنظیم می کند.

> اگر زمانی را روی ساعت سخت افزاری تنظیم کنید بدون اینکه UTC / Local بودن آن را ذکر کنید، `/etc/adjtime` در این مورد تصمیم می گیرد، اگر این فایل وجود نداشته باشد، از UTC استفاده می شود.

شما قبلاً درباره `timedatectl` و `date` از [فصل محلی‌سازی و جهانی‌سازی] (http://linux1st.com/1073-localisation-and-internationalisation.html) می‌دانید، بنابراین من آنها را در اینجا تکرار نمی‌کنم.


### مناطق زمانی
ما مناطق زمانی را در فصل های قبلی دیده ایم. اما به طور خلاصه دو فایل مهم در اینجا وجود دارد.

`/etc/timezone` یک فایل متنی است که منطقه زمانی شما را نشان می دهد. اگر برنامه ای بخواهد در مورد منطقه زمانی نمایش شما بداند از این مورد استفاده می شود. به عنوان مثال:

```
$ cat /etc/timezone 
Asia/Tehran
```

اما `/etc/localtime` یک فایل باینری است که اطلاعات منطقه زمانی شما را برای سیستم توصیف می کند (به عنوان مثال فایل `date`):

```
$ ls -l /etc/localtime 
lrwxrwxrwx 1 root root 31 Jun 22 11:19 /etc/localtime -> /usr/share/zoneinfo/Asia/Tehran
$ file /usr/share/zoneinfo/Asia/Tehran
/usr/share/zoneinfo/Asia/Tehran: timezone data, version 2, no gmt time flags, no std time flags, no leap seconds, 72 transition times, 8 abbreviation chars
```

در بسیاری از موارد، این یک پیوند نرم به فایلی است که در `/usr/share/zoneinfo/` قرار دارد، بنابراین در صورت به‌روزرسانی سیستم، به‌روزرسانی می‌شود.

### NTP

<iframe width="560" height="315" src="https://www.youtube.com/embed/ntyUBmG8F40" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

**پروتکل زمان شبکه** پروتکل مورد علاقه شخصی من است. اگر به جزئیات آن بپردازید، یکی از جالب ترین پروتکل های تاریخ است. اما متاسفانه برای LPIC1 شما نیازی به شیرجه رفتن در اعماق NTP ندارید. این پروتکل از سرورهای NTP برای پیدا کردن زمان دقیق نشان داده شده توسط بهترین ساعت های اتمی در این سیاره استفاده می کند. یکی از معروف ترین سرورهایی که توسط افراد ntp استفاده می شود `pool.ntp.org` است. اگر آن وب سایت را بررسی کنید، خواهید دید که آن یک **پول** از سرورهای ntp است و با دادن `pool.ntp.org` به سرور NTP خود، به یکی از سرورهای ntp متعدد موجود در آن استخر هدایت می شود.

#### ntpdate

مستقیم ترین دستور برای تنظیم ساعت سیستم `ntpdate` است و به این صورت استفاده می شود:

```
$ sudo ntpdate pool.ntp.org
23 Jun 14:49:55 ntpdate[160138]: adjust time server 31.214.170.254 offset +0.020196 sec
```

پس از این، باید ساعت hwclock را با استفاده از `sudo hwclock -w` روی زمان سیستمی که اخیراً همگام‌سازی شده است، تنظیم کنیم.

#### ntpd

به جای اینکه هر بار زمان را به صورت دستی تنظیم کنید، می توانید از یک سرویس لینوکس به نام `ntp` استفاده کنید تا زمان خود را با استفاده از برخی سرورهای زمان نگه دارید \(معروف ترین آنها pool.ntp.org\ است. `ntp` را نصب کنید و سرور را راه اندازی کنید:

در دبیان/اوبونتو: 

```
# apt install ntp
# systemctl start ntp
```

واقعیت سرگرم کننده؟ شما نمی توانید از هر دو استفاده کنید! به این نگاه کن:

```text
root@funlife:~# ntpdate pool.ntp.org
23 Jun 14:49:55 ntpdate[18670]: the NTP socket is in use, exiting
```

همانطور که می بینید، اکنون `ntp` از درگاه NTP استفاده می کند و `ntpdate` در راه اندازی مشکل دارد.

فایل پیکربندی اصلی `ntp` در `/etc/ntp.conf` قرار دارد:

```text
# cat /etc/ntp.conf
# /etc/ntp.conf, configuration for ntpd; see ntp.conf(5) for help

driftfile /var/lib/ntp/ntp.drift

# Enable this if you want statistics to be logged.
#statsdir /var/log/ntpstats/

statistics loopstats peerstats clockstats
filegen loopstats file loopstats type day enable
filegen peerstats file peerstats type day enable
filegen clockstats file clockstats type day enable


# You do need to talk to an NTP server or two (or three).
#server ntp.your-provider.example

# pool.ntp.org maps to about 1000 low-stratum NTP servers.  Your server will
# pick a different set every time it starts up.  Please consider joining the
# pool: <http://www.pool.ntp.org/join.html>
pool 0.debian.pool.ntp.org iburst
pool 1.debian.pool.ntp.org iburst
pool 2.debian.pool.ntp.org iburst
pool 3.debian.pool.ntp.org iburst


# Access control configuration; see /usr/share/doc/ntp-doc/html/accopt.html for
# details.  The web page <http://support.ntp.org/bin/view/Support/AccessRestrictions>
# might also be helpful.
#
# Note that "restrict" applies to both servers and clients, so a configuration
# that might be intended to block requests from certain clients could also end
# up blocking replies from your own upstream servers.

# By default, exchange time with everybody, but don't allow configuration.
restrict -4 default kod notrap nomodify nopeer noquery limited
restrict -6 default kod notrap nomodify nopeer noquery limited

# Local users may interrogate the ntp server more closely.
restrict 127.0.0.1
restrict ::1

# Needed for adding pool entries
restrict source notrap nomodify noquery

# Clients from this (example!) subnet have unlimited access, but only if
# cryptographically authenticated.
#restrict 192.168.123.0 mask 255.255.255.0 notrust


# If you want to provide time to your local subnet, change the next line.
# (Again, the address is an example only.)
#broadcast 192.168.123.255

# If you want to listen to time broadcasts on your local subnet, de-comment the
# next lines.  Please do this only if you trust everybody on the network!
#disable auth
#broadcastclient
```

در صورت نیاز، می توانید سرورهای ntp را به سرورهایی که می خواهید استفاده کنید تغییر دهید.

پیکربندی را مرور کنید و چیزهای جالبی مانند ارائه سرویس ntp خود به رایانه های دیگر خواهید دید، اگرچه برای عبور LPIC به آنها نیاز ندارید.

#### ntpq

`ntpq` سرویس ntp را پرس و جو می کند. یکی از سوئیچ های معروف `-p` \(برای چاپ\) است که استخری را که ما برای همگام سازی ساعت استفاده می کنیم نشان می دهد:

```text
 ntpq -p
     remote           refid      st t when poll reach   delay   offset  jitter
==============================================================================
 0.debian.pool.n .POOL.          16 p    -   64    0    0.000    0.000   0.000
 1.debian.pool.n .POOL.          16 p    -   64    0    0.000    0.000   0.000
 2.debian.pool.n .POOL.          16 p    -   64    0    0.000    0.000   0.000
 3.debian.pool.n .POOL.          16 p    -   64    0    0.000    0.000   0.000
+46.209.14.1     192.168.5.2      4 u    7   64    1   58.300  -15.546  14.519
-ntp.tums.ac.ir  195.161.115.4    4 u    4   64    1   30.636    2.485   4.025
*194.225.150.25  194.190.168.1    2 u    5   64    1   31.478   -3.870  95.635
+5.160.24.41     192.168.5.2      4 u    3   64    1   90.000  -28.328  21.643
```

در این خروجی یک `*` به این معنی است که ntp از این سرور به عنوان مرجع اصلی استفاده می کند، `+` به این معنی است که این سرور خوبی است و `-` یک سرور خارج از محدوده را نشان می دهد که نادیده گرفته می شود.

### کرونی
پروتکل NTP دیگر و جدیدتر، `chrony` است. در مقایسه با `ntpd`، این ابزار نتایج بهتری را در همگام سازی شرایط دشوار مانند اتصالات شبکه متناوب (مانند لپ تاپ) و شبکه های متراکم ارائه می دهد. Chrony کلاینت پیش‌فرض NTP در RedHat 8، SUSE 15 و بسیاری از توزیع‌های دیگر است. آداون دیگه


این یک نمونه فایل `chrony.conf` است:

```
$ cat /etc/chrony/chrony.conf 
# Welcome to the chrony configuration file. See chrony.conf(5) for more
# information about usable directives.

# Include configuration files found in /etc/chrony/conf.d.
confdir /etc/chrony/conf.d

# This will use (up to):
# - 4 sources from ntp.ubuntu.com which some are ipv6 enabled
# - 2 sources from 2.ubuntu.pool.ntp.org which is ipv6 enabled as well
# - 1 source from [01].ubuntu.pool.ntp.org each (ipv4 only atm)
# This means by default, up to 6 dual-stack and up to 2 additional IPv4-only
# sources will be used.
# At the same time it retains some protection against one of the entries being
# down (compare to just using one of the lines). See (LP: #1754358) for the
# discussion.
#
# About using servers from the NTP Pool Project in general see (LP: #104525).
# Approved by Ubuntu Technical Board on 2011-02-08.
# See http://www.pool.ntp.org/join.html for more information.
pool ntp.ubuntu.com        iburst maxsources 4
pool 0.ubuntu.pool.ntp.org iburst maxsources 1
pool 1.ubuntu.pool.ntp.org iburst maxsources 1
pool 2.ubuntu.pool.ntp.org iburst maxsources 2

# Use time sources from DHCP.
sourcedir /run/chrony-dhcp

# Use NTP sources found in /etc/chrony/sources.d.
sourcedir /etc/chrony/sources.d

# This directive specify the location of the file containing ID/key pairs for
# NTP authentication.
keyfile /etc/chrony/chrony.keys

# This directive specify the file into which chronyd will store the rate
# information.
driftfile /var/lib/chrony/chrony.drift

# Save NTS keys and cookies.
ntsdumpdir /var/lib/chrony

# Uncomment the following line to turn logging on.
#log tracking measurements statistics

# Log files location.
logdir /var/log/chrony

# Stop bad estimates upsetting machine clock.
maxupdateskew 100.0

# This directive enables kernel synchronization (every 11 minutes) of the
# real-time clock. Note that it can’t be used along with the 'rtcfile' directive.
rtcsync

# Step the system clock instead of slewing it if the adjustment is larger than
# one second, but only in the first three clock updates.
makestep 1 3

# Get TAI-UTC offset and leap seconds from the system tz database.
# This directive must be commented out when using time sources serving
# leap-smeared time.
leapsectz right/UTC
```

برای کنترل سرویس `chrony`، یک CLI (واسط خط فرمان (Command Line)) وجود دارد که `chronyc` نامیده می شود. از آن برای نظارت بر عملکرد chronyd و تغییر پارامترهای عملیاتی مختلف استفاده می شود. اگر یک "فرمان" به `chronyc` ارسال شود، نتایج نشان داده می شود، در غیر این صورت دستوری برای صدور دستورات خود دریافت خواهید کرد. نگاهی بیندازید:

```
$ chronyc tracking
Reference ID    : 0FED61D6 (paris.time.system76.com)
Stratum         : 3
Ref time (UTC)  : Fri Jun 23 12:44:20 2023
System time     : 0.001574947 seconds slow of NTP time
Last offset     : +0.000513619 seconds
RMS offset      : 0.065126784 seconds
Frequency       : 8.705 ppm slow
Residual freq   : +0.278 ppm
Skew            : 14.972 ppm
Root delay      : 0.180896595 seconds
Root dispersion : 0.013603540 seconds
Update interval : 128.6 seconds
Leap status     : Normal
$ chronyc
chrony version 4.2
Copyright (C) 1997-2003, 2007, 2009-2021 Richard P. Curnow and others
chrony comes with ABSOLUTELY NO WARRANTY.  This is free software, and
you are welcome to redistribute it under certain conditions.  See the
GNU General Public License version 2 for details.

chronyc> activity
200 OK
12 sources online
0 sources offline
0 sources doing burst (return to online)
0 sources doing burst (return to offline)
3 sources with unknown address

chronyc> sources
MS Name/IP address         Stratum Poll Reach LastRx Last sample               
===============================================================================
^? prod-ntp-4.ntp4.ps5.cano>     2   7   375    20  +5039us[+5039us] +/-   85ms
^? prod-ntp-5.ntp4.ps5.cano>     2   7   377    83    +12ms[  +15ms] +/-   87ms
^? prod-ntp-3.ntp4.ps5.cano>     2   7   177    22    +13ms[  +17ms] +/-   91ms
^? alphyn.canonical.com          2   7   277    22  +3298us[+6616us] +/-  185ms
^? mail.stumpflee.com            2   7   373    19  +6221us[+6221us] +/-  117ms
^? meetbsd.ir                    2   6   377    27    -23ms[  -20ms] +/-  231ms
^? 188.121.119.122               3   7   377    26    -27ms[  -23ms] +/-  131ms
^+ brazil.time.system76.com      2   7   377    20    -13ms[  -13ms] +/-  190ms
^+ ohio.time.system76.com        2   7   377    21    +23ms[  +23ms] +/-  171ms
^+ oregon.time.system76.com      2   7   377    23    +22ms[  +26ms] +/-  217ms
^* paris.time.system76.com       2   7   377    24  -4880us[-1560us] +/-  109ms
^+ virginia.time.system76.c>     2   7   163    19  +5465us[+5465us] +/-  148ms

chronyc> exit
$ sudo chronyc makestep
200 OK

```

`chrnoyc` با استفاده از سوکت های TCP یا Unix به سرویس chrony متصل می شود. بنابراین، می‌توان از یک `chronyc` محلی برای اتصال به `chrony` از راه دور و صدور فرمان‌ها استفاده کرد، اگرچه در این مورد به دلایل امنیتی عمدتاً به نظارت بر دستورات محدود می‌شوید.