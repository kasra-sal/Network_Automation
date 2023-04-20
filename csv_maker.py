#!/usr/bin/python

import csv

	
with open('roles/automation/CSV/sl2.csv','w',newline='') as file:
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
	
with open('roles/automation/CSV/Unused_Ports.csv','w',newline='') as file:
	writer = csv.writer(file)
	writer.writerow(["id","device","interface"])
	writer.writerow(["1","DLS1","g0/2-3, g1/3, g3/0-2"])
	writer.writerow(["2","DLS2","g0/2-3, g1/3, g3/0-2"])
	writer.writerow(["3","CLS1","g1/1-3, g3/0-2"])
	writer.writerow(["4","CLS2","g1/1-3, g3/0-2"])	
	file.close()	

with open('roles/automation/CSV/SVI.csv','w',newline='') as file:
	writer = csv.writer(file)
	writer.writerow(["id","device","vlan_id","ip_address"])
	writer.writerow(["1","DLS1","20,30,40,50","10.0.20.253, 10.0.30.253, 10.0.40.253, 10.0.50.253"])
	writer.writerow(["2","DLS2","20,30,40,50","10.0.20.252, 10.0.30.252, 10.0.40.252, 10.0.50.252"])
	writer.writerow(["3","ALS1","20,30,40,50","10.0.20.251, 10.0.30.251, 10.0.40.251, 10.0.50.251"])
	writer.writerow(["4","ALS2","20,30,40,50","10.0.20.250, 10.0.30.250, 10.0.40.250, 10.0.50.250"])
	file.close()	


with open('roles/automation/CSV/access_ports.csv','w',newline='') as file:
	writer = csv.writer(file)
	writer.writerow(["id","interface","vlan_id","voice"])
	writer.writerow(["1","g2/0-1","30",""])
	writer.writerow(["2","g0/0-3","20",""])
	writer.writerow(["3","g2/2-3","","40"])
	writer.writerow(["4","g3/0-1","50",""])
	file.close()
	
with open('roles/automation/CSV/trunk_ports.csv','w',newline='') as file:
	writer = csv.writer(file)
	writer.writerow(["id","device","interface","allowed_vlans","native_vlan","trunk_mode"])
	writer.writerow(["1","DLS1","g1/2","20,30,40,50,99","1000","dynamic desirable"])
	writer.writerow(["2","DLS2","g1/2","20,30,40,50,99","1000","dynamic desirable"])
	writer.writerow(["3","ALS1","g1/2","20,30,40,50,99","1000","dynamic auto"])
	writer.writerow(["4","ALS2","g1/2","20,30,40,50,99","1000","dynamic auto"])
	file.close()	

with open('roles/automation/CSV/loopback.csv','w',newline='') as file:
	writer = csv.writer(file)
	writer.writerow(["id","device","loopback_add","loopback_id"])
	writer.writerow(["1","CLS1","192.168.254.1","0"])
	writer.writerow(["2","CLS1","172.16.1.1","1"])
	writer.writerow(["3","CLS2","192.168.254.2","0"])
	writer.writerow(["4","CLS2","172.16.1.2","1"])
	writer.writerow(["5","DLS1","192.168.254.3","0"])
	writer.writerow(["6","DLS2","192.168.254.4","0"])
	writer.writerow(["7","ALS1","192.168.254.5","0"])
	writer.writerow(["8","ALS2","192.168.254.6","0"])
	file.close()
	
