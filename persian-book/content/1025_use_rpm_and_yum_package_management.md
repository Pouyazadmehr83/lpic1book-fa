Title: 102.5 از مدیریت بسته RPM و YUM استفاده کنید
Date: 2010-12-03 10:20
Category: LPIC1
Tags: LPIC1, 101, LPIC1-101-500
Authors: Jadi
Summary: داوطلبان باید بتوانند مدیریت بسته را با استفاده از RPM، YUM و Zypper انجام دهند.
sortorder: 100

_وزن: 3_

داوطلبان باید بتوانند مدیریت بسته را با استفاده از RPM، YUM و Zypper انجام دهند.

## حوزه های دانش کلیدی
- نصب، نصب مجدد، ارتقا و حذف بسته ها با استفاده از RPM، YUM، و Zypper
- اطلاعات مربوط به بسته های RPM مانند نسخه، وضعیت، وابستگی ها، یکپارچگی و امضاها را به دست آورید.
تعیین کنید که یک بسته چه فایل هایی را ارائه می دهد، و همچنین پیدا کنید که یک فایل خاص از کدام بسته می آید
آگاهی از dnf

در زیر لیستی جزئی از فایل ها، اصطلاحات و ابزارهای استفاده شده آمده است:

## شرایط و امکانات
* دور در دقیقه
* rpm2cpio
* `/etc/yum.conf`
* `/etc/yum.repos.d/`
*آره
* زیپ

## مقدمه

<iframe width="560" height="315" src="https://www.youtube.com/embed/qk6qcEAvf4A" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

**RedHat Package Manager \(RPM\)** و **YellowDog Update Manager \(YUM\)** توسط Fedora، RedHat، RHEL، CentOS، RocksOS، ... برای مدیریت بسته ها استفاده می شود. فرمت بسته RPM نامیده می شود و می تواند توسط ابزارهای `rpm` مدیریت شود، اما اگر می خواهید از مخازن نرم‌افزاری (Repositories) برای نصب، به روز رسانی، جستجو، ... بسته ها یا حتی ارتقاء کل سیستم استفاده کنید، می توانید از دستور `yum` استفاده کنید. برای درک عمیق تر از مخازن نرم‌افزاری (Repositories)، لطفاً به بخش قبلی (102.4) مراجعه کنید. در اینجا من فرض می کنم که شما مفهوم را می دانید.

##خوشمزه
`yum` مدیر بسته‌ها (Package Manager) مورد استفاده سیستم های مبتنی بر RedHat است. فایل های پیکربندی آن در `/etc/yum.conf` و `/etc/yum.repos.d/` قرار دارند. در زیر یک نمونه است.

```
# cat /etc/yum.conf
[main]
cachedir=/var/cache/yum/$basearch/$releasever
keepcache=0
debuglevel=2
logfile=/var/log/yum.log
exactarch=1
obsoletes=1
gpgcheck=1
plugins=1
installonly_limit=3
```

و در اینجا نمونه ای از یک فایل Repo واقعی در سیستم فدورا آمده است:

```
# cat /etc/yum.repos.d/fedora.repo
[fedora]
name=Fedora $releasever - $basearch
#baseurl=http://download.example/pub/fedora/linux/releases/$releasever/Everything/$basearch/os/
metalink=https://mirrors.fedoraproject.org/metalink?repo=fedora-$releasever&arch=$basearch
enabled=1
countme=1
metadata_expire=7d
repo_gpgcheck=0
type=rpm
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-fedora-$releasever-$basearch
skip_if_unavailable=False

[fedora-debuginfo]
name=Fedora $releasever - $basearch - Debug
#baseurl=http://download.example/pub/fedora/linux/releases/$releasever/Everything/$basearch/debug/tree/
metalink=https://mirrors.fedoraproject.org/metalink?repo=fedora-debug-$releasever&arch=$basearch
enabled=0
metadata_expire=7d
repo_gpgcheck=0
type=rpm
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-fedora-$releasever-$basearch
skip_if_unavailable=False

[fedora-source]
name=Fedora $releasever - Source
#baseurl=http://download.example/pub/fedora/linux/releases/$releasever/Everything/source/tree/
metalink=https://mirrors.fedoraproject.org/metalink?repo=fedora-source-$releasever&arch=$basearch
enabled=0
metadata_expire=7d
repo_gpgcheck=0
type=rpm
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-fedora-$releasever-$basearch
skip_if_unavailable=False
```


