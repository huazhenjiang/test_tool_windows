@echo off
setlocal

set val_revision=DVT
set val_sn=F97G-4D67-E7W6
set val_mac=02:12:13:10:15:11
set val_manufacturing_done=0
set val_part_number=60-420001-R1

set configs={\"Event\":\"WRITE_EEPROM\",\"HW_Revision\":\"%val_revision%\",\"SN\":\"%val_sn%\",\"MAC\":\"%val_mac%\",\"Manufacturing_done\":%val_manufacturing_done%,\"Part_number\":\"%val_part_number%\"}
echo %0 Start.
echo Host:%1
echo "Set data as %configs%"

curl.exe -s -X POST -H "Content-Type: application/json" -H "Accept: application/json" --data "%configs%" http://%1/cgi/set_eeprom
echo.
echo.
rem 'delay 5s'
@ping 127.0.0.1 -n 5 -w 1000 > nul
for /f "tokens=1" %%i in ('curl.exe -s -X GET -H "Accept: application/json" http://%1/cgi/get_eeprom') do set ret=%%i
echo "Read data: %ret%"

echo.
echo %0 Done.


endlocal
