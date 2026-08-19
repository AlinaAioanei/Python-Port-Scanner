import socket
import time
from datetime import datetime


# Common TCP ports and their explanations
COMMON_PORTS = {
    20: ("FTP Data", "Transfers files through the FTP data channel"),
    21: ("FTP", "File Transfer Protocol control service"),
    22: ("SSH", "Secure remote login and administration"),
    23: ("Telnet", "Unencrypted remote terminal access"),
    25: ("SMTP", "Transfers email between mail servers"),
    53: ("DNS", "Translates domain names into IP addresses"),
    80: ("HTTP", "Unencrypted website or web server"),
    110: ("POP3", "Retrieves email from a mail server"),
    111: ("RPCbind", "Maps remote procedure call services"),
    135: ("MS RPC", "Microsoft Remote Procedure Call service"),
    139: ("NetBIOS", "Windows file and printer sharing"),
    143: ("IMAP", "Accesses and manages email on a server"),
    161: ("SNMP", "Monitors and manages network devices"),
    389: ("LDAP", "Directory and identity service"),
    443: ("HTTPS", "Encrypted website or web server"),
    445: ("SMB", "Windows file and printer sharing"),
    465: ("SMTPS", "Secure email transfer"),
    514: ("Syslog", "Transfers system and network logs"),
    587: ("SMTP Submission", "Email submission by mail clients"),
    631: ("IPP", "Network printing service"),
    636: ("LDAPS", "Secure directory service"),
    993: ("IMAPS", "Secure IMAP email access"),
    995: ("POP3S", "Secure POP3 email retrieval"),
    1433: ("Microsoft SQL Server", "Microsoft database service"),
    1521: ("Oracle Database", "Oracle database service"),
    1883: ("MQTT", "Messaging service commonly used by IoT devices"),
    2049: ("NFS", "Network File System"),
    3306: ("MySQL", "MySQL database service"),
    3389: ("RDP", "Microsoft Remote Desktop service"),
    5432: ("PostgreSQL", "PostgreSQL database service"),
    5900: ("VNC", "Remote graphical desktop access"),
    6379: ("Redis", "In-memory database and cache"),
    8080: ("HTTP Alternate", "Alternative web server"),
    8443: ("HTTPS Alternate", "Alternative secure web server")
}


print("=" * 60)
print("PYTHON PORT SCANNER")
print("Cybersecurity Portfolio - Project 1")
print("=" * 60)

target = input("Enter an IP address or hostname: ").strip()

start_port_text = input("Enter start port (default 1): ").strip()
end_port_text = input("Enter end port (default 1024): ").strip()

start_port = int(start_port_text) if start_port_text else 1
end_port = int(end_port_text) if end_port_text else 1024


try:

    if start_port < 1 or end_port > 65535:
        print("Ports must be between 1 and 65535.")

    elif start_port > end_port:
        print("The start port cannot be greater than the end port.")

    else:

        ip = socket.gethostbyname(target)

        open_ports = []

        print(f"\nResolved IP: {ip}")
        print(f"Scanning ports {start_port} to {end_port}...\n")

        print(
            f"{'PORT':<10}"
            f"{'NAME':<25}"
            f"{'PURPOSE':<55}"
            f"{'STATUS'}"
        )

        print("-" * 100)

        start_time = time.time()

        for port in range(start_port, end_port + 1):

            sock = socket.socket(
                socket.AF_INET,
                socket.SOCK_STREAM
            )

            sock.settimeout(0.5)

            result = sock.connect_ex((ip, port))

            if result == 0:

                if port in COMMON_PORTS:
                    name, purpose = COMMON_PORTS[port]

                else:
                    name = "Unknown"
                    purpose = "General network service"

                open_ports.append(
                    (port, name, purpose)
                )

                print(
                    f"{port:<10}"
                    f"{name:<25}"
                    f"{purpose:<55}"
                    f"OPEN"
                )

            sock.close()

        end_time = time.time()
        scan_time = end_time - start_time

        print("-" * 100)

        if open_ports:
            print(f"\nOpen ports found: {len(open_ports)}")
        else:
            print("\nNo open ports found.")

        print(
            f"Scan completed in {scan_time:.2f} seconds"
        )

        print(
            "Scan date:",
            datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )


except socket.gaierror:
    print("Error: Hostname could not be resolved.")

except KeyboardInterrupt:
    print("\nScan stopped by user.")

except ValueError:
    print("Error: Please enter valid port numbers.")

except Exception as error:
    print(f"Error: {error}")