ما از yum مانند `yum [OPTIONS] [COMMAND] [PACKAGE_NAME]` استفاده می کنیم.

یکی از مهم‌ترین گزینه‌ها `-y` است که به سوالات Y/N _ بله می‌گوید.

و در اینجا می توانید برخی از دستورات را پیدا کنید:

|فرمان|توضیحات|
|-|-|
|update|متادیتا مخزن را به روز می کند و بسته مشخص شده یا همه بسته های نصب شده را به آخرین نسخه های موجود خود ارتقا می دهد.|
|نصب|نصب بسته|
|reinstall|نصب مجدد بسته|
|list|نمایش لیستی از بسته ها|
|اطلاعات|نمایش اطلاعات مربوط به یک بسته|
|remove|پکیج نصب شده را حذف می کند|
|جستجو|جستجوی مخازن نرم‌افزاری (Repositories) بسته ها|
| ارائه می دهد|بررسی کنید که کدام بسته ها یک فایل خاص را ارائه می دهند|
|upgrade|پکیج ها را ارتقا می دهد و بسته های منسوخ را حذف می کند|
|localinstall|نصب از فایل rpm محلی|
|localupdate|به روز رسانی از یک فایل rpm محلی|
|check-update|مخزن ها را برای به روز رسانی بسته های نصب شده بررسی می کند|
|deplist|وابستگی های یک بسته را نشان می دهد|
|groupinstall|گروهی را نصب کنید، بگویید "KDE Plasma Workspaces"|
|history|نمایش تاریخچه استفاده|

این یک نمونه نصب است:

```
# yum install bzr
Last metadata expiration check: 0:00:47 ago on Tue 21 Jun 2022 06:38:00 PM +0430.
Dependencies resolved.
=====================================================================================================================
 Package                                  Architecture       Version                       Repository           Size
=====================================================================================================================
Installing:
 breezy                                   x86_64             3.2.1-3.fc36                  fedora              6.0 M
Installing dependencies:
 libsodium                                x86_64             1.0.18-9.fc36                 fedora              163 k
 python3-bcrypt                           x86_64             3.2.2-1.fc36                  updates              43 k
 python3-certifi                          noarch             2021.10.8-1.fc36              fedora               15 k
 python3-configobj                        noarch             5.0.6-27.fc36                 fedora               63 k
 python3-cryptography                     x86_64             36.0.0-3.fc36                 fedora              1.0 M
 python3-dulwich                          x86_64             0.20.32-1.fc36                fedora              408 k
 python3-httplib2                         noarch             0.20.3-2.fc36                 fedora              122 k
 python3-jeepney                          noarch             0.7.1-2.fc36                  fedora              324 k
 python3-jwt                              noarch             2.4.0-1.fc36                  updates              41 k
 python3-keyring                          noarch             23.6.0-1.fc36                 updates              78 k
 python3-lazr-restfulclient               noarch             0.14.4-2.fc36                 fedora               84 k
 python3-lazr-uri                         noarch             1.0.6-2.fc36                  fedora               33 k
 python3-oauthlib                         noarch             3.0.2-12.fc36                 fedora              169 k
 python3-paramiko                         noarch             2.11.0-1.fc36                 updates             303 k
 python3-patiencediff                     x86_64             0.2.2-4.fc36                  fedora               45 k
 python3-pynacl                           x86_64             1.4.0-5.fc36                  fedora              108 k
 python3-secretstorage                    noarch             3.3.1-4.fc36                  fedora               35 k
 python3-wadllib                          noarch             1.3.6-2.fc36                  fedora               60 k
Installing weak dependencies:
 python3-jwt+crypto                       noarch             2.4.0-1.fc36                  updates             8.9 k
 python3-launchpadlib                     noarch             1.10.15.1-2.fc36              fedora              167 k
 python3-oauthlib+signedtoken             noarch             3.0.2-12.fc36                 fedora              8.5 k
 python3-pyasn1                           noarch             0.4.8-8.fc36                  fedora              134 k

Transaction Summary
=====================================================================================================================
Install  23 Packages

Total download size: 9.4 M
Installed size: 44 M
Is this ok [y/N]: y
Downloading Packages:
(1/23): python3-certifi-2021.10.8-1.fc36.noarch.rpm                                  1.8 kB/s |  15 kB     00:08
(2/23): libsodium-1.0.18-9.fc36.x86_64.rpm                                            15 kB/s | 163 kB     00:10
(3/23): python3-configobj-5.0.6-27.fc36.noarch.rpm                                    10 kB/s |  63 kB     00:06
(4/23): breezy-3.2.1-3.fc36.x86_64.rpm                                               262 kB/s | 6.0 MB     00:23
(5/23): python3-dulwich-0.20.32-1.fc36.x86_64.rpm                                     47 kB/s | 408 kB     00:08
(6/23): python3-cryptography-36.0.0-3.fc36.x86_64.rpm                                 77 kB/s | 1.0 MB     00:13
(7/23): python3-httplib2-0.20.3-2.fc36.noarch.rpm                                    105 kB/s | 122 kB     00:01
(8/23): python3-jeepney-0.7.1-2.fc36.noarch.rpm                                      259 kB/s | 324 kB     00:01
(9/23): python3-launchpadlib-1.10.15.1-2.fc36.noarch.rpm                              74 kB/s | 167 kB     00:02
(10/23): python3-lazr-restfulclient-0.14.4-2.fc36.noarch.rpm                          36 kB/s |  84 kB     00:02
(11/23): python3-lazr-uri-1.0.6-2.fc36.noarch.rpm                                     15 kB/s |  33 kB     00:02
(12/23): python3-oauthlib+signedtoken-3.0.2-12.fc36.noarch.rpm                       4.2 kB/s | 8.5 kB     00:02
(13/23): python3-oauthlib-3.0.2-12.fc36.noarch.rpm                                    58 kB/s | 169 kB     00:02
(14/23): python3-patiencediff-0.2.2-4.fc36.x86_64.rpm                                 15 kB/s |  45 kB     00:02
(15/23): python3-pyasn1-0.4.8-8.fc36.noarch.rpm                                       61 kB/s | 134 kB     00:02
(16/23): python3-pynacl-1.4.0-5.fc36.x86_64.rpm                                       36 kB/s | 108 kB     00:03
(17/23): python3-secretstorage-3.3.1-4.fc36.noarch.rpm                                12 kB/s |  35 kB     00:02
(18/23): python3-wadllib-1.3.6-2.fc36.noarch.rpm                                      24 kB/s |  60 kB     00:02
(19/23): python3-bcrypt-3.2.2-1.fc36.x86_64.rpm                                       16 kB/s |  43 kB     00:02
(20/23): python3-jwt+crypto-2.4.0-1.fc36.noarch.rpm                                  3.2 kB/s | 8.9 kB     00:02
(21/23): python3-jwt-2.4.0-1.fc36.noarch.rpm                                          16 kB/s |  41 kB     00:02
(22/23): python3-keyring-23.6.0-1.fc36.noarch.rpm                                     18 kB/s |  78 kB     00:04
(23/23): python3-paramiko-2.11.0-1.fc36.noarch.rpm                                    38 kB/s | 303 kB     00:08
---------------------------------------------------------------------------------------------------------------------
Total                                                                                177 kB/s | 9.4 MB     00:54
Running transaction check
Transaction check succeeded.
Running transaction test
Transaction test succeeded.
Running transaction
  Preparing        :                                                                                             1/1
  Installing       : python3-cryptography-36.0.0-3.fc36.x86_64                                                  1/23
  Installing       : python3-lazr-uri-1.0.6-2.fc36.noarch                                                       2/23
  Installing       : python3-jeepney-0.7.1-2.fc36.noarch                                                        3/23
  Installing       : python3-httplib2-0.20.3-2.fc36.noarch                                                      4/23
  Installing       : python3-secretstorage-3.3.1-4.fc36.noarch                                                  5/23
  Installing       : python3-keyring-23.6.0-1.fc36.noarch                                                       6/23
  Installing       : python3-wadllib-1.3.6-2.fc36.noarch                                                        7/23
  Installing       : python3-jwt-2.4.0-1.fc36.noarch                                                            8/23
  Installing       : python3-jwt+crypto-2.4.0-1.fc36.noarch                                                     9/23
  Installing       : python3-oauthlib-3.0.2-12.fc36.noarch                                                     10/23
  Installing       : python3-oauthlib+signedtoken-3.0.2-12.fc36.noarch                                         11/23
  Installing       : python3-lazr-restfulclient-0.14.4-2.fc36.noarch                                           12/23
  Installing       : python3-launchpadlib-1.10.15.1-2.fc36.noarch                                              13/23
  Installing       : python3-bcrypt-3.2.2-1.fc36.x86_64                                                        14/23
  Installing       : python3-pyasn1-0.4.8-8.fc36.noarch                                                        15/23
  Installing       : python3-patiencediff-0.2.2-4.fc36.x86_64                                                  16/23
  Installing       : python3-configobj-5.0.6-27.fc36.noarch                                                    17/23
  Installing       : python3-certifi-2021.10.8-1.fc36.noarch                                                   18/23
  Installing       : python3-dulwich-0.20.32-1.fc36.x86_64                                                     19/23
  Installing       : libsodium-1.0.18-9.fc36.x86_64                                                            20/23
  Installing       : python3-pynacl-1.4.0-5.fc36.x86_64                                                        21/23
  Installing       : python3-paramiko-2.11.0-1.fc36.noarch                                                     22/23
  Installing       : breezy-3.2.1-3.fc36.x86_64                                                                23/23
  Running scriptlet: breezy-3.2.1-3.fc36.x86_64                                                                23/23
  Verifying        : breezy-3.2.1-3.fc36.x86_64                                                                 1/23
  Verifying        : libsodium-1.0.18-9.fc36.x86_64                                                             2/23
  Verifying        : python3-certifi-2021.10.8-1.fc36.noarch                                                    3/23
  Verifying        : python3-configobj-5.0.6-27.fc36.noarch                                                     4/23
  Verifying        : python3-cryptography-36.0.0-3.fc36.x86_64                                                  5/23
  Verifying        : python3-dulwich-0.20.32-1.fc36.x86_64                                                      6/23
  Verifying        : python3-httplib2-0.20.3-2.fc36.noarch                                                      7/23
  Verifying        : python3-jeepney-0.7.1-2.fc36.noarch                                                        8/23
  Verifying        : python3-launchpadlib-1.10.15.1-2.fc36.noarch                                               9/23
  Verifying        : python3-lazr-restfulclient-0.14.4-2.fc36.noarch                                           10/23
  Verifying        : python3-lazr-uri-1.0.6-2.fc36.noarch                                                      11/23
  Verifying        : python3-oauthlib+signedtoken-3.0.2-12.fc36.noarch                                         12/23
  Verifying        : python3-oauthlib-3.0.2-12.fc36.noarch                                                     13/23
  Verifying        : python3-patiencediff-0.2.2-4.fc36.x86_64                                                  14/23
  Verifying        : python3-pyasn1-0.4.8-8.fc36.noarch                                                        15/23
  Verifying        : python3-pynacl-1.4.0-5.fc36.x86_64                                                        16/23
  Verifying        : python3-secretstorage-3.3.1-4.fc36.noarch                                                 17/23
  Verifying        : python3-wadllib-1.3.6-2.fc36.noarch                                                       18/23
  Verifying        : python3-bcrypt-3.2.2-1.fc36.x86_64                                                        19/23
  Verifying        : python3-jwt+crypto-2.4.0-1.fc36.noarch                                                    20/23
  Verifying        : python3-jwt-2.4.0-1.fc36.noarch                                                           21/23
  Verifying        : python3-keyring-23.6.0-1.fc36.noarch                                                      22/23
  Verifying        : python3-paramiko-2.11.0-1.fc36.noarch                                                     23/23

Installed:
  breezy-3.2.1-3.fc36.x86_64                                 libsodium-1.0.18-9.fc36.x86_64
  python3-bcrypt-3.2.2-1.fc36.x86_64                         python3-certifi-2021.10.8-1.fc36.noarch
  python3-configobj-5.0.6-27.fc36.noarch                     python3-cryptography-36.0.0-3.fc36.x86_64
  python3-dulwich-0.20.32-1.fc36.x86_64                      python3-httplib2-0.20.3-2.fc36.noarch
  python3-jeepney-0.7.1-2.fc36.noarch                        python3-jwt-2.4.0-1.fc36.noarch
  python3-jwt+crypto-2.4.0-1.fc36.noarch                     python3-keyring-23.6.0-1.fc36.noarch
  python3-launchpadlib-1.10.15.1-2.fc36.noarch               python3-lazr-restfulclient-0.14.4-2.fc36.noarch
  python3-lazr-uri-1.0.6-2.fc36.noarch                       python3-oauthlib-3.0.2-12.fc36.noarch
  python3-oauthlib+signedtoken-3.0.2-12.fc36.noarch          python3-paramiko-2.11.0-1.fc36.noarch
  python3-patiencediff-0.2.2-4.fc36.x86_64                   python3-pyasn1-0.4.8-8.fc36.noarch
  python3-pynacl-1.4.0-5.fc36.x86_64                         python3-secretstorage-3.3.1-4.fc36.noarch
  python3-wadllib-1.3.6-2.fc36.noarch

Complete!

```

