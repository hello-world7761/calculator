 # -*- coding: utf-8 -*-

from __future__ import division
from sympy import *
import wx
import re
from math import sin
from math import cos
from math import tan
from colorama.ansi import Style
from math import pi
from math import asin
from math import acos
from math import atan
from math import sqrt
from math import factorial
from math import e
from math import log

labels='1 1 1 1 1 EQ1 EQ2 EQ3 ( ) <- CE sin cos tan 7 8 9 / % 4 5 6 * ^ 1 2 3 - 0 0 . . + 2'.split()
last_labels = 'pi lg ln ! sqrt asin acos atan e 极限 微分 高微 1 1 1'.split()
def lg(x):
    return log(x, 10)
class EQFrame1(wx.Frame):
    def __init__(self, CalFrame):
        wx.Frame.__init__(self,CalFrame, -1, 'Solve Equation', size=(240, 310),
              style=wx.DEFAULT_FRAME_STYLE ^ (wx.RESIZE_BORDER | wx.MINIMIZE_BOX |wx.MAXIMIZE_BOX))
        panel = wx.Panel(self)
        panel.SetBackgroundColour('White')
        wx.StaticText(panel,-1,'Hint:The module is used to resolve the \nequation looks like follow:\n\
               ax2 + bx + c = 0\nThe format of input is "a,b,c" like "1,2,3".\nOr you will get an '+
               'error message.')
        wx.StaticText(panel,-1,'Input:', pos=(0,126))
        self.userText=wx.TextCtrl(panel,-1,"",pos = (0,145),
                             size=(150,25))
        wx.StaticText(panel,-1,'Result:',pos = (0,170))
        self.Button = wx.Button(panel, label='submit',size=(80,27),pos = (150,144), id=30)
        self.Button.Bind(wx.EVT_BUTTON,self.handler, self.Button)
        self.userText2=wx.TextCtrl(panel,-1,"",pos = (0,190),
                             size=(230,50), style = wx.TE_MULTILINE)
        self.ResetButton = wx.Button(panel, label='reset', size=(80,27), pos=(0,250), id=31)
        self.ResetButton.Bind(wx.EVT_BUTTON, self.reset, self.ResetButton)
    def reset(self, event):
        self.userText.SetValue('')
        self.userText2.SetValue('')
        return 
    def handler(self, event):
        s = self.userText.GetValue().split(',')
        if len(s) == 3:
            try:
                a = eval(s[0])
                b = eval(s[1])
                c = eval(s[2])
                if a == 0:
                    if b == 0:
                        message = 'No Resolution'
                    else:
                        x = -c/b
                        message = 'x=' + str(x)
                else:
                    judge = b**2 - 4 * a * c
                    if judge > 10**-6:
                        x1 = (-b + judge ** 0.5)/(2 * a)
                        x2 = (-b - judge ** 0.5)/(2 * a)
                        message = 'x1=' + str(x1) + '\nx2=' + str(x2)
                    elif 0<= judge < 10**-6:
                        x = -b / (2 * a)
                        message = 'x1=x2=' + str(x)
                    else:
                        message = 'No Real Resolution'
            except Exception:
                message = 'Invalid Input'
        else:
            message = 'Invalid Input'
        self.userText2.SetValue(message)
