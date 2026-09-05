- **Reconnaissance & Setup:** Built a target list of subdomains for `inlanefreight.local` and ran **EyeWitness** to capture screenshots and map active web applications.
    
- **IDOR Exploitation (`careers.inlanefreight.local`):** Fuzzed the user ID parameter (`profile?id=9`) using Burp Suite Intruder to exploit an Insecure Direct Object Reference (IDOR) vulnerability, successfully retrieving a profile flag.
    
- **HTTP Verb Tampering & RCE (`dev.inlanefreight.local`):** Located `/upload.php` via directory fuzzing, bypassed access restrictions using the `TRACK` HTTP method with a custom IP authorization header, uploaded a PHP web shell, and executed commands to fetch the flag.
    
- **WordPress Vulnerability Scan (`ir.inlanefreight.local`):** Performed a WPScan on the Investor Relations site, identifying an outdated WordPress 6.0 installation, vulnerable themes, and outdated plugins like `b2i-investor-tools` and `mail-masta`.