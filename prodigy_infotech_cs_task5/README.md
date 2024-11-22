README.md for GitHub

```markdown
# Network Packet Analyzer Tool

This project is a **Network Packet Analyzer Tool** designed to capture and analyze network traffic in real-time. Built using Python and the Scapy library, the tool extracts and logs details such as source and destination IP addresses, protocol type, and payload data.

---

Features

- Real-Time Packet Capture:
  - Captures network packets directly from the network interface.
  
- Detailed Analysis:
  - Extracts and displays:
    - Source and destination IP addresses.
    - Protocol type (TCP, UDP, ICMP).
    - Packet payload.

- Logging:
  - Outputs analyzed packet information to both the console and a text file (`network packet analyser_output.txt`).

---

How It Works

1. Packet Capture:
   - Uses the `scapy.sniff` function to capture network packets.
   
2. Protocol Identification:
   - Maps protocol numbers to human-readable names (e.g., TCP, UDP, ICMP).

3. Output:
   - Packet information is displayed on the console and saved to a log file.

---

Requirements

- Python 3.x
- Scapy library

Install Scapy
To install Scapy, run:
```bash
pip install scapy
```

---

Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/network-packet-analyzer.git
   cd network-packet-analyzer
   ```

2. Run the tool with administrator privileges:
   ```bash
   sudo python network_packet_analyser.py
   ```

3. The tool will start capturing packets and display the output in the console. It will also save packet details to the `network packet analyser_output.txt` file.

---

Output Example

```plaintext
Source IP: 192.168.1.5
Destination IP: 142.250.190.14
Protocol: TCP
Payload: Raw data (truncated for clarity)
--------------------------------------------------

Source IP: 192.168.1.1
Destination IP: 192.168.1.5
Protocol: UDP
Payload: Raw data (truncated for clarity)
--------------------------------------------------
```

---

Notes

- Permissions:
  - Packet sniffing typically requires root or administrator privileges.
  
- Ethical Use:
  - This tool is for educational purposes only. Ensure you have permission to capture traffic on the network you are analyzing.

---

License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

Contribution

Contributions are welcome! Feel free to fork the repository and submit a pull request.
