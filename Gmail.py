from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivymd.uix.navigationdrawer import MDNavigationDrawerMenu
from kivy.uix.screenmanager import ScreenManager,Screen
from kivymd.uix.list import ThreeLineAvatarIconListItem,ImageLeftWidget
from kivymd.icon_definitions import md_icons
from kivymd.uix.list import ThreeLineAvatarIconListItem
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.button import MDFloatingActionButton
import os,string,random

class Drawer_Menu(MDNavigationDrawerMenu):
    ...
class Inbox_screen(Screen):
    ...

class ListItem(ThreeLineAvatarIconListItem):
    '''Custom list item.'''
class Screen_Manager(ScreenManager):
    ...
class TopBar(MDTopAppBar):
    def __init__(self,*args,**kwargs):
        super(TopBar,self).__init__(*args,**kwargs)
        self.elevation=0
        self.size_hint_y=0.09       
        self.pos_hint= {"top":1}
        self.md_bg_color= "#DC4437"
        self.specific_text_color= 1,1,1,1

class Floatingbutton(MDFloatingActionButton):
    def __init__(self,*args,**kwargs):
        super(Floatingbutton,self).__init__(*args,**kwargs)
        self.icon= "pencil"
        self.levation:0
        self.md_bg_color="#DC4437"
        self.pos_hint={"center_x":.88,"center_y":.07}
            
class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        return Builder.load_file(os.path.join("Kivy_GUI_files/MY_pro","Gmail.kv"))
    
    def on_start(self):
        self.Generate_Emails(self.root.ids.inbox,20)
        
    def Generate_Emails(self,widget_id,num):
        for _ in range(num):
            letter = random.choice([let for let in string.ascii_uppercase])
            widget_id.add_widget(
                    ThreeLineAvatarIconListItem(
                        ImageLeftWidget(source= f"/storage/emulated/0/Kivy_GUI_files/MY_pro/Letters/{letter}.png",), 
                        text= "Sender",
                        secondary_text= "Email About",
                        tertiary_text= "Email Body....",
                        )
                            )
            
    def Main(self,screen_manager):
        screen_manager.current="first"
    
    def Starred(self,screen_manager):
        screen_manager.current="starred"
    
    def Important(self,screen_manager):
        screen_manager.current="important"
        self.Generate_Emails(self.root.ids.important_,10)
     
    def Sent(self,screen_manager):
        screen_manager.current="sent"
        self.Generate_Emails(self.root.ids.sent_,15)
        
    def Outbox(self,screen_manager):
        screen_manager.current="outbox"
        self.Generate_Emails(self.root.ids.outbox_,4)
        
    def All_mails(self,screen_manager):
        screen_manager.current="first"
        self.Generate_Emails(self.root.ids.all_mail_,25)
        
    def Drafts(self,screen_manager):
        screen_manager.current="drafts"
        self.Generate_Emails(self.root.ids.draft_,5)
        
    def Spam(self,screen_manager):
        screen_manager.current="spam"
        self.Generate_Emails(self.root.ids.spam_,5)
        
    def Trash(self,screen_manager):
        screen_manager.current="trash"
        self.Generate_Emails(self.root.ids.trash_,3)
    
MainApp().run()