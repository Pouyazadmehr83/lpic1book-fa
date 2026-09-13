Title: 108.4 چاپگرها و چاپ را مدیریت کنید
Date: 2010-12-03 10:20
Category: LPIC1
Tags: LPIC1, 102, LPIC1-102-500
Authors: Jadi
sortorder: 390
Summary: 

_وزن: 2_

داوطلبان باید بتوانند صف های چاپ و کارهای چاپی کاربر را با استفاده از CUPS و رابط سازگاری LPD مدیریت کنند.

### حوزه های دانش کلیدی

* پیکربندی پایه CUPS (برای چاپگرهای محلی و راه دور).
* صف های چاپ کاربر را مدیریت کنید.
* عیب یابی مشکلات کلی چاپ.
* کارها را از صف های چاپگر پیکربندی شده اضافه و حذف کنید.

### شرایط و امکانات

* فایل‌ها، ابزارها و ابزارهای پیکربندی CUPS
* `/etc/cups/`
* رابط قدیمی lpd \(lpr، lprm، lpq\)

<iframe width="560" height="315" src="https://www.youtube.com/embed/8I9J0gsLe-U" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## فنجان

اکثر توزیع های لینوکس از بسته CUPS برای چاپ استفاده می کنند. ممکن است لازم باشد آن را از طریق مدیریت بسته خود نصب کنید و سرویس آن را با استفاده از systemd یا سیستم init که سیستم شما استفاده می کند، شروع کنید.

```
$ sudo apt install cups
[sudo] password for jadi:
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following additional packages will be installed:
  acl avahi-daemon colord colord-data cups-browsed cups-client cups-common cups-core-drivers
  cups-daemon cups-filters cups-filters-core-drivers cups-ipp-utils cups-ppdc
  cups-server-common fonts-droid-fallback fonts-noto-mono fonts-urw-base35 ghostscript
  ipp-usb libavahi-core7 libavahi-glib1 libcolorhug2 libcupsfilters1 libdaemon0 libexif12
  libfontembed1 libgphoto2-6 libgphoto2-l10n libgphoto2-port12 libgs-common libgs10
  libgs10-common libgusb2 libidn12 libieee1284-3 libijs-0.35 libjbig2dec0 libjson-glib-1.0-0
  libjson-glib-1.0-common liblouis-data liblouis20 liblouisutdml-bin liblouisutdml-data
  liblouisutdml9 libltdl7 libnss-mdns libpaper-utils libpaper1 libpoppler-cpp0v5
  libpoppler-glib8 libpoppler126 libqpdf29 libsane-common libsane1 libsnmp-base libsnmp40
  lynx lynx-common mailcap poppler-data poppler-utils sane-airscan sane-utils update-inetd
  usb.ids
Suggested packages:
  avahi-autoipd colord-sensor-argyll cups-bsd cups-pdf foomatic-db-compressed-ppds
  | foomatic-db smbclient antiword docx2txt imagemagick fonts-noto fonts-freefont-otf
  | fonts-freefont-ttf fonts-texgyre gphoto2 ooo2dbk rtf2xml avahi-autoipd | zeroconf hplip
  snmp-mibs-downloader fonts-japanese-mincho | fonts-ipafont-mincho fonts-arphic-ukai
  fonts-arphic-uming fonts-nanum unpaper
The following NEW packages will be installed:
  acl avahi-daemon colord colord-data cups cups-browsed cups-client cups-common
  cups-core-drivers cups-daemon cups-filters cups-filters-core-drivers cups-ipp-utils
  cups-ppdc cups-server-common fonts-droid-fallback fonts-noto-mono fonts-urw-base35
  ghostscript ipp-usb libavahi-core7 libavahi-glib1 libcolorhug2 libcupsfilters1 libdaemon0
  libexif12 libfontembed1 libgphoto2-6 libgphoto2-l10n libgphoto2-port12 libgs-common
  libgs10 libgs10-common libgusb2 libidn12 libieee1284-3 libijs-0.35 libjbig2dec0
  libjson-glib-1.0-0 libjson-glib-1.0-common liblouis-data liblouis20 liblouisutdml-bin
  liblouisutdml-data liblouisutdml9 libltdl7 libnss-mdns libpaper-utils libpaper1
  libpoppler-cpp0v5 libpoppler-glib8 libpoppler126 libqpdf29 libsane-common libsane1
  libsnmp-base libsnmp40 lynx lynx-common mailcap poppler-data poppler-utils sane-airscan
  sane-utils update-inetd usb.ids
0 upgraded, 66 newly installed, 0 to remove and 7 not upgraded.
Need to get 40.7 MB of archives.
After this operation, 163 MB of additional disk space will be used.
Do you want to continue? [Y/n]
...
...
```

