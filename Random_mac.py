import subprocess
import optparse

print("[+] Mac Changer By Ronnie")
print("[+] Press Ctrl+C to Quit")
print("[+] Do you want to continue? Type y for yes and n for no ")
answer = input("[/] ")

interface = input("interface: ")

if answer == "y":
    subprocess.call(f"sudo ifconfig {interface} down", shell=True)
    subprocess.call(f"sudo macchanger -r {interface}", shell=True)
    subprocess.call(f"sudo ifconfig {interface} up", shell=True)

elif answer == "n":
    print("Quitting....")
    quit()
