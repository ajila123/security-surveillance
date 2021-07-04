import pandas as dp
df=dp.read_excel("Dtataset/automob.xlsx")
def menu():
    n=0
    while(n!=3):
        print("1.user")
        print("2.admin")
        print("3.exit")
        n=int(input(""))