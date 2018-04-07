#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import threading, os

def run_node(param):
    os.system(cmd + param)  

# def run_node(i):
    # os.system(cmd + node_list[i]) 

cmd = 'java -jar C:\\Users\\Han\\selenium_test\\selenium-server-standalone-3.11.0.jar -role '
# node_list = ['hub', 'node', 'node -port 5556','node -port 5557']
node_list = ['hub', 'node -port 5556','node -port 5557']
for i in range(len(node_list)):
    # class threading.Thread(group=None, target=None, name=None, args=(), kwargs={}, *, daemon=None)
    # args=() -> tuple -> need ","
    t = threading.Thread(target=run_node,args=(node_list[i],))
    # t = threading.Thread(target=run_node,args=(i,))
    t.start()

# 1. start selenium server hub and node on localhost
# localhost windows(192.168.2.41) VMware Network Adapter VMnet1(192.168.91.1):
# (C:\Users\Han\Anaconda3) C:\Users\Han\selenium_test\ch09>python run_selenium-server.py
# 15:39:08.704 INFO [GridLauncherV3.launch] - Selenium build info: version: '3.11.0', revision: 'e59cfb3'
# 15:39:08.719 INFO [GridLauncherV3$3.launch] - Launching a Selenium Grid node on port 5557
# 15:39:08.737 INFO [GridLauncherV3.launch] - Selenium build info: version: '3.11.0', revision: 'e59cfb3'
# 15:39:08.754 INFO [GridLauncherV3$2.launch] - Launching Selenium Grid hub on port 4444
# 15:39:08.784 INFO [GridLauncherV3.launch] - Selenium build info: version: '3.11.0', revision: 'e59cfb3'
# 15:39:08.791 INFO [GridLauncherV3$3.launch] - Launching a Selenium Grid node on port 5556 

# 2. start selenium server node on remote ubuntu 16
# remote ubuntu 16(192.168.157.130):
# han@han-virtual-machine:~$ java -jar selenium-server-standalone-3.11.0.jar -role node -port 5555 -hub http://192.168.2.41:4444/grid/register

# http://localhost:4444/grid/console

# 3. launch python script
# (C:\Users\Han\Anaconda3) C:\Users\Han\selenium_test\ch09>python local_hub_remote_node_2.py
# http://127.0.0.1:5556/wd/hub chrome
# http://127.0.0.1:5557/wd/hub firefox
# http://192.168.157.130:5555/wd/hub firefox