class EQFrame2(wx.Frame):
    def __init__(self, CalFrame):
        wx.Frame.__init__(self,CalFrame, -1, 'Solve Equations', size=(240, 310),
              style=wx.DEFAULT_FRAME_STYLE ^ (wx.RESIZE_BORDER | wx.MINIMIZE_BOX |wx.MAXIMIZE_BOX))
        panel = wx.Panel(self)
        panel.SetBackgroundColour('White')
        wx.StaticText(panel,-1,'Hint:The module is used to resolve the \nequation looks like follow:\n\
               ax + bx = e\n\
               cx + dx = f\nThe format of input is "a,b,e,c,d,f" \n\
               like "1,2,3,4,5,6".\nOr you will get an '+
               'error message.')
        wx.StaticText(panel,-1,'Input:', pos=(0,126))
        self.userText=wx.TextCtrl(panel,-1,"",pos = (0,145),
                             size=(150,25))
        wx.StaticText(panel,-1,'Result:',pos = (0,170))
        self.Button = wx.Button(panel, label='submit',size=(80,27),pos = (150,144), id=30)
        self.Button.Bind(wx.EVT_BUTTON,self.handler, self.Button)
        self.userText2=wx.TextCtrl(panel,-1,"",pos = (0,190),
                             size=(230,50), style = wx.TE_MULTILINE)
        self.ResetButton = wx.Button(panel, label='reset', size=(80,27), pos=(0,250), id=31)
        self.ResetButton.Bind(wx.EVT_BUTTON, self.reset, self.ResetButton)
    def reset(self, event):
        self.userText.SetValue('')
        self.userText2.SetValue('')
    def handler(self, event):
        s = self.userText.GetValue().split(',')
        if len(s) == 6:
            try:
                a = eval(s[0])
                b = eval(s[1])
                e = eval(s[2])
                c = eval(s[3])
                d = eval(s[4])
                f = eval(s[5])
                judge = a*d - b*c
                if 10**-6 < judge < 10**-6:
                    message = 'math error'
                else:
                    x = (d*e - b*f) / judge
                    y = (a*f - c*e) / judge
                    message = 'x=' + str(x) + '\ny=' + str(y)

            except Exception:
                message = 'math error'
        else:
            message = 'Invalid Input'
        self.userText2.SetValue(message)
class conframe(wx.Frame):
    def __init__(self, CalFrame):
        wx.Frame.__init__(self,CalFrame, -1, '进制转换', size=(300, 310))
        panel = wx.Panel(self)
        panel.SetBackgroundColour('White')
        userLabel=wx.StaticText(panel,-1,"请输入数字与进制，中间用逗号隔开：")
        self.Button = wx.Button(panel, label='ok',size=(50,60),pos = (100,10), id=30)
        self.Button.Bind(wx.EVT_BUTTON,self.handler, self.Button)
        self.userText2=wx.TextCtrl(panel,-1,"",pos = (0,30),
                             size=(100,-1))
        self.userText3=wx.TextCtrl(panel,-1,"",pos = (0,100),
                             size=(300,100))
    def handler(self, event):
        s = self.userText2.GetValue().split(',')
        a = s[0]
        b = s[1]
        c = int(s[0], int(s[1], 10))
        self.userText3.SetValue('十进制：'+ str(c)+ '\n'+ '二进制:  '+ bin(c)+ 
            '\n'+ '四进制:  '+ oct(c)+ '\n'+ '十六进制:  '+ hex(c))
class limitframe(wx.Frame):
    def __init__(self, CalFrame):
        wx.Frame.__init__(self,CalFrame, -1, '计算极限', size=(300, 310))
        panel = wx.Panel(self)
        panel.SetBackgroundColour('White')
        userLabel=wx.StaticText(panel,-1,"请输入函数式（x为自变量）与极限点，用逗号分开")
        self.Button = wx.Button(panel, label='ok',size=(50,60),pos = (100,10), id=30)
        self.Button.Bind(wx.EVT_BUTTON,self.handler, self.Button)
        self.userText2=wx.TextCtrl(panel,-1,"",pos = (0,30),
                             size=(100,-1))
        self.userText3=wx.TextCtrl(panel,-1,"",pos = (0,100),
                             size=(300,100))
    
    def handler(self, event):
        s = self.userText2.GetValue().split(',')
        func = s[0]
        num = s[1]
        x = Symbol('x')
        self.userText3.SetValue(str(limit(func, x, eval(num))))
