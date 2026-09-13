Title: 110.1 انجام وظایف مدیریت امنیتی
Date: 2010-12-03 10:20
Category: LPIC1
Tags: LPIC1, 102, LPIC1-102-500
Authors: Jadi
sortorder: 450
Summary: 

_وزن: 3_

داوطلبان باید بدانند که چگونه پیکربندی سیستم را برای اطمینان از امنیت میزبان مطابق با سیاست های امنیتی محلی بررسی کنند.

### حوزه های دانش کلیدی

* یک سیستم را برای یافتن فایل‌های دارای مجموعه بیت suid/sgid حسابرسی کنید.
* رمز عبور کاربر و اطلاعات قدیمی رمز عبور را تنظیم یا تغییر دهید.
* امکان استفاده از nmap و netstat برای کشف پورت های باز در یک سیستم.
* برای ورود کاربران، فرآیندها و استفاده از حافظه محدودیت ایجاد کنید.
* تعیین کنید کدام کاربران وارد سیستم شده اند یا در حال حاضر وارد سیستم شده اند.
* پیکربندی و استفاده اولیه sudo.

### شرایط و امکانات

* `find`
* `passwd`
* `fuser`
* `lsof`
* `nmap`
* `chage`
* `netstat`
* `sudo`
* `/etc/sudoers`
* `su`
* `usermod`
* `ulimit`
* `who, w, last`


<iframe width="560" height="315" src="https://www.youtube.com/embed/rNxitwVtRvo" title="LPIC 1 - 77  - 110.1 (1/3) - Perform Security Admin Tasks;su,sudo,online users &amp;password management" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## کاربران

<iframe width="560" height="315" src="https://www.youtube.com/embed/rNxitwVtRvo?si=V6a_wAv84xjOIbjx" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

### `sudo` در مقابل `su`

ما عملاً در تمام فصل‌ها از `sudo` و `su` استفاده کرده‌ایم و اکنون زمان آن است که نگاه دقیق‌تری داشته باشیم! `su` شما را به حساب دیگری تغییر می دهد. یک "هویت کاربر جایگزین". پس از `su` موفقیت آمیز بودن `su` به آن حساب، یک درخواست جدید با حساب کاربری جدید دریافت می کنید:

```text
jadi@funlife ~$ whoami
jadi
jadi@funlife ~$ su -
Password:
root@funlife:~# whoami
root
root@funlife:~# su jadi -
jadi@funlife /root$ whoami
jadi
jadi@funlife /root$ exit
exit
root@funlife:~# whoami
root
root@funlife:~# exit
logout
jadi@funlife ~$ whoami
jadi
jadi@funlife ~$
```

توجه داشته باشید که هنگام اجرای `su` باید **رمز عبور root** را برای تبدیل شدن به روت ارائه دهید. یا هر رمز عبور کاربر دیگری برای تبدیل شدن به آن کاربر!

از طرف دیگر، sudo رمز عبور خود را می‌خواهد و دستوری را که به آن داده‌اید، با امتیازات root اجرا می‌کند. بنابراین `sudo ls` پس از درخواست **رمز عبور**، دستور ls را با امتیازات ریشه اجرا می کند. بدیهی است که شما باید حق _sudo_ را برای صدور sudo داشته باشید. این در فایل `/etc/sudoers` تعریف شده است:

```text
$ sudo cat /etc/sudoers
#
# This file MUST be edited with the 'visudo' command as root.
#
# Please consider adding local content in /etc/sudoers.d/ instead of
# directly modifying this file.
#
# See the man page for details on how to write a sudoers file.
#
Defaults    env_reset
Defaults    mail_badpass
Defaults    secure_path="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"

# Host alias specification

# User alias specification

# Cmnd alias specification

# User privilege specification
root    ALL=(ALL:ALL) ALL

# Members of the admin group may gain root privileges
%admin ALL=(ALL) ALL

# Allow members of group sudo to execute any command
%sudo    ALL=(ALL:ALL) ALL

# See sudoers(5) for more information on "#include" directives:

#includedir /etc/sudoers.d
```

