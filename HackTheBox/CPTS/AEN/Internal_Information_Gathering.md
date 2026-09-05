
```
showmount -e <target_ip>
```

```
root@dmz01:/tmp/DEV01# mount -t nfs 172.16.8.20:/DEV01 .

```


```
root@dmz01:/tmp/DEV01/DNN# cat web.config
<?xml version="1.0"?>
<configuration>
  <!--
    For a description of web.config changes see http://go.microsoft.com/fwlink/?LinkId=235367.

    The following attributes can be set on the <httpRuntime> tag.
      <system.Web>
        <httpRuntime targetFramework="4.6.2" />
      </system.Web>
  -->
  <username>Administrator</username>
  <password>
        <value>D0tn31Nuk3R0ck$$@123</value>
  </password>
  <system.web>
    <compilation debug="true" targetFramework="4.5.2"/>
    <httpRuntime targetFramework="4.5.2"/>
  </system.web>
</configuration>root@dmz01:/tmp/DEV01/DNN# 

```


