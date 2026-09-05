#### 1. Rights vs. Privileges

- **Rights:** Authorizations to access objects (e.g., reading a specific file or folder).
    
- **Privileges:** Authorizations to perform specific system-level actions (e.g., shutting down a system, debugging programs, or loading drivers). Governed via **User Rights Assignment**.
    

#### 2. High-Risk Built-In Groups

- **Domain Admins:** Full administrative control over the entire domain.
    
- **Enterprise Admins:** Forest-wide administrative control (exists only in the root domain).
    
- **Backup Operators:** Can bypass file permissions to back up/restore files; can create shadow copies of the SAM/NTDS database to extract credentials.
    
- **Account Operators:** Can create/modify users and local/global groups (cannot manage administrative accounts).
    
- **Server Operators:** Can modify services, access SMB shares, and backup DCs.
    
- **DnsAdmins:** Access to network DNS information (frequently targeted for privilege escalation to Domain Admin).
    

#### 3. Dangerous User Privileges (`whoami /priv`)

- **`SeBackupPrivilege` / `SeRestorePrivilege`:** Allows backing up/restoring any file, enabling extraction of the NTDS.dit database or registry hives.
    
- **`SeDebugPrivilege`:** Allows debugging process memory, often abused with tools like Mimikatz to dump plaintext credentials from LSASS.
    
- **`SeImpersonatePrivilege`:** Allows token impersonation of privileged users (e.g., `NT AUTHORITY\SYSTEM`), exploitable via tools like PrintSpoofer or JuicyPotato.
    
- **`SeTakeOwnershipPrivilege`:** Allows taking ownership of files or objects.
    

#### 4. User Account Control (UAC)

- Windows security feature that restricts applications from running with full administrative privileges by default.
    
- Privileged users (like Domain Admins) require an **elevated** command prompt or PowerShell session to leverage their full suite of security rights and privileges.