from neutronclient.v2_0 import client
import novaclient.v1_1.client as nvclient
from credentials import get_credentials
from utils import print_values_server
from credentials import get_nova_credentials
from credentials import get_credentials
from utils import print_values


nova_credentials = get_nova_credentials()
nova_client = nvclient.Client(**nova_credentials)
neutron_credentials = get_credentials()
neutron = client.Client(**neutron_credentials)


def create_a_port():
	server_id= 'f9dec530-f163-4965-8aab-bfc43c955566'
	network_id= '17087163-a2a2-48d6-b26a-f1db86c0612a'
	server_detail = nova_client.servers.get(server_id)
	print server_detail.id
	print "Enter the name"
	name1 = raw_input();
	 
	if server_detail != None:
	    credentials = get_credentials()
	    neutron = client.Client(**credentials)
	 
	    body_value = {
		             "port": {
		                     "admin_state_up": True,
		                     "device_id": server_id,
		                     "name": name1,
		                     "network_id": network_id
		              }
		         }
	    response = neutron.create_port(body=body_value)
	    print response
	return

def list_the_ports():
	ports = neutron.list_ports()
	print print_values(ports, 'ports')
	return

def displayPortInfo()
	print "Enter the port id of the port"
	port_id = raw_input()
	syscall = "neutron --os-username admin --os-password kalyani345 --os-tenant-name admin --os-auth-url http://172.16.139.128:5000/v2.0 port-show " + port_id + ""
	os.system(syscall)
	return

def changeName()
	print "Enter the port id of the port: "
	port_id = raw_input()
	print "Enter the name that you want to give the port: "
	name = raw_input()
	syscall = "neutron --os-username admin --os-password kalyani345 --os-tenant-name admin --os-auth-url http://172.16.139.128:5000/v2.0 port-update " + port_id + " --name" + name + ""
	os.system(syscall)
	return

option = 0

while option != 3:
	print "\n1. Create Port\n2. List Ports\n3. Display Information by Port ID\n4. Update Name of the Port"
	option = int(raw_input())

	if option == 1:
		create_a_port()
	elif option == 2:
		list_the_ports()
	elif option == 3:
		displayPortInfo()
	elif option == 4:
		changeName()
	else
		break
