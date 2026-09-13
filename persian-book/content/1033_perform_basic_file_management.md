Title: 103.3 مدیریت فایل اولیه را انجام دهید
Date: 2010-12-03 10:20
Category: LPIC1
Tags: LPIC1, 101, LPIC1-101-500
Authors: Jadi
Summary: داوطلبان باید بتوانند از دستورات پایه لینوکس برای مدیریت فایل ها و دایرکتوری (پوشه) ها استفاده کنند.
sortorder: 140

_وزن: 4_

داوطلبان باید بتوانند از دستورات پایه لینوکس برای مدیریت فایل ها و دایرکتوری (پوشه) ها استفاده کنند.

## اهداف
* کپی، انتقال و حذف فایل ها و دایرکتوری (پوشه) ها به صورت جداگانه.
* چندین فایل و دایرکتوری (پوشه) را به صورت بازگشتی کپی کنید.
* فایل ها و دایرکتوری (پوشه) ها را به صورت بازگشتی حذف کنید.
* از مشخصات ساده و پیشرفته عام در دستورات استفاده کنید.
* استفاده از Find برای مکان یابی و عمل بر روی فایل ها بر اساس نوع، اندازه یا زمان.
* استفاده از tar، cpio و dd.

### شرایط
- cp
- `find`
- mkdir
- mv
- ls
- rm
- rmdir
- لمس کردن
- قیر
- cpio
- dd
- فایل
- gzip
- زیپ
- bzip2
- bunzip2
- xz
- unxz
- globbing فایل

<iframe width="560" height="315" src="https://www.youtube.com/embed/lTnkGg9o6u0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### حروف عام و globbing فایل
File globbing یک قابلیت پوسته است که به شما امکان می دهد مواردی مانند:
- همه فایل ها
- هر چیزی که با A شروع می شود
- تمام فایل‌های دارای نام 3 حرفی که به A یا B یا C ختم می‌شوند
-...

برای این کار باید این شخصیت ها را بدانید:

* `*` به معنای **هر رشته** است
* `?` به معنای هر کاراکتری است
* `[ABC]` با A، B یا C مطابقت دارد
* `[a-k]` با a، b، c، ...، k \(هر دو حروف کوچک و بزرگ\) مطابقت دارد.
* `[0-9a-z]` با تمام ارقام و اعداد مطابقت دارد
* `[!x]` به معنای X نیست.

با دانستن اینها، می توانید الگوهای خود را ایجاد کنید. به عنوان مثال:

| فرمان | معنی |
| :--- | :--- |
| rm * | تمام فایل های این دایرکتوری (پوشه) را حذف کنید |
| ls A*B | نمایش تمام فایل هایی که با A شروع می شوند و با B ختم می شوند
| cp ???.* /tmp | همه فایل‌های دارای 3 کاراکتر، سپس یک نقطه و سپس هر چیزی (حتی هیچ چیز) را در /tmp | کپی کنید
| rmdir [a-z\]* | تمام دایرکتوری (پوشه) های خالی که با حرف | شروع می شوند را حذف کنید

### دستورات کلی
#### فهرست با `ls`

`ls` برای _فهرست_ فهرست_ فهرست ها و فایل ها استفاده می شود. شما می توانید یک مسیر مطلق یا نسبی ارائه دهید. در صورت حذف "." به عنوان هدف استفاده خواهد شد.

```text
jadi@lpicjadi:~/lpic1-practice-iso/100/103.3$ ls -ltrh
total 16K
-rw-rw-r-- 1 jadi jadi 207 Aug 14 04:43 tasks.txt
-rw-rw-r-- 1 jadi jadi  29 Aug 14 04:43 info.txt
-rw-rw-r-- 1 jadi jadi  24 Aug 14 04:44 data.txt
-rw-rw-r-- 1 jadi jadi 116 Aug 14 04:44 note_to_self
```

