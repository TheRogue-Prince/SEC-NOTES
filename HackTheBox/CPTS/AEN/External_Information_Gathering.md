We start with a quick initial Nmap scan against our target to get a lay of the land and see what we're dealing with. We ensure to save all scan output to the relevant subdirectory in our project directory.

```
sudo nmap --open -oA inlanefreight_ept_tcp_1k -iL scope
Starting Nmap 7.99 ( https://nmap.org ) at 2026-07-19 08:10 +0530
Nmap scan report for inlanefreight.local (10.129.229.147)
Host is up (0.31s latency).
Not shown: 989 closed tcp ports (reset)
PORT     STATE SERVICE
21/tcp   open  ftp
22/tcp   open  ssh
25/tcp   open  smtp
53/tcp   open  domain
80/tcp   open  http
110/tcp  open  pop3
111/tcp  open  rpcbind
143/tcp  open  imap
993/tcp  open  imaps
995/tcp  open  pop3s
8080/tcp open  http-proxy

Nmap done: 1 IP address (1 host up) scanned in 8.91 seconds

```

we also tried an aggressive scan to get more info about the os and services.

```
sudo nmap --open -p- -A -oA inlanefreight_ept_tcp_all_svc -iL scope
Starting Nmap 7.99 ( https://nmap.org ) at 2026-07-19 08:13 +0530
Nmap scan report for inlanefreight.local (10.129.229.147)
Host is up (0.31s latency).
Not shown: 64735 closed tcp ports (reset), 789 filtered tcp ports (no-response)
Some closed ports may be reported as filtered due to --defeat-rst-ratelimit
PORT     STATE SERVICE  VERSION
21/tcp   open  ftp      vsftpd 3.0.3
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to ::ffff:10.10.15.187
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 2
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_-rw-r--r--    1 0        0              38 May 30  2022 flag.txt
22/tcp   open  ssh      OpenSSH 8.2p1 Ubuntu 4ubuntu0.5 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 71:08:b0:c4:f3:ca:97:57:64:97:70:f9:fe:c5:0c:7b (RSA)
|   256 45:c3:b5:14:63:99:3d:9e:b3:22:51:e5:97:76:e1:50 (ECDSA)
|_  256 2e:c2:41:66:46:ef:b6:81:95:d5:aa:35:23:94:55:38 (ED25519)
25/tcp   open  smtp     Postfix smtpd
|_smtp-commands: ubuntu, PIPELINING, SIZE 10240000, VRFY, ETRN, STARTTLS, ENHANCEDSTATUSCODES, 8BITMIME, DSN, SMTPUTF8, CHUNKING
53/tcp   open  domain   (unknown banner: 1337_HTB_DNS)
| dns-nsid: 
|_  bind.version: 1337_HTB_DNS
| fingerprint-strings: 
|   DNSVersionBindReqTCP: 
|     version
|     bind
|_    1337_HTB_DNS
80/tcp   open  http     Apache httpd 2.4.41 ((Ubuntu))
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-title: Inlanefreight
110/tcp  open  pop3     Dovecot pop3d
|_ssl-date: TLS randomness does not represent time
| ssl-cert: Subject: commonName=ubuntu
| Subject Alternative Name: DNS:ubuntu
| Not valid before: 2022-05-30T17:15:40
|_Not valid after:  2032-05-27T17:15:40
|_pop3-capabilities: SASL STLS UIDL CAPA PIPELINING TOP RESP-CODES AUTH-RESP-CODE
111/tcp  open  rpcbind  2-4 (RPC #100000)
| rpcinfo: 
|   program version    port/proto  service
|   100000  2,3,4        111/tcp   rpcbind
|   100000  2,3,4        111/udp   rpcbind
|   100000  3,4          111/tcp6  rpcbind
|_  100000  3,4          111/udp6  rpcbind
143/tcp  open  imap     Dovecot imapd (Ubuntu)
|_ssl-date: TLS randomness does not represent time
| ssl-cert: Subject: commonName=ubuntu
| Subject Alternative Name: DNS:ubuntu
| Not valid before: 2022-05-30T17:15:40
|_Not valid after:  2032-05-27T17:15:40
|_imap-capabilities: more Pre-login LITERAL+ have LOGIN-REFERRALS STARTTLS ID OK IMAP4rev1 post-login capabilities LOGINDISABLEDA0001 listed SASL-IR ENABLE IDLE
993/tcp  open  ssl/imap Dovecot imapd (Ubuntu)
|_imap-capabilities: AUTH=PLAINA0001 Pre-login LITERAL+ LOGIN-REFERRALS post-login ID OK IMAP4rev1 more capabilities have listed SASL-IR IDLE ENABLE
| ssl-cert: Subject: commonName=ubuntu
| Subject Alternative Name: DNS:ubuntu
| Not valid before: 2022-05-30T17:15:40
|_Not valid after:  2032-05-27T17:15:40
|_ssl-date: TLS randomness does not represent time
995/tcp  open  ssl/pop3 Dovecot pop3d
|_pop3-capabilities: SASL(PLAIN) USER UIDL CAPA PIPELINING TOP RESP-CODES AUTH-RESP-CODE
|_ssl-date: TLS randomness does not represent time
| ssl-cert: Subject: commonName=ubuntu
| Subject Alternative Name: DNS:ubuntu
| Not valid before: 2022-05-30T17:15:40
|_Not valid after:  2032-05-27T17:15:40
8080/tcp open  http     Apache httpd 2.4.41 ((Ubuntu))
|_http-server-header: Apache/2.4.41 (Ubuntu)
| http-open-proxy: Potentially OPEN proxy.
|_Methods supported:CONNECTION
|_http-title: Support Center
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port53-TCP:V=7.99%I=7%D=7/19%Time=6A5C3A31%P=x86_64-pc-linux-gnu%r(DNSV
SF:ersionBindReqTCP,39,"\x007\0\x06\x85\0\0\x01\0\x01\0\0\0\0\x07version\x
SF:04bind\0\0\x10\0\x03\xc0\x0c\0\x10\0\x03\0\0\0\0\0\r\x0c1337_HTB_DNS");
Device type: general purpose|router
Running: Linux 4.X|5.X, MikroTik RouterOS 7.X
OS CPE: cpe:/o:linux:linux_kernel:4 cpe:/o:linux:linux_kernel:5 cpe:/o:mikrotik:routeros:7 cpe:/o:linux:linux_kernel:5.6.3
OS details: Linux 4.15 - 5.19, MikroTik RouterOS 7.2 - 7.5 (Linux 5.6.3)
Network Distance: 2 hops
Service Info: Host:  ubuntu; OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE (using port 8080/tcp)
HOP RTT       ADDRESS
1   310.30 ms 10.10.14.1
2   311.10 ms inlanefreight.local (10.129.229.147)

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 172.44 seconds

```
Banner grabbing.

