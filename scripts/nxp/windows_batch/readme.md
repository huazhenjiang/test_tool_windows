### 簡介
本資料夾下所有windows batch script目的只用來在Windows OS上,採用curl指令的方式,對裝置下CGI進行測試

### 使用方式
1. 開始→打開命令列
2. 進入bat所在的資料夾
3. 確認資料夾內有curl.exe, jq-win64.exe, libcurl-x64.dll
4. 打開command line，進入本資料夾的路徑

#### Pitbull_For_SMT.bat
自動測試Pitbull_For_SMT
1. 執行Pitbull_For_SMT.bat <HOST IP>
	- e.g. F:\curl\curl_x64\bin>Pitbull_For_SMT.bat 192.168.200.18

Note:執行結果可參閱附圖Pitbull_SMT.png

#### write_eeprom_configs.bat
修改裝置內的EEPROM的內容值
1. 打開並編輯 write_eeprom_configs.bat, 在對應的項目中填入對應的值
2. 執行write_eeprom_configs.bat <HOST IP>
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
