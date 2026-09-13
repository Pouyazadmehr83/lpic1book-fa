Title: 107.1 حساب های کاربری و گروه و فایل های سیستم مربوطه را مدیریت کنید
Date: 2010-12-03 10:20
Category: LPIC1
Tags: LPIC1, 102, LPIC1-102-500
Authors: Jadi
sortorder: 330
Summary: 

_وزن: 5_

نامزدها باید بتوانند حساب های کاربری را اضافه، حذف، تعلیق و تغییر دهند.

### حوزه های دانش کلیدی

* اضافه کردن، تغییر و حذف کاربران و گروه ها.
* اطلاعات کاربر/گروه را در پایگاه داده های گذرواژه/گروه مدیریت کنید.
* ایجاد و مدیریت حساب های کاربری خاص و محدود.

### شرایط و امکانات

* `/etc/passwd`
* `/etc/shadow`
* `/etc/group`
* `/etc/skel/`
* `chage`
* `getent`
* `groupadd`
* `groupdel`
* `groupmod`
* `passwd`
* `useradd`
* `userdel`
* `usermod`

<iframe width="560" height="315" src="https://www.youtube.com/embed/xXQ1pw2sAQs" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## رمزهای عبور
### تغییر رمزهای عبور
هر کاربر می تواند رمز عبور خود را با استفاده از دستور `passwd` تغییر دهد:

```text
$ passwd
Changing password for jadi.
(current) UNIX password:
New password:
Retype new password:
passwd: password updated successfully
```

اگر رمز عبور خیلی کوتاه یا خیلی شبیه به رمز قبلی یا حتی یک کلمه فرهنگ لغت یا برابر با نام کاربری و مواردی از این قبیل باشد، ممکن است دستور `passwd` از تغییر آن امتناع کند. همچنین توجه داشته باشید که دستورات `passwd` ابتدا رمز عبور _current_ را درخواست می کند تا مطمئن شوید که توسط خودتان تغییر داده شده است. 

> کاربر اصلی می تواند رمز عبور هر کاربر را بدون ارائه رمز عبور فعلی خود به هر چیزی \(گذرواژه ضعیف\) تغییر دهد:

```text
# passwd jadi
New password:
BAD PASSWORD: it does not contain enough DIFFERENT characters
BAD PASSWORD: is too simple
Retype new password:
passwd: password updated successfully
```

## کاربران و گروه ها

لینوکس یک سیستم چند کاربره است و مدیریت این کاربران بخشی از کار ادمین سیستم است. به عنوان اولین گام، باید بتوانید کاربران را **افزودن**، *حذف** و *تغییر*********نویسی کنید.

لینوکس مفهوم **گروه** را نیز دارد. می توانید گروه ها را تعریف کنید، به آنها امتیاز دهید و کاربران را به این گروه ها اضافه کنید. همانطور که قبلاً در دستور `chmod` مشاهده کردید، ممکن است اجازه دسترسی به خواندن از `/dev/cdrom` را به گروهی به نام `cdrom` بدهید و سپس هرکسی را که نیاز به خواندن از CD-ROM دارد به این گروه اضافه کنید.

لطفاً توجه داشته باشید که هر کاربر می‌تواند عضو بسیاری از گروه‌ها باشد، اما تنها یکی از آنها گروه *اصلی* او خواهد بود. در مقابل، هر فایل فقط می تواند متعلق به یک گروه باشد.
### مدیریت کاربران
#### اضافه کردن کاربران

برای افزودن یک کاربر جدید به سیستم خود، از دستور `useradd` استفاده کنید. اینها کلیدهای اصلی هستند:

| سوئیچ | معنی |
| :--- | :--- |
| -d | فهرست اصلی \(-d /home/user\) |
| -m | ایجاد فهرست خانه |
| -s | مشخص کردن پوسته |
| -G | افزودن به گروه های اضافی |
| -c | نظر دادن بیشتر اوقات، نام واقعی کاربران. اگر نظرات دارای فاصله یا کاراکترهای خاص هستند از نقل قول استفاده کنید |

در برخی از سیستم‌ها `useradd` فهرست اصلی را ایجاد می‌کند و در برخی، باید سوئیچ `-m` را خودتان مشخص کنید. استفاده مداوم از آن تمرین خوبی است.

هنگامی که یک فهرست کاربری جدید ایجاد می شود، سیستم محتویات `/etc/skel` را در آدرس خانه آنها کپی می کند. `/etc/skel` به عنوان یک الگو برای خانه کاربران استفاده می شود.

> دستور دیگری برای افزودن کاربران `adduser` است. رمز عبور، دایرکتوری (پوشه) خانه و غیره را می خواهد و کاربر را ایجاد می کند.

#### تغییر کاربران