به 2 خط مهم توجه کنید:

- چگونه root حق اجرای تمام دستورات را می گیرد:

  ```
  root    ALL=(ALL:ALL) ALL
  ```
- و اینکه چگونه گروه‌های sudo و admin حقوق اجرای دستورات را به عنوان root دریافت می‌کنند: 

  ```
  # Members of the admin group may gain root privileges
  %admin ALL=(ALL) ALL

  # Allow members of group sudo to execute any command
  %sudo    ALL=(ALL:ALL) ALL
  ```

  `ALL:ALL` به این معنی است که این کاربران می توانند به عنوان هر کاربر و هر گروهی اجرا شوند. آخرین ALL به sudo می گوید که این کاربران/گروه ها می توانند همه دستورات را اجرا کنند. این امکان وجود دارد که `/bin/ping` را در قسمت آخر قرار دهید تا به sudo بگویید که این کاربر فقط می تواند پینگ را به عنوان root اجرا کند، مانند زیر:

  ```
  username ALL=(ALL) /bin/ping
  ```

> فایل /etc/sudoers بسیار مهم است و شکستن آن مشکلات بزرگی ایجاد می کند. برای جلوگیری از اضافه کردن خطوط غیرقابل تفسیر در آن فایل، باید به جای `vi /etc/sudoers` از دستور `visudo` استفاده شود. این ابزار ویرایش های شما را بررسی می کند تا مطمئن شود که دستور sudo می تواند آنها را درک کند.

اکنون می دانیم `sudo su -` به چه معناست. sudo به سیستم می گوید که دستور `su -` را با دسترسی ریشه اجرا کند. اگر دسترسی sudo دارید، رمز عبور شما را می‌پرسد و `su -` را به عنوان ریشه اجرا می‌کند. دستورات `su` کاربر شما را به روت تغییر می دهد و سوئیچ `-` متغیرهای محیط ریشه را بارگیری می کند. به این ترتیب می توانید با استفاده از رمز عبور خود از طریق اجرای `su` با `sudo` تبدیل به روت شوید.

### بررسی کاربران در سیستم

اگر می خواهید بررسی کنید چه کسی در سیستم شما \(و تا حدودی چه کاری انجام می دهد\) می توانید از این دستورات استفاده کنید:

```text
$  w
 22:03:37 up 3 days,  5:33, 13 users,  load average: 1.48, 1.12, 1.19
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
jadi     tty7     :0               Wed16    3days  2:30m  1.96s /sbin/upstart --user
jadi     pts/18   :0               Wed16    3:04m  1:02   1:02  /usr/bin/python manage.py runserver 0.0.0.0:8000
jadi     pts/19   :0               Wed16    1:11m  0.35s  0.35s /bin/bash
root     tty2                      Wed16    3days  0.07s  0.03s -bash
jadi     pts/21   :0               08:41   45:37   0.06s  0.06s /bin/bash
jadi     pts/23   :0               Thu11   46:49   0.25s  0.23s ssh startups
jadi     pts/21   funlife          Fri22   45:37   0.06s  0.06s /bin/bash
jadi     pts/25   :0               10:17   31:37   0.07s  5.81s /usr/bin/python /usr/bin/x-terminal-emulator
jadi     pts/26   :0               21:39    0.00s  0.07s  0.00s w
jadi     pts/27   :0               21:55    8:09   0.01s  0.01s /bin/bash
```

شما یک خط برای هر کاربر وارد شده دارید \(هر پنجره پوسته یک ورود جداگانه است\).

دستور مفید دیگر `who` است. بیایید آن را بررسی کنیم:

```text
$ who
jadi     tty7         2016-06-01 16:30 (:0)
jadi     pts/17       2016-06-01 16:30 (funlife)
jadi     pts/2        2016-06-01 16:32 (:0)
jadi     pts/18       2016-06-01 16:32 (:0)
jadi     pts/19       2016-06-01 16:33 (:0)
root     tty2         2016-06-01 16:36
jadi     pts/21       2016-06-04 08:41 (:0)
jadi     pts/22       2016-06-01 18:37 (funlife)
jadi     pts/23       2016-06-02 11:41 (:0)
jadi     pts/21       2016-06-03 22:22 (funlife)
jadi     pts/25       2016-06-04 10:17 (:0)
jadi     pts/26       2016-06-04 21:39 (:0)
jadi     pts/27       2016-06-04 21:55 (:0)
```

همانطور که می بینید هر دو این دستورات به شما می گویند زمانی که کاربر وارد سیستم شده است اما افراد خارج شده را نشان نمی دهد \(زیرا آنها دیگر در سیستم نیستند!\). اگر به آن داده نیاز دارید از دستور `last` استفاده کنید:

```text
~$ last | head
jadi     pts/27       :0               Sat Jun  4 21:55    gone - no logout
jadi     pts/26       :0               Sat Jun  4 21:39    gone - no logout
jadi     pts/26       :0               Sat Jun  4 18:55 - 19:42  (00:46)
jadi     pts/25       :0               Sat Jun  4 10:17    gone - no logout
jadi     pts/26       :0               Sat Jun  4 09:25 - 09:26  (00:00)
jadi     pts/26       :0               Sat Jun  4 09:25 - 09:25  (00:00)
jadi     pts/25       :0               Sat Jun  4 08:52 - 09:27  (00:35)
jadi     pts/21       :0               Sat Jun  4 08:41    gone - no logout
jadi     pts/21       funlife          Fri Jun  3 22:22 - 08:41  (10:18)
jadi     pts/21       :0               Fri Jun  3 18:44 - 19:47  (01:03)
```

> راهی برای بررسی ورود ناموفق نیز وجود دارد: `last -f /var/log/btmp`

### مدیریت رمز عبور
دستور `passwd` برای به روز رسانی / تغییر رمز عبور کاربران استفاده می شود. 

```
➜  passwd     
Changing password for jadi.
Current password: 
New password: 
Retype new password: 
passwd: password updated successfully
➜  sudo passwd jadi
New password: 
BAD PASSWORD: The password is shorter than 8 characters
Retype new password: 
passwd: password updated successfully
```

همچنین می توانید از این دستور برای بررسی وضعیت یک کاربر استفاده کنید:

```
➜  ~ passwd -S
jadi P 2023-09-14 0 99999 7 -1
```

می گوید کاربر من jadi است، رمز عبور *P* معتبری دارم (ممکن است *L*ocked یا *NP* بدون رمز عبور باشد)، آخرین زمان تغییر رمز عبور، حداقل و حداکثر سن رمز عبور، دوره هشدار قبل از انقضای رمز عبور و غیرفعال بودن مجاز رمز عبور در چند روز. دستور `passwd` همچنین می تواند برای `--lock` (یا `-l`) یک کاربر، `--expire` (یا `-e`) یک کاربر یا `--unlock` (یا ___IN_LINE_70) استفاده شود.

> همانطور که قبلا در بخش مدیریت کاربر مشاهده کردید، برای تغییر پوسته کاربر، خانه، ... باید از دستور `usermod` استفاده کنید.

اما برای بررسی صحیح/تغییر سن رمز عبور و تنظیمات کاربران، باید از ابزار `chage` استفاده شود. آن را با `-l` برای `list` اجرا کنید:

```
➜  ~ chage -l jadi
Last password change					: Sep 14, 2023
Password expires					: never
Password inactive					: never
Account expires						: never
Minimum number of days between password change		: 0
Maximum number of days between password change		: 99999
Number of days of warning before password expires	: 7
```

یا بدون هیچ سوئیچ برای حالت تعاملی:

