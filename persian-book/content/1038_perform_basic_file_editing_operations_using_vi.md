Title: 103.8 ویرایش اولیه فایل
Date: 2010-12-03 10:20
Category: LPIC1
Tags: LPIC1, 101, LPIC1-101-500
Authors: Jadi
Summary: 
sortorder: 190

_وزن: 3_

داوطلبان باید قادر به ویرایش فایل های متنی با استفاده از vi. این هدف شامل ناوبری vi، حالت‌های vi، درج، ویرایش، حذف، کپی و یافتن متن است. همچنین شامل آگاهی از سایر ویرایشگرهای رایج و تنظیم ویرایشگر پیش فرض است.

### اهداف

* با استفاده از vi در یک سند پیمایش کنید.
* درک و استفاده از حالت های vi.
* درج، ویرایش، حذف، کپی و یافتن متن در vi.
* آگاهی از Emacs، nano و vim.
* ویرایشگر استاندارد را پیکربندی کنید.

* vi
*/،؟
* h،j،k،l
* من، o، a
* d، p، y، dd، yy
* ZZ، :w!، :q!
* ویرایشگر

<iframe width="560" height="315" src="https://www.youtube.com/embed/7S5RaX1OsTE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

### مقدمه
مانند هر ابزار دیگری، در مورد ویرایشگرهای متن، طیف وسیعی از انتخاب داریم. یکی از رایج ترین و بسیار قدرتمندترین گزینه ها ویرایشگر `vi` است. این از پیش روی همه توزیع‌های اصلی لینوکس نصب شده است و می‌توانید مطمئن باشید که دانستن آن به شما امکان می‌دهد فایل‌های خود را در همه محیط‌ها ویرایش کنید، اجازه دهید یک سرور راه دور از طریق SSH یا یک محیط برنامه‌نویسی در دستگاه دسکتاپ شما یا یک دستگاه CyberDeck با حداقل صفحه کلید باشد. تنها اشکال آن ممکن است نوعی منحنی یادگیری کند آن باشد، اما من مطمئن هستم که پس از یک جلسه 1 ساعته با آن، شما موفق خواهید شد راه خود را در `vi` پیدا کنید.

یک نسخه _Improved_ از `vi` وجود دارد که _VIMproved_ یا `vim` نامیده می شود. گاهی اوقات این همان چیزی است که در سیستم خود پیدا می کنید و گاهی اوقات دستور `vi` نام مستعار یا به `vim` پیوند داده می شود. بیایید این را در سیستم خود بررسی کنیم (اوبونتو 22.04):

