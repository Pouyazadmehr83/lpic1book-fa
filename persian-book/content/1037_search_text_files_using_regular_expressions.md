Title: 103.7 فایل های متنی را با استفاده از عبارات باقاعده (Regular Expressions - Regex) جستجو کنید
Date: 2010-12-03 10:20
Category: LPIC1
Tags: LPIC1, 101, LPIC1-101-500
Authors: Jadi
Summary: 
sortorder: 180

_وزن: 3_

داوطلبان باید بتوانند فایل ها و داده های متنی را با استفاده از عبارات باقاعده (Regular Expressions - Regex) دستکاری کنند. این هدف شامل ایجاد عبارات باقاعده (Regular Expressions - Regex) ساده حاوی چندین عنصر نمادین و همچنین درک تفاوت بین عبارات باقاعده (Regular Expressions - Regex) پایه و توسعه یافته است. همچنین شامل استفاده از ابزارهای عبارت منظم برای انجام جستجو از طریق سیستم‌فایل (Filesystem) یا محتوای فایل است.


## اهداف

* عبارات باقاعده (Regular Expressions - Regex) ساده حاوی چندین عنصر نمادین ایجاد کنید.
* تفاوت بین عبارات باقاعده (Regular Expressions - Regex) پایه و توسعه یافته را درک کنید.
* مفاهیم کاراکترهای خاص، کلاس های کاراکتر، کمیت کننده ها و لنگرها را درک کنید.
* از ابزارهای عبارت منظم برای انجام جستجو در فایل سیستم یا محتوای فایل استفاده کنید.
* از عبارات باقاعده (Regular Expressions - Regex) برای حذف، تغییر و جایگزینی متن استفاده کنید.

* گرپ
* egrep
* fgrep
*سد
* regex (7)

<iframe width="560" height="315" src="https://www.youtube.com/embed/wa1OFZ-Ck-0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

### Regex

عبارت منظم، Regex، regex الگویی است برای توصیف آنچه می‌خواهید از یک متن _مطابق_کنید. برای مثال `a` و `ad` هر دو با `jadi` مطابقت دارند. `d.` یک مثال _عمیق_تر است زیرا `.` به معنای _هرچیزی است بنابراین `d.` با دو نویسه آخر `jadi` مطابقت دارد. در این بخش، دستور *grep** \(generalized regular expression processor\) را پوشش خواهیم داد. دارای گویش _ regex متفاوت است. به طور خلاصه Basic regex و Extended regex.

#### اصول Regex

**تطابق ساده**
شما به سادگی می توانید هر چیزی را که می خواهید مطابقت دهید بنویسید و regex آن را جستجو می کند.

| Regex | مطابقت خواهد داشت |
| :--- | :--- |
| یک | **a**fter, min**a**, b**a**nana, j**a**di |
| na | **na**rator, mi**na**, **na**nanana batman, so**na**r |

</br>

**تکرار**

* **`\*`** به معنای تکرار 0 یا بیشتر نویسه قبلی است.
* **`+`** به معنای تکرار نویسه قبلی 1 بار یا بیشتر است.
* **`?`** به معنای تکرار صفر یا یک است.
* **`{n,m}`** به این معنی است که مورد باید حداقل n بار، اما نه بیش از m بار مطابقت داشته باشد.

| Regex | مطابقت خواهد داشت | توجه |
| :--- | :--- | :--- |
| a\*b | ab, aaab, aaaab, aaabthis |  |
| a\*b | ب، هوشیار | باید صفر یا بیشتر `a`s و سپس `b` داشته باشیم |
| a+b | ab, aab, aaabenz | با **هوشیار** یا **b** مطابقت ندارد زیرا باید حداقل یک **a** | وجود داشته باشد
| a?b | ab، a**ab**، b، batman \(صفر a سپس b\)، ... | . |

</br>

**تناوب \(\|\)**

اگر بگویید `a|b` با `a` یا `b` مطابقت دارد.

</br>

**کلاس شخصیت**

نقطه \(**`.`**\) به معنای هر کاراکتری است. بنابراین **`..`** با هر چیزی که حداقل دو نویسه در آن باشد مطابقت خواهد داشت. همچنین می‌توانید کلاس‌های خود را با \[abc\] که با a یا b یا c و \[a-z\] که a با z مطابقت دارد ایجاد کنید.

همچنین می توانید به ارقام با \d مراجعه کنید. 

