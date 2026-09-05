import socket

ip = input("Enter the IP address to scan: ")
port = int(input("Enter the port to scan: "))

def test_single_port(ip, port):
    # 1. Create a network socket (like picking up the phone)
    s = socket.socket()
    
    # 2. Set a timeout so we don't wait forever if the port is closed
    s.settimeout(1.0)
    
    # 3. Try to connect to the IP and Port

    # connect_ex returns 0 if the connection succeeds!
    result = s.connect_ex((ip, port))
    
    if result == 0:
        print(f"[+] Port {port} is OPEN!")
    else:
        print(f"[-] Port {port} is closed.")
        
    # 4. Close the socket connection
    s.close()
test_single_port(ip, port)