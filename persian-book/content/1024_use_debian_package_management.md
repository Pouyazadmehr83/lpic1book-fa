Title: 102.4 از مدیریت بسته دبیان استفاده کنید
Date: 2010-12-03 10:20
Category: LPIC1
Tags: LPIC1, 101, LPIC1-101-500
Authors: Jadi
Summary: کاندیداها باید بتوانند مدیریت بسته را با استفاده از ابزارهای بسته دبیان انجام دهند.
sortorder: 090

_وزن: 3_

کاندیداها باید بتوانند مدیریت بسته را با استفاده از ابزارهای بسته دبیان انجام دهند.

* بسته های باینری دبیان را نصب، ارتقا و حذف نصب کنید.
* بسته های حاوی فایل ها یا کتابخانه های خاصی را پیدا کنید که ممکن است نصب شوند یا نباشند.
* اطلاعات بسته مانند نسخه، محتوا، وابستگی ها، یکپارچگی بسته، و وضعیت نصب \(چه بسته نصب شده باشد یا نه\) را دریافت کنید.
* آگاهی از apt.

## شرایط و امکانات

* `/etc/apt/sources.list`
* dpkg
* dpkg-تنظیم مجدد
* apt-get
* apt-cache

## مفهوم سیستم مدیریت بسته

<iframe width="560" height="315" src="https://www.youtube.com/embed/jtwbweigRxo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

برخی از مردم فکر می کنند که در گنو/لینوکس باید تمام نرم افزارهای مورد نیاز خود را به صورت دستی کامپایل کنیم. در 99 درصد موارد اینطور نیست و در 20 سال گذشته هرگز چنین نبوده است. گنو/لینوکس سلف چیزی است که ما این روزها اپ استور می نامیم. همه توزیع‌های بزرگ دارای آرشیوهای عظیمی از نرم‌افزارهای از پیش کامپایل‌شده به نام مخازن نرم‌افزاری (Repositories) خود هستند و نوعی نرم‌افزار **مدیر بسته‌ها (Package Manager)** است که وظیفه جستجوی این مخازن نرم‌افزاری (Repositories)، نصب نرم‌افزار از آنها، یافتن وابستگی‌ها، نصب آنها، رفع تضادها، و به روز رسانی سیستم و نرم‌افزار نصب شده را بر عهده دارد. توزیع‌های مبتنی بر دبیان از فایل‌های `.deb` به‌عنوان «بسته» استفاده می‌کنند و از ابزارهایی مانند `apt-get`، `dpkg`، `apt`، و ابزارهای دیگر برای مدیریت آن‌ها استفاده می‌کنند.

بسته های دبیان نام هایی مانند `NAME_VERSION-RELEASE_ARCHITECTURE.deb` هستند. بگویید `tmux_3.2a-4build1_amd64.deb`. 



## مخازن نرم‌افزاری (Repositories)
اما این بسته از کجا آمده است؟ چگونه سیستم عامل می‌داند که این بسته deb را کجا جستجو کند؟ پاسخ ** مخازن نرم‌افزاری (Repositories) ** است. هر توزیع دارای مخزن بسته های خود است. این می تواند روی یک دیسک، یک درایو شبکه، مجموعه ای از دی وی دی ها، یا معمولاً یک آدرس شبکه در اینترنت باشد. 

در سیستم‌های دبیان، مکان‌های اصلی پیکربندی عبارتند از:
* `/etc/apt/sources.list`
* `/etc/apt/sources.list.d/`

