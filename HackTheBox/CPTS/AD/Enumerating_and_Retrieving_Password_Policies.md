```
crackmapexec smb 172.16.5.5 -u wley -p transporter@4 --pass-pol
SMB         172.16.5.5      445    ACADEMY-EA-DC01  [*] Windows 10.0 Build 17763 x64 (name:ACADEMY-EA-DC01) (domain:INLANEFREIGHT.LOCAL) (signing:True) (SMBv1:False)
SMB         172.16.5.5      445    ACADEMY-EA-DC01  [+] INLANEFREIGHT.LOCAL\wley:transporter@4 
SMB         172.16.5.5      445    ACADEMY-EA-DC01  [+] Dumping password info for domain: INLANEFREIGHT
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Minimum password length: 8
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Password history length: 24
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Maximum password age: Not Set
SMB         172.16.5.5      445    ACADEMY-EA-DC01  
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Password Complexity Flags: 000001
SMB         172.16.5.5      445    ACADEMY-EA-DC01      Domain Refuse Password Change: 0
SMB         172.16.5.5      445    ACADEMY-EA-DC01      Domain Password Store Cleartext: 0
SMB         172.16.5.5      445    ACADEMY-EA-DC01      Domain Password Lockout Admins: 0
SMB         172.16.5.5      445    ACADEMY-EA-DC01      Domain Password No Clear Change: 0
SMB         172.16.5.5      445    ACADEMY-EA-DC01      Domain Password No Anon Change: 0
SMB         172.16.5.5      445    ACADEMY-EA-DC01      Domain Password Complex: 1
SMB         172.16.5.5      445    ACADEMY-EA-DC01  
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Minimum password age: 1 day 4 minutes 
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Reset Account Lockout Counter: 30 minutes 
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Locked Account Duration: 30 minutes 
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Account Lockout Threshold: 5
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Forced Log off Time: Not Set
┌─[htb-student@ea-attack01]─[~]
└──╼ $rpcclient -U "" -N 172.16.5.5                                                             
rpcclient $> querydomaininfo
command not found: querydomaininfo
rpcclient $> querydominfo
Domain:         INLANEFREIGHT
Server:
Comment:
Total Users:    3509
Total Groups:   0
Total Aliases:  203
Sequence No:    1
Force Logoff:   -1
Domain Server State:    0x1
Server Role:    ROLE_DOMAIN_PDC
Unknown 3:      0x1
rpcclient $> 

```

