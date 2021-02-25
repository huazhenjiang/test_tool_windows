import requests
import time
import json
import sys

Script_Name='Verkada Pitbull Write EEPROM'
#parameter
val_revision='DVT'
val_sn='F97G-4D67-E7W6'
val_mac='02:12:13:10:15:11'
val_manufacturing_done=0
val_part_number='60-420001-R1'

write_eeprom_ok = 0
read_eeprom_ok = 0
argc = len(sys.argv)
ip=sys.argv[1]
basic_url = 'http://{ip}/cgi/'.format(ip=sys.argv[1])
request_url = ''

if argc != 2:
	print ("Input Parameter Error")
	print ("Format: python set_eeprom.py <ip>")
	sys.exit()
else:
	print('[%s] Start'%(Script_Name))

#WRITE EEPROM
print ("------WRITE EEPROM EVENT------")
cgi='set_eeprom'
request_url = ''
request_url += basic_url
request_url += cgi

body = '{"Event":"WRITE_EEPROM","HW_Revision":"%s","SN":"%s","MAC":"%s","Manufacturing_done":%d,"Part_number":"%s"}'%(val_revision,val_sn,val_mac,val_manufacturing_done,val_part_number)
print(body)

headers = {
'Content-Type':'application/json; charset=UTF-8',
}
response = requests.post(url=request_url,data =body,headers=headers)
#print(response.text)

print('Server Response :{text}'.format(text=response.text))
print('')

#JSON PARSER
set_eeprom_ret = json.loads(response.text)
#print (set_eeprom_ret['state'])
if set_eeprom_ret['state'] == 'SUCCESS':
	write_eeprom_ok = 1

time.sleep(5)

#READ EEPROM
print ("------READ EEPROM EVENT------")
cgi='get_eeprom'
request_url = ''
request_url += basic_url
request_url += cgi

response = requests.get(request_url)
print('Server Response :{text}'.format(text=response.text))
print('')

#JSON PARSER
get_eeprom_ret = json.loads(response.text)
#print (get_eeprom_ret['state'])
if get_eeprom_ret['state'] == 'SUCCESS':
	read_eeprom_ok = 1

if write_eeprom_ok == 0:
	print ("[WRITE EEPROM] failed")

if read_eeprom_ok == 0:
	print ("[READ EEPROM] failed")

if write_eeprom_ok == 1 and read_eeprom_ok == 1:
	print ("All testing items are ok")
else :
	print ("Part of testing items failed, please try again.")

print('[%s] Done'%(Script_Name))
sys.exit()
