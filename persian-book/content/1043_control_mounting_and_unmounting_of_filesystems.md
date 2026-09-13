Title: 104.3 نصب و جداسازی فایل سیستم ها را کنترل کنید
Date: 2010-12-03 10:20
Category: LPIC1
sortorder: 220

_وزن: 3_

داوطلبان باید قادر به پیکربندی نصب یک فایل سیستم باشند.

- نصب و جدا کردن فایل سیستم ها به صورت دستی
- پیکربندی نصب فایل سیستم در بوت آپ.
- پیکربندی سیستم های فایل قابل جابجایی قابل نصب توسط کاربر.
- استفاده از برچسب ها و UUID ها برای شناسایی و نصب فایل سیستم ها.
- آگاهی از واحدهای نصب سیستم.

- /etc/fstab
- /رسانه/
- سوار کردن
- مقدار
- سیاه
- lsblk




<iframe width="560" height="315" src="https://www.youtube.com/embed/dod65eKzWtw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## نصب و جدا کردن
وقتی یک پارتیشن (Partition) فرمت شده داریم و نیاز به استفاده از آن داریم، باید آن را در جایی از سلسله مراتب دایرکتوری (پوشه) لینوکس `mount` کنیم. برخلاف ویندوز، *درایور* جدید اکنون به صورت دیسک های جدا شده نشان داده می شود، اما مانند *زیر شاخه های مجازی* جایی در درخت `/` شما. 

بگویید می‌خواهیم `/dev/sda3` را در `/media/mydisk` *mount کنیم. دایرکتوری (پوشه) `/media/mydisk` باید آنجا باشد و سپس، ما فقط اجرا می کنیم:

```
sudo mount -t ext4 /dev/sda3 /media/mydisk
```

همه فایل‌ها و پوشه‌های /dev/sda3 از /media/mydisk قابل دسترسی خواهند بود.

`mount` را بدون پارامتر اجرا کنید تا همه دستگاه های نصب شده را ببینید. برای **نوار کردن**، به سادگی از `umount` در درایو یا دایرکتوری (پوشه) استفاده کنید. این دو معادل هستند:

```
sudo umount /dev/sda3
sudo umount /media/mydisk
```

نصب و راه اندازی می تواند در انواع مختلف ذخیره سازی اتفاق بیفتد، به عنوان مثال در حافظه های ذخیره سازی NFS، ISO (با `-o loop`)، tmpfs، ...

> دیسک های swap نیازی به نصب ندارند. برای استفاده از آنها باید از `swapon` و `swapoff` استفاده کنید.

```
mount -t ext4 /dev/sda1 /media
```
سوئیچ `-t` نوع سیستم‌فایل (Filesystem) را نشان می دهد.

```
mount -o remount,ro /dev/sda1
```

سوئیچ `-o` برخی از گزینه‌ها را پاس می‌کند (برای فقط خواندن، بگویید `ro`)

معمولاً به عنوان دستور یک خطی استفاده می شود:

```
mount -t ext4 -o remount,ro /dev/sda1 /media 
```

> دایرکتوری (پوشه) های `/media` و `/mnt` برای نصب فایل سیستم ها استفاده می شوند، حتی اگر می توانید از هر دایرکتوری (پوشه) برای این منظور استفاده کنید.

### UUID و برچسب ها
همانطور که می دانید، هنگام کار با نام های کلاسیک دستگاه مانند `/dev/vdb1` مشکلی وجود دارد: آنها تغییر می کنند! `/dev/sdb` فعلی ممکن است پس از حذف/وصل مجدد به صورت `/dev/sdd` دیده شود. برای حل این مشکل، بهتر است با UUID (شناسه‌های منحصر به فرد جهانی) کار کنید. آنها را با `lsblk` علامت بزنید ( `-O` همه ستون های موجود را نشان می دهد یا با -o به صورت زیر مشخص می کند) و `blkid`.