CUPS مخفف Common Unix Printing System است و همانطور که می بینید، بسیاری از بسته های مرتبط را نصب می کند و حتی برخی دیگر را پیشنهاد می کند. این به این دلیل است که CUPS به اطلاعات زیادی در مورد چاپگرهای مختلف نیاز دارد و از ابزارهای زیادی برای چاپ استفاده می کند. پس از نصب، باید سرویس را راه اندازی کنید:

```
$ sudo systemctl start cups.service
$ sudo systemctl status cups.service
● cups.service - CUPS Scheduler
     Loaded: loaded (/lib/systemd/system/cups.service; enabled; preset: enabled)
     Active: active (running) since Sun 2023-07-16 13:50:20 EDT; 27s ago
TriggeredBy: ● cups.path
             ● cups.socket
       Docs: man:cupsd(8)
   Main PID: 2366 (cupsd)
     Status: "Scheduler is running..."
      Tasks: 1 (limit: 4583)
     Memory: 2.8M
        CPU: 400ms
     CGroup: /system.slice/cups.service
             └─2366 /usr/sbin/cupsd -l

Jul 16 13:50:20 debian systemd[1]: Starting cups.service - CUPS Scheduler...
Jul 16 13:50:20 debian systemd[1]: Started cups.service - CUPS Scheduler.
```

برای دسترسی به خدمات CUPS، راه‌های مختلفی وجود دارد، از جمله یک رابط مبتنی بر وب، برنامه‌های رابط کاربری گرافیکی در حالت‌های گرافیکی و حتی ابزارهای خط فرمان (Command Line). CUPS به گونه ای طراحی شده است که ساده باشد و بتواند از چاپگرهای مختلف از فروشندگان مختلف استفاده کند.

فایل های پیکربندی ###

مانند سایر برنامه های لینوکس، CUPS پیکربندی خود را در فهرست `/etc` ذخیره می کند.

```
# ls /etc/cups/
cups-browsed.conf  cups-files.conf  ppd		   raw.convs  snmp.conf  subscriptions.conf
cupsd.conf	   interfaces	    printers.conf  raw.types  ssl	 subscriptions.conf.O
```

فایل پیکربندی اصلی `cupsd.conf` است. نگاهی به آن بیندازید؛ درک آن بسیار آسان است. به عنوان مثال، خط `Listen localhost:631` به CUPS می‌گوید که در پورت localhost 631 گوش کند. در اینجا یک نمونه وجود دارد:

```
$ cat /etc/cups/cupsd.conf
#
# Configuration file for the CUPS scheduler.  See "man cupsd.conf" for a
# complete description of this file.
#

# Log general information in error_log - change "warn" to "debug"
# for troubleshooting...
LogLevel warn
PageLogFormat

# Specifies the maximum size of the log files before they are rotated.  The value "0" disables log rotation.
MaxLogSize 0

# Default error policy for printers
ErrorPolicy retry-job

# Only listen for connections from the local machine.
Listen localhost:631
Listen /run/cups/cups.sock

# Show shared printers on the local network.
Browsing Yes
BrowseLocalProtocols dnssd

# Default authentication type, when authentication is required...
DefaultAuthType Basic

# Web interface setting...
WebInterface Yes

# Timeout after cupsd exits if idle (applied only if cupsd runs on-demand - with -l)
IdleExitTimeout 60

# Restrict access to the server...
<Location />
  Order allow,deny
</Location>

# Restrict access to the admin pages...
<Location /admin>
  Order allow,deny
</Location>

# Restrict access to configuration files...
<Location /admin/conf>
  AuthType Default
  Require user @SYSTEM
  Order allow,deny
</Location>

# Restrict access to log files...
<Location /admin/log>
  AuthType Default
  Require user @SYSTEM
  Order allow,deny
</Location>

# Set the default printer/job policies...
<Policy default>
  # Job/subscription privacy...
  JobPrivateAccess default
  JobPrivateValues default
  SubscriptionPrivateAccess default
  SubscriptionPrivateValues default

  # Job-related operations must be done by the owner or an administrator...
  <Limit Create-Job Print-Job Print-URI Validate-Job>
    Order deny,allow
  </Limit>

  <Limit Send-Document Send-URI Hold-Job Release-Job Restart-Job Purge-Jobs Set-Job-Attributes Create-Job-Subscription Renew-Subscription Cancel-Subscription Get-Notifications Reprocess-Job Cancel-Current-Job Suspend-Current-Job Resume-Job Cancel-My-Jobs Close-Job CUPS-Move-Job CUPS-Get-Document>
    Require user @OWNER @SYSTEM
    Order deny,allow
  </Limit>

  # All administration operations require an administrator to authenticate...
  <Limit CUPS-Add-Modify-Printer CUPS-Delete-Printer CUPS-Add-Modify-Class CUPS-Delete-Class CUPS-Set-Default CUPS-Get-Devices>
    AuthType Default
    Require user @SYSTEM
    Order deny,allow
  </Limit>

  # All printer operations require a printer operator to authenticate...
  <Limit Pause-Printer Resume-Printer Enable-Printer Disable-Printer Pause-Printer-After-Current-Job Hold-New-Jobs Release-Held-New-Jobs Deactivate-Printer Activate-Printer Restart-Printer Shutdown-Printer Startup-Printer Promote-Job Schedule-Job-After Cancel-Jobs CUPS-Accept-Jobs CUPS-Reject-Jobs>
    AuthType Default
    Require user @SYSTEM
    Order deny,allow
  </Limit>

  # Only the owner or an administrator can cancel or authenticate a job...
  <Limit Cancel-Job CUPS-Authenticate-Job>
    Require user @OWNER @SYSTEM
    Order deny,allow
  </Limit>

  <Limit All>
    Order deny,allow
  </Limit>
</Policy>

# Set the authenticated printer/job policies...
<Policy authenticated>
  # Job/subscription privacy...
  JobPrivateAccess default
  JobPrivateValues default
  SubscriptionPrivateAccess default
  SubscriptionPrivateValues default

  # Job-related operations must be done by the owner or an administrator...
  <Limit Create-Job Print-Job Print-URI Validate-Job>
    AuthType Default
    Order deny,allow
  </Limit>

  <Limit Send-Document Send-URI Hold-Job Release-Job Restart-Job Purge-Jobs Set-Job-Attributes Create-Job-Subscription Renew-Subscription Cancel-Subscription Get-Notifications Reprocess-Job Cancel-Current-Job Suspend-Current-Job Resume-Job Cancel-My-Jobs Close-Job CUPS-Move-Job CUPS-Get-Document>
    AuthType Default
    Require user @OWNER @SYSTEM
    Order deny,allow
  </Limit>

  # All administration operations require an administrator to authenticate...
  <Limit CUPS-Add-Modify-Printer CUPS-Delete-Printer CUPS-Add-Modify-Class CUPS-Delete-Class CUPS-Set-Default>
    AuthType Default
    Require user @SYSTEM
    Order deny,allow
  </Limit>

  # All printer operations require a printer operator to authenticate...
  <Limit Pause-Printer Resume-Printer Enable-Printer Disable-Printer Pause-Printer-After-Current-Job Hold-New-Jobs Release-Held-New-Jobs Deactivate-Printer Activate-Printer Restart-Printer Shutdown-Printer Startup-Printer Promote-Job Schedule-Job-After Cancel-Jobs CUPS-Accept-Jobs CUPS-Reject-Jobs>
    AuthType Default
    Require user @SYSTEM
    Order deny,allow
  </Limit>

  # Only the owner or an administrator can cancel or authenticate a job...
  <Limit Cancel-Job CUPS-Authenticate-Job>
    AuthType Default
    Require user @OWNER @SYSTEM
    Order deny,allow
  </Limit>

  <Limit All>
    Order deny,allow
  </Limit>
</Policy>

# Set the kerberized printer/job policies...
<Policy kerberos>
  # Job/subscription privacy...
  JobPrivateAccess default
  JobPrivateValues default
  SubscriptionPrivateAccess default
  SubscriptionPrivateValues default

  # Job-related operations must be done by the owner or an administrator...
  <Limit Create-Job Print-Job Print-URI Validate-Job>
    AuthType Negotiate
    Order deny,allow
  </Limit>

  <Limit Send-Document Send-URI Hold-Job Release-Job Restart-Job Purge-Jobs Set-Job-Attributes Create-Job-Subscription Renew-Subscription Cancel-Subscription Get-Notifications Reprocess-Job Cancel-Current-Job Suspend-Current-Job Resume-Job Cancel-My-Jobs Close-Job CUPS-Move-Job CUPS-Get-Document>
    AuthType Negotiate
    Require user @OWNER @SYSTEM
    Order deny,allow
  </Limit>

  # All administration operations require an administrator to authenticate...
  <Limit CUPS-Add-Modify-Printer CUPS-Delete-Printer CUPS-Add-Modify-Class CUPS-Delete-Class CUPS-Set-Default>
    AuthType Default
    Require user @SYSTEM
    Order deny,allow
  </Limit>

  # All printer operations require a printer operator to authenticate...
  <Limit Pause-Printer Resume-Printer Enable-Printer Disable-Printer Pause-Printer-After-Current-Job Hold-New-Jobs Release-Held-New-Jobs Deactivate-Printer Activate-Printer Restart-Printer Shutdown-Printer Startup-Printer Promote-Job Schedule-Job-After Cancel-Jobs CUPS-Accept-Jobs CUPS-Reject-Jobs>
    AuthType Default
    Require user @SYSTEM
    Order deny,allow
  </Limit>

  # Only the owner or an administrator can cancel or authenticate a job...
  <Limit Cancel-Job CUPS-Authenticate-Job>
    AuthType Negotiate
    Require user @OWNER @SYSTEM
    Order deny,allow
  </Limit>

  <Limit All>
    Order deny,allow
  </Limit>
</Policy>
jadi@debian:~$
Broadcast message from root@debian on pts/3 (Sun 2023-07-16 20:54:04 EDT):

The system will power off now!

Connection to 192.168.64.7 closed by remote host.
Connection to 192.168.64.7 closed.
➜  lpic1book ssh jadi@192.168.64.7
jadi@192.168.64.7's password:
Linux debian 6.1.0-9-arm64 #1 SMP Debian 6.1.27-1 (2023-05-08) aarch64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
You have no mail.
Last login: Mon Jul 17 08:13:13 2023
jadi@debian:~$ sudo su -
[sudo] password for jadi:
root@debian:~# cd /etc/cups/
root@debian:/etc/cups# ls
cups-browsed.conf  cups-files.conf  ppd		   raw.convs  snmp.conf  subscriptions.conf
cupsd.conf	   interfaces	    printers.conf  raw.types  ssl	 subscriptions.conf.O
root@debian:/etc/cups# cd
root@debian:~# ls /etc/cups/
cups-browsed.conf  cups-files.conf  ppd		   raw.convs  snmp.conf  subscriptions.conf
cupsd.conf	   interfaces	    printers.conf  raw.types  ssl	 subscriptions.conf.O
root@debian:~# cat /etc/cups/cupsd.conf
#
# Configuration file for the CUPS scheduler.  See "man cupsd.conf" for a
# complete description of this file.
#

# Log general information in error_log - change "warn" to "debug"
# for troubleshooting...
LogLevel warn
PageLogFormat

# Specifies the maximum size of the log files before they are rotated.  The value "0" disables log rotation.
MaxLogSize 0

# Default error policy for printers
ErrorPolicy retry-job

# Only listen for connections from the local machine.
Listen localhost:631
Listen /run/cups/cups.sock

# Show shared printers on the local network.
Browsing Yes
BrowseLocalProtocols dnssd

# Default authentication type, when authentication is required...
DefaultAuthType Basic

# Web interface setting...
WebInterface Yes

# Timeout after cupsd exits if idle (applied only if cupsd runs on-demand - with -l)
IdleExitTimeout 60

# Restrict access to the server...
<Location />
  Order allow,deny
</Location>

# Restrict access to the admin pages...
<Location /admin>
  Order allow,deny
</Location>

# Restrict access to configuration files...
<Location /admin/conf>
  AuthType Default
  Require user @SYSTEM
  Order allow,deny
</Location>

# Restrict access to log files...
<Location /admin/log>
  AuthType Default
  Require user @SYSTEM
  Order allow,deny
</Location>

# Set the default printer/job policies...
<Policy default>
  # Job/subscription privacy...
  JobPrivateAccess default
  JobPrivateValues default
  SubscriptionPrivateAccess default
  SubscriptionPrivateValues default

  # Job-related operations must be done by the owner or an administrator...
  <Limit Create-Job Print-Job Print-URI Validate-Job>
    Order deny,allow
  </Limit>

  <Limit Send-Document Send-URI Hold-Job Release-Job Restart-Job Purge-Jobs Set-Job-Attributes Create-Job-Subscription Renew-Subscription Cancel-Subscription Get-Notifications Reprocess-Job Cancel-Current-Job Suspend-Current-Job Resume-Job Cancel-My-Jobs Close-Job CUPS-Move-Job CUPS-Get-Document>
    Require user @OWNER @SYSTEM
    Order deny,allow
  </Limit>

  # All administration operations require an administrator to authenticate...
  <Limit CUPS-Add-Modify-Printer CUPS-Delete-Printer CUPS-Add-Modify-Class CUPS-Delete-Class CUPS-Set-Default CUPS-Get-Devices>
    AuthType Default
    Require user @SYSTEM
    Order deny,allow
  </Limit>

  # All printer operations require a printer operator to authenticate...
  <Limit Pause-Printer Resume-Printer Enable-Printer Disable-Printer Pause-Printer-After-Current-Job Hold-New-Jobs Release-Held-New-Jobs Deactivate-Printer Activate-Printer Restart-Printer Shutdown-Printer Startup-Printer Promote-Job Schedule-Job-After Cancel-Jobs CUPS-Accept-Jobs CUPS-Reject-Jobs>
    AuthType Default
    Require user @SYSTEM
    Order deny,allow
  </Limit>

  # Only the owner or an administrator can cancel or authenticate a job...
  <Limit Cancel-Job CUPS-Authenticate-Job>
    Require user @OWNER @SYSTEM
    Order deny,allow
  </Limit>

  <Limit All>
    Order deny,allow
  </Limit>
</Policy>

# Set the authenticated printer/job policies...
<Policy authenticated>
  # Job/subscription privacy...
  JobPrivateAccess default
  JobPrivateValues default
  SubscriptionPrivateAccess default
  SubscriptionPrivateValues default

  # Job-related operations must be done by the owner or an administrator...
  <Limit Create-Job Print-Job Print-URI Validate-Job>
    AuthType Default
    Order deny,allow
  </Limit>

  <Limit Send-Document Send-URI Hold-Job Release-Job Restart-Job Purge-Jobs Set-Job-Attributes Create-Job-Subscription Renew-Subscription Cancel-Subscription Get-Notifications Reprocess-Job Cancel-Current-Job Suspend-Current-Job Resume-Job Cancel-My-Jobs Close-Job CUPS-Move-Job CUPS-Get-Document>
    AuthType Default
    Require user @OWNER @SYSTEM
    Order deny,allow
  </Limit>

  # All administration operations require an administrator to authenticate...
  <Limit CUPS-Add-Modify-Printer CUPS-Delete-Printer CUPS-Add-Modify-Class CUPS-Delete-Class CUPS-Set-Default>
    AuthType Default
    Require user @SYSTEM
    Order deny,allow
  </Limit>

  # All printer operations require a printer operator to authenticate...
  <Limit Pause-Printer Resume-Printer Enable-Printer Disable-Printer Pause-Printer-After-Current-Job Hold-New-Jobs Release-Held-New-Jobs Deactivate-Printer Activate-Printer Restart-Printer Shutdown-Printer Startup-Printer Promote-Job Schedule-Job-After Cancel-Jobs CUPS-Accept-Jobs CUPS-Reject-Jobs>
    AuthType Default
    Require user @SYSTEM
    Order deny,allow
  </Limit>

  # Only the owner or an administrator can cancel or authenticate a job...
  <Limit Cancel-Job CUPS-Authenticate-Job>
    AuthType Default
    Require user @OWNER @SYSTEM
    Order deny,allow
  </Limit>

  <Limit All>
    Order deny,allow
  </Limit>
</Policy>

# Set the kerberized printer/job policies...
<Policy kerberos>
  # Job/subscription privacy...
  JobPrivateAccess default
  JobPrivateValues default
  SubscriptionPrivateAccess default
  SubscriptionPrivateValues default

  # Job-related operations must be done by the owner or an administrator...
  <Limit Create-Job Print-Job Print-URI Validate-Job>
    AuthType Negotiate
    Order deny,allow
  </Limit>

  <Limit Send-Document Send-URI Hold-Job Release-Job Restart-Job Purge-Jobs Set-Job-Attributes Create-Job-Subscription Renew-Subscription Cancel-Subscription Get-Notifications Reprocess-Job Cancel-Current-Job Suspend-Current-Job Resume-Job Cancel-My-Jobs Close-Job CUPS-Move-Job CUPS-Get-Document>
    AuthType Negotiate
    Require user @OWNER @SYSTEM
    Order deny,allow
  </Limit>

  # All administration operations require an administrator to authenticate...
  <Limit CUPS-Add-Modify-Printer CUPS-Delete-Printer CUPS-Add-Modify-Class CUPS-Delete-Class CUPS-Set-Default>
    AuthType Default
    Require user @SYSTEM
    Order deny,allow
  </Limit>

  # All printer operations require a printer operator to authenticate...
  <Limit Pause-Printer Resume-Printer Enable-Printer Disable-Printer Pause-Printer-After-Current-Job Hold-New-Jobs Release-Held-New-Jobs Deactivate-Printer Activate-Printer Restart-Printer Shutdown-Printer Startup-Printer Promote-Job Schedule-Job-After Cancel-Jobs CUPS-Accept-Jobs CUPS-Reject-Jobs>
    AuthType Default
    Require user @SYSTEM
    Order deny,allow
  </Limit>

  # Only the owner or an administrator can cancel or authenticate a job...
  <Limit Cancel-Job CUPS-Authenticate-Job>
    AuthType Negotiate
    Require user @OWNER @SYSTEM
    Order deny,allow
  </Limit>

  <Limit All>
    Order deny,allow
  </Limit>
</Policy>
```

