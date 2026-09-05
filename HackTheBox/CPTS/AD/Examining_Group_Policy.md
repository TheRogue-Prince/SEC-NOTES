
### Group Policy Overview

Group Policy is a Windows feature used in Active Directory (AD) environments to centrally configure and enforce user, computer, application, and operating system settings across a network. It plays a critical role in defense-in-depth strategies and domain security management.

### Group Policy Objects (GPOs)

- **Definition:** A GPO is a collection of policy settings identified by a unique name and GUID.
    
- **Scope:** Can be linked to Sites, Domains, or Organizational Units (OUs). Single GPOs can be linked to multiple containers, and containers can contain multiple GPOs.
    
- **Application Types:** Contains settings that apply to either Computer Configuration (machine level) or User Configuration (user level).
    

### Order of Precedence

GPOs process in a specific order. Settings processed later in the sequence overwrite earlier settings:

1. **Local Group Policy:** Defined directly on the local machine. Overwritten by any domain-level policy.
    
2. **Site Policy:** Applied to the specific Enterprise Site where the host resides.
    
3. **Domain-wide Policy:** Applied across the entire domain (e.g., Default Domain Policy).
    
4. **Organizational Unit (OU):** Applied to specific OUs to enforce role-specific settings.
    
5. **Nested OUs:** Settings applied to child/nested OUs process last and override parent OU policies.
    

_Note:_ Computer-level policy settings always take priority over matching User-level policy settings.

### Links and Overrides

- **Link Order:** When multiple GPOs are linked to the same container, the GPO with Link Order 1 processes last and holds the highest precedence.
    
- **Enforced:** Setting a GPO to "Enforced" (formerly "No Override") prevents lower-level OU policies from overriding its settings. An Enforced Default Domain Policy takes precedence over all other GPOs.
    
- **Block Inheritance:** Applied at the OU level to prevent settings from parent OUs/Domains from being inherited. However, an **Enforced** GPO will bypass Block Inheritance.
    

### Refresh Frequency

- **Clients/Servers:** Refresh automatically every 90 minutes by default, with a random offset of +/- 30 minutes (60–120 minutes total) to prevent network congestion.
    
- **Domain Controllers:** Refresh every 5 minutes by default.
    
- **Manual Refresh:** Force immediate application using the command `gpupdate /force`.
    

### Security Considerations

- **Misconfigurations:** Excessive permissions on GPOs (e.g., granting write access to standard users) create high-risk attack vectors.
    
- **Abuse Vectors:** Attackers with GPO edit rights can achieve privilege escalation, lateral movement, or persistence by deploying scheduled tasks, adding local administrators, or executing malicious scripts domain-wide.