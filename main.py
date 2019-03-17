# -*- coding: utf-8 -*-
from kivy.app import App
#:kivy 1.10.0
import kivy
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import NumericProperty, ReferenceListProperty,\
    ObjectProperty
from kivy.graphics import Line
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager , Screen , FadeTransition
from kivy.uix.widget import Widget
from kivy.graphics import Line
from kivy.core.image import Image as CoreImage
from kivy.core.window import Window
from kivy.properties import NumericProperty
from kivy.clock import Clock
from kivy.uix.image import Image
from kivy.core.audio import SoundLoader
from kivy.core.window import Window
from kivy.utils import platform
try:
    from jnius import autoclass
    from jnius import JavaException
    global AdBuddiz,PythonActivity
    if platform=="android":
        PythonActivity = autoclass("org.renpy.android.PythonActivity")
        AdBuddiz = autoclass("com.purplebrain.adbuddiz.sdk.AdBuddiz")
        AdBuddiz.setPublisherKey("5040604f-47fb-42d4-8cfc-03e4edc15d65") # Replace with your real app key
        AdBuddiz.setTestModeActive() # Comment this line before releasing!
        AdBuddiz.cacheAds(PythonActivity.mActivity)
except Exception as e:
        popup = Popup(title=u'',title_font='DroidSansFallback.ttf',
                          content=Label(text='{}'.format(e),font_name='DroidSansFallback.ttf'),
                          pos_hint={'x':0.0,'y':0.3},size_hint=(1,0.4),auto_dismiss=True)
        popup.open()
def on_pause():
    return True
def on_resume():
    pass
def show_ads():
    global AdBuddiz,PythonActivity
    AdBuddiz.showAd(PythonActivity.mActivity)
import random
import time
import os
global in_flag,computer_guess_answer,input_memory,page_analysis
page_analysis = 0
input_memory=[[0 for i in range(50)] for i in range(3)]
computer_guess_answer = 1234
in_flag = 1
def make_data(file,line):
    if os.path.isfile(file):
        pass
    else:
        with open(file,'w',encoding='utf8') as f:
            f.write(line)
make_data('data.txt','0 0 0 0 0')
make_data('analysis_data.txt','')
global data_input_data,data_analysis_data,detail_page
detail_page = 0
with open('data.txt','r',encoding='utf8') as f:
    data_input_data = f.readline().split(' ')
    print(data_input_data)
with open('analysis_data.txt','r',encoding='utf8') as f:
    data_analysis_data = f.read().split('&\n')
    print(len(data_analysis_data),data_analysis_data[0].split('@\n'))
    
def computer_answer_make():
    global computer_answer
    while 1:
        flag_answer_2 = 0
        computer_answer = random.randint(1000,9877)
        computer_answer_str = str (computer_answer)
        for j in range(0,len( computer_answer_str)):
            for s in range(0,len( computer_answer_str)):
                if (s == j):
                    continue
                if  computer_answer_str[j] in  computer_answer_str[s] or computer_answer_str[j]== '0':
                    flag_answer_2 = 1
                    break
        if (flag_answer_2 == 0):
            print(computer_answer)
            break
def all_state():
    global AB_lib,computer_guess_answer
    AB_lib=[]
    for i in range(1000,10000):
        i_str = str(i)
        i_test=4*[None]
        for j in range(4):
             i_test[j] = i_str[j]
        flag = 0
        for j in range(4):
            for s in range(4):
                if (s == j):
                    continue
                if i_test[j] in i_test[s]:
                    flag = 1
        if flag==0:
            AB_lib.append(i)
all_state()
try:
    computer_guess_answer=str(AB_lib[random.randint(0,len(AB_lib)-1)])
except:
    pass

computer_answer_make()
class MainScreen(Screen):
    def __init__(self,**kw):
        super(MainScreen,self).__init__(**kw)
        Clock.schedule_once(self.button_name, -1)
        
    def button_name(self,dt):
        
        self.ids.computer_name.text=u"電腦猜玩家"
        self.ids.computer_name.font_name='DroidSansFallback.ttf'
        self.ids.player_name.text=u"玩家猜電腦"
        self.ids.player_name.font_name='DroidSansFallback.ttf'
        self.ids.analy.text=u"數據"
        self.ids.analy.font_name='DroidSansFallback.ttf'
        self.ids.play_way.text=u"玩法?"
        self.ids.play_way.font_name='DroidSansFallback.ttf'
    def data_data(self, *args):
        global data_input_data
        with open('data.txt','r',encoding='utf8') as f:
            data_input_data = f.readline().split(' ')
            print(data_input_data)
    def count_down(self, *args):
        global count,in_flag,time_count_2
        time_count_2 = 0
        in_flag = 0
        count = 0
        time.sleep(0.001)
class show_detail(Screen):
    def __init__(self,**kw):
        super(show_detail,self).__init__(**kw)
        Clock.schedule_once(self.button_name, -1)
##        Clock.schedule_interval(self.updata_data, 1)
    def button_name(self,dt):
        global page_analysis,analysis_input,detail_page
        #totalPAGE  analysis_input[0]
        self.ids.next.text=u"下一個"
        self.ids.next.font_name='DroidSansFallback.ttf'
        self.ids.next.font_size=50
        self.ids.up.text=u"前一個"
        self.ids.up.font_name='DroidSansFallback.ttf'
        self.ids.up.font_size=50
        self.ids.exit.text=u"離開"
        self.ids.exit.font_name='DroidSansFallback.ttf'
        self.ids.exit.font_size=50
        self.ids.updates.text=u"刷新"
        self.ids.updates.font_name='DroidSansFallback.ttf'
        self.ids.updates.font_size=50
    def updata_data(self,*args):
        global detail_page,analysis_input
        try:
            self.ids.title.text=u'您第{}/{}次猜測'.format(detail_page+1,analysis_input[0])
            self.ids.title.font_name='DroidSansFallback.ttf'
            self.ids.title.font_size=50
            self.ids.detail.text=u'{}'.format(analysis_input[detail_page+3])
            self.ids.detail.font_name='DroidSansFallback.ttf'
            self.ids.detail.font_size=40
        except:
            self.ids.title.text=u"第{}/{}場遊戲".format(0,0)
            self.ids.title.font_name='DroidSansFallback.ttf'
            self.ids.title.font_size=50
            self.ids.detail.text=u"您還沒有紀錄\n趕快去玩一場吧"
            self.ids.detail.font_name='DroidSansFallback.ttf'
            self.ids.detail.font_size=50
    def next_page(self,*args):
        global page_analysis,analysis_input,detail_page
        try:
            if (int(detail_page)+1< int(analysis_input[0])):
                detail_page += 1
        except:
            pass
        finally:
            self.updata_data()
    def up_page(self,*args):
        global page_analysis,analysis_input,detail_page
        try:
            if (int(detail_page)>0):
                detail_page -= 1
        except:
            pass
        finally:
            self.updata_data()
class show_analysis(Screen):
    def __init__(self,**kw):
        super(show_analysis,self).__init__(**kw)
        Clock.schedule_once(self.button_name, -1)
##        Clock.schedule_interval(self.updata_data, 1)
    def button_name(self,dt):
        global data_input_data,data_analysis_data
        global page_analysis
        print(len(data_analysis_data),data_analysis_data)
        if (len(data_analysis_data)>2):
            self.ids.title.text=u"第{}/{}場遊戲".format(1,len(data_analysis_data)-1)
            self.ids.title.font_name='DroidSansFallback.ttf'
            self.ids.title.font_size=50#update
        else:
            self.ids.title.text=u"第{}/{}場遊戲".format(0,0)
            self.ids.title.font_name='DroidSansFallback.ttf'
            self.ids.title.font_size=50
            self.ids.detail.text=u"您還沒有紀錄\n趕快去玩一場吧"
            self.ids.detail.font_name='DroidSansFallback.ttf'
            self.ids.detail.font_size=50
        self.ids.updates.text=u"刷新"
        self.ids.updates.font_name='DroidSansFallback.ttf'
        self.ids.updates.font_size=50
        self.ids.next.text=u"下一個"
        self.ids.next.font_name='DroidSansFallback.ttf'
        self.ids.next.font_size=50
        self.ids.up.text=u"前一個"
        self.ids.up.font_name='DroidSansFallback.ttf'
        self.ids.up.font_size=50
        self.ids.remind.text=u"查看"
        self.ids.remind.font_name='DroidSansFallback.ttf'
        self.ids.remind.font_size=50
        self.ids.exit.text=u"離開"
        self.ids.exit.font_name='DroidSansFallback.ttf'
        self.ids.exit.font_size=50
    
    def updata_data(self,*args):
        global data_input_data, data_analysis_data, analysis_input
        global page_analysis
        with open('analysis_data.txt','r',encoding='utf8') as f:
            data_analysis_data = f.read().split('&\n')
            print(len(data_analysis_data))
            if (len(data_analysis_data)!=0 and len(data_analysis_data)!=1):
                try:
                    print(u'page_analysis:{}'.format(page_analysis))
                    analysis_input = data_analysis_data[page_analysis].split('@\n')
                    self.ids.title.text=u"第{}/{}場遊戲".format(page_analysis+1,len(data_analysis_data)-1)
                    self.ids.title.font_name='DroidSansFallback.ttf'
                    self.ids.title.font_size=50
                    if (analysis_input[1] == '1'):
                        self.ids.detail.text=u"猜測次數:  {}\n使否為完美局:  {}\n電腦答案:  {}".format(analysis_input[0],'是',analysis_input[2])
                        self.ids.detail.font_name='DroidSansFallback.ttf'
                        self.ids.detail.font_size=50
                    else:
                        self.ids.detail.text=u"猜測次數:  {}\n使否為完美局:  {}\n電腦答案:  {}".format(analysis_input[0],'不是',analysis_input[2])
                        self.ids.detail.font_name='DroidSansFallback.ttf'
                        self.ids.detail.font_size=50
                except Exception as e:
                    popup = Popup(title=u'',title_font='DroidSansFallback.ttf',
                                  content=Label(text='發生錯誤\n{}'.format(e),font_name='DroidSansFallback.ttf'),
                                  pos_hint={'x':0.0,'y':0.3},size_hint=(1,0.4),auto_dismiss=True)
                    popup.open()
            elif(len(data_analysis_data)==1 or len(data_analysis_data)==0):
                self.ids.title.text=u"第{}/{}場遊戲".format(0,0)
                self.ids.title.font_name='DroidSansFallback.ttf'
                self.ids.title.font_size=50
                self.ids.detail.text=u"您還沒有紀錄\n趕快去玩一場吧"
                self.ids.detail.font_name='DroidSansFallback.ttf'
                self.ids.detail.font_size=50
    def next_page(self,*args):
        global page_analysis,data_analysis_data
        try:
            if (page_analysis+1 <len(data_analysis_data)-1):
                page_analysis += 1
            else:
                page_analysis = 0
        except:
            pass
        finally:
            self.updata_data()
    def up_page(self,*args):
        global page_analysis,data_analysis_data
        try:
            if (page_analysis+1 <=len(data_analysis_data)-1 and page_analysis!=0):
                page_analysis-= 1
            else:
                page_analysis = len(data_analysis_data)-2
        except:
            pass
        finally:
            self.updata_data()
    def sure(self,*args):
        global detail_page
        detail_page = 0

        
class data(Screen):
    def __init__(self,**kw):
        super(data,self).__init__(**kw)
        Clock.schedule_once(self.button_name, -1)
        Clock.schedule_interval(self.data_update, 1)
    def button_name(self,dt):
        self.ids.title.text=u"數據"
        self.ids.title.font_name='DroidSansFallback.ttf'
        self.ids.title.font_size=50
        
        self.ids.remind.text=u"紀錄"
        self.ids.remind.font_name='DroidSansFallback.ttf'
        self.ids.remind.font_size=50
        self.ids.reset.text=u"清除數據"
        self.ids.reset.font_name='DroidSansFallback.ttf'
        self.ids.reset.font_size=50
        
        self.ids.exit.text=u"離開"
        self.ids.exit.font_name='DroidSansFallback.ttf'
        self.ids.exit.font_size=50
    def remind(self,*args):
        global popup
##        popup = Popup(title=u'',title_font='DroidSansFallback.ttf',
##                          content=Label(text='此區域尚未完成',font_name='DroidSansFallback.ttf'),
##                          pos_hint={'x':0.0,'y':0.3},size_hint=(1,0.4),auto_dismiss=True)
##        popup.open()
        self.parent.current='show_analysis'
    def reset(self,*args):
        box = GridLayout(cols=2,rows=3)
        global popup87,input_memory
        box.add_widget(Label(text=u' 是否要清除\n數據??',font_name='DroidSansFallback.ttf'))
        box.add_widget(Label(text=u' (所有的數據\n將被清除)',font_name='DroidSansFallback.ttf'))
        bt1 = Button(text='yes',font_name='DroidSansFallback.ttf',size_hint_y=None)
        bt2=Button(text='NO',font_name='DroidSansFallback.ttf',size_hint_y=None)   
        box.add_widget(bt1)
        box.add_widget(bt2)     
        popup87 = Popup(title=u'請按下"yes"以清除',title_font='DroidSansFallback.ttf',auto_dismiss=False,
                        content=box,pos_hint={'x':0.1,'y':0.3},size_hint=(0.8,0.4))
        bt1.bind(on_press=self.yes_bye, on_release=popup87.dismiss)
        bt2.bind(on_press=popup87.dismiss, on_release=popup87.dismiss)
        popup87.open()
    def yes_bye(self,dt):
        global data_input_data,data_analysis_data,detail_page
        detail_page = 0
        data_input_data = ''
        os.remove('data.txt')
        make_data('data.txt','0 0 0 0 0')
        os.remove('analysis_data.txt')
        make_data('analysis_data.txt','')
        data_analysis_data = ['']
    def data_update(self,dt):
        global data_input_data
        try:
            with open('data.txt','r',encoding='utf8') as f:
                data_input_data = f.readline().split(' ')
                self.ids.detail.text=u"遊戲次數:   {}\n平均猜測次數:   {:.2f}\n合理猜測次數:   {}\n不合理猜測次數:   {}\n完美局次數:  {}".format(data_input_data[0],\
         int(data_input_data[1])/int(data_input_data[0]) ,data_input_data[2],data_input_data[3],data_input_data[4])
                self.ids.detail.font_name='DroidSansFallback.ttf'
                self.ids.detail.font_size=50
        except:
            self.ids.detail.text=u"遊戲次數:{}\n平均猜測次數:{}\n合理猜測次數:{}\n不合理猜測次數:{}\n完美局次數:{}".format(0,0,0,0,0)
            self.ids.detail.font_name='DroidSansFallback.ttf'
            self.ids.detail.font_size=50

