Makesense is a medium difficulty hackthebox machine.

```
└─$ sudo nmap -sCV -v -F 10.129.220.85 -oA nmap
[sudo] password for satoru: 
Sorry, try again.
[sudo] password for satoru: 
Starting Nmap 7.99 ( https://nmap.org ) at 2026-07-05 08:00 +0530
NSE: Loaded 158 scripts for scanning.
NSE: Script Pre-scanning.
Initiating NSE at 08:00
Completed NSE at 08:00, 0.00s elapsed
Initiating NSE at 08:00
Completed NSE at 08:00, 0.00s elapsed
Initiating NSE at 08:00
Completed NSE at 08:00, 0.00s elapsed
Initiating Ping Scan at 08:00
Scanning 10.129.220.85 [4 ports]
Completed Ping Scan at 08:00, 0.28s elapsed (1 total hosts)
Initiating Parallel DNS resolution of 1 host. at 08:00
Completed Parallel DNS resolution of 1 host. at 08:00, 0.50s elapsed
Initiating SYN Stealth Scan at 08:00
Scanning 10.129.220.85 [100 ports]
Discovered open port 22/tcp on 10.129.220.85
Discovered open port 443/tcp on 10.129.220.85
Completed SYN Stealth Scan at 08:00, 3.66s elapsed (100 total ports)
Initiating Service scan at 08:00
Scanning 2 services on 10.129.220.85
Completed Service scan at 08:00, 13.60s elapsed (2 services on 1 host)
NSE: Script scanning 10.129.220.85.
Initiating NSE at 08:00
Completed NSE at 08:00, 13.97s elapsed
Initiating NSE at 08:00
Completed NSE at 08:01, 3.01s elapsed
Initiating NSE at 08:01
Completed NSE at 08:01, 0.00s elapsed
Nmap scan report for 10.129.220.85
Host is up (0.28s latency).
Not shown: 97 closed tcp ports (reset)
PORT    STATE    SERVICE  VERSION
22/tcp  open     ssh      OpenSSH 9.6p1 Ubuntu 3ubuntu13.16 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   256 27:c3:7d:10:17:3b:dc:29:cf:05:83:33:ab:28:d0:38 (ECDSA)
|_  256 a3:46:f2:d7:1f:43:41:31:35:a2:88:31:ff:2a:0b:22 (ED25519)
80/tcp  filtered http
443/tcp open     ssl/http Apache httpd 2.4.58 ((Ubuntu))
| tls-alpn: 
|_  http/1.1
|_http-title: Agency LLC
|_http-generator: WordPress 7.0
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: Apache/2.4.58 (Ubuntu)
|_http-favicon: Unknown favicon MD5: C695E13D43A29AE824EBC6BAE9C1F8FA
| ssl-cert: Subject: commonName=makesense.htb
| Issuer: commonName=makesense.htb
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2026-05-29T16:37:29
| Not valid after:  2126-05-05T16:37:29
| MD5:     137e 40f1 46c6 4920 684e 34dc 3a8e 8887
| SHA-1:   a53c 8772 c319 515b 0b1d 42eb 2327 a5f7 1115 2a61
|_SHA-256: 59e3 04ab 3225 c2f6 3984 c784 ad89 508d 0baf 8b57 357b 0b2e d597 21d9 5a5b ead5
|_http-trane-info: Problem with XML parsing of /evox/about
|_ssl-date: TLS randomness does not represent time
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

NSE: Script Post-scanning.
Initiating NSE at 08:01
Completed NSE at 08:01, 0.00s elapsed
Initiating NSE at 08:01
Completed NSE at 08:01, 0.00s elapsed
Initiating NSE at 08:01
Completed NSE at 08:01, 0.00s elapsed
Read data files from: /usr/share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 36.59 seconds
           Raw packets sent: 118 (5.168KB) | Rcvd: 112 (4.476KB)
                                                                         
```

discovered ports 22,443,80.

add makesense.htb and ip to the /etc/hosts file and visit https://<ip>/

```
└─$ ffuf -w /home/walkerffx/SecLists/Discovery/Web-Content/common.txt:FUZZ -u https://makesense.htb/FUZZ -fs 0

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : https://makesense.htb/FUZZ
 :: Wordlist         : FUZZ: /home/walkerffx/SecLists/Discovery/Web-Content/common.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
 :: Filter           : Response size: 0
________________________________________________

.htaccess               [Status: 403, Size: 279, Words: 20, Lines: 10, Duration: 269ms]
.hta                    [Status: 403, Size: 279, Words: 20, Lines: 10, Duration: 274ms]
.gitignore              [Status: 200, Size: 1055, Words: 49, Lines: 90, Duration: 270ms]
.git/logs/              [Status: 200, Size: 34914, Words: 5289, Lines: 349, Duration: 483ms]
.htpasswd               [Status: 403, Size: 279, Words: 20, Lines: 10, Duration: 266ms]
cgi-bin/                [Status: 200, Size: 34914, Words: 5289, Lines: 349, Duration: 1655ms]
javascript              [Status: 301, Size: 321, Words: 20, Lines: 10, Duration: 1916ms]
scripts                 [Status: 301, Size: 318, Words: 20, Lines: 10, Duration: 813ms]
server-status           [Status: 403, Size: 279, Words: 20, Lines: 10, Duration: 528ms]
wp-admin                [Status: 301, Size: 319, Words: 20, Lines: 10, Duration: 508ms]
wp-includes             [Status: 301, Size: 322, Words: 20, Lines: 10, Duration: 288ms]
wp-content              [Status: 301, Size: 321, Words: 20, Lines: 10, Duration: 530ms]
xmlrpc.php              [Status: 405, Size: 42, Words: 6, Lines: 1, Duration: 2651ms]
:: Progress: [4744/4744] :: Job [1/1] :: 32 req/sec :: Duration: [0:02:42] :: Errors: 0 ::
```