```
sudo nmap -sV --script=banner --open 10.129.229.147
Starting Nmap 7.99 ( https://nmap.org ) at 2026-07-19 08:40 +0530
Nmap scan report for inlanefreight.local (10.129.229.147)
Host is up (0.49s latency).
Not shown: 989 closed tcp ports (reset)
PORT     STATE SERVICE  VERSION
21/tcp   open  ftp      vsftpd 3.0.3
|_banner: 220 (vsFTPd 3.0.3)
22/tcp   open  ssh      OpenSSH 8.2p1 Ubuntu 4ubuntu0.5 (Ubuntu Linux; protocol 2.0)
|_banner: SSH-2.0-OpenSSH_8.2p1 Ubuntu-4ubuntu0.5
25/tcp   open  smtp     Postfix smtpd
|_banner: 220 ubuntu ESMTP Postfix (Ubuntu)
53/tcp   open  domain   (unknown banner: 1337_HTB_DNS)
| fingerprint-strings: 
|   DNSVersionBindReqTCP: 
|     version
|     bind
|_    1337_HTB_DNS
80/tcp   open  http     Apache httpd 2.4.41 ((Ubuntu))
|_http-server-header: Apache/2.4.41 (Ubuntu)
110/tcp  open  pop3     Dovecot pop3d
|_banner: +OK Dovecot (Ubuntu) ready.
111/tcp  open  rpcbind  2-4 (RPC #100000)
| rpcinfo: 
|   program version    port/proto  service
|   100000  2,3,4        111/tcp   rpcbind
|   100000  2,3,4        111/udp   rpcbind
|   100000  3,4          111/tcp6  rpcbind
|_  100000  3,4          111/udp6  rpcbind
143/tcp  open  imap     Dovecot imapd (Ubuntu)
| banner: * OK [CAPABILITY IMAP4rev1 SASL-IR LOGIN-REFERRALS ID ENABLE ID
|_LE LITERAL+ STARTTLS LOGINDISABLED] Dovecot (Ubuntu) ready.
993/tcp  open  ssl/imap Dovecot imapd (Ubuntu)
| banner: * OK [CAPABILITY IMAP4rev1 SASL-IR LOGIN-REFERRALS ID ENABLE ID
|_LE LITERAL+ AUTH=PLAIN] Dovecot (Ubuntu) ready.
995/tcp  open  ssl/pop3 Dovecot pop3d
|_banner: +OK Dovecot (Ubuntu) ready.
8080/tcp open  http     Apache httpd 2.4.41 ((Ubuntu))
|_http-server-header: Apache/2.4.41 (Ubuntu)
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port53-TCP:V=7.99%I=7%D=7/19%Time=6A5C4041%P=x86_64-pc-linux-gnu%r(DNSV
SF:ersionBindReqTCP,39,"\x007\0\x06\x85\0\0\x01\0\x01\0\0\0\0\x07version\x
SF:04bind\0\0\x10\0\x03\xc0\x0c\0\x10\0\x03\0\0\0\0\0\r\x0c1337_HTB_DNS");
Service Info: Host:  ubuntu; OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 38.53 seconds

```
we did a dnszonetransfer and we got some good results.