class tocomputer(Screen):
    def __init__(self,**kw):
        super(tocomputer,self).__init__(**kw)
        Clock.schedule_once(self.button_name, -1)
    def button_name(self, dt):
        self.ids.think_num.text=u"請想一個:不重複的4位數\n\n請點擊任意處以開始"
        self.ids.think_num.font_name='DroidSansFallback.ttf'
        self.ids.think_num.font_size=50
    def setgood(self, *args):
        global time_count,AB_lib
        time_count = 0
        all_state()

class computer(Screen):
    
    def __init__(self,**kw):
        super(computer,self).__init__(**kw)
        Clock.schedule_once(self.button_name, -1)
    def button_name(self, dt):
        global AB_lib,flag,computer_guess_answer
        self.ids.computer_guess.text=u"電腦猜:"
        self.ids.computer_guess.font_name='DroidSansFallback.ttf'
        self.ids.computer_guess.font_size=60
        
        self.ids.computer_guess_ans.text=str(computer_guess_answer)
        self.ids.computer_guess_ans.font_name='DroidSansFallback.ttf'
        self.ids.computer_guess_ans.font_size=60

        self.ids.A.text=u"A"
        self.ids.A.font_name='DroidSansFallback.ttf'
        self.ids.A.font_size=60

        self.ids.B.text=u"B"
        self.ids.B.font_name='DroidSansFallback.ttf'
        self.ids.B.font_size=60

        self.ids.accept.text=u"確定"
        self.ids.accept.font_name='DroidSansFallback.ttf'

        self.ids.com_guess.text=''
        self.ids.play_guess.text=''
        
        self.ids.leave.text=u'離開'
        self.ids.leave.font_name='DroidSansFallback.ttf'

        
    def input(self):       
        global AB_lib,time_count,flag,computer_guess_answer
        change_AB = []
        print(computer_guess_answer)
        computer_guess_answer_old = computer_guess_answer
        flag=0
        if not self.ids.A_in.text:
            A_input=0
        else:
            
            try:
                A_input = int(self.ids.A_in.text)
            except:
                flag = 5
        if not self.ids.B_in.text:
            B_input=0
        else:
            try:
                B_input = int(self.ids.B_in.text)
            except:
                flag = 5
        if (A_input>4 or B_input>4 or A_input<0 or B_input<0 or A_input + B_input > 4):
            flag = 4
        if (flag!=0):
            self.ids.A_in.text=''
            self.ids.B_in.text=''
            popup = Popup(title=u'錯誤',title_font='DroidSansFallback.ttf', content=Label(text=str('請輸入正確的數字\n錯誤代號:'+str(ord(str(flag)))),font_name='DroidSansFallback.ttf'),pos_hint={'x':0.3,'y':0.3},
                          size_hint=(0.4,0.4),auto_dismiss=True)
            popup.open()
            
        elif (flag==0):
            time_count += 1
            if (A_input ==  4):
                all_state()
                try:
                    computer_guess_answer=str(AB_lib[random.randint(0,len(AB_lib)-1)])
                    self.ids.computer_guess_ans.text=str(computer_guess_answer)
                    self.ids.computer_guess_ans.font_size=60
                except:
                    pass
                self.ids.A_in.text=''
                self.ids.B_in.text=''
                self.ids.com_guess.text=''
                self.ids.play_guess.text=''
                if time_count<=3:
                    popup = Popup(title=u'電腦: 哼! 簡單~ 哇哈哈哈~~',title_font='DroidSansFallback.ttf',
                                  content=Label(text=str('電腦一共花了'+str(time_count)+'次'),font_name='DroidSansFallback.ttf'),
                                  pos_hint={'x':0.0,'y':0.3},size_hint=(1,0.4),auto_dismiss=True)
                    popup.open()
                elif time_count<=6:
                    popup = Popup(title=u'電腦: 不錯嘛! 有值得我猜的意義',title_font='DroidSansFallback.ttf',
                                  content=Label(text=str('電腦一共花了'+str(time_count)+'次'),font_name='DroidSansFallback.ttf'),
                                  pos_hint={'x':0.0,'y':0.3},size_hint=(1,0.4),auto_dismiss=True)
                    popup.open()
                else:
                    popup = Popup(title=u'電腦: 我..我才不會承認你很厲害甚麼的',title_font='DroidSansFallback.ttf',
                                  content=Label(text=str('電腦一共花了'+str(time_count)+'次\n\n電腦:這次是我放水的，下次一定直接猜到答案'),font_name='DroidSansFallback.ttf'),
                                  pos_hint={'x':0.0,'y':0.3},size_hint=(1,0.4),auto_dismiss=True)
                    popup.open()
                    self.root.current='MainScreen'
                time_count= 0
                
            if (A_input ==  0 and B_input == 0):
                print('0a4b')
                for j in range(0,len(AB_lib)):
                    test_lib = str(AB_lib[j])
                    flag_test = 0
                    test_same =[0,1,2,3]
                    for z in range(0,4): # 123   12 3  4 2145   01 3
                        if (computer_guess_answer[z]   in test_lib ):
                            break
                    if flag_test==0 and len(test_same)==0 and test_lib not in change_AB:
                        change_AB.append(test_lib)
    #******************0A4B******************************
            if (A_input ==  0 and B_input == 4):
                print('0a4b')
                for j in range(0,len(AB_lib)):
                    test_lib = str(AB_lib[j])
                    flag_test = 0
                    test_same =[0,1,2,3]
                    for z in range(0,4): # 123   12 3  4 2145   01 3
                        if (computer_guess_answer[z]  not in test_lib or computer_guess_answer[z]==test_lib[z]):
                            flag_test = 1
                            break
                        else:
                            test_same.remove(z)
                        if flag_test==0 and len(test_same)==0 and test_lib not in change_AB:
                            change_AB.append(test_lib)
    #****************2A2B*******************
            if (A_input ==  2 and B_input == 2):
                print('2a2b')
                for j in range(0,len(AB_lib)):
                    test_lib = str(AB_lib[j])
                    flag_test = 0
                    for q in range(0,4):
                        test_same =[0,1,2,3]
                        for r in range(0,4):
                            if (q!=r):
                                if( computer_guess_answer[q] == test_lib[q] and computer_guess_answer[r] == test_lib[r]):
                                    for z in range(0,4): # 123   12 3  4 2145   01 3
                                        if (z!=q and z!=r):
                                            if (computer_guess_answer[z]  not in test_lib or computer_guess_answer[z]==test_lib[z]):
                                                flag_test = 1
                                                break
                                            else:
                                                test_same.remove(z)
                                    if flag_test==0 and len(test_same)==2 and test_lib not in change_AB:
                                        change_AB.append(test_lib)
    #****************2A1B*******************
            if (A_input ==  2 and B_input == 1):
                print('2a1b')
                for j in range(0,len(AB_lib)):
                    test_lib = str(AB_lib[j])
                    flag_test = 0
                    flag_test1=1
                    flag_test2=1
                    flag_test3=0
                    flag_test = 0
                    for q in range(0,4):
                        test_same =[0,1,2,3]
                        for r in range(0,4):
                            if (q!=r):
                                if( computer_guess_answer[q] == test_lib[q] and computer_guess_answer[r] == test_lib[r]):
                                    for z in range(0,4): # 123   12 3  4 2145   01 3
                                        if (z!=q and z!=r):
                                            if (computer_guess_answer[z]  not in test_lib ):
                                                flag_test += 1
                                            elif computer_guess_answer[z]==test_lib[z]:
                                                flag_test = 20
                                            else :
                                                test_same.remove(z)
                                    if flag_test==2 and len(test_same)==3:
                                        change_AB.append(test_lib)
    #****************1A1B*******************
            if (A_input ==  1 and B_input == 1):
                print('1a1b')
                for j in range(0,len(AB_lib)):
                    test_lib = str(AB_lib[j])
                    flag_test = 0
                    flag_test1=1
                    flag_test2=1
                    flag_test3=0
                    flag_test = 0
                    for q in range(0,4):
                        if( computer_guess_answer[q] == test_lib[q]):
                            test_same =[0,1,2,3]
                            for z in range(0,4): # 123   12 3  4 2145   01 3
                                if (z!=q ):
                                    if (computer_guess_answer[z]  not in test_lib ):
                                        flag_test += 1
                                    elif computer_guess_answer[z]==test_lib[z]:
                                        flag_test = 20
                                    else :
                                        test_same.remove(z)
                            if flag_test==2 and len(test_same)==3:
                                change_AB.append(test_lib)
    #****************1A2B*******************
            if (A_input ==  1 and B_input == 2):
                print('1a2b')
                for j in range(0,len(AB_lib)):
                    test_lib = str(AB_lib[j])
                    flag_test = 0
                    flag_test1=1
                    flag_test2=1
                    flag_test3=0
                    flag_test = 0
                    for q in range(0,4):
                        if( computer_guess_answer[q] == test_lib[q]):
                            test_same =[0,1,2,3]
                            for z in range(0,4): # 123   12 3  4 2145   01 3
                                if (z!=q ):
                                    if (computer_guess_answer[z]  not in test_lib ):
                                        flag_test += 1
                                    elif computer_guess_answer[z]==test_lib[z]:
                                        flag_test = 2
                                    else :
                                        test_same.remove(z)
                            if flag_test==1 and len(test_same)==2:
                                change_AB.append(test_lib)
                            
    #****************1A3B*******************
            if (A_input ==  1 and B_input == 3):
                print('1a3b')
                for j in range(0,len(AB_lib)):
                    test_lib = str(AB_lib[j])
                    flag_test = 0
                    flag_test1=1
                    flag_test2=1
                    flag_test3=0
                    for q in range(0,4):
                        if( computer_guess_answer[q] == test_lib[q]):
                            test_same =[0,1,2,3]
                            for z in range(0,4): # 123   12 3  4 2145   01 3
                                if (z!=q ):
                                    if (computer_guess_answer[z]  not in test_lib or computer_guess_answer[z]==test_lib[z]):
                                        flag_test = 1
                                        break
                                    else:
                                        test_same.remove(z) 
                                    if flag_test==0 and len(test_same)==1 and test_lib not in change_AB:
                                        change_AB.append(test_lib)   
    #******************0A3B******************************
            if (A_input ==  0 and B_input == 3):
                print('0a3b')
                for j in range(0,len(AB_lib)):
                    test_lib = str(AB_lib[j])
                    flag_test = 0
                    flag_test1=1
                    flag_test2=1
                    flag_test3=0
                    for q in range(0,4):
                        if( computer_guess_answer[q] in test_lib ):
                            continue
                        test_same =[0,1,2,3]
                        for z in range(0,4): # 123   12 3  4 2145   01 3
                            if (z!=q ):
                                if (computer_guess_answer[z]  not in test_lib or computer_guess_answer[z]==test_lib[z]):
                                    flag_test = 1
                                    break
                                else:
                                    test_same.remove(z)
                        if flag_test==0 and len(test_same)==1 and test_lib not in change_AB:
                            change_AB.append(test_lib)
    #************************0A2B***********************
            if (A_input ==  0 and B_input == 2):
                print('0a2b')
                for j in range(0,len(AB_lib)):
                    test_lib = str(AB_lib[j])
                    if(computer_guess_answer[0] == test_lib[1] and
                       computer_guess_answer[1] == test_lib[2]):# 01 12
                        flag_test = 0
                        for r in range(0,4):
                            for z in range(0,4):
                                if ( (z==0 and r==1) or (z==1 and r==2)):
                                    continue
                                if (computer_guess_answer[z] == test_lib[r]):
                                    flag_test = 1
                        if (flag_test==0):

                            change_AB.append(test_lib)
                    if(computer_guess_answer[0] == test_lib[1] and
                       computer_guess_answer[1] == test_lib[3]): # 01 13
                        flag_test = 0
                        for r in range(0,4):
                            for z in range(0,4):
                                if ( (z==0 and r==1 ) or ( z==1 and r==3)):
                                    continue
                                if (computer_guess_answer[z] == test_lib[r]):
                                    flag_test = 1
                        if (flag_test==0):
                            change_AB.append(test_lib)
                    if(computer_guess_answer[0] == test_lib[1] and
                       computer_guess_answer[1] == test_lib[0]): # 01 10
                        flag_test = 0
                        for r in range(0,4):
                            for z in range(0,4):
                                if ( z==0 and r==1 or z==1 and r==0):
                                    continue
                                if (computer_guess_answer[z] == test_lib[r]):
                                    flag_test = 1
                        if (flag_test==0):
                            change_AB.append(test_lib)
                    if(computer_guess_answer[0] == test_lib[1] and
                       computer_guess_answer[2] == test_lib[0]): # 01 20
                        flag_test = 0
                        for r in range(0,4):
                            for z in range(0,4):
                                if ( z==0 and r==1 or z==2 and r==0):
                                    continue
                                if (computer_guess_answer[z] == test_lib[r]):
                                    flag_test = 1
                        if (flag_test==0):
                            change_AB.append(test_lib)
                    if(computer_guess_answer[0] == test_lib[1] and
                       computer_guess_answer[2] == test_lib[3]): # 01 23
                        flag_test = 0
                        for r in range(0,4):
                            for z in range(0,4):
                                if ( z==0 and r==1 or z==2 and r==3):
                                    continue
                                if (computer_guess_answer[z] == test_lib[r]):
                                    flag_test = 1
                        if (flag_test==0):
                            change_AB.append(test_lib)
                    if(computer_guess_answer[0] == test_lib[1] and
                       computer_guess_answer[3] == test_lib[0]): # 01 30
                        flag_test = 0
                        for r in range(0,4):
                            for z in range(0,4):
                                if ( z==0 and r==1 or z==3 and r==0):
                                    continue
                                if (computer_guess_answer[z] == test_lib[r]):
                                    flag_test = 1
                        if (flag_test==0):
                            change_AB.append(test_lib)
                    if(computer_guess_answer[0] == test_lib[1] and
                       computer_guess_answer[3] == test_lib[2]): # 01 
                        flag_test = 0
                        for r in range(0,4):
                            for z in range(0,4):
                                if ( z==0 and r==1 or z==3 and r==2):
                                    continue
                                if (computer_guess_answer[z] == test_lib[r]):
                                    flag_test = 1
                        if (flag_test==0):
                            change_AB.append(test_lib)
    #********* 02***
                    if(computer_guess_answer[0] == test_lib[2] and
                       computer_guess_answer[1] == test_lib[0]): # 02 10
                        flag_test = 0
                        for r in range(0,4):
                            for z in range(0,4):
                                if ( z==0 and r==2 or z==1 and r==0):
                                    continue
                                if (computer_guess_answer[z] == test_lib[r]):
                                    flag_test = 1
                        if (flag_test==0):
                            change_AB.append(test_lib)
                    if(computer_guess_answer[0] == test_lib[2] and
                       computer_guess_answer[1] == test_lib[3]): # 02 13
                        flag_test = 0
                        for r in range(0,4):
                            for z in range(0,4):
                                if ( z==0 and r==2 or z==1 and r==3):
                                    continue
                                if (computer_guess_answer[z] == test_lib[r]):
                                    flag_test = 1
                        if (flag_test==0):
                            change_AB.append(test_lib)
                    if(computer_guess_answer[0] == test_lib[2] and
                       computer_guess_answer[2] == test_lib[0]): # 02 20
                        flag_test = 0
                        for r in range(0,4):
                            for z in range(0,4):
                                if ( z==0 and r==2 or z==2 and r==0):
                                    continue
                                if (computer_guess_answer[z] == test_lib[r]):
                                    flag_test = 1
                        if (flag_test==0):
                            change_AB.append(test_lib)
                    if(computer_guess_answer[0] == test_lib[2] and
                       computer_guess_answer[2] == test_lib[1]): # 02 21
                        flag_test = 0
                        for r in range(0,4):
                            for z in range(0,4):
                                if ( z==0 and r==2 or z==2 and r==1):
                                    continue
                                if (computer_guess_answer[z] == test_lib[r]):
                                    flag_test = 1
                        if (flag_test==0):
                            change_AB.append(test_lib)
                    if(computer_guess_answer[0] == test_lib[2] and
                       computer_guess_answer[2] == test_lib[3]): # 02 23
                        flag_test = 0
                        for r in range(0,4):
                            for z in range(0,4):
                                if ( z==0 and r==2 or z==2 and r==3):
                                    continue
                                if (computer_guess_answer[z] == test_lib[r]):
                                    flag_test = 1
                        if (flag_test==0):
                            change_AB.append(test_lib)
                    if(computer_guess_answer[0] == test_lib[2] and
                       computer_guess_answer[3] == test_lib[0]): # 02 30
                        flag_test = 0
                        for r in range(0,4):
                            for z in range(0,4):
                                if ( z==0 and r==2 or z==3 and r==0):
                                    continue
                                if (computer_guess_answer[z] == test_lib[r]):
                                    flag_test = 1
                        if (flag_test==0):
                            change_AB.append(test_lib)
                    if(computer_guess_answer[0] == test_lib[2] and
                       computer_guess_answer[3] == test_lib[1]): # 02 31
                        flag_test = 0
                        for r in range(0,4):
                            for z in range(0,4):
                                if ( z==0 and r==2 or z==3 and r==1):
                                    continue
                                if (computer_guess_answer[z] == test_lib[r]):
                                    flag_test = 1
                        if (flag_test==0):
                            change_AB.append(test_lib)
                    
    #******** 03 *******
                    if(computer_guess_answer[0] == test_lib[3] and
                       computer_guess_answer[1] == test_lib[0]): # 03 10
                        flag_test = 0
                        for r in range(0,4):
                            for z in range(0,4):
                                if ( z==0 and r==3 or z==1 and r==0):
                                    continue
                                if (computer_guess_answer[z] == test_lib[r]):
                                    flag_test = 1
                        if (flag_test==0):
                            change_AB.append(test_lib)
                    if(computer_guess_answer[0] == test_lib[3] and
                       computer_guess_answer[1] == test_lib[2]): # 03 12
                        flag_test = 0
                        for r in range(0,4):
                            for z in range(0,4):
                                if ( z==0 and r==3 or z==1 and r==2):
                                    continue
                                if (computer_guess_answer[z] == test_lib[r]):
                                    flag_test = 1
                        if (flag_test==0):
                            change_AB.append(test_lib)
                    if(computer_guess_answer[0] == test_lib[3] and
                       computer_guess_answer[2] == test_lib[0]): # 03 20
                        flag_test = 0
                        for r in range(0,4):
                            for z in range(0,4):
                                if ( z==0 and r==3 or z==2 and r==0):
                                    continue
                                if (computer_guess_answer[z] == test_lib[r]):
                                    flag_test = 1
                        if (flag_test==0):
                            change_AB.append(test_lib)
                    if(computer_guess_answer[0] == test_lib[3] and
                       computer_guess_answer[2] == test_lib[1]): # 03 21
                        flag_test = 0
                        for r in range(0,4):
                            for z in range(0,4):
                                if ( z==0 and r==3 or z==2 and r==1):
                                    continue
                                if (computer_guess_answer[z] == test_lib[r]):
                                    flag_test = 1
                        if (flag_test==0):
                            change_AB.append(test_lib)
                    if(computer_guess_answer[0] == test_lib[3] and
                       computer_guess_answer[2] == test_lib[3]): # 03 23
                        flag_test = 0
                        for r in range(0,4):
                            for z in range(0,4):
                                if ( z==0 and r==3 or z==2 and r==3):
                                    continue
                                if (computer_guess_answer[z] == test_lib[r]):
                                    flag_test = 1
                        if (flag_test==0):
                            change_AB.append(test_lib)
                    if(computer_guess_answer[0] == test_lib[3] and
                       computer_guess_answer[3] == test_lib[0]): # 03 30
                        flag_test = 0
                        for r in range(0,4):
                            for z in range(0,4):
                                if ( z==0 and r==3 or z==3 and r==0):
                                    continue
                                if (computer_guess_answer[z] == test_lib[r]):
                                    flag_test = 1
                        if (flag_test==0):
                            change_AB.append(test_lib)
                    if(computer_guess_answer[0] == test_lib[3] and
                       computer_guess_answer[3] == test_lib[1]): # 03 31
                        flag_test = 0
                        for r in range(0,4):
                            for z in range(0,4):
                                if ( z==0 and r==3 or z==3 and r==1):
                                    continue
                                if (computer_guess_answer[z] == test_lib[r]):
                                    flag_test = 1
                        if (flag_test==0):
                            change_AB.append(test_lib)
                    if(computer_guess_answer[0] == test_lib[3] and
                       computer_guess_answer[3] == test_lib[2]): # 03 32
                        flag_test = 0
                        for r in range(0,4):
                            for z in range(0,4):
                                if ( z==0 and r==3 or z==3 and r==2):
                                    continue
                                if (computer_guess_answer[z] == test_lib[r]):
                                    flag_test = 1
                        if (flag_test==0):
                            change_AB.append(test_lib)
                            
    #********* 10***
                    if(computer_guess_answer[1] == test_lib[0] and
                       computer_guess_answer[2] == test_lib[1]): # 10 21
                        flag_test = 0
                        for r in range(0,4):
                            for z in range(0,4):
                                if ( z==1 and r==0 or z==2 and r==1):
                                    continue
                                if (computer_guess_answer[z] == test_lib[r]):
                                    flag_test = 1
                        if (flag_test==0):
                            change_AB.append(test_lib)
                    if(computer_guess_answer[1] == test_lib[0] and
                       computer_guess_answer[2] == test_lib[3]): # 1023
                        flag_test = 0
                        for r in range(0,4):
                            for z in range(0,4):
                                if ( z==1 and r==0 or z==2 and r==3):
                                    continue
                                if (computer_guess_answer[z] == test_lib[r]):
                                    flag_test = 1
                        if (flag_test==0):
                            change_AB.append(test_lib)
                    if(computer_guess_answer[1] == test_lib[0] and
                       computer_guess_answer[3] == test_lib[1]): # 10 31
                        flag_test = 0
                        for r in range(0,4):
                            for z in range(0,4):
                                if ( z==1 and r==0 or z==3 and r==1):
                                    continue
                                if (computer_guess_answer[z] == test_lib[r]):
                                    flag_test = 1
                        if (flag_test==0):
                            change_AB.append(test_lib)
                    if(computer_guess_answer[1] == test_lib[0] and
                       computer_guess_answer[3] == test_lib[2]): # 10 32
                        flag_test = 0
                        for r in range(0,4):
                            for z in range(0,4):
                                if ( z==1 and r==0 or z==3 and r==2):
                                    continue
                                if (computer_guess_answer[z] == test_lib[r]):
                                    flag_test = 1
                        if (flag_test==0):
                            change_AB.append(test_lib)
                            
                    if(computer_guess_answer[1] == test_lib[2] and
                       computer_guess_answer[2] == test_lib[0]): # 12 20
                        flag_test = 0
                        for r in range(0,4):
                            for z in range(0,4):
                                if ( z==1 and r==2 or z==2 and r==0):
                                    continue
                                if (computer_guess_answer[z] == test_lib[r]):
                                    flag_test = 1
                        if (flag_test==0):
                            change_AB.append(test_lib)
                    if(computer_guess_answer[1] == test_lib[2] and
                       computer_guess_answer[2] == test_lib[1]): # 12 21
                        flag_test = 0
                        for r in range(0,4):
                            for z in range(0,4):
                                if ( z==1 and r==2 or z==2 and r==1):
                                    continue
                                if (computer_guess_answer[z] == test_lib[r]):
                                    flag_test = 1
                        if (flag_test==0):
                            change_AB.append(test_lib)
                    if(computer_guess_answer[1] == test_lib[2] and
                       computer_guess_answer[2] == test_lib[3]): # 12 23
                        flag_test = 0
                        for r in range(0,4):
                            for z in range(0,4):
                                if ( z==1 and r==2 or z==2 and r==3):
                                    continue
                                if (computer_guess_answer[z] == test_lib[r]):
                                    flag_test = 1
                        if (flag_test==0):
                            change_AB.append(test_lib)
                    if(computer_guess_answer[1] == test_lib[2] and
                       computer_guess_answer[3] == test_lib[1]): # 12 31
                        flag_test = 0
                        for r in range(0,4):
                            for z in range(0,4):
                                if ( z==1 and r==2 or z==3 and r==1):
                                    continue
                                if (computer_guess_answer[z] == test_lib[r]):
                                    flag_test = 1
                        if (flag_test==0):
                            change_AB.append(test_lib)
                    if(computer_guess_answer[1] == test_lib[2] and
                       computer_guess_answer[3] == test_lib[0]): # 12 30
                        flag_test = 0
                        for r in range(0,4):
                            for z in range(0,4):
                                if ( z==1 and r==2 or z==3 and r==0):
                                    continue
                                if (computer_guess_answer[z] == test_lib[r]):
                                    flag_test = 1
                        if (flag_test==0):
                            change_AB.append(test_lib)
                    if(computer_guess_answer[1] == test_lib[3] and
                       computer_guess_answer[3] == test_lib[0]): # 13 30
                        flag_test = 0
                        for r in range(0,4):
                            for z in range(0,4):
                                if ( z==1 and r==3 or z==3 and r==0):
                                    continue
                                if (computer_guess_answer[z] == test_lib[r]):
                                    flag_test = 1
                        if (flag_test==0):
                            change_AB.append(test_lib)
                    if(computer_guess_answer[1] == test_lib[3] and
                       computer_guess_answer[3] == test_lib[1]): # 13 31
                        flag_test = 0
                        for r in range(0,4):
                            for z in range(0,4):
                                if ( z==1 and r==3 or z==3 and r==1):
                                    continue
                                if (computer_guess_answer[z] == test_lib[r]):
                                    flag_test = 1
                        if (flag_test==0):
                            change_AB.append(test_lib)
                    if(computer_guess_answer[1] == test_lib[3] and
                       computer_guess_answer[3] == test_lib[2]): # 13 32
                        flag_test = 0
                        for r in range(0,4):
                            for z in range(0,4):
                                if ( z==1 and r==3 or z==3 and r==2):
                                    continue
                                if (computer_guess_answer[z] == test_lib[r]):
                                    flag_test = 1
                        if (flag_test==0):
                            change_AB.append(test_lib)
                            
                    
    #**** 20
                    if(computer_guess_answer[2] == test_lib[0] and
                       computer_guess_answer[3] == test_lib[1]): # 20 31
                        flag_test = 0
                        for r in range(0,4):
                            for z in range(0,4):
                                if ( z==2 and r==0 or z==3 and r==1):
                                    continue
                                if (computer_guess_answer[z] == test_lib[r]):
                                    flag_test = 1
                        if (flag_test==0):
                            change_AB.append(test_lib)
                    if(computer_guess_answer[2] == test_lib[0] and
                       computer_guess_answer[3] == test_lib[2]): # 20 32
                        flag_test = 0
                        for r in range(0,4):
                            for z in range(0,4):
                                if ( z==2 and r==0 or z==3 and r==2):
                                    continue
                                if (computer_guess_answer[z] == test_lib[r]):
                                    flag_test = 1
                        if (flag_test==0):
                            change_AB.append(test_lib)
                    if(computer_guess_answer[2] == test_lib[1] and
                       computer_guess_answer[3] == test_lib[0]): # 21 30
                        flag_test = 0
                        for r in range(0,4):
                            for z in range(0,4):
                                if ( z==2 and r==1 or z==3 and r==0):
                                    continue
                                if (computer_guess_answer[z] == test_lib[r]):
                                    flag_test = 1
                        if (flag_test==0):
                            change_AB.append(test_lib)
                    if(computer_guess_answer[2] == test_lib[1] and
                       computer_guess_answer[3] == test_lib[2]): # 21 32
                        flag_test = 0
                        for r in range(0,4):
                            for z in range(0,4):
                                if ( z==2 and r==1 or z==3 and r==2):
                                    continue
                                if (computer_guess_answer[z] == test_lib[r]):
                                    flag_test = 1
                        if (flag_test==0):
                            change_AB.append(test_lib)
                    if(computer_guess_answer[2] == test_lib[3] and
                       computer_guess_answer[3] == test_lib[0]): # 23 30
                        flag_test = 0
                        for r in range(0,4):
                            for z in range(0,4):
                                if ( z==2 and r==3 or z==3 and r==0):
                                    continue
                                if (computer_guess_answer[z] == test_lib[r]):
                                    flag_test = 1
                        if (flag_test==0):
                            change_AB.append(test_lib)
                    if(computer_guess_answer[2] == test_lib[3] and
                       computer_guess_answer[3] == test_lib[1]): # 23 31
                        flag_test = 0
                        for r in range(0,4):
                            for z in range(0,4):
                                if ( z==1 and r==2 or z==3 and r==0):
                                    continue
                                if (computer_guess_answer[z] == test_lib[r]):
                                    flag_test = 1
                        if (flag_test==0):
                            change_AB.append(test_lib)
                    if(computer_guess_answer[2] == test_lib[3] and
                       computer_guess_answer[3] == test_lib[2]): # 23 32
                        flag_test = 0
                        for r in range(0,4):
                            for z in range(0,4):
                                if ( z==2 and r==3 or z==3 and r==2):
                                    continue
                                if (computer_guess_answer[z] == test_lib[r]):
                                    flag_test = 1
                        if (flag_test==0):
                            change_AB.append(test_lib)
    #************************0A1B*************************
            
            if (A_input ==  0 and B_input == 1):
                print('0a1b')
                for j in range(0,len(AB_lib)):
                    test_lib = str(AB_lib[j])
                    if(computer_guess_answer[0] == test_lib[1]): # 01 
                        flag_test = 0
                        for r in range(0,4):
                            for z in range(0,4):
                                if ( z==0 and r==1 ):
                                    continue
                                if (computer_guess_answer[z] == test_lib[r]):
                                    flag_test = 1
                        if (flag_test==0):
                            change_AB.append(test_lib)
                    if(computer_guess_answer[0] == test_lib[2]): # 02
                        flag_test = 0
                        for r in range(0,4):
                            for z in range(0,4):
                                if ( z==0 and r==2 ):
                                    continue
                                if (computer_guess_answer[z] == test_lib[r]):
                                    flag_test = 1
                        if (flag_test==0):
                            change_AB.append(test_lib)
                    if(computer_guess_answer[0] == test_lib[3]): # 03 
                        flag_test = 0
                        for r in range(0,4):
                            for z in range(0,4):
                                if ( z==0 and r==3 ):
                                    continue
                                if (computer_guess_answer[z] == test_lib[r]):
                                    flag_test = 1
                        if (flag_test==0):
                            change_AB.append(test_lib)
                    if(computer_guess_answer[1] == test_lib[0]): # 10
                        flag_test = 0
                        for r in range(0,4):
                            for z in range(0,4):
                                if ( z==1 and r==0 ):
                                    continue
                                if (computer_guess_answer[z] == test_lib[r]):
                                    flag_test = 1
                        if (flag_test==0):
                            change_AB.append(test_lib)
                    if(computer_guess_answer[1] == test_lib[2]): # 12
                        flag_test = 0
                        for r in range(0,4):
                            for z in range(0,4):
                                if ( z==1 and r==2 ):
                                    continue
                                if (computer_guess_answer[z] == test_lib[r]):
                                    flag_test = 1
                        if (flag_test==0):
                            change_AB.append(test_lib)
                    if(computer_guess_answer[1] == test_lib[3]):# 13
                        flag_test = 0
                        for r in range(0,4):
                            for z in range(0,4):
                                if ( z==1 and r==3 ):
                                    continue
                                if (computer_guess_answer[z] == test_lib[r]):
                                    flag_test = 1
                        if (flag_test==0):
                            change_AB.append(test_lib)
                    if(computer_guess_answer[2] == test_lib[0]): # 20 
                        flag_test = 0
                        for r in range(0,4):
                            for z in range(0,4):
                                if ( z==2 and r==0 ):
                                    continue
                                if (computer_guess_answer[z] == test_lib[r]):
                                    flag_test = 1
                        if (flag_test==0):
                            change_AB.append(test_lib)
                    if(computer_guess_answer[2] == test_lib[1]): # 21 
                        flag_test = 0
                        for r in range(0,4):
                            for z in range(0,4):
                                if ( z==2 and r==1 ):
                                    continue
                                if (computer_guess_answer[z] == test_lib[r]):
                                    flag_test = 1
                        if (flag_test==0):
                            change_AB.append(test_lib)
                    if(computer_guess_answer[2] == test_lib[3]): # 23 
                        flag_test = 0
                        for r in range(0,4):
                            for z in range(0,4):
                                if ( z==2 and r==3 ):
                                    continue
                                if (computer_guess_answer[z] == test_lib[r]):
                                    flag_test = 1
                        if (flag_test==0):
                            change_AB.append(test_lib)
                    if(computer_guess_answer[3] == test_lib[0]): # 30 
                        flag_test = 0
                        for r in range(0,4):
                            for z in range(0,4):
                                if ( z==3 and r==0 ):
                                    continue
                                if (computer_guess_answer[z] == test_lib[r]):
                                    flag_test = 1
                        if (flag_test==0):
                            change_AB.append(test_lib)
                    if(computer_guess_answer[3] == test_lib[1]): # 31
                        flag_test = 0
                        for r in range(0,4):
                            for z in range(0,4):
                                if ( z==3 and r==1 ):
                                    continue
                                if (computer_guess_answer[z] == test_lib[r]):
                                    flag_test = 1
                        if (flag_test==0):
                            change_AB.append(test_lib)
                    if(computer_guess_answer[3] == test_lib[2]): # 32
                        flag_test = 0
                        for r in range(0,4):
                            for z in range(0,4):
                                if ( z==3 and r==2 ):
                                    continue
                                if (computer_guess_answer[z] == test_lib[r]):
                                    flag_test = 1
                        if (flag_test==0):
                            change_AB.append(test_lib)
    #*************************************0A0B***********************************************
            if (A_input == 0 and B_input == 0):
                 for j in range(0,len(AB_lib)): 
                    flag_test = 0
                    test_lib = str(AB_lib[j])
                    for r in range(0,4):
                        for z in range(0,4):
                            if (computer_guess_answer[z] == test_lib[r]):
                                flag_test = 1
                    if (flag_test==0):
                        change_AB.append(test_lib)
    #****************************************** 1A0B***************************************************************
            if (A_input == 1 and B_input == 0):   #computer_guess_answer = str(AB_lib[0])
                for j in range(0,len(AB_lib)):
                    test_lib = str(AB_lib[j])
                    if(computer_guess_answer[0] == test_lib[0]):
                        flag_test = 0
                        for r in range(1,4):
                            for z in range(1,4):
                                if (computer_guess_answer[z] == test_lib[r]):
                                    flag_test = 1
                        if (flag_test==0):
                            change_AB.append(test_lib)
                    if(computer_guess_answer[1] == test_lib[1]):
                        flag_test = 0
                        for r in range(0,4):
                            for z in range(0,4):
                                if (r==1 or z==1):
                                    continue
                                if (computer_guess_answer[z] == test_lib[r]):
                                    flag_test = 1
                        if (flag_test==0):
                            change_AB.append(test_lib)
                    if(computer_guess_answer[2] == test_lib[2]):
                        flag_test = 0
                        for r in range(0,4):
                            for z in range(0,4):
                                if (r==2 or z==2):
                                    continue
                                if (computer_guess_answer[z] == test_lib[r]):
                                    flag_test = 1
                        if (flag_test==0):
                            change_AB.append(test_lib)
                    if(computer_guess_answer[3] == test_lib[3]):
                        flag_test = 0
                        for r in range(0,4):
                            for z in range(0,4):
                                if (r==3 or z==3):
                                    continue
                                if (computer_guess_answer[z] == test_lib[r]):
                                    flag_test = 1
                        if (flag_test==0):
                            change_AB.append(test_lib)
    #******************************************************2A0B START***********************************
            if (A_input == 2 and B_input == 0):
                 for j in range(0,len(AB_lib)):
                    test_lib = str(AB_lib[j])
                    if(computer_guess_answer[0] == test_lib[0] and computer_guess_answer[1] == test_lib[1]): # 01 
                        flag_test = 0
                        for r in range(0,4):
                            for z in range(0,4):
                                if (r==1 or z==1 or r==0 or z==0):
                                    continue
                                if (computer_guess_answer[z] == test_lib[r]):
                                    flag_test = 1
                        if (flag_test==0):
                            change_AB.append(test_lib)
                    if(computer_guess_answer[0] == test_lib[0] and computer_guess_answer[2] == test_lib[2]):# 02
                        flag_test = 0
                        for r in range(0,4):
                            for z in range(0,4):
                                if (r==2 or z==2 or r==0 or z==0):
                                    continue
                                if (computer_guess_answer[z] == test_lib[r]):
                                    flag_test = 1
                        if (flag_test==0):
                            change_AB.append(test_lib)

                    if(computer_guess_answer[0] == test_lib[0] and computer_guess_answer[3] == test_lib[3]):# 03 
                        flag_test = 0
                        for r in range(0,4):
                            for z in range(0,4):
                                if (r==3 or z==3 or r==0 or z==0):
                                    continue
                                if (computer_guess_answer[z] == test_lib[r]):
                                    flag_test = 1
                        if (flag_test==0):
                            change_AB.append(test_lib)

                    if(computer_guess_answer[1] == test_lib[1] and computer_guess_answer[2] == test_lib[2]):# 12 
                        flag_test = 0
                        for r in range(0,4):
                            for z in range(0,4):
                                if (r==1 or z==1 or r==2 or z==2):
                                    continue
                                if (computer_guess_answer[z] == test_lib[r]):
                                    flag_test = 1
                        if (flag_test==0):
                            change_AB.append(test_lib)
                    if(computer_guess_answer[1] == test_lib[1] and computer_guess_answer[3] == test_lib[3]):# 13 
                        flag_test = 0
                        for r in range(0,4):
                            for z in range(0,4):
                                if (r==1 or z==1 or r==3 or z==3):
                                    continue
                                if (computer_guess_answer[z] == test_lib[r]):
                                    flag_test = 1
                        if (flag_test==0):
                            change_AB.append(test_lib)
                    if(computer_guess_answer[2] == test_lib[2] and computer_guess_answer[3] == test_lib[3]):# 23
                        flag_test = 0
                        for r in range(0,4):
                            for z in range(0,4):
                                if (r==2 or z==2 or r==3 or z==3):
                                    continue
                                if (computer_guess_answer[z] == test_lib[r]):
                                    flag_test = 1
                        if (flag_test==0):
                            change_AB.append(test_lib)
    #***********************************3A0B********************************************
            if (A_input == 3 and B_input == 0):
                 for j in range(0,len(AB_lib)):
                    test_lib = str(AB_lib[j])
                    if(computer_guess_answer[0]==test_lib[0] and computer_guess_answer[1]==test_lib[1] and
                       computer_guess_answer[2]==test_lib[2]): 
                        flag_test = 0
                        for r in range(0,4):
                            for z in range(0,4):
                                if (r==1 or z==1 or r==0 or z==0 or r==2 or z==2):
                                    continue
                                if (computer_guess_answer[z] == test_lib[r]):
                                    flag_test = 1
                        if (flag_test==0):
                            change_AB.append(test_lib)
                    if(computer_guess_answer[0]==test_lib[0] and computer_guess_answer[1]==test_lib[1] and
                       computer_guess_answer[3]==test_lib[3]):
                            flag_test = 0
                            for r in range(0,4):
                                for z in range(0,4):
                                    if (r==1 or z==1 or r==0 or z==0 or r==3 or z==3):
                                        continue
                                    if (computer_guess_answer[z] == test_lib[r]):
                                        flag_test = 1
                            if (flag_test==0):
                                change_AB.append(test_lib)
                    if(computer_guess_answer[1]==test_lib[1] and computer_guess_answer[2]==test_lib[2] and
                       computer_guess_answer[3]==test_lib[3]):
                            flag_test = 0
                            for r in range(0,4):
                                for z in range(0,4):
                                    if (r==1 or z==1 or r==3 or z==3 or r==2 or z==2):
                                        continue
                                    if (computer_guess_answer[z] == test_lib[r]):
                                        flag_test = 1
                            if (flag_test==0):
                                change_AB.append(test_lib)
                    if(computer_guess_answer[0]==test_lib[0] and computer_guess_answer[3]==test_lib[3] and
                       computer_guess_answer[2]==test_lib[2]):
                            flag_test = 0
                            for r in range(0,4):
                                for z in range(0,4):
                                    if (r==3 or z==3 or r==0 or z==0 or r==2 or z==2):
                                        continue
                                    if (computer_guess_answer[z] == test_lib[r]):
                                        flag_test = 1
                            if (flag_test==0):
                                change_AB.append(test_lib)
            
    #******************************************************************************************************************************
            if (A_input != 4):    
                AB_lib = change_AB
                change_AB = []
                print(AB_lib)
                try:
                    computer_guess_answer=str(AB_lib[random.randint(0,len(AB_lib)-1)])
                    
                    self.ids.computer_guess_ans.text=str(computer_guess_answer)
                    self.ids.computer_guess_ans.font_name='DroidSansFallback.ttf'
                    self.ids.computer_guess_ans.font_size=60

                    self.ids.com_guess.text= str(self.ids.com_guess.text +'電腦猜測:    '+str(computer_guess_answer_old)+'\n')
                    self.ids.com_guess.font_name='DroidSansFallback.ttf'
                    self.ids.com_guess.font_size=40
                    
                    self.ids.play_guess.text=str(self.ids.play_guess.text +'玩家回應:    '+str(A_input)+'A'+str(B_input)+'B\n')
                    self.ids.play_guess.font_name='DroidSansFallback.ttf'
                    self.ids.play_guess.font_size=40
                except Exception as e:
                    print(e)
                    popup = Popup(title=u'電腦: 你這個錯誤代號 OwO#',title_font='DroidSansFallback.ttf',
                                  content=Label(text='發生了邏輯上的錯誤\n可能是輸入錯誤所導致的\n錯誤代號:87',font_name='DroidSansFallback.ttf'),pos_hint={'x':0.0,'y':0.3},
                                  size_hint=(1,0.4),auto_dismiss=True)
                    popup.open()
                    self.parent.current="MainScreen"
                    self.ids.A_in.text=''
                    self.ids.B_in.text=''
                    all_state()
                    self.ids.computer_guess_ans.text=str(computer_guess_answer)
                    self.ids.computer_guess_ans.font_size=60
                    self.ids.com_guess.text=''
                    self.ids.play_guess.text=''
    def clear(self, *args):
        box = GridLayout(cols=2,rows=3)
        global popup87
        
        box.add_widget(Label(text=' 是否真的要離開?',font_name='DroidSansFallback.ttf'))
        box.add_widget(Label(text=' (遊戲資料將會失去)',font_name='DroidSansFallback.ttf'))
        bt1 = Button(text='yes',font_name='DroidSansFallback.ttf',size_hint_y=None)
        bt2=Button(text='NO',font_name='DroidSansFallback.ttf',size_hint_y=None)   
        box.add_widget(bt1)
        box.add_widget(bt2)     
        popup87 = Popup(title=u'電腦:膽小者才會逃跑',title_font='DroidSansFallback.ttf',auto_dismiss=False,
                        content=box,pos_hint={'x':0.1,'y':0.3},size_hint=(0.8,0.4))
        bt1.bind(on_press=self.yes,on_release=popup87.dismiss)
        bt2.bind(on_press=popup87.dismiss,on_release=popup87.dismiss)
        popup87.open()
        #on_release:app.root.current="MainScreen"
    def no(self, *args):
        global time_count_2,popup87
        popup87.dismiss()
    def yes(self, *args):
        global time_count_2,popup87,computer_guess_answer
        try:
            self.ids.A_in.text=''
            self.ids.B_in.text=''
            all_state()
            computer_guess_answer=str(AB_lib[random.randint(0,len(AB_lib)-1)])
            self.ids.computer_guess_ans.text=str(computer_guess_answer)
            self.ids.com_guess.text=''
            self.ids.play_guess.text=''
            self.parent.current='MainScreen'
        except:
            pass