```
➜  ~ chage jadi
chage: Permission denied.
➜  ~ sudo chage jadi
Changing the aging information for jadi
Enter the new value, or press ENTER for the default

	Minimum Password Age [0]: 
	Maximum Password Age [99999]: 
	Last Password Change (YYYY-MM-DD) [2023-09-14]: 
	Password Expiration Warning [7]: 3
	Password Inactive [-1]: 
	Account Expiration Date (YYYY-MM-DD) [-1]: 
```

همچنین می توانید از سوئیچ ها برای تغییر مستقیم مقادیر استفاده کنید. بگویید `-m` برای --mindays یا `-M` برای --maxdays. 


### suid و راهنما

<iframe width="560" height="315" src="https://www.youtube.com/embed/1wyPXxrnI7g" title="LPIC 1 - 78  - 110.1 (2/3) - Perform Security Admin Tasks; suid, guid &amp; ulimits" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

ما قبلاً `suid` را پوشش داده ایم. به طور خلاصه، هنگامی که بیت suid روی یک فایل اجرایی تنظیم می شود، کاربر با سطح دسترسی صاحب فایل (و نه runner) اجرا می شود. به دستور `passwd` نگاهی بیندازید:

```
➜  ~ type passwd
passwd is /usr/bin/passwd
➜  ~ ls -ltrh /usr/bin/passwd 
-rwsr-xr-x 1 root root 63K Nov 23  2022 /usr/bin/passwd
```

`s` در قسمت حقوق دسترسی، فایل را با استفاده از دسترسی صاحبان (در اینجا ریشه آن) اجرا می کند. صرف نظر از اینکه چه کسی آن را اجرا می کند. این مورد نیاز است زیرا دستورات `passwd` باید بتوانند رمزهای عبور فایل *shadow* را تغییر دهند، حتی اگر یک کاربر عادی آن را اجرا کند. اما اگر شخصی suid دستور vi را تغییر دهد چه اتفاقی می افتد؟ بیایید ببینیم مالک `vi` کیست:

```text
jadi@funlife ~$ type vi
vi is /usr/bin/vi
jadi@funlife ~$ ls -ltrh /usr/bin/vi
lrwxrwxrwx 1 root root 20 Jun  1 12:52 /usr/bin/vi -> /etc/alternatives/vi
```

`vi` متعلق به root است، بنابراین اگر بیت suid تنظیم شود، vi همیشه به عنوان root اجرا می شود! در این صورت، هر کسی می‌تواند هر فایلی را ویرایش کند! بنابراین اگر یک هکر هستید و یک روت موقت دریافت می‌کنید، کافی است vi را در جایی کپی کنید (با نام غیر مشکوک دیگری) و به آن دسترسی `suid` بدهید. اکنون می توانید آن را با کاربران عادی اجرا کنید و در صورت نیاز فایل های سیستم را تغییر دهید! به همین دلیل است که یک مدیر سیستم باید بتواند در صورت نیاز فایل های اجرایی سیستم خود را با بیت `suid` بررسی کند:

```text
$sudo find / -perm -u+s
```

در اینجا، `-perm -u+s` به `find` می گوید که فایلی را که دارای `suid` در `user` است، جستجو کند. برای اطلاعات بیشتر، `man find` را بررسی کنید و `perm` را جستجو کنید. 

> همین امر در مورد راهنما نیز صدق می کند. اگر راهنما تنظیم شده باشد، فایل با دسترسی گروه خود اجرا می شود


### محدودیت های کاربر

منابع موجود در یک ماشین لینوکس را می توان با دستور `ulimit` برای کاربران مدیریت کرد. بخشی از سیستم PAM است. اگر می‌خواهید محدودیت‌های اجرای سیستم را بررسی کنید:

```text
~$ ulimit -a
core file size          (blocks, -c) 0
data seg size           (kbytes, -d) unlimited
scheduling priority             (-e) 0
file size               (blocks, -f) unlimited
pending signals                 (-i) 47457
max locked memory       (kbytes, -l) 64
max memory size         (kbytes, -m) unlimited
open files                      (-n) 1024
pipe size            (512 bytes, -p) 8
POSIX message queues     (bytes, -q) 819200
real-time priority              (-r) 0
stack size              (kbytes, -s) 8192
cpu time               (seconds, -t) unlimited
max user processes              (-u) 47457
virtual memory          (kbytes, -v) unlimited
file locks                      (-x) unlimited
```

و می توانید آنها را به این صورت تغییر دهید:

```text
$ ulimit -t 1
```

با این کار، CPU TIME هر فرآیندی به 1 ثانیه محدود می شود. اگر بیشتر از آن استفاده کنید، فرآیند به طور خودکار \(توسط ماژول PAM\) از بین می‌رود. لطفا توجه داشته باشید که زمان ساعت دیواری شما با زمان CPU متفاوت است. برای اینکه ببینید یک فرآیند چقدر از زمان CPU استفاده می کند، آن را به صورت زیر اجرا کنید:

```text
$ time firefox
```

تغییر ulimit همانطور که ما انجام دادیم یک چیز موقتی است. فقط در آن پوسته خاص باقی می ماند.

برای تغییر ulimits در سراسر سیستم:

```text
$ cat /etc/security/limits.conf
# /etc/security/limits.conf
#
#Each line describes a limit for a user in the form:
#
#<domain>        <type>  <item>  <value>
#
#Where:
#<domain> can be:
#        - a user name
#        - a group name, with @group syntax
#        - the wildcard *, for default entry
#        - the wildcard %, can be also used with %group syntax,
#                 for maxlogin limit
#        - NOTE: group and wildcard limits are not applied to root.
#          To apply a limit to the root user, <domain> must be
#          the literal username root.
#
#<type> can have the two values:
#        - "soft" for enforcing the soft limits
#        - "hard" for enforcing hard limits
#
#<item> can be one of the following:
#        - core - limits the core file size (KB)
#        - data - max data size (KB)
#        - fsize - maximum filesize (KB)
#        - memlock - max locked-in-memory address space (KB)
#        - nofile - max number of open files
#        - rss - max resident set size (KB)
#        - stack - max stack size (KB)
#        - cpu - max CPU time (MIN)
#        - nproc - max number of processes
#        - as - address space limit (KB)
#        - maxlogins - max number of logins for this user
#        - maxsyslogins - max number of logins on the system
#        - priority - the priority to run user process with
#        - locks - max number of file locks the user can hold
#        - sigpending - max number of pending signals
#        - msgqueue - max memory used by POSIX message queues (bytes)
#        - nice - max nice priority allowed to raise to values: [-20, 19]
#        - rtprio - max realtime priority
#        - chroot - change root to directory (Debian-specific)
#
#<domain>      <type>  <item>         <value>
#

#*               soft    core            0
#root            hard    core            100000
#*               hard    rss             10000
#@student        hard    nproc           20
#@faculty        soft    nproc           20
#@faculty        hard    nproc           50
#ftp             hard    nproc           0
#ftp             -       chroot          /ftp
#@student        -       maxlogins       4

# End of file
```

> محدودیت های نرم را می توان توسط کاربر تغییر داد اما محدودیت های سخت نقطه توقف واقعی هستند.


## پورت ها را باز کنید

<iframe width="560" height="315" src="https://www.youtube.com/embed/9yycyd7ShyM" title="LPIC 1 - 79  - 110.1 (3/3) - Perform Security Admin Tasks; checking for open ports &amp; scan with nmap" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

### netstat، fuser و lsof

