@echo off
setlocal

SET ver=1.7.17
SET TodayYear=%date:~0,4%
SET TodayMonthP0=%date:~5,2%
SET TodayDayP0=%date:~8,2%
rem Extract the hour and minute from the time
set TM=%TIME:~0,2%%TIME:~3,2%
rem Zero-pad the hour if it is before 10am
set TM=%TM: =0%

set prj_name=Pitbull_SMT
set sub_name=.txt

set log=%prj_name%_%TodayMonthP0%%TodayDayP0%%TM%%sub_name%

echo "[Console]: Pitbull SMT testing Start. ver:%ver%"
echo %0 Start. > %log%
echo Host:%1 >> %log%
echo. >> %log%
IF [%1]==[] (
echo Value Missing >> %log%
echo. >> %log%
goto exit
)

echo "[Console]: Get MAC start"
for /f "tokens=1" %%i in ('curl.exe -s -X GET -H "Accept: application/json" http://%1/cgi/get_eeprom') do set ret=%%i
echo 'Devie Info:%ret%' >> %log%
echo. >> %log%
echo "[Console]: Get MAC done"

echo "[Console]: Ethernet ping test start"
echo 'Ethernet ping test' >> %log%
ping %1 >> %log%
echo. >> %log%
echo "[Console]: Ethernet ping test done"

echo "[Console]: four_color_led_test start, please check the leds"
echo 'four_color_led_test' >> %log%
for /f "tokens=1" %%i in ('curl.exe -s -X GET -H "Accept: application/json" http://%1/cgi/four_color_led_test') do set ret=%%i
echo %ret% >> %log%
echo "[Console]: four_color_led_test done"

echo. >> %log%
echo. >> %log%
@ping 127.0.0.1 -n 5 -w 1000 > nul
echo "[Console]: rj45_led_test start, please check the leds"
echo 'rj45_led_test' >> %log%
for /f "tokens=1" %%i in ('curl.exe -s -X GET -H "Accept: application/json" http://%1/cgi/rj45_led_test') do set ret=%%i
echo %ret% >> %log%
echo "[Console]: rj45_led_test done"

echo. >> %log%
echo. >> %log%
@ping 127.0.0.1 -n 5 -w 1000 > nul
echo "[Console]: G-sensor_test start"
echo 'G-sensor_test' >> %log%
for /f "tokens=1" %%i in ('curl.exe -s -X GET -H "Accept: application/json" http://%1/cgi/gsensor_test') do set ret=%%i
echo %ret% >> %log%
echo "[Console]: G-sensor_test done"

echo. >> %log%
echo. >> %log%
@ping 127.0.0.1 -n 5 -w 1000 > nul
echo "[Console]: 1st Button_check start, please press the button and check the count after 2nd Button_check"
echo '1st Button_check' >> %log%
for /f "tokens=1" %%i in ('curl.exe -s -X GET -H "Accept: application/json" http://%1/cgi/button_check') do set ret=%%i
echo %ret% >> %log%
echo "[Console]: 1st Button_check done"
echo. >> %log%
echo. >> %log%

set /a countfiles=15
:button_print_loop
echo "[Console]: please press button at %countfiles%s .."
ping 127.0.0.1 -n 2 -w 1000 > nul
set /a countfiles-=1
IF %countfiles% GTR 0 (
goto button_print_loop
)

echo "[Console]: 2nd Button_check start, check the button whether it is larger than 1st Button_check"
echo '2nd Button_check' >> %log%
for /f "tokens=1" %%i in ('curl.exe -s -X GET -H "Accept: application/json" http://%1/cgi/button_check') do set ret=%%i
echo %ret% >> %log%
echo "[Console]: 2nd Button_check done"
echo. >> %log%
echo. >> %log%

:exit
echo %0 Done. >> %log%
echo "[Console]: The log message is saved in the %log%"


endlocal
