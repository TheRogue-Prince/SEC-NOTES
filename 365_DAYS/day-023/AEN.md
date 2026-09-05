- **Q7 (Gitlab):** Registered an account and logged into the Gitlab instance to retrieve the flag.
    
- **Q8 (XXE Vulnerability):** Discovered a new subdomain via the Gitlab repository, logged in with default credentials (`admin:admin`), and exploited an XXE vulnerability in the payment page's `userid` parameter to read `flag.txt`.
    
- **Q9 (Command Injection & Credential Brute-Forcing):**
    
    - Targeted `monitoring.inlanefreight.local/login.php` and cracked the `admin` password (`12qwaszx`) using `ffuf` and `hydra`.
        
    - Located the vulnerable ping interface (`ping.php`) post-login and executed command injection using a newline character (`%0a`) and field separators (`${IFS}`) to read the flag file (`00112233_flag.txt`).
        
- **Brute-Force Optimization:** Using a small, targeted wordlist paired with the exact failure string (`:F=Invalid credentials!`) prevents false positives and performance issues compared to using a massive wordlist like `rockyou.txt`.
-

### 1. Privilege Escalation on `dmz01` (`webdev` $\rightarrow$ `root`)

- **Log Enumeration (`webdev` $\rightarrow$ `srvadm`):** Used `aureport --tty` to inspect terminal logs, uncovering credentials for the `srvadm` user and successfully switching contexts via `su`.
    
- **Sudo Abuse (`srvadm` $\rightarrow$ `root`):** Identified `sudo -l` misconfigurations granting `srvadm` NOPASSWD execution over `/usr/bin/openssl`.
    
- **SSH Key Extraction:** Used `openssl enc` to read root's private key (`/root/.ssh/id_rsa`) directly from `/root/.ssh/`.
    
- **Root Access:** Saved and secured the private key (`chmod 600`) and successfully established an SSH connection as `root`.
    

### 2. Internal Network Enumeration & NFS Mounting

- **Share Discovery:** Identified an active NFS service on the internal network segment (`172.16.8.20`).
    
- **Mounting the Export:** Successfully mounted the remote share locally to inspect contents:
    
    Bash
    
    ```
    mount -t nfs 172.16.8.20:/DEV01 /tmp/DEV01
    ```
    

### 3. Credential Harvesting

- **File Discovery:** Navigated the mounted NFS directory structure to locate configuration files under `/tmp/DEV01/DNN/`.
    
- **Credential Extraction:** Inspected `web.config` and recovered cleartext administrative credentials:
    
    - **Username:** `Administrator`
        
    - **Password:** `D0tn31Nuk3R0ck$$@123`