class toplayer(Screen):
    def __init__(self,**kw):
        super(toplayer,self).__init__(**kw)
        global count 
        count = 0
        Clock.schedule_once(self.button_name, -1)
        Clock.schedule_interval(self.update,0.5)
    def button_name(self, dt):
        self.ids.think.text=u'電腦正在想數字中...'
        self.ids.think.font_name='DroidSansFallback.ttf'
        self.ids.think.font_size=60
        
    def update(self, dt):
        global count,in_flag
        count+=1
        self.ids.count_down.text=str('倒數...'+str(4-count))
        self.ids.count_down.font_name='DroidSansFallback.ttf'
        self.ids.count_down.font_size=60
        if (count==4 and in_flag==0):
            time.sleep(0.5)
            count = 0
            in_flag=1
            self.parent.current='player'
    
        
class player(Screen):
    def __init__(self,**kw):
        super(player,self).__init__(**kw)
        Clock.schedule_once(self.button_name, -1)
    def button_name(self, dt):
        global input_memory
        self.ids.guess_me.text=u'電腦: 猜猜我的數字阿~~'
        self.ids.guess_me.font_name='DroidSansFallback.ttf'
        self.ids.guess_me.font_size=50
        self.ids.accept.text=u'確定'
        self.ids.accept.font_name='DroidSansFallback.ttf'
        self.ids.leave.text=u'離開'
        self.ids.leave.font_name='DroidSansFallback.ttf'
        input_memory=[[0 for i in range(50)] for i in range(3)]
    def clear(self, *args):
        box = GridLayout(cols=2,rows=3)
        global popup87
        box.add_widget(Label(text=' 是否真的要離開?',font_name='DroidSansFallback.ttf'))
        box.add_widget(Label(text=' (遊戲資料將會失去)',font_name='DroidSansFallback.ttf'))
        bt1 = Button(text='yes',font_name='DroidSansFallback.ttf',size_hint_y=None)
        bt2=Button(text='NO',font_name='DroidSansFallback.ttf',size_hint_y=None)   
        box.add_widget(bt1)
        box.add_widget(bt2)     
        popup87 = Popup(title=u'電腦:膽小者才會逃跑',title_font='DroidSansFallback.ttf',auto_dismiss=False,
                        content=box,pos_hint={'x':0.1,'y':0.3},size_hint=(0.8,0.4))
        bt1.bind(on_press=self.yes,on_release=popup87.dismiss)
        bt2.bind(on_press=popup87.dismiss,on_release=popup87.dismiss)
        popup87.open()
        #on_release:app.root.current="MainScreen"
    def no(self, *args):
        global time_count_2,popup87
        popup87.dismiss()
        if (time_count_2 < 3) :
            popup = Popup(title=u'電腦: 竟然一下子就給你猜到了...',title_font='DroidSansFallback.ttf',
                          content=Label(text=str('您一共花了'+str(time_count_2)+'次猜到\n電腦:我才剛把茶泡好了說...'),font_name='DroidSansFallback.ttf'),
                          pos_hint={'x':0.0,'y':0.3},size_hint=(1,0.4),auto_dismiss=True)
            popup.open()
        elif (time_count_2 < 7) :
            popup = Popup(title=u'電腦: 還是被你給猜到了ㄋ',title_font='DroidSansFallback.ttf',
                          content=Label(text=str('您一共花了'+str(time_count_2)+'次猜到\n電腦:喝茶~~ >_<'),font_name='DroidSansFallback.ttf'),
                          pos_hint={'x':0.0,'y':0.3},size_hint=(1,0.4),auto_dismiss=True)
            popup.open()
        else:
            popup = Popup(title=u'電腦: 我都快睡著了',title_font='DroidSansFallback.ttf',
                          content=Label(text=str('您一共花了'+str(time_count_2)+'次猜到\n電腦:打哈欠 ERRR~'),font_name='DroidSansFallback.ttf'),
                          pos_hint={'x':0.0,'y':0.3},size_hint=(1,0.4),auto_dismiss=True)
            popup.open()
            
    def yes(self, *args):
        global time_count_2,popup87,input_memory
        try:
            computer_answer_make()
            self.ids.ply_res.text=''
            self.ids.com_res.text=''
            time_count_2=0
            input_memory=[[0 for i in range(50)] for i in range(3)]
            self.ids.inp.text=''
            all_state()
            self.parent.current='MainScreen'
        except:
            pass
        
    def ans_check(self, *args):
        box = GridLayout(cols=2,rows=3)
        global popup87,input_memory
        box.add_widget(Label(text=u' 是否要讓電腦\n檢查您的輸入?',font_name='DroidSansFallback.ttf'))
        box.add_widget(Label(text=u' 我們將分析\n您的猜測並紀錄\n(可在數據中查看)',font_name='DroidSansFallback.ttf'))
        bt1 = Button(text='yes',font_name='DroidSansFallback.ttf',size_hint_y=None)
        bt2=Button(text='NO',font_name='DroidSansFallback.ttf',size_hint_y=None)   
        box.add_widget(bt1)
        box.add_widget(bt2)     
        popup87 = Popup(title=u'分析你的猜測',title_font='DroidSansFallback.ttf',auto_dismiss=False,
                        content=box,pos_hint={'x':0.1,'y':0.3},size_hint=(0.8,0.4))
        bt1.bind(on_press=self.yes_check, on_release=popup87.dismiss)
        bt2.bind(on_press=self.no, on_release=popup87.dismiss)
        popup87.open()
        
    def yes_check(self, *args):
        global count_3,left_lib,count_4,past_prin,right_guess,wrong_guess
        right_guess = 0
        wrong_guess = 0
        self.parent.current='ans_analysis'
        count_3 = 0
        count_4 = 0
        all_state()
        left_lib = [[0 for i in range(5040)] for j in range(50)]
        past_prin = []
    def input(self, *args):
        global computer_answer,time_count_2,res_B,res_A,popup,input_memory,perfect,record
        flag = 0
        computer_answer_str = str(computer_answer)
        try:
            show_ads()
        except Exception as e:
            popup = Popup(title=u'',title_font='DroidSansFallback.ttf',
                                  content=Label(text='發生錯誤\n{}'.format(e),font_name='DroidSansFallback.ttf'),
                                  pos_hint={'x':0.0,'y':0.3},size_hint=(1,0.4),auto_dismiss=True)
            popup.open()
        try:
            entry_in=str(self.ids.inp.text)
            int_entry_in=int(self.ids.inp.text)
            if ( int_entry_in> 9876 or int_entry_in < 1023):
                flag = 2
                print('2')
            elif (1023<=int_entry_in<=9876):
                for j in range(0,len( entry_in)):
                    for s in range(0,len(entry_in)):
                        if (s == j):
                            continue
                        if  entry_in[j] in  entry_in[s]:
                            flag = 3
                            print('same')
                            break
        except:
            flag = 1
        if (flag!=0):
            self.ids.inp.text=''
            popup = Popup(title=u'錯誤',title_font='DroidSansFallback.ttf', content=Label(text=str('請輸入正確的數字\n錯誤代號: 87'),font_name='DroidSansFallback.ttf'),pos_hint={'x':0.0,'y':0.3},
                                  size_hint=(1,0.4),auto_dismiss=True)
            popup.open()
        elif (flag==0):
            time_count_2 += 1
            self.ids.inp.text=''
            
            if (computer_answer == int_entry_in):
                res_A = 4
                res_B = 0
                self.ans_check()
                computer_answer_make()
                self.ids.ply_res.text=''
                self.ids.com_res.text=''
                perfect = 0
                record = 0
                
            else:
                res_A=0
                res_B=0
                for j in range(0,4):
                    if (computer_answer_str[j] == entry_in[j]):
                        res_A +=1
                for j in range(0,4):
                    for s in range(0,4):
                        if (j==s):
                            continue
                        if (computer_answer_str[s] == entry_in[j]):
                            res_B +=1
                self.ids.com_res.text=str(self.ids.com_res.text + '電腦回應:   '+str(res_A)+'A'+str(res_B)+'B\n')
                self.ids.com_res.font_name='DroidSansFallback.ttf'
                self.ids.com_res.font_size=40
                
                self.ids.ply_res.text=str(self.ids.ply_res.text + '玩家猜測:   '+str(entry_in)+'\n')
                self.ids.ply_res.font_name='DroidSansFallback.ttf'
                self.ids.ply_res.font_size=40
            print('time_count_2:',time_count_2)
            input_memory[0][time_count_2-1] = entry_in
            input_memory[1][time_count_2-1] = res_A
            input_memory[2][time_count_2-1] = res_B