```
jadi@funlife:~$ whatis vi
vi (1)               - Vi IMproved, a programmer's text editor
jadi@funlife:~$ whereis vi
vi: /usr/bin/vi /usr/share/man/man1/vi.1.gz
jadi@funlife:~$ whatis vim
vim (1)              - Vi IMproved, a programmer's text editor
jadi@funlife:~$ whereis vim
vim: /usr/bin/vim /etc/vim /usr/share/vim /usr/share/man/man1/vim.1.gz
jadi@funlife:~$ vi --version
VIM - Vi IMproved 9.0 (2022 Jun 28, compiled Aug 23 2022 20:18:58)
Included patches: 1-242
Modified by team+vim@tracker.debian.org
Compiled by team+vim@tracker.debian.org
Huge version without GUI.  Features included (+) or not (-):
+acl               +file_in_path      +mouse_urxvt       -tag_any_white
+arabic            +find_in_path      +mouse_xterm       -tcl
+autocmd           +float             +multi_byte        +termguicolors
+autochdir         +folding           +multi_lang        +terminal
-autoservername    -footer            -mzscheme          +terminfo
-balloon_eval      +fork()            +netbeans_intg     +termresponse
+balloon_eval_term +gettext           +num64             +textobjects
-browse            -hangul_input      +packages          +textprop
++builtin_terms    +iconv             +path_extra        +timers
+byte_offset       +insert_expand     -perl              +title
+channel           +ipv6              +persistent_undo   -toolbar
+cindent           +job               +popupwin          +user_commands
-clientserver      +jumplist          +postscript        +vartabs
-clipboard         +keymap            +printer           +vertsplit
+cmdline_compl     +lambda            +profile           +vim9script
+cmdline_hist      +langmap           -python            +viminfo
+cmdline_info      +libcall           +python3           +virtualedit
+comments          +linebreak         +quickfix          +visual
+conceal           +lispindent        +reltime           +visualextra
+cryptv            +listcmds          +rightleft         +vreplace
+cscope            +localmap          -ruby              +wildignore
+cursorbind        -lua               +scrollbind        +wildmenu
+cursorshape       +menu              +signs             +windows
+dialog_con        +mksession         +smartindent       +writebackup
+diff              +modify_fname      +sodium            -X11
+digraphs          +mouse             -sound             -xfontset
-dnd               -mouseshape        +spell             -xim
-ebcdic            +mouse_dec         +startuptime       -xpm
+emacs_tags        +mouse_gpm         +statusline        -xsmp
+eval              -mouse_jsbterm     -sun_workshop      -xterm_clipboard
+ex_extra          +mouse_netterm     +syntax            -xterm_save
+extra_search      +mouse_sgr         +tag_binary        
-farsi             -mouse_sysmouse    -tag_old_static    
   system vimrc file: "/etc/vim/vimrc"
     user vimrc file: "$HOME/.vimrc"
 2nd user vimrc file: "~/.vim/vimrc"
      user exrc file: "$HOME/.exrc"
       defaults file: "$VIMRUNTIME/defaults.vim"
  fall-back for $VIM: "/usr/share/vim"
Compilation: gcc -c -I. -Iproto -DHAVE_CONFIG_H -Wdate-time -g -O2 -ffile-prefix-map=/build/vim-Oy69Mt/vim-9.0.0242=. -flto=auto -ffat-lto-objects -flto=auto -ffat-lto-objects -fstack-protector-strong -Wformat -Werror=format-security -DSYS_VIMRC_FILE=\"/etc/vim/vimrc\" -DSYS_GVIMRC_FILE=\"/etc/vim/gvimrc\" -D_REENTRANT -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 
Linking: gcc -Wl,-Bsymbolic-functions -flto=auto -ffat-lto-objects -flto=auto -Wl,-z,relro -Wl,-z,now -Wl,--as-needed -o vim -lm -ltinfo -lselinux -lsodium -lacl -lattr -lgpm -L/usr/lib/python3.10/config-3.10-x86_64-linux-gnu -lpython3.10 -lcrypt -ldl -lm -lm 
```

برای ویرایش یک فایل با vi کافیست نام فایل را به آن بدهید:

```text
$ vi file.txt
```

### حالت های vi

`vi` در دو حالت کار می کند:

1. **حالت دستور** جایی است که شما به دور فایل می روید، جستجو می کنید، متن را حذف می کنید، کپی پیست می کنید، جایگزین می کنید، ... و دستورات دیگری را به vi می دهید. برخی از دستورات با یک `:` شروع می شوند و برخی فقط یک فشار کلید هستند.
2. ** حالت درج ** جایی است که آنچه تایپ می کنید، در موقعیت مکان نما به فایل می رود.

> برای تغییر حالت Command، کلید ESC را فشار دهید. برای بازگشت به حالت Insert، می توانید از چندین دستور استفاده کنید اما یکی از دستورات رایج فشار دادن کلید `i` است.

### حرکت مکان نما

برای حرکت در یک فایل متنی، از این کلیدها در حالت فرمان استفاده کنید:

| کلید | تابع |
| :---: | :--- |
| h | یک کاراکتر در سمت چپ \(فقط خط فعلی\) |
| j | یک خط پایین |
| k | یک صف |
| l | یک کاراکتر در سمت راست \(فقط خط فعلی\) |
| w | کلمه بعدی در خط فعلی |
| e | انتهای بعدی کلمه در خط فعلی |
| b | شروع قبلی کلمه در خط فعلی |
| Ctrl-f | یک صفحه به جلو بروید |
| Ctrl-b | یک صفحه به عقب اسکرول کنید |

> تایپ یک عدد قبل از اکثر دستورات، این فرمان را چندین بار تکرار می کند \(یعنی `6h` 6 کاراکتر به سمت چپ می رود\)

#### پریدن به اطراف

| کلید | تابع |
| :---: | :--- |
| G | بدون شماره، به آخر می‌پرد و 10G به خط 10 می‌پرد |
| H | 5H از بالای صفحه به خط 5 می رود |
| L | 3L مکان نما را به خط 3 تا آخرین خط صفحه نمایش منتقل می کند |

