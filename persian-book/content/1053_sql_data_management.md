Title: 105.3 حذف شد!
Date: 2010-12-03 10:20
Category: LPIC1
Tags: LPIC1, 102, LPIC1-102-500
Authors: Jadi
Summary: 
sortorder: 290
Topic: Shells and Shell Scripting

چقدر خوش شانس! این حذف شده است. اگر اصرار دارید این متن قدیمی بود:
## 105.3 مدیریت داده های SQL

<div class="alert alert-danger" role="alert">
  This chapter is still a Work In Progress. Do not rely on it for LPIC version 500 exam. Will be updated in a few weeks.
</div>


_وزن: 2_

کاندیداها باید بتوانند با استفاده از دستورات اولیه SQL از پایگاه داده پرس و جو کرده و داده ها را دستکاری کنند. این هدف شامل انجام پرس و جوهایی است که شامل پیوستن به 2 جدول و/یا انتخاب فرعی است.

#### حوزه های دانش کلیدی

* استفاده از دستورات اولیه SQL
* دستکاری داده های اولیه را انجام دهید

#### شرایط و امکانات

* درج
* به روز رسانی
* انتخاب کنید
* `rm`
* از
* کجا
* گروه بر اساس
* سفارش توسط
* ملحق شوید

### پایگاه های داده

این ماژول در مورد زبان SQL است و MySQL یکی از بسیاری از پایگاه های داده SQL است. برای این درس، یک پایگاه داده از تعدادی **جدول** تشکیل شده است و هر جدول دارای تعدادی*****ها و **پرونده**ها است. بیایید نگاهی بیندازیم در این درس قرار نیست پایگاه داده _ایجاد_ یا _طراحی_ کنیم. فقط باید درک کلی از پایگاه‌های داده \(پایگاه‌های داده SQL\) داشته باشید و برخی از دستورات را برای استفاده از \ (خواندن پرس و جو یا به‌روزرسانی یا اضافه کردن به آنها\) بدانید. پایگاه داده ای که قرار است در این درس استفاده کنم `lpic` نام دارد و دارای دو جدول `contact` و `info` است.

### خط فرمان (Command Line) mysql

همانطور که گفتم، در اینجا قرار نیست `mysql` را یاد بگیریم، فقط باید روی `SQL` به عنوان یک زبان پرس و جو تمرکز کنیم. فقط باید بدانید که `mysql` یک برنامه خط فرمان (Command Line) برای اتصال غیر فعال به یک `mysql-server` است. من از آن به این صورت استفاده می کنم:

```text
$ mysql -u root -p
```

به این معنی که من از ریشه `u`ser استفاده خواهم کرد و یک رمز عبور ارائه خواهم کرد. همچنین می شد گفت:

```text
$ mysql -u root -p mypass lpic
```

برای ارائه پاس در خط فرمان (Command Line) \(به دلایل امنیتی ایده خوبی نیست!\) و به برنامه mysql بگویید هنگام شروع به پایگاه داده `lpic` متصل شود.

#### با استفاده از پایگاه داده

هنگامی که به یک پایگاه داده متصل می شوید، باید از دستور `use` برای انتخاب پایگاه داده ای که قرار است دستورات را صادر کنید، استفاده کنید. به طور معمول یک سرور پایگاه داده \(مثلا mysql\) می تواند 100 پایگاه داده مختلف در خود داشته باشد که هر کدام برای یک کاربر یا برنامه است.

```text
jadi@funlife:~$ mysql -u root -p
Enter password:
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 17
Server version: 5.6.25-0ubuntu0.15.04.1 (Ubuntu)

Copyright (c) 2000, 2015, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> SHOW DATABASES;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| bad                |
| good               |
| lpic               |
| mysql              |
| performance_schema |
| ugly               |
+--------------------+
7 rows in set (0.00 sec)

mysql> USE LPIC;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
mysql> SHOW TABLES;
+----------------+
| Tables_in_lpic |
+----------------+
| info           |
| phonebook      |
+----------------+
2 rows in set (0.00 sec)
```

همانطور که می بینید `mysql` دوستانه است و میزهای دوست داشتنی را نشان می دهد! به او گفتم `use lpic` و سپس `show tables` و اکنون می دانم که دو جدول دارم: اطلاعات و دفترچه تلفن.

> توجه: تایپ دستورات MYSQL با حروف بزرگ و نام ها و مقادیر و .. با حروف کوچک معمول است.

### انتخاب کنید

`SELECt` واضح است! از یک جدول انتخاب می کند. وقتی مطمئن نیستیم به دنبال چه فیلدی هستیم، می‌توانیم `*` را برای دریافت همه فیلدها انتخاب کنیم.

