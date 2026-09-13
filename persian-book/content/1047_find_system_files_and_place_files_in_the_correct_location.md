Title: 104.7 فایل های سیستم را بیابید و فایل ها را در محل صحیح قرار دهید
Date: 2010-12-03 10:20
Category: LPIC1
Tags: LPIC1, 101, LPIC1-101-500
Authors: Jadi
sortorder: 260
Summary: 

_وزن: 2_

داوطلبان باید با **استاندارد سلسله مراتبی سیستم‌فایل (Filesystem) \(FHS\)**، از جمله مکان های معمولی فایل ها و طبقه بندی دایرکتوری (پوشه) ها، کاملاً آشنا باشند.

### حوزه های دانش کلیدی

* مکان صحیح فایل ها را تحت FHS درک کنید.
* فایل ها و دستورات را در یک سیستم لینوکس پیدا کنید.
* مکان و هدف فایل ها و دایرکتوری (پوشه) های مهم را همانطور که در FHS تعریف شده است بدانید.


* `find`
* `locate`
* `updatedb`
* `whereis`
* `which`
* `type`
* `/etc/updatedb.conf`

## FHS

استاندارد سلسله مراتبی سیستم‌فایل (Filesystem) \(FHS\) سندی است که سلسله مراتب فایل لینوکس/یونیکس را توصیف می کند. دانستن این موارد بسیار مفید است زیرا به شما امکان می دهد به راحتی آنچه را که به عنوان مدیر سیستم به دنبال آن هستید پیدا کنید.

| دایرکتوری (پوشه) | استفاده |
| :---: | :--- |
| / | ریشه سلسله مراتب اولیه و دایرکتوری (پوشه) ریشه کل سلسله مراتب سیستم‌فایل (Filesystem) |
| /bin | باینری های دستور ضروری |
| /boot | فایل های استاتیک بوت‌لودر (Bootloader) |
| /dev | فایل های دستگاه |
| /و غیره | پیکربندی سیستم مخصوص میزبان |
| /lib | کتابخانه های مشترک ضروری و ماژول های هسته |
| /رسانه | نقطه نصب برای رسانه های قابل جابجایی |
| /mnt | نقطه اتصال برای نصب موقت فایل سیستم |
| /opt | بسته های نرم افزار کاربردی الحاقی |
| /sbin | باینری های سیستم ضروری |
| /srv | داده های خدمات ارائه شده توسط این سیستم |
| /tmp | فایل های موقت |
| /usr | سلسله مراتب ثانویه |
| /var | داده های متغیر |
| /خانه | فهرست راهنمای کاربر \(اختیاری\) |
| /lib | قالب جایگزین کتابخانه های مشترک ضروری \(اختیاری\) |
| /ریشه | فهرست اصلی برای کاربر اصلی \(اختیاری\) |

</br>

`/usr` دومین سطح سلسله مراتب است. این شامل داده های قابل اشتراک گذاری و فقط خواندنی است. می توان آن را بین سیستم ها به اشتراک گذاشت، اگرچه روش فعلی اغلب این کار را انجام نمی دهد.

سیستم‌فایل (Filesystem) `/var` حاوی فایل های داده متغیر است، از جمله فهرست ها و فایل های قرقره، داده های اداری و گزارش و فایل های موقت و موقت. برخی از بخش‌های var بین سیستم‌های مختلف قابل اشتراک‌گذاری نیستند، اما برخی دیگر مانند /var/mail، /var/cache/man، /var/cache/fonts و /var/spool/news ممکن است به اشتراک گذاشته شوند.

## مسیر

نصب عمومی لینوکس دارای تعداد زیادی فایل است. 741341 فایل در مورد من. پس چگونه پوسته یک فرمان را پیدا کرده و اجرا می کند؟ این کار توسط متغیری به نام PATH انجام می شود:

```text
$ echo $PATH
/home/jadi/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games;/home/jadi/bin/
```

و برای کاربر اصلی:

```text
# echo $PATH
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
```

همانطور که می بینید، این لیست دایرکتوری (پوشه) هایی است که با دو نقطه از هم جدا شده اند. بدیهی است که می توانید مسیر خود را با `export PATH=$PATH:/usr/new/dir` تغییر دهید یا این را در `.bashrc` قرار دهید تا دائمی شود.

## مکان یابی فایل ها

### `which`، `type` و `whereis`

دستور `which` اولین ظاهر دستور داده شده در مسیر را نشان می دهد. به عبارت دیگر `which mkfs` به شما می گوید که اگر این دستور `mkfs` را صادر کنید، چه چیزی اجرا می شود.

```text
$ which mkfs
/usr/bin/mkfs
jadi@ubuntuserver:~$ which ping
/usr/bin/ping
jadi@ubuntuserver:~$ which -a ping
/usr/bin/ping
/bin/ping
```

> از سوئیچ `-a` برای نشان دادن تمام ظاهر در مسیر و نه تنها مورد اول استفاده کنید.

