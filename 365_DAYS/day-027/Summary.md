**AD HTB**

- **Insecure by Design:** AD prioritizes availability and information sharing, meaning default installations lack essential hardening measures.
    
- **Key Hardening Tools:** Deploy **LAPS** for local admin password rotation, **gMSAs** for automated service account credential management, and **AppLocker** (Application Control Policies) to restrict unauthorized executables.
    
- **Privilege & Account Management:** Enforce strict **account separation** (distinct accounts for daily tasks vs. administration), limit **Domain Admin** usage exclusively to Domain Controllers, and eliminate stale or legacy accounts.
    
- **Policy & Monitoring:** Leverage Group Policy for **Restricted Groups** and robust account/local policies, implement timely patch management (WSUS/SCCM), and enforce **MFA** alongside strong passphrases (12+ characters) for remote access.

**Python**

**Core Language Fundamentals:** Mastered variable declaration, type casting with `int()`, interactive user handling via `input()`, and control flow structure using `for` loops alongside `if` / `elif` / `else` conditional logic.

**Input Sanitization & Parsing:** Utilized `.split(",")` and `.split("\n")` to parse raw input strings into structured lists, combined with `.strip()` to scrub leading/trailing whitespace and `\n` characters to prevent execution crashes.

**File I/O Management:** Implemented context-managed file handling (`with open()`) across `"r"` (read), `"w"` (overwrite), and `"a"` (append) modes to dynamically extract target lists and persist processed results to disk.

**Key Technical Takeaways:** File reads return `str` by default and require explicit casting to `int()` before numerical logic checks; `.strip()` must be applied to drop trailing empty lines and sanitize individual array elements.

**Silentium HTB Machine**

- **Reconnaissance & Enumeration:**
    - Discovered subdomains (`staging.silentium.htb`) via virtual host fuzzing.
    - Identified vulnerable web applications running inside internal services.
- **Credential Recovery / Reset:**
    - Leveraged password reset functionalities on staging APIs to recover and overwrite tokens/credentials for accounts.
- **Initial Access (Container):**
    - Exploited an application vulnerability (CVE-2025-8110) via MCP server configurations, achieving Remote Code Execution (RCE) and landing inside an initial Docker container via a reverse shell.
- **Internal Pivoting & Port Forwarding:**
    - Enumerated listening ports on the target environment (`ss -tunlp`) to discover internal services (such as port `3001`).
    - Used SSH local port forwarding (`-L`) to bridge access to internal applications running on the remote host.
- **Privilege Escalation:**
    - Exploited an internal service flaw (Gogs CVE-2025-8110 git symlink vulnerability) through the port-forwarded interface.
    - Delivered a payload that triggered code execution via git hooks, ultimately escalating to **root** privileges on the host machine.