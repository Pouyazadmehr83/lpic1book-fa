Title: 107.3 بومی سازی و بین المللی سازی
Date: 2010-12-03 10:20
Category: LPIC1
Tags: LPIC1, 102, LPIC1-102-500
Authors: Jadi
sortorder: 350
Summary: 

_وزن: 3_

داوطلبان باید بتوانند یک سیستم را به زبانی متفاوت از انگلیسی بومی سازی کنند. همچنین، درک اینکه چرا `LANG=C` هنگام نوشتن اسکریپت مفید است.

### حوزه های دانش کلیدی

* تنظیمات محلی و متغیرهای محیط را پیکربندی کنید.
* تنظیمات منطقه زمانی و متغیرهای محیط را پیکربندی کنید.

### شرایط و امکانات

* `/etc/timezone`
* `/etc/localtime`
* `/usr/share/zoneinfo/`
* `LC_*`
* `LC_ALL`
* `LANG`
* `TZ`
* `/usr/bin/locale`
* `tzselect`
* `timedatectl`
* `date`
* `iconv`
* UTF-8
* ISO-8859
* اسکی
* یونیکد

<iframe width="560" height="315" src="https://www.youtube.com/embed/kqoipsM7AMA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

### منطقه زمانی
زمین بزرگ و گرد است، بنابراین ما ***مناطق زمانی*** و ***زبان های مختلف*** داریم! حتی صحبت هایی در مورد منطقه زمانی مریخ وجود دارد و اگر با بیگانگان روبرو شویم، ممکن است آنها نیز زبان خود را داشته باشند. 

این چند مشکل ایجاد می کند:
1. ممکن است زبان محلی خود را برای لینوکس ترجیح دهیم
2. ما باید منطقه زمانی خود را به لینوکس بگوییم
3. برنامه ها ممکن است از لینوکس در مورد ترجیحات ما در مورد زبان ها، پیکربندی صفحه کلید و ... سوال کنند.
4. و حتی اگر در مورد خودتان چیزی ندارید، دستگاه های شما به منطقه زمانی شما نیاز دارند تا بتوانند وظایف را در زمان های مورد نیاز اجرا کنند. 

در این بخش به شما پاسخ هایی را نشان می دهم که لینوکس برای غلبه بر این مشکلات دارد. اما بیایید ساده شروع کنیم.

در سیستم های لینوکس می توانید از دستورات `date` و `cal` برای بررسی تاریخ و تقویم استفاده کنید. چاپ تاریخ سفارشی با استفاده از قالب‌بندی `+` امکان‌پذیر است:

```
[jadi@fedora ~]$ date
Fri Jun  2 02:07:35 PM EDT 2023
[jadi@fedora ~]$ date +'%Y%m%d-%M'
20230602-08
[jadi@fedora ~]$ date +'%Y%m%d-%H%M'
20230602-1408
```

برای دریافت اطلاعات بیشتر می توانید `timedatectl` را امتحان کنید:

```
[root@fedora ~]# timedatectl
               Local time: Fri 2023-06-02 14:23:34 EDT
           Universal time: Fri 2023-06-02 18:23:34 UTC
                 RTC time: Sat 2023-06-03 02:37:51
                Time zone: America/New_York (EDT, -0400)
System clock synchronized: no
              NTP service: active
          RTC in local TZ: no
```

منطقه زمانی تعیین می کند که تفاوت زمانی شما در مقایسه با منطقه زمانی مرجع چقدر است. به این ترتیب می توانید بدون توجه به موقعیت مکانی خود در مورد زمان ها صحبت کنید. به عبارت دیگر، می توانم به شما بگویم "درخواست تغییر را در ساعت 02:30 UTC شروع کنید" و هر دوی ما می دانیم که تغییر در منطقه زمانی خودمان چه زمانی آغاز می شود \(مال من 1 ساعت جلوتر خواهد بود بنابراین از ساعت 3:30 به وقت خودم شروع می کنم\).

