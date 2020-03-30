#<iplogger by Millinilliard>

ver = "1.0.0"

import time
import urllib.request

def log(entry):
    t = time.asctime(time.localtime(time.time()))
    w = str(t) + "   " + str(entry)
    print(w)
    logfile = open("ip.log", "a")
    logfile.write(w + "\n")
    logfile.close()

def error(msg):
    log("ERROR:   " + str(msg))
    
def event(msg):
    log("EVENT:   " + str(msg))
    
def update(msg):
    log("UPDATE:  " + str(msg))
    
def info(msg):
    log("INFO:    " + str(msg))
    
def init():
    event("starting iplogger version " + ver)

def AskForDelay():
    global unit
    unit = "trolololo"
    while unit != "ms" and unit != "s" and unit != "m" and unit != "h" and unit != "d":
        unit = input("Delay between checks in    INPUT:   (ms/s/min/h/d) ")
        if unit == "ms":
            multiplier = 0.001
        elif unit == "s":
            multiplier = 1
        elif unit == "min":
            multiplier = 60
        elif unit == "h":
            multiplier = 3600
        elif unit == "d":
            multiplier = 86400
        else:
            print("unit n/a")
    global delay_between_checks
    delay_between_checks = "trolololo"
    while delay_between_checks == "trolololo" or delay_between_checks < 0:
        try:
            global units
            units = int(input("Delay between checks       INPUT:   "))
            delay_between_checks = units * multiplier
            if delay_between_checks < 0:
                print("ur good... 10 seconds penalty")
                time.sleep(10)
        except Exception:
            print("Nice try... 2 seconds penalty")
            time.sleep(2)
    info("Delay between checks is " + str(units) + str(unit))
    input("Press Press <ENTER> to run iplogger")

def run():
    event("running iplogger")
    ip = 0
    while 0 == 0:
        ip = check(ip)

def check(ip):
    try:
        new_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
        if new_ip != ip:
            update("ip = " + new_ip)
            ip = new_ip
        return(ip)
    except Exception:
        error("Failed to check ip address")
    finally:
        time.sleep(delay_between_checks)
 
print("**********************************************************************")
event("opening iplogger")
print("Welcome to iplogger by Millinilliard\nwhen started and running, press <CTRL> + <C> to cancel\nopen ip.log to see the iplog")
input("Press <ENTER> to start iplogger")
try:
    init()
    AskForDelay()
    run()
except Exception as ex:
    error(ex)
finally:
    event("ending iplogger version " + ver)
    input("Press <ENTER> to close iplogger")
    event("close iplogger")
    print("**********************************************************************")
    exit()
    
#</iplogger by Millinilliard>