```text
mysql> SELECT * FROM phonebook;
+--------+------------------+----------------+
| name   | email            | phone          |
+--------+------------------+----------------+
| jadi   | jadi@jadi.net    | +9890something |
| nasrin | nasrin@lpic.test | +9898989898    |
| sina   | far@from.here    | +687randomnum  |
| haale  |                  | 0935secret     |
+--------+------------------+----------------+
4 rows in set (0.00 sec)
```

یا فیلد خاصی را بخواهید:

```text
mysql> SELECT name FROM phonebook;
+--------+
| name   |
+--------+
| jadi   |
| nasrin |
| sina   |
| haale  |
+--------+
3 rows in set (0.00 sec)
```

### کجا

می توانید _conditions_ را با استفاده از `WHERE` به جستارهای SQL خود اضافه کنید. بیایید به جدول دیگری که داریم نگاهی بیندازیم:

```text
mysql> SELECT * FROM info;
+--------+--------+--------+-------+
| name   | height | weight | mood  |
+--------+--------+--------+-------+
| jadi   |    180 |     74 | happy |
| sina   |    175 |     81 | happy |
| nasrin |    174 |     68 | happy |
| mina   |    171 |     59 | sad   |
+--------+--------+--------+-------+
4 rows in set (0.00 sec)
```

اگر فقط بخواهیم دوستان _خوشحال_مان را ببینیم چه؟

```text
mysql> SELECT * FROM info WHERE mood = 'happy';
+--------+--------+--------+-------+
| name   | height | weight | mood  |
+--------+--------+--------+-------+
| jadi   |    180 |     74 | happy |
| sina   |    175 |     81 | happy |
| nasrin |    174 |     68 | happy |
+--------+--------+--------+-------+
3 rows in set (0.00 sec)

mysql>
```

برای _مینا نترس بعدا خوشحالش می کنیم ولی فعلا باید دوستانی که خوشحال هستند و بیش از 80 کیلوگرم هستند را ببینیم.

```text
mysql> SELECT * FROM info WHERE mood = 'happy' AND weight >= 80;
+--------+--------+--------+-------+
| name   | height | weight | mood  |
+--------+--------+--------+-------+
| sina   |    175 |     81 | happy |
+--------+--------+--------+-------+
3 rows in set (0.00 sec)
```

یا اگر فقط به نام نیاز داشتم:

```text
mysql> SELECT name FROM info WHERE mood = 'happy' AND weight >= 80;
+------+
| name |
+------+
| sina |
+------+
1 row in set (0.00 sec)
```

### سفارش توسط

اگر بخواهید داده ها را بر اساس یک فیلد **مرتب کنید** استفاده می شود. در اینجا من دفترچه تلفن خود را بر اساس نام افراد بررسی می کنم:

```text
mysql> SELECT * FROM phonebook ORDER BY name;
+--------+------------------+----------------+
| name   | email            | phone          |
+--------+------------------+----------------+
| haale  |                  | 0935secret     |
| jadi   | jadi@jadi.net    | +9890something |
| nasrin | nasrin@lpic.test | +9898989898    |
| sina   | far@from.here    | +687randomnum  |
+--------+------------------+----------------+
4 rows in set (0.00 sec)
```

این سفارش در هر فیلدی از جمله اعداد قابل انجام است:

```text
mysql> SELECT * FROM info ORDER BY height;
+--------+--------+--------+-------+
| name   | height | weight | mood  |
+--------+--------+--------+-------+
| mina   |    171 |     59 | sad   |
| nasrin |    174 |     68 | happy |
| sina   |    175 |     81 | happy |
| jadi   |    180 |     74 | happy |
+--------+--------+--------+-------+
4 rows in set (0.00 sec)
```

### گروه توسط

این خروجی را گروه بندی می کند. متاسفانه این خیلی واضح نیست. بیایید مثال اول را ببینیم:

```text
mysql> SELECT * FROM info GROUP BY mood;
+------+--------+--------+-------+
| name | height | weight | mood  |
+------+--------+--------+-------+
| jadi |    180 |     74 | happy |
| mina |    171 |     59 | sad   |
+------+--------+--------+-------+
2 rows in set (0.00 sec)
```

ما دیدیم که فقط دو `mood` در جدول داریم: غمگین و شاد. هنگامی که `SELECT`همه فیلدها را \(یعنی `*`\) از این جدول `GROUP BY` می کند، SQL همه حالت ها را بررسی می کند و از هر کدام فقط یک مورد را به ما نشان می دهد. این را می توان مانند دستور `uniq` که از LPIC101 تکیه کردید استفاده کرد:

```text
mysql> SELECT mood FROM info GROUP BY mood;
+-------+
| mood  |
+-------+
| happy |
| sad   |
+-------+
2 rows in set (0.00 sec)
```