```text
jadi@lpicjadi:~$ cat /etc/apt/sources.list
#deb cdrom:[Ubuntu 22.04 LTS _Jammy Jellyfish_ - Beta amd64 (20220329.1)]/ jammy main restricted

# See http://help.ubuntu.com/community/UpgradeNotes for how to upgrade to
# newer versions of the distribution.
deb http://us.archive.ubuntu.com/ubuntu/ jammy main restricted
# deb-src http://us.archive.ubuntu.com/ubuntu/ jammy main restricted

## Major bug fix updates produced after the final release of the
## distribution.
deb http://us.archive.ubuntu.com/ubuntu/ jammy-updates main restricted
# deb-src http://us.archive.ubuntu.com/ubuntu/ jammy-updates main restricted

## N.B. software from this repository is ENTIRELY UNSUPPORTED by the Ubuntu
## team. Also, please note that software in the universe WILL NOT receive any
## review or updates from the Ubuntu security team.
deb http://us.archive.ubuntu.com/ubuntu/ jammy universe
# deb-src http://us.archive.ubuntu.com/ubuntu/ jammy universe
deb http://us.archive.ubuntu.com/ubuntu/ jammy-updates universe
# deb-src http://us.archive.ubuntu.com/ubuntu/ jammy-updates universe

## N.B. software from this repository is ENTIRELY UNSUPPORTED by the Ubuntu
## team, and may not be under a free license. Please satisfy yourself as to
## your rights to use the software. Also, please note that the software in
## multiverse WILL NOT receive any review or updates from the Ubuntu
## security team.
deb http://us.archive.ubuntu.com/ubuntu/ jammy multiverse
# deb-src http://us.archive.ubuntu.com/ubuntu/ jammy multiverse
deb http://us.archive.ubuntu.com/ubuntu/ jammy-updates multiverse
# deb-src http://us.archive.ubuntu.com/ubuntu/ jammy-updates multiverse

## N.B. software from this repository may not have been tested as
## extensively as that contained in the main release, although it includes
## newer versions of some applications which may provide useful features.
## Also, please note that software in backports WILL NOT receive any review
## or updates from the Ubuntu security team.
deb http://us.archive.ubuntu.com/ubuntu/ jammy-backports main restricted universe multiverse
# deb-src http://us.archive.ubuntu.com/ubuntu/ jammy-backports main restricted universe multiverse

deb http://security.ubuntu.com/ubuntu jammy-security main restricted
# deb-src http://security.ubuntu.com/ubuntu jammy-security main restricted
deb http://security.ubuntu.com/ubuntu jammy-security universe
# deb-src http://security.ubuntu.com/ubuntu jammy-security universe
deb http://security.ubuntu.com/ubuntu jammy-security multiverse
# deb-src http://security.ubuntu.com/ubuntu jammy-security multiverse

# This system was installed using small removable media
# (e.g. netinst, live or single CD). The matching "deb cdrom"
# entries were disabled at the end of the installation process.
# For information about how to configure apt package sources,
# see the sources.list(5) manual.
```

به روز رسانی اطلاعات منابع:

```text
apt-get update
```
با این کار تمام منابع موجود در تنظیمات بررسی می شود و اطلاعات مربوط به آخرین نرم افزار موجود در آنجا به روز می شود.

> این در واقع نرم افزار را ارتقا نمی دهد. *به روز رسانی* فقط *اطلاعات بسته ها را به روز می کند و نه خود بسته ها*.

## نصب پکیج

<iframe width="560" height="315" src="https://www.youtube.com/embed/IBnxIX_WceI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

بگویید درباره این مالتی پلکسر ترمینال شگفت انگیز به نام `tmux` شنیده اید و می خواهید آن را امتحان کنید.

```text
$ tmux
The program 'tmux' is currently not installed. You can install it by typing:
sudo apt-get install tmux
$ which tmux
$ type tmux
bash: type: tmux: not found
```

پس بیایید آن را نصب کنیم. اگر در مخازن نرم‌افزاری (Repositories) است، کافی است به مدیر بسته‌ها (Package Manager) بگویید آن را نصب کند:

```text
apt-get install tmux
```

توجه داشته باشید که

* نصب apt-get برای تأیید درخواست شد \(Y\)
* apt-get _dependencies_ را حل کرد، می داند برای نصب این بسته چه چیزی لازم است و آنها را نصب می کند
* بسته های دبیان چیزی هستند.deb

اگر فقط می‌خواهید یک اجرا/شبیه‌سازی خشک انجام دهید:

```text
apt-get install -s tmux
```

و این فقط فایل های مورد نیاز را بدون نصب در کش دانلود می کند:

```text
apt-get install --download-only tmux
```

بسته های دانلود شده به عنوان حافظه کش (Cache) در `/var/cache/apt/archive/` ذخیره می شوند.

اگر می خواهید فقط یک بسته خاص را دانلود کنید، می توانید انجام دهید:

```
apt-get download tmux
```
## حذف بسته های دبیان

```text
apt-get remove tmux
```

و اگر می خواهید وابستگی های نصب شده به طور خودکار را حذف کنید:

```text
$ apt-get autoremove tmux
```

یا حتی

```text
$ apt-get autoremove
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following packages will be REMOVED:
  linux-image-3.16.0-25-generic linux-image-extra-3.16.0-25-generic
0 upgraded, 0 newly installed, 2 to remove, and 0 not upgraded.
After this operation, 203 MB of disk space will be freed.
Do you want to continue? [Y/n] y
```