> فیلد اول نشان می دهد که آیا این یک فایل (`-`) یا فهرست (`d`) است.

برخی از سوئیچ های رایج عبارتند از:

* `-l` برای _long_ است (اطلاعات بیشتر برای هر فایل)
* `-1` در هر خط یک فایل چاپ می کند
* `-t` بر اساس تاریخ اصلاح مرتب می شود
* `-r` جستجو را معکوس می کند (بنابراین `-tr` زمان معکوس است (فایل های جدیدتر در پایین).

> می توانید سوئیچ ها را مخلوط کنید. یکی از معروف‌ترین آنها `-ltrh` (طول + اندازه‌های قابل خواندن توسط انسان + زمان معکوس) است.

### کپی (`cp`)، انتقال (`mv`)، و حذف (`rm`)
#### **cp**

با این کار فایل ها از یک مکان/نام به مکان/نام دیگر _کپی_ می شود. اگر هدف یک دایرکتوری (پوشه) باشد، همه منابع در آنجا کپی می شوند.

```text
cp source destination
```

یک سوئیچ معمولی `-r` (یا `-R`) است که به صورت بازگشتی (دایرکتوری (پوشه) ها و محتویات آنها) کپی می شود. بنابراین برای کپی کردن دایرکتوری (پوشه) به نام `A` در `/tmp/` می توانید `cp -r A /tmp/` را صادر کنید.


#### **mv**


فایل‌ها یا دایرکتوری (پوشه)‌ها را _move_ یا تغییر نام می‌دهد. مانند دستور `cp` عمل می کند. اگر در حال انتقال یک فایل در یک سیستم‌فایل (Filesystem) هستید، **inode** تغییر نمی کند.

به طور کلی:

* اگر هدف یک فهرست موجود باشد، تمام منابع در هدف کپی می شوند
* اگر دایرکتوری (پوشه) هدف وجود نداشته باشد، منبع باید تنها یک دایرکتوری (پوشه) باشد که به دایرکتوری (پوشه) هدف تغییر نام می‌دهد.
* اگر هدف یک فایل است، پس منبع باید فقط یک فایل باشد، بنابراین تغییر نام اتفاق خواهد افتاد.

اینها شبیه "فرمول" هستند اما عقل سلیم هستند!

#### **rm**

حذف (حذف) **فایل**. می توانید این کار را به صورت بازگشتی با استفاده از سوئیچ `-r` انجام دهید یا حتی با استفاده از سوئیچ `-f` (اجباری) از بررسی تاییدیه ها جلوگیری کنید. بنابراین یک `rm -rf /` به معنای *حذف همه چیز از سیستم‌فایل (Filesystem)* است.

**یادداشت**

به طور معمول، اگر فایل موجود قابل نوشتن باشد، دستور cp یک فایل را روی یک نسخه موجود کپی می کند. از سوی دیگر، `mv` در صورت وجود هدف، فایلی را جابجا یا تغییر نام نمی دهد. اگرچه این به شدت به پیکربندی سیستم شما بستگی دارد. اما در همه موارد، می توانید با استفاده از سوئیچ `-f` بر این مشکل غلبه کنید.

* `-f` (--force) باعث می شود که cp بازنویسی هدف را امتحان کند.
* `-i` (--تعاملی) سوال بلی/نه (حذف / بازنویسی) می پرسد.
* `-b` (--پشتیبان گیری) از فایل های رونویسی شده پشتیبان تهیه می کند
* `-p` ویژگی ها را _حفظ می کند.

### ایجاد (mkdir) و حذف (rmdir) دایرکتوری (پوشه) ها

دستور `mkdir` دایرکتوری (پوشه) ها را ایجاد می کند.

```
jadi@lpicjadi:~/lpic1-practice-iso/100/103.3$ ls -ltrh
total 16K
-rw-rw-r-- 1 jadi jadi 207 Aug 14 04:43 tasks.txt
-rw-rw-r-- 1 jadi jadi  29 Aug 14 04:43 info.txt
-rw-rw-r-- 1 jadi jadi  24 Aug 14 04:44 data.txt
-rw-rw-r-- 1 jadi jadi 116 Aug 14 04:44 note_to_self
jadi@lpicjadi:~/lpic1-practice-iso/100/103.3$ mkdir new_dir
jadi@lpicjadi:~/lpic1-practice-iso/100/103.3$ ls -ltrh
total 20K
-rw-rw-r-- 1 jadi jadi  207 Aug 14 04:43 tasks.txt
-rw-rw-r-- 1 jadi jadi   29 Aug 14 04:43 info.txt
-rw-rw-r-- 1 jadi jadi   24 Aug 14 04:44 data.txt
-rw-rw-r-- 1 jadi jadi  116 Aug 14 04:44 note_to_self
drwxrwxr-x 2 jadi jadi 4.0K Aug 14 04:57 new_dir
```

اگر می‌خواهید درختی از دایرکتوری (پوشه)‌ها ایجاد کنید، می‌توانید از سوئیچ `-p` استفاده کنید تا به `mkdir` بگویید در صورت نیاز، فهرست‌های *والد* را ایجاد کند:

```text
jadi@lpicjadi:~/lpic1-practice-iso/100/103.3$ ls -ltrh
total 20K
-rw-rw-r-- 1 jadi jadi  207 Aug 14 04:43 tasks.txt
-rw-rw-r-- 1 jadi jadi   29 Aug 14 04:43 info.txt
-rw-rw-r-- 1 jadi jadi   24 Aug 14 04:44 data.txt
-rw-rw-r-- 1 jadi jadi  116 Aug 14 04:44 note_to_self
drwxrwxr-x 2 jadi jadi 4.0K Aug 14 04:57 new_dir
jadi@lpicjadi:~/lpic1-practice-iso/100/103.3$ mkdir -p 1/2/3 
jadi@lpicjadi:~/lpic1-practice-iso/100/103.3$ tree
.
├── 1
│   └── 2
│       └── 3
├── data.txt
├── info.txt
├── new_dir
├── note_to_self
└── tasks.txt
```

اگر نیاز به حذف دایرکتوری (پوشه) دارید، دستور `rmdir` است و همچنین می توانید از -p برای حذف تودرتو استفاده کنید:

```
jadi@lpicjadi:~/lpic1-practice-iso/100/103.3$ rmdir -p 1/2/3
jadi@lpicjadi:~/lpic1-practice-iso/100/103.3$ rmdir new_dir
jadi@lpicjadi:~/lpic1-practice-iso/100/103.3$ tree
.
├── data.txt
├── info.txt
├── note_to_self
└── tasks.txt

0 directories, 4 files
```

> اگر از `rmdir` برای حذف دایرکتوری (پوشه) استفاده می کنید، *باید خالی باشد*! به همین دلیل است که بسیاری از افراد از `rm -rf directory_name` برای حذف پوشه خالی و هر آنچه در آن است استفاده می کنند.

<iframe width="560" height="315" src="https://www.youtube.com/embed/tSN1MSaFYEw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

#### *لمس**
`touch` یک فایل خالی ایجاد می کند (اگر وجود نداشته باشد) یا تاریخ **تغییر** یک فایل را در صورت وجود به روز می کند. زمان پیش‌فرض *اکنون* است اما می‌توانید زمان‌های دیگر را نیز مشخص کنید.

```
jadi@lpicjadi:~/lpic1-practice-iso/100/103.3$ ls -ltrh
total 16K
-rw-rw-r-- 1 jadi jadi 207 Aug 14 04:43 tasks.txt
-rw-rw-r-- 1 jadi jadi  29 Aug 14 04:43 info.txt
-rw-rw-r-- 1 jadi jadi  24 Aug 14 04:44 data.txt
-rw-rw-r-- 1 jadi jadi 116 Aug 14 04:44 note_to_self
jadi@lpicjadi:~/lpic1-practice-iso/100/103.3$ touch new_file
jadi@lpicjadi:~/lpic1-practice-iso/100/103.3$ ls -ltrh
total 16K
-rw-rw-r-- 1 jadi jadi 207 Aug 14 04:43 tasks.txt
-rw-rw-r-- 1 jadi jadi  29 Aug 14 04:43 info.txt
-rw-rw-r-- 1 jadi jadi  24 Aug 14 04:44 data.txt
-rw-rw-r-- 1 jadi jadi 116 Aug 14 04:44 note_to_self
-rw-rw-r-- 1 jadi jadi   0 Aug 14 05:08 new_file
jadi@lpicjadi:~/lpic1-practice-iso/100/103.3$ touch note_to_self
jadi@lpicjadi:~/lpic1-practice-iso/100/103.3$ ls -ltrh
total 16K
-rw-rw-r-- 1 jadi jadi 207 Aug 14 04:43 tasks.txt
-rw-rw-r-- 1 jadi jadi  29 Aug 14 04:43 info.txt
-rw-rw-r-- 1 jadi jadi  24 Aug 14 04:44 data.txt
-rw-rw-r-- 1 jadi jadi   0 Aug 14 05:08 new_file
-rw-rw-r-- 1 jadi jadi 116 Aug 14 05:08 note_to_self
```

یا می توانید زمان ها را مشخص کنید. می توانید از `-d` استفاده کنید و تاریخ بدهید یا از `-t` استفاده کنید و یک مهر زمانی به شکل `[[CC]YY]MMDDhhmm[.ss]` بدهید.

```text
$ touch -t 200908121510.59 file1
$ touch -d 11am file2
$ touch -d "last fortnight" file3
$ touch -d "yesterday 6am" file4
$ touch -d "2 days ago 12:00" file5
$ touch -d "tomorrow 02:00" file6
$ touch -d "5 Nov" file3
$ ls -ltrh file?
-rw-rw-r-- 1 jadi jadi 0 Aug 12  2009 file1
-rw-rw-r-- 1 jadi jadi 0 Aug 12 12:00 file5
-rw-rw-r-- 1 jadi jadi 0 Aug 13 06:00 file4
-rw-rw-r-- 1 jadi jadi 0 Aug 14  2022 file2
-rw-rw-r-- 1 jadi jadi 0 Aug 15  2022 file6
-rw-rw-r-- 1 jadi jadi 0 Nov  5  2022 file3
```

اوه.. و می توان از زمان فایل دیگری برای تنظیم استفاده کرد، با سوئیچ `-r` (برای -- مرجع)):

