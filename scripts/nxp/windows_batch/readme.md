### ²��
����Ƨ��U�Ҧ�windows batch script�ت��u�ΨӦbWindows OS�W,�ĥ�curl���O���覡,��˸m�UCGI�i�����

### �ϥΤ覡
1. �}�l�����}�R�O�C
2. �i�Jbat�Ҧb����Ƨ�
3. �T�{��Ƨ�����curl.exe, jq-win64.exe, libcurl-x64.dll
4. ���}command line�A�i�J����Ƨ������|

#### Pitbull_For_SMT.bat
�۰ʴ���Pitbull_For_SMT
1. ����Pitbull_For_SMT.bat <HOST IP>
	- e.g. F:\curl\curl_x64\bin>Pitbull_For_SMT.bat 192.168.200.18

Note:���浲�G�i�Ѿ\����Pitbull_SMT.png

#### write_eeprom_configs.bat
�ק�˸m����EEPROM�����e��
1. ���}�ýs�� write_eeprom_configs.bat, �b���������ؤ���J��������
2. ����write_eeprom_configs.bat <HOST IP>
	- e.g. F:\curl\curl_x64\bin>write_eeprom_configs.bat 192.168.200.18

If worked, it should look like the following:
~~~
write_eeprom_configs.bat Start.
Host:192.168.200.18
"Set data as {\"Event\":\"WRITE_EEPROM\",\"HW_Revision\":\"DVT\",\"SN\":\"F97G-4D67-E7W6\",\"MAC\":\"02:12:13:10:15:11\",\"Manufacturing_done\":1,\"Part_number\":\"60-420001-R1\"}"
{"state":"SUCCESS","val":0,"info":"SetEEPROM_OK"}

"Read data: {"state":"SUCCESS","val":0,"HW_Revision":"DVT","SN":"F97G-4D67-E7W6","MAC":"02:12:13:10:15:11","Manufacturing_done":1,"Part_number":"60-420001-R1"}"

write_eeprom_configs.bat Done.
~~~