```txt
# lsblk -o +UUID
NAME   MAJ:MIN RM  SIZE RO TYPE MOUNTPOINTS                             UUID
sr0     11:0    1  1.8G  0 rom  /run/media/jadi/Fedora-WS-Live-35_B-1-2 2021-09-22-21-47-34-00
zram0  251:0    0  1.9G  0 disk [SWAP]                                  
vda    252:0    0   20G  0 disk                                         
├─vda1 252:1    0  600M  0 part /boot/efi                               E13A-EF36
├─vda2 252:2    0    1G  0 part /boot                                   19ed96a1-3b36-4202-81bb-349f7adfb8b1
└─vda3 252:3    0 18.4G  0 part /home                                   076766a5-8864-4e35-a632-464b03396f7a
                                /                                       
vdb    252:16   0    2G  0 disk                                         
└─vdb1 252:17   0    2G  0 part /tmp/lkj                                4c1a51e6-47bf-4a34-84a2-87027c91e14a

# blkid
/dev/vdb1: UUID="4c1a51e6-47bf-4a34-84a2-87027c91e14a" BLOCK_SIZE="4096" TYPE="ext4" PARTUUID="5415e516-01"
/dev/sr0: BLOCK_SIZE="2048" UUID="2021-09-22-21-47-34-00" LABEL="Fedora-WS-Live-35_B-1-2" TYPE="iso9660"
/dev/zram0: LABEL="zram0" UUID="e459f522-1675-40d2-b318-51d9bd16d7bb" TYPE="swap"
/dev/vda2: UUID="19ed96a1-3b36-4202-81bb-349f7adfb8b1" BLOCK_SIZE="4096" TYPE="ext4" PARTUUID="5f4ee154-3ade-4af6-8809-6d90d5827d39"
/dev/vda3: LABEL="fedora_localhost-live" UUID="076766a5-8864-4e35-a632-464b03396f7a" UUID_SUB="a4340a29-6d9b-4c28-a7c8-b4aab5d08893" BLOCK_SIZE="4096" TYPE="btrfs" PARTUUID="a46e64aa-65ef-4a62-9bf8-96fd19aee353"
/dev/vda1: UUID="E13A-EF36" BLOCK_SIZE="512" TYPE="vfat" PARTLABEL="EFI System Partition" PARTUUID="a7a2b260-0302-45bc-a4db-42bd2e0ee7f2"

# blkid /dev/vdb1
/dev/vdb1: UUID="4c1a51e6-47bf-4a34-84a2-87027c91e14a" BLOCK_SIZE="4096" TYPE="ext4" PARTUUID="5415e516-01"

# mount UUID="4c1a51e6-47bf-4a34-84a2-87027c91e14a" /media/mydisk/
```

### fstab

<iframe width="560" height="315" src="https://www.youtube.com/embed/lQGvxIkdcSE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

برای نصب خودکار، لینوکس از فایل `/etc/fstab` استفاده می کند. مانند جدولی است که نشان می دهد چه فایل سیستمی باید در هنگام بوت در کجا نصب شود. این `/etc/fstab` فدورا من است:

```
# cat /etc/fstab

#
# /etc/fstab
# Created by anaconda on Wed Oct 20 13:16:38 2021
#
# Accessible filesystems, by reference, are maintained under '/dev/disk/'.
# See man pages fstab(5), findfs(8), mount(8) and/or blkid(8) for more info.
#
# After editing this file, run 'systemctl daemon-reload' to update systemd
# units generated from this file.
#
UUID=076766a5-8864-4e35-a632-464b03396f7a /                       btrfs   subvol=root,compress=zstd:1 0 0
UUID=19ed96a1-3b36-4202-81bb-349f7adfb8b1 /boot                   ext4    defaults        1 2
UUID=E13A-EF36          /boot/efi               vfat    umask=0077,shortname=winnt 0 2
UUID=076766a5-8864-4e35-a632-464b03396f7a /home                   btrfs   subvol=home,compress=zstd:1 0 0

```

اینها ستون ها هستند:

- سیستم‌فایل (Filesystem): برچسب، UUID، دستگاه
- نقطه نصب: مبادله یا هیچکدام برای تعویض
- type: می تواند ext4، xfs، nfs یا انواع دیگر فایل سیستم باشد
- گزینه ها: پیش فرض، rw / ro، noauto، کاربر، exec / noexec، noatime، umask
- dump: آیا دستور dump پشتیبان گیری می شود؟ اکثرا 0
- pass: مقادیر غیر صفر پاس، ترتیب بررسی سیستم های فایل در زمان بوت را مشخص می کند.

**توجه:**

- فایل سیستم های نصب شده توسط کاربر به طور پیش فرض noexec هستند مگر اینکه exec بعد از کاربر مشخص شده باشد.
- noatime ضبط زمان دسترسی را غیرفعال می کند. عدم استفاده از زمان دسترسی ممکن است عملکرد را بهبود بخشد.

## واحدهای نصب سیستمی

هنگام استفاده از systemd، یک فایل پیکربندی واحد که نام آن به ".mount" ختم می شود، اطلاعات مربوط به یک نقطه نصب سیستم‌فایل (Filesystem) را که توسط systemd کنترل و نظارت می شود، رمزگذاری می کند.