همچنین می توانید از حروف عام استفاده کنید:

```text
# yum update 'cal*'
```

> واقعیت جالب: فدورا لینوکس از `dnf` به عنوان مدیر بسته‌ها (Package Manager) خود استفاده می کند و دستورات `yum` شما را به معادل های `dnf` خود ترجمه می کند.

### yumdownloader
این ابزار rpm ها را بدون نصب از مخازن نرم‌افزاری (Repositories) دانلود می کند. اگر می‌خواهید همه وابستگی‌ها را نیز دانلود کنید، از سوئیچ `--resolve` استفاده کنید:

```text
yumdownloader --resolve bzr
```

## دور در دقیقه


<iframe width="560" height="315" src="https://www.youtube.com/embed/0E_EuBUSuz4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

دستور `rpm` می تواند ACTION ها را روی فایل های RPM مجزا اجرا کند. می توانید از آن مانند `rpm ACTION [OPTION] rpm_file.rpm` استفاده کنید

یکی از گزینه های رایج، `-v` برای خروجی پرمخاطب است و اینها ACTION های رایج هستند:

|فرم کوتاه|فرم بلند|توضیحات|
|-|-|-|
|-i|--install|یک بسته را نصب می کند|
|-e|--erase|یک بسته را حذف می کند|
|-U|--upgrade|یک بسته را نصب/ارتقا می‌دهد|
|-q|--query|بررسی می‌کند که آیا بسته نصب شده است|
|-F|--freshen|فقط اگر قبلاً نصب شده باشد به روز رسانی شود|
|-V|--verify|یکپارچگی نصب را بررسی کنید|
|-K|--checksig|یکپارچگی یک بسته rpm را بررسی می کند|


