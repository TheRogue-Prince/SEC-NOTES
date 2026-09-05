#### 1. User Accounts

- **Purpose:** Allow humans or programs (services) to authenticate and access resources. Generates an **access token** upon login containing identity and group memberships.
    
- **Types:**
    
    - **Standard/Admin:** Tied to individuals or roles.
        
    - **Service Accounts:** Run background applications/services.
        
    - **KRBTGT:** Built-in AD service account for Kerberos authentication (prime target for Golden Ticket attacks).
        
- **Attack Surface:** High risk due to weak passwords, misconfigurations, or over-privileged access.
    

#### 2. Local Accounts

- Stored locally on a single host; **do not** cross domain boundaries.
    
- **Key Built-in Accounts:**
    
    - **Administrator:** Full local control (SID `...-500`).
        
    - **Guest:** Disabled by default, limited access.
        
    - **SYSTEM (`NT AUTHORITY\SYSTEM`):** Highest possible privilege level on a Windows host; service account with no user profile.
        
    - **Network Service / Local Service:** Predefined accounts for running system services with minimal/network-specific privileges.
        

#### 3. Key Naming Attributes

- **UserPrincipalName (UPN):** Primary logon name (typically email format, e.g., `user@domain.local`).
    
- **SAMAccountName:** Legacy logon name format.
    
- **objectSID:** Unique Security Identifier for permissions.
    
- **ObjectGUID:** Immutable, globally unique identifier.
    
- **sIDHistory:** Retains past SIDs (often seen after domain migrations).
    

#### 4. Domain-Joined vs. Non-Domain-Joined

- **Domain-Joined:** Managed centrally via Active Directory/Group Policy; users can log into any domain host and share resources enterprise-wide.
    
- **Non-Domain-Joined (Workgroup):** Standalone management; accounts only exist locally on that specific machine.
    
- **Pro-Tip:** Gaining `NT AUTHORITY\SYSTEM` on a domain-joined machine grants similar read access to standard domain users, serving as a powerful pivot point for AD enumeration.