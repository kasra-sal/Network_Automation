#!/usr/bin/python

import csv

	
with open('roles/Layer2/CSV/sl2.csv','w',newline='') as file:
	writer = csv.writer(file)
	writer.writerow(["id","vlan_id","name"])
	writer.writerow(["1","20","office"])
	writer.writerow(["2","30","accounting"])
	writer.writerow(["3","40","voip"])
	writer.writerow(["4","50","guest"])
	writer.writerow(["5","70","unused_ports"])
	writer.writerow(["6","1000","native"])	
	writer.writerow(["7","99","management"])	
	file.close()	
	
with open('roles/Layer2/CSV/Unused_Ports.csv','w',newline='') as file:
	writer = csv.writer(file)
	writer.writerow(["id","device","interface"])
	writer.writerow(["1","DLS1","g0/0-3, g1/2-3, g3/0-2"])
	writer.writerow(["2","DLS2","g0/0-3, g1/2-3, g3/0-2"])
	writer.writerow(["3","DLS3","g0/0-3, g1/0-1, g3/0-2"])
	writer.writerow(["4","DLS4","g0/0-3, g1/0-1, g3/0-2"])
	writer.writerow(["5","CLS1","g2/1-3, g3/0-2"])
	writer.writerow(["6","CLS2","g2/1-3, g3/0-2"])
	writer.writerow(["7","ALS1","g3/2"])
	writer.writerow(["8","ALS2","g3/2"])	
	file.close()	

with open('roles/Layer2/CSV/SVI.csv','w',newline='') as file:
	writer = csv.writer(file)
	writer.writerow(["id","device","vlan_id","ip_address"])
	writer.writerow(["1","DLS1","20,30,40,50","10.0.20.253, 10.0.30.253, 10.0.40.253, 10.0.50.253"])
	writer.writerow(["2","DLS2","20,30,40,50","10.0.20.252, 10.0.30.252, 10.0.40.252, 10.0.50.252"])
	writer.writerow(["3","ALS1","20,30,40,50","10.0.20.251, 10.0.30.251, 10.0.40.251, 10.0.50.251"])
	writer.writerow(["4","DLS3","20,30,40,50","10.1.20.253, 10.1.30.253, 10.1.40.253, 10.1.50.253"])
	writer.writerow(["5","DLS4","20,30,40,50","10.1.20.252, 10.1.30.252, 10.1.40.252, 10.1.50.252"])
	writer.writerow(["6","ALS2","20,30,40,50","10.1.20.250, 10.1.30.250, 10.1.40.250, 10.1.50.250"])
	file.close()	


with open('roles/Layer2/CSV/access_ports.csv','w',newline='') as file:
	writer = csv.writer(file)
	writer.writerow(["id","interface","vlan_id","voice"])
	writer.writerow(["1","g1/0-1","30",""])
	writer.writerow(["2","g0/0-3","20",""])
	writer.writerow(["3","g1/2-3","","40"])
	writer.writerow(["4","g3/0-1","50",""])
	file.close()
	


with open('roles/Layer2/CSV/etherchannel_ports.csv','w',newline='') as file:
	writer = csv.writer(file)
	writer.writerow(["id","layer","device","interface","allowed_vlans","native_vlan","trunk_mode","mode","ip_address","subnetmask","portchannel_id"])
	writer.writerow(["1","3","CLS1","g0/0-3","","","","desirable","172.128.10.1","255.255.255.252","1"])
	writer.writerow(["2","3","CLS2","g0/0-3","","","","desirable","172.128.10.2","255.255.255.252","1"])

	writer.writerow(["1","2","DLS1","g2/0-1","20,30,40,50,99","1000","dynamic desirable","desirable","","","2"])
	writer.writerow(["2","2","DLS2","g2/0-1","20,30,40,50,99","1000","dynamic desirable","desirable","","","2"])
	writer.writerow(["1","2","DLS3","g2/0-1","20,30,40,50,99","1000","dynamic desirable","desirable","","","5"])
	writer.writerow(["2","2","DLS4","g2/0-1","20,30,40,50,99","1000","dynamic desirable","desirable","","","5"])

	writer.writerow(["1","2","DLS1","g2/2-3","20,30,40,50,99","1000","dynamic desirable","desirable","","","3"])
	writer.writerow(["2","2","DLS2","g2/2-3","20,30,40,50,99","1000","dynamic desirable","desirable","","","4"])
	writer.writerow(["1","2","DLS3","g2/2-3","20,30,40,50,99","1000","dynamic desirable","desirable","","","6"])
	writer.writerow(["2","2","DLS4","g2/2-3","20,30,40,50,99","1000","dynamic desirable","desirable","","","7"])
	
	writer.writerow(["3","2","ALS1","g2/0-1","20,30,40,50,99","1000","dynamic auto","auto","","","3"])
	writer.writerow(["4","2","ALS2","g2/0-1","20,30,40,50,99","1000","dynamic auto","auto","","","6"])
	writer.writerow(["3","2","ALS1","g2/2-3","20,30,40,50,99","1000","dynamic auto","auto","","","4"])
	writer.writerow(["4","2","ALS2","g2/2-3","20,30,40,50,99","1000","dynamic auto","auto","","","7"])
	file.close()	
	
	
