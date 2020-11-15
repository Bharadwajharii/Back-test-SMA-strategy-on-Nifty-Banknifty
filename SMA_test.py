import pandas as pd
import numpy as np
import datetime

def Buy(ent):
    global tran
    global b
    global i
    global idx
    sell=False
    while(not sell):
        i=i+1
        if((df.loc[i,'HIGH']<df.loc[i,'SMA30']) and (df.loc[i,'HIGH']<df.loc[i,'SMA100'])):
            tran.loc[idx,'SELL_TIME']=df.loc[i,'DATE_TIME']
            tran.loc[idx,'SELL_RATE']=df.loc[i,'CLOSE']
            idx=idx+1
            df.loc[i,'B/S']="SS"
            tran=tran.append({'SELL_TIME':df.loc[i,'DATE_TIME'],'SELL_RATE':df.loc[i,'CLOSE'],'B_S':False}, ignore_index=True)
            Sell(df.loc[i,'CLOSE'])
            sell=True
        elif((df.loc[i,'HIGH']<df.loc[i,'SMA30']) or (df.loc[i,'HIGH']<df.loc[i,'SMA100'])):
            df.loc[i,'B/S']="S"
            tran.loc[idx,'SELL_TIME']=df.loc[i,'DATE_TIME']
            tran.loc[idx,'SELL_RATE']=df.loc[i,'CLOSE']
            idx=idx+1
            b=False
            sell=True
        elif(df.loc[i,'CLOSE']>=ent*1.02):
            df.loc[i,'B/S']="S"
            tran.loc[idx,'SELL_TIME']=df.loc[i,'DATE_TIME']
            tran.loc[idx,'SELL_RATE']=df.loc[i,'CLOSE']
            idx=idx+1
            b=True
            sell=True
            CrossoverB()
        elif(df.loc[i,'CLOSE']<=ent*1.02):
            df.loc[i,'B/S']="S"
            tran.loc[idx,'SELL_TIME']=df.loc[i,'DATE_TIME']
            tran.loc[idx,'SELL_RATE']=df.loc[i,'CLOSE']
            idx=idx+1
            b=True
            sell=True
            CrossoverB()

    return

def Sell(ent):
    global tran
    global s
    global i
    global idx
    buy=False
    
    while(not buy):
        i=i+1
        if((df.loc[i,'LOW']>df.loc[i,'SMA30']) and (df.loc[i,'LOW']>df.loc[i,'SMA100'])):
            tran.loc[idx,'BUY_TIME']=df.loc[i,'DATE_TIME']
            tran.loc[idx,'BUY_RATE']=df.loc[i,'CLOSE']
            idx=idx+1
            buy=True
            df.loc[i,'B/S']="BB"
            tran=tran.append({'BUY_TIME':df.loc[i,'DATE_TIME'],'BUY_RATE':df.loc[i,'CLOSE'],'B_S':True}, ignore_index=True)
            Buy(df.loc[i,'CLOSE'])
        elif((df.loc[i,'LOW']>df.loc[i,'SMA30']) or (df.loc[i,'LOW']>df.loc[i,'SMA100'])):
            df.loc[i,'B/S']="B"
            tran.loc[idx,'BUY_TIME']=df.loc[i,'DATE_TIME']
            tran.loc[idx,'BUY_RATE']=df.loc[i,'CLOSE']
            idx=idx+1
            s=False
            buy=True
        elif(df.loc[i,'CLOSE']<=ent*1.02):
            df.loc[i,'B/S']="B"
            tran.loc[idx,'BUY_TIME']=df.loc[i,'DATE_TIME']
            tran.loc[idx,'BUY_RATE']=df.loc[i,'CLOSE']
            idx=idx+1
            s=True
            buy=True
            CrossoverS()
        elif(df.loc[i,'CLOSE']>=ent*1.02):
            df.loc[i,'B/S']="B"
            tran.loc[idx,'BUY_TIME']=df.loc[i,'DATE_TIME']
            tran.loc[idx,'BUY_RATE']=df.loc[i,'CLOSE']
            idx=idx+1
            buy=True
            s=True
            CrossoverS()
    return

def IfBuy():
    global df
    global tran
    global i
    if((df.loc[i,'LOW']>df.loc[i,'SMA30']) and (df.loc[i,'LOW']>df.loc[i,'SMA100'])):
        df.loc[i,'B/S']="B"
        tran=tran.append({'BUY_TIME':df.loc[i,'DATE_TIME'],'BUY_RATE':df.loc[i,'CLOSE'],'B_S':True}, ignore_index=True)
        Buy(df.loc[i,'CLOSE'])
    return True
def IfSell():
    global df
    global tran
    global i
    if((df.loc[i,'HIGH']<df.loc[i,'SMA30']) and (df.loc[i,'HIGH']<df.loc[i,'SMA100'])and (not s)):
        df.loc[i,'B/S']="S"
        tran=tran.append({'SELL_TIME':df.loc[i,'DATE_TIME'],'SELL_RATE':df.loc[i,'CLOSE'],'B_S':False}, ignore_index=True)
        Sell(df.loc[i,'CLOSE'])
    return True

def CrossoverB():
    global df
    global tran
    global i
    f=False
    while(not f):
        i=i+1
        if((df.loc[i,'HIGH']<df.loc[i,'SMA30']) or (df.loc[i,'HIGH']<df.loc[i,'SMA100'])):
            f=True
            IfSell()

def CrossoverS():
    global df
    global tran
    global i
    f=False
    while(not f):
        i=i+1
        if((df.loc[i,'LOW']>df.loc[i,'SMA30']) or (df.loc[i,'LOW']>df.loc[i,'SMA100'])):
            f=True
            IfBuy()
    

n=0
i=0
idx=0
b=False
s=False
while(i<len(df)):
    if(IfBuy()):
        n=n+1
    elif(IfSell):
        n=n+1
    i=i+1
    