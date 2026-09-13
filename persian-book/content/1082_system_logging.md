Title: 108.2 ثبت سیستم
Date: 2010-12-03 10:20
Category: LPIC1
Tags: LPIC1, 102, LPIC1-102-500
Authors: Jadi
sortorder: 370
Summary: 

_وزن: 4_

کاندیداها باید بتوانند rsyslog را پیکربندی کنند. این هدف همچنین شامل پیکربندی شبح ورود به سیستم برای ارسال خروجی ورود به یک سرور ثبت مرکزی یا پذیرش خروجی گزارش به عنوان سرور ثبت مرکزی است. استفاده از زیرسیستم ژورنال systemd پوشش داده شده است. همچنین، آگاهی از syslog و syslog-ng به‌عنوان سیستم‌های ثبت جایگزین گنجانده شده است.

### حوزه های دانش کلیدی

* پیکربندی اولیه rsyslog.
* شناخت امکانات، اولویت ها و اقدامات استاندارد.
* از ژورنال systemd پرس و جو کنید.
* داده های مجله systemd را بر اساس معیارهایی مانند تاریخ، سرویس یا اولویت فیلتر کنید.
* ذخیره سازی مجله سیستم و اندازه مجله مداوم را پیکربندی کنید.
* داده های ژورنال systemd قدیمی را حذف کنید.
* داده های مجله systemd را از یک سیستم نجات یا کپی سیستم‌فایل (Filesystem) بازیابی کنید.
* تعامل rsyslog با systemd-journald را درک کنید.
* پیکربندی logrotate.
* آگاهی از syslog و syslog-ng.

### شرایط و امکانات

* `/etc/rsyslog.conf`
* `/var/log/`
* `logger`
* `logrotate`
* `/etc/logrotate.conf`
* `/etc/logrotate.d/`
* `journalctl`
* `systemd-cat`
* `/etc/systemd/journald.conf`
* `/var/log/journal/`

<iframe width="560" height="315" src="https://www.youtube.com/embed/qtHTf6q_UaI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>


### تاریخچه
لاگ ها بخش مهمی از فلسفه و طراحی یونیکس هستند. هسته، سرویس‌ها، برنامه‌ها و بیشتر رویدادها (بگذارید یک خرابی یا تلاش برای ورود به سیستم باشد) گزارش‌ها را ایجاد می‌کنند. این گزارش ها را می توان برای به دست آوردن بینش در مورد سیستم و وضعیت آن بررسی / نظارت کرد. اگر به مدت 1 ساعت یک مرد لینوکس را روی یک دستگاه ویندوز تماشا کنید، خواهید شنید که "Log ها کجا هستند؟" 

اگر هر برنامه سعی کند لاگ های خود را مدیریت کند، با 2 مشکل مواجه خواهیم شد (حداقل!). 1. برنامه نویسی دشوار خواهد بود زیرا شما نیاز به اختراع (یا وارد کردن) چرخ دارید و 2. برنامه نویسان مختلف انواع، فرمت ها و مکان های مختلفی را برای گزارش های خود تولید می کنند و نگه داشتن آنها تحت کنترل شما دشوار خواهد بود. برای غلبه بر این موضوع، جهان یونیکس راه حل خاص خود را داشت: سرویس ثبت مرکزی.

ابزار قدیمی‌تر برای مدیریت گزارش‌ها `syslog` نام داشت، سپس `syslog-ng` (نسل جدید) و بعدا `rsyslog` داشتیم که تا چند سال پیش اکثر توزیع‌ها از آن استفاده می‌کردند. `rsyslog` هنوز وجود دارد و بخشی از جهان گنو/لینوکس است. می‌تواند گزارش‌ها را از برنامه‌های مختلف (حتی از طریق شبکه) دریافت کند و آنها را در مکان‌های مختلف (فایل‌ها یا فایل‌های موجود در شبکه یا حتی اجرای برخی اقدامات روی آنها) ذخیره کند. گزارش‌های آن در قالب متن ذخیره می‌شوند و می‌توانند توسط ابزار انتخابی شما مدیریت شوند، اجازه دهید `grep`، `less`، `tail`، `zless` (کمتر یک فایل فشرده بدون باز کردن صریح آن)، ____INLINE_29 (به طور واضح آن را باز کنید)، ____INLINE_3 `grep`، ....

