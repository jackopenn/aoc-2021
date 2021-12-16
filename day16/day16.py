with open("day16/input", 'r') as f:
    input = [line.rstrip() for line in f.readlines()]

input = input[0]
input2 = '38006F4529120'
input3 = 'C0015000016115A2E0802F182340'

all_v = []
def parse(packet):
    print()
    print(f"Packet: {packet}")



    V = int(packet[:3], 2)
    T = int(packet[3:6], 2)

    print(f"v: {V}")
    # print(V, T)
    all_v.append(V)

    if T == 4:
        print(f"T: Lit/ {T}")
        right = packet[6:]
        L = ''
        i=0
        while True:
            block = right[i:i+5]
            L += block[1:]

            i += 5
            if block[0] == '0':
                break

        right = right[len(L)+(i//5):]

        L = int(L, 2)
        print(f"Value: {L}")
        print(f"Right: {right}")
        if '1' in right:
            return parse(right)

        # print(L)
        # return V, T, L
        return

    
    I = packet[6]
    
    print(f"T: {T}")
    print(f"I: {I}")
    if I == '0':
        L = int(packet[7:22], 2)
        print(f"Size: {L}")
        left_packets = packet[22:22+L]
        right_packets = packet[22+L:]
        parse(left_packets)

        if '1' in right_packets:
            parse(right_packets)

    else:
        L = int(packet[7:18], 2)
        print(f"Count: {L}")
        sub_packets = packet[18:]
        parse(sub_packets)
    
    return


# bina = bin(int(input, 16))[2:].zfill(len(input)*4)
# # print(bina)
# parse(bina)

# print(all_v)
# print(sum(all_v))




bina2 = bin(int(input2, 16))[2:].zfill(len(input2)*4)
# print(bina2)
parse(bina2)

# print('\n\n')
# bina3 = bin(int(input3, 16))[2:].zfill(len(input3)*4)
# # print(bina3)
# parse(bina3)


