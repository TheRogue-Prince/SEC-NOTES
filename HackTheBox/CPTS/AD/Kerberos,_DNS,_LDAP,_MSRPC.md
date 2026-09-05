## 1. Kerberos (Port 88 TCP/UDP)

Kerberos is the default **ticket-based, stateless** authentication protocol for Active Directory. It avoids sending raw passwords over the network by relying on a **Key Distribution Center (KDC)** running on Domain Controllers.

### The 5-Step Kerberos Authentication Flow

1. **AS-REQ (Authentication Request):** User encrypts a timestamp with their password hash and sends it to the KDC to prove identity.
    
2. **AS-REP (Authentication Reply):** KDC validates credentials and returns a **Ticket Granting Ticket (TGT)**, encrypted using the secret key of the domain's `krbtgt` account.
    
3. **TGS-REQ (Service Request):** User presents the valid TGT to the KDC to request access to a specific service.
    
4. **TGS-REP (Service Reply):** KDC issues a **Ticket Granting Service (TGS)** ticket, encrypted with the target service account's NTLM password hash.
    
5. **AP-REQ (Application Request):** User presents the TGS to the target service/application to authenticate and gain access.
    

## 2. DNS (Port 53 TCP/UDP)

DNS is essential for locating resources within Active Directory. It resolves hostnames to IP addresses and relies on **Service (SRV) records** to direct clients to specific domain services (like Domain Controllers).

- **Protocol Behavior:** Uses UDP 53 by default; falls back to TCP 53 when payload sizes exceed 512 bytes.
    
- **Dynamic DNS (DDNS):** Automatically updates IP changes in the DNS database.
    
- **Common Enumeration Commands (`nslookup`):**
    
    - `nslookup INLANEFREIGHT.LOCAL` $\rightarrow$ Returns IP addresses of Domain Controllers (Forward Lookup).
        
    - `nslookup 172.16.6.5` $\rightarrow$ Returns FQDN of the host (Reverse Lookup).
        

## 3. LDAP (Port 389 / Port 636 LDAPS)

Lightweight Directory Access Protocol is the language applications use to query and interact with Active Directory objects (_Analogy: AD is to Apache as LDAP is to HTTP_). Specified under **RFC 4511**.

### Authentication Types (BIND Operations)

- **Simple Authentication:** Authenticates directly via unencrypted or encrypted username/password BIND requests.
    
- **SASL Authentication:** Uses external security mechanisms (e.g., Kerberos) to handle the authentication state before binding to LDAP.
    
- **Security Risk:** Plaintext LDAP traffic can be sniffed on internal networks if TLS encryption (LDAPS) is not enforced.
    

## 4. MSRPC (Microsoft Remote Procedure Call)

MSRPC enables interprocess communication between clients and AD services using four core RPC interfaces:

| **Interface**  | **Purpose**                             | **Penetration Testing / Security Note**                                                                                                                      |
| -------------- | --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **`lsarpcA`**  | Local Security Authority (LSA) policies | Manages local security, audit policies, and interactive logons.                                                                                              |
| **`netlogon`** | Background authentication               | Continuously validates users and services across the domain.                                                                                                 |
| **`samr`**     | Remote Security Account Manager         | Used by admins to manage accounts. Attackers (and tools like BloodHound) query `samr` to map internal domain paths. Can be restricted via registry settings. |
| **`drsuapi`**  | Directory Replication Service           | Handles DC-to-DC replication. Attackers exploit `drsuapi` to extract the `NTDS.dit` database (DCSync attack) to dump all domain password hashes.             |