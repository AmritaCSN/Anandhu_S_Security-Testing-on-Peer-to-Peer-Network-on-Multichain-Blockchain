from scapy.all import *
import random

dst_ip = "192.168.204.136"
source_port = 2911
total_packets = 800  # 

for _ in range(total_packets):
  if random.randint(0, 1) == 0:
    packet = IP(src=RandIP(), dst=dst_ip)/TCP(sport=source_port, dport=80)/Raw(load="Sample Data - TCP")
  else:
    random_name = f"www.random-{random.randint(1000,9999)}.com"
    packet = IP(src=RandIP(), dst=dst_ip)/UDP(sport=source_port, dport=53)/DNS(rd=1, qd=DNSQR(qname=random_name, qtype="A"))
  send(packet)
print(f"Sent {total_packets} mixed TCP and DNS packets to {dst_ip} from source port {source_port}")