##            print(input_memory)
class ans_analysis(Screen):
    def __init__(self,**kw):
        super(ans_analysis,self).__init__(**kw)
        Clock.schedule_once(self.button_name, -1)
    def button_name(self, dt):
        self.ids.next.text=u'開始'
        self.ids.next.font_name='DroidSansFallback.ttf'
        self.ids.output.text=u'請按下開始'
        self.ids.output.font_name='DroidSansFallback.ttf'
        self.ids.up.text=u'上一頁'
        self.ids.up.font_name='DroidSansFallback.ttf'
        self.ids.exit.text=u"離開"
        self.ids.exit.font_name='DroidSansFallback.ttf'
        self.ids.exit.font_size=50
    def up_page(self, *args):
        global input_memory,count_4,AB_lib,left_lib,past_prin,time_count_2,count_3
        try:
            count_3 -= 1
            print('count_3:{},count_4:{}'.format(count_3,count_4))
            if (count_3 >= 1):
                print(count_3)
                self.ids.title.text=u'您第{}/{}次猜測'.format(count_3,time_count_2)
                self.ids.title.font_name='DroidSansFallback.ttf'
                self.ids.title.font_size=50
                
                self.ids.output.text=u'{}'.format( past_prin[count_3-1] )
                self.ids.output.font_size=40
            else:
                self.ans_check()
                count_3 += 1
        except:
            pass
    def ans_check(self, *args):
        box = GridLayout(cols=2,rows=3)
        global popup87,input_memory
        box.add_widget(Label(text=' 是否要離開?',font_name='DroidSansFallback.ttf'))
        box.add_widget(Label(text=' (我們將失去所有分析)',font_name='DroidSansFallback.ttf'))
        bt1 = Button(text='yes',font_name='DroidSansFallback.ttf',size_hint_y=None)
        bt2=Button(text='NO',font_name='DroidSansFallback.ttf',size_hint_y=None)   
        box.add_widget(bt1)
        box.add_widget(bt2)     
        popup87 = Popup(title=u'請確定是否有按下一步到最後一次',title_font='DroidSansFallback.ttf',auto_dismiss=False,
                        content=box,pos_hint={'x':0.1,'y':0.3},size_hint=(0.8,0.4))
        bt1.bind(on_press=self.yes_bye, on_release=popup87.dismiss)
        bt2.bind(on_press=popup87.dismiss, on_release=popup87.dismiss)
        popup87.open()
    def ans_check_2(self, *args):
        box = GridLayout(cols=2,rows=3)
        global popup87,input_memory
        box.add_widget(Label(text=' 是否要離開?',font_name='DroidSansFallback.ttf'))
        box.add_widget(Label(text=' (若要回顧請在\n主畫面的數據中查詢)',font_name='DroidSansFallback.ttf'))
        bt1 = Button(text='yes',font_name='DroidSansFallback.ttf',size_hint_y=None)
        bt2=Button(text='NO',font_name='DroidSansFallback.ttf',size_hint_y=None)   
        box.add_widget(bt1)
        box.add_widget(bt2)     
        popup87 = Popup(title=u'請確定是否有按下一步到最後一次',title_font='DroidSansFallback.ttf',auto_dismiss=False,
                        content=box,pos_hint={'x':0.1,'y':0.3},size_hint=(0.8,0.4))
        bt1.bind(on_press=self.yes_bye, on_release=popup87.dismiss)
        bt2.bind(on_press=popup87.dismiss, on_release=popup87.dismiss)
        popup87.open()
        
    def yes_bye(self,*args):
        global count_3,left_lib,count_4,past_prin,right_guess,time_count_2,perfect,record
        record = 0
        right_guess = 0
        wrong_guess = 0
        self.parent.current='player'
        self.ids.output.text=u'請按下開始'
        self.ids.output.font_name='DroidSansFallback.ttf'
        self.ids.next.text=u'開始'
        self.ids.next.font_name='DroidSansFallback.ttf'
        count_3 = 0
        count_4 = 0
        all_state()
        left_lib = [[0 for i in range(5040)] for j in range(50)]
        past_prin = []
        time_count_2=0
        perfect = 0
        input_memory=[[0 for i in range(50)] for i in range(3)]
    def next_page(self, *args):
        global input_memory,count_3,AB_lib,left_lib,past_prin,res_str,count_4,right_guess,wrong_guess,time_count_2,perfect
        global record
        self.ids.next.text=u'下一頁'
        self.ids.next.font_name='DroidSansFallback.ttf'
        print(u'count_3:{},count_4:{}'.format(count_3,count_4))
        try:
            if (count_4 == count_3 and count_3 != time_count_2):  
                res_str = u'你猜測:{}    電腦回應:{}A{}B'.format(input_memory[0][count_3],input_memory[1][count_3],input_memory[2][count_3])
                if (count_3 == 0) :
                    res_str = res_str + u'\n第一次猜測沒有對錯之分'
                elif (input_memory[0][count_3] in AB_lib and input_memory[1][count_3] != 4):
                    right_guess += 1
                    res_str = res_str +u'\n此猜測為合理猜測'
                elif(input_memory[0][count_3] not in AB_lib and input_memory[1][count_3] != 4):
                    wrong_guess += 1
                    res_str = res_str +u'\n此猜測為不合理猜測\n'
                    flag_wrong = 0
                    for i in range(count_3):
                        if (input_memory[0][count_3] in left_lib[i][:]):
                            continue
                        else:
                            flag_wrong += 1
                            res_str = res_str +u'\n與第{}次猜測:{}  {}A{}B 產生矛盾'.format(i+1,input_memory[0][i],input_memory[1][i],input_memory[2][i])
                            print(input_memory[0][i],input_memory[0][count_3])
                    if (flag_wrong ==0):
                        res_str = res_str + u'\n無矛盾之處\n若看到這一段字請將\n電腦答案及猜測過程上傳'
                            
                    res_str = res_str + u'\n\n建議此時應該猜測 {} (剩下{}個可能)\n(此建議只是為了能符合條件所產生答案)'.format(AB_lib[random.randint(0,len(AB_lib)-1)],len(AB_lib))
                if (input_memory[1][count_3] == 4):
                    try:
                        res_str = res_str +u'\n此猜測為答案\n\n猜對此答案的機率為:{:.5%} ({}/{})'.format(1/len(AB_lib),1,len(AB_lib))
                    except:
                        res_str = res_str +u'\n此猜測為答案\n\n猜對此答案的機率為:'+'({}/{})'.format(1,len(AB_lib))
                    try:
                        if(time_count_2!=1):
                            if(1/len(AB_lib)<0.05):
                                res_str = res_str +u'\n恭喜你，你可以去簽樂透了'
                            res_str = res_str + u'\n\n'+'合理猜測:{}/{} 不合理猜測:{}/{}'.format(right_guess,time_count_2-2,wrong_guess,time_count_2-2)
                            if (right_guess == time_count_2-2 ):
                                perfect = 1
                                res_str = res_str + u'\n此為完美猜測局'
                        elif(time_count_2==1):
                            if(1/len(AB_lib)<0.05):
                                res_str = res_str +u'\n恭喜你，你可以去簽樂透了'
                            res_str = res_str + u'\n\n'+'合理猜測:1/1 不合理猜測:0/1'
                            perfect = 1
                            res_str = res_str + u'\n此為完美猜測局'
                    except:
                        pass
                past_prin.append(res_str)
                self.ids.output.text=u'{}'.format(res_str)
                self.ids.output.font_size=40
                self.analysis()
                count_4 = count_3
            elif(count_3 != time_count_2):
                count_3 += 1
                self.ids.title.text=u'您第{}/{}次猜測'.format(count_3,time_count_2)
                self.ids.title.font_name='DroidSansFallback.ttf'
                self.ids.title.font_size=50
                self.ids.output.text=u'{}'.format(past_prin[count_3-1])
                self.ids.output.font_name='DroidSansFallback.ttf'
                self.ids.output.font_size=40
            elif(count_3 == time_count_2):
                try:
                    if (record == 0):
                        with open('data.txt','r+',encoding='utf8') as f:
                            data_input = f.readline().split(' ')
                            # 遊戲次數，猜測次數，合理猜測,不合理猜測，完美局 0 1 2 3
                            if (perfect == 1 ):
                                data_input[4] =int(data_input[4]) + 1
                            data_input[0] = int(data_input[0]) + 1
                            data_input[1] = int(data_input[1]) + time_count_2
                            data_input[2] = int(data_input[2]) + right_guess
                            data_input[3] = int(data_input[3]) + wrong_guess
                        os.remove('data.txt')
                        print(data_input)
                        with open('data.txt','w',encoding='utf8') as f:
                            for i in range(0,5):
                                f.write(u'{} '.format( data_input[i] ))
                        with open('analysis_data.txt','a',encoding='utf8') as g:
                            data_in = '{}@\n{}@\n{}@\n'.format(time_count_2,perfect,input_memory[0][time_count_2-1])
