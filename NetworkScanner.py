import scapy.all as scp
import optparse

def users_input():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i","--ipaddress", dest="ip_address",help="Enter IP Address")
    (user_input,arguments) = parse_object.parse_args()

    if not user_input.ip_address:
        print("Enter IP Address")
    return user_input

def ag_tarayici(ip):
    arp_request = scp.ARP(pdst=ip)


    broadcast = scp.Ether(dst="ff:ff:ff:ff:ff:ff")


    birlestir = broadcast/arp_request
    (cevaplananlar,cevaplanmayanlar) = scp.srp(birlestir,timeout=1)
    cevaplananlar.summary()

users_ip = users_input()
ag_tarayici(users_ip.ip_address)