from dataclasses import dataclass
import pprint
from functools import reduce

pp = pprint.PrettyPrinter(indent=4)


@dataclass
class Packet:
    v: int
    t: int


@dataclass
class PacketLit(Packet):
    lit: int

@dataclass
class PacketOp(Packet):
    sub_packets: list[Packet]


def hex_2_bin(hex_):
    return bin(int(hex_, 16))[2:].zfill(len(hex_)*4)


def parse(binary):

    def take(take):
        nonlocal binary
        value = int(binary[:take], 2)
        binary = binary[take:]
        return value

    sub_packets = []

    v = take(3)
    t = take(3)

    if t == 4:
        lit = ''
        i=0
        while True:
            block = binary[i:i+5]
            lit += block[1:]
            i += 5
            if block[0] == '0':
                break
        binary = binary[len(lit)+(i//5):]

        return PacketLit(v, t, int(lit, 2)), binary
    
    i = take(1)

    if i == 0:
        l = take(15)
        start_len = len(binary)
        while start_len - len(binary) < l:
            sub_packet, binary = parse(binary)
            sub_packets.append(sub_packet)
        
    else:
        l = take(11)
        for _ in range(l):
            sub_packet, binary = parse(binary)
            sub_packets.append(sub_packet)

    return PacketOp(v, t, sub_packets), binary

def eval(packet):
    if not isinstance(packet, PacketLit):
        sub_packets = [eval(sub_packet) for sub_packet in packet.sub_packets]

        match packet.t:
            case 0:
                return sum(sub_packets)
            case 1:
                return reduce(lambda a, c: a * c, sub_packets, 1)
            case 2:
                return min(sub_packets)
            case 3:
                return max(sub_packets)
            # case 4:
            #     return packet.lit
            case 5:
                return 1 if sub_packets[0] > sub_packets[1] else 0
            case 6:
                return 1 if sub_packets[0] < sub_packets[1] else 0
            case 7:
                return 1 if sub_packets[0] == sub_packets[1] else 0
    else:
        return packet.lit


with open("day16/input", 'r') as f:
    input = f.readline().rstrip()

    
packet, _ = parse(hex_2_bin(input))
# pp.pprint(p)

vs = []
def dfs(packet):
    vs.append(packet.v)
    if isinstance(packet, PacketLit):
        return
    else:
        for sub_packet in packet.sub_packets:
            dfs(sub_packet)

dfs(packet)
print(sum(vs))

result = eval(packet)
print(result)