```
jadi@lpicjadi:~/lpic1-practice-iso/100/103.3$ ls -l /etc/debian_version
-rw-r--r-- 1 root root 13 Aug 22  2021 /etc/debian_version
jadi@lpicjadi:~/lpic1-practice-iso/100/103.3$ touch -r /etc/debian_version file1
jadi@lpicjadi:~/lpic1-practice-iso/100/103.3$ ls -ltrh
total 20K
-rw-rw-r-- 1 jadi jadi   0 Aug 22  2021 file1
```

#### **پرونده**

برای تعیین نوع فایل باید از دستور `file` استفاده کنید. *به* فایل نگاه می کند و نوع آن را تعیین می کند.

```
jadi@lpicjadi:~/lpic1-practice-iso/100/103.3$ file file1
file1: empty
jadi@lpicjadi:~/lpic1-practice-iso/100/103.3$ file note_to_self
note_to_self: ASCII text
jadi@lpicjadi:~/lpic1-practice-iso/100/103.3$ file /bin/bash
/bin/bash: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=33a5554034feb2af38e8c75872058883b2988bc5, for GNU/Linux 3.2.0, stripped
```

> سوئیچ `-i` قالب mime را چاپ می کند

#### **dd**
دستور `dd` داده ها را از ورودی خود به خروجی آن (مثلاً فایل ها یا دستگاه ها) کپی می کند. شما می توانید از آن درست مانند کپی استفاده کنید:

```
jadi@lpicjadi:~/lpic1-practice-iso/100/103.3$ dd if=note_to_self of=new_file
0+1 records in
0+1 records out
116 bytes copied, 0.00141561 s, 81.9 kB/s
jadi@lpicjadi:~/lpic1-practice-iso/100/103.3$ cat new_file
I will continue learning... and if I get confused, I'll repeat the last section once more till everything is clear!
jadi@lpicjadi:~/lpic1-practice-iso/100/103.3$
```

* `if` فایل ورودی است
* `of` فایل خروجی است

اما معمولاً مردم از آن برای خواندن/نوشتن از دستگاه‌های بلوکی (Block Devices) استفاده می کنند. برای مثال، این کار همه بخش‌ها را از `/dev/sdb` می‌خواند و آنها را در فایلی به نام`backup.dd` می‌نویسد. بعداً می‌توانید با تعویض `if` و `of` و نوشتن از `backup.dd` به `/dev/sdb`، این نسخه پشتیبان را بازیابی کنید. 


```
# dd if=/dev/sda of=backup.dd bs=4096
```

یا حتی:

```
# dd if=/dev/sda2 | gzip > backup.dd.gzip
```

یکی دیگر از کاربردهای رایج ایجاد فایل هایی با اندازه های خاص است:

