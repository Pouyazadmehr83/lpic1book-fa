Title: 103.2 جریان های متن را با استفاده از فیلترها پردازش کنید
Date: 2010-12-03 10:20
Category: LPIC1
Tags: LPIC1, 101, LPIC1-101-500
Authors: Jadi
Summary: داوطلبان باید بتوانند فیلترهایی را برای جریان متن اعمال کنند.
sortorder: 130

_وزن: 2_

توضیحات: داوطلبان باید بتوانند فیلترهایی را برای جریان متن اعمال کنند.

## اهداف

فایل‌های متنی و جریان‌های خروجی را از طریق فیلترهای ابزار متن ارسال کنید تا خروجی را با استفاده از دستورات استاندارد یونیکس موجود در بسته GNU textutils تغییر دهید.

## شرایط
* bzcat
* `cat`
* `cut`
* `head`
* `less`
* md5sum
* nl
* od
*رب
*سد
* sha256sum
* sha512sum
* `sort`
* `split`
* `tail`
* tr
* یونیک
* توالت فرنگی
* xzcat
* zcat

## جریان

<iframe width="560" height="315" src="https://www.youtube.com/embed/2mTH7HbErh8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

در دنیای **یونیکس** بسیاری از داده ها به صورت TEXT هستند. فایل‌های گزارش، پیکربندی‌ها، داده‌ها و غیره. **فیلتر کردن** این داده به معنای گرفتن جریان ورودی متن و انجام مقداری تبدیل روی متن قبل از ارسال آن به جریان خروجی است. در این زمینه، **جریان** چیزی بیش از _"توالی بایتی است که می توان با استفاده از توابع کتابخانه ای که جزئیات یک دستگاه زیرین را از برنامه مخفی می کند خوانده یا نوشت"_ نیست.

به عبارت ساده، جریان متن ورودی متنی از یک صفحه کلید، یک فایل، یک دستگاه شبکه و ... است که از طریق دستورات text util قابل مشاهده، تغییر، بررسی و ... است.

محیط‌ها و پوسته‌های برنامه‌نویسی مدرن \(از جمله bash\) از سه جریان ورودی/خروجی استاندارد (Standard Output - stdout) استفاده می‌کنند:

* **stdin** جریان ورودی استاندارد (Standard Input - stdin) است که ورودی دستورات را فراهم می کند.
* **stdout** جریان خروجی استاندارد (Standard Output - stdout) است که خروجی از دستورات را نمایش می دهد.
* **stderr** جریان خطای استاندارد (Standard Error - stderr) است که خروجی خطا از دستورات را نمایش می دهد

در اینجا ما در مورد **stdin** و مشاهده یا دستکاری آن از طریق دستورات و ابزارهای مختلف صحبت می کنیم. در مورد این جریان‌ها بیشتر خواهید دید و خواهید دید که چگونه می‌توانیم دستورات را با ورودی‌ها و خروجی‌های *PIPE* دستورات مختلف در فصل 103.4 ترکیب کنیم.

## مشاهده دستورات
### گربه

این دستور به سادگی جریان ورودی خود را \(یا نام فایلی که به آن می‌دهید\) خروجی می‌دهد. همانطور که در قسمت قبل دیدید. مانند اکثر دستورات، اگر ورودی به آن ندهید، داده ها را از صفحه کلید می خواند.

```text
jadi@funlife:~/w/lpic/101$ cat > mydata
test
this is the second line
bye
jadi@funlife:~/w/lpic/101$ cat mydata
test
this is the second line
bye
```

> هنگام وارد کردن ورودی از طریق صفحه کلید، `ctrl+d` جریان را پایان می دهد.

همچنین می‌توانید بیش از یک نام فایل ورودی ارائه دهید:

```text
jadi@funlife:~/w/lpic/101$ cat mydata directory_data
test
this is the second line
bye
total 0
-rw-rw-r-- 1 jadi jadi 0 Jan  4 17:33 12
-rw-rw-r-- 1 jadi jadi 0 Jan  4 17:33 62
-rw-rw-r-- 1 jadi jadi 0 Jan  4 17:33 neda
-rw-rw-r-- 1 jadi jadi 0 Jan  4 17:33 jadi
-rw-rw-r-- 1 jadi jadi 0 Jan  4 17:33 you
-rw-rw-r-- 1 jadi jadi 0 Jan  4 17:34 amir
-rw-rw-r-- 1 jadi jadi 0 Jan  4 17:37 directory_data
```

برخی از کلیدهای متداول گربه عبارتند از `-n` برای نشان دادن شماره خطوط، `-s` برای فشردن جاهای خالی، `-T` برای نشان دادن برگه ها، و `-v` برای نشان دادن کاراکترهای غیرچاپی.

