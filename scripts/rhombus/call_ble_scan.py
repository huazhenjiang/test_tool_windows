import requests
import time
import json
import sys
import string

scan_index = 1
scan_times = 300
#for i in sys.argv:
#    print (i)
#print (sys.argv[1])
# argc
argc = len(sys.argv)
#print (argc)

#http://<ip>:8888/pt/bsa/app_discover?target_bdaddr=<BDADDR>

basic_url = 'http://{ip}:8888/pt/bsa/app_discover?target_bdaddr='.format(ip=sys.argv[1])
request_url = ''
MAC_ADDR = ''

#print ('request_url : {text}'.format(text=request_url))

def print_usage():
	print ("Input Parameter Error")
	print ("Format: python call_ble_scan.py <ip> <mac>")
	print ("e.g: python call_ble_scan.py 192.168.200.99 01:23:45:67:89:ab")
	sys.exit()
	
def split_mac(str):
	mac_addr = ''
	x = str.split(":", -1)
	for i in range(6):
		if (all(c in string.hexdigits for c in x[i])) :
			#print(x[i])	
			mac_addr += x[i]
			#print(mac_addr)
		else:
			#print('x_{text} is not hex'.format(text=i))
			print_usage()

	return mac_addr
	
if argc != 3:
	print_usage()
else:
	if len(sys.argv[2]) != 17 :
		print_usage()
	else:
		MAC_ADDR=split_mac(sys.argv[2])
		#print('MAC :{text}'.format(text=MAC_ADDR))
	
print ('To call cgi : {text}{mac}'.format(text=basic_url,mac=MAC_ADDR))

while (scan_index <= scan_times) :

	print ("[Call BLE scan] Start, Loop {text}".format(text=scan_index))
	
	request_url = ''
	request_url += basic_url
	request_url += MAC_ADDR
	#print ('To call request_url : {text}'.format(text=request_url))
	response = requests.get(request_url)
	print('Server Response :{text}'.format(text=response.text))

	#JSON PARSER
	scan_ret = json.loads(response.text)
	#print (led_ret['state'])
	if scan_ret['error_desc'] == 'success':
		print("Find the device !")
	else:
		print("Can not find the device !")

	scan_index=scan_index+1
	#time.sleep(5)

	print ("[Call BLE scan] Done")
	print('')
sys.exit()