همه داده‌های چاپگر در `/etc/cups/printers.conf` ذخیره می‌شوند. رابط وب یا هر رابط کاربری گرافیکی دیگری در واقع این فایل را ویرایش می کند.

```
# cat /etc/cups/printers.conf
# Printer configuration file for CUPS v2.4.2
# Written by cupsd
# DO NOT EDIT THIS FILE WHEN CUPSD IS RUNNING
NextPrinterId 2
<Printer MyPrinter>
PrinterId 1
UUID urn:uuid:cea56d60-93a0-31bf-443b-5a7288e2cd51
Info My Printer
Location other room
MakeModel HP DesignJet 600 pcl, 1.0
DeviceURI http://thatprinter:631/ipp/
State Idle
StateTime 1689596391
ConfigTime 1689596367
Type 8450116
Accepting Yes
Shared Yes
JobSheets none none
QuotaPeriod 0
PageLimit 0
KLimit 0
OpPolicy default
ErrorPolicy retry-job
</Printer>
```

دایرکتوری (پوشه) پیکربندی مهم دیگر در `/etc/cups/ppd/` قرار دارد. این دایرکتوری (پوشه) حاوی فایل های توضیحات چاپگر PostScript (PPD) است. اینها به چاپگرهایی که از آنها استفاده می کنند اجازه می دهند به درستی کار کنند. 