اما این روزها `systemd` در حال تسخیر بیشتر دنیای لینوکس است و لاگ ها نیز از این قاعده مستثنی نیستند. سرویس ثبت نام SystemDs `journald` نامیده می شود و ما از دستور `journalctl` برای خواندن گزارش های آن استفاده می کنیم. متأسفانه آنها دیگر فایل متنی نیستند.

همچنین باید چند ابزار دیگر (مانند `logrotate` برای پاکسازی گزارش‌های قدیمی‌تر) را بدانید و با برخی از گزارش‌های مهم‌تر سیستم تحت گنو/لینوکس آشنا باشید. پس بیایید شروع کنیم.

> دانستن اینکه چگونه سیاهههای مربوط به عمق بیشتری کار می کنند سرگرم کننده است. اینجاست: هرکسی که می‌خواهد چیزی را ثبت کند، در نهایت پیام‌های خود را به دستگاه‌های `/dev/log` یا `/dev/kmsg` می‌فرستد (اغلب با استفاده از ابزار کمکی). ابزار گزارش‌گیری (مثلا `rsyslog`) از این دستگاه‌ها می‌خواند و گزارش‌ها را بر اساس تنظیمات آن پردازش می‌کند. و اکنون، پیام ها سیاهههای مربوط هستند!

## dmesg
همانطور که به شما گفتم، لینوکس لاگ را دوست دارد و از ثبت همه چیز خوشحال خواهد شد. اما در مورد فرآیند بوت چطور؟ اگر هسته بخواهد چیزی را قبل از آماده شدن دیسک ها ثبت کند، چه اتفاقی می افتد؟ این گزارش‌ها توسط هسته در *Kernel Ring Buffer* ذخیره می‌شوند. با استفاده از دستور `dmesg` می توانید به آن دسترسی داشته باشید. 


## چرخش گزارش
بنابراین سیاهههای مربوط در حال تولید و ذخیره می شوند! کسی باید آنها را تمیز کند تا از پر شدن دیسک جلوگیری کند. ابزار `logrotate` این کار را بر عهده می گیرد.  پیکربندی اصلی در `/etc/logrotate.conf` است:

```
root@debian:# cat /etc/logrotate.conf
# see "man logrotate" for details

# global options do not affect preceding include directives

# rotate log files weekly
weekly

# keep 4 weeks worth of backlogs
rotate 4

# create new (empty) log files after rotating old ones
create

# use date as a suffix of the rotated file
#dateext

# uncomment this if you want your log files compressed
#compress

# packages drop log rotation information into this directory
include /etc/logrotate.d

# system-specific logs may also be configured here.
```

و سرویس‌های خاص گزارش‌های خود را در `/etc/logrotate.d/` ایجاد می‌کنند:

```
root@debian:# cat /etc/logrotate.d/apt
/var/log/apt/term.log {
  rotate 12
  monthly
  compress
  missingok
  notifempty
}

/var/log/apt/history.log {
  rotate 12
  monthly
  compress
  missingok
  notifempty
}
```


اینها معنای برخی از این پارامترها هستند:

| پارامتر | معنی |
| :---: | :---: |
| هفتگی | چرخش سیاهههای مربوط به صورت هفتگی |
| missingok | اگر گزارشی برای این هفته وجود نداشته باشد خوب است |
| چرخش 52 | آخرین 52 گزارش را نگه دارید و موارد قدیمی تر را حذف کنید |
| فشرده سازی | فشرده سازی سیاهههای مربوط |
| ایجاد 0640 www-data adm | فایل ها را با این دسترسی و صاحبان | ایجاد کنید
| چرخش قبل و بعد | این اسکریپت ها یا دستورات را قبل و بعد از چرخش | اجرا کنید