##                            g.write(u'{}'.format(time_count_2))
##                            g.write(u'@\n')
##                            g.write(u'{}'.format(perfect))
##                            g.write(u'@\n')
##                            g.write(u'{}'.format(input_memory[0][time_count_2-1]))
##                            g.write(u'@\n')
                            for i in range(0,len(past_prin)):
##                                g.write(u'{}'.format(past_prin[i]))
##                                g.write(u'@\n')
                                data_in = data_in + str(past_prin[i]) + '@\n'
                            g.write(u'{}&\n'.format(data_in.encode('utf-8').decode('utf8')))
                        record = 1
                    self.ans_check_2()
                except Exception as e:
                    popup = Popup(title=u'',title_font='DroidSansFallback.ttf',
                                  content=Label(text=u'{}'.format(e),font_name='DroidSansFallback.ttf'),
                                  pos_hint={'x':0.0,'y':0.3},size_hint=(1,0.4),auto_dismiss=True)
                    popup.open()
        except Exception as e:
            popup = Popup(title=u'',title_font='DroidSansFallback.ttf',
                          content=Label(text=u'{}'.format(e),font_name='DroidSansFallback.ttf'),
                          pos_hint={'x':0.0,'y':0.3},size_hint=(1,0.4),auto_dismiss=True)
            popup.open()
    def analysis(self, *args):
        global input_memory,time_count_2,count_3,AB_lib,left_lib
        try:
            change_AB = []
            count_3 += 1
    ##        print(count_3,time_count_2)
            print(input_memory)
            computer_guess_answer = str(input_memory[0][count_3-1])
            A_input = input_memory[1][count_3-1]
            B_input = input_memory[2][count_3-1]
            titit = u'您第{}/{}次猜測'.format(count_3,time_count_2)
            self.ids.title.text= u'{}'.format(titit)
            self.ids.title.font_name='DroidSansFallback.ttf'
            self.ids.title.font_size=50
            print('analysis:',computer_guess_answer,A_input,B_input)
        except Exception as e:
            popup = Popup(title=u'',title_font='DroidSansFallback.ttf',
                          content=Label(text=u'{}\n{}'.format(e[0:int(len(e)/2)],e[int(len(e)/2):len(e)]),font_name='DroidSansFallback.ttf'),
                          pos_hint={'x':0.0,'y':0.3},size_hint=(1,0.4),auto_dismiss=True)
            popup.open()
        if (A_input ==  0 and B_input == 0):
                print('0a4b')
                for j in range(0,len(AB_lib)):
                    test_lib = str(AB_lib[j])
                    flag_test = 0
                    test_same =[0,1,2,3]
                    for z in range(0,4): # 123   12 3  4 2145   01 3
                        if (computer_guess_answer[z]   in test_lib ):
                            break
                    if flag_test==0 and len(test_same)==0 and test_lib not in change_AB:
                        change_AB.append(test_lib)
    #******************0A4B******************************
        if (A_input ==  0 and B_input == 4):
            print('0a4b')
            for j in range(0,len(AB_lib)):
                test_lib = str(AB_lib[j])
                flag_test = 0
                test_same =[0,1,2,3]
                for z in range(0,4): # 123   12 3  4 2145   01 3
                    if (computer_guess_answer[z]  not in test_lib or computer_guess_answer[z]==test_lib[z]):
                        flag_test = 1
                        break
                    else:
                        test_same.remove(z)
                    if flag_test==0 and len(test_same)==0 and test_lib not in change_AB:
                        change_AB.append(test_lib)
