import sys
import hashlib


def generate_md5_hash(word):
    md5 = hashlib.md5(word.encode())
    return md5.hexdigest()


def load_puzzle():
    with open("data/brands.txt", "r") as ins:
        tmp = ins.read().split("\n")
        brandlist = [i.split(" ") for i in tmp]

    return brandlist


def solve_puzzle(brandlist):
    final = 0

    for brand in brandlist:
        wordlist = brand
        hashlist = []
        is_valid = False

        for word in wordlist:
            print(word)
            # hash = generate_md5_hash(word)
            #   print(hash)
            #   print('')
            hashlist.append(hash)

        is_valid = check_duplicates(hashlist)
        # if is_valid:
            # final += 1

    return final


def check_duplicates(hashlist):
    print('')
    print('hashlist: ', hashlist)

    hashcounts = {}
    is_valid = False

    for i in hashlist:
        hashcounts[i] = hashlist.count(i)
    #    print('hashcounts: ', hashcounts)

    maxval = max(zip(hashcounts.values(), hashcounts.keys()))
    if maxval[0] == 1:
        is_valid = True

    return is_valid


def show_puzzle(output):
    print('')
    print('solution: ', output)


def main():
    print('(filestuff) main:')
    print('')

    mydata = load_puzzle()

    mysolution = solve_puzzle(mydata)
    show_puzzle(mysolution)
    print('')

    print('')
    print('(filestuff) end::')


# ----------------------------------------
if __name__ == '__main__':
    result = main()
    sys.exit(result)
