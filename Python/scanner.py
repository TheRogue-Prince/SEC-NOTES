target_ip = input("Enter the target IP address: ")
port_list = input("Enter the ports you want to scan (comma-separated): ").split(",")


for port in port_list:
    port = int(port.strip())
    print(f"checking {target_ip}:{port}...")
    if port ==80:
        print(f"port {port} is secure web service ")
        with open("results.txt", "a") as file:
            file.write(f"port {port} is web service \n")

    elif port == 443:
        print(f"port {port} is secure web service ")
        with open("results.txt", "a") as file:
            file.write(f"port {port} is secure web service \n")
    else :
        print(f"port {port} is not a web service ")
        with open("results.txt", "a") as file:
            file.write(f"port {port} is not a web service \n")