#****************2A2B*******************
        if (A_input ==  2 and B_input == 2):
            print('2a2b')
            for j in range(0,len(AB_lib)):
                test_lib = str(AB_lib[j])
                flag_test = 0
                for q in range(0,4):
                    test_same =[0,1,2,3]
                    for r in range(0,4):
                        if (q!=r):
                            if( computer_guess_answer[q] == test_lib[q] and computer_guess_answer[r] == test_lib[r]):
                                for z in range(0,4): # 123   12 3  4 2145   01 3
                                    if (z!=q and z!=r):
                                        if (computer_guess_answer[z]  not in test_lib or computer_guess_answer[z]==test_lib[z]):
                                            flag_test = 1
                                            break
                                        else:
                                            test_same.remove(z)
                                if flag_test==0 and len(test_same)==2 and test_lib not in change_AB:
                                    change_AB.append(test_lib)
#****************2A1B*******************
        if (A_input ==  2 and B_input == 1):
            print('2a1b')
            for j in range(0,len(AB_lib)):
                test_lib = str(AB_lib[j])
                flag_test = 0
                flag_test1=1
                flag_test2=1
                flag_test3=0
                flag_test = 0
                for q in range(0,4):
                    test_same =[0,1,2,3]
                    for r in range(0,4):
                        if (q!=r):
                            if( computer_guess_answer[q] == test_lib[q] and computer_guess_answer[r] == test_lib[r]):
                                for z in range(0,4): # 123   12 3  4 2145   01 3
                                    if (z!=q and z!=r):
                                        if (computer_guess_answer[z]  not in test_lib ):
                                            flag_test += 1
                                        elif computer_guess_answer[z]==test_lib[z]:
                                            flag_test = 20
                                        else :
                                            test_same.remove(z)
                                if flag_test==2 and len(test_same)==3:
                                    change_AB.append(test_lib)
#****************1A1B*******************
        if (A_input ==  1 and B_input == 1):
            print('1a1b')
            for j in range(0,len(AB_lib)):
                test_lib = str(AB_lib[j])
                flag_test = 0
                flag_test1=1
                flag_test2=1
                flag_test3=0
                flag_test = 0
                for q in range(0,4):
                    if( computer_guess_answer[q] == test_lib[q]):
                        test_same =[0,1,2,3]
                        for z in range(0,4): # 123   12 3  4 2145   01 3
                            if (z!=q ):
                                if (computer_guess_answer[z]  not in test_lib ):
                                    flag_test += 1
                                elif computer_guess_answer[z]==test_lib[z]:
                                    flag_test = 20
                                else :
                                    test_same.remove(z)
                        if flag_test==2 and len(test_same)==3:
                            change_AB.append(test_lib)
#****************1A2B*******************
        if (A_input ==  1 and B_input == 2):
            print('1a2b')
            for j in range(0,len(AB_lib)):
                test_lib = str(AB_lib[j])
                flag_test = 0
                flag_test1=1
                flag_test2=1
                flag_test3=0
                flag_test = 0
                for q in range(0,4):
                    if( computer_guess_answer[q] == test_lib[q]):
                        test_same =[0,1,2,3]
                        for z in range(0,4): # 123   12 3  4 2145   01 3
                            if (z!=q ):
                                if (computer_guess_answer[z]  not in test_lib ):
                                    flag_test += 1
                                elif computer_guess_answer[z]==test_lib[z]:
                                    flag_test = 2
                                else :
                                    test_same.remove(z)
                        if flag_test==1 and len(test_same)==2:
                            change_AB.append(test_lib)
                        
#****************1A3B*******************
        if (A_input ==  1 and B_input == 3):
            print('1a3b')
            for j in range(0,len(AB_lib)):
                test_lib = str(AB_lib[j])
                flag_test = 0
                flag_test1=1
                flag_test2=1
                flag_test3=0
                for q in range(0,4):
                    if( computer_guess_answer[q] == test_lib[q]):
                        test_same =[0,1,2,3]
                        for z in range(0,4): # 123   12 3  4 2145   01 3
                            if (z!=q ):
                                if (computer_guess_answer[z]  not in test_lib or computer_guess_answer[z]==test_lib[z]):
                                    flag_test = 1
                                    break
                                else:
                                    test_same.remove(z) 
                                if flag_test==0 and len(test_same)==1 and test_lib not in change_AB:
                                    change_AB.append(test_lib)   
#******************0A3B******************************
        if (A_input ==  0 and B_input == 3):
            print('0a3b')
            for j in range(0,len(AB_lib)):
                test_lib = str(AB_lib[j])
                flag_test = 0
                flag_test1=1
                flag_test2=1
                flag_test3=0
                for q in range(0,4):
                    if( computer_guess_answer[q] in test_lib ):
                        continue
                    test_same =[0,1,2,3]
                    for z in range(0,4): # 123   12 3  4 2145   01 3
                        if (z!=q ):
                            if (computer_guess_answer[z]  not in test_lib or computer_guess_answer[z]==test_lib[z]):
                                flag_test = 1
                                break
                            else:
                                test_same.remove(z)
                    if flag_test==0 and len(test_same)==1 and test_lib not in change_AB:
                        change_AB.append(test_lib)
#************************0A2B***********************
        if (A_input ==  0 and B_input == 2):
            print('0a2b')
            for j in range(0,len(AB_lib)):
                test_lib = str(AB_lib[j])
                if(computer_guess_answer[0] == test_lib[1] and
                   computer_guess_answer[1] == test_lib[2]):# 01 12
                    flag_test = 0
                    for r in range(0,4):
                        for z in range(0,4):
                            if ( (z==0 and r==1) or (z==1 and r==2)):
                                continue
                            if (computer_guess_answer[z] == test_lib[r]):
                                flag_test = 1
                    if (flag_test==0):

                        change_AB.append(test_lib)
                if(computer_guess_answer[0] == test_lib[1] and
                   computer_guess_answer[1] == test_lib[3]): # 01 13
                    flag_test = 0
                    for r in range(0,4):
                        for z in range(0,4):
                            if ( (z==0 and r==1 ) or ( z==1 and r==3)):
                                continue
                            if (computer_guess_answer[z] == test_lib[r]):
                                flag_test = 1
                    if (flag_test==0):
                        change_AB.append(test_lib)
                if(computer_guess_answer[0] == test_lib[1] and
                   computer_guess_answer[1] == test_lib[0]): # 01 10
                    flag_test = 0
                    for r in range(0,4):
                        for z in range(0,4):
                            if ( z==0 and r==1 or z==1 and r==0):
                                continue
                            if (computer_guess_answer[z] == test_lib[r]):
                                flag_test = 1
                    if (flag_test==0):
                        change_AB.append(test_lib)
                if(computer_guess_answer[0] == test_lib[1] and
                   computer_guess_answer[2] == test_lib[0]): # 01 20
                    flag_test = 0
                    for r in range(0,4):
                        for z in range(0,4):
                            if ( z==0 and r==1 or z==2 and r==0):
                                continue
                            if (computer_guess_answer[z] == test_lib[r]):
                                flag_test = 1
                    if (flag_test==0):
                        change_AB.append(test_lib)
                if(computer_guess_answer[0] == test_lib[1] and
                   computer_guess_answer[2] == test_lib[3]): # 01 23
                    flag_test = 0
                    for r in range(0,4):
                        for z in range(0,4):
                            if ( z==0 and r==1 or z==2 and r==3):
                                continue
                            if (computer_guess_answer[z] == test_lib[r]):
                                flag_test = 1
                    if (flag_test==0):
                        change_AB.append(test_lib)
                if(computer_guess_answer[0] == test_lib[1] and
                   computer_guess_answer[3] == test_lib[0]): # 01 30
                    flag_test = 0
                    for r in range(0,4):
                        for z in range(0,4):
                            if ( z==0 and r==1 or z==3 and r==0):
                                continue
                            if (computer_guess_answer[z] == test_lib[r]):
                                flag_test = 1
                    if (flag_test==0):
                        change_AB.append(test_lib)
                if(computer_guess_answer[0] == test_lib[1] and
                   computer_guess_answer[3] == test_lib[2]): # 01 
                    flag_test = 0
                    for r in range(0,4):
                        for z in range(0,4):
                            if ( z==0 and r==1 or z==3 and r==2):
                                continue
                            if (computer_guess_answer[z] == test_lib[r]):
                                flag_test = 1
                    if (flag_test==0):
                        change_AB.append(test_lib)
