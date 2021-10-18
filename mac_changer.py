import subprocess
import optparse


def mac_change(interface, new_mac):
    print("[+] Mac Changer By Ronnie")
    print("[+] Press Ctrl+C to Quit")
    print("[+] Do you want to continue? Type y for yes and n for no ")
    answer = input("[/] ")

    if answer == "y":
        subprocess.call(f"sudo ifconfig {interface} down", shell=True)
        subprocess.call(f"sudo ifconfig {interface} hw ether {new_mac}", shell=True)
        subprocess.call(f"sudo ifconfig {interface} up", shell=True)

    elif answer == "n":
        print("Quitting....")
        quit()


parse = optparse.OptionParser()

parse.add_option("-i", "--interface", dest="Interface", help="This is a program develop to change mac address")
parse.add_option("-m", "--new_mac", dest="New_Mac_Address", help="New Mac Address!")

(options, arguments) = parse.parse_args()


mac_change(options.Interface, options.New_Mac_Address)
