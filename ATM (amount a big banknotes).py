#ATM bank v0.1

money = int(input('Withdrawal amount:'))
banknotes = [1000,500,200,100,50]
for i in banknotes:
    if money >= 0:
        change = money // i
        money -= change * i
    if change != 0:
        print ('Get your money!:'+str(change)+'*'+str(i)+'$')
else:
    print ('GoodBye! See later!')