برای پیدا کردن گزارش‌های CUPS، دایرکتوری (پوشه) `/var/log` را بررسی کنید:

```
# ls /var/log/cups/
access_log  error_log
```
### رابط وب CUPS
برای فعال کردن رابط وب CUPS، باید پیکربندی زیر را در `/etc/cups/cupsd.conf` فعال کنید:

```
WebInterface Yes
```

سپس از طریق پورت **631** به رابط کاربری گرافیکی دسترسی خواهید داشت. بنابراین کافی است از مرورگر خود به **localhost:631** یا **127.0.0.1:631** (یا آدرس **IP** سرور در پورت **631**) دسترسی داشته باشید.

![CUPS web interface on port 631](/images/cups_we_interface.png)

برخی از بخش های مهم در صفحه بالا وجود دارد:

|بخش|استفاده|
|-------|-----|
| مدیریت |افزودن چاپگرها، مدیریت کارها و پیکربندی سرور CUPS |
| مشاغل | بررسی مشاغل فعال، در انتظار و تکمیل شده |  
| چاپگر | فهرست یا جستجو در چاپگرهای نصب شده |

به طور پیش‌فرض، کاربران سیستم می‌توانند چاپگرها و کارهای در صف را مشاهده کنند، اما تغییرات (مانند افزودن چاپگرها) به دسترسی بیشتری نیاز دارد. این در قسمت پایین فایل `cupsd.conf` پیکربندی شده است. به عنوان مثال، پیکربندی زیر دسترسی `CUPS-Add-Modify-Printer CUPS-Delete-Printer CUPS-Set-Defaul` را برای هر کسی در گروه `@printer_admin` فراهم می کند.