```
$ dd if=/dev/zero of=1g.bin bs=1G count=1
```

یا حتی *نوشتن* فایل های iso خود بر روی یک دیسک USB برای داشتن یک USB قابل بوت زنده:

```
$ sudo dd if=ubuntu.iso of=/dev/sdc bs=2048
```

> احتیاط: در اینجا شما مستقیماً روی یک دستگاه بلوک می نویسید. اگر کار اشتباهی انجام دهید ... دیسک خود را خراب می کنید و باید آن را دوباره فرمت کنید.
#### **پیدا کردن**
دستور `find` به ما کمک می کند تا فایل ها را بر اساس معیارهای مختلف پیدا کنیم. به این نگاه کن:

```
$ find . -iname "[a-j]*"
./howcool.sort
./alldata
./mydir/howcool.sort
./mydir/newDir/insideNew
./howcool
```

* پارامتر اول می گوید کجا باید جستجو کنیم (از جمله زیر شاخه ها).
* سوئیچ `-name` معیارها را نشان می‌دهد (در اینجا `iname` به معنای جستجوی فایل‌های با این نام است و حروف حروف را نادیده می‌گیرید (z برابر است با Z)). 

سوئیچ رایج دیگر `-type` برای نشان دادن نوع مورد جستجوی ما است (`f` برای فایل های معمولی، `d` برای فهرست ها، و `l` برای پیوندهای نمادین):

```
jadi@lpicjadi:~/lpic1-practice-iso/100/103.3$ find . -type d -iname "[a-j]*"
./directory
./directory/innder_one
```

اگر می خواهید اندازه فایل ها را جستجو کنید به صورت زیر عمل کنید:

| فرمان | معنی |
| :--- | :--- |
| -سایز 100c | فایل هایی که دقیقا 100 کاراکتر/بایت هستند (می توانید از `b` نیز استفاده کنید) |
| -سایز +100k | فایل های بیش از 100 کیلوبایت |
| -سایز -20M | فایل های کوچکتر از 20 مگابایت |
| اندازه +2G | فایل های بزرگتر از 2 گیگابایت |

بنابراین تمام فایل‌هایی که به _tmp_ ختم می‌شوند را با اندازه‌های بین 1 تا 100 مگابایت در فهرست /var/ پیدا می‌کند:

