from scapy.all import *
import random

# Define destination IP
dst_ip = "192.168.204.136"
# Define source port
source_port = 2911
# Total number of packets 
total_packets = 800  # 

for _ in range(total_packets):
  # Randomly choose TCP or DNS
  if random.randint(0, 1) == 0:
    # TCP packet (modify data)
    packet = IP(src=RandIP(), dst=dst_ip)/TCP(sport=source_port, dport=80)/Raw(load="Sample Data - TCP")
  else:
    # DNS packet (modify question)
    random_name = f"www.random-{random.randint(1000,9999)}.com"
    packet = IP(src=RandIP(), dst=dst_ip)/UDP(sport=source_port, dport=53)/DNS(rd=1, qd=DNSQR(qname=random_name, qtype="A"))
  # Send the packet directly
  send(packet)
print(f"Sent {total_packets} mixed TCP and DNS packets to {dst_ip} from source port {source_port}")
