# Python Network Sniffer

A lightweight, basic network packet sniffer written in Python using the `scapy` library. This tool captures live network traffic, dissects the packets, and displays key information such as source and destination IP addresses, transport layer protocols (TCP/UDP), port numbers, and snippets of the raw payload data.

## Features
*   **Live Packet Capture:** Intercepts network traffic in real-time.
*   **Protocol Parsing:** Automatically identifies and extracts data from IPv4, TCP, and UDP layers.
*   **Payload Inspection:** Extracts and previews the first 60 characters of the raw application data payload.
*   **Memory Efficient:** Discards packets after processing to prevent memory overflow during extended capture sessions.

## Prerequisites
*   Python 3.x
*   Administrative/root privileges (required for putting the network interface into promiscuous mode).
*   Kali Linux (recommended) or any Debian-based distribution.

## Installation

On Kali Linux, it is recommended to install `scapy` via the system package manager rather than `pip` to avoid environment conflicts.

1. Clone the repository:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/python-network-sniffer.git](https://github.com/YOUR_USERNAME/python-network-sniffer.git)
   cd python-network-sniffer