```text
find /var -iname '*tmp' -size +1M -size -100M
```

> می‌توانید همه فایل‌های خالی را با `find . -size 0b` یا `find . -empty` پیدا کنید

یکی دیگر از معیارهای جستجوی مفید زمان است. اینها برخی از گزینه ها هستند:

| سوئیچ | معنی | نمونه ها |
| :--- | :--- | :--- |
| -امین | دقیقه دسترسی | `-amin 40` به معنای "فایل هایی است که دقیقاً 40 دقیقه قبل به آن ها دسترسی پیدا کرده اند" یا `-amin +40` فایل هایی که بیش از 40 دقیقه پیش به آن ها دسترسی پیدا کرده اند و `-amin -40` به معنای فایل هایی است که کمتر از 40 دقیقه پیش به آن ها دسترسی یافته اند|
| -cm | حداقل تغییر وضعیت | `-cmin +60` وضعیت فایل قبل از آخرین ساعت تغییر کرد |
| -mmin | صورتجلسه اصلاح شده | `-mmin -60` فایل های اصلاح شده در ساعت گذشته را به ما می دهد |
| -atime | زمان دسترسی به روز | `-atime +1` یعنی دسترسی به فایل "بیش از 1 روز پیش (یعنی 2 روز و بیشتر)|
| -ctime | تغییر وضعیت در چند روز ||
| -mtime | روزهای اصلاح شده | |
| -جدیدتر | جدیدتر از مرجع | `-newer file1` به شما فایل هایی می دهد که جدیدتر از file1 |


> اگر سوئیچ `-daystart` را به -mtime یا -atime اضافه کنید، به این معنی است که می خواهیم روزها را به عنوان روزهای تقویم در نظر بگیریم که از نیمه شب شروع می شود.


#### اقدام بر روی فایل ها

ما می‌توانیم با سوئیچ‌های مختلف، دستورات را اجرا کنیم یا اقدامات دیگری را روی فایل‌ها انجام دهیم:

| سوئیچ | معنی |
| :--- | :--- |
| -ls | ls -dils را روی هر فایل اجرا می کند |
| -چاپ | نام کامل فایل ها را در هر خط چاپ می کند |

اما بهترین راه برای اجرای دستورات روی فایل های یافت شده سوئیچ `-exec` است. می‌توانید با `'{}'` یا `{}` به فایل اشاره کنید و دستور خود را با `\;` تمام کنید.

به عنوان مثال، این همه فایل های خالی این فهرست و زیرشاخه های آن را حذف می کند:

```
find . -empty -exec rm '{}' \;
```

یا با این کار نام تمام فایل های htm به html تغییر می کند

```
find . -name "*.htm" -exec mv '{}' '{}l' \;
```
> از آنجایی که حذف فایل های یافت شده یک کار رایج است، یک سوئیچ برای آن وجود دارد: `-delete`


