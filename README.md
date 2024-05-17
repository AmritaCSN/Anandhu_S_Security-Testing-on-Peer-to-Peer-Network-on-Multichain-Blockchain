# Security-testing-on-peer-to-peer-network-on-multichain-blockchain

This projects explores security testing on multichain blockchain systems, revealing that nodes with lower computing capacity are more vulnerable to network-level attacks.

Setup
A multichain blockchain network was set up using various devices. Node 1 was a laptop with an i3 processor running Bodhi Linux, while Nodes 2 and 4 were Raspberry Pi 4 and 3B+ running Ubuntu Unity. Node 3 was a laptop with a powerful i7 processor running Bodhi Linux and was patched. Git and curl were installed for remote administration. A new blockchain was created on Node 1, and the chain parameters and network settings were configured on all nodes. Nodes 2, 3, and 4 were added to the network, and their connections were verified. Permissions for critical operations were enabled to ensure secure network governance.

# Multichain Setup
## Nodes and Specifications
- Node 1: Laptop with i3 processor running Bodhi Linux
- Node 2: Raspberry Pi 4 running Ubuntu Unity
- Node 3: Laptop with i7 processor running Bodhi Linux
- Node 4: Raspberry Pi 3B+ running Ubuntu Unity

## Software
- Bodhi Linux
- Ubuntu Unity
- Multichain


## Setup Instructions
* create a new blockchain : `multichain-util create chain1`
* start the chain : `multichaind chain1 -daemon`
* Configure Chain Parameter : `nano ~/.multichain/chain1/multichain.conf`
* Connect Additional Nodes (Nodes 2, 3, 4) : `multichaind chain1@<Node1_IP>:<port>`
* Verify Connections : `multichain-cli chain1 getinfo`
* Enable Permissions for Secure Network Governance : `multichain-cli chain1 grant <address> connect,send,receive`

# Attack on P2P Network

* DOS - A DoS attack overwhelms a network or service with excessive traffic, causing it to slow down or become unavailable. This prevents legitimate users from accessing the service.
* DDOS - A DDoS attack uses multiple compromised devices to flood a network or service with traffic, making it hard to stop. This results in severe disruptions and unavailability of the service.
* Eclipse Attack - An eclipse attack isolates a blockchain node by surrounding it with malicious nodes.
* Livness Attack - A liveness attack disrupts a blockchain network's ability to confirm transactions by preventing nodes from communicating effectively. This leads to delays and potential downtime.
* Transaction Flooding - Transaction flooding involves sending a large number of transactions to a blockchain network, causing congestion. This slows down processing time.
* Time Jacking - Time jacking manipulates a node's network time to disrupt transaction ordering and block validation. This can lead to inconsistent transaction processing and potential double-spending.
* Spatial Partitioning Attack - A spatial partitioning attack creates divisions within a blockchain network, isolating nodes and disrupting communication. 

# Implementation of Attack

* DOS
  - TCP Flooding : A TCP SYN flood attack overwhelms a server with numerous SYN requests, causing resource exhaustion, slowdowns, and potential server crashes due to high CPU and memory usage.
  - DNS Flooding : A DNS flood attack overwhelms a DNS server, causing delays and failures in domain name resolution, causing widespread disruptions and difficulty accessing websites and online services.
  [Contribution guidelines for this project](/DOS code.py)


* DDOS
  - A DDoS attack occurs when two zombie nodes, controlled by a single main node, overwhelm the network with excessive requests, disrupting normal operations and potentially compromising security.
    * The same code we used on DoS is used here with running in other nodes

* Eclipse Attack :
  We need to change the permission from
    * anyone-can-connect  	 :false
    * anyone-can-send	       :false
    * anyone-can-receive	   :false
    * anyone-can-create    	 :false
    * anyone-can-activate	   :false
    * anyone-can-admin	 	   :false 

   to the below:
    * anyone-can-connect  	 :true
    * anyone-can-send	       :true
    * anyone-can-receive	   :true
    * anyone-can-create    	 :true
    * anyone-can-activate	   :true
    * anyone-can-admin	 	   :true


* Livness Attack :
 we aim to deactivate a node by sending malicious shell code that blocks the port, rendering the node non-operational if the code is executed. This disrupts the node's ability to participate in network activities and compromises the overall system's functionality.

* Transaction Flooding: Transaction flooding as an attack involves overwhelming the blockchain network with a massive number of transactions, aiming to degrade its performance and disrupt normal operations. The code for sending transaction is above

* Time Jacking: Time jacking involves manipulating the system time on each node to create discrepancies and then initiating two transactions to check the timestamp logs. This attack tests whether inconsistent times across nodes can be exploited to gain an advantage or cause errors. However, modern blockchain protocols have safeguards against such attacks, making time jacking ineffective.

* Spatial Partitioning Attack: A Spatial Partitioning Attack, which attempts to divide the network into isolated segments, is not possible in MultiChain because only one node can be isolated at a time. Because of this limitation, partitioning the entire network is impossible, making the attack ineffective.


