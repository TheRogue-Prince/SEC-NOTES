## Active Directory Objects: Core Summary

In **Active Directory (AD)**, an **object** is any resource within the network environment—from individual users to entire network domains.

### 1. Security Principals vs. Non-Security Principals

- **Security Principals** get assigned a **SID** (Security Identifier) and a **GUID** (Globally Unique Identifier). They can be granted direct permissions to access resources and are prime targets for attackers looking to enumerate or pivot through a domain.
    
    - **Users:** Leaf objects representing individuals. Feature 800+ potential attributes (email, manager, password history).
        
    - **Computers:** Workstations or servers joined to the domain. Full control over a computer (`NT AUTHORITY\SYSTEM`) yields privileges similar to a domain user.
        
    - **Groups:** Container objects used to manage permissions efficiently at scale. _Nested groups_ (groups inside groups) are frequently audited during security assessments (e.g., via BloodHound) to expose unintended privilege escalation paths.
        
- **Non-Security Principals** only have a **GUID**. They are used for informational tracking or target mapping, but cannot directly own permissions.
    
    - **Contacts:** External non-domain entities (e.g., third-party vendors).
        
    - **Printers:** References to physical network printers.
        
    - **Shared Folders:** Pointers to shared storage locations with specific access control lists (ACLs).
        

### 2. Organizational Units (OUs) & Structural Containers

- **Organizational Units (OUs):** Administrative containers used to group objects (users, computers) for **delegation** (e.g., letting Help Desk reset passwords without full admin rights) and applying targeted **Group Policy Objects (GPOs)**.
    
- **Domain:** The fundamental structure of an AD network, holding its own separate database and applying baseline security policies (e.g., password complexity).
    
- **Domain Controllers (DCs):** The "brains" of AD. They validate login requests, maintain the domain database, and enforce authorization policies.
    
- **Sites:** Subnet groupings connected by high-speed links designed to optimize DC database replication.
    
- **Built-in:** Default container housing pre-configured system groups upon domain creation.
    
- **Foreign Security Principals (FSPs):** Placeholder objects storing the SID of an external user, group, or computer from a trusted external forest.