برای تغییر کاربری، باید از دستور `usermod` استفاده کنید. از اکثر سوئیچ های `useradd` پشتیبانی می کند. برای مثال می‌توانید پوسته ورود _jadi_ را با صدور `usermod -s /bin/csh jadi` تغییر دهید. اما 3 سوئیچ دیگر نیز وجود دارد:

| سوئیچ | معنی |
| :--- | :--- |
| -L | قفل این حساب |
| -U | باز کردن قفل حساب |
| -aG | به گروه های بیشتر اضافه کنید \(مثلا `usermod -aG wheel jadi`\) |

> توجه: اگر `usermod -G wheel,users jadi` را انجام دهید، jadi فقط عضو این دو گروه خواهد بود. به همین دلیل است که از `-aG newgoup` برای *افزودن به گروه ها* استفاده می کنیم تا این گروه را به گروه های jadi اضافه کنیم. `-G` مانند این است که بگویید "گروه های jadi ... هستند" و `-aG` مانند "جادی را به این گروه ها نیز اضافه کنید".

#### حذف کاربران

اگر می‌خواهید کاربری را حذف کنید، از `userdel` استفاده کنید. مستقیم به جلو:

```text
userdel jadi
```

اگر سوئیچ `-r` را اضافه کنید، فهرست اصلی و قرقره نامه نیز پاک می شوند!

### مدیریت گروه ها

این مانند کاربران است، می توانید `groupadd`، `groupdel` و `groupmod` را انجام دهید. هر گروه یک *id* و یک *نام* دارد.

```text
# groupadd -g 1200 newgroup
```

گروهی به نام _newgroup_ با شناسه 1200 اضافه می کند. در صورت نیاز، کاربر ریشه می تواند با صدور `groupmod -g 2000 newgroup` یا حذف گروه توسط `groupdel newgroup`، شناسه گروه \(به 2000\) را تغییر دهد.

بدیهی است که اگر روت گروهی را با اعضا حذف کند، افراد حذف نخواهند شد! آنها دیگر عضو آن گروه نخواهند بود.

> در اکثر سیستم ها، شناسه کاربری یا شناسه گروه کاربران و گروه های ایجاد شده توسط ادمین دارای شناسه 1000، 1001، 1002، ...


### فایل های مربوط به کاربران و گروه ها
<iframe width="560" height="315" src="https://www.youtube.com/embed/V69h5V5wdTw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

#### `/etc/passwd`

این فایل شامل تمام اطلاعات کاربر در سیستم شما است:

```text
tail /etc/passwd
scard:x:491:489:Smart Card Reader:/var/run/pcscd:/usr/sbin/nologin
sshd:x:493:491:SSH daemon:/var/lib/sshd:/bin/false
statd:x:488:65534:NFS statd daemon:/var/lib/nfs:/sbin/nologin
tftp:x:496:493:TFTP account:/srv/tftpboot:/bin/false
lightdm:x:10:14:Light Display Manager:/var/lib/lightdm:/bin/false
wwwrun:x:30:8:WWW daemon apache:/var/lib/wwwrun:/bin/false
jadi:x:1000:100:jadi:/home/jadi:/bin/bash
svn:x:485:482:user for Apache Subversion svnserve:/srv/svn:/sbin/nologin
privoxy:x:484:480:Daemon user for privoxy:/var/lib/privoxy:/bin/false
```

همانطور که می بینید فرمت این است:

```text
username:x:userid:primary group id:Name and comments:home dir:shell
```

همانطور که می بینید، فیلد دوم به صورت "`x`" در اینجا نشان داده شده است. در قدیم رمز عبور یا رمز عبور هش شده کاربر در این فایل نشان داده می شد اما امروزه به فایل `/etc/shadow` منتقل شده است.

> توجه: /etc/passwd باید برای همه کاربران قابل خواندن باشد و این باعث می شود که مکان بسیار بدی برای حفظ رمز عبور کاربران باشد! به همین دلیل است که به جای رمز عبور، یک `x` می بینیم، این نشان می دهد که رمزهای عبور اصلی باید از فایل `/etc/shadow` جستجو شوند.

توجه داشته باشید که چگونه کاربران _ویژه_ مانند `lightdm` `/bin/false` را به عنوان پوسته خود دارند. این مانع از ورود واقعی آنها به سیستم می شود. در زمان های قدیم هکرها از این حساب ها برای ورود استفاده می کردند.

#### `/etc/shadow`

این فایل حاوی رمز عبور \(رمزهای هش شده\) کاربران است. ببینید چگونه `/etc/passwd` برای همه قابل خواندن است اما `/etc/shadow` فقط برای root و اعضای گروه `shadow` قابل خواندن است:

```text
# ls -ltrh /etc/passwd /etc/shadow
-rw-r--r-- 1 root root   1.9K Oct 28 15:47 /etc/passwd
-rw-r----- 1 root shadow  851 Oct 29 19:06 /etc/shadow
```

اما در آن چیست؟

```text
# tail /etc/shadow
scard:!:16369::::::
sshd:!:16369::::::
statd:!:16369::::::
tftp:!:16369::::::
uucp:*:16369::::::
lightdm:*:16369::::::
jadi:$6$enk5I3bv$uSQrRpen7m9xDapYLgwgh3P/71OLZUgj31n8AwzgIM2lA5Hc/BmRVAMC0eswdBGkseuXSvmaz0lsYFtduvuqUo:16737:0:99999:7:::
svn:!:16736::::::
privoxy:!:19473::::::
```


عجب! Jadi یک رمز عبور رمزگذاری شده در آنجا دارد. برخی اعداد نیز از آن رمز عبور رمزگذاری شده پیروی می کنند: **`16737:0:99999:7:::`**. یعنی چی؟ جدول زیر به شما می گوید.

| ثبت شده | معنی |
| :--- | :--- |
| 19473 | آخرین باری که این رمز عبور تغییر کرده کی بوده است |
| 0 | کاربر نمی تواند 0 روز پس از هر تغییر رمز عبور را تغییر دهد |
| 99999 | پس از این چند روز، کاربر باید رمز عبور خود را تغییر دهد |
| 7 | ...و 7 روز قبل از انقضا به کاربر اطلاع داده می شود که رمز عبور خود را تغییر دهد |

> توجه: اعداد "روزهای پس از 1 ژانویه 1970" یا زمان دوره به روز هستند. به عنوان مثال 16737 یعنی 16737 روز پس از 1 ژانویه 1970. عجیب اما کاربردی!

اما نیازی نیست که این عدد عجیب را به صورت دستی تغییر دهیم. در صورت نیاز، می‌توانیم از ابزار `chage` برای تغییر این اعداد استفاده کنیم. اگر `chage jadi` را صادر کنید، سیستم تمام پارامترها را یکی یکی از شما می خواهد. همچنین می توان از سوئیچ ها برای تغییر پارامترهای خاص در خط فرمان (Command Line) استفاده کرد.

| سوئیچ | معنی |
| :---: | :--- |
| -l | اطلاعات فهرست |
| -E | تاریخ انقضا را تنظیم کنید. تاریخ می تواند یک عدد باشد، در قالب YYYY-MM-DD یا -1 که به معنای _هرگز_ خواهد بود |

```text
# chage -l jadi
Last password change                    : Apr 26, 2023
Password expires                    : never
Password inactive                    : never
Account expires                        : never
Minimum number of days between password change        : 0
Maximum number of days between password change        : 99999
Number of days of warning before password expires    : 7
```
> توجه: `!` به این معنی است که حساب قفل شده است و کاربر نمی تواند با استفاده از حساب وارد سیستم شود. در برخی از سیستم‌ها (مانند RedHat) ممکن است `!!` را نیز ببینید که به این معنی است که حساب هرگز استفاده نشده است.

#### `/etc/group`

این فایل شامل گروه ها و شناسه آنها می باشد.

```text
# tail /etc/group
avahi:x:486:
kdm:!:485:
mysql:x:484:
winbind:x:483:
at:x:25:
svn:x:482:
vboxusers:x:481:
input:x:1000:jadi,joe
privoxy:x:480:
```

> توجه: می بینید که `x` آنجاست؟ از نظر تئوری گروه ها می توانند رمز عبور داشته باشند اما هرگز در هیچ توزیعی استفاده نمی شود! فایل `/etc/gshadow` است

### در حال بررسی اطلاعات کاربر

قبلاً `chage -l jadi` را دیدید اما دستورات بیشتری برای بررسی وضعیت کاربر وجود دارد. یکی `id` است:

```text
# id jadi
uid=1000(jadi) gid=100(users) groups=1000(input),100(users)
```

راه حل دیگر `getent` \(برای **دریافت ورودی**\) است. می‌تواند پایگاه‌های داده مهم را برای ورودی‌های خاص جستجو کند. این پایگاه داده ها شامل `/etc/passwd`، `/etc/hosts`، `/etc/shadow`، `/etc/group`، ...

```text
funlife:~ # getent group tor
tor:x:479:
funlife:~ # getent passwd jadi
jadi:x:1000:100:jadi:/home/jadi:/bin/bash
funlife:~ # getent shadow jadi
jadi:$6$enk5I3bv$uSQrRpen7m9xDapYLgwgh3P/71OLZUgj31n8AwzgIM2lA5Hc/BmRVAMC0eswdBGkseuXSvmaz0lsYFtduvuqUo:16737:0:99999:7:::
```