اما دستور `cd` کجاست؟

```
jadi@ubuntuserver:~$ which cd
jadi@ubuntuserver:~$ type cd
cd is a shell builtin
```

همانطور که می بینید، `which` چیزی برای `cd` پیدا نکرد، بنابراین ما آن را با `type` امتحان کردیم تا ببینیم h**l چیست.

```text
$ type type
type is a shell builtin
$ type for
for is a shell keyword
$ type mkfs
mkfs is /sbin/mkfs
$ type chert
bash: type: chert: not found
```

دستور `type` کلی تر از `which` است و همچنین کلمات کلیدی _bash_ را می فهمد و نشان می دهد.

یکی دیگر از دستورات مفید در این دسته، `whereis` است. برخلاف `which`، `whereis` صفحات man و کد منبع برنامه ها را در کنار مکان باینری آنها نشان می دهد.

```text
$ whereis mkfs
mkfs: /usr/sbin/mkfs /usr/share/man/man8/mkfs.8.gz
```

> نکته: یک دستور `whatis` نیز وجود دارد، آن را امتحان کنید.

### پیدا کنید

ما قبلاً این دستور را در [فصل 103.7] (/1037-search-text-files-using-regular-expressions.html) دیده‌ایم، اما اجازه دهید چند سوئیچ جدید را ببینیم.

* `-user` و `-group` کاربر و گروه خاصی را مشخص می کند
* `-maxdepth` به یافتن می گوید که تا چه حد باید به فهرست ها برود.

```text
$ find /tmp/ -maxdepth 1 -user jadi | head
/tmp/1
/tmp/2
```

یا حتی فایل هایی را پیدا کنید که متعلق به هیچ کاربر/گروهی با `-nouser` و `-nogroup` نیستند.

> مانند سایر _تست‌ها، می‌توانید یک `!` را درست قبل از هر عبارتی برای نفی آن اضافه کنید. بنابراین فایل‌هایی را پیدا می‌کند **که** متعلق به jadi نیستند: `find . ! -user jadi`

همچنین استفاده از آن برای فایل هایی با رشته های خاص در نام آنها بسیار رایج است:

```
$ sudo find /etc -iname "*vmware*"
/etc/vmware-tools
/etc/vmware-tools/scripts/vmware
```



### مکان یابی و به روز رسانی b

شما `find` را امتحان کردید و آن را دوست داشتید، اما مشکلی در آن وجود دارد: یک جستجوی فعال زنده انجام می دهد! این می تواند سیستم شما را کند کند یا فشار بیش از حد بر روی سخت افزار شما وارد کند یا روی سیستم های فایل بزرگتر زمان زیادی ببرد. برای حل این مشکل، یک دستور سریعتر وجود دارد:

```
$ locate networking
/etc/cloud/cloud.cfg.d/subiquity-disable-cloudinit-networking.cfg
/snap/core20/1408/usr/lib/python3/dist-packages/cloudinit/distros/networking.py
/snap/core20/1408/usr/lib/python3/dist-packages/cloudinit/distros/__pycache__/networking.cpython-38.pyc
/snap/core20/1826/usr/lib/python3/dist-packages/cloudinit/distros/networking.py
/snap/core20/1826/usr/lib/python3/dist-packages/cloudinit/distros/__pycache__/networking.cpython-38.pyc
/usr/lib/python3/dist-packages/cloudinit/distros/networking.py
/usr/lib/python3/dist-packages/cloudinit/distros/__pycache__/networking.cpython-310.pyc
/usr/lib/python3/dist-packages/sos/report/plugins/networking.py
/usr/lib/python3/dist-packages/sos/report/plugins/__pycache__/networking.cpython-310.pyc
```

و سریع است:

```
$ time locate kernel / | wc -l
16989

real	0m0.091s
user	0m0.094s
sys	0m0.034s
```

این سریع است زیرا داده های آن از یک پایگاه داده ایجاد شده با `updatedb` می آید (بسته آن در دبیان `plocate` نامیده می شود). معمولاً این دستور به صورت خودکار (با یک cronjob) به صورت روزانه اجرا می شود. فایل پیکربندی آن `/etc/updatedb.conf` یا `/etc/sysconfig/locate` است:

```
$ cat /etc/updatedb.conf
PRUNE_BIND_MOUNTS="yes"
# PRUNENAMES=".git .bzr .hg .svn"
PRUNEPATHS="/tmp /var/spool /media /home/.ecryptfs"
PRUNEFS="NFS nfs nfs4 rpc_pipefs afs binfmt_misc proc smbfs autofs iso9660 ncpfs coda devpts ftpfs devfs mfs shfs sysfs cifs lustre tmpfs usbfs udf fuse.glusterfs fuse.sshfs curlftpfs ecryptfs fusesmb devtmpfs"
```

می‌توانید با اجرای `updatedb` به‌عنوان روت، db را به‌روزرسانی کنید.