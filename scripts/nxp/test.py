import requests
import time
import json
import sys

led_ok = 0
gsensor_ok = 0
button_ok = 0

#for i in sys.argv:
#    print (i)
#print (sys.argv[1])
# argc
argc = len(sys.argv)
#print (argc)
basic_url = 'http://{ip}/cgi/'.format(ip=sys.argv[1])
request_url = ''
print (request_url)
if argc != 2:
	print ("Input Parameter Error")
	print ("Format: python test.py <ip>")
	print ("e.g: python test.py 192.168.200.13")
	sys.exit()
else:
	print ("[Verkada Pitbull Test] Start")

print ("------LED EVENT------")
cgi='led_test'
request_url = ''
request_url += basic_url
request_url += cgi
response = requests.get(request_url)
print('Server Response :{text}'.format(text=response.text))
print('')

#JSON PARSER
led_ret = json.loads(response.text)
#print (led_ret['state'])
if led_ret['state'] == 'SUCCESS':
	led_ok = 1

time.sleep(5)

print ("------G-sensor EVENT------")
cgi='gsensor_test'
request_url = ''
request_url += basic_url
request_url += cgi
response = requests.get(request_url)
print('Server Response :{text}'.format(text=response.text))
print('')

#JSON PARSER
gsensor_ret = json.loads(response.text)
#print (gsensor_ret['state'])
if gsensor_ret['state'] == 'SUCCESS':
	gsensor_ok = 1
	
time.sleep(5)


print ("------Button EVENT 1st------")
cgi='button_check'
request_url = ''
request_url += basic_url
request_url += cgi
response = requests.get(request_url)
print('Server Response :{text}'.format(text=response.text))

#JSON PARSER
button_1st = json.loads(response.text)
#print (button_1st['state'])

times=5
for i in range(times):
	temp = 'Please press the button in {count} sec..'.format(count=times-i)
	print (temp)
	time.sleep(1)

print('')
print ("------Button EVENT 2nd------")
response = requests.get(request_url)
print('Server Response :{text}'.format(text=response.text))
print('')

#JSON PARSER
button_2nd = json.loads(response.text)
#print (button_2nd['val'])
time.sleep(5)

if button_1st['state'] == 'SUCCESS' and button_2nd['state'] == 'SUCCESS':
	if button_2nd['val'] > button_1st['val']:
		button_ok = 1

if led_ok == 0:
	print ("[LED Test] failed")
	
if gsensor_ok == 0:
	print ("[G-sensor Test] failed")	

if button_ok == 0:
	print ("[Button Test] failed")
	
if led_ok == 1 and gsensor_ok == 1 and button_ok == 1:
	print ("All testing items are ok")
else :
	print ("Part of testing items failed, please try again.")
	
print ("[Verkada Pitbull Test] Done")
sys.exit()