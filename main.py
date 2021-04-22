from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.core.audio import SoundLoader
from kivy.uix.screenmanager import ScreenManager, Screen, WipeTransition
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivymd.uix.label import MDLabel
from kivy.utils import get_color_from_hex
from kivy.uix.button import Button
from kivy.animation import Animation
from kivy.clock import Clock
from datetime import datetime
from congrat import Congrat
from kivymd.toast import toast
from kivy.config import Config


class Starting(Screen, FloatLayout):
    pass

class Main(Screen):
    pass


class MainApp(MDApp):
    ind= 0
    minutes= 0
    sub_mins= 0
    secs= range(59, -1, -1)
    is50= 'no'
    isbreak= False

    def build(self):
        Config.set('graphics', 'resizable', False)
        Window.size= (360, 640)
        Window.minimum_width, Window.minimum_height = (360, 640)
        return Builder.load_file("main.kv")

    def enable_btn(self, name, *args):
        self.btn.disabled= False
        with open('data/username.txt', 'w') as file:
            file.write(name.strip())

    def on_start(self):
        card= self.root.ids.start_screen.ids['the_card']
        self.btn= self.root.ids.start_screen.ids['btn']
        with open('data/username.txt', 'r') as username:
            content= username.read()
        if content == '':
            card.height= 150
            self.btn.disabled= True
            self.container= FloatLayout()
            self.text= Label(text='let us know your username:',
                             size_hint=[.7, .2],
                             pos_hint={"top":.95, 'x':.1},
                             font_size='20sp',
                             bold=True,
                             color=[0,0,0,1])
            self.feild= TextInput(background_color=get_color_from_hex('#730000'),
                             size_hint=[.9, .3],
                             pos_hint={"top":.6, 'center_x':.5},
                             hint_text='your username...'.upper(),
                             hint_text_color=[0,0,0,1],
                             multiline=False)
            self.butn= Button(text='Done',
                             background_normal='',
                             color=[0,0,0,1],
                             background_color=get_color_from_hex('#730088'),
                             size_hint=[.9, .2],
                             pos_hint={"top":.25, 'center_x':.5},
                             font_size="20sp",
                             bold=True)
            self.butn.bind(on_release= lambda x: self.enable_btn(self.feild.text) if
                           self.feild.text!='' else print('enter your name'))
            self.container.add_widget(self.text)
            self.container.add_widget(self.feild)
            self.container.add_widget(self.butn)
            card.add_widget(self.container)
        elif content != '':
            card.height= 190
            self.container= FloatLayout()
            self.text1= Label(text='Welcome Back {}!'.format(content.title()),
                              size_hint=[.8, .2],
                              pos_hint={"top":.95, 'x':.1},
                              font_size='27sp',
                              bold=True,
                              color=[0,0,0,1])
            self.text2= Label(text='HAPPY FOCUS :)',
                              size_hint=[.6, .2],
                              pos_hint={"top":.23, 'x':.1},
                              font_size='27sp',
                              bold=True,
                              color=[0,0,0,1])
            self.para= Label(text='''make sure that you\'re not surrounded\nby any sort of distractions...\nyou can click the green button\nwhenever you\'re ready.''',
                             font_size='17sp',
                             size_hint=[.7, .4],
                             pos_hint={"top":.7, 'x':.18},
                             color= [0,0,0,1])
            self.container.add_widget(self.text1)
            self.container.add_widget(self.para)
            self.container.add_widget(self.text2)
            card.add_widget(self.container)

    def switch_to_main(self):
        manager= self.root.ids.screen_manager
        manager.transition= WipeTransition()
        manager.transition.duration= 0.8
        manager.current= 'main_screen'

    def get_time(self, period):
        self.minutes= period
        self.updater=Clock.schedule_interval(self.countdown, 1)
        self.play_sound()

    def countdown(self, *args):
        timer_lbl= self.root.ids.main_screen.ids.timer
        btn25= self.root.ids.main_screen.ids.the25
        btn50= self.root.ids.main_screen.ids.the50
        timer= [1,1]
        if self.minutes == 0 and self.ind == 60:
            if self.isbreak == True:
                self.call_popup()
                toast('Take a Break!', 1)
            else: pass
            self.stop_it()
            self.updater.cancel() #this function cancels the countdown
            btn25.disabled= False
            btn50.disabled= False
        else:
            if self.ind == 60:
                self.ind=0
                self.seconds= self.secs[self.ind]
                self.ind+=1
            else:
                self.seconds= self.secs[self.ind]
                self.ind+=1
            timer[1]=str(self.seconds)
            if timer[1] == '59':
                #self.sub_mins+=1
                self.minutes= self.minutes - 1
            else:
                pass
            timer[0]=str(self.minutes)
            timer_lbl.text= f'{timer[0].zfill(2)}:{timer[1].zfill(2)}'
            self.clock_highlighting()

    def clock_highlighting(self):
        self.min_nums= [self.root.ids.main_screen.ids.n1, self.root.ids.main_screen.ids.n2,
                    self.root.ids.main_screen.ids.n3, self.root.ids.main_screen.ids.n4,
                    self.root.ids.main_screen.ids.n5, self.root.ids.main_screen.ids.n6,
                    self.root.ids.main_screen.ids.n7, self.root.ids.main_screen.ids.n8,
                    self.root.ids.main_screen.ids.n9, self.root.ids.main_screen.ids.n10,
                    self.root.ids.main_screen.ids.n11, self.root.ids.main_screen.ids.n12,
                    self.root.ids.main_screen.ids.n13]
        if (self.is50 == 'yes' and self.minutes == 20) and self.ind == 60:
            self.min_nums[6].color= [0,1,0,1]
        elif  (self.is50 == 'yes' and self.minutes == 15) and self.ind == 60:
            self.min_nums[7].color= [0,1,0,1]
        elif  (self.is50 == 'yes' and self.minutes == 10) and self.ind == 60:
            self.min_nums[8].color= [0,1,0,1]
        elif  (self.is50 == 'yes' and self.minutes == 5) and self.ind == 60:
            self.min_nums[9].color= [0,1,0,1]
        elif  (self.is50 == 'yes' and self.minutes == 0) and self.ind == 60:
            self.min_nums[10].color= [0,1,0,1]
        elif (self.minutes == 24 or self.minutes == 49) and self.ind == 60:
            self.min_nums[0].color= [0,1,0,1]
        elif (self.minutes == 20 or self.minutes == 45) and self.ind == 60:
            self.min_nums[1].color= [0,1,0,1]
        elif (self.minutes == 15 or self.minutes == 40) and self.ind == 60:
            self.min_nums[2].color= [0,1,0,1]
        elif (self.minutes == 10 or self.minutes == 35) and self.ind == 60:
            self.min_nums[3].color= [0,1,0,1]
        elif (self.minutes == 5 or self.minutes == 30) and self.ind == 60:
            self.min_nums[4].color= [0,1,0,1]
        elif(self.minutes == 0 or self.minutes == 25) and self.ind == 60:
            self.min_nums[5].color= [0,1,0,1]
        else: pass

    # gives all self.min_nums a black color
    def reseter(self):
        for lbl in self.min_nums:
            lbl.color= [0,0,0,1]

    def stop_it(self):
        tbtn25= self.root.ids.main_screen.ids.the25
        rr= self.root.ids.main_screen.ids.tt
        tbtn50= self.root.ids.main_screen.ids.the50
        ttimer_lbl= self.root.ids.main_screen.ids.timer
        stoper= self.root.ids.main_screen.ids.stop_timer
        self.updater.cancel()
        tbtn25.disabled= False
        tbtn50.disabled= False
        stoper.disabled= True
        rr.source='imgs/timer.png'
        ttimer_lbl.text= '00:00'
        self.reseter()
        self.ind= 0
        self.minutes= 0
        self.sub_mins= 0
        self.secs= range(59, -1, -1)
        self.sound.stop()

    def call_popup(self):
        pop= Congrat(app)
        pop.open()
        self.pomodone_sound()

    def play_sound(self):
        self.sound= SoundLoader.load('sounds/tick.wav')
        self.sound.play()

    def pomodone_sound(self):
        self.noise= SoundLoader.load('sounds/noise.wav')
        self.noise.play()

    def reset_btns(self):
        self.root.ids.main_screen.ids.the25.disabled= True
        self.root.ids.main_screen.ids.the50.disabled= True
        self.root.ids.main_screen.ids.stop_timer.disabled= False

if __name__ == '__main__':
    app= MainApp()
    app.run()