<iframe width="560" height="315" src="https://www.youtube.com/embed/6MLaCDTRgis" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### فشرده سازی
#### **gzip & gunzip**
مستقیم به جلو، یک فایل gzips و یک فایل ungzips. در محل:
```
jadi@lpicjadi:~/lpic1-practice-iso/100/103.3$ ls -ltrh
total 20K
-rw-rw-r-- 1 jadi jadi  207 Aug 14 04:43 tasks.txt
-rw-rw-r-- 1 jadi jadi   29 Aug 14 04:43 info.txt
-rw-rw-r-- 1 jadi jadi   24 Aug 14 04:44 data.txt
-rw-rw-r-- 1 jadi jadi    0 Aug 14 05:08 new_file
-rw-rw-r-- 1 jadi jadi  116 Aug 14 05:08 note_to_self
drwxrwxr-x 3 jadi jadi 4.0K Aug 14 05:20 directory
jadi@lpicjadi:~/lpic1-practice-iso/100/103.3$ ls -ltrh
total 20K
-rw-rw-r-- 1 jadi jadi  171 Aug 14 04:43 tasks.txt.gz
-rw-rw-r-- 1 jadi jadi   29 Aug 14 04:43 info.txt
-rw-rw-r-- 1 jadi jadi   24 Aug 14 04:44 data.txt
-rw-rw-r-- 1 jadi jadi    0 Aug 14 05:08 new_file
-rw-rw-r-- 1 jadi jadi  116 Aug 14 05:08 note_to_self
drwxrwxr-x 3 jadi jadi 4.0K Aug 14 05:20 directory
jadi@lpicjadi:~/lpic1-practice-iso/100/103.3$ gunzip tasks.txt.gz
jadi@lpicjadi:~/lpic1-practice-iso/100/103.3$ ls -ltrh
total 20K
-rw-rw-r-- 1 jadi jadi  207 Aug 14 04:43 tasks.txt
-rw-rw-r-- 1 jadi jadi   29 Aug 14 04:43 info.txt
-rw-rw-r-- 1 jadi jadi   24 Aug 14 04:44 data.txt
-rw-rw-r-- 1 jadi jadi    0 Aug 14 05:08 new_file
-rw-rw-r-- 1 jadi jadi  116 Aug 14 05:08 note_to_self
drwxrwxr-x 3 jadi jadi 4.0K Aug 14 05:20 directory
```

* gzip زمان را حفظ می کند
* gzip فایل فشرده جدیدی را با همین نام اما با انتهای gz. ایجاد می کند
* gzip فایل های اصلی را پس از ایجاد فایل فشرده حذف می کند (می توانید فایل ورودی را با سوئیچ `-k` نگه دارید)



#### **bzip2 و bunzip2**

`bzip2` یکی دیگر از ابزارهای فشرده سازی است. درست مانند `gzip` معروف اما با الگوریتم فشرده سازی متفاوت کار می کند.

```
jadi@lpicjadi:~/lpic1-practice-iso/100/103.3$ bzip2 tasks.txt
jadi@lpicjadi:~/lpic1-practice-iso/100/103.3$ ls  -ltrh
total 20K
-rw-rw-r-- 1 jadi jadi  172 Aug 14 04:43 tasks.txt.bz2
-rw-rw-r-- 1 jadi jadi   29 Aug 14 04:43 info.txt
-rw-rw-r-- 1 jadi jadi   24 Aug 14 04:44 data.txt
-rw-rw-r-- 1 jadi jadi    0 Aug 14 05:08 new_file
-rw-rw-r-- 1 jadi jadi  116 Aug 14 05:08 note_to_self
drwxrwxr-x 3 jadi jadi 4.0K Aug 14 05:20 directory
jadi@lpicjadi:~/lpic1-practice-iso/100/103.3$ bunzip2 tasks.txt.bz2
jadi@lpicjadi:~/lpic1-practice-iso/100/103.3$ ls
data.txt  directory  info.txt  new_file  note_to_self  tasks.txt
```

#### **xz & unxz**

یکی دیگر از ابزارهای فشرده سازی/فشرده سازی درست مانند `gzip` و `bzip2` است. 

```
jadi@lpicjadi:~/lpic1-practice-iso/100/103.3$ xz tasks.txt
jadi@lpicjadi:~/lpic1-practice-iso/100/103.3$ ls -ltrh
total 24K
-rw-rw-r-- 1 jadi jadi  224 Aug 14 04:43 tasks.txt.xz
-rw-rw-r-- 1 jadi jadi   29 Aug 14 04:43 info.txt
-rw-rw-r-- 1 jadi jadi   24 Aug 14 04:44 data.txt
-rw-rw-r-- 1 jadi jadi  116 Aug 14 05:08 note_to_self
drwxrwxr-x 3 jadi jadi 4.0K Aug 14 05:20 directory
-rw-rw-r-- 1 jadi jadi  116 Aug 14 07:51 new_file
jadi@lpicjadi:~/lpic1-practice-iso/100/103.3$ unxz tasks.txt.xz
jadi@lpicjadi:~/lpic1-practice-iso/100/103.3$ ls -ltrh
total 24K
-rw-rw-r-- 1 jadi jadi  207 Aug 14 04:43 tasks.txt
-rw-rw-r-- 1 jadi jadi   29 Aug 14 04:43 info.txt
-rw-rw-r-- 1 jadi jadi   24 Aug 14 04:44 data.txt
-rw-rw-r-- 1 jadi jadi  116 Aug 14 05:08 note_to_self
drwxrwxr-x 3 jadi jadi 4.0K Aug 14 05:20 directory
-rw-rw-r-- 1 jadi jadi  116 Aug 14 07:51 new_file
```