### bzcat، xzcat، zcat، gzcat
برای مستقیم `cat` فایل های فشرده bz، xz، و Z و gz استفاده می شود. اینها به شما امکان می دهند محتویات فایل های فشرده را بدون اینکه ابتدا آنها را از حالت فشرده خارج کنید، مشاهده کنید.

### کمتر
این یک ابزار قدرتمند برای مشاهده فایل های متنی بزرگتر است. می تواند صفحه بندی، جستجو و حرکت در فایل های متنی را انجام دهد.

> دستور دیگری به نام `more` وجود دارد. برای افرادی که از محیط DOS می آیند بیشتر آشناست و در دنیای لینوکس چندان رایج نیست. از آن استفاده نکنید. به خاطر داشته باشید: `less` بیشتر از `more` است.

برخی از دستورات کمتر رایج به شرح زیر است.

|فرمان|استفاده|
|-|-|
|ق|خروج|
|/foo|جستجوی foo|
|n|بعدی (جستجو)|
|N|قبلی (جستجو)|
|?foo|جستجوی عقب برای foo|
|G|به پایان بروید|
|nG|به خط n بروید
|PageUp, PageDown, UpArrow, DownArrow | شما حدس بزنید!|

### od

این دستور _dump_s files \(فایل‌ها را در قالب‌هایی غیر از متن نشان می‌دهد. رفتار عادی OctalDump است \(نمایش در پایه 8\):

```text
jadi@funlife:~/w/lpic/101$ od mydata
0000000 062564 072163 072012 064550 020163 071551 072040 062550
0000020 071440 061545 067543 062156 066040 067151 005145 074542
0000040 005145
0000042
```

به اندازه کافی برای انسان های عادی خوب نیست. بیایید از چند سوئیچ استفاده کنیم:

* **-t** نشان می دهد که چه فرمتی چاپ شود:
  </br>`-t a` فقط برای نمایش نویسه‌های نام‌گذاری شده
  </br>`-t c` برای نمایش نویسه های فرار شده.</br>
می توانید دو مورد بالا را به `-a` و `-c` خلاصه کنید
* **-A** برای انتخاب نحوه ارائه فیلد افست: 
  </br> `-A d` برای اعشار،
  </br> `-A o` برای Octal،
  </br> `-A x` برای هگز 
  </br> `-A n` برای هیچکدام

> `od` برای یافتن مشکلات در فایل‌های متنی شما بسیار مفید است - بگویید که آیا از برگه‌ها استفاده می‌کنید یا انتهای خطوط درست است.

## انتخاب بخش هایی از فایل ها

<iframe width="560" height="315" src="https://www.youtube.com/embed/nw3Ic3RxbVI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### تقسیم

فایل ها را تقسیم می کند. این برای انتقال فایل های عظیم در رسانه های کوچکتر بسیار مفید است (مثلاً یک فایل 3 ترابایتی را به قطعات 8 گیگابایتی تقسیم کنید و آنها را به دستگاه دیگری با دیسک USB منتقل کنید).

```text
jadi@funlife:~/w/lpic/101$ cat mydata
hello
this is the second line
but as you can see we are
still writing
and this is getting longer
.
.
and longer
and longer!
jadi@funlife:~/w/lpic/101$ ls
mydata
jadi@funlife:~/w/lpic/101$ split -l 2 mydata
jadi@funlife:~/w/lpic/101$ ls
mydata    xaa  xab  xac  xad  xae
jadi@funlife:~/w/lpic/101$ cat xab
but as you can see we are
still writing
```

* به طور پیش فرض، split از xaa، xab، xac، ... برای نام فایل های خروجی استفاده می کند. می توان آن را با `split -l 2 mydata output` تغییر داد که mydata را به outputaa، outputab، ... تقسیم می کند. 2 خط در هر فایل
* `-l 2` 2 خط را در هر فایل تقسیم می کند. می توان از `-b 42` برای تقسیم هر 42 بایت یا حتی `-n 5` برای اجبار 5 فایل خروجی استفاده کرد.
* اگر خروجی عددی می خواهید \(x00, x01, ..\) از گزینه `-d` استفاده کنید.

> آیا باید به این فایل ها بپیوندید؟ `cat` آنها را با `cat x* > originalfile`.


### سر و دم
ابتدا (سر) یا انتهای (دم) فایل های متنی را نشان می دهد. به‌طور پیش‌فرض، 10 خط نشان داده می‌شود، اما می‌توانید آن را با `-n20` یا `-20` تغییر دهید.

> `tail -f` خطوط جدیدی را که در انتهای فایل نوشته می شود، دنبال می کند. بسیار مفید.

### برش

دستور `cut` یک یا چند ستون از یک فایل را برش می دهد. مناسب برای جداسازی فیلدها:

بیایید قسمت _first_ یک فایل را برش دهیم.

```text
jadi@funlife:~/w/lpic/101$ cat howcool
jadi    5
sina    6
rubic    2
you     12
jadi@funlife:~/w/lpic/101$ cut -f1 howcool
jadi
sina
rubic
you
```

> جداکننده پیش‌فرض TAB است. از `-dx` برای تغییر آن به "x" یا `-d' '` برای تغییر آن به فاصله استفاده کنید

همچنین می توان فیلدهای 1، 2، و 3 را با `-f1-3` یا فقط کاراکترهایی با نمایه 4، 5، 7، 8 از هر خط `-c4,5,7,8`_برش داد.


## تغییر جریان

<iframe width="560" height="315" src="https://www.youtube.com/embed/IpJpI3CzN_o" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### nl

این دستور برای نمایش شماره خطوط است.

```text
jadi@funlife:~/w/lpic/101$ nl mydata  | head -3
     1    hello
     2    this is the second line
     3    but as you can see we are
```

> `cat -n` همچنین خطوط را شماره گذاری می کند.

### مرتب سازی و یونیک

ورودی\(ها) خود را مرتب می کند.

```text
jadi@funlife:~/w/lpic/101$ cat uses
you fedora
jadi ubuntu
rubic windows
neda mac
jadi@funlife:~/w/lpic/101$ cat howcool
jadi    5
sina    6
rubic    2
you     12
jadi@funlife:~/w/lpic/101$ sort howcool uses
jadi    5
jadi ubuntu
neda mac
rubic    2
rubic windows
sina    6
you     12
```

اگر مرتب‌سازی معکوس می‌خواهید، از کلید `-r` استفاده کنید.

> اگر می‌خواهید NUMERICALLY \(بنابراین 9 کمتر از 19 باشد\) مرتب کنید، از `-n` استفاده کنید.

و `uniq` ورودی های تکراری را از ورودی خود حذف می کند. رفتار عادی فقط خطوط تکراری را حذف می کند، اما شما می توانید رفتار آن را تغییر دهید، برای مثال سوئیچ `-f1` آن را مجبور می کند که فیلد اول را بررسی نکند.

```text
jadi@funlife:~/w/lpic/101$ uniq what_i_have.txt
laptop
socks
tshirt
ball
socks
glasses
jadi@funlife:~/w/lpic/101$ sort what_i_have.txt | uniq
ball
glasses
laptop
socks
tshirt
jadi@funlife:~/w/lpic/101$
```

> همانطور که می بینید، ورودی باید مرتب شود تا uniq کار کند.

uniq سوئیچ های عالی دارد:

```text
jadi@funlife:~/w/lpic/101$ cat what_i_have.txt
laptop
socks
tshirt
ball
socks
glasses
jadi@funlife:~/w/lpic/101$ sort what_i_have.txt  | uniq -c  #show count of each item
      1 ball
      1 glasses
      1 laptop
      2 socks
      1 tshirt
jadi@funlife:~/w/lpic/101$ sort what_i_have.txt  | uniq -u #show only non-repeated items
ball
glasses
laptop
tshirt
jadi@funlife:~/w/lpic/101$ sort what_i_have.txt  | uniq -d #show only repeated items
socks
```

## خمیر

دستور paste خطوط دو یا چند فایل را در کنار هم قرار می دهد! شما نمی توانید این کار را در یک ویرایشگر متن عمومی به راحتی انجام دهید!

```text
jadi@funlife:~/w/lpic/101$ cat howcool
jadi    5
sina    6
rubic    2
you     12
jadi@funlife:~/w/lpic/101$ cat uses
you fedora
jadi ubuntu
rubic windows
neda mac
jadi@funlife:~/w/lpic/101$ paste howcool uses
jadi    5    you fedora
sina    6    jadi ubuntu
rubic    2    rubic windows
you     12    neda mac
```

### tr
دستور `tr` نویسه های موجود در جریان را _ترجمه می کند. به عنوان مثال، `tr 'ABC' '123'` A را با 1، B را با 2، و C را با 3 در جریان ارائه شده جایگزین می کند. این یک فیلتر خالص است و نام فایل ورودی را نمی پذیرد. در صورت نیاز می توانید گربه را با آن لوله کنید (به فصل 103.4 مراجعه کنید).

```text
jadi@funlife:~/w/lpic/101$ cat mydata
hello
this is the second line
but as you can see we are
still writing
and this is getting longer
.
.
and longer
and longer!
jadi@funlife:~/w/lpic/101$ cat mydata | tr 'and' 'AND'
hello
this is the second liNe
but As you cAN see we Are
still writiNg
AND this is gettiNg loNger
.
.
AND loNger
AND loNger!
```

> توجه: همه **'a'**ها با **'A'** جایگزین می شوند.


### sed

sed **s**tream **اد**itor است. این قدرتمند است و می تواند کارهایی انجام دهد که دور از جادو نیست! درست مانند بسیاری از ابزارهایی که تاکنون دیده‌ایم، sed می‌تواند به عنوان یک فیلتر کار کند یا ورودی یک فایل را بگیرد. Sed یک ابزار عالی برای جایگزینی متن با استفاده از **عبارات باقاعده (Regular Expressions - Regex)** است. اگر نیاز دارید A را با B فقط یک بار در هر خط در جریانی جایگزین کنید، فقط `sed 's/A/B/'` را صادر کنید:

```text
jadi@funlife:~/w/lpic/101$ cat uses
you fedora
jadi ubuntu
rubic windows
neda mac
jadi@funlife:~/w/lpic/101$ sed 's/ubuntu/debian/' uses
you fedora
jadi debian
rubic windows
neda mac
jadi@funlife:~/w/lpic/101$
```

الگوی تغییر هر رخداد A به B در یک خط، `sed 's/A/B/g'` است.

شخصیت های فرار را به خاطر دارید؟ آنها همچنین در اینجا کار می کنند و هر _new line_ را از یک فایل حذف می کند و آن را با یک فاصله جایگزین می کند:

```text
jadi@funlife:~/w/lpic/101$ cat mydata
hello
this is the second line
but as you can see we are
still writing
and this is getting longer
.
.
and longer
and longer!
jadi@funlife:~/w/lpic/101$ sed 's/ /\t/g' mydata > mydata.tab
jadi@funlife:~/w/lpic/101$ cat mydata.tab
hello
this    is the second    line
but    as    you    can    see    we    are
still    writing
and    this    is    getting    longer
.
.
and    longer
and    longer!
```

## دریافت آمار

<iframe width="560" height="315" src="https://www.youtube.com/embed/wUi0lmmzm3k" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### توالت فرنگی

`wc` _شمارش کلمه است. خطوط، کلمات و بایت ها را در جریان ورودی شمارش می کند.

```text
jadi@funlife:~/w/lpic/101$ wc mydata
  9  25 121 mydata
```

> شمارش شماره خطوط با سوئیچ `-l` بسیار رایج است.


### -

باید بدانید که اگر به جای نام فایل `-` را قرار دهید، داده ها از لوله \(یا صفحه کلید stdin\) جایگزین می شوند.

```text
jadi@funlife:~/w/lpic/101$ wc -l mydata | cat mydata - mydata  
hello
this is the second line
but as you can see we are
still writing
and this is getting longer
.
.
and longer
and longer!
9 mydata
hello
this is second line
but as you can see we are
still writing
and this is getting longer
.
.
and longer
and longer!
```

## هش کردن
تابع هش هر تابعی است که می تواند برای نگاشت داده های با اندازه دلخواه به مقادیر با اندازه ثابت استفاده شود. هش های مختلفی وجود دارد و ما از آنها برای اهداف مختلف استفاده می کنیم. به عنوان مثال، یک سایت ممکن است رمز عبور شما را در پایگاه داده خود هش کند تا آن را ایمن نگه دارد (و هش رمز عبور ارائه شده را با هشی که از قبل در DB دارد در هنگام ورود بررسی کنید) ممکن است یک سایت هش یک فایل را ارائه دهد تا مطمئن شوید که فایل صحیح را دانلود کرده اید و ...

الگوریتم های هش تحت پوشش LPIC1 عبارتند از:

- md5sum
- sha256sum
- sha512sum

می‌توانید هر فایلی (یا هش جریان‌های ورودی را با چیزی شبیه به این) بررسی کنید:

```
jadi@ocean:~$ md5sum /tmp/myfile.txt
8183aa57a23658efe7ba7aebe60816bc  /tmp/myfile.txt
jadi@ocean:~$ sha256sum /tmp/myfile.txt
7ddcfda184b55ee06b0c81e0ad136b1aa4a86daeb1078bcaeccc246eb2c8693b  /tmp/myfile.txt
jadi@ocean:~$ sha512sum /tmp/myfile.txt
79e5d789528e5e55fc1bddcb381afd56e896b1b452347a76777fb38d76c9754278700036f35df2a53c4d53d3e3623538a8b9ed155a3fd5275e667bdbf3c0b359  /tmp/myfile.txt
```

همانطور که می بینید، `sha512sum` هش طولانی تری ایجاد می کند که ایمن تر است.