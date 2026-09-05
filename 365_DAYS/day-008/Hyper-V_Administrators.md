
The [Hyper-V Administrators](https://docs.microsoft.com/en-us/windows/security/identity-protection/access-control/active-directory-security-groups#hyper-v-administrators) group has full access to all [Hyper-V features](https://docs.microsoft.com/en-us/windows-server/manage/windows-admin-center/use/manage-virtual-machines). If Domain Controllers have been virtualized, then the virtualization admins should be considered Domain Admins. They could easily create a clone of the live Domain Controller and mount the virtual disk offline to obtain the NTDS.dit file and extract NTLM password hashes for all users in the domain.

#### Target File

An example of this is Firefox, which installs the `Mozilla Maintenance Service`. We can update [this exploit](https://raw.githubusercontent.com/decoder-it/Hyper-V-admin-EOP/master/hyperv-eop.ps1) (a proof-of-concept for NT hard link) to grant our current user full permissions on the file below:
```

        shellsession
`C:\Program Files (x86)\Mozilla Maintenance Service\maintenanceservice.exe`
```

#### Taking Ownership of the File

After running the PowerShell script, we should have full control of this file and can take ownership of it.

```
        cmd
`C:\htb> takeown /F C:\Program Files (x86)\Mozilla Maintenance Service\maintenanceservice.exe`

```
#### Starting the Mozilla Maintenance Service

Next, we can replace this file with a malicious `maintenanceservice.exe`, start the maintenance service, and get command execution as SYSTEM.

```
        cmd
`C:\htb> sc.exe start MozillaMaintenance`
```