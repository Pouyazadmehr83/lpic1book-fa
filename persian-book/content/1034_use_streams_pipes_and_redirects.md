Title: 103.4 از جریان ها، لوله ها و تغییر مسیرها استفاده کنید
Date: 2010-12-03 10:20
Category: LPIC1
Tags: LPIC1, 101, LPIC1-101-500
Authors: Jadi
Summary: 
sortorder: 150

_وزن: 4_

کاندیداها باید بتوانند جریان‌ها را ریدایرکت / تغییر مسیر (Redirection) داده و آنها را برای پردازش مؤثر داده‌های متنی متصل کنند. وظایف شامل ریدایرکت / تغییر مسیر (Redirection) ورودی استاندارد (Standard Input - stdin)، خروجی استاندارد (Standard Output - stdout) و خطای استاندارد (Standard Error - stderr)، پایپینگ / پایپ / لوله (Pipe) (Piping) خروجی یک دستور به ورودی دستور دیگر، استفاده از خروجی یک دستور به عنوان آرگومان برای دستور دیگر و ارسال خروجی به stdout و یک فایل است.


## اهداف
* ریدایرکت / تغییر مسیر (Redirection) ورودی استاندارد (Standard Input - stdin)، خروجی استاندارد (Standard Output - stdout) و خطای استاندارد (Standard Error - stderr).
* خروجی یک دستور را به ورودی فرمان دیگر لوله کنید.
* از خروجی یک دستور به عنوان آرگومان برای دستور دیگر استفاده کنید.
* خروجی را هم به stdout و هم به یک فایل ارسال کنید.

## شرایط
* سه راهی
* xargs

این ویژگی ها به ما کمک می کند تا ورودی/خروجی دستورات را کنترل کنیم و کارهایی مانند ذخیره خروجی یک دستور در یک فایل، دریافت ورودی یک دستور از دستور دیگر یا جداسازی خروجی عادی از خطاها را انجام دهیم. ما قبلاً از آنها در بخش های قبلی استفاده کرده ایم، اما بیایید بیشتر بیاموزیم و درک خود را از آنها عمیق تر کنیم.

<iframe width="560" height="315" src="https://www.youtube.com/embed/PeUhwMoSCko" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## ریدایرکت / تغییر مسیر (Redirection) IO استاندارد

در سیستم لینوکس، اکثر پوسته ها از جریان ها برای ورودی و خروجی استفاده می کنند. این استریم ها می توانند از (و به سمت) چیزهای مختلفی از جمله صفحه کلید، دستگاه‌های بلوکی (Block Devices) (هارد، USB، ..)، فایل ها و ... باشند.

ما 3 جریان استاندارد مختلف داریم:

<ol start="0">
<li><b>STDIN</b> جریان ورودی استاندارد (Standard Input - stdin) است که ورودی یک فرمان را ارائه می دهد.</li>
<li><b>STDOUT</b> جریان خروجی استاندارد (Standard Output - stdout) است که شامل خروجی یک فرمان است.</li>
<li><b>STDERR</b> جریان خطای استاندارد (Standard Error - stderr) است که شامل خروجی خطای یک فرمان است.</li>
</ol>

> شماره گذاری `0`، `1` و `2` بر این اساس ***STDIN***، ***STDOUT*** و ***STDERR** را نشان می دهد. به عنوان مثال، اگر می خواهید stderror را ریدایرکت / تغییر مسیر (Redirection) دهید، می توانید از 2> استفاده کنید و STDERR ریدایرکت / تغییر مسیر (Redirection) داده می شود.

اینها تغییر مسیرهای دیگری هستند که می توانید استفاده کنید:

|اپراتور|استفاده|
|--|--|
|>|STDOUT را به یک فایل هدایت کنید. بازنویسی در صورت وجود|
|>>|STDOUT را به یک فایل هدایت کنید. در صورت وجود پیوست کنید|
|2>|STDERR را به یک فایل هدایت کنید. بازنویسی در صورت وجود|
|2>>|STDERR را به یک فایل هدایت کنید. در صورت وجود پیوست کنید|
|&>|ریدایرکت / تغییر مسیر (Redirection) STDOUT و STDERR. بازنویسی در صورت وجود|
|&>>|ریدایرکت / تغییر مسیر (Redirection) STDOUT و STDERR; در صورت وجود پیوست کنید|
|<|ریدایرکت / تغییر مسیر (Redirection) STDIN از یک فایل|
|<>|STDIN را از فایل هدایت کنید و STDOUT را به آن ارسال کنید|

</br>
چند نمونه: 

```
$ ls
bob	jack	jadi	linus	sara who_uses_what.txt
$ ls x*
ls: x*: No such file or directory
$ ls j*
jack	jadi
$ ls j* x* > output 2> errors
$ cat output
jack
jadi
$ cat errors
ls: x*: No such file or directory
$ cat who_uses_what.txt
jadi, fedora
linux, fedora
bob, ubuntu
jack, arch
sara, fedora
$ tr ' ', '' < who_uses_what.txt
tr: empty string2
$ cat who
$ tr ',', '|' < who_uses_what.txt
jadi| fedora
linux| fedora
bob| ubuntu
jack| arch
sara| fedora
```

همچنین می توان از `&1` و `&2` و `&0` برای مراجعه به **هدف** STDOUT، STDERR و STDIN استفاده کرد. در این مورد `ls > file1 2>&1` به معنای _redirect خروجی به file1 و خروجی stderr به همان مکان stdout \(file1\)_ است.

