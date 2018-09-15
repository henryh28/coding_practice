# Complete the luckBalance function below.
def luckBalance(k, contests):
    luck = 0
    importants = []

    for contest in contests:
        luck += contest[0]
        if contest[1] == 1:
            importants.append(contest)

    importants.sort(reverse = True)

    for i in range(len(importants) - k):
        luck -= (importants.pop()[0] * 2)

    return (luck)
