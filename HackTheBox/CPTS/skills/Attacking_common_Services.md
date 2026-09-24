**Attacking Common Services - Easy

We were commissioned by the company Inlanefreight to conduct a penetration test against three different hosts to check the servers' configuration and security. We were informed that a flag had been placed somewhere on each server to prove successful access. These flags have the following format:

HTB{...}
Our task is to review the security of each of the three servers and present it to the customer. According to our information, the first server is a server that manages emails, customers, and their files.

Q1. You are targeting the inlanefreight.htb domain. Assess the target server and obtain the contents of the flag.txt file. Submit it as the answer.

```
sudo nmap -sCV 10.129.159.146 -oA nmap
[sudo] password for satoru: 
Starting Nmap 7.99 ( https://nmap.org ) at 2026-09-11 08:47 +0530
Nmap scan report for 10.129.159.146
Host is up (0.41s latency).
Not shown: 993 filtered tcp ports (no-response)
PORT     STATE SERVICE       VERSION
21/tcp   open  ftp
|_ssl-date: 2026-09-11T03:20:45+00:00; +11s from scanner time.
| ssl-cert: Subject: commonName=Test/organizationName=Testing/stateOrProvinceName=FL/countryName=US
| Not valid before: 2022-04-21T19:27:17
|_Not valid after:  2032-04-18T19:27:17
| fingerprint-strings: 
|   GenericLines: 
|     220 Core FTP Server Version 2.0, build 725, 64-bit Unregistered
|     Command unknown, not supported or not allowed...
|     Command unknown, not supported or not allowed...
|   NULL: 
|_    220 Core FTP Server Version 2.0, build 725, 64-bit Unregistered
25/tcp   open  smtp          hMailServer smtpd
| smtp-commands: WIN-EASY, SIZE 20480000, AUTH LOGIN PLAIN, HELP
|_ 211 DATA HELO EHLO MAIL NOOP QUIT RCPT RSET SAML TURN VRFY
80/tcp   open  http          Apache httpd 2.4.53 ((Win64) OpenSSL/1.1.1n PHP/7.4.29)
|_http-server-header: Apache/2.4.53 (Win64) OpenSSL/1.1.1n PHP/7.4.29
| http-title: Welcome to XAMPP
|_Requested resource was http://10.129.159.146/dashboard/
443/tcp  open  ssl/https     Core FTP HTTPS Server
|_ssl-date: 2026-09-11T03:20:43+00:00; +10s from scanner time.
| ssl-cert: Subject: commonName=Test/organizationName=Testing/stateOrProvinceName=FL/countryName=US
| Not valid before: 2022-04-21T19:27:17
|_Not valid after:  2032-04-18T19:27:17
| fingerprint-strings: 
|   FourOhFourRequest: 
|     HTTP/1.1 401 Unauthorized
|     Date:Fri, 11 Aug 2026 03:17:58 GMT
|     Server: Core FTP HTTPS Server
|     Connection: close
|     WWW-Authenticate: Basic realm="Restricted Area"
|     Content-Type: text/html
|     Content-length: 61
|     <BODY>
|     <HTML>
|     HTTP/1.1 401 Unauthorized
|     </BODY>
|     </HTML>
|   GenericLines, HTTPOptions, Help, Kerberos, LDAPSearchReq, LPDString, RTSPRequest, SIPOptions, SSLSessionReq, TLSSessionReq, TerminalServerCookie: 
|     Command Not Recognized
|   GetRequest: 
|     HTTP/1.1 401 Unauthorized
|     Date:Fri, 11 Aug 2026 03:17:54 GMT
|     Server: Core FTP HTTPS Server
|     Connection: close
|     WWW-Authenticate: Basic realm="Restricted Area"
|     Content-Type: text/html
|     Content-length: 61
|     <BODY>
|     <HTML>
|     HTTP/1.1 401 Unauthorized
|     </BODY>
|_    </HTML>
|_http-server-header: Core FTP HTTPS Server
587/tcp  open  smtp          hMailServer smtpd
| smtp-commands: WIN-EASY, SIZE 20480000, AUTH LOGIN PLAIN, HELP
|_ 211 DATA HELO EHLO MAIL NOOP QUIT RCPT RSET SAML TURN VRFY
3306/tcp open  mysql         MariaDB 5.5.5-10.4.24
| mysql-info: 
|   Protocol: 10
|   Version: 5.5.5-10.4.24-MariaDB
|   Thread ID: 10
|   Capabilities flags: 63486
|   Some Capabilities: Speaks41ProtocolNew, ODBCClient, SupportsLoadDataLocal, ConnectWithDatabase, InteractiveClient, SupportsCompression, SupportsTransactions, DontAllowDatabaseTableColumn, Speaks41ProtocolOld, LongColumnFlag, IgnoreSigpipes, IgnoreSpaceBeforeParenthesis, Support41Auth, FoundRows, SupportsAuthPlugins, SupportsMultipleStatments, SupportsMultipleResults
|   Status: Autocommit
|   Salt: d4wz~.e6x}.f9(\wbdQH
|_  Auth Plugin Name: mysql_native_password
3389/tcp open  ms-wbt-server Microsoft Terminal Services
| ssl-cert: Subject: commonName=WIN-EASY
| Not valid before: 2026-09-10T03:03:45
|_Not valid after:  2027-03-12T03:03:45
| rdp-ntlm-info: 
|   Target_Name: WIN-EASY
|   NetBIOS_Domain_Name: WIN-EASY
|   NetBIOS_Computer_Name: WIN-EASY
|   DNS_Domain_Name: WIN-EASY
|   DNS_Computer_Name: WIN-EASY
|   Product_Version: 10.0.17763
|_  System_Time: 2026-09-11T03:20:06+00:00
|_ssl-date: 2026-09-11T03:20:43+00:00; +11s from scanner time.
2 services unrecognized despite returning data. If you know the service/version, please submit the following fingerprints at https://nmap.org/cgi-bin/submit.cgi?new-service :
==============NEXT SERVICE FINGERPRINT (SUBMIT INDIVIDUALLY)==============
SF-Port21-TCP:V=7.99%I=7%D=9/11%Time=6AA372CE%P=x86_64-pc-linux-gnu%r(NULL
SF:,41,"220\x20Core\x20FTP\x20Server\x20Version\x202\.0,\x20build\x20725,\
SF:x2064-bit\x20Unregistered\r\n")%r(GenericLines,AD,"220\x20Core\x20FTP\x
SF:20Server\x20Version\x202\.0,\x20build\x20725,\x2064-bit\x20Unregistered
SF:\r\n502\x20Command\x20unknown,\x20not\x20supported\x20or\x20not\x20allo
SF:wed\.\.\.\r\n502\x20Command\x20unknown,\x20not\x20supported\x20or\x20no
SF:t\x20allowed\.\.\.\r\n");
==============NEXT SERVICE FINGERPRINT (SUBMIT INDIVIDUALLY)==============
SF-Port443-TCP:V=7.99%T=SSL%I=7%D=9/11%Time=6AA372D8%P=x86_64-pc-linux-gnu
SF:%r(GetRequest,110,"HTTP/1\.1\x20401\x20Unauthorized\r\nDate:Fri,\x2011\
SF:x20Aug\x202026\x2003:17:54\x20GMT\r\nServer:\x20Core\x20FTP\x20HTTPS\x2
SF:0Server\r\nConnection:\x20close\r\nWWW-Authenticate:\x20Basic\x20realm=
SF:\"Restricted\x20Area\"\r\nContent-Type:\x20text/html\r\nContent-length:
SF:\x2061\r\n\r\n<BODY>\r\n<HTML>\r\nHTTP/1\.1\x20401\x20Unauthorized\r\n<
SF:/BODY>\r\n</HTML>\r\n\r\n")%r(HTTPOptions,1A,"Command\x20Not\x20Recogni
SF:zed\r\n\r\n")%r(FourOhFourRequest,110,"HTTP/1\.1\x20401\x20Unauthorized
SF:\r\nDate:Fri,\x2011\x20Aug\x202026\x2003:17:58\x20GMT\r\nServer:\x20Cor
SF:e\x20FTP\x20HTTPS\x20Server\r\nConnection:\x20close\r\nWWW-Authenticate
SF::\x20Basic\x20realm=\"Restricted\x20Area\"\r\nContent-Type:\x20text/htm
SF:l\r\nContent-length:\x2061\r\n\r\n<BODY>\r\n<HTML>\r\nHTTP/1\.1\x20401\
SF:x20Unauthorized\r\n</BODY>\r\n</HTML>\r\n\r\n")%r(GenericLines,1A,"Comm
SF:and\x20Not\x20Recognized\r\n\r\n")%r(RTSPRequest,1A,"Command\x20Not\x20
SF:Recognized\r\n\r\n")%r(Help,1A,"Command\x20Not\x20Recognized\r\n\r\n")%
SF:r(SSLSessionReq,1A,"Command\x20Not\x20Recognized\r\n\r\n")%r(TerminalSe
SF:rverCookie,1A,"Command\x20Not\x20Recognized\r\n\r\n")%r(TLSSessionReq,1
SF:A,"Command\x20Not\x20Recognized\r\n\r\n")%r(Kerberos,1A,"Command\x20Not
SF:\x20Recognized\r\n\r\n")%r(LPDString,1A,"Command\x20Not\x20Recognized\r
SF:\n\r\n")%r(LDAPSearchReq,1A,"Command\x20Not\x20Recognized\r\n\r\n")%r(S
SF:IPOptions,1A,"Command\x20Not\x20Recognized\r\n\r\n");
Service Info: Host: WIN-EASY; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
|_clock-skew: mean: 10s, deviation: 0s, median: 10s

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 229.70 seconds

```

