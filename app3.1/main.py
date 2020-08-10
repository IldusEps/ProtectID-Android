# -*- coding: utf-8 -*-
"""
Created on Wed May 13 17:05:27 2020

@author: Ильдус Яруллин
"""


import os
from kivymd.app import MDApp
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.uix.image import AsyncImage

from kivymd.theming import ThemableBehavior
from kivymd.uix.list import OneLineListItem, MDList
from kivy.properties import StringProperty
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.clock import Clock
import platform
import time

from kivy.storage.jsonstore import JsonStore
from kivy.graphics.texture import Texture
from kivy.uix.camera import Camera
from kivy.graphics.opengl import glReadPixels
from kivy.utils import platform

from jnius import autoclass
from jnius import JavaException
try:
	from android.permissions import request_permissions, Permission
except:
			print('Error_permissions_importpackage')
print('Hi')
#Window.size=[240,480]
Window.clearcolor = (0, 0.67, 1, 1) #00abff

Activity = autoclass('org.kivy.android.PythonActivity')
activity = Activity.mActivity

class ContentNavigationDrawer(BoxLayout):
    pass

class myCamera(Camera):
	pass

class NavLayout(Screen):
	pass


class ItemDrawer(OneLineListItem):
    icon = StringProperty()


class DrawerList(ThemableBehavior, MDList):
	def set_color_item(self, instance_item):
		"""Called when tap on a menu item."""

		# Set the color of the icon and text for the menu item.
		for item in self.children:
			if item.text_color == self.theme_cls.primary_color:
				item.text_color = self.theme_cls.text_color
				break
		instance_item.text_color = self.theme_cls.primary_color
		if instance_item.text=="Лица":
			App.root.current="face"
		elif instance_item.text=="Главная":
			App.root.current="menu"

class PredictContainer(Screen):
	def on_enter(self):
		self.cam = myCamera(index=1,play=True, size_hint=(1,0.75),resolution = (1280, 960), pos_hint={'center_x':0.5,'center_y':0.5})
		self.add_widget(self.cam)
		#Clock.schedule_once(self.update, 6.0)
	def on(self):
		self.cam.export_to_png(filename="predict.png")
		Clock.schedule_once(self.update, 2.0)

	def update(self,dt):
		if activity.Predict("predict.png")==True:
			App.root.Form2()
		else:
			self.ident.text="Ошибка-повторите идентификацию"
			#self.ident.
	#def update(self,dt):
	#	Activity = autoclass('org.kivy.android.PythonActivity')
	#	activity = Activity.mActivity
	#	self.cam.export_to_png(filename="predict.png")
	#	if activity.Predict("predict.png")==True:
	#		App.root.Form2()
	#	else:
	#		Clock.schedule_once(self.update, 3.0)

class MainContainer(Screen):    
	def on_enter(self):
		if (App.store.exists('use')==True):
			if (App.store.get('use')['uses']=='2'):
				self.startStop.state="down"
	def StartStop(self,state):
		if state == 'down':
			App.store.put('use',uses='2',id_=App.store.get('use')['id_'])
			
			activity.restartNotify()
		else:
			print(state)
			activity.stopNotify()
			App.store.put('use',uses='1',id_=App.store.get('use')['id_'])
	def Start(self):
		App.store.put('use',uses='0',id_='0')

class TrainContainer(Screen):
	def train(self):
		print('HiGGG')
		if platform=="android":
			Hardware = autoclass('org.myapp.Hardware')
			hardware = Hardware()
			hardware.train()
			time.sleep(4)
		App.root.Form2()
class FImage(AsyncImage):
	pass
class FaceContainer(Screen):
	def on_enter(self):
		icons_item = {"-1": "Главная","0": "Лица","1": "Контакты"}
		App.root.current_screen.nav_layout.content_drawer.ids.md_list.add_widget(ItemDrawer(text=icons_item["-1"]))
		App.root.current_screen.nav_layout.content_drawer.ids.md_list.add_widget(ItemDrawer(text=icons_item["0"]))
		App.root.current_screen.nav_layout.content_drawer.ids.md_list.add_widget(ItemDrawer(text=icons_item["1"]))
		images=activity.Images()
		for image in images:
			print(image)
			self.grid.add_widget(FImage(source=image,size_hint=[1,1]))
	def first(self):
		App.root.current="first"
	def delete(self):
		activity.delete(self.grid.index+1)
		