with open('roles/Layer2/CSV/HSRP.csv','w',newline='') as file:
	writer = csv.writer(file)
	writer.writerow(["id","device","svi_id","standby_id","virtual_address","preempt","priority"])
	writer.writerow(["1","DLS1","20,30,40,50,99","2,3,4,5,9","10.0.20.254, 10.0.30.254, 10.0.40.254, 10.0.50.254, 192.168.1.254","yes","100,90,100,90,100"])
	writer.writerow(["2","DLS2","20,30,40,50,99","2,3,4,5,9","10.0.20.254, 10.0.30.254, 10.0.40.254, 10.0.50.254, 192.168.1.254","yes","90,100,90,100,90"])	
	writer.writerow(["1","DLS3","20,30,40,50,99","2,3,4,5,9","10.1.20.254, 10.1.30.254, 10.1.40.254, 10.1.50.254, 192.168.1.254","yes","100,90,100,90,100"])
	writer.writerow(["2","DLS4","20,30,40,50,99","2,3,4,5,9","10.1.20.254, 10.1.30.254, 10.1.40.254, 10.1.50.254, 192.168.1.254","yes","90,100,90,100,90"])
	file.close()	

with open('roles/Layer2/CSV/spanning_tree.csv','w',newline='') as file:
	writer = csv.writer(file)
	writer.writerow(["id","device","mode","associated_vlan","priority"])
	writer.writerow(["1","DLS1","rapid-pvst","20,30,99,1000","4096"])
	writer.writerow(["2","DLS2","rapid-pvst","40,50","4096"])
	writer.writerow(["3","DLS1","rapid-pvst","40,50","8192"])
	writer.writerow(["4","DLS2","rapid-pvst","20,30","8192"])
	writer.writerow(["1","DLS3","rapid-pvst","20,30,99,1000","4096"])
	writer.writerow(["2","DLS4","rapid-pvst","40,50","4096"])
	writer.writerow(["3","DLS3","rapid-pvst","40,50","8192"])
	writer.writerow(["4","DLS4","rapid-pvst","20,30","8192"])
	file.close()

with open('roles/Layer3/CSV/OSPF.csv','w',newline='') as file:
	writer = csv.writer(file)
	writer.writerow(["id","device","interface","router_id","area","ospf_id"])
	writer.writerow(["1","DLS1","loopback 9 , vlan 99 , g1/0-1","10.1.1.10","0","20"])
	writer.writerow(["2","DLS2","loopback 9 , vlan 99 , g1/0-1","10.2.2.10","0","20"])
	writer.writerow(["1","DLS3","loopback 9 , vlan 99 , g1/2-3","10.3.3.10","0","20"])
	writer.writerow(["2","DLS4","vlan 99 , loopback 9 , g1/2-3","10.4.4.10","0","20"])
	writer.writerow(["3","CLS1","vlan 99 , port-channel 1, g1/0-3, g2/0","1.1.1.1","0","20"])
	writer.writerow(["4","CLS2","vlan 99 , port-channel 1, g1/0-3","2.2.2.2","0","20"])
	writer.writerow(["5","DLS1","vlan 20 , vlan 30 , vlan 40 , vlan 50 , loopback 1","10.1.1.10","10","20"])
	writer.writerow(["6","DLS2","vlan 20 , vlan 30 , vlan 40 , vlan 50 , loopback 1","10.2.2.10","10","20"])
	writer.writerow(["5","DLS3","vlan 20 , vlan 30 , vlan 40 , vlan 50 , loopback 1","10.3.3.10","30","20"])
	writer.writerow(["6","DLS4","vlan 20 , vlan 30 , vlan 40 , vlan 50 , loopback 1","10.4.4.10","30","20"])
	writer.writerow(["5","MGMT1","g3/3","99.99.99.99","0","20"])
	writer.writerow(["5","MGMT1","vlan 99","99.99.99.99","0","20"])
	file.close()


with open('roles/Layer3/CSV/BGP.csv','w',newline='') as file:
	writer = csv.writer(file)
	writer.writerow(["id","device","neighbor","as","remote_as","network","password"])
	writer.writerow(["1","CLS2","128.100.0.2","65001","65002","","homelab"])
	writer.writerow(["2","R1","128.100.0.1","65002","65001","100.1.1.9 255.255.255.255,172.16.1.7 255.255.255.255","homelab"])
	file.close()