لطفاً توجه داشته باشید که هر عمل ممکن است گزینه های خاص خود را داشته باشد.
### نصب و به روز رسانی
در بیشتر موارد، ما از `-U` استفاده می کنیم که بسته ای را نصب یا ارتقا می دهد. 

* RPM پایگاه داده نصب بسته خودکار ندارد، بنابراین نمی تواند وابستگی های نصب شده به طور خودکار را حذف کند.

اگر یک دور در دقیقه با همه وابستگی‌های آن دارید، می‌توانید با استفاده از `rpm -Uvh *.rpm` آنها را نصب کنید. این به rpm می‌گوید در صورت ارائه در فایل‌های دیگر، از وابستگی‌ها شکایت نکند. در اینجا `-h` 50 علامت هش ایجاد می کند تا پیشرفت را نشان دهد.

در برخی موارد - اگر می‌دانید دارید چه کار می‌کنید - می‌توانید از `--nodeps` برای جلوگیری از بررسی وابستگی استفاده کنید یا حتی از `--force` برای اجبار نصب/ارتقا با وجود همه مشکلات و شکایات استفاده کنید.

### پرس و جو

یک پرس و جو معمولی به این صورت است:

```
[root@fedora tmp]# rpm -q breezy-3.2.1-3.fc36.x86_64.rpm
breezy-3.2.1-3.fc36.x86_64
[root@fedora tmp]# rpm -q breezy
breezy-3.2.1-3.fc36.x86_64
[root@fedora tmp]# rpm -q emacs
package emacs is not installed
```
و می‌توانید از این گزینه‌ها برای تند کردن آن استفاده کنید:

|کوتاه|طولانی|توضیحات|
|-|-|-|
|-c|--configfiles|نمایش فایل های پیکربندی بسته ها|
|-i|--info|اطلاعات تفصیلی درباره یک بسته|
|-a|--all|نمایش همه بسته های نصب شده|
||--whatprovides|نشان می دهد که چه بسته هایی این فایل را ارائه می دهند|
|-l|--list|لیست فایل هایی را که بسته نصب می کند پرس و جو کنید|
|-R|--requires|نمایش وابستگی های یک بسته|
|-f|--file|پرونده مالک بسته پرس و جو|

