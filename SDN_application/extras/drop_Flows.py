#!/usr/bin/env python
import httplib
import json
  
class StaticFlowPusher(object):
  
    def __init__(self, server):
        self.server = server
  
    def get(self, data):
        ret = self.rest_call({}, 'GET')
        return json.loads(ret[2])
  
    def set(self, data):
        ret = self.rest_call(data, 'POST')
        return ret[0] == 200
  
    def remove(self, objtype, data):
        ret = self.rest_call(data, 'DELETE')
        return ret[0] == 200
  
    def rest_call(self, data, action):
        path = '/wm/staticflowpusher/json'
        headers = {
            'Content-type': 'application/json',
            'Accept': 'application/json',
            }
        body = json.dumps(data)
        conn = httplib.HTTPConnection(self.server, 8080)
        conn.request(action, path, body, headers)
        response = conn.getresponse()
        ret = (response.status, response.reason, response.read())
        print ret
        conn.close()
        return ret
  
pusher = StaticFlowPusher('127.0.0.1')
  

# Rule: switch drop any packets coming from (X.X.X.X)

#pusher.remove(json, flow1)
def get_ip(mali_node):
    ip = '10.0.0.'+mali_node
    return ip

def get_dpid(mac_mali_node):
    dpid = '00:00:00:00:00:00:00:'+mac_mali_node
    return dpid

def get_name(node_id):
    _name = 'drop-flow-'+node_id
    return _name    

def manipulate_flows(choice):
    if choice == 1:
        mali_node = raw_input("Enter last IP number: \n")
        mac_mali_node = raw_input("Enter last DPID number: \n")
        ip = get_ip(mali_node)
        dpid = get_dpid(mac_mali_node)
        _name = get_name(mali_node)
        print("\n ",dpid, ip, _name)
        conf = input("*** Adding Rule\n Confirm with 1: \n")
        if conf == 1:
            pusher.set({'switch':dpid,"name":_name,"eth_type":"0x0800","ipv4_src":ip,"active":"true"})
        else : print("*** No changes made ***")

    elif choice == 2:
        mali_node = raw_input("Enter last IP number: \n")
        mac_mali_node = raw_input("Enter last DPID number: \n")
        ip = get_ip(mali_node)
        dpid = get_dpid(mac_mali_node)
        _name = get_name(mali_node)
        print("\n ",dpid, ip, _name)
        conf = input("*** Deleting Rule\n Confirm with 1: \n")
        if conf == 1:
            pusher.remove(json, {'switch':dpid,"name":_name,"eth_type":"0x0800","ipv4_src":ip,"active":"true"})
        else : print("*** No changes Made ***")

    else: print("**** Gues You are just bored ****")


try:
    choice = input("Enter 1: Set rule\nEnter 2: Remove rule\n")
    manipulate_flows(choice)
except Exception:
    print("[*] Wrong input [*]")