این پیکربندی بالا یک فایل فشرده برای هر هفته ایجاد می کند و تنها 52 مورد از آنها را به جای یک فایل لاگ بزرگ برای این برنامه نگه می دارد.



`logrotate` با استفاده از cron ها اجرا می شود و کار خود را به صورت روزانه بر اساس پیکربندی در `/etc/cron.daily/logrotate` انجام می دهد.


## چند فایل لاگ معروف

معمولاً گزارش‌ها در `/var/log` ذخیره می‌شوند. در صورت بروز هر مشکلی و اگر نمی‌دانید چه کاری باید انجام دهید، این یک روش معمول است که یک `ls -ltrh /var/log/` را اجرا کنید تا ببینید آیا برنامه‌ای گزارش جدیدی تولید کرده است یا خیر.

اما اجازه دهید نگاهی به برخی از لاگ های معروف بیندازیم:


##### `/var/log/auth.log` (در دبیان مبتنی بر)

فرآیندهای احراز هویت در اینجا وارد می شوند. مواردی مانند مشاغل `cron`، ورود ناموفق، اطلاعات `sudo`، ...
##### `/var/log/syslog`

در صورتی که فایل لاگ خاصی در `/etc/rsyslog.conf` ارائه نشده باشد، یک مکان متمرکز بیشتر گزارش‌های دریافت شده توسط `rsyslogd`
##### `/var/log/debug`

اشکال زدایی اطلاعات از برنامه ها

##### `/var/log/kern.log`

پیام های هسته
##### `/var/log/messages`

پیام های آموزنده از خدمات. همچنین این مکان پیش‌فرض برای گزارش‌ها برای مشتریان راه دور است.
##### `/var/run/utmp` & `/var/log/wtmp`

لاگین های موفق
##### `/var/log/btmp`

ورود ناموفق شما می توانید این را بررسی کنید تا ببینید آیا کسی سعی در حدس زدن رمزهای عبور شما دارد یا خیر!
##### `/var/log/faillog`

تلاش‌های احراز هویت ناموفق بود.
##### `/var/log/lastlog`
تاریخ و زمان آخرین ورود کاربران

##### گزارش های خدمات
گزارش‌های سرویس فایل‌ها یا دایرکتوری (پوشه)‌ها را در `/var/log` ایجاد می‌کنند و گزارش‌های خود را در آنجا به‌روزرسانی می‌کنند. برای مثال ممکن است یک `/var/log/apache2/` (یا `/var/log/httpd`) برای سرور HTTP Apache یا یک `/var/log/mysql` برای MySQL DB وجود داشته باشد.





## rsyslog

<iframe width="560" height="315" src="https://www.youtube.com/embed/xliHONdwFy0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

این نسل جدید syslogs است و در بسیاری از محیط ها استفاده می شود. پیکربندی اصلی آن در `/etc/rsyslog.conf` قرار دارد و همچنین هر چیزی را در فهرست `/etc/rsyslog.d/` می خواند. پیکربندی آن از 3 بخش اصلی تشکیل شده است: 

1. `MODULES`، ماژول های استفاده شده. برای مثال اجازه دهید rsyslog از اتصالات UDP استفاده کند
2. `GLOBAL DIRECTIVES`، پیکربندی‌های عمومی مانند دسترسی‌های دایرکتوری (پوشه)‌ها
3. `RULES`، ترکیبی از *امکانات*، *اولویت*ها* و *اقدامات* به `rsyslog` می گوید که با هر گزارش چه کاری انجام دهد.

