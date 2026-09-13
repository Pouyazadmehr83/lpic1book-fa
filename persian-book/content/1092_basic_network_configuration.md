Title: 109.2 پیکربندی شبکه پایدار
Date: 2010-12-03 10:20
Category: LPIC1
Tags: LPIC1, 102, LPIC1-102-500
Authors: Jadi
sortorder: 410
Summary: 

_وزن: 4_

کاندیداها باید قادر به مشاهده، تغییر و تأیید تنظیمات پیکربندی در میزبان مشتری باشند.

### حوزه های دانش کلیدی

* پیکربندی اصلی میزبان TCP/IP را بدانید
* پیکربندی شبکه اترنت و وای فای را با استفاده از NetworkManager پیکربندی کنید
* آگاهی از systemd-networkd

### شرایط و امکانات

* `/etc/hostname`
* `/etc/hosts`
* `/etc/nsswitch.conf`
* `/etc/resolv.conf`
* `nmcli`
* `hostnamectl`
* `ifup`
* `ifdown`

### مقدمه

<iframe width="560" height="315" src="https://www.youtube.com/embed/YN8sJuy9df8?si=BEs4RmfvW1zdSUA4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

همانطور که در قسمت قبل دیدیم، هر رایانه شخصی، سرور، لپ تاپ، تلفن، .. باید یک پیکربندی IP (IP، Netmask، Default Gateway، DNS، ...) داشته باشد تا در شبکه به درستی کار کند. این را می توان به روش های مختلف انجام داد. برخی از دستگاه‌ها مانند لپ‌تاپ‌ها دائماً شبکه خود را تغییر می‌دهند و باید بتوانند با تغییرات همراه باشند. برخی از سرورها در تمام طول عمر خود در یک مکان (از لحاظ فیزیکی و شبکه) باقی می مانند و باید این پیکربندی را پس از راه اندازی مجدد، قطع، ارتقاء و تغییرات HW حفظ کنند.

در این بخش خواهیم دید که چگونه می توان به این امر در سیستم های مدرن گنو/لینوکس دست یافت.


### رابط شبکه
NIC (یا کارت رابط شبکه) سخت افزار فیزیکی شبکه در رایانه شما است. این می تواند تراشه + آنتن تلفن همراه شما یا یک کارت اترنت متصل به کابل شبکه در رایانه شخصی شما باشد.

در سیستم‌های قدیمی‌تر، مواردی مانند `eth0`، `eth1`، `eth2`، ... نامیده می‌شدند که در آن 0، 1 و 2 توسط هسته تعیین می‌شدند - بیشتر بر اساس ترتیب بارگیری درایورها. در ماشین‌های لینوکس اخیر، NIC‌ها توسط `wlan0`، `eno1`، `ens1`، `enp3s2` و غیره فراخوانی می‌شوند. این بر اساس برخی داده‌های ملموس‌تر است، مانند `wireless` یا `ethernet`، PCI (`ens`) یا اتوبوسی مانند (`enp`) بودن. 

دستور `ip` می تواند این موارد را نشان دهد:

```
➜  ~ ip link show
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN mode DEFAULT group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
2: wlp108s0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP mode DORMANT group default qlen 1000
    link/ether 00:bb:60:97:6b:07 brd ff:ff:ff:ff:ff:ff
3: docker0: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc noqueue state DOWN mode DEFAULT group default 
    link/ether 02:42:75:d3:e6:ff brd ff:ff:ff:ff:ff:ff
```

> `lo` یک آداپتور شبکه مجازی به نام دستگاه *loopback* است. همیشه وجود دارد و به "این دستگاه یا 127.0.0.1 همانطور که IPv4 آن را می نامد" اشاره می کند.

### پیکربندی کارت های شبکه

<iframe width="560" height="315" src="https://www.youtube.com/embed/KKL-r4eAZHI?si=Av2ehqBv7eoRHuGw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