### ویرایش متن

این دستورات در حالت _command_ به شما کمک می کند تا وارد، ویرایش، جایگزینی و متن کنید:

| کلید | تابع |
| :---: | :--- |
| من | وارد حالت درج |
| یک | بعد از موقعیت فعلی مکان نما وارد حالت درج شوید
| r | جایگزینی تنها یک کاراکتر |
| o | یک خط جدید زیر مکان نما باز کنید و به حالت درج | بروید
| O | یک خط جدید بالای مکان نما باز کنید و به حالت درج | بروید
| ج | به یک مکان پاک کنید و به حالت درج بروید و تا آنجا جایگزین کنید و سپس درج معمولی \(`cw` کلمه فعلی را بازنویسی می کند\) |
| d | حذف کنید. می توانید برای حذف یک کلمه با w \(`dw`\) ترکیب کنید. مانند cw اما dw به حالت درج نمی رود |
| dd | حذف خط فعلی |
| x | حذف کاراکتر در موقعیت مکان نما |
| p | آخرین متن حذف شده را بعد از نشانگر | قرار دهید
| P | آخرین متن حذف شده را قبل از نشانگر | قرار دهید
| xp | کاراکتر را در موقعیت مکان نما با نویسه سمت راست آن |

### جستجو

| کلید | تابع |
| :---: | :--- |
| / | به جلو جستجو کنید \(`/happiness` شادی بعدی را خواهد یافت\) |
| ? | جستجو به عقب |
| n | جستجوی قبلی را تکرار کنید همچنین می توانید از `/` و `?` بدون هیچ پارامتری استفاده کنید\) |

> پس از رسیدن به انتهای فایل، جستجو به بالا می‌پیچد

### در حال خروج

همیشه خنده دار است وقتی می بینید که شخصی وارد vi می شود و نمی داند چگونه از آن خارج شود! اینها را یاد بگیرید و از خنده جلوگیری کنید:

| کلید | تابع |
| :---: | :--- |
| :ق! | ترک ویرایش بدون ذخیره = فرار بعد از هر اشتباه |
| :w! | فایل \(چه اصلاح شده باشد چه نباشد\) را بنویسید. تلاش برای بازنویسی فایل های موجود یا فقط خواندنی یا سایر فایل های غیرقابل نوشتن |
| :w myfile.txt | نوشتن به نام جدید |
| ZZ | از فایل خارج شده و در صورت تغییر | ذخیره کنید
| :e! | بارگیری مجدد فایل از دیسک |
| : | اجرای یک فرمان پوسته |

وارد کردن کولون \(`:`\) در حالت _command mode، مکان نما را به پایین صفحه منتقل می کند و vi منتظر دستورات شما می ماند. ESC را فشار دهید تا به حالت دستور عادی برگردید.

> علامت تعجب در اکثر دستورات می‌گوید «من می‌دانم چه کار می‌کنم» و در صورت دسترسی روی فایل‌های فقط خواندنی می‌نویسد و بدون درخواست از آن خارج می‌شوید.

> امکان ترکیب دستورات وجود دارد. برای مثال می‌توانید `:w` و `:q` را ترکیب کنید و فقط بگویید `:wq` (نوشتن و خروج).
### کمک کنید

همیشه می‌توانید با `:help` یا `:help subject` کمک بخواهید. به این ترتیب vi یک متن راهنما را باز می کند که می توانید مانند هر متن دیگری از آن استفاده کنید / جستجو کنید. با دستور `:q` آن را ببندید.

## سایر ویرایشگران
در صورت تمایل می توانید از ویرایشگرهای دیگر نیز استفاده کنید. یکی از گزینه‌های آسان برای استفاده و رایج، `nano` است و برخی از گزینه‌های دیگر عبارتند از `micro`، `emacs` (کاملاً برجسته) و `neovim` (به‌روزرسانی برای vim).

## ویرایشگر پیش فرض
ویرایشگر پیش‌فرض در `bash` با استفاده از متغیر محیطی `EDITOR` تنظیم شده است. شما می توانید آن را با:

```
$ export EDITOR='vim'
```

یا با افزودن خط بالا به فایل `.bashrc`. در فصل های بعدی این موارد را با جزئیات بیشتر خواهیم دید.