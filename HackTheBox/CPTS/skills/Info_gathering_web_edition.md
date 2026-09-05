
**Skills Assessment

Q1. What is the IANA ID of the registrar of the inlanefreight.com domain?
![](Attachments/Pasted%20image%2020260901103916.png)

Q2. What http server software is powering the inlanefreight.htb site on the target system? Respond with the name of the software, not the version, e.g., Apache.

```
whatweb 154.57.164.82:31043
http://154.57.164.82:31043 [200 OK] Country[UNITED STATES][US], HTML5, HTTPServer[nginx/1.26.1], IP[154.57.164.82], Title[inlanefreight], nginx[1.26.1]

```

Q3. What is the API key in the hidden admin directory that you have discovered on the target system?

```
gobuster vhost \
  -u http://154.57.164.73:30313/ \    
  -w /home/satoru/SecLists/Discovery/DNS/subdomains-top1million-110000.txt \
  --domain inlanefreight.htb \
  --append-domain \
  -t 30
===============================================================
Gobuster v3.8.2
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                       http://154.57.164.73:30313/
[+] Method:                    GET
[+] Threads:                   30
[+] Wordlist:                  /home/satoru/SecLists/Discovery/DNS/subdomains-top1million-110000.txt
[+] User Agent:                gobuster/3.8.2
[+] Timeout:                   10s
[+] Append Domain:             true
[+] Exclude Hostname Length:   false
===============================================================
Starting gobuster in VHOST enumeration mode
===============================================================
Progress: 1254 / 114442 (1.10%)[ERROR] error on word dream: timeout occurred during the request
[ERROR] error on word ldap2: timeout occurred during the request
[ERROR] error on word buy: timeout occurred during the request
[ERROR] error on word tfs: timeout occurred during the request
[ERROR] error on word sigma: timeout occurred during the request
[ERROR] error on word one: timeout occurred during the request
[ERROR] error on word a4: timeout occurred during the request
[ERROR] error on word merlin: timeout occurred during the request
[ERROR] error on word h: timeout occurred during the request
Progress: 1259 / 114442 (1.10%)[ERROR] error on word webcon: timeout occurred during the request
[ERROR] error on word homer: timeout occurred during the request
[ERROR] error on word widgets: timeout occurred during the request
[ERROR] error on word happy: timeout occurred during the request
[ERROR] error on word ls: timeout occurred during the request
#www.inlanefreight.htb Status: 400 [Size: 157]
#mail.inlanefreight.htb Status: 400 [Size: 157]
#smtp.inlanefreight.htb Status: 400 [Size: 157]
#pop3.inlanefreight.htb Status: 400 [Size: 157]
web1337.inlanefreight.htb Status: 200 [Size: 104]
Progress: 114442 / 114442 (100.00%)
===============================================================
Finished
===============================================================

```

![](Attachments/Pasted%20image%2020260901155213.png)
```

 curl -i http://web1337.inlanefreight.htb:30313/admin_h1dd3n/
HTTP/1.1 200 OK
Server: nginx/1.26.1
Date: Tue, 01 Sep 2026 10:41:39 GMT
Content-Type: text/html
Content-Length: 255
Last-Modified: Thu, 01 Aug 2024 09:35:23 GMT
Connection: keep-alive
ETag: "66ab56db-ff"
Accept-Ranges: bytes

<!DOCTYPE html><html><head><title>web1337 admin</title></head><body><h1>Welcome to web1337 admin site</h1><h2>The admin panel is currently under maintenance, but the API is still accessible with the key e963d863ee0e82ba7080fbf558ca0d3f</h2></body></html>
                                                                         
```

Q4. ### After crawling the inlanefreight.htb domain on the target system, what is the email address you have found? Respond with the full email, e.g., mail@inlanefreight.htb.

```
 gobuster vhost \
  -u http://web1337.inlanefreight.htb:30313 \
  -w /home/satoru/SecLists/Discovery/DNS/subdomains-top1million-110000.txt \
  --append-domain \
  -t 40
===============================================================
Gobuster v3.8.2
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                       http://web1337.inlanefreight.htb:30313
[+] Method:                    GET
[+] Threads:                   40
[+] Wordlist:                  /home/satoru/SecLists/Discovery/DNS/subdomains-top1million-110000.txt
[+] User Agent:                gobuster/3.8.2
[+] Timeout:                   10s
[+] Append Domain:             true
[+] Exclude Hostname Length:   false
===============================================================
Starting gobuster in VHOST enumeration mode
===============================================================
dev.web1337.inlanefreight.htb:30313 Status: 200 [Size: 123]
Progress: 1750 / 114442 (1.53%)^C

```

