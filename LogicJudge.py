import Hack
import GUI01


def Judge(dict):
    l1 = len(dict)
    if l1 == 2:
        Hack.WienerHacker(dict['e'], dict['n'])
    if l1 == 3:
        if 'dp' in dict:
            Hack.dpHacker(dict['e'], dict['n'], dict['dp'])
        else:
            Hack.LowEHacker(dict['e'], dict['n'], dict['c'])
    if l1 == 4:
        Hack.IntegerFactorizationHacker(dict['n1'], dict['n2'], dict['e1'], dict['e2'])

    if l1 == 5:
        if 'dp' in dict and 'dq' in dict:
            Hack.dpAnddqHacker(dict['dp'], dict['dq'], dict['p'], dict['q'], dict['c'])
        else:
            Hack.CommonModeHacker(dict['e1'], dict['e2'], dict['c1'], dict['c2'], dict['n'])


def main():
    l1 = list()
    l2 = list()
    GUI01.show()
    print("Input some value:(Such as: e=xxx,n=xxx)")
    str1 = input("Please:")
    str1 = str1.split(",")
    for i in range(len(str1)):
        l1.append(str1[i].split('=')[0])
        l2.append(int(str1[i].split('=')[1]))
    dict_from_list = dict(zip(l1, l2))
    GUI01.HackWork()
    Judge(dict_from_list)
    GUI01.End()




if __name__ == '__main__':
    main()