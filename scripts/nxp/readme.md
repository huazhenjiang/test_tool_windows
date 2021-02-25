### How to use the testing python script:
1. Install python3, and check the firmware version(commit 5afc23b)
2. Make sure the device connecting to the same LAN with your testing PC
3. Find the ip address of the device that you want to test.
	- To find the ip in LAN, you can use iw2 or check the logs from debug console

Note : The avaiable version worked on LPC54606 only.

#### test.py
1. input the command such as the following:
	- python test.py 192.168.200.13

If worked, it should look like the following:
~~~
[Verkada Pitbull Test] Start
------LED EVENT------
Server Response :{"state":"SUCCESS","val":0,"info":"Check LED"}

------G-sensor EVENT------
Server Response :{"state":"SUCCESS","val":196,"info":"G-sensor val"}

------Button EVENT 1st------
Server Response :{"state":"SUCCESS","val":5,"info":"Button count"}
Please press the button in 5 sec..
Please press the button in 4 sec..
Please press the button in 3 sec..
Please press the button in 2 sec..
Please press the button in 1 sec..

------Button EVENT 2nd------
Server Response :{"state":"SUCCESS","val":6,"info":"Button count"}

All testing items are ok
[Verkada Pitbull Test] Done
~~~

If failed, it should look like the following:
~~~
[Verkada Pitbull Test] Start
------LED EVENT------
Server Response :{"state":"SUCCESS","val":0,"info":"Check LED"}

------G-sensor EVENT------
Server Response :{"state":"SUCCESS","val":236,"info":"G-sensor val"}

------Button EVENT 1st------
Server Response :{"state":"SUCCESS","val":6,"info":"Button count"}
Please press the button in 5 sec..
Please press the button in 4 sec..
Please press the button in 3 sec..
Please press the button in 2 sec..
Please press the button in 1 sec..

------Button EVENT 2nd------
Server Response :{"state":"SUCCESS","val":6,"info":"Button count"}

[Button Test] failed
Part of testing items failed, please try again.
[Verkada Pitbull Test] Done
~~~


#### Reference
1. Verkada 按鍵專案 (SoC: NXP LPC54016JBD100 )
   https://confluence.vivotek.com/pages/viewpage.action?pageId=279058756