#********* 02***
                if(computer_guess_answer[0] == test_lib[2] and
                   computer_guess_answer[1] == test_lib[0]): # 02 10
                    flag_test = 0
                    for r in range(0,4):
                        for z in range(0,4):
                            if ( z==0 and r==2 or z==1 and r==0):
                                continue
                            if (computer_guess_answer[z] == test_lib[r]):
                                flag_test = 1
                    if (flag_test==0):
                        change_AB.append(test_lib)
                if(computer_guess_answer[0] == test_lib[2] and
                   computer_guess_answer[1] == test_lib[3]): # 02 13
                    flag_test = 0
                    for r in range(0,4):
                        for z in range(0,4):
                            if ( z==0 and r==2 or z==1 and r==3):
                                continue
                            if (computer_guess_answer[z] == test_lib[r]):
                                flag_test = 1
                    if (flag_test==0):
                        change_AB.append(test_lib)
                if(computer_guess_answer[0] == test_lib[2] and
                   computer_guess_answer[2] == test_lib[0]): # 02 20
                    flag_test = 0
                    for r in range(0,4):
                        for z in range(0,4):
                            if ( z==0 and r==2 or z==2 and r==0):
                                continue
                            if (computer_guess_answer[z] == test_lib[r]):
                                flag_test = 1
                    if (flag_test==0):
                        change_AB.append(test_lib)
                if(computer_guess_answer[0] == test_lib[2] and
                   computer_guess_answer[2] == test_lib[1]): # 02 21
                    flag_test = 0
                    for r in range(0,4):
                        for z in range(0,4):
                            if ( z==0 and r==2 or z==2 and r==1):
                                continue
                            if (computer_guess_answer[z] == test_lib[r]):
                                flag_test = 1
                    if (flag_test==0):
                        change_AB.append(test_lib)
                if(computer_guess_answer[0] == test_lib[2] and
                   computer_guess_answer[2] == test_lib[3]): # 02 23
                    flag_test = 0
                    for r in range(0,4):
                        for z in range(0,4):
                            if ( z==0 and r==2 or z==2 and r==3):
                                continue
                            if (computer_guess_answer[z] == test_lib[r]):
                                flag_test = 1
                    if (flag_test==0):
                        change_AB.append(test_lib)
                if(computer_guess_answer[0] == test_lib[2] and
                   computer_guess_answer[3] == test_lib[0]): # 02 30
                    flag_test = 0
                    for r in range(0,4):
                        for z in range(0,4):
                            if ( z==0 and r==2 or z==3 and r==0):
                                continue
                            if (computer_guess_answer[z] == test_lib[r]):
                                flag_test = 1
                    if (flag_test==0):
                        change_AB.append(test_lib)
                if(computer_guess_answer[0] == test_lib[2] and
                   computer_guess_answer[3] == test_lib[1]): # 02 31
                    flag_test = 0
                    for r in range(0,4):
                        for z in range(0,4):
                            if ( z==0 and r==2 or z==3 and r==1):
                                continue
                            if (computer_guess_answer[z] == test_lib[r]):
                                flag_test = 1
                    if (flag_test==0):
                        change_AB.append(test_lib)
                
#******** 03 *******
                if(computer_guess_answer[0] == test_lib[3] and
                   computer_guess_answer[1] == test_lib[0]): # 03 10
                    flag_test = 0
                    for r in range(0,4):
                        for z in range(0,4):
                            if ( z==0 and r==3 or z==1 and r==0):
                                continue
                            if (computer_guess_answer[z] == test_lib[r]):
                                flag_test = 1
                    if (flag_test==0):
                        change_AB.append(test_lib)
                if(computer_guess_answer[0] == test_lib[3] and
                   computer_guess_answer[1] == test_lib[2]): # 03 12
                    flag_test = 0
                    for r in range(0,4):
                        for z in range(0,4):
                            if ( z==0 and r==3 or z==1 and r==2):
                                continue
                            if (computer_guess_answer[z] == test_lib[r]):
                                flag_test = 1
                    if (flag_test==0):
                        change_AB.append(test_lib)
                if(computer_guess_answer[0] == test_lib[3] and
                   computer_guess_answer[2] == test_lib[0]): # 03 20
                    flag_test = 0
                    for r in range(0,4):
                        for z in range(0,4):
                            if ( z==0 and r==3 or z==2 and r==0):
                                continue
                            if (computer_guess_answer[z] == test_lib[r]):
                                flag_test = 1
                    if (flag_test==0):
                        change_AB.append(test_lib)
                if(computer_guess_answer[0] == test_lib[3] and
                   computer_guess_answer[2] == test_lib[1]): # 03 21
                    flag_test = 0
                    for r in range(0,4):
                        for z in range(0,4):
                            if ( z==0 and r==3 or z==2 and r==1):
                                continue
                            if (computer_guess_answer[z] == test_lib[r]):
                                flag_test = 1
                    if (flag_test==0):
                        change_AB.append(test_lib)
                if(computer_guess_answer[0] == test_lib[3] and
                   computer_guess_answer[2] == test_lib[3]): # 03 23
                    flag_test = 0
                    for r in range(0,4):
                        for z in range(0,4):
                            if ( z==0 and r==3 or z==2 and r==3):
                                continue
                            if (computer_guess_answer[z] == test_lib[r]):
                                flag_test = 1
                    if (flag_test==0):
                        change_AB.append(test_lib)
                if(computer_guess_answer[0] == test_lib[3] and
                   computer_guess_answer[3] == test_lib[0]): # 03 30
                    flag_test = 0
                    for r in range(0,4):
                        for z in range(0,4):
                            if ( z==0 and r==3 or z==3 and r==0):
                                continue
                            if (computer_guess_answer[z] == test_lib[r]):
                                flag_test = 1
                    if (flag_test==0):
                        change_AB.append(test_lib)
                if(computer_guess_answer[0] == test_lib[3] and
                   computer_guess_answer[3] == test_lib[1]): # 03 31
                    flag_test = 0
                    for r in range(0,4):
                        for z in range(0,4):
                            if ( z==0 and r==3 or z==3 and r==1):
                                continue
                            if (computer_guess_answer[z] == test_lib[r]):
                                flag_test = 1
                    if (flag_test==0):
                        change_AB.append(test_lib)
                if(computer_guess_answer[0] == test_lib[3] and
                   computer_guess_answer[3] == test_lib[2]): # 03 32
                    flag_test = 0
                    for r in range(0,4):
                        for z in range(0,4):
                            if ( z==0 and r==3 or z==3 and r==2):
                                continue
                            if (computer_guess_answer[z] == test_lib[r]):
                                flag_test = 1
                    if (flag_test==0):
                        change_AB.append(test_lib)
                        
#********* 10***
                if(computer_guess_answer[1] == test_lib[0] and
                   computer_guess_answer[2] == test_lib[1]): # 10 21
                    flag_test = 0
                    for r in range(0,4):
                        for z in range(0,4):
                            if ( z==1 and r==0 or z==2 and r==1):
                                continue
                            if (computer_guess_answer[z] == test_lib[r]):
                                flag_test = 1
                    if (flag_test==0):
                        change_AB.append(test_lib)
                if(computer_guess_answer[1] == test_lib[0] and
                   computer_guess_answer[2] == test_lib[3]): # 1023
                    flag_test = 0
                    for r in range(0,4):
                        for z in range(0,4):
                            if ( z==1 and r==0 or z==2 and r==3):
                                continue
                            if (computer_guess_answer[z] == test_lib[r]):
                                flag_test = 1
                    if (flag_test==0):
                        change_AB.append(test_lib)
                if(computer_guess_answer[1] == test_lib[0] and
                   computer_guess_answer[3] == test_lib[1]): # 10 31
                    flag_test = 0
                    for r in range(0,4):
                        for z in range(0,4):
                            if ( z==1 and r==0 or z==3 and r==1):
                                continue
                            if (computer_guess_answer[z] == test_lib[r]):
                                flag_test = 1
                    if (flag_test==0):
                        change_AB.append(test_lib)
                if(computer_guess_answer[1] == test_lib[0] and
                   computer_guess_answer[3] == test_lib[2]): # 10 32
                    flag_test = 0
                    for r in range(0,4):
                        for z in range(0,4):
                            if ( z==1 and r==0 or z==3 and r==2):
                                continue
                            if (computer_guess_answer[z] == test_lib[r]):
                                flag_test = 1
                    if (flag_test==0):
                        change_AB.append(test_lib)
                        
                if(computer_guess_answer[1] == test_lib[2] and
                   computer_guess_answer[2] == test_lib[0]): # 12 20
                    flag_test = 0
                    for r in range(0,4):
                        for z in range(0,4):
                            if ( z==1 and r==2 or z==2 and r==0):
                                continue
                            if (computer_guess_answer[z] == test_lib[r]):
                                flag_test = 1
                    if (flag_test==0):
                        change_AB.append(test_lib)
                if(computer_guess_answer[1] == test_lib[2] and
                   computer_guess_answer[2] == test_lib[1]): # 12 21
                    flag_test = 0
                    for r in range(0,4):
                        for z in range(0,4):
                            if ( z==1 and r==2 or z==2 and r==1):
                                continue
                            if (computer_guess_answer[z] == test_lib[r]):
                                flag_test = 1
                    if (flag_test==0):
                        change_AB.append(test_lib)
                if(computer_guess_answer[1] == test_lib[2] and
                   computer_guess_answer[2] == test_lib[3]): # 12 23
                    flag_test = 0
                    for r in range(0,4):
                        for z in range(0,4):
                            if ( z==1 and r==2 or z==2 and r==3):
                                continue
                            if (computer_guess_answer[z] == test_lib[r]):
                                flag_test = 1
                    if (flag_test==0):
                        change_AB.append(test_lib)
                if(computer_guess_answer[1] == test_lib[2] and
                   computer_guess_answer[3] == test_lib[1]): # 12 31
                    flag_test = 0
                    for r in range(0,4):
                        for z in range(0,4):
                            if ( z==1 and r==2 or z==3 and r==1):
                                continue
                            if (computer_guess_answer[z] == test_lib[r]):
                                flag_test = 1
                    if (flag_test==0):
                        change_AB.append(test_lib)
                if(computer_guess_answer[1] == test_lib[2] and
                   computer_guess_answer[3] == test_lib[0]): # 12 30
                    flag_test = 0
                    for r in range(0,4):
                        for z in range(0,4):
                            if ( z==1 and r==2 or z==3 and r==0):
                                continue
                            if (computer_guess_answer[z] == test_lib[r]):
                                flag_test = 1
                    if (flag_test==0):
                        change_AB.append(test_lib)
                if(computer_guess_answer[1] == test_lib[3] and
                   computer_guess_answer[3] == test_lib[0]): # 13 30
                    flag_test = 0
                    for r in range(0,4):
                        for z in range(0,4):
                            if ( z==1 and r==3 or z==3 and r==0):
                                continue
                            if (computer_guess_answer[z] == test_lib[r]):
                                flag_test = 1
                    if (flag_test==0):
                        change_AB.append(test_lib)
                if(computer_guess_answer[1] == test_lib[3] and
                   computer_guess_answer[3] == test_lib[1]): # 13 31
                    flag_test = 0
                    for r in range(0,4):
                        for z in range(0,4):
                            if ( z==1 and r==3 or z==3 and r==1):
                                continue
                            if (computer_guess_answer[z] == test_lib[r]):
                                flag_test = 1
                    if (flag_test==0):
                        change_AB.append(test_lib)
                if(computer_guess_answer[1] == test_lib[3] and
                   computer_guess_answer[3] == test_lib[2]): # 13 32
                    flag_test = 0
                    for r in range(0,4):
                        for z in range(0,4):
                            if ( z==1 and r==3 or z==3 and r==2):
                                continue
                            if (computer_guess_answer[z] == test_lib[r]):
                                flag_test = 1
                    if (flag_test==0):
                        change_AB.append(test_lib)
                        
                
#**** 20
                if(computer_guess_answer[2] == test_lib[0] and
                   computer_guess_answer[3] == test_lib[1]): # 20 31
                    flag_test = 0
                    for r in range(0,4):
                        for z in range(0,4):
                            if ( z==2 and r==0 or z==3 and r==1):
                                continue
                            if (computer_guess_answer[z] == test_lib[r]):
                                flag_test = 1
                    if (flag_test==0):
                        change_AB.append(test_lib)
                if(computer_guess_answer[2] == test_lib[0] and
                   computer_guess_answer[3] == test_lib[2]): # 20 32
                    flag_test = 0
                    for r in range(0,4):
                        for z in range(0,4):
                            if ( z==2 and r==0 or z==3 and r==2):
                                continue
                            if (computer_guess_answer[z] == test_lib[r]):
                                flag_test = 1
                    if (flag_test==0):
                        change_AB.append(test_lib)
                if(computer_guess_answer[2] == test_lib[1] and
                   computer_guess_answer[3] == test_lib[0]): # 21 30
                    flag_test = 0
                    for r in range(0,4):
                        for z in range(0,4):
                            if ( z==2 and r==1 or z==3 and r==0):
                                continue
                            if (computer_guess_answer[z] == test_lib[r]):
                                flag_test = 1
                    if (flag_test==0):
                        change_AB.append(test_lib)
                if(computer_guess_answer[2] == test_lib[1] and
                   computer_guess_answer[3] == test_lib[2]): # 21 32
                    flag_test = 0
                    for r in range(0,4):
                        for z in range(0,4):
                            if ( z==2 and r==1 or z==3 and r==2):
                                continue
                            if (computer_guess_answer[z] == test_lib[r]):
                                flag_test = 1
                    if (flag_test==0):
                        change_AB.append(test_lib)
                if(computer_guess_answer[2] == test_lib[3] and
                   computer_guess_answer[3] == test_lib[0]): # 23 30
                    flag_test = 0
                    for r in range(0,4):
                        for z in range(0,4):
                            if ( z==2 and r==3 or z==3 and r==0):
                                continue
                            if (computer_guess_answer[z] == test_lib[r]):
                                flag_test = 1
                    if (flag_test==0):
                        change_AB.append(test_lib)
                if(computer_guess_answer[2] == test_lib[3] and
                   computer_guess_answer[3] == test_lib[1]): # 23 31
                    flag_test = 0
                    for r in range(0,4):
                        for z in range(0,4):
                            if ( z==1 and r==2 or z==3 and r==0):
                                continue
                            if (computer_guess_answer[z] == test_lib[r]):
                                flag_test = 1
                    if (flag_test==0):
                        change_AB.append(test_lib)
                if(computer_guess_answer[2] == test_lib[3] and
                   computer_guess_answer[3] == test_lib[2]): # 23 32
                    flag_test = 0
                    for r in range(0,4):
                        for z in range(0,4):
                            if ( z==2 and r==3 or z==3 and r==2):
                                continue
                            if (computer_guess_answer[z] == test_lib[r]):
                                flag_test = 1
                    if (flag_test==0):
                        change_AB.append(test_lib)
