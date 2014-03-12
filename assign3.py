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
	 
	if server_detail != None:
	    credentials = get_credentials()
	    neutron = client.Client(**credentials)
	 
	    body_value = {
		             "port": {
		                     "admin_state_up": True,
		                     "device_id": server_id,
		                     "name": "port1",
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

option = 0

while option != 3:
	print "1. Create Port\n2. List Ports\n3. Exit"
	option = int(raw_input())

	if option == 1:
		create_a_port()
	elif option == 2:
		list_the_ports()
	else:
		break
