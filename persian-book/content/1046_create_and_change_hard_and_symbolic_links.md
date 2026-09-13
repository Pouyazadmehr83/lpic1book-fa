Title: 104.6 پیوندهای سخت و نمادین ایجاد و تغییر دهید
Date: 2010-12-03 10:20
Category: LPIC1
Tags: LPIC1, 101, LPIC1-101-500
Authors: Jadi
sortorder: 250
Summary: 

_وزن: 2_

داوطلبان باید بتوانند پیوندهای سخت و نمادین یک فایل را ایجاد و مدیریت کنند.

### حوزه های دانش کلیدی

* ایجاد لینک
* لینک های سخت و/یا نرم افزاری را شناسایی کنید.
* کپی کردن در مقابل پیوند دادن فایل ها.
* از پیوندها برای پشتیبانی از وظایف مدیریت سیستم استفاده کنید.


* `ln`
* `unlink`

## لینک

در یک دستگاه ذخیره سازی، یک فایل یا دایرکتوری (پوشه) در یک بلوک ذخیره می شود و یک مرجع به آن در جدول تخصیص FAT، ext، ... در کنار داده های مربوط به مالک، مجوزها، آخرین زمان دسترسی به آن، اندازه آن و موارد دیگر ذخیره می شود. همانطور که می دانید، ما می توانیم این را با استفاده از دستور `ls` بررسی کنیم.

```
$ ls -i script.sh
785379 script.sh
$ ls -l script.sh
-rwxr--r-t 1 jadi adm 34 Mar  5 13:38 script.sh
$ ls -R
.:
check_tr181_file.php  etc_apparmom.tar  index.html  php_checker  script.sh  test.csv  w

./php_checker:
check_tr181_file.php  index.html  test.csv

./w:
```

اما امکان ایجاد لینک نیز وجود دارد. پیوند به سادگی یک ورودی فهرست اضافی برای یک فایل یا فهرست است:

```
$ ls -l
total 4
-rwxr-xr-x 1 jadi adm 34 Mar  5 13:38 script.sh
$ ln -s script.sh copy_of_script.sh
$ ls -ltrh
total 4.0K
-rwxr-xr-x 1 jadi adm  34 Mar  5 13:38 script.sh
lrwxrwxrwx 1 jadi jadi  9 Mar  6 11:31 copy_of_script.sh -> script.sh
$ ls -i
785349 copy_of_script.sh  785379 script.sh
```

یک پیوند به سادگی یک ورودی فهرست اضافی برای یک فایل یا فهرست است که دو یا چند نام را برای یک فایل مجاز می کند. **پیوند سخت (Hard Link)** یک ورودی دایرکتوری (پوشه) است که به یک inode اشاره می کند، در حالی که **پیوند نرم یا پیوند نمادین (Symbolic Link)** ورودی دایرکتوری (پوشه) است که به یک inode اشاره می کند که نام ورودی دایرکتوری (پوشه) دیگری را ارائه می دهد. مکانیسم دقیق ذخیره نام دوم ممکن است به سیستم‌فایل (Filesystem) و طول نام بستگی داشته باشد. به پیوندهای نمادین، پیوندهای نمادین نیز می گویند.

پیوندهای نرم یا پیوندهای نمادین، صرفاً به فایل یا دایرکتوری (پوشه) دیگری با نام اشاره می کنند و نه با inode. پیوندهای نرم می توانند از مرزهای سیستم‌فایل (Filesystem) عبور کنند.

```
$ vi new_file
$ ls -ltrh
total 4.0K
-rw------- 1 jadi jadi 9 Mar  6 11:37 new_file
$ ln new_file hard_link
$ ln -s new_file soft_link
$ ls -ltrh
total 8.0K
-rw------- 2 jadi jadi 9 Mar  6 11:37 new_file
-rw------- 2 jadi jadi 9 Mar  6 11:37 hard_link
lrwxrwxrwx 1 jadi jadi 8 Mar  6 11:37 soft_link -> new_file
$ rm new_file
$ ls -ltrh
total 4.0K
-rw------- 1 jadi jadi 9 Mar  6 11:37 hard_link
lrwxrwxrwx 1 jadi jadi 8 Mar  6 11:37 soft_link -> new_file
$ cat hard_link
new file
$ cat soft_link
cat: soft_link: No such file or directory
```

> وقتی یک پیوند نمادین (Symbolic Link) داریم، به `l` به عنوان اولین کاراکتر در لیست مجوزهای `ls -l` توجه کنید.

شما می توانید لینک های سخت را فقط برای فایل ها ایجاد کنید، نه برای دایرکتوری (پوشه) ها. استثنا، ورودی های دایرکتوری (پوشه) ویژه در یک فهرست برای خود دایرکتوری (پوشه) و برای والد آن \(`.` و `..`\) است.



> اگر بخواهید پیوندهای سختی را ایجاد کنید که از سیستم های فایل متقاطع یا برای دایرکتوری (پوشه) ها هستند، با خطا مواجه می شوید.

```
$ ln mydir link2dir # ln: mydir: hard link not allowed for director
$ ln -s mydir link2dir # works just fine
```

اگر از نام‌های نسبی استفاده می‌کنید، معمولاً می‌خواهید فهرست کاری فعلی دایرکتوری (پوشه) باشد که در آن پیوند ایجاد می‌کنید. در غیر این صورت، پیوندی که ایجاد می کنید، نسبت به نقطه دیگری از سیستم‌فایل (Filesystem) خواهد بود.

```
$ ln -s myfile.txt mydir/ #broken link
$ cd mydir 
$ ln -s ../myfile.txt .
```

توصیه می شود از مسیر دقیق برای پیوندها استفاده کنید.

```
$ ln -s /tmp/myfile.txt /tmp/Foo/Bar/myfile.txt
$ ls -l /tmp/Foo/Bar/myfile.txt 
lrwxrwxrwx. 1 jadi jadi 9 Mar  6 12:37 /tmp/Foo/Bar/myfile.txt -> /tmp/myfile.txt

```

ما می توانیم پیوندهای نمادین را با استفاده از دستور `find` پیدا کنیم:

```
$ find . -type l
```

آنها برای نگه داشتن یک نام خاص که به یک نام باینری در حال تغییر اشاره دارد بسیار استفاده می شوند. به عنوان مثال، ما همیشه باید بتوانیم `python3` را اجرا کنیم، بنابراین آن را به آخرین پایتون نصب شده در سیستم نشان می دهیم:

```
$ which python3
/usr/bin/python3
$ ls -l /usr/bin/python3
lrwxrwxrwx 1 root root 10 Mar 25  2022 /usr/bin/python3 -> python3.10
```

برای حذف پیوندها، می توانید از دستور `rm` یا `unlink` استفاده کنید.