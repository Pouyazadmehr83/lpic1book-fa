Title: 110.3 ایمن سازی داده ها با رمزگذاری
Date: 2010-12-03 10:20
Category: LPIC1
Tags: LPIC1, 102, LPIC1-102-500
Authors: Jadi
sortorder: 470
Summary: 

_وزن: 4_

داوطلب باید بتواند از تکنیک های کلید عمومی برای ایمن سازی داده ها و ارتباطات استفاده کند.

### حوزه های دانش کلیدی

* پیکربندی و استفاده اولیه کلاینت OpenSSH 2 را انجام دهید.
* نقش کلیدهای میزبان سرور OpenSSH 2 را درک کنید.
* پیکربندی، استفاده و لغو اولیه GnuPG را انجام دهید.
* از GPG برای رمزگذاری، رمزگشایی، امضا و تأیید فایل ها استفاده کنید.
* تونل های پورت SSH \(از جمله تونل های X11\) را بدانید.

### شرایط و امکانات

* ssh
* ssh-keygen
* ssh-agent
* ssh-add
* ~/.ssh/id\_rsa و id\_rsa.pub
* ~/.ssh/id\_dsa و id\_dsa.pub
* ~/.ssh/id_ecdsa و id_ecdsa.pub
* ~/.ssh/id_ed25519 و id_ed25519.pub
* /etc/ssh/ssh\_host\_rsa\_key و ssh\_host\_rsa\_key.pub
* /etc/ssh/ssh\_host\_dsa\_key و ssh\_host\_dsa\_key.pub
* /etc/ssh/ssh_host_ecdsa_key و ssh_host_ecdsa_key.pub
* /etc/ssh/ssh_host_ed25519_key و ssh_host_ed25519_key.pub
* ~/.ssh/authorized\_keys
* ssh\_known\_hosts
* gpg
* gpg-agent
* ~/.gnupg/

<iframe width="560" height="315" src="https://www.youtube.com/embed/ElbC0EtZc4c?si=PemOqHr6s7V53wwS" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## جفت کلید

در رمزنگاری سنتی، از کلیدهای متقارن استفاده می شد: هر دو طرف یک رمز عبور مشترک داشتند. داده ها با آن رمز رمزگذاری شده و سپس با استفاده از همان رمز رمزگشایی شدند. اما در سال 1976، ایده جدیدی مطرح شد: اگر 2 کلید ایجاد کنیم (اجازه دهید آنها را کلید خصوصی و کلید عمومی بنامیم) به گونه ای که فقط افرادی که کلید عمومی را دارند بتوانند هر چیزی را که با کلید خصوصی رمزگذاری شده است را باز کنند؟ دانشمندان این را به واقعیت تبدیل کردند و اکنون، بیشتر رمزگذاری های ما از طریق این **جفت کلید**ها انجام می شود. هنگام تولید یک جفت کلید، ما دو کلید را با استفاده از یک الگوریتم کامپیوتری تولید می کنیم، به گونه ای که هر پیامی که با استفاده از یکی رمزگذاری می شود، تنها با استفاده از دیگری باز می شود. اینها کلید عمومی و خصوصی نامیده می شوند. شما کلید عمومی را برای دوستان خود یا حتی به صورت عمومی در شبکه منتشر می کنید و اگر شخصی بخواهد برای شما پیام رمزگذاری شده ارسال کند، با استفاده از کلید عمومی شما آن را رمزگذاری می کند و با هر وسیله ای برای شما ارسال می کند (یا پیام رمزگذاری شده را در اینترنت منتشر می کند) و فقط و فقط شما قادر خواهید بود آن را باز کنید، زیرا شما هستید که کلید خصوصی را دارید!

> نکته مهم در مورد کلید عمومی / خصوصی این است که داده ها را می توان از طریق اینترنت بدون ترس از هکرها یا دولت ها منتقل کرد. شما در حال انتشار کلید خود در جهان هستید، یکی آن را انتخاب می کند و از آن برای رمزگذاری برخی داده ها استفاده می کند و نتیجه را برای شما ارسال می کند. مردم می توانند ببینند که شما "برخی داده ها" را دریافت می کنید اما نمی توانند آن را رمزگذاری کنند زیرا کلید خصوصی مورد نیاز برای رمزگشایی آن را ندارند.

