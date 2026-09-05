
## 1. FSMO Roles (Flexible Single Master Operation)

Active Directory uses multi-master replication for most tasks, but **5 specialized roles** must be handled by a single Domain Controller (DC) at any given time to prevent conflicts.

### Forest-Wide Roles (1 per Forest)

- **Schema Master:** Controls read/write access to the AD Schema (defines object classes and attributes).
    
- **Domain Naming Master:** Ensures unique domain names across the forest when adding/removing domains.
    

### Domain-Wide Roles (1 per Domain)

- **RID Master (Relative ID):** Distributes blocks of unique RIDs to DCs. An object's **SID** = Domain SID + RID.
    
- **PDC Emulator:** Authoritative DC for password changes, time synchronization, domain authentication, and Group Policy updates.
    
- **Infrastructure Master:** Translates GUIDs, SIDs, and Distinguished Names (DNs) across domains. If down, Access Control Lists (ACLs) show raw SIDs instead of resolved account names.
    

## 2. Functional Levels

Functional levels dictate which AD DS features are active and which Windows Server OS versions can act as Domain Controllers.

### Key Domain Functional Level Additions

- **Server 2003:** Added `lastLogonTimestamp`, constrained delegation, and `netdom.exe`.
    
- **Server 2008:** Added AES Kerberos support, Fine-Grained Password Policies, and DFS-R.
    
- **Server 2008 R2:** Added Managed Service Accounts (MSAs).
    
- **Server 2012 / 2012 R2:** Added Protected Users group, Kerberos armoring (FAST), Authentication Policies, and Silos.
    
- **Server 2016:** Introduced interactive smart card requirements and enhanced Kerberos protections.
    
- **Server 2019 note:** Introduced no new functional level; minimum requirement to add a Server 2019 DC is Server 2008 level with DFS-R for `SYSVOL`.
    

### Key Forest Functional Level Capabilities

- **Server 2003:** Introduced forest trusts, domain renaming, and Read-Only DCs (RODCs).
    
- **Server 2008 R2:** Introduced the **Active Directory Recycle Bin** for soft-deleting objects.
    
- **Server 2016:** Introduced Privileged Access Management (PAM) via Microsoft Identity Manager (MIM).
    

## 3. AD Trusts & Authentication Mechanics

Trusts link domain authentication systems, allowing users to access resources in external domains or forests.

### Trust Types

- **Parent-Child:** Automatic 2-way transitive trust between parent and child domains in the same forest.
    
- **Cross-link:** Speed-up trust established between sibling child domains.
    
- **Tree-root:** 2-way transitive trust formed when adding a new tree root domain to an existing forest.
    
- **Forest:** Transitive trust between two forest root domains.
    
- **External:** Non-transitive link between domains in separate forests (uses **SID filtering**).
    

### Direction and Transitivity

- **Transitive vs. Non-Transitive:** Transitive trusts extend to other domains that the target trusts (A trusts B, B trusts C $\rightarrow$ A trusts C). Non-transitive stops at the target domain only.
    
- **Trust Direction vs. Access Direction:** Access flows in the **opposite direction** of trust (If Domain A _trusts_ Domain B, users in Domain B can _access_ resources in Domain A).
    
- **Security Implications:** Misconfigured or legacy trusts (e.g., post-merger) often leave paths open for cross-domain attacks like Kerberoasting.