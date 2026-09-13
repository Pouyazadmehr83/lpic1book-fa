Title: 104.1 ایجاد پارتیشن (Partition) و فایل سیستم
Date: 2010-12-03 10:20
Category: LPIC1
Tags: LPIC1, 101, LPIC1-101-500
Authors: Jadi
Summary: 
sortorder: 200

_وزن: 2_

توضیحات: داوطلبان باید بتوانند پارتیشن (Partition) های دیسک را پیکربندی کنند و سپس سیستم های فایلی را روی رسانه هایی مانند هارد دیسک ایجاد کنند. این شامل مدیریت پارتیشن (Partition) های مبادله می شود.

### هدف

* جداول پارتیشن (Partition) MBR و GPT را مدیریت کنید
* از دستورات مختلف mkfs برای ایجاد فایل سیستم های مختلف مانند:
    * ext2/ext3/ext4
    * XFS
    * VFAT
    * exFAT
* دانش اولیه ویژگی های Btrfs، از جمله سیستم های فایل چند دستگاهی، فشرده سازی و حجم های فرعی.

* fdisk
* gdisk
* جدا شد
* mkfs
* mkswap

<iframe width="560" height="315" src="https://www.youtube.com/embed/xSQdIIMGG2g" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

### دستگاه ها را مسدود کنید
دستگاه بلوک یک دستگاه ذخیره سازی انبوه غیر فرار است که اطلاعات آن به هر ترتیبی قابل دسترسی است. مانند هارد دیسک ها، حافظه های USB، فلاپی دیسک ها و سی دی رام ها. ما این دستگاه ها را به بلوک هایی با اندازه ثابت *فرمت* می کنیم.

می‌توانیم با استفاده از دستور `lsblk` همه دستگاه‌های مسدود را بررسی کنیم. علاوه بر این در قالب طولانی ls (`-l`)، دستگاه‌های بلوک با `b` در ستون اول نشان داده می‌شوند:

```
jadi@debianamd:~$ ls /dev/ -l | grep "^b"
brw-rw----  1 root disk      8,   0 Feb  3  2023 sda
brw-rw----  1 root disk      8,  16 Feb  3  2023 sdb
brw-rw----  1 root disk      8,  17 Feb  3  2023 sdb1
brw-rw----  1 root disk      8,  18 Feb  3  2023 sdb2
brw-rw----  1 root disk      8,  19 Feb  3  2023 sdb3
brw-rw----+ 1 root cdrom    11,   0 Feb  3  2023 sr0
```


امکان ایجاد **پارتیشن (Partition)** بر روی یک دستگاه بلوک و حتی تقسیم آن و استفاده از آن به عنوان چندین دیسک وجود دارد. سیستم‌هایی که بوت‌لودرهای قدیمی بایوس دارند از روش **Master Boot Record (MBR)** برای نصب و سیستم‌های جدیدتر UEFI، از فرمت‌های **GUID Parition Table (GPT)** استفاده می‌کنند.

سیستم‌های لینوکس از `udev` برای اضافه کردن دستگاه‌های بلوک و پارتیشن (Partition)‌های آن‌ها به `/dev` به شکل `/dev/sdb1` (دیسک دوم (b) و پارتیشن (Partition) اول (1)) استفاده می‌کنند. 

### ویرایش جداول پارتیشن (Partition)
#### fdisk

`fdisk` دستور اصلی برای مشاهده / تغییر و ایجاد پارتیشن (Partition) در سیستم های MBR است. سوئیچ `-l` پارتیشن (Partition) ها را فهرست می کند:

```
# fdisk -l /dev/sdb
Disk /dev/sdb: 20 GiB, 21474836480 bytes, 41943040 sectors
Disk model: QEMU HARDDISK
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: gpt
Disk identifier: 11D48091-5AA7-422A-85F7-A23F476CDFD7

Device        Start      End  Sectors  Size Type
/dev/sdb1      2048  1050623  1048576  512M EFI System
/dev/sdb2   1050624 39942143 38891520 18.5G Linux filesystem
/dev/sdb3  39942144 41940991  1998848  976M Linux swap
```

