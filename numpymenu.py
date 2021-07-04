import numpy as np
def admatrix():
    n=int(input("enter the no. of rows:"))
    m=int(input("enter the no. of columns:"))
    x=[]
    for i in range(n):
        y=[]
        for j in range(m):
            z=int(input("enter the value of first matrix:"))
            y.append(z)
        x.append(y)
    print(x)
    array1=np.array(x)
    print(array1)
    p=[]
    for i in range(n):
        q = []
        for i in range(m):

            r=int(input("enter the value of second matrix:"))
            q.append(r)
        p.append(q)
    array2=np.array(p)
    print(array2)
    print("ADD")
    array3=np.divide(array1,array2)
    print(array3)
def sub():
    n = int(input("enter the no. of rows:"))
    m = int(input("enter the no. of columns:"))
    x = []
    for i in range(n):
        y = []
        for j in range(m):
            z = int(input("enter the value of first matrix:"))
            y.append(z)
        x.append(y)
    print(x)
    array1 = np.array(x)
    print(array1)
    p = []
    for i in range(n):
        q = []
        for i in range(m):
            r = int(input("enter the value of second matrix:"))
            q.append(r)
        p.append(q)
    array2 = np.array(p)
    print(array2)
    print("ADD")
    array3 = np.divide(array1, array2)
    print(array3)
def multimatrix():
    n = int(input("enter the no. of rows:"))
    m = int(input("enter the no. of columns:"))
    x = []
    for i in range(n):
        y = []
        for j in range(m):
            z = int(input("enter the value of first matrix:"))
            y.append(z)
        x.append(y)
    print(x)
    array1 = np.array(x)
    print(array1)
    p = []
    for i in range(n):
        q = []
        for i in range(m):
            r = int(input("enter the value of second matrix:"))
            q.append(r)
        p.append(q)
    array2 = np.array(p)
    print(array2)
    print("ADD")
    array3 = np.divide(array1, array2)
    print(array3)
def dotmatrix():
    n = int(input("enter the no. of rows:"))
    m = int(input("enter the no. of columns:"))
    x = []
    for i in range(n):
        y = []
        for j in range(m):
            z = int(input("enter the value of first matrix:"))
            y.append(z)
        x.append(y)
    print(x)
    array1 = np.array(x)
    print(array1)
    p = []
    for i in range(n):
        q = []
        for i in range(m):
            r = int(input("enter the value of second matrix:"))
            q.append(r)
        p.append(q)
    array2 = np.array(p)
    print(array2)
    print("ADD")
    array3 = np.divide(array1, array2)
    print(array3)
def dividematrix():
    n = int(input("enter the no. of rows:"))
    m = int(input("enter the no. of columns:"))
    x = []
    for i in range(n):
        y = []
        for j in range(m):
            z = int(input("enter the value of first matrix:"))
            y.append(z)
        x.append(y)
    print(x)
    array1 = np.array(x)
    print(array1)
    p = []
    for i in range(n):
        q = []
        for i in range(m):
            r = int(input("enter the value of second matrix:"))
            q.append(r)
        p.append(q)
    array2 = np.array(p)
    print(array2)
    print("ADD")
    array3 = np.divide(array1, array2)
    print(array3)
def menu():
    a=0
    while(a!=6):
        print("1.matrix add")
        print("2.matrix sub")
        print("3.matrix multi")
        print("4.matrix dot")
        print("5.matrix divide")
        print("6.exit")
        a=int(input("enter the choice:"))
        if a==1:
            admatrix()
        elif a==2:
            sub()
    elif a==3:
        multimatrix()
    elif a==4:
        dotmatrix()
    elif a==5:
        dividematrix()
    else:
        print("exit")
    admatrix()
    sub()
    multimatrix()
    dotmatrix()
    dividematrix()
menu()