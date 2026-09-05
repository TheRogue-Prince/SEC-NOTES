<?xml version="1.0" encoding="utf-8"?> 
<methodCall> 
  <methodName>wp.getUsersBlogs</methodName> 
  <params> 
    <param><value><string>admin</string></value></param> 
    <param><value><string>bLs6z8iv3gWpsvyeabFosDjb4YQe7jdU13rI</string></value></param> 
  </params> 
</methodCall>


curl -i -X POST https://makesense.htb/xmlrpc.php \
  -H "Content-Type: text/xml" \
  -d @rpc_check.xml \
  -k
