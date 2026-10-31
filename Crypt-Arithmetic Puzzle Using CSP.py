from itertools import permutations

letters = "SENDMORY"

for values in permutations(range(10), 8):
    d = dict(zip(letters, values))

    if d['S'] == 0 or d['M'] == 0:
        continue

    send = (
        d['S'] * 1000 + d['E'] * 100 +
        d['N'] * 10 + d['D']
    )

    more = (
        d['M'] * 1000 + d['O'] * 100 +
        d['R'] * 10 + d['E']
    )

    money = (
        d['M'] * 10000 + d['O'] * 1000 +
        d['N'] * 100 + d['E'] * 10 + d['Y']
    )

    if send + more == money:
        print("SEND =", send)
        print("MORE =", more)
        print("MONEY =", money)
        break
