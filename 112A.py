'Petya and Strings'

gift1= input()
gift2 =input()
gift1 = gift1.lower()
gift2 = gift2.lower() 

if gift1 < gift2:
    print(-1)
elif gift2< gift1:
    print(1)
else:
    print(0)