برای حذف خودکار هر چیزی که دیگر مورد نیاز نیست.

یادداشت ها:

* حذف یک بسته، وابستگی های آن را حذف نمی کند
* در صورت حذف یک وابستگی، هشداری در مورد مواردی که در کنار این بسته حذف خواهند شد دریافت خواهید کرد

## جستجو برای بسته ها
اگر از لباس مناسب استفاده می کنید، جستجو از طریق `apt-cache` انجام می شود یا می توانید از `apt` عمومی استفاده کنید. 

```text
$ apt-cache search "tiny window"
$ apt search grub2
```

## ارتقاء

برای به روز رسانی یک بسته واحد:

```text
apt-get install tzdata
```

و برای ارتقای هر آنچه که نصب شده است:

```text
apt-get upgrade
```

یا رفتن به توزیع جدید:

```text
apt-get dist-upgrade
```

توجه: مانند اکثر ابزارهای دیگر، می توانید تنظیمات پیش فرض را در `/etc/apt/apt.conf` پیکربندی کنید و یک برنامه apt-config برای این منظور وجود دارد.

## پیکربندی مجدد بسته ها

بسته‌های دبیان می‌توانند دارای اقدامات پیکربندی باشند که پس از نصب بسته انجام می‌شوند. این کار توسط `debconf` انجام می شود. به عنوان مثال، tzdata پس از نصب از شما در مورد تنظیمات منطقه زمانی سوال خواهد کرد. اگر می‌خواهید بسته‌ای را که قبلاً نصب شده است * پیکربندی مجدد* کنید، می‌توانید از `dpkg-reconfigure` استفاده کنید:

```text
 dpkg-reconfigure tzdata
```

## اطلاعات بسته با dpkg

ابزار اساسی برای کار با فایل های `.deb` `dpkg` است. اگر می‌خواهید اقدامات دستی روی یک بسته deb انجام دهید، این ابزار برای رفتن شماست. قالب کلی این است:

```
dpkg [OPTIONS] ACTION PACKAGE
```

برخی از اقدامات رایج عبارتند از:

|سوئیچ|توضیحات|
|-|-|
|-c یا --contents| نمایش محتویات یک بسته|
|-C یا --audit| جستجو برای بسته های نصب شده خراب و پیشنهاد راه حل |
|--پیکربندی| پیکربندی مجدد بسته نصب شده|
|-i یا --install| یک بسته را نصب یا ارتقا دهید. وابستگی ها را حل / نصب نمی کند|
|-I یا --info| نمایش اطلاعات|
|-l یا --list| لیست تمام بسته های نصب شده|
|-L یا --listfiles | لیست تمام فایل های مربوط به این بسته|
|-P یا --purge| بسته و فایل های پیکربندی آن را حذف کنید|
|-r یا --remove| بسته را بردارید؛ تنظیمات را حفظ کنید|
|-s یا --status| نمایش وضعیت یک بسته|
|-S یا --search| جستجو کنید و ببینید کدام بسته مالک این فایل است|

می توانید مطالب را بررسی کنید:

```
jadi@lpicjadi:/tmp$ dpkg --contents bzr_2.7.0+bzr6622+brz_all.deb
drwxr-xr-x root/root         0 2019-09-19 18:25 ./
drwxr-xr-x root/root         0 2019-09-19 18:25 ./usr/
drwxr-xr-x root/root         0 2019-09-19 18:25 ./usr/share/
drwxr-xr-x root/root         0 2019-09-19 18:25 ./usr/share/doc/
drwxr-xr-x root/root         0 2019-09-19 18:25 ./usr/share/doc/bzr/
-rw-r--r-- root/root       404 2019-09-19 18:25 ./usr/share/doc/bzr/NEWS.Debian.gz
-rw-r--r-- root/root      1301 2019-09-19 18:25 ./usr/share/doc/bzr/changelog.gz
-rw-r--r-- root/root      1769 2019-09-19 18:25 ./usr/share/doc/bzr/copyright
```

یا یک بسته deb (بدون وابستگی های آن) را نصب کنید یا وضعیت آن را بررسی کنید:

