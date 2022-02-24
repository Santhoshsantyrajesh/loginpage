import pyrebase
from kivymd.app import MDApp
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.screen import MDScreen
from kivy.clock import Clock
from kivy.uix.widget import Widget
from kivymd.uix.dialog import MDDialog
from kivy.uix.textinput import TextInput
from kivy.config import Config
from kivymd.uix.label import MDLabel
from kivy.core.window import Window
from kivy.lang import Builder

s="""
Screen:
    name:"login"
    MDFloatLayout:

        MDTextField:
            id: email
            hint_text: "Enter username"
            helper_text: "or click on forgot username"
            helper_text_mode: "on_focus"
            icon_right: "android"
            icon_right_color: app.theme_cls.primary_color
            pos_hint:{'center_x': 0.5, 'center_y': 0.7}
            size_hint_x:None
            width:300

        MDTextField:
            id: password
            hint_text: "Enter password"
            helper_text: "or click on forgot password"
            helper_text_mode: "on_focus"
            icon_right: "lock"
            icon_right_color: app.theme_cls.primary_color
            pos_hint:{'center_x': 0.5, 'center_y': 0.58}
            size_hint_x:None
            width:300
        MDRaisedButton:
            text:"LOGIN"
            pos_hint:{'center_x': 0.6, 'center_y': 0.4}
            md_bg_color: 1, 0, 1, 1
            on_release:app.user()
        MDRaisedButton:
            text:"SIGNUP"
            pos_hint:{'center_x': 0.4, 'center_y': 0.4}
            md_bg_color: 1, 0, 1, 1
            on_release:app.user()
        """
LO = '''
MDScreen:
    name:"pre"
    MDFloatLayout:
        md_bg_color: 115/255.0, 62/255.0, 198/255.0, 1
        MDLabel:
            text:"Welcome"
            pos_hint:{"center_x": .5, "center_y": .2}
            halign:"center"
            theme_text_color:"Custom"
            text_color: 1, 1, 1, 1
            font_size:"35sp"
        MDLabel:
            text:"App by santhoshkumar"
            pos_hint:{"center_x": .5, "center_y": .15}
            halign:"center"
            theme_text_color:"Custom"
            text_color: 1, 1, 1, 1
            font_size:"14sp"

     '''

class MenuScreen(Screen):
    pass


class ProfileScreen(Screen):
    pass


class UploadScreen(Screen):
    pass
firebaseConfig = {
  'apiKey': "AIzaSyDm-LJynXuZNWoq_50Wrd9puKarelUP6Uc",
  'authDomain': "santhosh-5732d.firebaseapp.com",
  'databaseURL': "https://santhosh-5732d-default-rtdb.firebaseio.com",
  'projectId': "santhosh-5732d",
  'storageBucket': "santhosh-5732d.appspot.com",
  'messagingSenderId': "544817255699",
  'appId': "1:544817255699:web:c2a46412443e68707776e6",
  'measurementId': "G-DMQXCVBR0Q"
}
firebase=pyrebase.initialize_app(firebaseConfig)
auth=firebase.auth()

class DemoApp(MDApp):
    def build(self):
        screen = Screen()
        Builder.load_string(LO)
        kv = Builder.load_string(s)
        return kv
    def user(self):
        email = self.root.ids.email.text
        password=self.root.ids.password.text
        try:
            auth.create_user_with_email_and_password(email,password)

        except:
            print("unsucess")

if __name__ == "__main__":
    DemoApp().run()