
decToHex = {
    0: "0",
    1: "1",
    2: "2",
    3: "3",
    4: "4",
    5: "5",
    6: "6",
    7: "7",
    8: "8",
    9: "9",
    10: "A",
    11: "B",
    12: "C",
    13: "D",
    14: "E",
    15: "F"
}
dec = int(input('Enter a decimal number:'))
result = ""
while dec != 0:
    rem = dec % 16
    result = result + decToHex[rem]
    dec //= 16

print("0x" + result[::-1])