> regex به حروف بزرگ و کوچک حساس است.

**محدوده**

کوتاه‌نویسی برای کلاس‌های رایج وجود دارد. کلاس‌های نام‌گذاری‌شده با `[:` شروع و با `:]` خاتمه می‌یابند.

| محدوده | معنی |
| :--- | :--- |
| \[:alnum:\] | کاراکترهای حروف عددی |
| \[:blank:\] | کاراکترهای Space و Tab |
| \[:digit:\] | ارقام 0 تا 9 \(معادل 0-9\) |
| \[:upper:\] و \[:lower:\] | حروف بزرگ و کوچک به ترتیب. |
| ^ \(نفی\) | همانطور که اولین کاراکتر بعد از \[ در یک کلاس کاراکتر، حس بقیه کاراکترهای |

> یک regex رایج مورد استفاده .\* است که با هر کاراکتر \(صفر یا هر طول\) مطابقت دارد.

**تطابق در مکان های خاص **

* کارت **`^`** به معنای ابتدای رشته است.
* دلار **`$`** به معنای انتهای رشته است.

#### نمونه ها

* `^a.*` با هر چیزی که با **a** شروع می شود مطابقت دارد.
* `^a.*b$` با هر چیزی که با **a** شروع می شود و با **b** ختم می شود مطابقت دارد.
* `^a.*\d+.*b$` با هر چیزی که با **a** شروع می شود، وسط آن تعدادی رقم و با **b** ختم می شود مطابقت دارد.
* `^(l|b)oo` با هر چیزی که با **l** یا **b** شروع می شود و سپس **oo** دارد مطابقت دارد.
* `[f-h]|[A-K]$` آخرین نویسه باید **f** تا **h** \(small\) یا **A** تا **K** \(capital\) باشد.

### grep

دستور `grep` می تواند در داخل فایل ها جستجو کند.

```text
$ grep funk words 
Garfunkel
Garfunkel's
funk
funked
funkier
funkiest
funking
funk's
funks
funky

```

اینها رایج ترین سوئیچ ها هستند:

| سوئیچ | معنی |
| :--- | :--- |
| -c | فقط تعداد را نشان دهید |
| -v | معکوس کردن جستجو |
| -n | نمایش شماره خطوط |
| -l | نمایش فقط نام فایل |
| -i | حساس به حروف بزرگ و کوچک |
| -r | خواندن تمام فایل های زیر هر فهرست، به صورت بازگشتی |

</br>

```
$ grep a *txt
friends.txt:Rosha
friends.txt:Xavier
friends.txt:Krishna
friends.txt:Mary
my_thinkgs.txt:laptop
$ grep z *txt
$ grep z *txt -i 
friends.txt:Zee
$ grep x words -i -c 
2264
$ grep z *txt -i -l
friends.txt
$ grep Z *txt -v
friends.txt:Rosha
friends.txt:Jim
friends.txt:Xavier
friends.txt:Krishna
friends.txt:Mary
my_thinkgs.txt:laptop
my_thinkgs.txt:pillow
my_thinkgs.txt:shorts
my_thinkgs.txt:t-shirt
$ grep Z friends.txt -v
Rosha
Jim
Xavier
Krishna
Mary
$ 
```

به عنوان مثالی دیگر، بیایید تمام `/etc` را برای همه فایل‌های حاوی یک آدرس IP جستجو کنیم و خطاها (عمدتاً "شما مجوز خواندن این را ندارید") را به `/dev/null` ارسال کنیم:

```
$ egrep -r "192.168.(1|0)." /etc/ 2> /dev/null
/etc/privoxy/config:#      address 192.168.0.1 on your local private network
/etc/privoxy/config:#      (192.168.0.0) and has another outside connection with a
/etc/privoxy/config:#        listen-address  192.168.0.1:8118
/etc/avahi/hosts:# 192.168.0.1 router.local
/etc/dhcp/dhclient-exit-hooks.d/rfc3442-classless-routes:#   new_rfc3442_classless_static_routes='24 192 168 10 192 168 1 1 8 10 10 17 66 41'
/etc/dhcp/dhclient-exit-hooks.d/rfc3442-classless-routes:#   192.168.10.0/24 via 192.168.1.1
/etc/hosts:192.168.1.22 atiteltestbed
/etc/hosts:192.168.100.244 adpsms
/etc/ppp/options:# ms-dns 192.168.1.1
/etc/ppp/options:# ms-dns 192.168.1.2
/etc/ppp/options:# ms-wins 192.168.1.50
/etc/ppp/options:# ms-wins 192.168.1.51
/etc/ssl/openssl.cnf:# proxy = # set this as far as needed, e.g., http://192.168.1.1:8080
/etc/cups/cups-browsed.conf:# BrowseAllow 192.168.1.12
/etc/cups/cups-browsed.conf:# BrowseAllow 192.168.1.0/24
/etc/cups/cups-browsed.conf:# BrowseAllow 192.168.1.0/255.255.255.0
/etc/cups/cups-browsed.conf:# BrowseDeny 192.168.1.13
/etc/proxychains4.conf:## Exclude connections to 192.168.1.0/24 with port 80
/etc/proxychains4.conf:# localnet 192.168.1.0:80/255.255.255.0
/etc/proxychains4.conf:## Exclude connections to 192.168.100.0/24
/etc/proxychains4.conf:# localnet 192.168.100.0/255.255.255.0
/etc/proxychains4.conf:# localnet 192.168.0.0/255.255.0.0
/etc/proxychains4.conf:#	 	socks4	192.168.1.49	1080
/etc/sane.d/kodakaio.conf:#net 192.168.1.2 0x4041
/etc/sane.d/kodakaio.conf:#net 192.168.1.17 0x4067
/etc/sane.d/epsonds.conf:# net 192.168.1.123
/etc/sane.d/airscan.conf:#"Kyocera MFP Scanner" = http://192.168.1.102:9095/eSCL
/etc/sane.d/airscan.conf:#ip    = 192.168.0.1    ; blacklist by address
/etc/sane.d/airscan.conf:#ip    = 192.168.0.0/24 ; blacklist the whole subnet
/etc/sane.d/dell1600n_net.conf:#named_scanner: 192.168.0.20
/etc/sane.d/epson2.conf:# net 192.168.1.123
/etc/sane.d/magicolor.conf:# net 192.168.0.1
/etc/sane.d/saned.conf:#192.168.0.1
/etc/sane.d/saned.conf:#192.168.0.1/29
/etc/fwupd/redfish.conf:# ex: https://192.168.0.133:443
```

### grep گسترده
Regex جالب است و `grep` عالی است، بنابراین افراد زیادی سعی کرده اند به آنها اضافه کنند یا انواع آنها را اختراع کنند. یکی گنو Extended grep است. این گویش regex نیازی به فرار زیاد ندارد و می توانید از طریق سوئیچ `-E` یا استفاده از `egrep` به جای `grep` معمولی از آن استفاده کنید. برای مثال، `|` در یک regex توسعه یافته به معنای "یا" است. بنابراین می‌توانید یک `egrep "a|b" words` انجام دهید تا هر چیزی را با `a` یا `b` مطابقت دهید. 

### grep ثابت شد

اگر نیاز به جستجوی رشته‌های دقیق دارید \(و نه اینکه آن را به صورت regex تفسیر کنید)، از `grep -F` یا `fgrep` استفاده کنید تا `fgrep this$` به انتهای خط نرود و در عوض _this$that_ را پیدا کند.

### sed

در درس‌های قبلی، استفاده ساده از `sed` را دیدیم و اکنون یک خبر عالی برای شما دارم: **sed regex را می‌فهمد**! می‌توانید از سوئیچ `-r` استفاده کنید تا به sed بگویید که از regexe استفاده می‌کنیم.

```
$ sed -r "s/(Z|R|J)/starts with ZRJ/" friends.txt 
starts with ZRJee
starts with ZRJosha
starts with ZRJim
Xavier
Krishna
Mary
```

سوئیچ های رایج:

| سوئیچ | معنی |
| :--- | :--- |
| -r | استفاده از regex پیشرفته |
| -n | سرکوب خروجی، می توانید از p در انتهای regex \( /something/p \) برای چاپ خروجی استفاده کنید |

</br>

```
sed -rn "s/happy/HAPPY/p" words 
HAPPY
slapHAPPY
unHAPPY
```

هنوز مشتاق یادگیری هستید؟ ببینید چگونه می توانید Wordle را با استفاده از regexes حل کنید:

<iframe width="560" height="315" src="https://www.youtube.com/embed/ZbdTghkVM_4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>