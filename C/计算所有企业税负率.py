import pandas as pd
import xlwt
df2=pd.read_csv('2.csv')#进项
df=pd.read_excel('1.xlsx')
df3=pd.read_csv('3.csv')#销项
a1=pd.read_excel('out2.xlsx')

name=list(a1['企业代号'])
#name=list(df['企业代号'])
namelist=list(df2['企业代号'])
namelist3=list(df3['企业代号'])

mon=list(df3['税额'])#销税
monlist3=list(df3['金额'])#销项
monlist=list(df2['税额'])#进税
a={}
b={}
c={}

for i in name:#进税
    for j in range(len(namelist)):
        if namelist[j]==i:
            if i not in a.keys():
                a[i]=monlist[j]
            else:
                a[i]=a[i]+monlist[j]
    print(i)
print(a)

for i in name:#销项
    for j in range(len(namelist3)):
        if namelist3[j]==i:
            if i not in b.keys():
                b[i]=monlist3[j]
            else:
                b[i]=b[i]+monlist3[j]
    print(i)
print(b)

for i in name:#销税
    for j in range(len(namelist3)):
        if namelist3[j]==i:
            if i not in c.keys():
                c[i]=mon[j]
            else:
                c[i]=c[i]+mon[j]
    print(i)
print(c)

ans={}

for i in name:
    h=c[i]-a[i]
    if h>0:
        ans[i]=h/b[i]
    else:
        ans[i]=h
print(ans)
path=pd.ExcelWriter('out3.xlsx')
w=pd.DataFrame(ans,index=[0])
w.to_excel(path,index=False)
path.save()