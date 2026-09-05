#### 1. The Core Challenge of Active Directory (AD)

- AD is designed around central management and rapid, flexible information sharing.
    
- By default, it is **insecure by design** and lacks many hardening measures out of the box.
    
- It leans heavily toward **Availability** and **Confidentiality** over absolute security.
    

#### 2. General Active Directory Hardening Measures

- **LAPS (Local Administrator Password Solution):** Randomizes and rotates local administrator passwords on Windows hosts to prevent lateral movement.
    
- **Group Managed Service Accounts (gMSA):** Secure, non-interactive service accounts with automatically managed 120-character passwords rotated by domain controllers.
    
- **Account Separation:** Administrators must use two distinct accounts: a standard account for daily tasks (email, browsing) and a separate `_admin` account for administrative duties.
    
- **Limiting Domain Admin Usage:** Domain Admin accounts should **only** be used to log into Domain Controllers, never regular workstations, jump hosts, or web servers, to prevent credential theft from memory.
    

#### 3. Group Policy & Security Policies

- **Account Policies:** Control password rules, lockout thresholds, and Kerberos ticket lifetimes.
    
- **Local Policies:** Manage security event auditing, user rights assignments, and restrictions on hardware/software.
    
- **Application Control Policies (AppLocker):** Restrict users from running unauthorized executables, scripts, or installers (e.g., blocking standard users from running `cmd.exe` or `PowerShell`).
    
- **Restricted Groups:** Enforce strict group membership across domain hosts via GPO (e.g., locking down local Administrators groups).
    

#### 4. Operational Best Practices

- **Patch Management:** Timely updates using WSUS or SCCM to prevent exploitation of known vulnerabilities.
    
- **Audit Policies & Logging:** Robust logging and monitoring to detect anomalies like password spraying, Kerberoasting, or AD enumeration.
    
- **Stale Account Auditing:** Regularly disable or remove unused, legacy service and user accounts.
    
- **Role Separation:** Do not install unnecessary server roles (like IIS web servers or databases) directly onto Domain Controllers.
    
- **Strong Authentication:** Enforce long passphrases (12+ characters), custom password filters, and **Multi-Factor Authentication (MFA)** for all remote access (RDP/WinRM).