```
root@debian:~# cat /etc/rsyslog.conf
# /etc/rsyslog.conf configuration file for rsyslog
#
# For more information install rsyslog-doc and see
# /usr/share/doc/rsyslog-doc/html/configuration/index.html


#################
#### MODULES ####
#################

module(load="imuxsock") # provides support for local system logging
module(load="imklog")   # provides kernel logging support
#module(load="immark")  # provides --MARK-- message capability

# provides UDP syslog reception
#module(load="imudp")
#input(type="imudp" port="514")

# provides TCP syslog reception
#module(load="imtcp")
#input(type="imtcp" port="514")


###########################
#### GLOBAL DIRECTIVES ####
###########################

#
# Set the default permissions for all log files.
#
$FileOwner root
$FileGroup adm
$FileCreateMode 0640
$DirCreateMode 0755
$Umask 0022

#
# Where to place spool and state files
#
$WorkDirectory /var/spool/rsyslog

#
# Include all config files in /etc/rsyslog.d/
#
$IncludeConfig /etc/rsyslog.d/*.conf


###############
#### RULES ####
###############

#
# Log anything besides private authentication messages to a single log file
#
*.*;auth,authpriv.none		-/var/log/syslog

#
# Log commonly used facilities to their own log file
#
auth,authpriv.*			/var/log/auth.log
cron.*				-/var/log/cron.log
kern.*				-/var/log/kern.log
mail.*				-/var/log/mail.log
user.*				-/var/log/user.log

#
# Emergencies are sent to everybody logged in.
#
*.emerg				:omusrmsg:*
```

همانطور که می بینید **امکانات** می تواند مواردی مانند:
  > `kern`، `user`، `mail`، `daemon`، `cron`، `auth`، `ntp`، ___INLINE____IN____، `syslog`، ... 

**اولویت** می تواند یکی از موارد زیر باشد:
  > `emerg`/`panic`, `alert`, `crit`, `err`/`error`, `warn`/___INLINE____IN___, `info` یا `debug`. 

در قسمت **اکشن** می توانیم مواردی مانند این داشته باشیم:

| اقدام | نمونه | معنی |
| :---: | :---: | :--- |
| نام فایل | /usr/log/logins.log | گزارش را در این فایل می نویسد |
| نام کاربری | جادی | به آن شخص روی صفحه اطلاع می دهد |
| @ip | @192.168.1.100 | این گزارش را به این سرور ورود ارسال می کند و آن سرور ورود تصمیم می گیرد که با آن بر اساس تنظیماتش چه کند |

بنابراین خطی مانند این، کرنل را به یک سرور گزارش راه دور نشان می دهد و همچنین همه چیز را در هر سطح در یک فایل گزارش ثبت می کند:

```text
kern.panic      @192.168.1.100
*.*             /var/log/messages
```

اگر اولویت خاصی را وارد کنید، همه چیزهای **مهمتر** نیز ثبت خواهند شد! بنابراین اگر بنویسید `cron.notice /var/log/cron/cron.log`، در حال ثبت گزارش های `emerg/panic`، `alert`، `critical`، `error`، `warning` و `notice` از دسته cc نیز هستید.


سطوح اولویت (براساس Syslog (3) و manpage logger):

```text

       This determines the importance of the message.  The levels are, in order of decreasing importance:

       emerge      system is unusable

       alert      action must be taken immediately

       crit       critical conditions

       error        error conditions

       warning    warning conditions

       notice     normal, but significant, condition

       info       informational message

       debug      debug-level message


       panic      deprecated synonym for emerg
       error      deprecated synonym for err
       warn       deprecated synonym for warning

```

> اگر باید فقط یک سطح خاص را وارد کنید، یک علامت مساوی \(=\) قبل از اولویت مانند این `local3.=alert /var/log/user.alert.log` اضافه کنید.

دانستن این نکته مهم است که باینری که رده _\*kern_ را ثبت می کند یک دیمون مستقل است. این دیمون `klogd` نام دارد و از همان فایل های پیکربندی استفاده می کند. چرا؟ بنابراین حتی پس از خراب شدن همه چیز، `klogd` می‌تواند خرابی‌های هسته را ثبت کند ;\).


### لاگر
اگر می‌خواهید چیزی به سمت `rsyslog` ارسال کنید، می‌توانید از ابزار `logger` استفاده کنید. 