اکثر توزیع ها در حین نصب از شما در مورد منطقه زمانی شما می پرسند. می‌توانید بعداً این را تغییر دهید، یا با یک رابط کاربری گرافیکی در تنظیمات سیستم یا با استفاده از یک رابط کاربری مبتنی بر متن (TUI) مانند `tzconfig` قدیمی‌تر یا یک `tzselect` جدیدتر.

```
[jadi@fedora ~]$ tzselect
Please identify a location so that time zone rules can be set correctly.
Please select a continent, ocean, "coord", or "TZ".
1) Africa							     7) Europe
2) Americas							     8) Indian Ocean
3) Antarctica							     9) Pacific Ocean
4) Asia								    10) coord - I want to use geographical coordinates.
5) Atlantic Ocean						    11) TZ - I want to specify the timezone using the Posix TZ format.
6) Australia
#? 5
Please select a country whose clocks agree with yours.
1) Bermuda				       4) Faroe Islands				      7) Spain
2) Cape Verde				       5) Portugal
3) Falkland Islands			       6) South Georgia & the South Sandwich Islands
#? 1

The following information has been given:

	Bermuda

Therefore TZ='Atlantic/Bermuda' will be used.
Selected time is now:	Fri Jun  2 15:15:06 ADT 2023.
Universal Time is now:	Fri Jun  2 18:15:06 UTC 2023.
Is the above information OK?
1) Yes
2) No
#? 1

You can make this change permanent for yourself by appending the line
	TZ='Atlantic/Bermuda'; export TZ
to the file '.profile' in your home directory; then log out and log in again.

Here is that TZ value again, this time on standard output so that you
can use the /usr/bin/tzselect command in shell scripts:
Atlantic/Bermuda
```

پس از اتمام، این برنامه به شما پیشنهاد می کند که متغیری به نام `TZ` را به صورت زیر تنظیم کنید تا منطقه زمانی _خودتان را تنظیم کنید، اما نه سیستم ها:

```text
TZ='Atlantic/Bermuda'; export TZ
```

یا یک بار از آن برای بررسی زمان در یک شهر خاص استفاده کنید:

```
$ env TZ='Asia/Tokyo' date
Sat Jun  3 03:25:40 AM JST 2023
```

### پیکربندی منطقه زمانی

فهرست راهنمای `/usr/share/zoneinfo/` حاوی تمام اطلاعات منطقه زمانی است. این فایل های باینری هستند. اگر می‌خواهید منطقه زمانی سیستم خود را تغییر دهید، باید `/etc/localtime` را به یکی از این فایل‌ها پیوند کوتاه دهید:

```
# ls -ltrh /etc/localtime
lrwxrwxrwx. 1 root root 38 Apr 26 09:41 /etc/localtime -> ../usr/share/zoneinfo/America/New_York
```

این فایل باید با فایل صحیح از `/usr/share/zoneinfo/` جایگزین شود. ایجاد یک پیوند نمادین (Symbolic Link) به جای کپی کردن فایل واقعی بهتر است. این از مشکلات در طول ارتقاء بعدی جلوگیری می کند.

### پیکربندی زبان ها

برای بررسی وضعیت زبان سیستم انتخابی فعلی، از دستور `locale` استفاده کنید:

```
[root@fedora ~]# locale
LANG=en_US.UTF-8
LC_CTYPE="en_US.UTF-8"
LC_NUMERIC="en_US.UTF-8"
LC_TIME="en_US.UTF-8"
LC_COLLATE="en_US.UTF-8"
LC_MONETARY="en_US.UTF-8"
LC_MESSAGES="en_US.UTF-8"
LC_PAPER="en_US.UTF-8"
LC_NAME="en_US.UTF-8"
LC_ADDRESS="en_US.UTF-8"
LC_TELEPHONE="en_US.UTF-8"
LC_MEASUREMENT="en_US.UTF-8"
LC_IDENTIFICATION="en_US.UTF-8"
LC_ALL=
```