### تأیید کنید
می توانید بسته های خود را تأیید کنید و ببینید که آیا آنها به درستی نصب شده اند یا خیر. می‌توانید از گزینه `-Vv` برای خروجی کامل استفاده کنید یا فقط از `-V` برای تأیید و مشاهده فقط مشکلات استفاده کنید. این خروجی پس از ویرایش دستی `/bin/tmux` است:

```
[root@fedora tmp]# rpm -V tmux
S.5....T.    /usr/bin/tmux
```

و این بخشی از بخش `man rpm` `-V` است:

```
    S Size differs
    M Mode differs (includes permissions and file type)
    5 digest (formerly MD5 sum) differs
    D Device major/minor number mismatch
    L readLink(2) path mismatch
    U User ownership differs
    G Group ownership differs
    T mTime differs
    P caPabilities differ
```

همچنین می‌توانید یکپارچگی یک بسته دور در دقیقه را با `-K` بررسی کنید:

```
# rpm -Kv breezy-3.2.1-3.fc36.x86_64.rpm
breezy-3.2.1-3.fc36.x86_64.rpm:
    Header V4 RSA/SHA256 Signature, key ID 38ab71f4: OK
    Header SHA256 digest: OK
    Header SHA1 digest: OK
    Payload SHA256 digest: OK
    V4 RSA/SHA256 Signature, key ID 38ab71f4: OK
    MD5 digest: OK
```

خروجی بالا نشان می دهد که این فایل معتبر است.

### حذف نصب کنید
```
[root@fedora tmp]# rpm -e tmux
error: Failed dependencies:
	tmux is needed by (installed) anaconda-install-env-deps-36.16.5-1.fc36.x86_64
```

* دور در دقیقه بسته را بدون درخواست حذف می کند!
* دور در دقیقه بسته ای را که بسته دیگری به آن نیاز دارد حذف نمی کند

### فایل های RPM را استخراج کنید

#### rpm2cpio

**cpio** یک فرمت آرشیو است (درست مانند zip یا rar یا tar). می‌توانید از دستور `rpm2cpio` برای تبدیل فایل‌های RPM به _cpio_ استفاده کنید و سپس از ابزار `cpio` برای استخراج آن‌ها استفاده کنید:

```
[root@fedora tmp]# rpm2cpio breezy-3.2.1-3.fc36.x86_64.rpm > breezy.cpio
[root@fedora tmp]# cpio -idv < breezy.cpio
./usr/bin/brz
./usr/bin/bzr
./usr/bin/bzr-receive-pack
./usr/bin/bzr-upload-pack
./usr/bin/git-remote-brz
./usr/bin/git-remote-bzr
[...]
```

## زیپر
لینوکس SUSE و برادرش openSUSE از ZYpp به عنوان موتور مدیریت بسته خود استفاده می کنند. می توانید از ابزارهای YAST یا Zypper برای برقراری ارتباط با آن استفاده کنید. 

اینها دستورات اصلی استفاده شده در `zypper` هستند:

|فرمان|توضیحات|
|-|-|
|راهنما|کمک عمومی|
|install|یک بسته را نصب می کند|
|info|نمایش اطلاعات یک بسته|
|list-updates|به روز رسانی های موجود را نشان می دهد|
|lr|اطلاعات مخزن را نشان می دهد|
|packages|لیست تمام بسته ها یا بسته های موجود از یک مخزن خاص|
|what-provides|نمایش صاحب یک فایل|
|refresh|اطلاعات مخازن نرم‌افزاری (Repositories) را تازه می کند|
|remove|یک بسته را از سیستم حذف می کند|
|جستجو|جستجوی بسته|
|update|مخزن ها را بررسی می کند و بسته های نصب شده را به روز می کند|
|verify|یک بسته و وابستگی های آن را بررسی می کند|

> هنگام استفاده از `zypper` می توانید فرمان را کوتاه کنید، بنابراین `zypper se tmux` tmux را جستجو می کند.


## ابزارهای دیگر
YUM و RPM مدیران بسته اصلی در Fedora، RHEL و Centos هستند، اما ابزارهای دیگری نیز در دسترس هستند. همانطور که گفته شد، SUSE از `YaST` استفاده می کند، و برخی از دسکتاپ های مدرن \(KDE & Gnome\) از `PackageKit` استفاده می کنند که یک ابزار گرافیکی است. همچنین خوب است توجه داشته باشید که مجموعه `dnf` نیز در حال محبوبیت است و بر روی سیستم های فدورا از قبل نصب شده است.