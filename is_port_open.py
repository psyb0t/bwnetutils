from random import choice
from scapy.all import *


def is_port_open(ip_addr, port):
    ip = IP()
    ip.dst = ip_addr

    syn = TCP()
    syn.sport = choice(range(1000, 9999))
    syn.dport = port
    syn.flags = 'S'
    syn.seq = 1

    packet = ip/syn

    synack = sr1(packet)

    if synack.sprintf('%TCP.flags%') == 'SA':
        return True

    return False