```
root@debian:# logger Testing my lovely tool
root@debian:# logger local1.emerg Nothing emergent for sure
root@debian:# tail -3 /var/log/syslog
2023-06-30T06:05:01.325358-04:00 debian CRON[914]: (root) CMD (command -v debian-sa1 > /dev/null && debian-sa1 1 1)
2023-06-30T06:13:27.671410-04:00 debian root: Testing my lovely tool
2023-06-30T06:13:45.795158-04:00 debian root: local1.emerg Nothing emergent for sure
```



## مجله

<iframe width="560" height="315" src="https://www.youtube.com/embed/jXO7q_7a6-s" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

شما `systemd` را در بخش های مختلف این دوره دیده اید. ما دیدیم که چگونه بخشی از فرآیند init است و چگونه خدمات و تایمرها را مدیریت می کند. همه این فعالیت‌ها (و سایر گزارش‌هایی که به سیستم ژورنالیست سیستم می‌رسند) در فایل‌های باینری ثبت می‌شوند و با استفاده از `journalctl` که بخشی از ابزار `systemd-journald` است، قابل خواندن هستند.

```
root@debian:~# systemctl status systemd-journald
● systemd-journald.service - Journal Service
     Loaded: loaded (/lib/systemd/system/systemd-journald.service; static)
     Active: active (running) since Fri 2023-06-30 05:28:50 EDT; 52min ago
TriggeredBy: ● systemd-journald-dev-log.socket
             ● systemd-journald-audit.socket
             ● systemd-journald.socket
       Docs: man:systemd-journald.service(8)
             man:journald.conf(5)
   Main PID: 261 (systemd-journal)
     Status: "Processing requests..."
      Tasks: 1 (limit: 4583)
     Memory: 17.1M
        CPU: 138ms
     CGroup: /system.slice/systemd-journald.service
             └─261 /lib/systemd/systemd-journald

Jun 30 05:28:50 debian systemd-journald[261]: Journal started
Jun 30 05:28:50 debian systemd-journald[261]: Runtime Journal (/run/log/journal/ec22e43962c64359b9b25cfa650b025b) is 4.9M, max 39.1M,>
Jun 30 05:28:50 debian systemd-journald[261]: Time spent on flushing to /var/log/journal/ec22e43962c64359b9b25cfa650b025b is 23.816ms>
Jun 30 05:28:50 debian systemd-journald[261]: System Journal (/var/log/journal/ec22e43962c64359b9b25cfa650b025b) is 28.2M, max 4.0G, >
Jun 30 05:28:50 debian systemd-journald[261]: Received client request to flush runtime journal.
Notice: journal has been rotated since unit was started, output may be incomplete.
```

و اینجا فایل پیکربندی است:

```
root@debian:~# cat /etc/systemd/journald.conf
#  This file is part of systemd.
#
#  systemd is free software; you can redistribute it and/or modify it under the
#  terms of the GNU Lesser General Public License as published by the Free
#  Software Foundation; either version 2.1 of the License, or (at your option)
#  any later version.
#
# Entries in this file show the compile time defaults. Local configuration
# should be created by either modifying this file, or by creating "drop-ins" in
# the journald.conf.d/ subdirectory. The latter is generally recommended.
# Defaults can be restored by simply deleting this file and all drop-ins.
#
# Use 'systemd-analyze cat-config systemd/journald.conf' to display the full config.
#
# See journald.conf(5) for details.

[Journal]
#Storage=auto
#Compress=yes
#Seal=yes
#SplitMode=uid
#SyncIntervalSec=5m
#RateLimitIntervalSec=30s
#RateLimitBurst=10000
#SystemMaxUse=
#SystemKeepFree=
#SystemMaxFileSize=
#SystemMaxFiles=100
#RuntimeMaxUse=
#RuntimeKeepFree=
#RuntimeMaxFileSize=
#RuntimeMaxFiles=100
#MaxRetentionSec=
#MaxFileSec=1month
#ForwardToSyslog=yes
#ForwardToKMsg=no
#ForwardToConsole=no
#ForwardToWall=yes
#TTYPath=/dev/console
#MaxLevelStore=debug
#MaxLevelSyslog=debug
#MaxLevelKMsg=notice
#MaxLevelConsole=info
#MaxLevelWall=emerg
#LineMax=48K
#ReadKMsg=yes
#Audit=no
```