```text
$ dpkg -s bzr
Package: bzr
Status: deinstall ok config-files
Priority: optional
Section: vcs
Installed-Size: 102
Maintainer: Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com>
Architecture: all
Version: 2.6.0+bzr6595-1ubuntu1
Config-Version: 2.6.0+bzr6595-1ubuntu1
Depends: python-bzrlib (<= 2.6.0+bzr6595-1ubuntu1.1~), python-bzrlib (>= 2.6.0+bzr6595-1ubuntu1), python:any
Recommends: python-gpgme
Suggests: bzr-doc, bzrtools, python-bzrlib.tests
Breaks: bzr-pqm (<< 1.4.0~bzr80), bzr-xmloutput (<< 0.8.8+bzr160), python-bzrlib (<< 2.4.0~beta3~)
Conffiles:
 /etc/bash_completion.d/bzr b8d9ca95521a7c5f14860e205a854da2
Description: easy to use distributed version control system
 Bazaar is a distributed version control system designed to be easy to
 use and intuitive, able to adapt to many workflows, reliable, and
 easily extendable.
 .
 Publishing of branches can be done over plain HTTP, that is, no special
 software is needed on the server to host Bazaar branches. Branches can
 be pushed to the server via sftp (which most SSH installations come
 with), FTP, or over a custom and faster protocol if bzr is installed in
 the remote end.
 .
 Merging in Bazaar is easy, as the implementation can avoid many
 spurious conflicts deals well with repeated merges between branches,
 and can handle modifications to renamed files correctly.
 .
 Bazaar is written in Python and has a flexible plugin interface that
 can be used to extend its functionality. Many plugins exist, providing
 useful commands (bzrtools), graphical interfaces (qbzr), or native
 interaction with Subversion branches (bzr-svn).
 .
 Install python-paramiko if you are going to push branches to remote
 hosts with sftp, and python-pycurl if you'd like SSL certificates
 always to be verified.
Homepage: http://bazaar-vcs.org
Original-Maintainer: Debian Bazaar Maintainers <pkg-bazaar-maint@lists.alioth.debian.org>
```
یا حتی **پاکسازی** یک بسته نصب شده. حذف بسته و تمام تنظیمات آن. برای پاکسازی بسته، از کلید **-P** یا **--purge** استفاده کنید.

همچنین **-L** برای بررسی فایل ها و دایرکتوری (پوشه) های بسته نصب شده وجود دارد:

```text
$ dpkg -L bzr
/.
/usr
/usr/bin
/usr/bin/jcal
/usr/share
/usr/share/doc
/usr/share/doc/jcal
/usr/share/doc/jcal/README
/usr/share/doc/jcal/copyright
/usr/share/man
/usr/share/man/man1
/usr/share/man/man1/jcal.1.gz
/usr/share/doc/jcal/changelog.Debian.gz
```

و **-S** نشان می دهد که کدام بسته فایل داده شده را نصب کرده است:

```text
$ dpkg -S /var/lib/mplayer/prefs/mirrors
mplayer: /var/lib/mplayer/prefs/mirrors
```


## گزینه های متداول apt-get
|گزینه|استفاده|
|-|-|
|autoclean|بسته های استفاده نشده را حذف می کند|
|بررسی|دسی بل را برای مشکلات بررسی کنید|
|clean|DB را تمیز کنید، می توانید یک `clean all` انجام دهید تا همه چیز را تمیز کنید و از نو شروع کنید|
|dist-upgrade|نسخه های جدید سیستم عامل را بررسی می کند. ارتقاء اساسی|
|نصب|نصب یا ارتقاء بسته ها|
|remove|یک بسته را حذف می کند|
|source|سورس یک بسته را نصب کنید|
|update|اطلاعات مربوط به بسته ها را از مخازن نرم‌افزاری (Repositories) به روز می کند|
| ارتقا|تمام بسته ها را ارتقا می دهد|

> در برخی موارد یک بسته نصب شده است اما بدون وابستگی مناسب (مثلاً با استفاده از `dpkg`) یا نصب به هر دلیلی قطع می شود. در این موارد ممکن است یک `apt-get install -f` کمک کند، `-f` برای `fix broken` است. 
## گزینه های رایج apt-cache

|گزینه|استفاده|
|-|-|
|وابستگی|نمایش وابستگی|
|pkgnames|همه بسته های نصب شده را نشان می دهد|
|جستجو|جستجو|
|showpkg|نمایش اطلاعات مربوط به یک بسته|
|stats|نمایش آمار|
|unmet|نمایش وابستگی‌های برآورده نشده برای همه بسته‌های نصب‌شده یا بسته‌هایی که مشخص کرده‌اید|


## ابزارهای دیگر
ابزارهای بیشتری نیز وجود دارد، ابزارهایی با رابط کاربری گرافیکی فانتزی یا ابزارهای مبتنی بر متن و ابزارهای رابط کاربری مانند `aptitude`.