```
 python3 ReconSpider.py http://dev.web1337.inlanefreight.htb:30313/
2026-09-01 16:11:13 [scrapy.utils.log] INFO: Scrapy 2.17.0 started (bot: scrapybot)
2026-09-01 16:11:13 [scrapy.utils.log] INFO: Versions:
{'lxml': '6.1.0',
 'libxml2': '2.15.3',
 'cssselect': '1.5.0',
 'parsel': '1.11.0',
 'w3lib': '2.4.1',
 'Twisted': '26.4.0',
 'Python': '3.14.6 (main, Jun 10 2026, 18:54:31) [GCC 15.2.0]',
 'pyOpenSSL': '26.2.0 (OpenSSL 3.6.3 9 Jun 2026)',
 'cryptography': '47.0.0',
 'Platform': 'Linux-7.0.12+kali-amd64-x86_64-with-glibc2.42'}
2026-09-01 16:11:13 [scrapy.addons] INFO: Enabled addons:
[]
2026-09-01 16:11:13 [scrapy.extensions.telnet] INFO: Telnet Password: 7d387604a279aa12
2026-09-01 16:11:13 [scrapy.middleware] INFO: Enabled extensions:
['scrapy.extensions.corestats.CoreStats',
 'scrapy.extensions.logcount.LogCount',
 'scrapy.extensions.telnet.TelnetConsole',
 'scrapy.extensions.memusage.MemoryUsage',
 'scrapy.extensions.logstats.LogStats']
2026-09-01 16:11:13 [scrapy.crawler] INFO: Overridden settings:
{'LOG_LEVEL': 'INFO'}
2026-09-01 16:11:14 [scrapy.middleware] INFO: Enabled downloader middlewares:
['scrapy.downloadermiddlewares.offsite.OffsiteMiddleware',
 'scrapy.downloadermiddlewares.httpauth.HttpAuthMiddleware',
 'scrapy.downloadermiddlewares.downloadtimeout.DownloadTimeoutMiddleware',
 'scrapy.downloadermiddlewares.defaultheaders.DefaultHeadersMiddleware',
 'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware',
 '__main__.CustomOffsiteMiddleware',
 'scrapy.downloadermiddlewares.retry.RetryMiddleware',
 'scrapy.downloadermiddlewares.redirect.MetaRefreshMiddleware',
 'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware',
 'scrapy.downloadermiddlewares.redirect.RedirectMiddleware',
 'scrapy.downloadermiddlewares.cookies.CookiesMiddleware',
 'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware',
 'scrapy.downloadermiddlewares.stats.DownloaderStats']
2026-09-01 16:11:14 [scrapy.middleware] INFO: Enabled spider middlewares:
['scrapy.spidermiddlewares.start.StartSpiderMiddleware',
 'scrapy.spidermiddlewares.httperror.HttpErrorMiddleware',
 'scrapy.spidermiddlewares.referer.RefererMiddleware',
 'scrapy.spidermiddlewares.urllength.UrlLengthMiddleware',
 'scrapy.spidermiddlewares.depth.DepthMiddleware']
2026-09-01 16:11:14 [scrapy.middleware] INFO: Enabled item pipelines:
[]
2026-09-01 16:11:14 [scrapy.core.engine] INFO: Spider opened
2026-09-01 16:11:14 [scrapy.extensions.logstats] INFO: Crawled 0 pages (at 0 pages/min), scraped 0 items (at 0 items/min)
2026-09-01 16:11:14 [scrapy.extensions.telnet] INFO: Telnet console listening on 127.0.0.1:6023
2026-09-01 16:11:50 [scrapy.core.engine] INFO: Closing spider (finished)
2026-09-01 16:11:50 [scrapy.statscollectors] INFO: Dumping Scrapy stats:
{'downloader/request_bytes': 32100,
 'downloader/request_count': 100,
 'downloader/request_method_count/GET': 100,
 'downloader/response_bytes': 34117,
 'downloader/response_count': 100,
 'downloader/response_status_count/200': 100,
 'elapsed_time_seconds': 36.9196402689995,
 'finish_reason': 'finished',
 'finish_time': datetime.datetime(2026, 9, 1, 10, 41, 50, 954444, tzinfo=datetime.timezone.utc),
 'items_per_minute': 0.0,
 'log_count/INFO': 3,
 'memusage/max': 85032960,
 'memusage/startup': 85032960,
 'request_depth_max': 99,
 'response_received_count': 100,
 'responses_per_minute': 166.66666666666669,
 'scheduler/dequeued': 100,
 'scheduler/dequeued/memory': 100,
 'scheduler/enqueued': 100,
 'scheduler/enqueued/memory': 100,
 'start_time': datetime.datetime(2026, 9, 1, 10, 41, 14, 34797, tzinfo=datetime.timezone.utc)}
2026-09-01 16:11:50 [scrapy.core.engine] INFO: Spider closed (finished)
                                                                                                
┌──(satoru㉿satoru)-[~/…/HTB/CPTS/skills/web_enum]
└─$ cat results.json                                   
{
    "emails": [
        "1337testing@inlanefreight.htb"
    ],
    "links": [
        "http://dev.web1337.inlanefreight.htb:30313/index-909.html",
        "http://dev.web1337.inlanefreight.htb:30313/index-748.html",
        "http://dev.web1337.inlanefreight.htb:30313/index-555.html",
        "http://dev.web1337.inlanefreight.htb:30313/index-798.html",
        "http://dev.web1337.inlanefreight.htb:30313/index-329.html",
        "http://dev.web1337.inlanefreight.htb:30313/index-134.html",
        "http://dev.web1337.inlanefreight.htb:30313/index-248.html",
        "http://dev.web1337.inlanefreight.htb:30313/index-80.html",
        "http://dev.web1337.inlanefreight.htb:30313/index-807.html",
        "http://dev.web1337.inlanefreight.htb:30313/index-292.html",
        "http://dev.web1337.inlanefreight.htb:30313/index-77.html",
        "http://dev.web1337.inlanefreight.htb:30313/index-291.html",
        "http://dev.web1337.inlanefreight.htb:30313/index-567.html",
        "http://dev.web1337.inlanefreight.htb:30313/index-561.html",
        "http://dev.web1337.inlanefreight.htb:30313/index-1000.html",
        "http://dev.web1337.inlanefreight.htb:30313/index-302.html",
        "http://dev.web1337.inlanefreight.htb:30313/index-332.html",
        "http://dev.web1337.inlanefreight.htb:30313/index-226.html",
        "http://dev.web1337.inlanefreight.htb:30313/index-105.html",
        "http://dev.web1337.inlanefreight.htb:30313/index-165.html",
        "http://dev.web1337.inlanefreight.htb:30313/index-643.html",
        "http://dev.web1337.inlanefreight.htb:30313/index-977.html",
        "http://dev.web1337.inlanefreight.htb:30313/index-949.html",
        "http://dev.web1337.inlanefreight.htb:30313/index-789.html",
        "http://dev.web1337.inlanefreight.htb:30313/index-224.html",
        "http://dev.web1337.inlanefreight.htb:30313/index-947.html",
        "http://dev.web1337.inlanefreight.htb:30313/index-244.html",
        "http://dev.web1337.inlanefreight.htb:30313/index-459.html",
        "http://dev.web1337.inlanefreight.htb:30313/index-964.html",
        "http://dev.web1337.inlanefreight.htb:30313/index-379.html",
        "http://dev.web1337.inlanefreight.htb:30313/index-933.html",
        "http://dev.web1337.inlanefreight.htb:30313/index-817.html",
        "http://dev.web1337.inlanefreight.htb:30313/index-504.html",
        "http://dev.web1337.inlanefreight.htb:30313/index-737.html",
        "http://dev.web1337.inlanefreight.htb:30313/index-727.html",
        "http://dev.web1337.inlanefreight.htb:30313/index-577.html",
        "http://dev.web1337.inlanefreight.htb:30313/index-626.html",
        "http://dev.web1337.inlanefreight.htb:30313/index-247.html",
        "http://dev.web1337.inlanefreight.htb:30313/index-465.html",
        "http://dev.web1337.inlanefreight.htb:30313/index-204.html",
        "http://dev.web1337.inlanefreight.htb:30313/index-403.html",
        "http://dev.web1337.inlanefreight.htb:30313/index-581.html",
        "http://dev.web1337.inlanefreight.htb:30313/index-769.html",
        "http://dev.web1337.inlanefreight.htb:30313/index-334.html",
        "http://dev.web1337.inlanefreight.htb:30313/index-799.html",
        "http://dev.web1337.inlanefreight.htb:30313/index-938.html",
        "http://dev.web1337.inlanefreight.htb:30313/index-531.html",
        "http://dev.web1337.inlanefreight.htb:30313/index-939.html",
        "http://dev.web1337.inlanefreight.htb:30313/index-734.html",
        "http://dev.web1337.inlanefreight.htb:30313/index-888.html",
        "http://dev.web1337.inlanefreight.htb:30313/index-760.html",
        "http://dev.web1337.inlanefreight.htb:30313/index-189.html",
        "http://dev.web1337.inlanefreight.htb:30313/index-785.html",
        "http://dev.web1337.inlanefreight.htb:30313/index-631.html",
        "http://dev.web1337.inlanefreight.htb:30313/index-114.html",
        "http://dev.web1337.inlanefreight.htb:30313/index-472.html",
        "http://dev.web1337.inlanefreight.htb:30313/index-944.html",
        "http://dev.web1337.inlanefreight.htb:30313/index-350.html",
        "http://dev.web1337.inlanefreight.htb:30313/index-525.html",
        "http://dev.web1337.inlanefreight.htb:30313/index-733.html",
        "http://dev.web1337.inlanefreight.htb:30313/index-988.html",
        "http://dev.web1337.inlanefreight.htb:30313/index-458.html",
        "http://dev.web1337.inlanefreight.htb:30313/index-728.html",
        "http://dev.web1337.inlanefreight.htb:30313/index-660.html",
        "http://dev.web1337.inlanefreight.htb:30313/index-326.html",
        "http://dev.web1337.inlanefreight.htb:30313/index-24.html",
        "http://dev.web1337.inlanefreight.htb:30313/index-385.html",
        "http://dev.web1337.inlanefreight.htb:30313/index-989.html",
        "http://dev.web1337.inlanefreight.htb:30313/index-342.html",
        "http://dev.web1337.inlanefreight.htb:30313/index-795.html",
        "http://dev.web1337.inlanefreight.htb:30313/index-166.html",
        "http://dev.web1337.inlanefreight.htb:30313/index-553.html",
        "http://dev.web1337.inlanefreight.htb:30313/index-615.html",
        "http://dev.web1337.inlanefreight.htb:30313/index-203.html",
        "http://dev.web1337.inlanefreight.htb:30313/index-384.html",
        "http://dev.web1337.inlanefreight.htb:30313/index-220.html",
        "http://dev.web1337.inlanefreight.htb:30313/index-431.html",
        "http://dev.web1337.inlanefreight.htb:30313/index-408.html",
        "http://dev.web1337.inlanefreight.htb:30313/index-254.html",
        "http://dev.web1337.inlanefreight.htb:30313/index-364.html",
        "http://dev.web1337.inlanefreight.htb:30313/index-635.html",
        "http://dev.web1337.inlanefreight.htb:30313/index-755.html",
        "http://dev.web1337.inlanefreight.htb:30313/index-714.html",
        "http://dev.web1337.inlanefreight.htb:30313/index-815.html",
        "http://dev.web1337.inlanefreight.htb:30313/index-513.html",
        "http://dev.web1337.inlanefreight.htb:30313/index-862.html",
        "http://dev.web1337.inlanefreight.htb:30313/index-574.html",
        "http://dev.web1337.inlanefreight.htb:30313/index-463.html",
        "http://dev.web1337.inlanefreight.htb:30313/index-585.html",
        "http://dev.web1337.inlanefreight.htb:30313/index-925.html",
        "http://dev.web1337.inlanefreight.htb:30313/index-437.html",
        "http://dev.web1337.inlanefreight.htb:30313/index-641.html",
        "http://dev.web1337.inlanefreight.htb:30313/index-300.html",
        "http://dev.web1337.inlanefreight.htb:30313/index-202.html",
        "http://dev.web1337.inlanefreight.htb:30313/index-918.html",
        "http://dev.web1337.inlanefreight.htb:30313/index-895.html",
        "http://dev.web1337.inlanefreight.htb:30313/index-335.html",
        "http://dev.web1337.inlanefreight.htb:30313/index-687.html",
        "http://dev.web1337.inlanefreight.htb:30313/index-948.html"
    ],
    "external_files": [],
    "js_files": [],
    "form_fields": [],
    "images": [],
    "videos": [],
    "audio": [],
    "comments": [
        "<!-- Remember to change the API key to ba988b835be4aa97d068941dc852ff33 -->"
    ]
}                                                                                    
```

Q5. What is the API key the inlanefreight.htb developers will be changing too?

```
<!-- Remember to change the API key to ba988b835be4aa97d068941dc852ff33 -->
```