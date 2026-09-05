with open("targets.txt", "r") as file:
    target_port = file.read().strip()
for port in target_port.split("\n") :
    port = int(port.strip())
    if port <= 1024 :
        print(f"Port {port} is system privileged port...")
    else :
        print(f"Port {port} is user port...")
    