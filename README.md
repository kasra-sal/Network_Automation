# Network Automation

The goal of this project is to automate configuration of switches and routers using ansible. This project is used to demonstrate basic understanding of ansible and jinja. This project was NOT intended to show knowledge of networking, although basic networking has been done to make this project functional.

# Before We Start

This repository contains necessary yaml files to perform this basic automation. HOWEVER, I decided to not use some of the built in modules such as ios.ios.l2_interfaces to configure as it somewhat limited what I had planned. So I just generated my own csv files and used jinja to import necessary variables into a config format to allow more customizability. It's worth noting a few things:
  -  The contents in the repo are a base point of what could be done, feel free to take ideas and improve it.
  -  This is not an educational project for networking, it is intended to illustrate how you could send configs manually or through pipelines.
  -  The devices are hosted on gns3 vm, you will need to acquire ios qemus through purchasing license from cisco modeling labs.
  -  You may want to host the topology on a server or cloud for better performance and scalability, as 12 cores will not be enough to handle more than what's already implemented.

# Getting started

## Prerquisites
- Git
- Ansible
- GNS3
- VMware or Virtualbox
- vios and vios_l2 images 

## Git Installation

Download the git installer from [Git](https://git-scm.com/downloads) follow the installation steps to install git on your device. If you are using linux, use the following inside terminal:
```
git --version 
```
If the output shows git with a version, then skip the Git installation section as you already have git installed.

If git was not installed, do the following:
```
sudo apt-get update; sudo apt-get install git -y
```
or if you are using an Arch-based distro:
```
sudo pacman -Sy git
```
## Ansible Installation

Please refere to this [link](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html) to install Ansible

## VMware or VirtualBox Installation
To install [VMware](https://kb.vmware.com/s/article/2057907) or [VirtualBox](https://www.virtualbox.org/manual/ch02.html), use corresponding links.

## GNS3 Installation
To install GNS3 and GNS3VM use this [link](https://docs.gns3.com/docs/getting-started/installation/linux/).

## Vios Images
To acquire Vios images, you need to purchase CML license. Use this [link](https://learningnetworkstore.cisco.com/cisco-modeling-labs-personal/cisco-modeling-labs-personal/CML-PERSONAL.html).

# Cloning this repository

Use the following command to clone this repository
```
git clone https://github.com/kasra-sal/Network_Automation.git
```

# Topology Diagrams
To gain a better understanding of what we will be doing, I made topology diagrams. Use them as reference point.
![Untitled design(1)](https://user-images.githubusercontent.com/118489496/233561963-0d085855-e409-495d-8f75-935fced588b1.png)




# Initializing Configs for Remote Management
To start using ansible to remotely configure each node, I created a base config initialized that will configure ssh, rsa keys, domain name, necessary addresses on interfaces to be able to remotely manage it. Here is an example output :

## Router:
```
en
 conf t
 hostname Router1
 interface g0/3
 ip address 192.168.1.10 255.255.255.0
 no shutdown
 exit
 ip name-server 8.8.8.8
 ip domain-name homelab.com
 crypto key generate rsa
 2048
 ip ssh version 2
 username admin privilege 15 secret PaSsWoRd
 line vty 0 15
 transport input ssh
 login local
 ```
## Switch:
```
en
 conf t
 hostname Switch1
 interface vlan 99
 ip address 192.168.1.1 255.255.255.0
 no shutdown
 exit
 int g3/3
 switchport trunk encap dot1q
 switchport mode trunk
 switchport trunk native vlan 99
 ip default-gateway 192.168.1.254
 ip name-server 8.8.8.8
 ip domain-name homelab.com
 crypto key generate rsa
 2048
 ip ssh version 2
 username admin privilege 15 secret PaSsWoRd
 line vty 0 15
 transport input ssh
 login local
```

This template should be more than sufficient to get us started. 

# Configuring Ansible for Remote Management
Once we pushed necessary configs for the switches and routers, we can configure ansible with the following commands:
inside your ansible.cfg file, type in the following command if it doesn't already exist
```
[defaults]
host_key_checking = False
``` 
It's important to know that, this change should ONLY be implemented in a lab environment. 
After we have configured the ansible.cfg, change the directory to the project directory and run the following commands:
```
cd Network_Automation
ansible switch -m ping -i inventory.yml
```
This will use the module ping to test connectivity to the switches. If everything is correct, it will respond with "pong"
![Screenshot from 2023-04-21 03-03-19](https://user-images.githubusercontent.com/118489496/233564810-4bbdf14c-5236-47ef-b033-ff54dc734ff1.png)

To run the playbook provided, use the following command:
```
ansible-playbook site.yml -i inventory.yml
```
It may take a while to go through, for the sake of simplicity, I will not be explaining how each file is being pulled and exactly where but I will give a brief description of how it's done:
1. CSV file is generated through "csv_maker.py". I could've done it directly through excel but oh oops.
2. Added an entry to main.yml inside respective roles folder => tasks.
3. Inside the template folde, I created a jinja template respective to the csv
4. Back into main.yml inside tasks folder, I added an entry to replace necessary parameters inside the jinja template and then push them to the device using ios_config modules.


https://user-images.githubusercontent.com/118489496/233573072-e1bf80ba-2b43-40c4-966a-f2b4c1eb6b7d.mp4


To have a better understanding of what each jinja template does, I screenshotted some of the outputs: (Need to be Finished)

VLAN
Unused Ports
STP
SVI
HSRP
OSPF

TFTP and config pulling needs to be added