### کلیدهای ssh
همین فناوری (رمزنگاری کلید عمومی یا رمزنگاری نامتقارن) را می توان در بیشتر ارتباطات شبکه نیز مورد استفاده قرار داد. در واقع `ssh` بر اساس این مفهوم کار می کند. برای احراز هویت هاست و ایمن سازی ترافیک استفاده می شود. 

```
➜  ~ ssh 192.168.70.2
The authenticity of host '192.168.70.2 (192.168.70.2)' can't be established.
ED25519 key fingerprint is SHA256:4Wp2zz6sgPAhnbqhkNjOd6QDpNQ4jvjX7qAzslPX09U.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? y
Please type 'yes', 'no' or the fingerprint: yes
Warning: Permanently added '192.168.70.2' (ED25519) to the list of known hosts.
jadi@192.168.70.2's password:
Linux debian 6.4.0-2-arm64 #1 SMP Debian 6.4.4-3 (2023-08-08) aarch64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
You have no mail.
Last login: Sun Sep 17 04:43:18 2023 from 192.168.70.1
jadi@debian:~$
```

در بالای سرور، اثر انگشت کلید ED25519 خود را به ما نشان می دهد و از ما می خواهد که آن را تأیید کنیم. از این به بعد، سیستم ما برای همان کلید با همان سرور به ما هشدار نمی دهد. اما اگر اثر انگشت (پس کلید) همان سرور تغییر کند، یک مورد جدی در نظر گرفته می شود:

```
➜  ~ ssh 192.168.70.2
Host key verification failed.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@    WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!     @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
IT IS POSSIBLE THAT SOMEONE IS DOING SOMETHING NASTY!
Someone could be eavesdropping on you right now (man-in-the-middle attack)!
It is also possible that a host key has just been changed.
The fingerprint for the ED25519 key sent by the remote host is
SHA256:4Wp2zz6sgPAhnbqhkNjOd6QDpNQ4jvjX7qAzslPX09U.
Please contact your system administrator.
Add correct host key in /Users/jadi/.ssh/known_hosts to get rid of this message.
Offending RSA key in /Users/jadi/.ssh/known_hosts:548
Host key for 192.168.70.2 has changed and you have requested strict checking.
```

اگر می خواهید این مشکل را حل کنید - پس از اطمینان از اینکه این یک حمله نیست - باید داده های 192.168.70.2 را از فایل `.ssh/known_hosts` حذف کنید. خوشبختانه نیازی به ویرایش مستقیم فایل ندارید. برای استفاده از دستور `ssh-keygen` کافی است:

```
➜  ~ ssh-keygen -R 192.168.70.2
# Host 192.168.70.2 found: line 547
# Host 192.168.70.2 found: line 548
# Host 192.168.70.2 found: line 549
/Users/jadi/.ssh/known_hosts updated.
Original contents retained as /Users/jadi/.ssh/known_hosts.old
```

#### جفت کلید خود را ایجاد کنید

شما به راحتی می توانید هر تعداد جفت کلید بخواهید ایجاد کنید. حتی با الگوریتم های مختلف (تعریف شده توسط سوئیچ `-t` و شامل dsa، ecdsa، ecdsa-sk، ed25519، ed25519-sk، rsa). انتخاب های رایج عبارتند از *rsa* که پیش فرض است و *ecdsa* که توسط بیت کوین استفاده می شود!

بیایید یک جفت کلید ecdsa در دستگاه خود ایجاد کنیم. ما می‌توانیم از این برای ورود به سرورها بدون ارائه رمز عبور یا امضا/رمزگذاری پیام‌ها استفاده کنیم.