در ماژول 109.1 در مورد پورت ها صحبت کردیم. پورت ها مانند کل سیستم های ما هستند که توسط برنامه ها برای گوش دادن به دنیای خارج استفاده می شود. اگر من یک وب سرور را روی رایانه خود اجرا می کنم، باید یک پورت باز داشته باشم تا مردم بتوانند از آن سرور بپرسند "لطفا index.html خود را به من نشان دهید". بسیاری از بدافزارها پورت ها را باز می کنند تا مهاجم بتواند با آنها ارتباط برقرار کند. مهم است که هر چند وقت یکبار رایانه خود را از نظر پورت های باز بررسی کنید. دستور قدیمی برای این `netstat` است. با استفاده از سوئیچ `-na` یا `-ap` یا `-tuna`.. مطمئنم اگر از ساندویچ تن ماهی لذت برده اید **تونا** را به راحتی به خاطر بسپارید.

```text
jadi@funlife ~$ netstat -tuna
Active Internet connections (servers and established)
Proto Recv-Q Send-Q Local Address           Foreign Address         State      
tcp        0      0 127.0.0.1:3306          0.0.0.0:*               LISTEN     
tcp        0      0 0.0.0.0:80              0.0.0.0:*               LISTEN     
tcp        0      0 127.0.1.1:53            0.0.0.0:*               LISTEN     
tcp        0      0 127.0.0.1:9050          0.0.0.0:*               LISTEN     
tcp       25      0 192.168.59.9:49934      192.168.59.192:139      CLOSE_WAIT
tcp        0      0 127.0.0.1:60228         127.0.0.1:1080          ESTABLISHED
tcp        0      0 192.168.1.35:55324      159.203.148.169:8385    ESTABLISHED
tcp        0      0 127.0.0.1:59590         127.0.0.1:1080          ESTABLISHED
tcp        0      0 127.0.0.1:60212         127.0.0.1:1080          ESTABLISHED
tcp        0      0 192.168.1.35:54220      159.203.148.169:8385    ESTABLISHED
tcp        0      0 127.0.0.1:57186         127.0.0.1:1080          ESTABLISHED
tcp        0      0 192.168.1.35:49574      173.194.122.231:443     ESTABLISHED
tcp        0      0 127.0.0.1:59002         127.0.0.1:1080          ESTABLISHED
udp        0      0 0.0.0.0:54502           0.0.0.0:*                          
udp        0      0 0.0.0.0:5353            0.0.0.0:*                          
udp        0      0 0.0.0.0:5353            0.0.0.0:*
```

همه پورت های `LISTEN` سرور هستند. آنها در حال گوش دادن به اتصالات ورودی جدید هستند. اتصالات `ESTABLISHED` اتصالات فعال بین رایانه شما و رایانه دیگری هستند. در این جداول `0.0.0.0` _any address_ یا _any interface_ را دیکته می کند.

ابزارهای مفید دیگر `ss` برای همان هدفی هستند که در فصل 109 و `lsof` و `fuser` دیدید. `lsof` قبلاً در بخش های قبلی مورد بحث قرار گرفته است. فایل های باز روی سیستم را نشان می دهد و با در نظر گرفتن اینکه _همه چیز در لینوکس یک فایل یا یک فرآیند است_ می توانید نتیجه بگیرید که این دستور باید بتواند اتصالات باز را نیز نمایش دهد. و حق با شماست:

```text
# lsof -i
COMMAND     PID       USER   FD   TYPE  DEVICE SIZE/OFF NODE NAME
privoxy     806    privoxy    4u  IPv4   16130      0t0  TCP funlife:8118 (LISTEN)
cups-brow   903       root    8u  IPv4   17477      0t0  UDP *:ipp
mysqld      971      mysql   19u  IPv4   20875      0t0  TCP funlife:mysql (LISTEN)
tor        1038 debian-tor    6u  IPv4   19155      0t0  TCP funlife:9050 (LISTEN)
dnsmasq    1260     nobody   11u  IPv4 1910037      0t0  UDP *:18666
adb        1278       jadi    5u  IPv4  579541      0t0  TCP funlife:5037 (LISTEN)
chromium-  2891       jadi   88u  IPv4  813611      0t0  TCP 192.168.1.35:45702->do-13.lastpass.com:https (ESTABLISHED)
chromium-  2891       jadi  126u  IPv4 1907389      0t0  TCP 192.168.1.35:50642->ntt-2.lastpass.com:https (ESTABLISHED)
chromium-  2891       jadi  133u  IPv4 1909733      0t0  TCP 192.168.1.35:50644->ntt-2.lastpass.com:https (ESTABLISHED)
chromium-  2891       jadi  268u  IPv4  785289      0t0  TCP 192.168.1.35:60736->lf-in-f188.1e100.net:5228 (ESTABLISHED)
python     4925       jadi    4u  IPv4  658287      0t0  TCP funlife:8000 (LISTEN)
Telegram   4943       jadi   39u  IPv4  773463      0t0  TCP 192.168.1.35:44732->149.154.175.50:https (ESTABLISHED)
dhclient   9984       root    6u  IPv4  787885      0t0  UDP *:bootpc
nginx     11095       root    6u  IPv4   17998      0t0  TCP *:http (LISTEN)
nginx     11099   www-data    7u  IPv6   17999      0t0  TCP *:http (LISTEN)
chrome    14264       jadi  114u  IPv4  788089      0t0  UDP *:mdns
chrome    14264       jadi  126u  IPv4 1872872      0t0  TCP funlife:60370->funlife:socks (ESTABLISHED)
chrome    14264       jadi  138u  IPv4 1908382      0t0  TCP funlife:60408->funlife:socks (ESTABLISHED)
```

عجب! این دستور فرمان، PID، کاربر در حال اجرا و IP مبدا و مقصد را نشان می دهد و می گوید که آیا این یک اتصال LISTENING یا STABLISHED است.

اگر می‌خواهید بررسی کنید کدام فرآیند از پورت 80 استفاده می‌کند، می‌توانید خروجی هر دستور بالا را grep کنید یا به سادگی از دستور `fuser` (کاربر فایل؛ کسی که از این فایل استفاده می‌کند) استفاده کنید تا تمام PID‌های مربوط به آن پورت خاص را پیدا کنید. یک سوئیچ رایج `-v` است که پرمخاطب است. 

```text
➜  bin sudo fuser 22/tcp -v      
                     USER        PID ACCESS COMMAND
22/tcp:              root          1 F.... systemd
```

### nmap

`nmap` یکی از ابزارهای محبوب هکرها است! شما می توانید یک سرور را nmap کنید تا از اطلاعات زیادی در مورد آن سرور مطلع شوید:

```text
# nmap localhost

Starting Nmap 7.01 ( https://nmap.org ) at 2016-06-04 21:32 IRDT
Nmap scan report for localhost (127.0.0.1)
Host is up (0.0000070s latency).
rDNS record for 127.0.0.1: funlife
Not shown: 995 closed ports
PORT     STATE SERVICE
80/tcp   open  http
1080/tcp open  socks
3306/tcp open  mysql
8000/tcp open  http-alt
9050/tcp open  tor-socks

Nmap done: 1 IP address (1 host up) scanned in 1.66 seconds
root@funlife:~#
```

در ابتدایی ترین شکل، nmap تمام پورت های باز را از 1 تا 1000 بررسی می کند و نتایج را چاپ می کند. سوئیچ های زیادی برای یافتن اطلاعات دیگر در مورد هاست وجود دارد و هر هکری که می خواهد وضعیت سرور را بررسی کند از آنها استفاده می کند.

یک جستجوی سریع برای [nmap oneliners] (https://duckduckgo.com/?t=h_&q=nmap+oneliners&ia=web) انجام دهید و ده ها دستور و ترفند جالب برای آن پیدا خواهید کرد. آنقدر جالب است که وب سایت آن [بخشی درباره nmap در فیلم ها دارد] (https://nmap.org/movies/)!