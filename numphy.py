import numpy as np
def numpybasics():
    array1=np.array([1.45,7.8])
    print(array1)
    array2=np.array([2.5,55.7])
    print(array2)
    array3=np.array(['a','c'])
    print(array3)

    array4=np.array([2,4.5,'g'])
    print(array4)

    array5=array4[1:2]
    print(array5)

    array5=array4[:2]
    print(array5)

    array6=np.array([1,3,4,6,7,8,9,99,77,888,900])
    print(array6)
    array7=array6[0:4]
    print(array7)

    a=[1,2,3,4]
    a.append(6)
    print(a)

    array8=np.array(a)
    print(array8)

    array9=array8.copy()
    print(array9)

    array0=np.concatenate((array4,array5))
    print(array0)

    array11=np.where(array7>2)
    print(array11)
    array7[2]=7
    print(array7)

def numpysort():
    b=[6,5,9,2,43,21]
    array12=np.array(b)
    print(array12)
    array13=np.sort(array12)
    print(array13)
    c=['ami','aji','anu','adhi']
    array14=np.array(c)
    print(array14)
    array15=np.sort(array14)
    print(array15)
    d=[1.25,1.05,1.00,1.75,1.95]
    array16=np.array(d)
    print(array16)
    array17=np.sort(array16)
    print(array17)

#numpysort()

def numpyfilter():
    e=[2,5,7,8,1]
    array19=np.array(e)
    print(array19)
    filter=array19>5
    print(filter)
    array20=array19[filter]
    print(array20)

#numpyfilter()

def numpymultdmntnarry():
    a=[[1,2],[2,3],[1,4]]
    array22=np.array(a)
    print(array22)
    array23=np.array([[1,6],[2,7],[6,5]])
    print(array23)
    array24=np.add(array22,array23)
    print(array24)

#numpymultdmntnarry()


