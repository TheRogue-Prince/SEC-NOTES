Session 1 :  Firewall and IDS/IPS Evasion

Q1. Our client wants to know if we can identify which operating system their provided machine is running on. Submit the OS name as the answer.

```
sudo nmap -sV -p 22,80,10001 10.129.127.63
Starting Nmap 7.99 ( https://nmap.org ) at 2026-08-24 11:10 +0530
Stats: 0:02:27 elapsed; 0 hosts completed (1 up), 1 undergoing Service Scan
Service scan Timing: About 66.67% done; ETC: 11:14 (0:01:13 remaining)
Nmap scan report for 10.129.127.63
Host is up (0.31s latency).

PORT      STATE SERVICE     VERSION
22/tcp    open  ssh         OpenSSH 7.6p1 Ubuntu 4ubuntu0.7 (Ubuntu Linux; protocol 2.0)
80/tcp    open  http        Apache httpd 2.4.29 ((Ubuntu))
10001/tcp open  scp-config?
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port10001-TCP:V=7.99%I=7%D=8/24%Time=6A8BD951%P=x86_64-pc-linux-gnu%r(G
SF:etRequest,1F,"220\x20HTB{pr0F7pDv3r510nb4nn3r}\r\n")%r(SIPOptions,1F,"2
SF:20\x20HTB{pr0F7pDv3r510nb4nn3r}\r\n");
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 177.65 seconds
```


Q2. After the configurations are transferred to the system, our client wants to know if it is possible to find out our target's DNS server version. Submit the DNS server version of the target as the answer.

```
 nmap -sSU -p 53 --script dns-nsid  10.129.2.48
Starting Nmap 7.99 ( https://nmap.org ) at 2026-08-24 11:39 +0530
Nmap scan report for 10.129.2.48
Host is up (0.30s latency).

PORT   STATE    SERVICE
53/tcp filtered domain
53/udp open     domain
| dns-nsid: 
|_  bind.version: HTB{GoTtgUnyze9Psw4vGjcuMpHRp}

Nmap done: 1 IP address (1 host up) scanned in 5.03 seconds

```

Q3. Now our client wants to know if it is possible to find out the version of the running services. Identify the version of service our client was talking about and submit the flag as the answer.

```
use nc to banner grab

```