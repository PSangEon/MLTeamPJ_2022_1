""" sel = int(input("입력 진수 결정(16/10/8/2) : "))
num = input("값 입력 : ")

if sel == 16:
    num10 = int(num,16)
if sel == 10:
    num10 = int(num,10)
if sel == 8:
    num10 = int(num,8)
if sel == 2:
    num10 = int(num,2)

print("16진수 ==> ",hex(num10))
print("10진수 ==> ",num10)
print("8진수 ==> ",oct(num10))
print("2진수 ==> ",bin(num10)) """

'''a = 200
if a < 100:
    print("100보다 작군요")
print("집가고싶다")

print("졸려")'''

'''for i in range(1,10):
    print("집보내줘")'''

'''aa=[0,0,0,0]
hap=0
for i in range(0,4):
    aa[i]=int(input("%d번째 숫자 : " %(i+1)))
    hap=hap+aa[i]

print("합계 ==> %d" %hap)'''

'''import pandas as pd

data = {'name':["jon","ann","pter","park"],'loc':["busan","서울","경기","강원"],'age':[10,20,23,10]}

data_pandas = pd.DataFrame(data)

print(data_pandas)'''