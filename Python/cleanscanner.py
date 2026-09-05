target_ip = input("Enter the target IP address: ")
port_list = input("Enter the ports you want to scan (comma-separated): ").split(",")

# Open the file ONCE before the loop starts using append mode ("a")
with open("results.txt", "a") as file:
    file.write(f"\n--- Scan Results for {target_ip} ---\n")

    for port in port_list:
        port = int(port.strip())
        print(f"checking {target_ip}:{port}...")

        if port == 80:
            msg = f"port {port} is web service\n"
            print(msg.strip())
            file.write(msg)

        elif port == 443:
            msg = f"port {port} is secure web service\n"
            print(msg.strip())
            file.write(msg)

        else:
            msg = f"port {port} is not a web service\n"
            print(msg.strip())
            file.write(msg)

print("[+] Scan complete! Results saved to results.txt")