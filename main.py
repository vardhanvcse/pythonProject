# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import array
import numpy
import UtilPackage

def print_hi(name):

    a = ['today','is ','sunny']

    for i in (1,2,{3,4,5}):
        print(i)
        if  type(i)== type({0}):
            for j in i:
                print(j,end= ' ')


    p = array.array('i',[1,2,3,5])
    #p=array.array(["aa","b","cc",'dddd'])
    #import  *

    p.extend((1,2,3))
    p=p*2
    p.append(100)
    print( len(p))
    print(p)

    print(p.index(100))

    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, arr -> {a} fraction ->{-5//3} ')  # Press Ctrl+F8 to toggle the breakpoint.

    j = array.array('i',[2,10,8,5,3,1])

    for p in range(len(j)):
        for q in range(p):
            if j[p] < j[q]:
                o = j[p]
                j[p] = j[q]
                j[q] = o
    z = [ elem for elem in j if elem % 2 == 0]
    print(z)
    import numpy as np
    a = np.array([10,20,30])
    a= np.array(['aa','bb','cc'])
    b = np.array(a)
    b[0] = 'xys'
    print(a)
    print(b)
    import numpy as np
    print(np.zeros(10,int))
    print(range(10))
    print('Enter vals@@@')
    p = int(input())
    z= np.arange(10)
    print(z)
    #from numpy import arrang
    #j.remove(i in [1,100])
            # Press the green button in the gutter to run the script.
if __name__ == '__main__':
    UtilPackage.Arrays()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
