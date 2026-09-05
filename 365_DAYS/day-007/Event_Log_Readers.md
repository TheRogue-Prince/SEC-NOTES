Administrators or members of the [Event Log Readers](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/dn579255\(v=ws.11\)?redirectedfrom=MSDN#event-log-readers) group have permission to access event log. It is conceivable that system administrators might want to add power users or developers into this group to perform certain tasks without having to grant them administrative access.

check the group privilege,then run  wevtutil to read the logs.

```


PS C:\Users\logger> net localgroup

Aliases for \\WINLPE-SRV01

-------------------------------------------------------------------------------
*Access Control Assistance Operators
*Administrators
*Backup Operators
*Certificate Service DCOM Access
*Cryptographic Operators
*Distributed COM Users
*Event Log Readers
*Guests
*Hyper-V Administrators
*IIS_IUSRS
*Network Configuration Operators
*Performance Log Users
*Performance Monitor Users
*Power Users
*Print Operators
*RDS Endpoint Servers
*RDS Management Servers
*RDS Remote Access Servers
*Remote Desktop Users
*Remote Management Users
*Replicator
*SQLServer2005SQLBrowserUser$WINLPE-SRV01
*Storage Replica Administrators
*System Managed Accounts Group
*Users
The command completed successfully.

PS C:\Users\logger> net localgroup "Event Log Readers"
Alias name     Event Log Readers
Comment        Members of this group can read event logs from local machine

Members

-------------------------------------------------------------------------------
logger
The command completed successfully.


PS C:\Users\logger>  wevtutil qe Security /rd:true /f:text | Select-String "/user

        Process Command Line:   cmdkey  /add:WEB01 /user:amanda /pass:Passw0rd!
        Process Command Line:   net  use Z: \\DB01\scripts /user:mary 
        Process Command Line:   net  use T: \\fs01\backups /user:tim MyStr0ngP@ss