اینها متغیرهای محیطی (Environment Variables) هستند که به سیستم می گویند از چه زبانی استفاده کند. در اینجا من از `LANG=en_US.UTF-8` استفاده می کنم، به این معنی که از انگلیسی با نوع US و رمزگذاری UTF-8 استفاده می کنم.

> UTF-8 و سایر رمزگذاری‌ها کمی بعد در این فصل مورد بحث قرار خواهند گرفت

سایر متغیرهایی که در بالا مشاهده می کنید، به سیستم می گویند که چگونه چیزهای مختلف را بر اساس سیستم های محلی سازی نشان دهد. به عنوان مثال، اگر `LC_TIME` را به `"en\_GB.UTF-8"` تغییر دهیم، زمان در قالب بریتانیای کبیر چاپ می شود.

تنظیمات مهم دیگر `LC_ALL` است. می توان از آن برای تغییر تنظیمات **ALL** استفاده کرد. اگر یک `export LC_ALL=fa_IR.UTF-8` را انجام دهید، بدون استثنا، همه تنظیمات روی آن تنظیم می‌شوند. همیشه امکان `unset LC_ALL` وجود دارد.

#### LANG=C

تنظیمات `LANG=C` در بسیاری از برنامه ها و اسکریپت ها استفاده می شود تا اطمینان حاصل شود که سیستم نتایج منسجم و قابل پیش بینی را در همه محیط ها ایجاد می کند. به عنوان مثال برای اطمینان از اینکه ترتیب مرتب سازی به ترتیب باینری خواهد بود و تمام تنظیمات زبان پیش فرض (en.US) خواهد بود.

#### تغییر یا اضافه کردن مناطق

این بخشی از آزمون LPIC نیست، اما خوب است بدانید که در یک ماشین مبتنی بر دبیان، می‌توانید با استفاده از `dpkg-reconfigure locales`، _locales_ پیش‌فرض خود را تغییر دهید، اضافه یا تنظیم کنید.

این فایل هم هست:

```
[root@fedora ~]# cat /etc/locale.conf
LANG="en_US.UTF-8"
```

و همچنین می توانید پیکربندی `LANG` مورد نظر خود را به `~/.bash_profile` یا `~/.profile` خود اضافه کنید.

> در `systemd` از `localectl` برای بررسی منطقه استفاده کنید یا از `localectl set-locale LANG=en_US.UTF-8` برای تنظیم آن استفاده کنید.

### رمزگذاری کاراکتر

#### ACSII

کامپیوترهایی که با رمزگذاری کاراکترهای 7 بیتی کار می کردند. این به ما 128 کاراکتر می دهد که برای اعداد، علائم نگارشی و ارقام کافی است!

#### ISO-8859

کاراکترهای بیشتری داشت و مجموعه‌های زیادی برای زبان‌های تایلندی، عربی و دیگر زبان‌ها داشت، اما همچنان مجموعه‌های کاراکتر ASCII داشت.

#### UTF-8

`Unicode Transformation Format` جدیدترین روش رمزگذاری است. این یک رمزگذاری جهانی واقعی با کاراکترها نه تنها برای همه زبان های نوشتاری بلکه برای کاراکترهای سرگرم کننده مانند ¾، ♠، π و ⚤ است. با ASCII سازگار است و از واحدهای کد 8 بیتی \(**نه کدگذاری 8 بیتی!**\) استفاده می کند. در بیشتر موارد استفاده از UTF-8 ایده خوبی است و مطمئن باشید که سیستم شما عملاً در همه موارد کار می کند.


نماد ###

اگر نیاز به تبدیل کدنویسی به یکدیگر داشتید، دستور `iconv` است. سوئیچ `-l` همه کدگذاری های موجود را به شما نشان می دهد:

```text
iconv -f WINDOWS-1258 -t UTF-8 /tmp/myfile.txt
```

> توجه: -f برای "از" و -t برای "به" است. آسان به خاطر سپردن

در سال 2023 به ندرت به این دستور نیاز خواهید داشت، اما دانستن آن ضروری است، به خصوص اگر در یک کشور غیر آمریکایی زندگی می کنید!