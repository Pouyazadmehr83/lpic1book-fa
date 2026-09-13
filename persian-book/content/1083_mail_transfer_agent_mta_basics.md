Title: 108.3 اصول اولیه عامل انتقال نامه (MTA).
Date: 2010-12-03 10:20
Category: LPIC1
Tags: LPIC1, 102, LPIC1-102-500
Authors: Jadi
sortorder: 380
Summary: 

_وزن: 3_

کاندیداها باید از برنامه های متداول MTA در دسترس آگاه باشند و بتوانند تنظیمات اولیه فوروارد و نام مستعار را در میزبان مشتری انجام دهند. سایر فایل های پیکربندی پوشش داده نمی شوند.

### حوزه های دانش کلیدی

* `uname` مستعار ایمیل ایجاد کنید.
* پیکربندی ارسال ایمیل.
* دانش برنامه های متداول MTA \(`postfix`, `sendmail`, `exim`\) \(بدون پیکربندی\)

### شرایط و امکانات

* `~/.forward`
* دستورات لایه شبیه سازی sendmail
* `newaliases`
* `mail`
* `mailq`
* `postfix`
* `sendmail`
* `exim`

<iframe width="560" height="315" src="https://www.youtube.com/embed/0Uh7jUFQAWs" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>


### MTAs

ایمیل بخشی جدایی ناپذیر از بسیاری از سیستم های گنو/لینوکس و یونیکس است. هر کاربر یک صندوق پستی دارد و می‌تواند برای سایر کاربران محلی ایمیل ارسال یا دریافت کند. این کار از طریق MTAs (Mai Transfer Agents) انجام می شود. به عبارت دیگر، MTAها برنامه هایی هستند که ایمیل ها را در سیستم عامل شما مدیریت می کنند. آنها می توانند ایمیل ها را به صورت محلی و از طریق شبکه دریافت و ارسال کنند. گزینه های مختلفی برای MTA ها وجود دارد. در این بخش، مروری سریع بر روی آن‌ها انجام می‌دهیم و خواهید دید که چگونه می‌توانید ایمیل‌ها را به موارد دیگر (یا از طریق اینترنت) ارسال کنید و چگونه می‌توانید ایمیل‌های محلی خود را بررسی کنید.

#### ارسال ایمیل
یکی از قدیمی ترین گزینه های موجود است. پیکربندی آن بسیار بزرگ و به نوعی دشوار است و نه آنچنان امنیتی. به همین دلیل، تعداد کمی از سیستم ها از آن به عنوان پیش فرض MTA خود استفاده می کنند.


#### exim
هدف آن این است که یک ارسال کننده عمومی و انعطاف پذیر با امکانات گسترده برای بررسی ایمیل های دریافتی باشد. این ویژگی غنی از ACL ها، احراز هویت و بسیاری از ویژگی های دیگر است.

#### پسوند
این یک جایگزین جدید برای `sendmail` است و از فایل های پیکربندی آسان برای درک استفاده می کند. از چندین دامنه، رمزگذاری و غیره پشتیبانی می کند. Postfix همان چیزی است که در اکثر توزیع ها به عنوان MTA پیش فرض می بینید.

> اکثر توزیع های دسکتاپ MTA را به طور پیش فرض نصب نمی کنند. اگر می خواهید، پیشنهاد می کنم `postfix` (و `mailx` یا `bsd-mailx`) را از طریق مدیر بسته‌ها (Package Manager) خود نصب کنید.

### لایه شبیه سازی sendmail
همانطور که می دانید، `sendmail` قدیمی ترین MTA موجود است و بنابراین، بسیاری از MTA های دیگر سعی می کنند از آن پیروی کنند و دارای یک لایه _sendmail شبیه سازی_ هستند تا خود را با sendmail سازگار نگه دارند. به همین دلیل است که می توانید `sendmail` را در هر توزیعی که هستید تایپ کنید یا از `mailq` استفاده کنید و ایمیل خود را بدون توجه به انتخاب MTA خود بررسی کنید.

### نام مستعار

تعدادی نام مستعار ایمیل در سیستم وجود دارد. در `/etc/aliases` تعریف شده است.

```text
$ cat /etc/aliases
#
#  Aliases in this file will NOT be expanded in the header from
#  Mail, but WILL be visible over networks or from /bin/mail.
#
#       >>>>>>>>>>      The program "newaliases" must be run after
#       >> NOTE >>      this file is updated for any changes to
#       >>>>>>>>>>      show through to sendmail.
#

# Basic system aliases -- these MUST be present.
mailer-daemon:  postmaster
postmaster:     root

# General redirections for pseudo accounts.
bin:            root
daemon:         root
adm:            root
lp:             root
sync:           root
shutdown:       root
halt:           root
mail:           root
news:           root
uucp:           root
operator:       root
games:          root
www:            webmaster
webmaster:      root
[ .... ]
```

