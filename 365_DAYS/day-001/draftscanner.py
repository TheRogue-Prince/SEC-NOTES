# The function/tool
def scan_service(service_name):
    print(f"[*] Checking {service_name}...")
    
    # Logic to check for vulnerabilities
    if service_name == "Old_SSH_v1":
        print("[CRITICAL] Vulnerable to remote code execution!")
    elif service_name == "Apache_v2.4":
        print("[WARNING] Outdated version detected.")
    else:
        print("[+] Service appears secure.")

# A list of services discovered on a target network
discovered_services = ["Apache_v2.4", "Secure_Shell_v9", "Old_SSH_v1"]

# The loop running the tool on every service
for service in discovered_services:
    scan_service(service)