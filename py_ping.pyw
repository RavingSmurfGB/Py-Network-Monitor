import os, time, re
from datetime import datetime


##########################################[TO DO]##########################################
#
# Add in support for split tunnel vpn
#   Look in to using power shell commands in python
#       check for vpn adapter via python
#       install vpn adapter using powershell script
#   Check if VPN adapter is installed
#   Install it if not
#   set it to launch by defualt 
#   use DNS name for my MX

# Work on ping logging
#   Store 6 months worth of logs
#       store month logs in seperate files
#       delete anythin that is older
#   Store whether the Ip was last reachable in a dictionary with the IP                         Done
#       only log on successfull ping if previous ping was unsuccessfull                         Done
#       only log on unsuccessfull ping if previous was not successfull                          Done

# Ping 
#   Use threading for ping checks
#   Check for current active IP and add it to the ip_dictionary
#   Check for the current defualt gateway and add it to the ip_dictionary
#   Check arp table for ip address if recieved failed responde
#       Then log accorgingly

# DNS 
#   Try to do a nslookup for google, yahoo etc..
#       only log on not connect if previous log was connect
#       only log on connect if previous was not connect


##########################################




##########################################[ISSUES]##########################################
#

##########################################




OS_TYPE = os.name
# Sets the count modifier to the os type
COUNT = '-n' if OS_TYPE == 'nt' else '-c'

#ip_list = ["127.0.0.1", "192.168.3.200", "192.168.3.1", "1.1.1.1", "Google.com", "192.168.3.205"]
#ip_list = ["192.168.3.245"]


ip_dictionary = { #Creates an dictionary with all the ip addresses needed and whether they are currently reachable
    "127.0.0.1" : False,
    "192.168.3.200" : True,
    "192.168.3.1" : True,
    "1.1.1.1" : True,
    "8.8.8.8" : True,
    "192.168.3.205" : True
}
ip_list = [*ip_dictionary] # Selects only the keys from the dictionary, for use in pinging


response = os.popen(f"route print").read()

#print(response)

#if "0.0.0.0" in response:


list_response = response.splitlines()

#print(list_response)


for line in list_response:
    if '0.0.0.0' in line:
        print (line)



txt = "The rain in Spain"
x = re.search("^0.0.0.0$", str(list_response))

if x:
  print("YES! We have a match!")
else:
  print("No match")



print(re.findall("0.0.0.0", str(list_response)))


'''
dataLog = []
with open('results.txt', 'rt') as f:
    data = f.readlines()
for line in data:
    if line.__contains__('Unsuccessful'):
        print(line)
        dataLog.append(line)
print(dataLog)
'''

'''
##########################################[Ping Logic & logging]##########################################
while True:
    for ip in ip_list:
        response = os.popen(f"ping {ip} {COUNT} 1").read()
        #print(ip_dictionary)
        dt_string = datetime.now().strftime("%d/%m/%Y %H:%M:%S") #set's the date and time to now



        ##### SUCCESSFULL PING
        if "Received = 1" in response and "Approximate" in response: #If there is the string "Received = 0" in the response then do:
            print(f"UP {ip} Ping Successful")
            for ip_dict, bool_dict in ip_dictionary.items(): # Iterates through ip_dictionary and assigns ip_dict to key and bool_dict to value
                

                ##### SUCCESSFULL PING & PREVIOUSLY SUCCESFULL
                if ip == ip_dict and bool_dict == True: # If recieved response from ping & last ping was succesfull then:
                    ip_dictionary[ip] = True # set current IP in dictionary to True, as ping was succesfull
                    print(ip + str(bool_dict))


                ##### SUCCESSFULL PING & PREVIOUSLY UNSUCCESSFULL
                elif ip == ip_dict and bool_dict == False: # If recieved response from ping & last ping was not succesfull then:
                    ip_dictionary[ip] = True # set current IP in dictionary to True, as ping was succesfull
                    print(ip + str(bool_dict))
                    with open("results.txt", "a") as file: #open's the file to allow it to be written to
                        file.write(dt_string + f" -- UP {ip} Ping Successful" + "\n")# writes to log, includes date/tim
                    


            
        ##### UNSUCCESSFULL PING
        else: ## need to implement not successgull correctly like above
            print(f"Down {ip} Ping Unsuccessful")
            for ip_dict, bool_dict in ip_dictionary.items(): # Iterates through ip_dictionary and assigns ip_dict to key and bool_dict to value


                ##### UNSUCCESSFULL PING & PREVIOUSLY SUCCESFULL
                if ip == ip_dict and bool_dict == True: # If did not recieve response from ping & last ping was succesfull then:
                    ip_dictionary[ip] = False # set current IP in dictionary to False, as ping was unsuccesfull
                    print(ip + str(bool_dict))
                    with open("results.txt", "a") as file: #open's the file to allow it to be written to
                        file.write(dt_string + f" -- Down {ip} Ping Unsuccessful" + "\n") #writes to log, includes date/time


                ##### UNSUCCESSFULL PING & PREVIOUSLY UNSUCCESSFULL
                elif ip == ip_dict and bool_dict == False: # If did not recieve response from ping & last ping was not succesfull then:
                    ip_dictionary[ip] = False # set current IP in dictionary to False, as ping was unsuccesfull
                    print(ip + str(bool_dict))


        time.sleep(2)

##########################################
'''






''' Based on
https://github.com/labeveryday/ping_script/blob/master/tool.py
'''