### استعلام محتوای مجله

اگر `journalctl` را اجرا کنید، همه گزارش‌ها را دریافت خواهید کرد... خیلی زیاد. بنابراین چند سوئیچ مفید وجود دارد:

| سوئیچ | معنی |
| :---: | :---: |
| -r | نمایش معکوس؛ جدیدتر در بالا |
| -f | به نشان دادن دم ادامه دهید |
| -e | نمایش و رفتن تا آخر |
| -n | این تعداد خطوط را از آخر نشان دهید (جدیدترین ها) |
| -k | نمایش پیام هسته (برابر با `dmesg`) |
| -b | نمایش از یک بوت خاص، -1 بوت قبلی است، 0 بوت فعلی است. می‌توانید با استفاده از `--list-boots` | فهرست را بررسی کنید
| -p | از اولویت خاص، بگویید `-p err` |
| -u | از یک واحد systemd خاص |

همچنین می‌توانید از `--since` و `--until` برای نمایش یک محدوده زمانی خاص استفاده کنید، می‌توانید زمان را به‌عنوان `YYYY-MM-DD HH:MM:SS` ارائه کنید یا از مواردی مانند `yesterday`، `today`، ___INLINE_، حتی _1__IN_، یا حتی استفاده کنید. `--since "10 minutes ago"` که برابر است با `--since "-2 minutes"`.

> اگر تعداد خطوط زیاد است، `>` را فشار دهید تا به انتها بپرید (یا `<` را برای رفتن به ابتدا فشار دهید)

همچنین می توانید نام برنامه را به دستور اضافه کنید تا گزارش های مربوط به آن برنامه خاص را مشاهده کنید. بگویید `journalctl /usr/bin/xrdp` یا از برخی فیلدها مانند `PRIORITY=`، `_PID=` استفاده کنید و مقادیر را ارائه دهید.

### systemd-cat
این ابزار زمانی استفاده می شود که بخواهید به صورت دستی گزارش ها را به سیستم ژورنالینگ ارسال کنید. ورودی خود را به ژورنال می فرستد یا در صورت ارائه دستور را اجرا می کند و نتیجه را به مجله ارسال می کند.

```
root@debian:~# echo "This is my first test" | systemd-cat
root@debian:~# systemd-cat -p info uptime #sending priority too
root@debian:~# journalctl -n 3
Jun 30 06:31:01 debian systemd[1]: Finished apt-daily.service - Daily apt download activities.
Jun 30 06:34:18 debian cat[1020]: This is my first test
Jun 30 06:34:48 debian uptime[1022]:  06:34:48 up  1:05,  4 users,  load average: 0.00, 0.00, 0.00
```

## مدیریت ذخیره سازی
ژورنال های systemd می توانند گزارش های خود را در حافظه نگه دارند یا آنها را روی دیسک بنویسند یا همه گزارش ها را رها کنند. این توسط پیکربندی های موجود در `/etc/systemd/journald.conf` تعیین می شود. اما رفتار پیش فرض به صورت زیر است:

1. سیستم `/var/log/journal` را بررسی می کند. اگر این دایرکتوری (پوشه) وجود داشته باشد، گزارش‌های موجود در دایرکتوری (پوشه) داخل آن ذخیره می‌شوند. نام دایرکتوری (پوشه) با نگاه کردن به `/etc/machine-id` تعیین می شود
2. اگر `/var/log/journal` وجود ندارد، گزارش‌ها در حافظه `/run/log/jouranl` و در فهرستی که توسط `/etc/machine-id` تعیین شده ذخیره می‌شود.

