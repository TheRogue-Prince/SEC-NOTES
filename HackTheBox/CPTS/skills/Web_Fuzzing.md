Q1. Run a sub-domain/vhost fuzzing scan on '*.academy.htb' for the IP shown above. What are all the sub-domains you can identify? (Only write the sub-domain name)

```
ffuf -u http://154.57.164.65:30611/ \
  -H 'Host: FUZZ.academy.htb' \
  -w /home/satoru/SecLists/Discovery/DNS/subdomains-top1million-110000.txt \
  -t 64 -fs 985

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://154.57.164.65:30611/
 :: Wordlist         : FUZZ: /home/satoru/SecLists/Discovery/DNS/subdomains-top1million-110000.txt
 :: Header           : Host: FUZZ.academy.htb
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 64
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
 :: Filter           : Response size: 985
________________________________________________

test                    [Status: 200, Size: 0, Words: 1, Lines: 1, Duration: 611ms]
archive                 [Status: 200, Size: 0, Words: 1, Lines: 1, Duration: 606ms]
faculty                 [Status: 200, Size: 0, Words: 1, Lines: 1, Duration: 956ms]

```

Q2. Before you run your page fuzzing scan, you should first run an extension fuzzing scan. What are the different extensions accepted by the domains?
```
ffuf -u http://archive.academy.htb:30611/index.FUZZ -w /home/satoru/SecLists/Discovery/Web-Content/web-extensions.txt       

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://archive.academy.htb:30611/index.FUZZ
 :: Wordlist         : FUZZ: /home/satoru/SecLists/Discovery/Web-Content/web-extensions.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
________________________________________________

.phps                   [Status: 403, Size: 287, Words: 20, Lines: 10, Duration: 748ms]
:: Progress: [43/43] :: Job [1/1] :: 10 req/sec :: Duration: [0:00:05] :: Errors: 0 ::
                                                                                                
┌──(satoru㉿satoru)-[~/…/HTB/CPTS/skills/web_fuzzing]
└─$ ffuf -u http://test.academy.htb:30611/index.FUZZ -w /home/satoru/SecLists/Discovery/Web-Content/web-extensions.txt       

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://test.academy.htb:30611/index.FUZZ
 :: Wordlist         : FUZZ: /home/satoru/SecLists/Discovery/Web-Content/web-extensions.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
________________________________________________

.phps                   [Status: 403, Size: 284, Words: 20, Lines: 10, Duration: 816ms]
:: Progress: [43/43] :: Job [1/1] :: 21 req/sec :: Duration: [0:00:03] :: Errors: 0 ::
                                                                                                
┌──(satoru㉿satoru)-[~/…/HTB/CPTS/skills/web_fuzzing]
└─$ ffuf -u http://faculty.academy.htb:30611/index.FUZZ -w /home/satoru/SecLists/Discovery/Web-Content/web-extensions.txt       

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://faculty.academy.htb:30611/index.FUZZ
 :: Wordlist         : FUZZ: /home/satoru/SecLists/Discovery/Web-Content/web-extensions.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
________________________________________________

.phps                   [Status: 403, Size: 287, Words: 20, Lines: 10, Duration: 754ms]
:: Progress: [43/43] :: Job [1/1] :: 13 req/sec :: Duration: [0:00:04] :: Errors: 0 ::


use a bigger wordlist.

```




```
 ffuf -u 'http://test.academy.htb:30611/index.FUZZ' \
-w <(printf "php\nphp7\nphps\n") \
-mc all

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://test.academy.htb:30611/index.FUZZ
 :: Wordlist         : FUZZ: /proc/self/fd/11
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: all
________________________________________________

php                     [Status: 200, Size: 0, Words: 1, Lines: 1, Duration: 336ms]
php7                    [Status: 404, Size: 281, Words: 23, Lines: 10, Duration: 337ms]
phps                    [Status: 403, Size: 284, Words: 20, Lines: 10, Duration: 342ms]
:: Progress: [3/3] :: Job [1/1] :: 8 req/sec :: Duration: [0:00:01] :: Errors: 0 ::

```

Q3. One of the pages you will identify should say 'You don't have access!'. What is the full page URL?


```
You sure you wanna cancel this scan: http://faculty.academy.htb:30611/? [Y/n]
Stopping http://faculty.academy.htb:30611/...




 ___  ___  __   __     __      __         __   ___
|__  |__  |__) |__) | /  `    /  \ \_/ | |  \ |__
|    |___ |  \ |  \ | \__,    \__/ / \ | |__/ |___
by Ben "epi" Risher                    ver: 2.13.1
───────────────────────────┬──────────────────────
     Target Url            │ http://faculty.academy.htb:30611/
     In-Scope Url          │ faculty.academy.htb
     Threads               │ 64
     Wordlist              │ /home/satoru/SecLists/Discovery/Web-Content/directory-list-2.3-medium.txt
     Status Codes          │ [200, 204, 301, 302, 307, 401, 403]
     Timeout (secs)        │ 7
     User-Agent            │ feroxbuster/2.13.1
     Config File           │ /etc/feroxbuster/ferox-config.toml
     Extract Links         │ true
     Extensions            │ [php, php7, phps]
     HTTP methods          │ [GET]
     Recursion Depth       │ 4
───────────────────────────┴──────────────────────
 🏁  Press [ENTER] to use the Scan Management Menu™
──────────────────────────────────────────────────
200      GET        0l        0w        0c http://faculty.academy.htb:30611/                    200      GET        0l        0w        0c http://faculty.academy.htb:30611/index.php           200      GET        0l        0w        0c http://faculty.academy.htb:30611/index.php7          301      GET        9l       28w      337c http://faculty.academy.htb:30611/courses => http://faculty.academy.htb:30611/courses/                                                                200      GET        0l        0w        0c http://faculty.academy.htb:30611/courses/index.php   200      GET        0l        0w        0c http://faculty.academy.htb:30611/courses/index.php7  200      GET       53l       81w      774c http://faculty.academy.htb:30611/courses/linux-security.php7

```

i used feroxbuster instead its actually faster and easy.


