
#red 1-33
#blue 1-16
def retMap(*args):
    i=args[0]
    mapping={}
    while i<args[1]:
        mapping[i]=0
        i=i+1
    print(mapping)
    print(len(mapping))
    for i in mapping.keys():
        print(mapping[i])
def rangetest():
    for i in range(1,7):
        print(i)
if __name__ == '__main__':
    rangetest()