لطفاً توجه داشته باشید که *فشرده کردن* یک فایل متنی کوچک آن را بزرگتر می کند. این امر در فایل‌های کوچک *طبیعی* است زیرا همه سرصفحه‌ها و ابرداده‌ها هستند.

> در برخی موارد، دستوراتی مانند `unxz` فقط یک تماس با `xz --dcompress` است.

### بایگانی با tar & cpio

گاهی اوقات ما نیاز به ایجاد یک محفظه فایل آرشیو از بسیاری از فایل های دیگر داریم. این عملیات با فشرده سازی متفاوت است، فایل ها را در یکی ترکیب می کند و سپس دوباره آنها را استخراج می کند. آرشیو بیشتر در پشتیبان گیری، انتقال فایل ها به مکان جدید (مثلاً از طریق ایمیل) و مواردی از این دست استفاده می شود. این کار با `cpio` و `tar` انجام می شود.

#### **تار**

TapeARchive یا tar رایج ترین ابزار بایگانی است. به طور خودکار یک فایل بایگانی را از یک دایرکتوری (پوشه) و همه زیرشاخه های آن ایجاد می کند.

سوئیچ های رایج عبارتند از:

| سوئیچ | معنی |
| :--- | :--- |
| -cf `myarchive.tar` | ایجاد فایل با نام myarchive.tar |
| -xf `myarchive.tar` | فایلی به نام myarchive.tar | را استخراج کنید
| -z | پس از ایجاد آرشیو با gzip فشرده کنید
| -j | پس از ایجاد آرشیو با bzip2 آن را فشرده کنید
| -v | پر حرف! اطلاعات زیادی در مورد آنچه اتفاق می افتد چاپ کنید |
| -r | فایل های جدید را به آرشیو موجود در حال حاضر اضافه کنید |

> اگر مسیرهای مطلق صادر می کنید، tar به دلایل ایمنی هنگام ایجاد بایگانی، اسلش شروع \(/\) را حذف می کند. اگر می خواهید لغو کنید، از گزینه -p استفاده کنید.
>
> تار می تواند با نوارها و سایر انبارها کار کند. به همین دلیل است که از `-f` استفاده می کنیم تا به آن بگوییم که با فایل ها کار می کنیم.

#### **cpio**

لیستی از فایل ها را دریافت می کند و یک آرشیو (یک فایل) ایجاد می کند. این فایل می تواند بعدا برای استخراج فایل های اصلی استفاده شود.

```
$ ls | cpio -o > allfilesls.cpio
3090354 blocks
```

* `-o` به cpio می گوید که از ورودی خود خروجی ایجاد کند

لطفاً توجه داشته باشید که `cpio` به پوشه ها نگاه نمی کند. بنابراین بیشتر ما از آن با find استفاده می کنیم:

```
find . -name "*" | cpio -o > myarchivefind.cpio
```

برای استخراج فایل های اصلی:

```
mkdir extract
mv myarchivefind.cpio extract
cd extract
cpio -id < myarchivefind.cpio
```

* `-d` پوشه ها را ایجاد می کند
* `-i` برای استخراج است