* پرچم **Boot** نشان می دهد که کدام پارتیشن (Partition) بوت را در رایانه های DOS شروع می کند و در LILO & GRUB اهمیتی ندارد.
* شروع و پایان نشان می دهد که این پارتیشن (Partition) در کجای دیسک قرار دارد.
* اندازه اندازه هر پارتیشن (Partition) را نشان می دهد.
* شناسه فرمت پارتیشن (Partition) را نشان می دهد \(82 swap است، 83 داده لینوکس است، ... همه را با `l` در حالت تعاملی بررسی کنید.

همچنین امکان اجرای fdisk در حالت تعاملی نیز وجود دارد. `m` منوی راهنما را به شما نشان می دهد:

```
~# fdisk /dev/sda

Welcome to fdisk (util-linux 2.36.1).
Changes will remain in memory only, until you decide to write them.
Be careful before using the write command.

Device does not contain a recognized partition table.
Created a new DOS disklabel with disk identifier 0xe2dbaded.

Command (m for help): m

Help:

  DOS (MBR)
   a   toggle a bootable flag
   b   edit nested BSD disklabel
   c   toggle the dos compatibility flag

  Generic
   d   delete a partition
   F   list free unpartitioned space
   l   list known partition types
   n   add a new partition
   p   print the partition table
   t   change a partition type
   v   verify the partition table
   i   print information about a partition

  Misc
   m   print this menu
   u   change display/entry units
   x   extra functionality (experts only)

  Script
   I   load disk layout from sfdisk script file
   O   dump disk layout to sfdisk script file

  Save & Exit
   w   write table to disk and exit
   q   quit without saving changes

  Create a new label
   g   create a new empty GPT partition table
   G   create a new empty SGI (IRIX) partition table
   o   create a new empty DOS partition table
   s   create a new empty Sun partition table


Command (m for help):
```

برای بررسی لیست پارتیشن (Partition) فعلی، دستور `p` (چاپ) را امتحان کنید:

```
Command (m for help): p
Disk /dev/sdb: 20 GiB, 21474836480 bytes, 41943040 sectors
Disk model: QEMU HARDDISK
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: gpt
Disk identifier: 11D48091-5AA7-422A-85F7-A23F476CDFD7

Device        Start      End  Sectors  Size Type
/dev/sdb1      2048  1050623  1048576  512M EFI System
/dev/sdb2   1050624 39942143 38891520 18.5G Linux filesystem
/dev/sdb3  39942144 41940991  1998848  976M Linux swap
```

شما باید مفاهیم طرح‌بندی دیسک را از [فصل 102.1] (/1021-design-hard-disk-layout.html) به خاطر بسپارید. بنابراین اجازه دهید با استفاده از `fdisk` چند پارتیشن (Partition) ایجاد کنیم. من از `n` برای *جدید* استفاده خواهم کرد:

```
# fdisk /dev/sda

Welcome to fdisk (util-linux 2.36.1).
Changes will remain in memory only, until you decide to write them.
Be careful before using the write command.

Device does not contain a recognized partition table.
Created a new DOS disklabel with disk identifier 0x40bd0f72.

Command (m for help): n
Partition type
   p   primary (0 primary, 0 extended, 4 free)
   e   extended (container for logical partitions)
Select (default p): p
Partition number (1-4, default 1):
First sector (2048-8388607, default 2048):
Last sector, +/-sectors or +/-size{K,M,G,T,P} (2048-8388607, default 8388607): +1G

Created a new partition 1 of type 'Linux' and of size 1 GiB.

Command (m for help): p
Disk /dev/sda: 4 GiB, 4294967296 bytes, 8388608 sectors
Disk model: QEMU HARDDISK
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: dos
Disk identifier: 0x40bd0f72

Device     Boot Start     End Sectors Size Id Type
/dev/sda1        2048 2099199 2097152   1G 83 Linux
```

بیایید یک پارتیشن (Partition) Extened دیگری ایجاد کنیم و یک پارتیشن (Partition) لینوکس (83) و یک پارتیشن (Partition) Swap (82) را در آنجا اضافه کنیم. 

```
Command (m for help): n
Partition type
   p   primary (1 primary, 0 extended, 3 free)
   e   extended (container for logical partitions)
Select (default p): e
Partition number (2-4, default 2):
First sector (2099200-8388607, default 2099200):
Last sector, +/-sectors or +/-size{K,M,G,T,P} (2099200-8388607, default 8388607):

Created a new partition 2 of type 'Extended' and of size 3 GiB.

Command (m for help): p
Disk /dev/sda: 4 GiB, 4294967296 bytes, 8388608 sectors
Disk model: QEMU HARDDISK
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: dos
Disk identifier: 0x40bd0f72

Device     Boot   Start     End Sectors Size Id Type
/dev/sda1          2048 2099199 2097152   1G 83 Linux
/dev/sda2       2099200 8388607 6289408   3G  5 Extended

Command (m for help): n
All space for primary partitions is in use.
Adding logical partition 5
First sector (2101248-8388607, default 2101248):
Last sector, +/-sectors or +/-size{K,M,G,T,P} (2101248-8388607, default 8388607):

Created a new partition 5 of type 'Linux' and of size 3 GiB.

Command (m for help): p
Disk /dev/sda: 4 GiB, 4294967296 bytes, 8388608 sectors
Disk model: QEMU HARDDISK
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: dos
Disk identifier: 0x40bd0f72

Device     Boot   Start     End Sectors Size Id Type
/dev/sda1          2048 2099199 2097152   1G 83 Linux
/dev/sda2       2099200 8388607 6289408   3G  5 Extended
/dev/sda5       2101248 8388607 6287360   3G 83 Linux
```

اوه! فراموش کردم فضا را برای پارتیشن (Partition) swap اختصاص دهم. بیایید قبلی را حذف کنیم و دو مورد جدید اضافه کنیم:

```
Command (m for help): d
Partition number (1,2,5, default 5): 5

Partition 5 has been deleted.

Command (m for help): n
All space for primary partitions is in use.
Adding logical partition 5
First sector (2101248-8388607, default 2101248):
Last sector, +/-sectors or +/-size{K,M,G,T,P} (2101248-8388607, default 8388607): +1G

Created a new partition 5 of type 'Linux' and of size 1 GiB.

Command (m for help): p
Disk /dev/sda: 4 GiB, 4294967296 bytes, 8388608 sectors
Disk model: QEMU HARDDISK
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: dos
Disk identifier: 0x40bd0f72

Device     Boot   Start     End Sectors Size Id Type
/dev/sda1          2048 2099199 2097152   1G 83 Linux
/dev/sda2       2099200 8388607 6289408   3G  5 Extended
/dev/sda5       2101248 4198399 2097152   1G 83 Linux

Command (m for help): n
All space for primary partitions is in use.
Adding logical partition 6
First sector (4200448-8388607, default 4200448):
Last sector, +/-sectors or +/-size{K,M,G,T,P} (4200448-8388607, default 8388607):

Created a new partition 6 of type 'Linux' and of size 2 GiB.
```

و اکنون، باید نوع پارتیشن (Partition) 6 را برای تعویض تغییر دهم:

```
Command (m for help): t
Partition number (1,2,5,6, default 6): 6
Hex code or alias (type L to list all): L

00 Empty            24 NEC DOS          81 Minix / old Lin  bf Solaris
01 FAT12            27 Hidden NTFS Win  82 Linux swap / So  c1 DRDOS/sec (FAT-
02 XENIX root       39 Plan 9           83 Linux            c4 DRDOS/sec (FAT-
03 XENIX usr        3c PartitionMagic   84 OS/2 hidden or   c6 DRDOS/sec (FAT-
04 FAT16 <32M       40 Venix 80286      85 Linux extended   c7 Syrinx
05 Extended         41 PPC PReP Boot    86 NTFS volume set  da Non-FS data
06 FAT16            42 SFS              87 NTFS volume set  db CP/M / CTOS / .
07 HPFS/NTFS/exFAT  4d QNX4.x           88 Linux plaintext  de Dell Utility
08 AIX              4e QNX4.x 2nd part  8e Linux LVM        df BootIt
09 AIX bootable     4f QNX4.x 3rd part  93 Amoeba           e1 DOS access
0a OS/2 Boot Manag  50 OnTrack DM       94 Amoeba BBT       e3 DOS R/O
0b W95 FAT32        51 OnTrack DM6 Aux  9f BSD/OS           e4 SpeedStor
0c W95 FAT32 (LBA)  52 CP/M             a0 IBM Thinkpad hi  ea Linux extended
0e W95 FAT16 (LBA)  53 OnTrack DM6 Aux  a5 FreeBSD          eb BeOS fs
0f W95 Ext'd (LBA)  54 OnTrackDM6       a6 OpenBSD          ee GPT
10 OPUS             55 EZ-Drive         a7 NeXTSTEP         ef EFI (FAT-12/16/
11 Hidden FAT12     56 Golden Bow       a8 Darwin UFS       f0 Linux/PA-RISC b
12 Compaq diagnost  5c Priam Edisk      a9 NetBSD           f1 SpeedStor
14 Hidden FAT16 <3  61 SpeedStor        ab Darwin boot      f4 SpeedStor
16 Hidden FAT16     63 GNU HURD or Sys  af HFS / HFS+       f2 DOS secondary
17 Hidden HPFS/NTF  64 Novell Netware   b7 BSDI fs          fb VMware VMFS
18 AST SmartSleep   65 Novell Netware   b8 BSDI swap        fc VMware VMKCORE
1b Hidden W95 FAT3  70 DiskSecure Mult  bb Boot Wizard hid  fd Linux raid auto
1c Hidden W95 FAT3  75 PC/IX            bc Acronis FAT32 L  fe LANstep
1e Hidden W95 FAT1  80 Old Minix        be Solaris boot     ff BBT

Aliases:
   linux          - 83
   swap           - 82
   extended       - 05
   uefi           - EF
   raid           - FD
   lvm            - 8E
   linuxex        - 85
Hex code or alias (type L to list all): swap

Changed type of partition 'Linux' to 'Linux swap / Solaris'.

Command (m for help): p
Disk /dev/sda: 4 GiB, 4294967296 bytes, 8388608 sectors
Disk model: QEMU HARDDISK
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: dos
Disk identifier: 0x40bd0f72

Device     Boot   Start     End Sectors Size Id Type
/dev/sda1          2048 2099199 2097152   1G 83 Linux
/dev/sda2       2099200 8388607 6289408   3G  5 Extended
/dev/sda5       2101248 4198399 2097152   1G 83 Linux
/dev/sda6       4200448 8388607 4188160   2G 82 Linux swap / Solaris
```

راضی! بیایید `v`تأیید کنیم و سپس `w`نتایج را بازنویسی کنیم:

```
Command (m for help): v
No errors detected.
Remaining 4094 unallocated 512-byte sectors.

Command (m for help): w
The partition table has been altered.
Calling ioctl() to re-read partition table.
Syncing disks.

root@debianamd:~# fdisk -l /dev/sda
Disk /dev/sda: 4 GiB, 4294967296 bytes, 8388608 sectors
Disk model: QEMU HARDDISK
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: dos
Disk identifier: 0x40bd0f72

Device     Boot   Start     End Sectors Size Id Type
/dev/sda1          2048 2099199 2097152   1G 83 Linux
/dev/sda2       2099200 8388607 6289408   3G  5 Extended
/dev/sda5       2101248 4198399 2097152   1G 83 Linux
/dev/sda6       4200448 8388607 4188160   2G 82 Linux swap / Solaris
```
#### gdisk
همانطور که در [فصل 102.1] (/1021-design-hard-disk-layout.html) مشاهده شد، ما از `gdisk` در ماشین های GPT استفاده کرده ایم. تفاوت چندانی با `fdisk` ندارد. بیایید به دستورات اصلی آن نگاهی بیندازیم:

```txt
root@debianamd:~# gdisk /dev/sda
GPT fdisk (gdisk) version 1.0.6  

Warning: Partition table header claims that the size of partition table
entries is 0 bytes, but this program  supports only 128-byte entries.
Adjusting accordingly, but partition table may be garbage.
Warning: Partition table header claims that the size of partition table
entries is 0 bytes, but this program  supports only 128-byte entries.
Adjusting accordingly, but partition table may be garbage.
Partition table scan:
  MBR: MBR only
  BSD: not present
  APM: not present
  GPT: not present


***************************************************************
Found invalid GPT and valid MBR; converting MBR to GPT format
in memory. THIS OPERATION IS POTENTIALLY DESTRUCTIVE! Exit by
typing 'q' if you don't want to convert your MBR partitions
to GPT format!
***************************************************************

Command (? for help): ?
b	back up GPT data to a file
c	change a partition's name
d	delete a partition
i	show detailed information on a partition
l	list known partition types
n	add a new partition
o	create a new empty GUID partition table (GPT)
p	print the partition table
q	quit without saving changes
r	recovery and transformation options (experts only)
s	sort partitions
t	change a partition's type code
v	verify disk
w	write table to disk and exit
x	extra functionality (experts only)
?	print this menu
```

همانطور که می بینید، جدول پارتیشن (Partition Table) (Partition) باید با تنظیمات BIOS/UEFI شما سازگار باشد. 

#### جدا شد
`parted` ابزار گنو برای ویرایش پارتیشن (Partition) ها است. مزیت اصلی آن توانایی تغییر اندازه پارتیشن (Partition) های تعریف شده فعلی است، اما استفاده از آن کمی پیچیده تر از `fdisk` و `gdisk` است:

```txt
# parted
GNU Parted 3.4
Using /dev/sda
Welcome to GNU Parted! Type 'help' to view a list of commands.
(parted) help
  align-check TYPE N                       check partition N for TYPE(min|opt) alignment
  help [COMMAND]                           print general help, or help on COMMAND
  mklabel,mktable LABEL-TYPE               create a new disklabel (partition table)
  mkpart PART-TYPE [FS-TYPE] START END     make a partition
  name NUMBER NAME                         name partition NUMBER as NAME
  print [devices|free|list,all|NUMBER]     display the partition table, available devices, free space, all found partitions, or a particular partition
  quit                                     exit program
  rescue START END                         rescue a lost partition near START and END
  resizepart NUMBER END                    resize partition NUMBER
  rm NUMBER                                delete partition NUMBER
  select DEVICE                            choose the device to edit
  disk_set FLAG STATE                      change the FLAG on selected device
  disk_toggle [FLAG]                       toggle the state of FLAG on selected device
  set NUMBER FLAG STATE                    change the FLAG on partition NUMBER
  toggle [NUMBER [FLAG]]                   toggle the state of FLAG on partition NUMBER
  unit UNIT                                set the default unit to UNIT
  version                                  display the version number and copyright information of GNU Parted
```

#### اشاره؟ از gparted استفاده کنید
ابزار `gparted` ابزاری گرافیکی برای مدیریت پارتیشن (Partition) بندی شماست. قابلیت تغییر اندازه پارتیشن (Partition) ها را دارد و استفاده از آن فوق العاده آسان است. این بخشی از آزمون LPIC نیست، اما دانستن در مورد آن خوب است. فقط در صورت امکان ;) [gparted.org](https://gparted.org/)

### فرمت کردن پارتیشن (Partition)

<iframe width="560" height="315" src="https://www.youtube.com/embed/rQZVYtVOEhU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

#### سیستم های فایل
بعد از اینکه دستگاه‌های بلوکی (Block Devices) خود را پارتیشن (Partition) بندی کردید، باید آنها را فرمت کنید تا برای ذخیره فایل ها و دایرکتوری (پوشه) ها قابل استفاده باشند. فرمت کردن یک فایل سیستم، نقشه ای ایجاد می کند که مکان و نام فایل ها و دایرکتوری (پوشه) ها را ذخیره می کند و امکان جابجایی فایل ها بین پوشه ها، حذف یا تغییر نام آنها را فراهم می کند. آن را به عنوان نمایه یک کتاب در نظر بگیرید. 

چندین سیستم‌فایل (Filesystem) در دنیای لینوکس وجود دارد، اما اینها رایج ترین آنها هستند:

| قالب | توضیحات |
| :---: | :--- |
| ext2 | دومین فایل سیستم توسعه یافته برای رفع کاستی های سیستم‌فایل (Filesystem) قدیمی یونیکس/مینیکس که در نسخه های اولیه لینوکس استفاده می شد، توسعه یافت. چندین سال است که به طور گسترده در لینوکس استفاده می شود. در ext2 خبری از ژورنال وجود ندارد و تا حد زیادی با ext3 و اخیراً ext4 جایگزین شده است. |
| ext3 | ext2 + journaling حداکثر حجم فایل 2 ترابایت و حداکثر حجم فایل سیستم 16 ترابایت |
| ext4 | نسخه فعلی ext، حداکثر اندازه فایل 16 ترابایت و حداکثر اندازه فایل سیستم 1EB (1000*1000 ترابایت) است |
| XFS | ژورنالینگ، کش در حافظه رم، عالی برای منابع تغذیه بدون وقفه، حداکثر حجم فایل و فایل سیستم 8EB است |
| مبادله | Swap زمانی استفاده می شود که سیستم نیاز به استفاده از رم بیشتر از آنچه دارد داشته باشد. این مانند یک رم اضافی روی دیسک است |
| VFAT | FAT32، بدون ژورنال، برای تبادل داده با ویندوز خوب است، **مجوزها** و پیوندهای نمادین را درک نمی کند |
| exFAT | چربی طولانی نسخه جدیدتر FAT که عمدتاً برای دستگاه های توسعه یافته استفاده می شود که باید روی همه ماشین ها کار کند. مانند دیسک های USB |
| btrfs | یک فایل سیستم جدید با کارایی بالا. حداکثر حجم و حجم فایل 16 EB است. دارای فرم خاص خود از RAID و LVM و عکس های فوری داخلی و تحمل خطا و فشرده سازی داده ها در حال پرواز. |

#### ایجاد فایل سیستم
می توانید پارتیشن (Partition) های خود را با دستور `mkfs` \(و `mkswap` برای تعویض\) قالب بندی کنید. این قسمت جلویی برای دستوراتی مانند `mkfs.ext3` برای *ext3*، `mkfs.ext4` برای *ext4* و `mkfs.reiserfs` برای *ReiserFS* است. لیست کامل نصب شده روی سیستم شما اینجاست:

```
# ls /sbin/mk*
/sbin/mkdosfs  /sbin/mkexfatfs	/sbin/mkfs.bfs	   /sbin/mkfs.exfat  /sbin/mkfs.ext3  /sbin/mkfs.fat	/sbin/mkfs.msdos  /sbin/mkfs.vfat	  /sbin/mkinitramfs   /sbin/mkntfs
/sbin/mke2fs   /sbin/mkfs	/sbin/mkfs.cramfs  /sbin/mkfs.ext2   /sbin/mkfs.ext4  /sbin/mkfs.minix	/sbin/mkfs.ntfs   /sbin/mkhomedir_helper  /sbin/mklost+found  /sbin/mkswap
```

اگر از `mkfs` استفاده می کنید، سوئیچ اصلی `-type` \(یا `-t`\) برای تعیین قالب است:

```
# mkfs -t ext4 /dev/sda1
mke2fs 1.46.2 (28-Feb-2021)
Discarding device blocks: done
Creating filesystem with 262144 4k blocks and 65536 inodes
Filesystem UUID: 63625ecd-857a-419f-a300-12395aaad89f
Superblock backups stored on blocks:
	32768, 98304, 163840, 229376

Allocating group tables: done
Writing inode tables: done
Creating journal (8192 blocks): done
Writing superblocks and filesystem accounting information: done

root@debianamd:~# mkfs.exfat /dev/sda5
mkexfatfs 1.3.0
Creating... done.
Flushing... done.
File system created successfully.
```

اگر نیاز به اختصاص یک lable به پارتیشن (Partition) دارید، باید از گزینه `-L lable_name` استفاده کنید. لطفاً توجه داشته باشید که در سیستم اخیر، مردم به جای برچسب از UUID استفاده می کنند. UUID یک دیسک را می توان با موارد زیر مشاهده کرد:

```   
# blkid /dev/sda1
/dev/sda1: UUID="63625ecd-857a-419f-a300-12395aaad89f" BLOCK_SIZE="4096" TYPE="ext4" PARTUUID="40bd0f72-01"
```

و به عنوان آخرین کار، اجازه می‌دهیم یک مبادله در `/dev/sda6` ایجاد کنیم:

```
# mkswap /dev/sda6
Setting up swapspace version 1, size = 2 GiB (2144333824 bytes)
no label, UUID=6a59cf20-8fd6-4d86-b044-89f7bc67993b
```

و سپس 

```
# swapon /dev/sda6
```

در فصل 14.3 خواهیم دید که چگونه می توانیم این فایل سیستم ها را *mount* / *unmount کنیم.