```
find the creds using smtp user enum, first find the user then spary the username to pass list, after getting creds login to ftp and also we can login to mariadb.

we have file writepriv, use it to write a webshell.php file in the root of xamp, and using the xamp web url access the flag. 
```

**Attacking Common Services - Medium

The second server is an internal server (within the inlanefreight.htb domain) that manages and stores emails and files and serves as a backup of some of the company's processes. From internal conversations, we heard that this is used relatively rarely and, in most cases, has only been used for testing purposes so far.

Q1. Assess the target server and find the flag.txt file. Submit the contents of this file as your answer.

```
run a full port scan and find the internal ftp and login using anonymous, get the notes and try bruteforce using hydra/nxc, login to ftp and get the flag

```

**Attacking Common Services - Hard


The third server is another internal server used to manage files and working material, such as forms. In addition, a database is used on the server, the purpose of which we do not know.. 

Q1. What file can you retrieve that belongs to the user "simon"? (Format: filename.txt)

```
sudo nmap -p 135,445,1433,3389 -sCV 10.129.203.10 
Starting Nmap 7.99 ( https://nmap.org ) at 2026-09-12 16:51 +0530
Nmap scan report for 10.129.203.10
Host is up (0.30s latency).

PORT     STATE SERVICE       VERSION
135/tcp  open  msrpc         Microsoft Windows RPC
445/tcp  open  microsoft-ds?
1433/tcp open  ms-sql-s      Microsoft SQL Server 2019 15.00.2000.00; RTM
|_ssl-date: 2026-09-12T11:23:04+00:00; +12s from scanner time.
| ms-sql-ntlm-info: 
|   10.129.203.10:1433: 
|     Target_Name: WIN-HARD
|     NetBIOS_Domain_Name: WIN-HARD
|     NetBIOS_Computer_Name: WIN-HARD
|     DNS_Domain_Name: WIN-HARD
|     DNS_Computer_Name: WIN-HARD
|_    Product_Version: 10.0.17763
| ms-sql-info: 
|   10.129.203.10:1433: 
|     Version: 
|       name: Microsoft SQL Server 2019 RTM
|       number: 15.00.2000.00
|       Product: Microsoft SQL Server 2019
|       Service pack level: RTM
|       Post-SP patches applied: false
|_    TCP port: 1433
| ssl-cert: Subject: commonName=SSL_Self_Signed_Fallback
| Not valid before: 2026-09-12T11:08:37
|_Not valid after:  2056-09-12T11:08:37
3389/tcp open  ms-wbt-server Microsoft Terminal Services
|_ssl-date: 2026-09-12T11:23:04+00:00; +13s from scanner time.
| ssl-cert: Subject: commonName=WIN-HARD
| Not valid before: 2026-09-11T11:08:24
|_Not valid after:  2027-03-13T11:08:24
| rdp-ntlm-info: 
|   Target_Name: WIN-HARD
|   NetBIOS_Domain_Name: WIN-HARD
|   NetBIOS_Computer_Name: WIN-HARD
|   DNS_Domain_Name: WIN-HARD
|   DNS_Computer_Name: WIN-HARD
|   Product_Version: 10.0.17763
|_  System_Time: 2026-09-12T11:22:24+00:00
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-time: 
|   date: 2026-09-12T11:22:25
|_  start_date: N/A
|_clock-skew: mean: 12s, deviation: 0s, median: 11s
| smb2-security-mode: 
|   3.1.1: 
|_    Message signing enabled but not required

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 67.23 seconds
                                                                                            
```

```

```