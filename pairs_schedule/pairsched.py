# experimental pairing scripts
import sys
import random


def main():
    print('(pairsched) main:')
    print()

    teams = ('AA', 'BB', 'CC', 'DD', 'EE', 'FF', 'GG', 'HH')
    half = int(len(teams) / 2)

    print(teams)
    print(teams[:half])
    print(teams[half:][::-1])

    teamslist = list(teams)
    tmp = teamslist

    randoms = [tmp.pop(random.randrange(len(tmp))) for _ in range(len(teams))]
    print('result: ', randoms)

    newresult = list(grouper(randoms,2))
    print('pairings:: ', newresult)

    teamslist = list(teams)
    tmp = teamslist
    for h in range(0, half):
        t1 = tmp.pop(0)
        t2 = tmp.pop(0)
        print('pair: ', t1, t2)

    print()
    print('(pairsched) end::')

    return 0


def grouper(inputs, n=2):
    iters = [iter(inputs)] * n
    return zip(*iters)


# ----------------------------------------
if __name__ == '__main__':
    result = main()
    sys.exit(0)
