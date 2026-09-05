#### 1. Groups vs. Organizational Units (OUs)

- **Groups:** Primarily used to assign permissions and access rights to resources.
    
- **OUs:** Used for grouping objects to manage Group Policy deployment and delegate administrative tasks.
    

#### 2. Group Types

- **Security Groups:** Used to assign permissions and rights to multiple users simultaneously (key target for security audits and penetration testing).
    
- **Distribution Groups:** Used exclusively for email distribution lists (cannot be used for resource permissions).
    

#### 3. Group Scopes

- **Domain Local Group:**
    
    - _Scope:_ Local to the domain where created.
        
    - _Membership:_ Can contain users/groups from **other** domains, but only controls resources within its own domain.
        
- **Global Group:**
    
    - _Scope:_ Can grant access to resources in other domains.
        
    - _Membership:_ Can **only** contain accounts from the domain where it was created.
        
- **Universal Group:**
    
    - _Scope:_ Spans multiple domains across the entire forest.
        
    - _Membership:_ Can contain users from any domain. Stored in the Global Catalog (GC)—changes cause **forest-wide replication**.
        

#### 4. Nested Group Membership

- Groups placed inside other groups.
    
- Users inherit permissions from groups they belong to directly, as well as any parent groups.
    
- Can create hidden privilege escalation paths (often discovered using tools like **BloodHound**).
    

#### 5. Important Group Attributes

- `cn`: Common Name.
    
- `member`: Direct members of the group (users, computers, other groups).
    
- `memberOf`: Parent groups containing this group.
    
- `groupType`: Defines the type and scope using an integer.
    
- `objectSid`: Unique Security Identifier for the group.