> مراقب باش! `ls 2>&1 > file1` به معنای _print stderr در محل فعلی stdout (ترمینال) است و سپس stdout را به file1_ تغییر دهید.

#### ارسال به null

در لینوکس **/dev/null** دستگاه مانند یک پرتگاه کار می کند. شما می توانید هر چیزی را به آنجا بفرستید و بدون اینکه باری بر سیستم شما وارد شود ناپدید می شود. پس طبیعی است که بگوییم:

```
$ ls j* x* > file1
ls: x*: No such file or directory
$ ls j* x* > file1 2>/dev/null
$ cat file1
jack
jadi
```


#### در اینجا اسناد

بسیاری از پوسته‌ها اسناد here-docs (همچنین اینجا-docs نامیده می‌شوند) را به عنوان راهی برای ورودی دارند. شما از `<<` و یک `WORD` استفاده می کنید و سپس هر آنچه را که وارد می کنید، stdin در نظر گرفته می شود تا زمانی که فقط WORD را در یک خط بدهید.

```
$ tr ' ' '.' << END_OF_DATA
> this is a line
> and then this
>
> we'll still type
> and,
> done!
> END_OF_DATA
this.is.a.line
and.then.this

we'll.still.type
and,
done!
```

> اگر در حال نوشتن اسکریپت و کارهای خودکار هستید، اسناد اینجا بسیار مفید هستند.

<iframe width="560" height="315" src="https://www.youtube.com/embed/j3L_7Wxcl0U" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
### لوله ها

با لوله (`|`)، می‌توانید STDOUT، STDIN، و STDERR را بین چند دستور در یک خط فرمان (Command Line) هدایت کنید. وقتی `command1 | command2 ` را انجام می دهید؛ فرمان 1 اجرا می شود اما STDOUT آن به عنوان STDIN به COMMAND2 هدایت می شود. 


```
$ cat who_uses_what.txt
jadi, fedora
linux, fedora
bob, ubuntu
jack, arch
sara, fedora
$ cut -f2 -d, who_uses_what.txt | sed -e 's/ //g' | sort  | uniq -c | sort -nr
   3 fedora
   1 ubuntu
   1 arch
```

> اگر می‌خواهید پایپ / لوله (Pipe) خود را با محتوای یک فایل شروع کنید، با `cat filename | ...` شروع کنید یا از یک ریدایرکت / تغییر مسیر (Redirection) `<` stdin استفاده کنید.

لوله ها یکی از ویژگی های فوق العاده قوی و فوق العاده شگفت انگیز در دنیای یونیکس هستند. آنها به شما اجازه می دهند با ترکیب ابزارهایی که کارهای اتمی را انجام می دهند، ابزارهای *جدید* ایجاد کنید. به عنوان مثال، این را بررسی کنید:

<iframe width="560" height="315" src="https://www.youtube.com/embed/86V5amp1u7U" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### xargs

ابزار xargs رشته های فاصله، تب، خط جدید و انتهای فایل را از ورودی استاندارد (Standard Input - stdin) می خواند و ابزار ارائه شده را با رشته ها به عنوان آرگومان های آنها اجرا می کند.

```
$ ls
bob			file1			jadi			output			who_uses_what.txt
errors			jack			linus			sara
$ ls | xargs echo these are files:
these are files: bob errors file1 jack jadi linus output sara who_uses_what.txt
```

> اگر هیچ فرمانی به `xargs` ندهید، echo دستور پیش فرض خواهد بود. 

یکی از سوئیچ های رایج `-I` است. اگر بخواهید آرگومان های stdin را در وسط (یا حتی شروع) دستورات خود ارسال کنید، مفید است. از آن به این صورت استفاده کنید: `xargs -I SOMETHING echo here is SOMETHING end`:

```
$ cat who_uses_what.txt
jadi, fedora
linus, fedora
bob, ubuntu
jack, arch
sara, fedora
$ cat who_uses_what.txt | xargs -I DATA echo name is DATA is the choice.
name is jadi, fedora is the choice.
name is linus, fedora is the choice.
name is bob, ubuntu is the choice.
name is jack, arch is the choice.
name is sara, fedora is the choice.
```

دو سوئیچ مفید دیگر:
1. `-L 1` بر اساس خطوط جدید شکسته می شود 
2. `-n 1` به xargs می گوید که پس از دریافت 1 آرگومان، ابزار ارائه شده را فراخوانی کند.  

### سه راهی

مشکل ریدایرکت / تغییر مسیر (Redirection) این است که نمی توانید پیشرفت دستورات خود را در همان ترمینال ببینید. ابزار `tee` این مشکل را حل می کند. اگر باید خروجی را روی صفحه ببینید و همچنین آن را در یک فایل ذخیره کنید، `tee` دوست شماست. یک یا چند نام فایل به آن بدهید و این کار را انجام می دهد.

```
$ ls -1 | tee allfiles myfiles
bob
errors
file1
jack
jadi
linus
output
sara
who_uses_what.txt
$ cat allfiles myfiles
bob
errors
file1
jack
jadi
linus
output
sara
who_uses_what.txt
bob
errors
file1
jack
jadi
linus
output
sara
who_uses_what.txt
```
سوئیچ `-a` در صورت وجود به فایل‌ها اضافه می‌شود.

> اگر باید ***stderr*** را نیز ذخیره کنید، ابتدا آن را به ***stdout*** هدایت کنید.