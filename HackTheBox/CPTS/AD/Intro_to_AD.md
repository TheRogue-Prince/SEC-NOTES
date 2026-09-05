# **Active Directory Terminology Notes**

### **Core Directory Components**

- **Object:** Any resource in AD (users, computers, printers, OUs, Domain Controllers).
    
- **Attributes:** Characteristics defining an object (e.g., hostname, `displayName`, `givenName`). Accessed via LDAP names.
    
- **Schema:** The blueprint/database definition of AD. Defines object classes (e.g., `user`, `computer`) and their attributes. Creating an object from a class is called **instantiation**.
    
- **Domain:** A logical grouping of AD objects operating independently or connected via trust relationships.
    
- **Tree:** A collection of AD domains sharing a single root domain, contiguous namespace, and Global Catalog. Adding a domain under another forms a parent-child trust.
    
- **Forest:** The topmost container in AD, consisting of one or more domain trees sharing a common schema, configuration, and Global Catalog. Forests operate independently but can form trust relationships.
    
- **Container:** An object that holds other objects in the hierarchy.
    
- **Leaf:** An object that cannot contain other objects, sitting at the end of the hierarchy.
    

### **Object Identification & Naming**

- **GUID (Globally Unique Identifier):** A unique 128-bit value assigned to every AD object at creation (`ObjectGUID`). It never changes during the object's lifetime and is the most accurate way to query objects.
    
- **Security Principal:** Any authenticated entity (users, computer accounts, service processes) that can manage or be granted access to resources.
    
- **SID (Security Identifier):** A unique string issued by a DC to identify security principals/groups. Stored in access tokens during login. Never reused once deleted. Includes well-known SIDs (e.g., `Everyone` group).
    
- **Distinguished Name (DN):** The full directory path to an object (e.g., `cn=bjones,ou=IT,ou=Employees,dc=inlanefreight,dc=local`).
    
- **Relative Distinguished Name (RDN):** A single unique component of a DN at the current hierarchy level (e.g., `bjones`).
    
- **sAMAccountName:** The traditional logon name (max 20 characters, must be unique).
    
- **userPrincipalName (UPN):** An optional identity attribute in email format (`user@domain.local`).
    
- **sIDHistory:** Preserves original SIDs during domain migrations to retain legacy access permissions. Can be abused if SID Filtering is disabled.
    

### **Domain Infrastructure & Roles**

- **FSMO Roles (Flexible Single Master Operation):** Multi-master roles designed to prevent conflicts during critical operations:
    
    - _Forest-wide (1 per forest):_ **Schema Master**, **Domain Naming Master**.
        
    - _Domain-wide (1 per domain):_ **RID Master**, **PDC Emulator**, **Infrastructure Master**.
        
- **Global Catalog (GC):** A DC role storing a full copy of its own domain objects and a partial copy of all objects across the entire forest. Used for forest-wide searches and cross-domain authentication.
    
- **Read-Only Domain Controller (RODC):** A read-only replica of AD used in low-security/branch offices. Does not cache passwords by default (except its own account & KRBTGT) and does not push changes out.
    
- **Replication:** The synchronization mechanism managed by the **Knowledge Consistency Checker (KCC)** service to replicate object updates across DCs.
    

### **Access Control & Security Mechanisms**

- **Service Principal Name (SPN):** Unique identifier for a service instance used in Kerberos authentication to associate service accounts without revealing account details.
    
- **Group Policy Object (GPO):** Virtual collection of user and computer policy settings applied domain-wide or per OU. Identified by a GUID.
    
- **ACL (Access Control List):** An ordered collection of Access Control Entries (ACEs).
    
- **DACL (Discretionary ACL):** Lists ACEs defining explicitly allowed or denied permissions for security principals. Checked sequentially until matched.
    
- **SACL (System ACL):** Defines auditing parameters to log access attempts to secured objects in the event log.
    
- **AdminSDHolder:** Protects built-in privileged groups via the **SDProp** (SD Propagator) process, which runs every hour on the PDC Emulator to overwrite non-standard ACLs on protected accounts.
    
- **adminCount:** Attribute set to `1` for accounts protected by the SDProp process. Frequently targeted by attackers.
    
- **dsHeuristics:** A forest-wide configuration string; can be configured to exclude specific built-in groups from AdminSDHolder/SDProp protection.
    

### **Storage, Recovery & Management Tools**

- **FQDN (Fully Qualified Domain Name):** Complete host network address formatted as `hostname.domain.tld` (e.g., `DC01.INLANEFREIGHT.LOCAL`).
    
- **NTDS.DIT:** The primary Active Directory database located at `C:\Windows\NTDS\ NTDS.dit`. Contains domain data, group memberships, and user password hashes.
    
- **SYSVOL:** A shared network folder replicated across DCs containing logon scripts, Group Policies, and system policies via FRS/DFSR.
    
- **Tombstone:** A container holding deleted AD objects with `isDeleted=TRUE`. Default lifetime is 60 or 180 days before permanent purging. Restored objects lose most attributes.
    
- **AD Recycle Bin:** Feature introduced in Server 2008 R2 allowing full restoration of deleted objects with all attributes intact without needing DC reboots or backups. Default retention is 60 days.
    
- **ADUC (Active Directory Users & Computers):** Standard GUI console/PowerShell interface for managing users, groups, computers, and OUs.
    
- **ADSI Edit:** Advanced GUI editor providing direct attribute-level access and modifications to the AD database hierarchy.
    
- **MSBROWSE:** Obsolete legacy Windows LAN protocol used to browse shared resources and locate DCs via `nbtstat` or `nltest`. Replaced by SMB/CIFS.