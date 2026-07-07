from scapy.all import sniff, IP, TCP, UDP, Raw

def process_packet(packet):
    """
    This callback function is executed for every packet captured.
    It dissects the packet and prints the relevant information.
    """
    # 1. Check if the packet has an IP layer (Network Layer)
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        
        # 2. Check for TCP or UDP layers (Transport Layer)
        if TCP in packet:
            protocol = "TCP"
            src_port = packet[TCP].sport
            dst_port = packet[TCP].dport
        elif UDP in packet:
            protocol = "UDP"
            src_port = packet[UDP].sport
            dst_port = packet[UDP].dport
        else:
            protocol = "Other"
            src_port = "N/A"
            dst_port = "N/A"
            
        # Print the connection details
        print(f"[{protocol}] {src_ip}:{src_port} --> {dst_ip}:{dst_port}")
        
        # 3. Check if there is actual data (Payload) attached
        if Raw in packet:
            raw_data = packet[Raw].load
            # Print the first 60 characters of the payload to keep the output readable
            print(f"   Payload: {raw_data[:60]}...")
            
        print("-" * 65)

if __name__ == "__main__":
    print("Starting network sniffer... Press Ctrl+C to stop.")
    
    # Start capturing packets. 
    # prn = function to call for each packet
    # store = False prevents keeping all packets in RAM (prevents crashes over time)
    try:
        sniff(prn=process_packet, store=False)
    except KeyboardInterrupt:
        print("\nSniffing stopped by user.")
    except PermissionError:
        print("\nError: You must run this script with Administrator/Root privileges.")