class diffframe(wx.Frame):
    def __init__(self, CalFrame):
        wx.Frame.__init__(self,CalFrame, -1, '计算微分', size=(300, 310))
        panel = wx.Panel(self)
        panel.SetBackgroundColour('White')
        userLabel=wx.StaticText(panel,-1,"请输入函数式（x为自变量）")
        self.Button = wx.Button(panel, label='ok',size=(50,60),pos = (100,10), id=30)
        self.Button.Bind(wx.EVT_BUTTON,self.handler, self.Button)
        self.userText2=wx.TextCtrl(panel,-1,"",pos = (0,30),
                             size=(100,-1))
        self.userText3=wx.TextCtrl(panel,-1,"",pos = (0,100),
                             size=(300,100))
    
    def handler(self, event):
        s = self.userText2.GetValue()
        x = Symbol('x')
        self.userText3.SetValue(str(diff(s, x)))
class diff2frame(wx.Frame):
    def __init__(self, CalFrame):
        wx.Frame.__init__(self,CalFrame, -1, '计算高阶微分', size=(300, 310))
        panel = wx.Panel(self)
        panel.SetBackgroundColour('White')
        userLabel=wx.StaticText(panel,-1,"请输入函数式（x为自变量）与阶数，用逗号分开")
        self.Button = wx.Button(panel, label='ok',size=(50,60),pos = (100,10), id=30)
        self.Button.Bind(wx.EVT_BUTTON,self.handler, self.Button)
        self.userText2=wx.TextCtrl(panel,-1,"",pos = (0,30),
                             size=(100,-1))
        self.userText3=wx.TextCtrl(panel,-1,"",pos = (0,100),
                             size=(300,100))
    
    def handler(self, event):
        s = self.userText2.GetValue().split(',')
        x = Symbol('x')
        exp = s[0]
        num = eval(s[1])
        self.userText3.SetValue(str(diff(exp, x, num)))
class integrateframe(wx.Frame):
    def __init__(self, CalFrame):
        wx.Frame.__init__(self,CalFrame, -1, '计算定积分', size=(300, 310))
        panel = wx.Panel(self)
        panel.SetBackgroundColour('White')
        userLabel=wx.StaticText(panel,-1,"请输入函数式（x为自变量）与积分下限，积分上限，用逗号分开")
        self.Button = wx.Button(panel, label='ok',size=(50,60),pos = (100,10), id=30)
        self.Button.Bind(wx.EVT_BUTTON,self.handler, self.Button)
        self.userText2=wx.TextCtrl(panel,-1,"",pos = (0,30),
                             size=(100,-1))
        self.userText3=wx.TextCtrl(panel,-1,"",pos = (0,100),
                             size=(300,100))
    
    def handler(self, event):
        s = self.userText2.GetValue().split(',')
        x = Symbol('x')
        exp = s[0]
        num1 = eval(s[1])
        num2 = eval(s[2])
        self.userText3.SetValue(str(integrate(exp, (x, num1, num2))))



class CalFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None, -1, 'Calculator', size=(230,400),
                         style=wx.DEFAULT_FRAME_STYLE ^ (wx.RESIZE_BORDER | wx.MINIMIZE_BOX |wx.MAXIMIZE_BOX))
        panel=wx.Panel(self)
        panel.SetBackgroundColour('White')

        self.createButtons(panel)
        self.flag = False

    def createButtons(self,panel):
        sizer = wx.GridBagSizer(hgap=5, vgap=5)#grid sizer
        self.text=wx.TextCtrl(panel, wx.NewId(),value='', style=wx.TE_READONLY |
                              wx.TE_RIGHT | wx.TE_NOHIDESEL|wx.TE_MULTILINE, size=(50,50))
        sizer.Add(self.text,pos=(0,0),span=(1,5),flag=wx.EXPAND)
        i=0
        for row in range(1,7):
            for col in range(5):
                i=i+1
                self.button=wx.Button(panel, label=str(labels[row*5+col]),size=(40,30), id=i)
                self.button.Bind(wx.EVT_BUTTON, self.Handler, self.button) 
                sizer.Add(self.button,pos=(row,col))

        sizer.Detach(25)
        sizer.Detach(29)
        sizer.Detach(25)
        sizer.Detach(25)
        
        self.button=wx.Button(panel, label='=',size=(40,60), id=30)
        self.button.Bind(wx.EVT_BUTTON,self.Handler, self.button)
        sizer.Add(self.button,pos=(5,4),span=(2,1),flag=wx.EXPAND)

        self.button=wx.Button(panel,label='0',id=25)
        self.button.Bind(wx.EVT_BUTTON,self.Handler, self.button)
        sizer.Add(self.button,pos=(6,0),span=(1,2),flag=wx.EXPAND)

        self.button=wx.Button(panel, label='微分',size=(40,30), id=50)
        self.button.Bind(wx.EVT_BUTTON,self.Handler, self.button)
        sizer.Add(self.button,pos=(9,0), flag=wx.EXPAND)
        
        self.button=wx.Button(panel, label='高阶微分', id=51)
        self.button.Bind(wx.EVT_BUTTON,self.Handler, self.button)
        sizer.Add(self.button,pos=(9,1),span=(1,2), flag=wx.EXPAND)  
  

        self.button=wx.Button(panel, label='定积分', id=52)
        self.button.Bind(wx.EVT_BUTTON,self.Handler, self.button)
        sizer.Add(self.button,pos=(9,3),span=(1,2), flag=wx.EXPAND)  

        for row in range(0, 2):
            for col in range(5):
                self.button = wx.Button(panel, label=str(last_labels[row*5+col]), size=(40,30), id=row*5+col+40)
                self.button.Bind(wx.EVT_BUTTON, self.Handler, self.button)
                sizer.Add(self.button, pos=(row+7, col))
        
        panel.SetSizer(sizer)
        panel.Fit()

        self.operand1=None
        self.operand2=None
        self.operator=None
        self.temp1=0
        
    def Handler(self,event):
        Id=event.GetId()
        pattern1 = re.compile(r'\^')
        pattern2 = re.compile(r'ln')
        pattern4 = re.compile(r'\((.+)\)!')
        pattern5 = re.compile(r'([1-9][0-9]*)!')
        pattern6 = re.compile(r'(0)!')
        if Id in [4,5,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,28,29,40,43,48]:
            if not self.flag:
                self.text.SetValue(event.GetEventObject().GetLabel())
                self.flag = True
            else:
                self.text.SetValue(self.text.GetValue()+event.GetEventObject().GetLabel())
        elif Id==7: #CE
            self.text.SetValue('')
        elif Id==6 and self.flag: #<-
            s = self.text.GetValue()
            if s[-1:].isalpha():
                while s[-1:].isalpha():
                    s = s[:-1]
                self.text.SetValue(s)
            else:
                self.text.SetValue(s[0:-1])           
        elif Id in [8, 9, 10, 41, 42, 44, 45, 46, 47]:
            if not self.flag:
                self.text.SetValue(event.GetEventObject().GetLabel() + '(')
                self.flag = True
            else:
                self.text.SetValue(self.text.GetValue()+event.GetEventObject().GetLabel()+'(')                   
        elif Id==30: #=
            try:
                result = self.text.GetValue()
                result = re.sub(pattern1, '**', result)
                result = re.sub(pattern2, 'log', result)
                result = re.sub(pattern4, r'factorial(\1)', result)
                result = re.sub(pattern5, r'factorial(\1)', result)
                result = re.sub(pattern6, r'factorial(\1)', result)
                print(result)
                self.flag = False
                self.text.AppendText('\n' + str(eval(result)))
            except Exception as e:
                self.text.SetValue('Invid Input')
        elif Id==1:
            a = EQFrame1(self)
            a.Show()
        elif Id==2:
            a = EQFrame2(self)
            a.Show()
        elif Id==3:
            a = conframe(self)
            a.Show()
        elif Id==49:
            a = limitframe(self)
            a.Show()
        elif Id==50:
            a = diffframe(self)
            a.Show()
        elif Id==51:
            a = diff2frame(self)
            a.Show()
        elif Id==52:
            a = integrateframe(self)
            a.Show()

                          
app=wx.PySimpleApp()
frame=CalFrame()
frame.Show()
app.MainLoop()
