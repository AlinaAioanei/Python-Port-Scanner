# Python Port Scanner

Project Overview

This is my first cybersecurity portfolio project: a Python-based TCP port scanner built from scratch.

The purpose of this project is to improve my understanding of networking, TCP ports, Python socket programming, and basic network reconnaissance.

The scanner allows the user to enter an IP address or hostname and choose a range of ports to scan. When an open port is detected, the program displays the port number together with information about common services where available.

## Technologies Used

* Python 3
* Python `socket` module
* Visual Studio Code
* macOS
* Git and GitHub

## Features

The scanner can:

* Accept an IP address or hostname as a target
* Resolve hostnames to IP addresses
* Scan a user-selected TCP port range
* Detect open TCP ports
* Identify common services associated with ports
* Validate port numbers
* Display the number of open ports found
* Measure the total scan time
* Display the date and time of the scan
* Handle invalid input and connection errors

## Port Ranges

TCP/UDP port numbers range from **0 to 65535**.

For this project, I learned about the main port categories:

* **Well-known ports:** 0–1023
* **Registered ports:** 1024–49151
* **Dynamic/Private ports:** 49152–65535

The scanner accepts ports from **1 to 65535**.

Examples of Common Ports

| Port | Service | Purpose                   |
| ---- | ------- | ------------------------- |
| 21   | FTP     | File transfer             |
| 22   | SSH     | Secure remote access      |
| 23   | Telnet  | Unencrypted remote access |
| 25   | SMTP    | Email transmission        |
| 53   | DNS     | Domain name resolution    |
| 80   | HTTP    | Web traffic               |
| 110  | POP3    | Email retrieval           |
| 143  | IMAP    | Email access              |
| 443  | HTTPS   | Secure web traffic        |
| 3389 | RDP     | Windows Remote Desktop    |

## How to Run

Make sure Python 3 is installed.

Run:

```bash
python3 port_scanner.py
```

## The program will ask for:

1. An IP address or hostname
2. A starting port
3. An ending port

The scanner will then test the selected TCP ports and report any open ports it finds.

## Testing and Screenshots

I tested the scanner in a controlled environment using devices and systems that I own or have permission to test.

## The testing process includes:

1.Localhost scan (127.0.0.1) across ports 1–1024

2.Detection of an intentionally opened HTTP test server on port 8080

3.Larger port-range scan across ports 1–10000

Screenshots of the tests are available in the `screenshots` folder.

## What I Learned

Through this project I developed a better understanding of:

* TCP ports and network services
* IP addresses and hostnames
* Python socket programming
* Basic network reconnaissance
* Error and input handling
* Port ranges and common network services
* Using GitHub to document cybersecurity projects

This project also helped me understand how port scanning can be used by security professionals to identify exposed network services.

## Ethical Use

This project is for educational and cybersecurity learning purposes only.

Port scanning should only be performed against systems and networks that you own or have explicit permission to test.

## Future Improvements

Future versions could include:

* Faster scanning using multithreading
* Improved service detection
* Exporting scan results to a file
* Command-line arguments
* Improved logging and reporting
* Comparison with tools such as Nmap

---

**Cybersecurity Portfolio – Project 1**