```
jadi@debian:~$ ssh-keygen -t ecdsa
Generating public/private ecdsa key pair.
Enter file in which to save the key (/home/jadi/.ssh/id_ecdsa):
/home/jadi/.ssh/id_ecdsa already exists.
Overwrite (y/n)? y
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in /home/jadi/.ssh/id_ecdsa
Your public key has been saved in /home/jadi/.ssh/id_ecdsa.pub
The key fingerprint is:
SHA256:WvJu5D7ns0a2z0sB6l8ZrCXnAgxSmb2kSwgo/lK0QYA jadi@debian
The key's randomart image is:
+---[ECDSA 256]---+
|.oo.  .+         |
|E .o .o o        |
|o ..+..o ..      |
| . o..oo.. o     |
|  o  ...S . *    |
| . .  .*..o* +   |
|  .   .oooo.=    |
|       .+.==     |
|       oo=+++.   |
+----[SHA256]-----+
```

و از آنجایی که رایگان است، اجازه دهید یک کلید rsa نیز ایجاد کنیم:

```
jadi@debian:~$ ssh-keygen
Generating public/private rsa key pair.
Enter file in which to save the key (/home/jadi/.ssh/id_rsa):
/home/jadi/.ssh/id_rsa already exists.
Overwrite (y/n)? y
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in /home/jadi/.ssh/id_rsa
Your public key has been saved in /home/jadi/.ssh/id_rsa.pub
The key fingerprint is:
SHA256:Q67Ob1DOfmF3gG449OfNLHXxE5QEH4B/UzHR8ycAHao jadi@debian
The key's randomart image is:
+---[RSA 3072]----+
|          .oo++*=|
|           oo .+=|
|        . ......+|
|       oo.. ...=o|
|       =E+   ...*|
|      ..=.* o o.o|
|      .o + = * ..|
|     o  o . o +  |
|      oo..   .   |
+----[SHA256]-----+
```

آن _Image_ سرگرم کننده چیزی است که می توانید به دوستان خود نشان دهید تا مطمئن شوند که از کلید صحیح استفاده می کنند. 

> در بالا، رمز عبور برای کلیدها قرار ندادم. اگر این کار را می‌کردم، باید هر بار که می‌خواستم از آن کلید استفاده کنم، آن رمز عبور را ارائه می‌کردم

این کلیدها در فهرست کاربران `~/.ssh` ذخیره می شوند. همانطور که می توانید حدس بزنید، کلیدهای گسترده سیستم مورد استفاده برای سرور ssh در `/etc/ssh` قرار دارند.


### بر اساس کلید / ورود بدون رمز عبور
سرور ssh را می توان برای بررسی هویت شما با استفاده از کلیدهای خود پیکربندی کرد. کافی است کلید عمومی خود را در حساب کاربری سرور ذخیره کنید و به سرور بگویید لاگین های مبتنی بر کلید را نیز بررسی کند. در این صورت کلاینت ssh شما کلید خصوصی شما را به عنوان مدرک هویت در اختیار سرور ssh قرار می دهد و می توانید بدون ارائه پسورد وارد کاربر شوید.

ابتدا کلید *public* خود را کپی کرده و وارد سرور شوید. فایل `~/.ssh/authorized_keys` را باز کنید و فایل خود را اضافه کنید. همچنین مطمئن شوید که `/etc/ssh/sshd_config` حاوی `PubkeyAuthentication yes` باشد. اکنون از سیستم خارج شوید و در ورود بعدی بتوانید بدون رمز ورود وارد شوید! وقتی سرورهای زیادی را مدیریت می‌کنید یا می‌خواهید کپی‌های `scp` و موارد دیگر را خودکار کنید، بسیار کاربردی است. همچنین از نظر sysadmin ایمن تر است زیرا اگر لازم باشد به کاربر جدیدی اجازه ورود به سیستم من را بدهم، نیازی به اشتراک گذاری رمز عبور یا ارتباط رمز عبور در هیچ کانالی ندارم. کافی است از شخص **کلید عمومی** خود را بخواهید و آن را به فایل `.ssh/authorized_keys` کاربران اضافه کنید.

اوه! و نیازی نیست _key copying_ را به صورت دستی انجام دهید. فقط از دستور `ssh-copy-id` استفاده کنید:

```
➜  ~ ssh-copy-id 192.168.70.2
/usr/bin/ssh-copy-id: INFO: Source of key(s) to be installed: "/Users/jadi/.ssh/id_dsa.pub"
/usr/bin/ssh-copy-id: INFO: attempting to log in with the new key(s), to filter out any that are already installed
/usr/bin/ssh-copy-id: INFO: 1 key(s) remain to be installed -- if you are prompted now it is to install the new keys
jadi@192.168.70.2's password:

Number of key(s) added:        1

Now try logging into the machine, with:   "ssh '192.168.70.2'"
and check to make sure that only the key(s) you wanted were added.
```