```
dig axfr inlanefreight.local @10.129.229.147

; <<>> DiG 9.20.24-1+b1-Debian <<>> axfr inlanefreight.local @10.129.229.147
;; global options: +cmd
inlanefreight.local.    86400   IN      SOA     ns1.inlanfreight.local. dnsadmin.inlanefreight.local. 21 604800 86400 2419200 86400
inlanefreight.local.    86400   IN      NS      inlanefreight.local.
inlanefreight.local.    86400   IN      A       127.0.0.1
blog.inlanefreight.local. 86400 IN      A       127.0.0.1
careers.inlanefreight.local. 86400 IN   A       127.0.0.1
dev.inlanefreight.local. 86400  IN      A       127.0.0.1
flag.inlanefreight.local. 86400 IN      TXT     "HTB{DNs_ZOn3_Tr@nsf3r}"
gitlab.inlanefreight.local. 86400 IN    A       127.0.0.1
ir.inlanefreight.local. 86400   IN      A       127.0.0.1
status.inlanefreight.local. 86400 IN    A       127.0.0.1
support.inlanefreight.local. 86400 IN   A       127.0.0.1
tracking.inlanefreight.local. 86400 IN  A       127.0.0.1
vpn.inlanefreight.local. 86400  IN      A       127.0.0.1
inlanefreight.local.    86400   IN      SOA     ns1.inlanfreight.local. dnsadmin.inlanefreight.local. 21 604800 86400 2419200 86400
;; Query time: 300 msec
;; SERVER: 10.129.229.147#53(10.129.229.147) (TCP)
;; WHEN: Sun Jul 19 08:25:36 IST 2026
;; XFR size: 14 records (messages 1, bytes 448)

```

findings.
```
ffuf -w /home/satoru/SecLists/Discovery/DNS/namelist.txt:FUZZ -u http://10.129.229.147/ -H 'Host:FUZZ.inlanefreight.local' -fs 15157

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://10.129.229.147/
 :: Wordlist         : FUZZ: /home/satoru/SecLists/Discovery/DNS/namelist.txt
 :: Header           : Host: FUZZ.inlanefreight.local
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
 :: Filter           : Response size: 15157
________________________________________________

blog                    [Status: 200, Size: 8708, Words: 1509, Lines: 232, Duration: 795ms]
careers                 [Status: 200, Size: 51806, Words: 22041, Lines: 732, Duration: 335ms]
dev                     [Status: 200, Size: 2048, Words: 643, Lines: 74, Duration: 332ms]
gitlab                  [Status: 302, Size: 113, Words: 5, Lines: 1, Duration: 365ms]
ir                      [Status: 200, Size: 28548, Words: 2885, Lines: 210, Duration: 1509ms]
monitoring              [Status: 200, Size: 56, Words: 3, Lines: 4, Duration: 312ms]
status                  [Status: 200, Size: 878, Words: 105, Lines: 43, Duration: 326ms]
support                 [Status: 200, Size: 26635, Words: 11730, Lines: 523, Duration: 313ms]
tracking                [Status: 200, Size: 35211, Words: 10413, Lines: 791, Duration: 354ms]
vpn                     [Status: 200, Size: 1578, Words: 414, Lines: 35, Duration: 336ms]
:: Progress: [151265/151265] :: Job [1/1] :: 131 req/sec :: Duration: [0:20:51] :: Errors: 0 ::

```

```
blog.inlanefreight.local

careers.inlanefreight.local

dev.inlanefreight.local

flag.inlanefreight.local

gitlab.inlanefreight.local

ir.inlanefreight.local

status.inlanefreight.local

support.inlanefreight.local

tracking.inlanefreight.local

vpn.inlanefreight.local

monitoring.inlanefreight.local
```

