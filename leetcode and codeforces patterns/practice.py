
def accountsMerge(accounts):
    accs = {}
    i = 0
    for account in accounts:
        flag = False
        for acc in accs:
            if accs[acc][0] == account[0] and (set(accs[acc][1:]) & set(account[1:])):
                res = [account[0]] + sorted(list(set(accs[acc][1:]) | set(account[1:])))
                flag = True
                accs[acc] = res
                break
        if not flag:
            accs[i] = account
            i += 1
    print(accs)
    return [["d"]]
accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
accountsMerge(accounts)