#### ssh-agent
`ssh-agent` مانند یک مدیر کلید برای کلیدهای ssh شما کار می کند. کلیدهای خصوصی شما را در حافظه نگه می دارد و در صورت نیاز آنها را ارائه می دهد. به عنوان مثال اگر روی کلید خود رمز عبور تعیین کرده اید، باید هر بار که می خواهید از آن کلید استفاده کنید رمز عبور را تایپ کنید. برای سهولت در استفاده از ssh-agent، باید پوسته ای را با ssh-agent وارد کنید و تمام کلید خود را به عامل اضافه کنید:

```
jadi@debian:~$ ssh-agent /bin/bash
jadi@debian:~$ ssh-add
Identity added: /home/jadi/.ssh/id_rsa (jadi@debian)
Identity added: /home/jadi/.ssh/id_ecdsa (jadi@debian)
Identity added: /home/jadi/.ssh/id_dsa (/home/jadi/.ssh/id_dsa)
```

اکنون، نماینده در مورد کلیدهای شما می داند و دیگر رمز عبور را نمی خواهد.

`ssh-agent` همچنین می تواند کلیدهای شما را به صورت ایمن در حافظه به سرورهای دیگر _انتقال_ کند. فرض کنید باید به سرور A ssh کنید و زمانی که در سرور A هستید، از کلید خود برای ssh به سرور B استفاده کنید (یا با استفاده از کلیدهای خصوصی خود git pull را انجام دهید). کلیدها در سرور A هستند و کپی کردن آنها به صورت واقعی و فیزیکی در سرور B امن نیست. در این حالت شما `ssh-agent` را اجرا می کنید و حتی زمانی که در سرور B هستید کلیدهای خود را در اختیار دارید. 

#### تونل های ssh

<iframe width="560" height="315" src="https://www.youtube.com/embed/bjvOJNmWgYI?si=UFKx2TDaF9l5GCjw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

ssh همچنین می تواند برای _tunnelling_ استفاده شود. این یک مفهوم بسیار سرگرم کننده و یک ابزار فوق العاده کاربردی در دست یک نینجا شبکه است! صادقانه بگویم که ما همیشه از آن برای حل مشکلات پیچیده استفاده می کنیم. 

همانطور که از نام پیداست، تیونینگ ssh *تونل* داده ها را بین ماشین ها ایجاد می کند. به این مثال نگاه کنید:

```
ssh -L 9000:hckrnews.com:80 root@5.161.197.79
```

در اینجا من به رایانه خود می گویم که با استفاده از کاربر `root` (که ایده خوبی نیست) به سرور `5.161.197.79` ssh کند. و یک **تونل محلی** (`-L`) از دستگاه من به سمت پورت `hckrnews.com` `80` از طریق آن دستگاه ایجاد کنید. اکنون اگر به `localhost:9000` **در دستگاه خود** متصل شوم، درخواست از طریق `5.161.197.79` به سمت پورت 80 hckrnews.com خواهد بود. می توانید آن را با `curl localhost:9000` امتحان کنید.

چرا این مفید است؟ فرض کنید برنامه ای روی سرور خود دارید که فقط به درخواست های محلی (و نه اینترنت) پاسخ می دهد. با استفاده از حمل و نقل محلی، می توانید یک پورت را در رایانه خود به پورتی که برنامه ها روی آن کار می کنند، فوروارد کنید و از برنامه در دستگاه خود استفاده کنید!

همچنین مفهوم **Remote Forwarding** وجود دارد. در این حالت، یک پورت را از یک سرور راه دور به سرور دیگری (عمدتاً رایانه شخصی خود) متصل می کنید. با استفاده از این، می توانید یک وب سرور را از رایانه شخصی خود در اینترنت در معرض دید قرار دهید:

```
$ ssh -R 8000:localhost:80 root@5.161.197.79
```