```
  <Limit CUPS-Add-Modify-Printer CUPS-Delete-Printer CUPS-Set-Default>
    AuthType Default
    Require user @printer_admin
    Order deny,allow
  </Limit>
```

> CUPS اکثر درایورهای رایج چاپگر را نصب کرده است. فقط باید چاپگر را از منوی کشویی انتخاب کنید تا آن را اضافه کنید.


### ابزارهای قدیمی

درست مانند برنامه‌های [MTA](//1083-mail-transfer-agent-mta-basics.html)، CUPS از همه برنامه‌های خط فرمان (Command Line) قدیمی نیز پشتیبانی می‌کند. اینها قبلاً دستورات چاپی در دنیای BSD بودند، بنابراین ممکن است لازم باشد بسته `cups-bsd` را نصب کنید تا به آنها اجازه دهید در محیط CUPS شما کار کنند. جدول زیر دستورات سازگاری چاپ BSD را فهرست می کند:

| فرمان | استفاده |
| :--- | :--- |
| lpr | چاپ یک فایل |
| lpq | نمایش صف چاپ / مشاغل |
| lprm | rm/حذف فایل از صف پرینر |
| lpc | برنامه کنترل / عیب یابی چاپگر |

#### `lpq`

**q** مخفف **صف** است. بنابراین `lpq` صف چاپگر را نشان می دهد و زمانی استفاده می شود که می خواهید کارهای چاپ را ببینید. اگر از سوئیچ `-a` استفاده می کنید، `lpq` کارهای **همه** چاپگرها را فهرست می کند. یا می‌توانید از کلید `-P` برای نمایش کارهای یک چاپگر خاص استفاده کنید. بنابراین دستور زیر کارهای چاپگری به نام Apple-Dot-Matrix را نشان می دهد:

```
# lpq -PApple-Dot-Matrix
Apple-Dot-Matrix is ready and printing
Rank    Owner   Job     File(s)                         Total Size
active  unknown 1       unknown                         7168 bytes
1st     unknown 2       unknown                         2048 bytes
```

> نباید بین `-P` و نام چاپگر فاصله وجود داشته باشد. عجیبه؟ بله :دی

#### `lpr`

این دستور یک کار را به یک چاپگر ارسال می کند. چاپگر از طریق سوئیچ `-P` مشخص می شود.

```
$ lpr -PApple-Dot-Matrix for_print.txt
$ lpq
Apple-Dot-Matrix is ready and printing
Rank    Owner   Job     File(s)                         Total Size
active  jadi    1       Untitled Document 1             7168 bytes
1st     jadi    2       Untitled1                       2048 bytes
2nd     jadi    3       for_print.txt                   1024 bytes
```

> اگر هیچ چاپگری مشخص نشده باشد، از چاپگر پیش فرض استفاده می شود

#### `lprm`

**rm** مخفف **حذف** است. بنابراین دستور `lprm` کارها را از صف حذف می کند. بدیهی است که باید **شناسه شغلی** را ارائه دهید.

```
$ lpq
Apple-Dot-Matrix is ready and printing
Rank    Owner   Job     File(s)                         Total Size
active  jadi    1       Untitled Document 1             7168 bytes
1st     jadi    2       Untitled1                       2048 bytes
2nd     jadi    3       for_print.txt                   1024 bytes
jadi@funlife:/tmp$ lprm 2
jadi@funlife:/tmp$ lpq
Apple-Dot-Matrix is ready and printing
Rank    Owner   Job     File(s)                         Total Size
active  jadi    1       Untitled Document 1             7168 bytes
1st     jadi    3       for_print.txt                   1024 bytes
```

> فقط root می تواند کارهای چاپی افراد دیگر را حذف کند

اگر می‌خواهید همه کارهای چاپگر خاصی را حذف کنید، می‌توانید با `-Pprinter_name -` بروید. بله! این فقط یک خط خط \(`-`\) بعد از نام چاپگر است. به همین دلیل است که به این دستور یک فرمان قدیمی می گویند.

> `lprm -` همه کارهای چاپ را حذف می کند

#### `lpc`

**c** مخفف **کنترل** است. بنابراین `lpc` به شما امکان می دهد وضعیت \(از طریق `lpc status`\) را کنترل، بررسی کنید و چاپگرهای خود را عیب یابی کنید.

```text
$ lpc status
Apple-Dot-Matrix:
    printer is on device 'ipp' speed -1
    queuing is enabled
    printing is enabled
    2 entries
    daemon present
```

در پاسخ فوق،

* **صف فعال است** به ما بگویید که صف می تواند کارهای چاپ جدید را بپذیرد. اگر صف غیرفعال باشد، حتی نمی توانید کارهای جدید را به چاپگر ارسال کنید.
* **چاپ فعال است** به این معنی است که چاپگر در واقع می تواند روی کاغذ چاپ کند. اگر جوهر یا کاغذ چاپگر تمام شده باشد یا کاغذ گیر کرده باشد، این حالت غیرفعال می شود.

اگر با چاپگر خود مشکل دارید یا باید از پذیرش کارهای جدید جلوگیری کنید یا اجازه دهید کارها را بپذیرد اما چاپ واقعی را انجام ندهد، این چهار دستور می تواند به شما کمک کند:

| فرمان | استفاده |
| :--- | :--- |
| فنجان قبول | به صف چاپگر می گوید که کارهای جدید را بپذیرد |
| رد فنجان | به چاپگر می گوید که هر کار جدید را رد کند |
| فنجانی | چاپ واقعی/فیزیکی کارها را فعال می کند |
| فنجان غیرفعال | چاپ فیزیکی کارها را غیرفعال می کند |

> در همه موارد، باید نام چاپگر چاپگر را ارائه دهید. همچنین می توان با استفاده از سوئیچ `-r` دلیل ارائه کرد.

```
$ cupsdisable Apple-Dot-Matrix -r "need more paper"
$ lpc status
Apple-Dot-Matrix:
    printer is on device 'ipp' speed -1
    queuing is enabled
    printing is disabled
    2 entries
    daemon present
```