with open('roles/automation/CSV/etherchannel_ports.csv','w',newline='') as file:
	writer = csv.writer(file)
	writer.writerow(["id","layer","device","interface","allowed_vlans","native_vlan","trunk_mode","mode","ip_address","subnetmask","portchannel_id"])
	writer.writerow(["1","2","DLS1","g1/0-1","20,30,40,50,99","1000","dynamic desirable","desirable","","","5"])
	writer.writerow(["2","2","DLS2","g1/0-1","20,30,40,50,99","1000","dynamic desirable","desirable","","","6"])
	writer.writerow(["3","2","ALS1","g1/0-1","20,30,40,50,99","1000","dynamic auto","auto","","","5"])
	writer.writerow(["4","2","ALS2","g1/0-1","20,30,40,50,99","1000","dynamic auto","auto","","","6"])
	writer.writerow(["5","2","DLS1","g0/0-1","20,30,40,50,99","1000","dynamic desirable","desirable","","","7"])
	writer.writerow(["6","2","DLS2","g0/0-1","20,30,40,50,99","1000","dynamic desirable","desirable","","","7"])
	writer.writerow(["7","3","CLS1","g0/0-3","","","","desirable","10.168.1.1","255.255.255.252","1"])
	writer.writerow(["8","3","CLS2","g0/0-3","","","","desirable","10.168.1.2","255.255.255.252","1"])
	writer.writerow(["9","3","DLS1","g2/0-1","","","","desirable","10.168.0.2","255.255.255.252","2"])
	writer.writerow(["10","3","DLS2","g2/0-1","","","","desirable","10.168.0.5","255.255.255.252","3"])
	writer.writerow(["11","3","CLS1","g2/0-1","","","","desirable","10.168.0.1","255.255.255.252","2"])
	writer.writerow(["12","3","CLS2","g2/0-1","","","","desirable","10.168.0.6","255.255.255.252","3"])
	writer.writerow(["13","3","DLS1","g2/2-3","","","","desirable","10.168.0.9","255.255.255.252","4"])
	writer.writerow(["14","3","DLS2","g2/2-3","","","","desirable","10.168.0.13","255.255.255.252","5"])
	writer.writerow(["15","3","CLS1","g2/2-3","","","","desirable","10.168.0.14","255.255.255.252","5"])
	writer.writerow(["16","3","CLS2","g2/2-3","","","","desirable","10.168.0.10","255.255.255.252","4"])
	file.close()	
	
with open('roles/automation/CSV/HSRP.csv','w',newline='') as file:
	writer = csv.writer(file)
	writer.writerow(["id","device","svi_id","standby_id","virtual_address","preempt","priority"])
	writer.writerow(["1","DLS1","20,30,40,50","2,3,4,5","10.0.20.254, 10.0.30.254, 10.0.40.254, 10.0.50.254","yes","100,90,100,90"])
	writer.writerow(["2","DLS2","20,30,40,50","2,3,4,5","10.0.20.254, 10.0.30.254, 10.0.40.254, 10.0.50.254","yes","90,100,90,100"])	
	file.close()	

with open('roles/automation/CSV/spanning_tree.csv','w',newline='') as file:
	writer = csv.writer(file)
	writer.writerow(["id","device","mode","associated_vlan","priority"])
	writer.writerow(["1","DLS1","rapid-pvst","20,30,99,1000","4096"])
	writer.writerow(["2","DLS2","rapid-pvst","40,50","4096"])
	writer.writerow(["3","DLS1","rapid-pvst","40,50","8192"])
	writer.writerow(["4","DLS2","rapid-pvst","20,30","8192"])
	file.close()

with open('roles/automation/CSV/OSPF.csv','w',newline='') as file:
	writer = csv.writer(file)
	writer.writerow(["id","device","interface","passive_interface","router_id","area","ospf_id"])
	writer.writerow(["1","DLS1","port-channel 2, port-channel 4, loopback 0","","10.1.1.10","0","20"])
	writer.writerow(["2","DLS2","port-channel 3, port-channel 5, loopback 0","","10.2.2.10","0","20"])
	writer.writerow(["3","CLS1","port-channel 2, port-channel 5, loopback 0","loopback 1","1.1.1.1","0","20"])
	writer.writerow(["4","CLS2","port-channel 3, port-channel 4, loopback 0","loopback 1","2.2.2.2","0","20"])
	writer.writerow(["5","DLS1","vlan 50, loopback 0","vlan 20, vlan 30, vlan 40, vlan 70, vlan 99, vlan 1000","10.1.1.10","20","20"])
	writer.writerow(["6","DLS2","vlan 50, loopback 0","vlan 20, vlan 30, vlan 40, vlan 70, vlan 99, vlan 1000","10.2.2.10","20","20"])
	file.close()

'''
with open('roles/Vlan/CSV/mgmt_csv.csv','w',newline='') as file:
	writer = csv.writer(file)
	writer.writerow(["id","vlan_id","name"])
	writer.writerow(["1","10","Server"])
	writer.writerow(["2","20","office"])
	writer.writerow(["6","70","native"])	
	writer.writerow(["7","99","management"])	
	file.close()
	
	
	'''