در مثال بالا، من به ssh می گویم که یک تونل **Remote** ایجاد کند. پس از این، هر درخواستی در پورت 8000 از کامپیوتر 5.161.197.79 به پورت 80 لوکال هاست (دستگاه من) می رسد!

حتی می‌توانید از دستگاه راه دور بخواهید که در یک پورت خاص در تمام رابط‌هایش (به روی شبکه و نه فقط لوکال هاست باز شود) شروع به گوش دادن کند:

```
ssh -R 0.0.0.0:8000:localhost:7777 192.168.70.2
```

در بالا، من به دستگاه 192.168.70.2 می گویم که پورت 8000 را به همه اینترفیس ها باز کند و هر آنچه را که به دست آورد را به پورت machiens 7777 من ارسال کند.

> برای اینکه به کلاینت‌ها اجازه دهید پورت‌های گوش را به هر چیزی غیر از localhost متصل کنند، پیکربندی `GatewayPorts clientspecified` باید در فایل پیکربندی سرور ssh تنظیم شود.

موارد استفاده بیشتر هم وجود دارد. برای مثال شما از سوئیچ -D برای فواردینگ درگاه سطح برنامه `dynamic` استفاده می کنید. این مانند یک پروکسی / ضد سانسور کار می کند. اگر انجام دهم 

```
ssh -D 1080 192.168.70.2
```

پورت 1080 کار خواهد کرد از یک پروکسی *socks* در دستگاه من بپرسید و هر درخواستی را که به آن رسید به دستگاه 192.168.70.2 فوروارد کرده و پاسخ ها را برمی گرداند. اکنون می توانم برنامه های خود را طوری پیکربندی کنم که از localhost:1080 به عنوان پراکسی socks خود استفاده کنند و 192.168.70.2 به عنوان یک پروکسی در اینجا کار خواهد کرد. این زمانی مفید است که در لوکال هاست خود اینترنت ندارید، اما 192.168.70.2 آن را دارد.

##### X Forwarding
آخرین مفهومی که می خواهم در بخش فورواردینگ در مورد آن صحبت کنم، حمل و نقل X است. همانطور که قبلاً از [ماژول 106] (1061-install-and-configure-x11.html) می دانید، برنامه های گرافیکی لینوکس از X به عنوان میزبان گرافیکی خود استفاده می کنند. این X همچنین می تواند در شبکه به عنوان هر ارتباط مبتنی بر شبکه دیگر ارسال شود. حتی سوئیچ خود را روی برنامه ssh دارد. برای ارسال X، کافی است یک `-X` به ssh خود اضافه کنید. لطفاً توجه داشته باشید که پیکربندی `X11Forwarding yes` باید در فایل sshd_config شما وجود داشته باشد.

برای فعال کردن ارسال X11 در یک جلسه ssh، کافی است `-X` را به ssh خود اضافه کنید:

```
ssh -X 192.168.70.2
```

و سپس می توانید برنامه های گرافیکی (برای سرگرمی مثلا `xeyes`) را روی دستگاه راه دور اجرا کنید و قسمت گرافیکی آن را روی سرور X خودتان ببینید!

> اگر در دستگاه گنو/لینوکس با سرور X11 نیستید، باید آن را نصب کنید (به عنوان مثال XQuartz در مک)

این زمانی بسیار مفید است که می خواهید برنامه ای را روی یک سرور پرمحتوا اجرا کنید یا از خانه کار کنید در حالی که برنامه های گرافیکی شما در دفتر هستند ؛)

## ecnrypt کرده و با استفاده از gpg امضا کنید

<iframe width="560" height="315" src="https://www.youtube.com/embed/BX6BB8bqy24?si=iIWhRQnFmADr93n6" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

همانطور که در بخش قبل توضیح داده شد، می توان از یک جفت کلید عمومی و خصوصی برای رمزگذاری یا امضای پیام ها استفاده کرد. یک پیاده سازی از این روش به نام `gpg` وجود دارد که می تواند در لینوکس (و سایر ماشین ها) برای انجام این کارها استفاده شود. ابتدا باید یک کلید ایجاد کنید:

```text
jadi@debian:~$ gpg --gen-key
gpg (GnuPG) 2.2.40; Copyright (C) 2022 g10 Code GmbH
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.

gpg: directory '/home/jadi/.gnupg' created
gpg: keybox '/home/jadi/.gnupg/pubring.kbx' created
Note: Use "gpg --full-generate-key" for a full featured key generation dialog.

GnuPG needs to construct a user ID to identify your key.

Real name: Jadi
Name must be at least 5 characters long
Real name: Jadi M
Email address: jadijadi@gmail.com
You selected this USER-ID:
    "Jadi M <jadijadi@gmail.com>"

Change (N)ame, (E)mail, or (O)kay/(Q)uit?
Change (N)ame, (E)mail, or (O)kay/(Q)uit? O
We need to generate a lot of random bytes. It is a good idea to perform
some other action (type on the keyboard, move the mouse, utilize the
disks) during the prime generation; this gives the random number
generator a better chance to gain enough entropy.
We need to generate a lot of random bytes. It is a good idea to perform
some other action (type on the keyboard, move the mouse, utilize the
disks) during the prime generation; this gives the random number
generator a better chance to gain enough entropy.
gpg: /home/jadi/.gnupg/trustdb.gpg: trustdb created
gpg: directory '/home/jadi/.gnupg/openpgp-revocs.d' created


gpg: revocation certificate stored as '/home/jadi/.gnupg/openpgp-revocs.d/E279681DC09318AB5B23D359C9063DD26365986A.rev'
public and secret key created and signed.

pub   rsa3072 2023-09-17 [SC] [expires: 2025-09-16]
      E279681DC09318AB5B23D359C9063DD26365986A
uid                      Jadi M <jadijadi@gmail.com>
sub   rsa3072 2023-09-17 [E] [expires: 2025-09-16]
```

اکنون کلید در پوشه `~/.gnupg` ایجاد شده است و ما می توانیم کلید عمومی خود را با دیگران به اشتراک بگذاریم:

```text
jadi@debian:~$ gpg --list-keys
/home/jadi/.gnupg/pubring.kbx
-----------------------------
pub   rsa3072 2023-09-17 [SC] [expires: 2025-09-16]
      E279681DC09318AB5B23D359C9063DD26365986A
uid           [ultimate] Jadi M <jadijadi@gmail.com>
sub   rsa3072 2023-09-17 [E] [expires: 2025-09-16]

jadi@debian:~$ gpg --export jadi > jadi.pub.key
jadi@debian:~$ file jadi.pub.key
jadi.pub.key: OpenPGP Public Key Version 4, Created Sun Sep 17 12:39:19 2023, RSA (Encrypt or Sign, 3072 bits); User ID; Signature; OpenPGP Certificate
```

> کلید صادر شده در فرمت باینری است، `-a` را به آن در ascii اضافه کنید

حالا باید این کلید را بین دیگران توزیع کنید. می توانید آن را در جایی آپلود کنید، آن را ایمیل کنید، آن را در وب سایت خود قرار دهید یا از برخی از فروشگاه های کلید عمومی برای به اشتراک گذاری آن با دیگران استفاده کنید. اگر کسی آن را دریافت کرد، می تواند با استفاده از دستور زیر آن را به فروشگاه کلید خود وارد کند:

```text
gpg --import jadi.pub.key
```

اوه! و اگر احساس کنید کلید شما به خطر افتاده است چه اتفاقی می افتد!؟ در این حالت باید یک فایل **ابطال** ایجاد کنید و آن را با دیگران به اشتراک بگذارید تا به آنها بگویید که کلید شما دیگر معتبر نیست:

```text
gpg --output jadi.revoke.asc --gen-revoke jadijadi@gmail.com
```

این به gpg می‌گوید که یک فایل ابطال به نام jadi.revoke.asc برای هویت jadijadi@gmail.com ایجاد کند. اگر jadijadi@gmail.com نیاز به باطل کردن کلید عمومی خود داشته باشد، باید این فایل را در اینترنت یا سرورهای کلید منتشر کند و دیگران بدانند که کلید عمومی قبلی دیگر معتبر نیست.

### رمزگذاری / رمزگشایی فایل ها

