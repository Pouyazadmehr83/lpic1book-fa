Title: 104.4 حذف شد
Date: 2010-12-03 10:20
Category: LPIC1
Tags: LPIC1, 101, LPIC1-101-500
Authors: Jadi
Summary: 
sortorder: 230

<div class="alert alert-danger" role="alert">
  This chapter is removed in the latest version (500) of LPIC1 and is kept here as a reference.
</div>

<iframe width="560" height="315" src="https://www.youtube.com/embed/KJPvfqe-Bls" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>


## 104.4 مدیریت سهمیه دیسک

_وزن: 1_

کاندیداها باید بتوانند سهمیه دیسک را برای کاربران مدیریت کنند.

### اهداف

* یک سهمیه دیسک برای یک سیستم‌فایل (Filesystem) تنظیم کنید.
* ویرایش، بررسی و تولید گزارش سهمیه کاربران.
* سهمیه
* سهمیه بندی
* سهمیه بندی مجدد
* `quoting`

### فعال کردن سهمیه ها

سهمیه‌ها به سرپرست سیستم اجازه می‌دهد تا میزان مصرف دیسک توسط کاربر یا گروه را کنترل کند. سهمیه نسخه 2 مورد بحث در LPIC، به هسته 2.4 و بالاتر نیاز دارد. این بسته `quota` نام دارد.

این گزینه باید به فایل `/etc/fstab` مورد نیاز اضافه شود. معروف ترین آنها عبارتند از:

| گزینه | معنی |
| :--- | :--- |
| usrquota | سهمیه کاربران |
| uqouta | همان usrquota |
| سهمیه | همان usrquota |
| grpquota | سهمیه گروهی |
| gquota | همان grpquota |

به عنوان مثال، اگر می‌خواهیم سهمیه‌ها را در sda2 فعال کنیم، باید خط را در /etc/fstab به شکل زیر تغییر دهیم:

```text
/dev/sda2  /home  ext4    defaults,usrquota,grpquota          1 2
```

در مرحله بعد باید سهمیه هر کاربر و هر گروه را مشخص کنیم. دو فایل به نام های `aquota.user` و `aquota.group` در سیستم‌فایل (Filesystem) ریشه این کار را انجام می دهند. حالا کافی است دستور `quotacheck` را اجرا کنید.

> اگر aquota.user و aquota.group وجود نداشته باشند دستور `quotacheck` ایجاد می کند.

```text
# quotacheck -u -a -m -c -v
quotacheck: Your kernel probably supports journaled quota but you are not using it. Consider switching to journaled quota to avoid running quotacheck after an unclean shutdown.
quotacheck: Scanning /dev/sda1 [/boot] done
quotacheck: Old group file name could not been determined. Usage will not be subtracted.
quotacheck: Checked 13 directories and 389 files
# ls /boot/
aquota.user
```

**C** فایل های سهمیه ای را برای **u**sers در **a**ll سیستم های فایل بازخوانی می کند و روی سیستم های فایل **m**ounted کار می کند. ** v**erbose بودن.

سپس باید بررسی سهمیه را روشن کنید:

```text
# quotaon -auv ##all in /etc/fstab, for user quotas and be verbose
/dev/sda1 [/boot]: user quotas turned on
```

### تعیین محدودیت

دستور اصلی برای _editing_ quota _\*edquota_ است. سهمیه کاربران را از تمام سیستم های فایل بررسی می کند و آنها را در یک ویرایشگر فایل به شما ارائه می دهد.

```text
#edquota -u jadi
Disk quotas for user jadi (uid 1000):
  Filesystem                   blocks       soft       hard     inodes     soft     hard
  /dev/sda1                         0          0          0          0        0        0
```

همانطور که می بینید، سیستم بلوک های فعلی 1k داده، تعداد inodes \(تعداد فایل ها و دایرکتوری (پوشه) ها\) و محدودیت های نرم و سخت را برای هر یک از آنها نشان می دهد. اگر کاربر از محدودیت های نرم خود عبور کند، ایمیل هایی وجود خواهد داشت. محدودیت های سخت محدودیت های واقعی هستند و کاربر نمی تواند از آنها عبور کند. اگر نیاز به ذخیره محدودیت های نرم یا سخت دارید، فقط فایل را تغییر دهید و آن را ذخیره کنید.

> برای به روز رسانی این داده ها باید `quotacheck` را اجرا کنید

برای کپی محدودیت های یک کاربر به کاربر دیگر، از سوئیچ `-p` استفاده کنید:

```text
# edquota -p jadi newuser neweruser lastuser
```

### گزارش سهمیه

اگر نیاز به بررسی سهمیه تنها یک کاربر دارید از دستور `quota` استفاده کنید.

```text
# quota  jadi
Disk quotas for user jadi (uid 1000):
     Filesystem  blocks   quota   limit   grace   files   quota   limit   grace
      /dev/sda1       5    5000       0               2       0       0
```

اگر کاربران زیادی دارید، این کار آسانی نیست، بنابراین می توانید از `repquota` به شرح زیر استفاده کنید:

```text
# repquota -u -a
*** Report for user quotas on device /dev/sda1
Block grace time: 7days; Inode grace time: 7days
                        Block limits                File limits
User            used    soft    hard  grace    used  soft  hard  grace
----------------------------------------------------------------------
root      --  120288       0       0            401     0     0       
jadi      --       5    5000       0              2     0     0
```

### هشدار به کاربران

دستوری برای بررسی سهمیه ها و هشدار به کاربران به نام `warnquota` وجود دارد. خوب است که آن را هر چند وقت یکبار با استفاده از یک crontab اجرا کنید \(این crontabها را بعداً مشاهده خواهید کرد.

.

.

.

.

.

.

.

.

.

.

.