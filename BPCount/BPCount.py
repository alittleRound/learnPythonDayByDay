import math
totalWinChips = input()
constant = input()
room_mul = input()
Att = input()
BP = round(totalWinChips/(math.pow(totalWinChips*1.0/constant, 0.1) * (constant*1.0/10)) * room_mul * Att, 0)
print(BP)
