from kivy.utils import get_color_from_hex
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.card import MDCard
from kivy.uix.label import Label
from kivy.uix.button import Button, ButtonBehavior


class TheCard(MDCard):
    def __init__(self, **kwargs):
        super(TheCard, self).__init__(**kwargs)
        self.size_hint=[.98,.2]
        self.orientation='vertical'
        self.pos_hint={'top':.98, 'center_x':.5}                      
        self.md_bg_color=get_color_from_hex('#730000')
        self.elevation=0


class LabelBtn(ButtonBehavior, Label):
    pass


class Congrat(Popup):
    def __init__(self,the_app,**kwargs):
        super(Congrat, self).__init__(**kwargs)
        self.app= the_app
        self.app.isbreak= False
        self.auto_dismiss= False
        self.size_hint= [None, None]
        self.size= [340, 380]
        self.pos_hint= {'top':.8, 'center_x':.5}
        self.title= "CONGRATULATIONS!!!"
        self.title_align= 'center'
        self.title_color= get_color_from_hex('#730000')
        self.title_size= '23sp'
        self.separator_color= get_color_from_hex('#730000')
        self.separator_height= 5
        self.container0= FloatLayout(size_hint=[1,1])
        self.the_card= TheCard()
        self.caption1= Label(text='Well Done, {}!'.format(self.get_name()),
                            size_hint=[.4, .05],
                            font_size='30sp',
                            pos_hint={'top':1, "center_x":.5},
                            bold=True, color=[0,0,0,1])
        self.caption2= Label(text='you\'ve just finished an entire\nPomoDoro, keep going until you\'re\ndone with all of your assignments...',
                            size_hint=[.6, .35],
                            pos_hint={'top':.8, 'x':.18},
                            font_size='18sp',color=get_color_from_hex('#730000'))
        self.break_btn= Button(size_hint=[.98, .13],
                            pos_hint={'top':.45, 'center_x':.5},
                            text='Take a Break',
                            background_normal='',
                            background_color=get_color_from_hex('#216802'),
                            bold=True, font_size='20sp', color=[0,0,0,1])
        self.skip_btn= LabelBtn(text='skip to next pomodoro.',
                            size_hint=[.8, .05],
                            font_size='20sp',
                            pos_hint={'top':.25, 'center_x':.5},
                            underline=True, color=get_color_from_hex('#216802'))
        self.skip_btn.bind(on_release=lambda x: self.dismiss())
        self.break_btn.bind(on_press=lambda x:self.app.get_time(5))
        self.break_btn.bind(on_press= self.change_img)
        self.break_btn.bind(on_release=lambda x: self.dismiss())
        self.the_card.add_widget(self.caption1)
        self.container0.add_widget(self.caption2)
        self.container0.add_widget(self.break_btn)
        self.container0.add_widget(self.skip_btn)
        self.container0.add_widget(self.the_card)
        self.add_widget(self.container0)
    
    @staticmethod
    def get_name():
        with open('data/username.txt', 'r') as f:
            name= f.read()
        return name.title()

    def change_img(self, *args):
        self.app.root.ids.main_screen.ids.tt.source='imgs/timer2.png'
        self.app.reseter()
        self.app.reset_btns()