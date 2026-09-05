## 1. Hash vs. Protocol Overview

It's critical to distinguish between **hash algorithms** (how passwords are stored) and **authentication protocols** (how credentials are sent over a network). Neither LM nor NTLM uses a salt.

|**Category**|**Storage / Protocol**|**Cryptographic Technique**|**Mutual Auth?**|**Primary Use / Status**|
|---|---|---|---|---|
|**LM**|Hash Algorithm|DES-based|No|Legacy hash; disabled by default since Windows Vista/Server 2008.|
|**NT / NTLM**|Hash Algorithm|MD4(UTF-16-LE)|No|Modern Windows password storage (SAM / NTDS.DIT).|
|**NTLMv1**|Protocol|Challenge-Response|No|Net-NTLMv1 authentication protocol; vulnerable to cracking.|
|**NTLMv2**|Protocol|HMAC-MD5|No|Default Net-NTLM protocol since Windows 2000.|
|**Kerberos**|Protocol|Symmetric & Asymmetric|**Yes**|Preferred domain authentication mechanism.|

## 2. Windows Password Hashes

### LAN Manager (LM) Hash

- **Structure:** Max 14 characters, non-case-sensitive. Password is split into two 7-character chunks, padded with NULLs, encrypted with fixed key `KGS!@#$%`, and concatenated.
    
- **Flaw:** Attackers only need to brute-force two 7-character chunks independently. Passwords $\le$ 7 chars always produce the same second half (`aad3c435b514a4ee`).
    

### NTHash / NTLM Hash

- **Structure:** `MD4(UTF-16-LE(password))`.
    
- **Full Output Structure (SAM/NTDS dump):**
    
    `Username : RID : LM-Hash : NT-Hash :::`
    
    _Example:_ `Rachel:500:aad3c435b514a4eeaad3b935b51304fe:e46b9e548fa0d122de7f59fb6d48eaa2:::`
    
- **Key Attack:** Vulnerable to **Pass-the-Hash (PtH)**. An attacker can authenticate as a local/domain user using _only_ the NT hash without knowing the cleartext password.
    

## 3. Net-NTLM Protocols (Challenge-Response)

When authenticating over a network via NTLM, a **3-way handshake** occurs:

1. **`NEGOTIATE_MESSAGE`** (Client $\rightarrow$ Server)
    
2. **`CHALLENGE_MESSAGE`** (Server $\rightarrow$ Client; sends an 8-byte server challenge)
    
3. **`AUTHENTICATE_MESSAGE`** (Client $\rightarrow$ Server; responds with the Net-NTLM hash)
    

### Net-NTLMv1 vs. Net-NTLMv2

- **Net-NTLMv1:** Client encrypts the 8-byte server challenge using DES keys derived from the NT/LM hash. Easily cracked offline.
    
- **Net-NTLMv2:** Employs HMAC-MD5 with client challenges, variable domain details, and timestamps to prevent replay and relay attacks.
    
- **Important:** Net-NTLM challenge-response hashes captured over the network **CANNOT** be used for Pass-the-Hash; they must be cracked offline to recover the cleartext password.
    

## 4. Domain Cached Credentials (MSCache / DCC)

- **Purpose:** Allows domain users to log into Windows hosts when disconnected from a Domain Controller (e.g., offline or network outages).
    
- **Storage Location:** `HKEY_LOCAL_MACHINE\SECURITY\Cache` (requires local admin privileges to read).
    
- **Default Retained Count:** **10 hashes** (`DCC2` / `MSCache2`).
    
- **Limitations:** Very slow/expensive to crack (even with powerful GPUs) and **cannot** be used for Pass-the-Hash or NTLM relays.