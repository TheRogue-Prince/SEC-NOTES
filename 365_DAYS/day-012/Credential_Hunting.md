Credentials can unlock many doors for us during our assessments. We may find credentials during our privilege escalation enumeration that can lead directly to local admin access, grant us a foothold into the Active Directory domain environment, or even be used to escalate privileges within the domain. There are many places that we may find credentials on a system, some more obvious than others.

Search the file system for a file containing a password. Submit the password as your answer.

```
Get-ChildItem -Path C:\Users\ -Include *.cfg, *.config, *.ini, *.xml, *.inf, *.conf -Recurse -ErrorAction SilentlyContinue | Select-String -Pattern "password"
```

Connect as the bob user and practice decrypting the credentials in the pass.xml file. Submit the contents of the flag.txt on the desktop once you are done.

```
Get-ChildItem -Path C:\Users\ -Filter "pass.xml" -Recurse -ErrorAction SilentlyContinue

$hexString = "01000000d08c9ddf0115d1118c7a00c04fc297eb0100000016548747b77ab84f9262fa5a851d5f71000000000200000000001066000000010000200000002494ddabd3338a4fccf788171788421fefac6998b41a9c05beeb5a9a5dc39cb6000000000e8000000002000020000000736dfd85852ebbabd9d902c6450c4c51ee78f0d2e4f5c895dc1363b7178f2e0c30000000017cca90a9f8861150c51de9504bb3a3e591b85f834f8b53134f5258541fbda6ec9941ae6fa99db5e0b2e82ba0a170b04000000064b5740c7e8f2e845293abdf942e54dff0e4a563770b99e7cf9d74b6e7726143ade7ce82db92689f59291826b32098553e6b3786e3bacf4ee1af0df529b9a583"


$secureString = ConvertTo-SecureString $hexString


[System.Net.NetworkCredential]::new("", $secureString).Password




```