در این مرحله، من یک کلید دارم و دوستانم کلید عمومی من را در دستگاه خود وارد می کنند. اگر هر یک از آنها بخواهد یک پیام رمزگذاری شده برای من ارسال کند، می تواند کارهای زیر را انجام دهد: 

```
echo "I Loved your course! I'll tell all my friends about it." > file.txt
gpg --out file.txt.encrypted --recipient jadijdai@gmail.com --encrypt file.txt
```

حالا کافی است این فایل را برای من بفرستند. حتی استفاده از کانال های ناامن، زیرا توسط ابزارهای درجه یک رمزگذاری شده است. همه می توانند این فایل را دانلود کنند اما فقط من می توانم آن را رمزگشایی کنم. چون فقط من **کلید خصوصی** jadijadi@gmail.com را دارم.

```text
gpg --out out.txt --decrypt file.txt.encrypted
```

> اگر این دوره را دوست داشتید، نیازی به رمزگذاری پیام نیست، فقط [linux1st.com](https://linux1st.com) را در اینترنت به اشتراک بگذارید! 

#### امضا و تایید فایل ها

در قسمت قبل از gpg برای رمزگذاری داده ها استفاده کردیم. ما از کلید عمومی شخصی برای رمزگذاری استفاده کردیم و سپس از کلید خصوصی خود برای رمزگشایی داده ها استفاده کردیم. اما اگر من از کلید خصوصی خود در کنار خود استفاده کنم و به دیگران اجازه دهم از کلید عمومی من برای _باز کردن_ داده ها استفاده کنند، چه اتفاقی می افتد؟ به این می گویند **امضاء**.

لطفاً به یاد داشته باشید که فقط من به کلید خصوصی خود دسترسی دارم. بنابراین اگر آن را روی یک فایل اعمال کنم، هر کدام:

1. قادر خواهد بود فایل را با استفاده از کلید عمومی من باز کند
2. مطمئن باشید که **I** این را امضا کرده است زیرا فقط **I** به کلید خصوصی کلید عمومی که برای باز کردن فایل استفاده کرده است دسترسی دارد.

بیایید یک پیام را امضا کنیم:

```
$ echo "I'm Jadi and I'm glad that you reached to the end of your LPIC study" > message-jadi.txt
$ gpg --output message-jadi.sig --sign message-jadi.txt
```

اکنون برای من کافی است که `message-jadi.sig` را در اینترنت منتشر کنم یا برای کسی ارسال کنم. اگر آنها می خواهند مطمئن شوند که واقعاً از من ارسال می شود، کافی است امضای من را بررسی کنند (بدیهی است پس از وارد کردن کلید عمومی من):

```
jadi@debian:~$ gpg --verify message-jadi.sig
gpg: Signature made Sun 17 Sep 2023 09:26:15 AM EDT
gpg:                using RSA key E279681DC09318AB5B23D359C9063DD26365986A
gpg: Good signature from "Jadi M <jadijadi@gmail.com>" [ultimate]
```

این فقط امضا را بررسی می‌کند، در صورتی که آنها نیاز به رمزگشایی پیامی را که باید به شرح زیر انجام می‌دادند:

```
jadi@debian:~$ gpg --output message.jadi --decrypt message-jadi.sig
gpg: Signature made Sun 17 Sep 2023 09:26:15 AM EDT
gpg:                using RSA key E279681DC09318AB5B23D359C9063DD26365986A
gpg: Good signature from "Jadi M <jadijadi@gmail.com>" [ultimate]
jadi@debian:~$ cat message.jadi
I'm Jadi and I'm glad that you reached to the end of your LPIC study
```

لطفاً به گزینه `--clearsign` نیز توجه کنید. این گزینه یک فایل با پایان `.asc` ایجاد می کند که حاوی پیام اصلی رمزگذاری نشده (متن پاک) در کنار امضا است. به این ترتیب افراد غیرمتخصص فناوری نیز می‌توانند پیام را بخوانند و فقط در صورت تمایل، او می‌تواند `--verify` امضا کند.

```text
jadi@debian:~$ cat message-jadi.txt
I'm Jadi and I'm glad that you reached to the end of your LPIC study
jadi@debian:~$ gpg --clearsign message-jadi.txt
jadi@debian:~$ ls -ltrh
total 16M
drwxr-xr-x 27 jadi jadi 4.0K Jun 15 09:00 rust-for-linux
drwxr-xr-x  2 jadi jadi 4.0K Jun 15 09:09 Downloads
drwx------  2 jadi jadi 4.0K Jul 17 10:53 BRF
-rw-r--r--  1 jadi jadi    6 Jul 17 10:57 myfile
drwxr-xr-x  5 jadi jadi 4.0K Jul 25 13:34 nltk_data
drwxr-xr-x  4 jadi jadi 4.0K Aug 13 07:29 w
-rw-r--r--  1 jadi jadi  16M Aug 24 01:15 nvim-linux64.tar.gz
drwxr-xr-x  6 jadi jadi 4.0K Aug 24 05:38 nvim-linux64
-rw-r--r--  1 jadi jadi 3.8K Aug 27 15:49 report.xml
-rw-r--r--  1 jadi jadi 1.8K Sep 17 08:50 jadi.pub.key
-rw-r--r--  1 jadi jadi   69 Sep 17 09:26 message-jadi.txt
-rw-r--r--  1 jadi jadi  549 Sep 17 09:26 message-jadi.sig
-rw-r--r--  1 jadi jadi   69 Sep 17 09:27 message.jadi
-rw-r--r--  1 jadi jadi  777 Sep 17 09:28 message-jadi.txt.asc
jadi@debian:~$ cat message-jadi.txt.asc
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA512

I'm Jadi and I'm glad that you reached to the end of your LPIC study
-----BEGIN PGP SIGNATURE-----

iQGzBAEBCgAdFiEE4nloHcCTGKtbI9NZyQY90mNlmGoFAmUG/xYACgkQyQY90mNl
mGqpXQv/QNv0NlCR+S7HJhxiOZcKXE3RB1sx4jRVrOtMd6ZoXYLb28Zz4xN/Lzh2
sipohDbNttr1ovNZvMMu83bbuSeViY9L7nvjNjKsY50u5V1KnrMJPHRaGV8g/0p2
t5zFJuzSFWXQczIjjXMpoLVH8jK3mJuBOmVFwLuBqUoW8827tCLIdr1DNyHXBW47
fcLK5/bO/ljdwGnAX46d+Prg0TIfMLjPpb7uFXVkRBo+zMtCEVDGObaVHQ3J8t6w
8i2YgMrmA3h9h4Gy/yM9Agb2kPeKl6iToeCfQ0EwTcnPF1TN0KZ1PS8Pr3Jp3LcS
A+p32zj7YTzTeE1uBAb7/BorBqaArX8HtLe15yFkNKhPluXya9GG4/Nsxk33Qpd3
c1KiLK9YhTFy7u+Q6tbTKG+uuGj71wANhkqRP30iMjLcBQ7aAO3ehVSYZFyZ7dbL
SJollwyG1sf4zH0g5SQZOxpjyz874IrlFc7GldDCr5jXZw6H+4NuY2yiVWKAcOcU
Qv23xWL2
=q81y
-----END PGP SIGNATURE-----
jadi@debian:~$ gpg --verify message-jadi.txt.asc
gpg: Signature made Sun 17 Sep 2023 09:28:54 AM EDT
gpg:                using RSA key E279681DC09318AB5B23D359C9063DD26365986A
gpg: Good signature from "Jadi M <jadijadi@gmail.com>" [ultimate]
gpg: WARNING: not a detached signature; file 'message-jadi.txt' was NOT verified!
```

> در اینجا `--clearsign` به gpg می گوید که پیام متنی واضح را نیز در فایل خروجی قرار دهد. فایل خروجی originalfile.asc خواهد بود

و یکی دیگر برای تأیید اینکه یک سند به درستی نوشته شده است:

```text
gpg --verify recievedfile
```


#### gpg-agent
درست مانند `ssh-agent`، `gpg-agent` ابزاری است که مانند یک مدیر رمز عبور برای کلیدهای gpg شما عمل می کند. این کلیدها را در حافظه نگه می دارد، بنابراین نیازی به ارائه رمز عبور در هر بار استفاده ندارید.