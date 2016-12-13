from random import choice
from scapy.all import IP, TCP, sr1


def is_port_open(ip_addr, port, timeout=5, verbose=False):
    ip = IP()
    ip.dst = ip_addr

    syn = TCP()
    syn.sport = choice(range(1000, 50000))
    syn.dport = port
    syn.flags = 'S'
    syn.seq = 1

    packet = ip/syn

    synack = sr1(packet, timeout=timeout, verbose=verbose)

    if synack and synack.sprintf('%TCP.flags%') == 'SA':
        return True

    return False
