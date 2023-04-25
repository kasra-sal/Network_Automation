# Network Automation

The aim of this project is to utilize Ansible and Jinja to automate the configuration of switches and routers. It serves as a means to demonstrate a fundamental comprehension of these technologies. While basic networking knowledge was applied to make the project functional, the project itself was not intended to showcase networking expertise.

# Before We Start

Please note that this repository comprises the essential YAML files needed to execute this basic automation. However, it is important to mention that certain built-in modules, such as ios.ios.l2_interfaces, were not employed due to limitations that would have constrained the desired outcome. Instead, custom CSV files were generated and Jinja was utilized to import necessary variables into a configuration format, providing more flexibility. It's worth noting a few things:
  -  The contents in the repo are a base point of what could be done, feel free to take ideas and improve it.
  -  This is not an educational project for networking, it is intended to illustrate how you could send configs manually or through pipelines.
  -  The devices are hosted on gns3 vm, you will need to acquire ios qemus through purchasing license from cisco modeling labs.
  -  You may want to host the topology on a server or cloud for better performance and scalability, as 12 cores will not be enough to handle more than what's already implemented.

# Table of Contents
- [Getting started](#getting-started)
  * [Prerquisites](#prerquisites)
  * [Git Installation](#git-installation)
  * [Ansible Installation](#ansible-installation)
  * [VMware or VirtualBox Installation](#vmware-or-virtualbox-installation)
  * [GNS3 Installation](#gns3-installation)
  * [Vios Images](#vios-images)
- [Cloning this repository](#cloning-this-repository)
- [Topology Diagrams](#topology-diagrams)
- [Initializing Configs for Remote Management](#initializing-configs-for-remote-management)
  * [Router Initial Config](#router-)
  * [Switch Initial Config](#switch-)
- [Configuring Ansible for Remote Management](#configuring-ansible-for-remote-management)
- [Jinja Template Outputs](#jinja-template-outputs)
  * [VLAN](#vlan)
  * [Unused Ports](#unused-ports)
  * [STP](#stp)
  * [SVI](#svi)
  * [HSRP](#hsrp)
  * [OSPF](#ospf)
- [TFTP](#tftp)


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
To gain a better understanding of what we will be doing, I made topology diagrams. Use them as reference point. (Click to zoom in)

![Topology](https://user-images.githubusercontent.com/118489496/234165650-331bf932-a669-4fae-9560-7b0b3fbf6faa.png)

Here is my initial hand drawn draft:
![Hand_Drawn_Topology](https://user-images.githubusercontent.com/118489496/234173833-86b5ff00-a78e-4fe8-9b1c-818f970453e5.jpg)


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
It's important to know that, this change should ONLY be implemented in a lab environment as it poses a securirty risk by using weaker encryption for key pairing. 
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
The process of generating the CSV file and utilizing it for remote configuration is outlined below, with a brief description of each step:

1. A CSV file is created using "csv_maker.py". Although Excel could have been used, this script was utilized instead.
2. An entry is added to main.yml within the respective roles folder => tasks.
3. A Jinja template is created in the template folder that corresponds to the CSV file.
4. In main.yml within the tasks folder, an entry is added to replace the necessary parameters within the Jinja template and then push them to the device using the ios_config modules.

Keep in mind that due to virtualization limitations, you may need to wait for longer period of time for the config to go through. If you receive "Timeout" error, increase timeout time for that specific task.

# Jinja Template Outputs

To keep this section short, I've only included 1 template output for each task.
Here is what some of the Jinja templates will output:

## VLAN
DLS1 :
```
{% if inventory_hostname in groups['distribution'] or inventory_hostname in groups['access'] %}
{% for i in vlan_list %}
  vlan {{ i.vlan_id }}
  name {{i.name }}
{% endfor %}
{% endif %}
```
```
vlan 20
name office
vlan 30
name accounting
vlan 40
name voip
vlan 50
name guest
vlan 70
name unused_ports
vlan 1000
name native
vlan 99
name management
```

## Unused Ports
DLS1:  
```
{% for i in unused_list %}
  {% if inventory_hostname == i.device %}
  {% if skip_loop is not defined or not skip_loop %}
  interface range {{ i.interface }}
  switchport mode access
  switchport access vlan 70
  shutdown
  {% if loop.first %}{% set skip_loop = True %}{% endif %}
  {% endif %}
  {% endif %}
{% endfor %}

```
```
interface range g0/0-3, g1/2-3, g3/0-2
switchport mode access
switchport access vlan 70
shutdown
```

## STP
DLS1: Template
```
{% if inventory_hostname in groups['distribution'] or inventory_hostname in groups['access'] %}
spanning-tree mode rapid-pvst
spanning-tree portfast edge default
{% for i in stp_list %}
  {% if inventory_hostname == i.device %}
  {% if skip_loop is not defined or not skip_loop %}
  {% set associated_vlan = i.associated_vlan.split(',') %}
  {% for index in range(associated_vlan|length) %}
    spanning-tree vlan {{ associated_vlan[index] }} priority {{ i.priority }}
  {% endfor %}
  {% else %}
  {% if loop.first %}{% set skip_loop = True %}{% endif %}
  {% endif %}
  {% endif %} 
{% endfor %}
{% endif %}
```
Output:
```
spanning-tree mode rapid-pvst
spanning-tree portfast edge default
spanning-tree vlan 20 priority 4096
spanning-tree vlan 30 priority 4096
spanning-tree vlan 99 priority 4096
spanning-tree vlan 1000 priority 4096
spanning-tree vlan 40 priority 8192
spanning-tree vlan 50 priority 8192
```

## SVI
DLS1: Template
```
{% for i in svi_list %}
  {% if inventory_hostname == i.device %}
  {% if skip_loop is not defined or not skip_loop %}
  {% set vlan_id = i.vlan_id.split(',') %}
  {% set ip_address = i.ip_address.split(',') %}
  {% for index in range(vlan_id|length) %}
    interface vlan{{ vlan_id[index] }}
    ip address {{ ip_address[index] }} 255.255.255.0
    no shutdown
  {% endfor %}
  {% endif %}
  {% endif %}
{% endfor %}
```
Output:
```
interface vlan20
ip address 10.0.20.253 255.255.255.0
no shutdown
interface vlan30
ip address  10.0.30.253 255.255.255.0
no shutdown
interface vlan40
ip address  10.0.40.253 255.255.255.0
no shutdown
interface vlan50
ip address  10.0.50.253 255.255.255.0
no shutdown
```
## HSRP
DLS1: Template
```
{% if inventory_hostname in groups['distribution'] %}
{% for i in hsrp_list %}
  {% if inventory_hostname == i.device %}
  {% if skip_loop is not defined or not skip_loop %}
  {% set svi_id = i.svi_id.split(',') %}
  {% set standby_id = i.standby_id.split(',') %}
  {% set priority = i.priority.split(',') %}
  {% set virtual_address = i.virtual_address.split(',') %}
  {% for index in range(svi_id|length) %}
    interface vlan{{ svi_id[index] }}
    standby version 2
    standby {{ standby_id[index] }} ip {{ virtual_address[index] }} 
    standby {{ standby_id[index] }} preempt
    standby {{ standby_id[index] }} priority {{ priority[index] }}
  {% endfor %}
  {% endif %}
  {% endif %}
{% endfor %}
{% endif %}
```
Output:
```
interface vlan20
standby version 2
standby 2 ip 10.0.20.254 
standby 2 preempt
standby 2 priority 100
interface vlan30
standby version 2
standby 3 ip  10.0.30.254 
standby 3 preempt
standby 3 priority 90
interface vlan40
standby version 2
standby 4 ip  10.0.40.254 
standby 4 preempt
standby 4 priority 100
interface vlan50
standby version 2
standby 5 ip  10.0.50.254 
standby 5 preempt
standby 5 priority 90
interface vlan99
standby version 2
standby 9 ip  192.168.1.254 
standby 9 preempt
standby 9 priority 100
```
## OSPF

CLS1: Template
```
{% set configured_hosts =[] %}
{% for i in ospf_list %}
  {% if inventory_hostname == i.device %}
  {% if inventory_hostname not in configured_hosts %}
  ip routing
  ipv6 unicast-routing
  router ospfv3 {{ i.ospf_id }}
  {% if item.redistribute is defined %}
  address-family ipv4 
  redistribute bgp 65001 metric-type 2
  exit
  {% endif%}
  router-id {{ i.router_id }}
  passive-interface default
  interface range {{ i.interface }}
  ipv6 enable
  ospfv3 {{ i.ospf_id }} ipv4 area {{ i.area }}
  no shutdown
  {{ configured_hosts.append(inventory_hostname) }}
  {% elif inventory_hostname in configured_hosts %}
  interface range {{ i.interface }}
  ipv6 enable
  ospfv3 {{ i.ospf_id }} ipv4 area {{ i.area }}
  no shutdown
  {% endif %}
  {% endif %}
{% endfor %}
```
Output:
```
ip routing
ipv6 unicast-routing
router ospfv3 20
router-id 1.1.1.1
passive-interface default
interface range vlan 99 , port-channel 1, g1/0-3, g2/0
ipv6 enable
ospfv3 20 ipv4 area 0
no shutdown
```

# TFTP
Although there are choices like sftp, I decided to keep it simple since this is just a lab. So I just configured my server and connected it to the same lan as the topology. 

Here is the screen shot of configs being pulled from the devices:
![Screenshot from 2023-04-24 18-12-52](https://user-images.githubusercontent.com/118489496/234131171-e6bd5219-55a1-42bb-ba9d-40202ea34bf0.png)
![Screenshot from 2023-04-24 18-12-38](https://user-images.githubusercontent.com/118489496/234131175-67c49563-5245-4951-aef8-2663533ef620.png)