#************************0A1B*************************
        
        if (A_input ==  0 and B_input == 1):
            print('0a1b')
            for j in range(0,len(AB_lib)):
                test_lib = str(AB_lib[j])
                if(computer_guess_answer[0] == test_lib[1]): # 01 
                    flag_test = 0
                    for r in range(0,4):
                        for z in range(0,4):
                            if ( z==0 and r==1 ):
                                continue
                            if (computer_guess_answer[z] == test_lib[r]):
                                flag_test = 1
                    if (flag_test==0):
                        change_AB.append(test_lib)
                if(computer_guess_answer[0] == test_lib[2]): # 02
                    flag_test = 0
                    for r in range(0,4):
                        for z in range(0,4):
                            if ( z==0 and r==2 ):
                                continue
                            if (computer_guess_answer[z] == test_lib[r]):
                                flag_test = 1
                    if (flag_test==0):
                        change_AB.append(test_lib)
                if(computer_guess_answer[0] == test_lib[3]): # 03 
                    flag_test = 0
                    for r in range(0,4):
                        for z in range(0,4):
                            if ( z==0 and r==3 ):
                                continue
                            if (computer_guess_answer[z] == test_lib[r]):
                                flag_test = 1
                    if (flag_test==0):
                        change_AB.append(test_lib)
                if(computer_guess_answer[1] == test_lib[0]): # 10
                    flag_test = 0
                    for r in range(0,4):
                        for z in range(0,4):
                            if ( z==1 and r==0 ):
                                continue
                            if (computer_guess_answer[z] == test_lib[r]):
                                flag_test = 1
                    if (flag_test==0):
                        change_AB.append(test_lib)
                if(computer_guess_answer[1] == test_lib[2]): # 12
                    flag_test = 0
                    for r in range(0,4):
                        for z in range(0,4):
                            if ( z==1 and r==2 ):
                                continue
                            if (computer_guess_answer[z] == test_lib[r]):
                                flag_test = 1
                    if (flag_test==0):
                        change_AB.append(test_lib)
                if(computer_guess_answer[1] == test_lib[3]):# 13
                    flag_test = 0
                    for r in range(0,4):
                        for z in range(0,4):
                            if ( z==1 and r==3 ):
                                continue
                            if (computer_guess_answer[z] == test_lib[r]):
                                flag_test = 1
                    if (flag_test==0):
                        change_AB.append(test_lib)
                if(computer_guess_answer[2] == test_lib[0]): # 20 
                    flag_test = 0
                    for r in range(0,4):
                        for z in range(0,4):
                            if ( z==2 and r==0 ):
                                continue
                            if (computer_guess_answer[z] == test_lib[r]):
                                flag_test = 1
                    if (flag_test==0):
                        change_AB.append(test_lib)
                if(computer_guess_answer[2] == test_lib[1]): # 21 
                    flag_test = 0
                    for r in range(0,4):
                        for z in range(0,4):
                            if ( z==2 and r==1 ):
                                continue
                            if (computer_guess_answer[z] == test_lib[r]):
                                flag_test = 1
                    if (flag_test==0):
                        change_AB.append(test_lib)
                if(computer_guess_answer[2] == test_lib[3]): # 23 
                    flag_test = 0
                    for r in range(0,4):
                        for z in range(0,4):
                            if ( z==2 and r==3 ):
                                continue
                            if (computer_guess_answer[z] == test_lib[r]):
                                flag_test = 1
                    if (flag_test==0):
                        change_AB.append(test_lib)
                if(computer_guess_answer[3] == test_lib[0]): # 30 
                    flag_test = 0
                    for r in range(0,4):
                        for z in range(0,4):
                            if ( z==3 and r==0 ):
                                continue
                            if (computer_guess_answer[z] == test_lib[r]):
                                flag_test = 1
                    if (flag_test==0):
                        change_AB.append(test_lib)
                if(computer_guess_answer[3] == test_lib[1]): # 31
                    flag_test = 0
                    for r in range(0,4):
                        for z in range(0,4):
                            if ( z==3 and r==1 ):
                                continue
                            if (computer_guess_answer[z] == test_lib[r]):
                                flag_test = 1
                    if (flag_test==0):
                        change_AB.append(test_lib)
                if(computer_guess_answer[3] == test_lib[2]): # 32
                    flag_test = 0
                    for r in range(0,4):
                        for z in range(0,4):
                            if ( z==3 and r==2 ):
                                continue
                            if (computer_guess_answer[z] == test_lib[r]):
                                flag_test = 1
                    if (flag_test==0):
                        change_AB.append(test_lib)
#*************************************0A0B***********************************************
        if (A_input == 0 and B_input == 0):
             for j in range(0,len(AB_lib)): 
                flag_test = 0
                test_lib = str(AB_lib[j])
                for r in range(0,4):
                    for z in range(0,4):
                        if (computer_guess_answer[z] == test_lib[r]):
                            flag_test = 1
                if (flag_test==0):
                    change_AB.append(test_lib)
#****************************************** 1A0B***************************************************************
        if (A_input == 1 and B_input == 0):   #computer_guess_answer = str(AB_lib[0])
            for j in range(0,len(AB_lib)):
                test_lib = str(AB_lib[j])
                if(computer_guess_answer[0] == test_lib[0]):
                    flag_test = 0
                    for r in range(1,4):
                        for z in range(1,4):
                            if (computer_guess_answer[z] == test_lib[r]):
                                flag_test = 1
                    if (flag_test==0):
                        change_AB.append(test_lib)
                if(computer_guess_answer[1] == test_lib[1]):
                    flag_test = 0
                    for r in range(0,4):
                        for z in range(0,4):
                            if (r==1 or z==1):
                                continue
                            if (computer_guess_answer[z] == test_lib[r]):
                                flag_test = 1
                    if (flag_test==0):
                        change_AB.append(test_lib)
                if(computer_guess_answer[2] == test_lib[2]):
                    flag_test = 0
                    for r in range(0,4):
                        for z in range(0,4):
                            if (r==2 or z==2):
                                continue
                            if (computer_guess_answer[z] == test_lib[r]):
                                flag_test = 1
                    if (flag_test==0):
                        change_AB.append(test_lib)
                if(computer_guess_answer[3] == test_lib[3]):
                    flag_test = 0
                    for r in range(0,4):
                        for z in range(0,4):
                            if (r==3 or z==3):
                                continue
                            if (computer_guess_answer[z] == test_lib[r]):
                                flag_test = 1
                    if (flag_test==0):
                        change_AB.append(test_lib)
#******************************************************2A0B START***********************************
        if (A_input == 2 and B_input == 0):
             for j in range(0,len(AB_lib)):
                test_lib = str(AB_lib[j])
                if(computer_guess_answer[0] == test_lib[0] and computer_guess_answer[1] == test_lib[1]): # 01 
                    flag_test = 0
                    for r in range(0,4):
                        for z in range(0,4):
                            if (r==1 or z==1 or r==0 or z==0):
                                continue
                            if (computer_guess_answer[z] == test_lib[r]):
                                flag_test = 1
                    if (flag_test==0):
                        change_AB.append(test_lib)
                if(computer_guess_answer[0] == test_lib[0] and computer_guess_answer[2] == test_lib[2]):# 02
                    flag_test = 0
                    for r in range(0,4):
                        for z in range(0,4):
                            if (r==2 or z==2 or r==0 or z==0):
                                continue
                            if (computer_guess_answer[z] == test_lib[r]):
                                flag_test = 1
                    if (flag_test==0):
                        change_AB.append(test_lib)

                if(computer_guess_answer[0] == test_lib[0] and computer_guess_answer[3] == test_lib[3]):# 03 
                    flag_test = 0
                    for r in range(0,4):
                        for z in range(0,4):
                            if (r==3 or z==3 or r==0 or z==0):
                                continue
                            if (computer_guess_answer[z] == test_lib[r]):
                                flag_test = 1
                    if (flag_test==0):
                        change_AB.append(test_lib)

                if(computer_guess_answer[1] == test_lib[1] and computer_guess_answer[2] == test_lib[2]):# 12 
                    flag_test = 0
                    for r in range(0,4):
                        for z in range(0,4):
                            if (r==1 or z==1 or r==2 or z==2):
                                continue
                            if (computer_guess_answer[z] == test_lib[r]):
                                flag_test = 1
                    if (flag_test==0):
                        change_AB.append(test_lib)
                if(computer_guess_answer[1] == test_lib[1] and computer_guess_answer[3] == test_lib[3]):# 13 
                    flag_test = 0
                    for r in range(0,4):
                        for z in range(0,4):
                            if (r==1 or z==1 or r==3 or z==3):
                                continue
                            if (computer_guess_answer[z] == test_lib[r]):
                                flag_test = 1
                    if (flag_test==0):
                        change_AB.append(test_lib)
                if(computer_guess_answer[2] == test_lib[2] and computer_guess_answer[3] == test_lib[3]):# 23
                    flag_test = 0
                    for r in range(0,4):
                        for z in range(0,4):
                            if (r==2 or z==2 or r==3 or z==3):
                                continue
                            if (computer_guess_answer[z] == test_lib[r]):
                                flag_test = 1
                    if (flag_test==0):
                        change_AB.append(test_lib)
#***********************************3A0B********************************************
        if (A_input == 3 and B_input == 0):
             for j in range(0,len(AB_lib)):
                test_lib = str(AB_lib[j])
                if(computer_guess_answer[0]==test_lib[0] and computer_guess_answer[1]==test_lib[1] and
                   computer_guess_answer[2]==test_lib[2]): 
                    flag_test = 0
                    for r in range(0,4):
                        for z in range(0,4):
                            if (r==1 or z==1 or r==0 or z==0 or r==2 or z==2):
                                continue
                            if (computer_guess_answer[z] == test_lib[r]):
                                flag_test = 1
                    if (flag_test==0):
                        change_AB.append(test_lib)
                if(computer_guess_answer[0]==test_lib[0] and computer_guess_answer[1]==test_lib[1] and
                   computer_guess_answer[3]==test_lib[3]):
                        flag_test = 0
                        for r in range(0,4):
                            for z in range(0,4):
                                if (r==1 or z==1 or r==0 or z==0 or r==3 or z==3):
                                    continue
                                if (computer_guess_answer[z] == test_lib[r]):
                                    flag_test = 1
                        if (flag_test==0):
                            change_AB.append(test_lib)
                if(computer_guess_answer[1]==test_lib[1] and computer_guess_answer[2]==test_lib[2] and
                   computer_guess_answer[3]==test_lib[3]):
                        flag_test = 0
                        for r in range(0,4):
                            for z in range(0,4):
                                if (r==1 or z==1 or r==3 or z==3 or r==2 or z==2):
                                    continue
                                if (computer_guess_answer[z] == test_lib[r]):
                                    flag_test = 1
                        if (flag_test==0):
                            change_AB.append(test_lib)
                if(computer_guess_answer[0]==test_lib[0] and computer_guess_answer[3]==test_lib[3] and
                   computer_guess_answer[2]==test_lib[2]):
                        flag_test = 0
                        for r in range(0,4):
                            for z in range(0,4):
                                if (r==3 or z==3 or r==0 or z==0 or r==2 or z==2):
                                    continue
                                if (computer_guess_answer[z] == test_lib[r]):
                                    flag_test = 1
                        if (flag_test==0):
                            change_AB.append(test_lib)
        
#******************************************************************************************************************************
        if (A_input != 4):    
            AB_lib = change_AB
##        print(AB_lib)
        left_lib[count_3-1][0:len(AB_lib)-1]=AB_lib
        return AB_lib
class playway(Screen):
    def __init__(self,**kw):
        super(playway,self).__init__(**kw)
        Clock.schedule_once(self.button_name, -1)
    def button_name(self, dt):
        self.ids.how.text=u'玩法'
        self.ids.how.font_name='DroidSansFallback.ttf'
        self.ids.how.font_size=100

        self.ids.how_one.text=u'這是一個個人進行的益智數學遊戲。\n\
首先電腦或玩家會想好一組由左至\n\
右排列好的四個數碼（數字0不可以\n\
在最前面，且數碼不可以重複出現\n\
被使用），例如1847，讓玩者去猜\n\
。猜題後電腦會給猜題者提示，譬\n\
如玩者猜了6149，則提示是1A1B，\n\
其中A表示有這個數字，且數字是在\n\
正確的位置，B表示有這個數字，但\n\
位置不對因為數字4被猜對了位置也\n\
正確，而數字1被雖猜對了但位置不\n\
正確，所以得到1A1B。用這樣的遊\n\
戲規則，看能否最少的步驟猜中電\n\
腦中設的數字。(輸入時: 若不填數\n\
字 默認為0)(當電腦猜對時填4a即可)'
        self.ids.how_one.font_name='DroidSansFallback.ttf'
##        self.ids.how_one.font_size=25
        self.ids.leave.text=u'離開'
        self.ids.leave.font_name='DroidSansFallback.ttf'



class ScreenManagement(ScreenManager):
    pass


presentation = Builder.load_file("main.kv")
class AB_Game(App):
    def __init__(self,**kw):
        super(AB_Game,self).__init__(**kw)
        Window.bind(on_key_down=self.Android_back_click)       
    def Android_back_click(self,window,key,*args):
        if key in  (1000,27):
            try:
                popup.dismiss()
                popup87.dismiss()
            except:
                pass
            if self.root.current =='MainScreen':
                return False
            elif self.root.current =='tocomputer':
                self.root.current='MainScreen'
            elif self.root.current =='show_detail':
                self.root.current='show_analysis'
            elif self.root.current =='show_analysis':
                self.root.current='data'
            elif self.root.current =='data':
                self.root.current='MainScreen'
            elif self.root.current =='toplayer':
                pass
            elif self.root.current =='playway':
                self.root.current='MainScreen'
            elif self.root.current =='player':
                pass
            elif self.root.current =='computer':
                pass
            
            return True

    def build(self):
        return presentation
if __name__=="__main__":
    AB_Game().run()
