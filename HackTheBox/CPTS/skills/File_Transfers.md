**Windows File Transfer Methods

Q1. Download the file flag.txt from the web root using wget from the Pwnbox. Submit the contents of the file as your answer.
```
 curl http://10.129.146.230/flag.txt 
b1a4ca918282fcd96004565521944a3b                                                                                                

```

Q2. Upload the attached file named upload_win.zip to the target using the method of your choice. Once uploaded, unzip the archive, and run "hasher upload_win.txt" from the command line. Submit the generated hash as your answer.

```
PS C:\Users\htb-student> Invoke-WebRequest -Uri "http://10.10.15.219:8000/upload_win.txt" -OutFile ".\upload.txt"
PS C:\Users\htb-student> ls


    Directory: C:\Users\htb-student


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
d-r---         9/9/2020   1:55 PM                Contacts
d-r---         9/9/2020   1:56 PM                Desktop
d-r---         9/9/2020   1:55 PM                Documents
d-r---         9/9/2020   1:55 PM                Downloads
d-r---         9/9/2020   1:55 PM                Favorites
d-r---         9/9/2020   1:55 PM                Links
d-r---         9/9/2020   1:55 PM                Music
d-r---         9/9/2020   1:55 PM                Pictures
d-r---         9/9/2020   1:55 PM                Saved Games
d-r---         9/9/2020   1:55 PM                Searches
d-r---         9/9/2020   1:55 PM                Videos
-a----         9/3/2026   8:49 PM             32 upload.txt


PS C:\Users\htb-student> hasher .\upload.txt
f458303ea783c224c6b4e7ef7f17eb9d
PS C:\Users\htb-student>



```

**Linux File Transfer Methods

Q1.Download the file flag.txt from the web root using Python from the Pwnbox. Submit the contents of the file as your answer.

```
wget 10.129.146.249/flag.txt
Prepended http:// to '10.129.146.249/flag.txt'
--2026-09-04 10:11:30--  http://10.129.146.249/flag.txt
Connecting to 10.129.146.249:80... connected.
HTTP request sent, awaiting response... 200 OK
Length: 33 [text/plain]
Saving to: ‘flag.txt’

flag.txt                100%[===============================>]      33  --.-KB/s    in 0s      

2026-09-04 10:11:31 (2.29 MB/s) - ‘flag.txt’ saved [33/33]


```

Q2. Upload the attached file named upload_nix.zip to the target using the method of your choice. Once uploaded, SSH to the box, extract the file, and run "hasher < extracted file>" from the command line. Submit the generated hash as your answer.

```
scp upload_nix.txt htb-student@10.129.146.249:/home/htb-student/

The authenticity of host '10.129.146.249 (10.129.146.249)' can't be established.
ED25519 key fingerprint is: SHA256:z4rcb3qcf0IdRnoTBNEJ4i8TlDystDA4uOJFxVcb41E
This host key is known by the following other names/addresses:
    ~/.ssh/known_hosts:48: [hashed name]
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '10.129.146.249' (ED25519) to the list of known hosts.
** WARNING: connection is not using a post-quantum key exchange algorithm.
** This session may be vulnerable to "store now, decrypt later" attacks.
** The server may need to be upgraded. See https://openssh.com/pq.html
htb-student@10.129.146.249's password: 
upload_nix.txt                                                100%   32     0.1KB/s   00:00    
                                                                                              
```

```
htb-student@nix04:~$ hasher upload_nix.txt
159cfe5c65054bbadb2761cfa359c8b0
htb-student@nix04:~$ 

```