در توزیع‌های قدیمی‌تر، از `ifconfig` برای بررسی/پیکربندی تنظیمات IP در کارت‌های شبکه استفاده می‌شد. نگاهی بیندازید:

```text
$ ifconfig
enp0s25: flags=4099<UP,BROADCAST,MULTICAST>  mtu 1500
        ether f0:de:f1:62:c5:73  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
        device interrupt 20  memory 0xd1500000-d1520000  

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10<host>
        loop  txqueuelen 1  (Local Loopback)
        RX packets 560719  bytes 339937974 (324.1 MiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 560719  bytes 339937974 (324.1 MiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

wlp3s0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 192.168.1.35  netmask 255.255.255.0  broadcast 192.168.1.255
        inet6 fe80::8ea9:82ff:fe7b:8906  prefixlen 64  scopeid 0x20<link>
        ether 8c:a9:82:7b:89:06  txqueuelen 1000  (Ethernet)
        RX packets 2325385  bytes 2629859900 (2.4 GiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 2023796  bytes 510997240 (487.3 MiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
```

همچنین می توان از `ifconfig` برای تغییر تنظیمات شبکه استفاده کرد، اما باید دسترسی ریشه داشته باشید:

```text
$  sudo ifconfig enp0s25 192.168.42.42
password for jadi:
$ ifconfig enp0s25
enp0s25: flags=4099<UP,BROADCAST,MULTICAST>  mtu 1500
        inet 192.168.42.42  netmask 255.255.255.0  broadcast 192.168.42.255
        ether f0:de:f1:62:c5:73  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
        device interrupt 20  memory 0xd1500000-d1520000  

$
```

اگر می‌خواهید نقاب شبکه یک رابط را تغییر دهید، `ifconfig eth0 netmask 255.255.0.0` را انجام دهید یا همانطور که اغلب ما انجام می‌دادیم، هر دو را در یک دستور صادر کنید:

```text
# ifconfig eth0 192.168.42.42 netmask 255.255.255.0
```

همچنین می توان رابط های _up_ و _down_ \(روشن و خاموش\) را با استفاده از تنظیمات از پیش تعریف شده توسط:

```text
$ sudo ifconfig enp0s25 down
[sudo] password for jadi:
$ ifconfig
lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10<host>
        loop  txqueuelen 1  (Local Loopback)
        RX packets 562273  bytes 340257228 (324.4 MiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 562273  bytes 340257228 (324.4 MiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

wlp3s0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 192.168.1.35  netmask 255.255.255.0  broadcast 192.168.1.255
        inet6 fe80::8ea9:82ff:fe7b:8906  prefixlen 64  scopeid 0x20<link>
        ether 8c:a9:82:7b:89:06  txqueuelen 1000  (Ethernet)
        RX packets 2330388  bytes 2634026235 (2.4 GiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 2027352  bytes 511549072 (487.8 MiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
```

همانطور که می بینید، پایین آوردن رابط، آن را از لیست رابط های فعال حذف کرد، با استفاده از سوئیچ `-a` به `ifconfig` می گوید که همه اینترفیس ها را نشان دهد، حتی اگر خاموش باشند.

در بسیاری از سیستم ها دستورات `ifup` و `ifdown` به طور مستقیم به رابط های بالا و پایین وجود دارد. آنها درست مانند `ifup eth0` کار می کنند.

این پیکربندی‌های از پیش تعریف‌شده در `/etc/network/interfaces` در ماشین‌های مبتنی بر Debian و در `/etc/sysconfig/network-scripts/` در توزیع مبتنی بر RPM قرار دارند. 

این نمونه ای از چنین فایلی در توزیع مبتنی بر RedHat است:

```text
$ cat /etc/sysconfig/network-scripts/ifcfg-eth0
DEVICE=eth0
ONBOOT=yes
TYPE=Ethernet
IPADDR=192.168.1.10
NETMASK=255.255.255.0
DNS1=4.2.2.4
```
در سیستم های RPM، دروازه پیش فرض از طریق فایل زیر پیکربندی می شود:

```text
cat /etc/sysconfig/network
NETWORKING=yes
HOSTNAME=lpictest
GATEWAY=192.168.1.1
```

در سیستم های مبتنی بر دبیان \(از جمله اوبونتو\) فایل پیکربندی اصلی برای رابط های شبکه `/etc/network/interfaces` است. این یک فایل دارای پیکربندی برای تمام رابط ها است. نگاهی بیندازید:

```text
auto lo
iface lo inte loopback

auto eth0
#ifconfig eth0 inet dhcp
iface eth0 inet static
address 192.168.1.10
netmask 255.255.255.0
gateway 192.168.1.1
dns-nameservers 4.2.2.4
```

### `ip` 
توزیع های اخیر بیشتر از دستور `ip` استفاده می کنند. این دستور می‌تواند کارهای زیادی از جمله نمایش و پیکربندی آدرس‌های IP، ماسک‌های شبکه، دروازه‌های پیش‌فرض و قوانین مسیریابی را انجام دهد.

```
ip addr add 172.19.1.10/24 dev eth2 # temporary adding an IP
ip addr show eth2
ip addr del 172.19.1.10/24 dev eth2 # deleting an IP address
ip link set eth2 up # brining a NIC up
ip route show
ip route add default via 192.168.1.1 # add default gateway
```
لطفاً توجه داشته باشید که دستورات بالا تغییرات موقتی را انجام می دهند که پس از راه اندازی مجدد سرویس `NetworkManager` از بین می روند. اگر به تغییرات دائمی نیاز دارید، باید با استفاده از فایل های پیکربندی یا رابط های Network Manager انجام شود. 

### مدیر شبکه و `nmcli`
در سال های اخیر، خدمات `NetworkManager` محبوبیت زیادی پیدا کرده است. این سرویس می تواند وضعیت شبکه و پیکربندی های مختلف را تماشا کند و کارت های شبکه (مخصوصاً وای فای) را بر اساس آن پیکربندی کند. این همان چیزی است که باعث می‌شود لپ‌تاپ ما هر زمان که آن را در منطقه‌ای با وای‌فای شناخته‌شده باز می‌کنیم یا در مورد رمز عبور می‌پرسیم اگر می‌خواهیم به شبکه جدیدی متصل شویم یا به محض اتصال کابل به کارت اترنت خود آدرس‌های IP اختصاص دهیم، متصل شود. این تخصیص IP ممکن است از طریق "پیکربندی IP دائمی" در دستگاه شما یا پروتکلی به نام DHCP اتفاق بیفتد. هنگام استفاده از DHCP (پروتکل پیکربندی میزبان پویا)، رایانه شما از یک سرور DHCP (مثلا روتر وای فای خانه شما) در مورد IP، Netmask، دروازه پیش فرض، DNS و موارد دیگر سؤال می کند و آنها را تنظیم می کند.

به طور پیش فرض، شبح NetworkManager شبکه هایی را که در `/etc/network/interfaces` ذکر نشده اند، کنترل می کند. این سرویس در پس زمینه اجرا می شود و NIC هایی را که در آنجا پیکربندی نشده اند کنترل می کند. برنامه‌های مختلف رابط کاربری گرافیکی (واسط کاربری گرافیکی) یا TUI (واسط کاربری متنی. `nmtui` را امتحان کنید) یا CLI (واسط‌های خط فرمان (Command Line)) برای کنترل یا پیکربندی شبح NetworkManager وجود دارد. اگر از یک لینوکس رومیزی استفاده می کنید، احتمالاً قبلاً از آن استفاده کرده اید / می شناسید (مثلاً اپلت مدیر شبکه). در اینجا نحوه استفاده از `nmcli` را از خط فرمان (Command Line) به شما نشان خواهم داد.

ما همیشه `nmcli` را با یکی از دستورات مختلف آن فراخوانی می کنیم، در اینجا لیستی وجود دارد:

| فرمان | استفاده |
| ------- | ----- |
| عمومی | وضعیت کلی و عملیات NetworkManager. |
| شبکه | کنترل کلی شبکه | 
| رادیو |            سوئیچ های رادیویی NetworkManager. |
| اتصال | کنترل اتصال |
| دستگاه | دستگاه های کنترل شده توسط NetworkManager |
| عامل | مامور مخفی یا پولکیت |
| مانیتور | نظارت بر تغییرات |

برای مثال، می‌توانیم وضعیت فعلی را با دستور `general` بررسی کنیم:

```
➜  ~ nmcli general
STATE      CONNECTIVITY  WIFI-HW  WIFI     WWAN-HW  WWAN    
connected  full          enabled  enabled  missing  enabled
```
                
یا اگر می‌خواهید دستگاه‌ها یا لیست اتصالات Wi-Fi را بررسی کنید:

```
➜  ~ nmcli device          
DEVICE            TYPE      STATE                   CONNECTION          
wlp108s0          wifi      connected               Sharm Bar Sansoor 5 
docker0           bridge    connected (externally)  docker0             
lo                loopback  connected (externally)  lo                  
p2p-dev-wlp108s0  wifi-p2p  disconnected            --                  
➜  ~ nmcli device wifi     
IN-USE  BSSID              SSID                 MODE   CHAN  RATE        SIGNAL  BARS  SECURITY  
        6C:AD:EF:38:13:38  AxLTE                Infra  3     270 Mbit/s  84      ▂▄▆█  WPA2      
        00:E0:4C:93:1D:B8  Lanat Be Sansoorchi  Infra  6     130 Mbit/s  59      ▂▄▆_  WPA2      
*       24:F5:A2:42:DE:CE  Sharm Bar Sansoor 5  Infra  36    540 Mbit/s  47      ▂▄__  WPA2      
        30:A2:20:DD:8B:54  AvinaAmin            Infra  7     270 Mbit/s  29      ▂___  WPA1 WPA2 
        30:85:A9:8C:71:2C  bahram               Infra  11    65 Mbit/s   29      ▂___  WPA2
```

برای اتصال به یک شبکه Wi-Fi، باید:

```
nmcli device wifi connect AxLTE password AFunkyPassword 
```

### نام های فانتزی برای کامپیوترها

<iframe width="560" height="315" src="https://www.youtube.com/embed/yR07UaiNeME?si=UcsRifk-HXLH-L4U" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

#### نام میزبان
به خاطر سپردن آدرس های IP برای روبات ها آسان است اما برای انسان ها نه. به همین دلیل است که ما "نام میزبان" را داریم. نام میزبان مانند یک لیست تماس است که در آن شما فقط به "Call Jadi" بگویید و سیستم شماره تلفن من را می‌داند. اگر `/etc/hostname` خود را بررسی کنید، نام دستگاه خود را در آنجا خواهید دید. اگرچه می توانید آن را به طور موقت (یا دائم) تغییر دهید. دستور `hostnamectl` است. 

```
[funlap ~]# hostnamectl set-hostname mycoolmachine
[funlap ~]# hostname
mycoolmachine
[funlap ~]# cat /etc/hostname 
mycoolmachine
[funlap ~]# bash
[mycoolmachine ~]# 
```

یا می توانید آن را به عنوان *گذرا* تغییر دهید، که یک تغییر موقت با استفاده از سوئیچ `--transient` است.

همچنین می توان یک نام "زیبا" برای رایانه خود تعریف کرد تا سایر سیستم ها آن را در رابط های خود به خوبی نشان دهند:

```
[mycoolmachine ~]# hostnamectl --pretty set-hostname "LAN Shared Storage"
[mycoolmachine ~]# hostnamectl status
 Static hostname: mycoolmachine
 Pretty hostname: LAN Shared Storage
       Icon name: computer-convertible
         Chassis: convertible
      Machine ID: 0b126c4b6f4347168140eaa6202ce8be
         Boot ID: 675eff37f42648c6bdea31177596557f
Operating System: Manjaro Linux                   
          Kernel: Linux 6.1.38-1-MANJARO
    Architecture: x86-64
 Hardware Vendor: Dell Inc.
  Hardware Model: Latitude 7390 2-in-1
Firmware Version: 1.30.0
```

#### `/etc/hosts`
این فایل حاوی لیستی از IP ها و نام های مربوط به آنها، از جمله رایانه های شخصی شما است. 

```
[mycoolmachine ~]# head -20 /etc/hosts
##
# Host Database
#
# localhost is used to configure the loopback interface
# when the system is booting.  Do not change this entry.
##
127.0.0.1	localhost funlife db
255.255.255.255	broadcasthost
::1             localhost
##
# Host Database
#
# localhost is used to configure the loopback interface
# when the system is booting.  Do not change this entry.
##

198.74.56.50 jobs.jadi.net
192.168.1.22 amoledtesting 

67.217.170.72 vps
```

بنابراین هنگامی که شما نیاز به دسترسی به دستگاهی با نام آن دارید، سیستم عامل شما اکنون به کدام IP دسترسی دارد.

#### پیکربندی DNS
DNS (که مخفف Domain Name System) است سروری است که نام‌های دامنه قابل خواندن توسط انسان (یا از نظر فنی، نام دامنه مبتنی بر متن) را به آدرس‌های IP مربوطه ترجمه می‌کند. باید رایانه خود را برای استفاده از DNS پیکربندی کنید تا بداند اگر می‌خواهید به `linux1st.com` (و شاید [اهدا] (https://linux1st.com/support) دسترسی پیدا کنید، با کدام IP تماس بگیرید.

این پیکربندی را می توان در `/etc/resolv.conf` پیدا کرد.

```
nameserver 192.168.1.1
nameserver 4.2.2.4
domain jadi.net
search jadi.net company.com
```

در اینجا من به رایانه خود می گویم که اگر نیاز به ترجمه آدرس به IP داشت، با DNS در شبکه خانگی من (192.168.1.1) یا یک DNS واقع در 4.2.2.4 تماس بگیرد. 

پیکربندی `domain` یک نام دامنه محلی تنظیم می‌کند، بنابراین ماشین‌های موجود در این دامنه می‌توانند از یک نام کوتاه (tv، به جای tv.jadi.net) استفاده کنند و پیکربندی `search` نیز همین کار را می‌کند و به حل‌کننده می‌گوید که `tv.jadi.net` و ____IN_7 را جستجو کند و ____IN_7 را حل کند. `tv`.

#### nsswitch

فایل `/etc/nsswitch.conf` برای پیکربندی سرویس هایی که قرار است برای تعیین اطلاعاتی مانند نام میزبان، فایل های رمز عبور و فایل های گروهی استفاده شوند، استفاده می شود. مال من است

```text
# cat /etc/nsswitch.conf
# Begin /etc/nsswitch.conf

passwd: files
group: files
shadow: files

publickey: files

hosts: files dns myhostname
networks: files

protocols: files
services: files
ethers: files
rpc: files

netgroup: files

# End /etc/nsswitch.conf
```

بنابراین اگر شخصی بخواهد رمز عبور را بررسی کند، سیستم رمز عبور _file_ را در سیستم امتحان می کند. یا اگر بخواهند آدرس آی‌پی نام میزبان را بررسی کنند، پیکربندی من می‌گوید `hosts: files dns myhostname`، بنابراین کامپیوتر ابتدا فایل‌های \(/etc/hosts\) را امتحان می‌کند و سپس به سراغ DNS می‌رود. اگر اینها را برگردانم و خط را به

```text
hosts:      dns files
```

هر درخواست حل و فصل ابتدا به یک سرور DNS ارسال می شود و از /etc/hosts فقط در صورتی استفاده می شود که سرورهای DNS پاسخ "نمی دانم!"