bb=0
class firstContainer(Screen):
	i=1
	def on(self):
		timestr = time.strftime("%Y%m%d_%H%M%S")
		self.cam.export_to_png(filename=App.store.get('use')['id_']+'-selfie_'+str(self.i)+".png")
		self.i=self.i+1
		if self.i==6:
			App.root.current="train"
			App.store.put('use',uses='1',id_=App.store.get('use')['id_'])
	def enter(self):
		print('Hi1')
		self.i=1
		self.cam = myCamera(index=1,play=True, size_hint=(1,0.75),resolution = (1280, 960), pos_hint={'center_x':0.5,'center_y':0.5})
		print('Hi1')
		self.add_widget(self.cam)
		print('hi')
		App.store.put('use',id_=str(len(activity.Images())),uses=App.store.get('use')['uses'])

class StartContainer(Screen):
    pass

class Container(Screen):
	def __new__(secondContainer, *args, **kwargs):
		return super().__new__(secondContainer)
	
	def Start_(self):
		print('Hi')
		App.root.current='menu'
		icons_item = {"0": "Лица","1": "Контакты"}
		App.root.current_screen.nav_layout.content_drawer.ids.md_list.add_widget(ItemDrawer(text=icons_item["0"]))
		App.root.current_screen.nav_layout.content_drawer.ids.md_list.add_widget(ItemDrawer(text=icons_item["1"]))
        #lock.schedule_interval(App.root.current_screen.update, 1.0)

	def change_image(self,LR):
		if LR=='R':
			self.img_start.load_next()

			if self.img_start.index+1==2:
				self.arrow_rigth.size_hint=0,0.05
			else:
				self.arrow_left.size_hint=0.05,0.05
				self.arrow_rigth.size_hint=0.05,0.05
		elif LR=='L':
			self.img_start.load_previous()
			if self.img_start.index-1==0:
				self.arrow_left.size_hint=0,0.05
			else:
				self.arrow_left.size_hint=0.05,0.05
				self.arrow_rigth.size_hint=0.05,0.05

class sm(ScreenManager):
	def Enter_(self):
		print('Hi')
		#self.add_widget(facesContainer(name="faces"))
		if (App.store.exists('use')==False):
			App.store.put('use',uses='0',id_='0')
			print('Hi')
		if (App.store.get('use')['uses']=='0'):
			print('Hi')
			self.current='first'
			print('Hi')
		elif (App.store.get('use')['uses']=='2') or (App.store.get('use')['uses']=='1'):
			k=0
			self.current="predict"
		print(self.current)
	
	def Form2(self):
		self.current='menu'
		icons_item = {"0": "Лица","1": "Контакты"}
		print(icons_item["0"])
		self.current_screen.nav_layout.ids.content_drawer.ids.md_list.add_widget(ItemDrawer(text=icons_item["0"]))
		print(icons_item["1"])
		self.current_screen.nav_layout.ids.content_drawer.ids.md_list.add_widget(ItemDrawer(text=icons_item["1"]))
		
        
        

class MyApp(MDApp):
	store=JsonStore('Parametr.json')
	def build(self):
		#self.icon_folder=
		try:
			request_permissions([Permission.CAMERA,Permission.WRITE_EXTERNAL_STORAGE,Permission.READ_EXTERNAL_STORAGE])
		except:
			print('Error_permissions')
		Sm=sm()
		print('Hi')
		Sm.on_pre_enter=Sm.Enter_()
		return Sm
	def first(self):
		App.root.current="first"

if __name__ == '__main__':
	App=MyApp()
	App.run()
	#cv2.destroyAllWindows()