که همه حالات موجود در جدول را به شما می دهد. در زندگی واقعی این خیلی مفید نیست و بیشتر اوقات با `count` ترکیب می شود. نگاهی بیندازید:

```text
mysql> SELECT count(mood), mood FROM info GROUP BY mood;
+-------------+-------+
| count(mood) | mood  |
+-------------+-------+
|           3 | happy |
|           1 | sad   |
+-------------+-------+
2 rows in set (0.00 sec)
```

به نظر می رسد خانه بسیاری از ردیف ها آن حالت خاص را دارند. بنابراین من 3 دوست شاد و یک دوست غمگین دارم.

> توجه: `count` بخشی از LPIC 105.3 نیست

### درج کنید

یک دستور واضح دیگر. این یک ردیف جدید به یک جدول اضافه می کند. بگویید می‌خواهم مقداری داده به دفترچه تلفن اضافه کنم:

```text
mysql>  INSERT INTO phonebook (name, phone, email) VALUES ('ghasem', '+982112345678', '');
Query OK, 1 row affected (0.01 sec)

mysql> SELECT * FROM phonebook;
+--------+------------------+----------------+
| name   | email            | phone          |
+--------+------------------+----------------+
| jadi   | jadi@jadi.net    | +9890something |
| nasrin | nasrin@lpic.test | +9898989898    |
| sina   | far@from.here    | +687randomnum  |
| haale  |                  | 0935secret     |
| ghasem |                  | +982112345678  |
+--------+------------------+----------------+
5 rows in set (0.00 sec)
```

### حذف

شما آن را می دانید! این از یک جدول حذف می شود. اما مواظب چیزهایی که حذف می‌کنید باشید... شیطان شما اینجاست:

mysql> حذف از دفترچه تلفن WHERE name = 'ghasem'; پرس و جو تأیید شد، 1 ردیف تحت تأثیر قرار گرفت \(0.01 ثانیه\)

```text
mysql> SELECT * FROM phonebook;
+--------+------------------+----------------+
| name   | email            | phone          |
+--------+------------------+----------------+
| jadi   | jadi@jadi.net    | +9890something |
| nasrin | nasrin@lpic.test | +9898989898    |
| sina   | far@from.here    | +687randomnum  |
| haale  |                  | 0935secret     |
+--------+------------------+----------------+
4 rows in set (0.00 sec)
```

### به روز رسانی

آیا به شما گفتم که SQL شبیه انگلیسی ساده است؟ حق با من بود زیرا می دانید `UPDATE` چه می کند! ردیف \(تغییرها\) را به روز می کند و دوباره `WHERE` دوست شماست:

```text
mysql> SELECT * FROM phonebook;
+--------+------------------+----------------+
| name   | email            | phone          |
+--------+------------------+----------------+
| jadi   | jadi@jadi.net    | +9890something |
| nasrin | nasrin@lpic.test | +9898989898    |
| sina   | far@from.here    | +687randomnum  |
| haale  |                  | 0935secret     |
+--------+------------------+----------------+
4 rows in set (0.00 sec)

mysql> UPDATE phonebook SET  email='haale@lpic.fake' WHERE name = 'haale';
Query OK, 1 row affected (0.01 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> SELECT * FROM phonebook;
+--------+------------------+----------------+
| name   | email            | phone          |
+--------+------------------+----------------+
| jadi   | jadi@jadi.net    | +9890something |
| nasrin | nasrin@lpic.test | +9898989898    |
| sina   | far@from.here    | +687randomnum  |
| haale  | haale@lpic.fake  | 0935secret     |
+--------+------------------+----------------+
4 rows in set (0.00 sec)
```

### بپیوندید

دستور JOIN می تواند پیچیده باشد اما خوشبختانه ما در LPIC1-Exam 102 هستیم و نیازی به یادگیری چیزهای زیادی نداریم. فقط این را بررسی کنید:

```text
mysql>  SELECT * FROM phonebook JOIN info;
+--------+------------------+----------------+--------+--------+--------+-------+
| name   | email            | phone          | name   | height | weight | mood  |
+--------+------------------+----------------+--------+--------+--------+-------+
| jadi   | jadi@jadi.net    | +9890something | jadi   |    180 |     74 | happy |
| nasrin | nasrin@lpic.test | +9898989898    | jadi   |    180 |     74 | happy |
| sina   | far@from.here    | +687randomnum  | jadi   |    180 |     74 | happy |
| haale  | haale@lpic.fake  | 0935secret     | jadi   |    180 |     74 | happy |
| jadi   | jadi@jadi.net    | +9890something | sina   |    175 |     81 | happy |
| nasrin | nasrin@lpic.test | +9898989898    | sina   |    175 |     81 | happy |
| sina   | far@from.here    | +687randomnum  | sina   |    175 |     81 | happy |
| haale  | haale@lpic.fake  | 0935secret     | sina   |    175 |     81 | happy |
| jadi   | jadi@jadi.net    | +9890something | nasrin |    174 |     68 | happy |
| nasrin | nasrin@lpic.test | +9898989898    | nasrin |    174 |     68 | happy |
| sina   | far@from.here    | +687randomnum  | nasrin |    174 |     68 | happy |
| haale  | haale@lpic.fake  | 0935secret     | nasrin |    174 |     68 | happy |
| jadi   | jadi@jadi.net    | +9890something | mina   |    171 |     59 | sad   |
| nasrin | nasrin@lpic.test | +9898989898    | mina   |    171 |     59 | sad   |
| sina   | far@from.here    | +687randomnum  | mina   |    171 |     59 | sad   |
| haale  | haale@lpic.fake  | 0935secret     | mina   |    171 |     59 | sad   |
+--------+------------------+----------------+--------+--------+--------+-------+
16 rows in set (0.00 sec)
```

هر ردیف از جدول اول \(دفترچه تلفن\) در مقابل جدول دوم \(اطلاعات\) کپی می شود. _هنوز خیلی مفید نیست. زمانی مفید می شود که یک _فیلد مشترک_ بدهید یا بر اساس یک معیار به جداول JOIN بگویید. با استفاده از `WHERE`. جادو اینجاست:

```text
mysql> SELECT * FROM phonebook JOIN info ON phonebook.name = info.name;
+--------+------------------+----------------+--------+--------+--------+-------+
| name   | email            | phone          | name   | height | weight | mood  |
+--------+------------------+----------------+--------+--------+--------+-------+
| jadi   | jadi@jadi.net    | +9890something | jadi   |    180 |     74 | happy |
| sina   | far@from.here    | +687randomnum  | sina   |    175 |     81 | happy |
| nasrin | nasrin@lpic.test | +9898989898    | nasrin |    174 |     68 | happy |
+--------+------------------+----------------+--------+--------+--------+-------+
3 rows in set (0.00 sec)
```

عالیه حالا من لیست firned ها، حالات روحی و شماره تلفن آنها را دارم! بگو من حوصله ام سر رفته است و باید با یک دوست خوب تماس بگیرم:

```text
mysql> SELECT phonebook.name, phone, mood FROM phonebook JOIN info ON phonebook.name = info.name WHERE mood = 'happy';
+--------+----------------+-------+
| name   | phone          | mood  |
+--------+----------------+-------+
| jadi   | +9890something | happy |
| sina   | +687randomnum  | happy |
| nasrin | +9898989898    | happy |
+--------+----------------+-------+
3 rows in set (0.00 sec)
```

> توجه: هر دو جدول دارای یک فیلد به نام `name` هستند، بنابراین باید از phonebook.name استفاده کنم تا به SQL بگویم کدام نام را می خواهم نشان دهم.

بدیهی است که می‌توانیم معیارهای بیشتری اضافه کنیم و با فردی با قد کوتاه‌تر از 175 سانتی‌متر بیرون برویم:

```text
mysql> SELECT phonebook.name, phone, mood FROM phonebook JOIN info ON phonebook.name = info.name AND height < 175;
+--------+-------------+-------+
| name   | phone       | mood  |
+--------+-------------+-------+
| nasrin | +9898989898 | happy |
+--------+-------------+-------+
1 row in set (0.00 sec)
```

باحال؟ اما ما هنوز تمام نشده ایم من دوست ندارم دوستان غمگینی داشته باشم و یکی دارم، اجازه دهید او را نیز خوشحال کنیم!

```text
mysql> SELECT * FROM info WHERE mood = 'sad';
+------+--------+--------+------+
| name | height | weight | mood |
+------+--------+--------+------+
| mina |    171 |     59 | sad  |
+------+--------+--------+------+
1 row in set (0.01 sec)

mysql> UPDATE info SET mood = 'happy' WHERE name = 'mina';
Query OK, 0 rows affected (0.02 sec)
Rows matched: 1  Changed: 0  Warnings: 0

mysql> SELECT * FROM info WHERE mood = 'sad';                                   
Empty set (0.00 sec)

mysql> SELECT * FROM info;
+--------+--------+--------+-------+
| name   | height | weight | mood  |
+--------+--------+--------+-------+
| jadi   |    180 |     74 | happy |
| sina   |    175 |     81 | happy |
| nasrin |    174 |     68 | happy |
| mina   |    171 |     59 | happy |
+--------+--------+--------+-------+
4 rows in set (0.00 sec)
```

آسان. دستور آخر حتی ساده تر است:

### ترک

```text
mysql> quit
Bye
jadi@funlife:~$
```

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