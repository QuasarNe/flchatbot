import jieba
import jieba.posseg as pseg
import COPYRIGHT as cp
rv=1
j=False
def initialize():
    global j
    if(j==False):
        print('[语义分析模块加载成功]')
        j=True
def 评价系统(ch):
    global rv
    if(rv==1):
        print(f"你觉得{ch}怎么样？")
    op='东西'
    if "ns" in part:op='地方'
    if 'nr' in part:op='人'
    if 1<rv<=3:
        print(f'我知道了，{ch}是个坏{op}')
    elif rv==5:
        print(f'知道了知道了，{ch}是个好{op}')
        rv=1
def 绘图系统():
    import matplotlib.pyplot as plt
    import numpy as np
    import sympy as sp
    def value(c,virable):
        global t
        symbol=sp.Symbol(virable)
        expr=sp.sympify(c)
        f = sp.lambdify(symbol, expr, "numpy")
        t=np.linspace(-10,10,100)
        return f(t)
    
    op=input('函数(b) 参数方程(c)') 
    while(True):
        if(op=='c'):
            print('参数名为t，指数符号**，平方根函数sqrt()，请开始你的输入：')
            x=value(input("x="),'t')
            y=value(input('y='),'t')         
            plt.figure()
            plt.plot(x,y)
            plt.show()
        elif(op=='b'):
            print('指数符号**，平方根函数sqrt()，请开始表达式输入（自变量为x）y=',end='')
            f = input()
            for i in range(1,len(f)):
                if 'a'<f[i]<'z':
                    v=f[i]
                else:v='x'
                y=value(f,'x')
                plt.figure()
                plt.plot(t,y)
                plt.show()    
                Q=input('继续吗？(Y/n)')
                if Q=='n':break

cp.cop("flchatbot")
x=input("请键入以开始对话……\n>")
#x='函数'
while(True):
    run=False
    words = pseg.lcut(x)
    initialize()
    for word, part in words:
        i=0
        if word=='函数' or 'func' in word:
            绘图系统()
            break
        if 'n' in part and part!='eng':
            if part=='ns' or 'nr':
                run=True   
                lw=word
                if(rv>1 and lw==words[i].word): continue
                else:print(f'跟我聊聊{word}')
                if(rv>1):评价系统(word)
                rv+=1
                i+=1
                break
            else:
                print(f"我不知道{word}是什么，你能说说吗？")
                run=True
        elif part=='l': 
            print(word)
            run=True
        
    if run!=True:
        if (len(words))<=1:print(f'{x}甚')
        else:print("Knowledge is power of the world,I'll learn more")
    #print(words)
    #print('rv=',rv,len(words),word)
    x=input('>')