اما می توانید با بخش های زیر بر این تنظیمات غلبه کنید:

```
Storage=volatile     # keep the logs in memory
Storage=persistent   # keep on disk, if needed create the directories
Storage=auto         # will write to disk only if the directory exists
Storage=none         # do not keep logs
```

اگر گزارش‌ها روی دیسک نوشته می‌شوند، این متغیر مصرف دیسک را مدیریت می‌کند:

| نام متغیر | استفاده |
| :----: | --- | 
| SystemMaxUse | حداکثر استفاده از دیسک، مثلاً 500M. پیش‌فرض روی `10%` است |
| SystemKeepFree | حداقل این مقدار را رایگان نگه دارید، مثلاً 1G. پیش فرض 15% است |
| SystemMaxFileSize | حداکثر اندازه هر فایل جداگانه پیش فرض 1/8 SystemMaxUse | است
| SystemMaxFiles | حداکثر تعداد فایل‌هایی که در حال حاضر فعال نیستند. پیش فرض 100 |

اگر گزارش‌ها را در **حافظه** نگه می‌دارید، متغیرهای معادل عبارتند از `RuntimeMaxUse`، `RuntimeKeepFree`، `RuntimeMaxFileSize`، و `RuntimeMaxFiles`.  

در صورتی که لازم است پاکسازی را به صورت دستی انجام دهید (حتماً با کمک ابزارهای systemd)، می توانید `journalctl` را با این سوئیچ ها اجرا کنید:


 
| سوئیچ | استفاده |
| :----: | --- | 
| --وکیوم-زمان | همه چیز قدیمی تر از این را تمیز کنید به عنوان مثال `--vacuum-time=3months` هر چیزی قدیمی تر از 3 ماه را تمیز کنید. می‌توانید از `s`، `m`، `h` برای ثانیه‌ها، دقیقه‌ها و روزها و `d`/`days`، `months`، ___IN_LINE_1___، ___IN_LINE_1_14 و `days`، `m`، ___IN_LINE_1___ و `years`/`y`. 
| --وکیوم اندازه | حذف تا زمانی که سیاهههای مربوط یک اندازه خاص را اشغال کنند. بگو 1G |
| --vacuum-files | فقط این مقدار فایل بایگانی را نگه دارید |

### چک کردن گزارش‌ها از یک سیستم بازیابی شده
اگر یک سیستم خراب / غیر بوت شده دارید، همچنان می توانید گزارش های آن را بررسی کنید. اگر فایل ها وجود دارد همانطور که می‌دانید فایل‌ها در `/var/log/journal/{mchine-id}` هستند، جایی که machine-id در `/etc/machine-id` دستگاه خراب است. 

می‌توانید این فایل‌ها را پس از راه‌اندازی دستگاه از کار افتاده با لینوکس زنده به دایرکتوری (پوشه) منتقل کنید یا آن را روی دستگاه دیگری نصب کنید یا حتی آن‌ها را در جای خود بررسی کنید. سوئیچ `-D` (یا `--directory`) `journalctl` مکان فایل های مجله را نشان می دهد. بنابراین اگر شناسه دستگاه خراب شما `ec22e43962c64359b9b25cfa650b025b` است و `/var/` آن را در پوشه `/mnt/var/` خود نصب کرده اید، می توانید این دستور را صادر کنید تا گزارش های آن را بخوانید و ببینید چه اتفاقی افتاده است:

```
journalctl -D=/mnt/var/log/journal/ec22e43962c64359b9b25cfa650b025b/
```

همچنین می‌توانید از سوئیچ `--merge` برای ادغام این گزارش‌ها در دستگاه خود استفاده کنید یا از `--file` برای بررسی فقط یک فایل مجله خاص استفاده کنید. در نهایت اگر مکان دقیق فایل‌های مجله مشخص نیست، می‌توانید از `--root /mnt` استفاده کنید و به `journalctl` بگویید تا فایل‌های مجله را در آنجا جستجو کند.