end points found in the sourcecode.

https://makesense.htb/wp-content/themes/webagency/
https://makesense.htb/wp-admin/admin-ajax.php

and from https://10.129.220.85/wp-content/themes/webagency/assets/js/whisper/whisper-wrapper.js we found https://makesense.htb//wp-content/ai-models/models/

https://makesense.htb/wp-content/themes/webagency/assets/js/main.js

ENCRYPTION_KEY = 'bLs6z8iv3gWpsvyeabFosDjb4YQe7jdU13rI';



https://makesense.htb/wp-login.php
https://makesense.htb/wp-admin/
https://makesense.htb/wp-content/uploads/

```
└─$ wpscan --url https://makesense.htb --disable-tls-checks

_______________________________________________________________
         __          _______   _____
         \ \        / /  __ \ / ____|
          \ \  /\  / /| |__) | (___   ___  __ _ _ __ ®
           \ \/  \/ / |  ___/ \___ \ / __|/ _` | '_ \
            \  /\  /  | |     ____) | (__| (_| | | | |
             \/  \/   |_|    |_____/ \___|\__,_|_| |_|

         WordPress Security Scanner by the WPScan Team
                         Version 3.8.28
       Sponsored by Automattic - https://automattic.com/
       @_WPScan_, @ethicalhack3r, @erwan_lr, @firefart
_______________________________________________________________

[i] It seems like you have not updated the database for some time.
 
[+] URL: https://makesense.htb/ [10.129.220.85]
[+] Started: Sun Jul  5 09:06:11 2026

Interesting Finding(s):

[+] Headers
 | Interesting Entry: Server: Apache/2.4.58 (Ubuntu)
 | Found By: Headers (Passive Detection)
 | Confidence: 100%

[+] XML-RPC seems to be enabled: https://makesense.htb/xmlrpc.php
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%
 | References:
 |  - http://codex.wordpress.org/XML-RPC_Pingback_API
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_ghost_scanner/
 |  - https://www.rapid7.com/db/modules/auxiliary/dos/http/wordpress_xmlrpc_dos/
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_xmlrpc_login/
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_pingback_access/

[+] WordPress readme found: https://makesense.htb/readme.html
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%

[+] Upload directory has listing enabled: https://makesense.htb/wp-content/uploads/
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%

[+] The external WP-Cron seems to be enabled: https://makesense.htb/wp-cron.php
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 60%
 | References:
 |  - https://www.iplocation.net/defend-wordpress-from-ddos
 |  - https://github.com/wpscanteam/wpscan/issues/1299

Fingerprinting the version - Time: 00:03:07 <===============> (702 / 702) 100.00% Time: 00:03:07
[i] The WordPress version could not be detected.

[+] WordPress theme in use: webagency
 | Location: https://makesense.htb/wp-content/themes/webagency/
 | Style URL: https://makesense.htb/wp-content/themes/webagency/style.css?ver=7.0
 | Style Name: WebAgency
 | Style URI: https://example.com
 | Description: Modern web development agency theme with Tailwind CSS...
 | Author: WebAgency Team
 | Author URI: https://example.com
 |
 | Found By: Css Style In Homepage (Passive Detection)
 | Confirmed By: Css Style In 404 Page (Passive Detection)
 |
 | Version: 1.0 (80% confidence)
 | Found By: Style (Passive Detection)
 |  - https://makesense.htb/wp-content/themes/webagency/style.css?ver=7.0, Match: 'Version: 1.0'

[+] Enumerating All Plugins (via Passive Methods)

[i] No plugins Found.

[+] Enumerating Config Backups (via Passive and Aggressive Methods)
 Checking Config Backups - Time: 00:00:09 <=================> (137 / 137) 100.00% Time: 00:00:09

[i] No Config Backups Found.

[!] No WPScan API Token given, as a result vulnerability data has not been output.
[!] You can get a free API token with 25 daily requests by registering at https://wpscan.com/register

[+] Finished: Sun Jul  5 09:09:48 2026
[+] Requests Done: 1444
[+] Cached Requests: 8
[+] Data Sent: 391.079 KB
[+] Data Received: 35.636 MB
[+] Memory used: 348.176 MB
[+] Elapsed time: 00:03:36
                                                                                   
```


https://makesense.htb/xmlrpc.php
XML-RPC server accepts POST requests only.


https://makesense.htb/wp-content/uploads/2026/01/voice-message.wav
Hey this is Jake, I'm testing the new feature and it's exciting, I'm going there, 
Oops, login, hum, Jake, clear, light, Nice, smooth, 4, 9, 2, 3


I'm testing the new feature and its exciting. 

I'm going there. 

Oops, Jake. 

Clear light eyes smooth for nine two three.