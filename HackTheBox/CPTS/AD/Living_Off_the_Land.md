```
PS C:\Users\htb-student> Get-MpComputerStatus | Select-Object AMProductVersion

AMProductVersion
----------------
4.18.2109.6


PS C:\Users\htb-student>





```

```
S C:\Users\htb-student> net localgroup administrators
Alias name     administrators
Comment        Administrators have complete and unrestricted access to the computer/domain

Members

-------------------------------------------------------------------------------
Administrator
INLANEFREIGHT\adunn
INLANEFREIGHT\Domain Admins
INLANEFREIGHT\Domain Users
The command completed successfully.
```

```
S C:\Users\htb-student> Get-ADUser -Filter {Enabled -eq $false} -Properties Description, AdminCount | Select-Object SamAccountName, Description, AdminCount

SamAccountName       Description                                              AdminCount
--------------       -----------                                              ----------
guest                Built-in account for guest access to the computer/domain
krbtgt               Key Distribution Center Service Account                  1
bross                HTB{LD@P_I$_W1ld}                                        1
$725000-9jb50uejje9f
sm_752cbd23e73649258
sm_8b3ff26494d94da89
sm_434e56f7c43f4534a
sm_51dc5f77b78546d7b
sm_c6ccf50003bf4310b
sm_c7c8c6f5727449fbb
sm_925f7acdff9344408
sm_820598b3d6c548a08
sm_8f47aca8186c4f0da
```