- **WordPress Exploitation & RCE:** Brute-forced WordPress admin credentials (`ilfreightwp`) using WPScan, logged into the dashboard, and injected a PHP reverse shell payload into the `404.php` template of the Twenty Twenty theme to establish a netcat listener shell as `www-data`.
    
- **Database Enumeration via SQLi:** Ran SQLMap against a vulnerable tracking/status endpoint to target the `status` database, dumping the contents and recovering user credentials including the "Flag" user record.
    
- **XSS Cookie Hijacking:** Identified a vulnerability in the support ticket message field (`ticket.php`), set up a local PHP server (`0.0.0.0:9000`), and injected an XSS payload via an external script to capture the administrator's session cookie (`session=fcfaf93ab169bc943b92109f0a845d99`).
    
- **SSRF / XSS to Local File Read:** Exploited an input field in the tracking feature that rendered injected JavaScript in generated PDFs, using an `XMLHttpRequest` payload (`file:///flag.txt`) to extract the final flag.