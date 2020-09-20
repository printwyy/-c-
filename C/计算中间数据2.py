import pandas as pd
df=pd.read_excel('2.xlsx',sheet_name='销项发票信息')
#df2=pd.read_excel('2.xlsx')
#name=list(df2['企业代号'])
name2=list(df['企业代号'])
time=list(df['开票日期'])

c=df.copy()
g=c.groupby([df['企业代号']]).sum()
g.to_excel('2x.xlsx')