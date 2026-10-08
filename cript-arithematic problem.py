from itertools import permutations

def crypt_arithmetic():
    letters = ['S', 'E', 'N', 'D', 'M', 'O', 'R', 'Y']

    for values in permutations(range(10), len(letters)):
        d = dict(zip(letters, values))

        # First letters cannot be zero
        if d['S'] == 0 or d['M'] == 0:
            continue

        SEND = 1000*d['S'] + 100*d['E'] + 10*d['N'] + d['D']
        MORE = 1000*d['M'] + 100*d['O'] + 10*d['R'] + d['E']
        MONEY = 10000*d['M'] + 1000*d['O'] + 100*d['N'] + 10*d['E'] + d['Y']

        if SEND + MORE == MONEY:
            print("Solution found:")
            print("S =", d['S'])
            print("E =", d['E'])
            print("N =", d['N'])
            print("D =", d['D'])
            print("M =", d['M'])
            print("O =", d['O'])
            print("R =", d['R'])
            print("Y =", d['Y'])

            print("\n", SEND)
            print("+", MORE)
            print("-------")
            print(MONEY)
            break

crypt_arithmetic()
