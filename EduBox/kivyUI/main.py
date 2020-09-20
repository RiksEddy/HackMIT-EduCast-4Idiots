from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.factory import Factory
from kivy.properties import ObjectProperty

from src.evince_vlc_ir import open_file

import os

#Window.fullscreen = 'auto' - Problems with returning to window after playback
Window.maximize()

class Root(FloatLayout): #Uses Root Layout in kv file
    def file_open(self, path, filename): #Calls function to start subprocesses
        if filename[0].endswith(".mp4"):
            open_file(os.path.join(path, filename[0]), ".mp4")
        elif filename[0].endswith(".pdf"):
            open_file(os.path.join(path, filename[0]), ".pdf")

class Browser(App): #Runs App
    pass

Factory.register('Root', cls=Root)

Browser().run()