این به سیستم می گوید که اگر پیامی برای *news* وجود دارد، باید به *root* تحویل داده شود و اگر ایمیل به *www* نوشته شده است باید به *وب مستر* تحویل داده شود. 

در صورت تغییر در این فایل، باید دستور `newaliases` را اجرا کنید.


### ارسال نامه

امکان ارسال ایمیل از خط فرمان (Command Line) با استفاده از دستور `mail` وجود دارد:

```text
[jadi@funlife ~]$ mail news
Subject: Email to news user
hahah.. we know where this will go.
this will go to root and then to jadi!

Hi Jadi!

Cc:
[jadi@funlife ~]$ mail
Mail version 8.1.2 01/15/2001.  Type ? for help.
"/var/mail/jadi": 12 messages 12 new
>N  1 root@funlife       Sat Jan 02 08:50   39/1373  apt-listchanges: news for f
 N  2 root@funlife       Sat Jan 02 09:01  165/7438  apt-listchanges: news for f
 N  3 jadi@funlife       Sat Jan 02 19:58   18/640   *** SECURITY information fo
 N  4 jadi@funlife       Sat Jan 02 20:04   18/631   *** SECURITY information fo
 N  5 jadi@funlife       Sun Jan 03 10:15   18/664   *** SECURITY information fo
 N  6 root@funlife       Mon Jan 04 12:42   27/941   Cron <jadi@funlife> /home/j
 N  7 root@funlife       Mon Jan 04 17:11   26/845   apt-listchanges: news for f
 N  8 root@funlife       Tue Jan 05 18:42   27/945   Cron <jadi@funlife> /home/j
 N  9 root@funlife       Wed Jan 06 09:17   46/1788  apt-listchanges: news for f
 N 10 root@funlife       Thu Jan 07 12:42   27/945   Cron <jadi@funlife> /home/j
 N 11 root@funlife       Thu Jan 07 18:42   27/943   Cron <jadi@funlife> /home/j
 N 12 jadi@funlife       Thu Jan  7 19:53   17/478   Email to news user
& 12
Message 12:
From jadi@funlife  Thu Jan  7 19:53:08 2016
X-Original-To: news
To: news@funlife
Subject: Email to news user
Date: Thu,  7 Jan 2016 19:53:08 +0330 (IRST)
From: jadi@funlife (jadi)

hahah.. we know where this will go.
this will go to root and then to jadi!

Hi Jadi!

& d
& q
Held 11 messages in /var/mail/jadi
```

### مهاجمان محلی

دیدیم که می‌توان ایمیل‌ها را با استفاده از `/etc/aliases` فوروارد کرد. آن فایل توسط کاربران عادی قابل نوشتن نیست، پس یک کاربر معمولی مانند _jadi_ باید چه کار کند؟

هر کاربر می‌تواند یک فایل `.forward` در فهرست راهنمای خود ایجاد کند و تمام نامه‌های هدفمند به آن کاربر به آن آدرس بازارسال می‌شود.

> حتی می توانید یک آدرس ایمیل کامل مانند `jadijadi@gmail.com` را در فایل `.forward` خود قرار دهید.

همچنین می‌تواند از طریق خط فرمان (Command Line) یا حتی در اسکریپت‌های شما ایمیل ارسال کند و چیزی مانند `echo -e "email content" | mail -s "email subject" "example@example.com"` ارسال کند.

### mailq

این دستور صف ایمیل را لیست می کند. هر ورودی شناسه فایل صف، اندازه پیام، زمان رسیدن، فرستنده و گیرندگانی که هنوز باید تحویل داده شوند را نشان می دهد. اگر نامه در آخرین تلاش تحویل داده نشد، دلیل شکست نشان داده می شود. sysadmin می تواند از این دستور برای بررسی وضعیت ایمیل هایی که هنوز در صف هستند استفاده کند.

```text
$ mailq
-Queue ID- --Size-- ----Arrival Time---- -Sender/Recipient-------
AA52C228E6B      468 Thu Jan  7 19:59:41  jadi@funlife
(connect to alt2.gmail-smtp-in.l.google.com[2404:6800:4003:c01::1a]:25: Network is unreachable)
                                         jadijadi@gmail.com

-- 0 Kbytes in 1 Request.
```