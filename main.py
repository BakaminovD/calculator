#! /usr/bin/env python
# -*- coding: utf-8 -*-

# импорт необходимых модулей kivy

from kivy.app import App
from kivy.core import text
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.modalview import ModalView
from kivy.core.text import markup
from functools import partial

# создание класса приложения, переопределение метода build

class MainApp(App):

	def build(self):
		
# создание необходимых виждетов, их размещение к конструкторах, которые потом размещаются в супер конструкторе

		self.flag = 10
		self.flag_rezult = 0
		
		super_layout= BoxLayout(orientation = 'vertical')
		
		ver1=BoxLayout(orientation='vertical')
		
		self.lbl_nazv = Label(text = '[b]\n\n\nКуЛьКуЛяТыР\n[/b]', size_hint = (1, .8), pos_hint = {'center_x': .5, 'center_y': .5}, color = (.95, .78, .14, 1), markup=True)
		ver1.add_widget(self.lbl_nazv)

		ver_dop=BoxLayout(orientation='vertical')
		
		self.lbl_primer = Label(text='x + y = й')
		ver_dop.add_widget(self.lbl_primer)
		
		ver2=BoxLayout(orientation='vertical')
		
		self.lbl_rezult = Label(text='0', markup=True)
		ver2.add_widget(self.lbl_rezult)

		ver3=BoxLayout(orientation='horizontal')

		self.lbl_10ss_dop = Label(text='x[sub]10[/sub]:', size_hint = (.1, 1), color = (.95, .78, .14, 1), markup=True)
		ver3.add_widget(self.lbl_10ss_dop)
		
		self.lbl_10ss = Label(text='', color = (.95, .78, .14, 1))
		ver3.add_widget(self.lbl_10ss)

		ver4=BoxLayout(orientation='horizontal')

		self.lbl_2ss_dop = Label(text='x[sub]2[/sub]:', size_hint = (.1, 1), markup=True)
		ver4.add_widget(self.lbl_2ss_dop)
		
		self.lbl_2ss = Label(text='')
		ver4.add_widget(self.lbl_2ss)

		ver5=BoxLayout(orientation='horizontal')

		self.lbl_16ss_dop = Label(text='x[sub]16[/sub]:', size_hint = (.1, 1), markup=True)
		ver5.add_widget(self.lbl_16ss_dop)
		
		self.lbl_16ss = Label(text='')
		ver5.add_widget(self.lbl_16ss)

		H0=BoxLayout(orientation='horizontal')

		self.btn_E=Button(text='E')
		self.btn_E.bind(on_press = partial(self.press_btn, digit = 'E'))
		H0.add_widget(self.btn_E)

		self.btn_F=Button(text='F')
		self.btn_F.bind(on_press = partial(self.press_btn, digit = 'F'))
		H0.add_widget(self.btn_F)

		self.btn_x10=Button(text='[b]x[sub]10[/sub][/b]', color = (.95, .78, .14, 1), markup=True)
		self.btn_x10.bind(on_press = self.pres_x10)
		H0.add_widget(self.btn_x10)

		self.btn_x16=Button(text='[b]x[sub]16[/sub][/b]', markup=True)
		self.btn_x16.bind(on_press = self.pres_x16)
		H0.add_widget(self.btn_x16)

		self.btn_x2=Button(text='[b]x[sub]2[/sub][/b]', markup=True)
		self.btn_x2.bind(on_press = self.pres_x2)
		H0.add_widget(self.btn_x2)
		
		H1=BoxLayout(orientation='horizontal')

		self.btn_D=Button(text='D')
		self.btn_D.bind(on_press = partial(self.press_btn, digit = 'D'))
		H1.add_widget(self.btn_D)
		
		self.btn_7=Button(text='7')
		self.btn_7.bind(on_press = partial(self.press_btn, digit = '7'))
		H1.add_widget(self.btn_7)
		
		self.btn_8=Button(text='8')
		self.btn_8.bind(on_press = partial(self.press_btn, digit = '8'))
		H1.add_widget(self.btn_8)
		
		self.btn_9=Button(text='9')
		self.btn_9.bind(on_press = partial(self.press_btn, digit = '9'))
		H1.add_widget(self.btn_9)
		
		self.btn_plus=Button(text='+')
		self.btn_plus.bind(on_press = self.pres_plus)
		H1.add_widget(self.btn_plus)
		
		H2=BoxLayout(orientation='horizontal')

		self.btn_C=Button(text='C')
		self.btn_C.bind(on_press = partial(self.press_btn, digit = 'C'))
		H2.add_widget(self.btn_C)
		
		self.btn_4=Button(text='4')
		self.btn_4.bind(on_press = partial(self.press_btn, digit = '4'))
		H2.add_widget(self.btn_4)
		
		self.btn_5=Button(text='5')
		self.btn_5.bind(on_press = partial(self.press_btn, digit = '5'))
		H2.add_widget(self.btn_5)
		
		self.btn_6=Button(text='6')
		self.btn_6.bind(on_press = partial(self.press_btn, digit = '6'))
		H2.add_widget(self.btn_6)
		
		self.btn_minus=Button(text='-')
		self.btn_minus.bind(on_press = self.pres_minus)
		H2.add_widget(self.btn_minus)
		
		H3=BoxLayout(orientation='horizontal')

		self.btn_B=Button(text='B')
		self.btn_B.bind(on_press = partial(self.press_btn, digit = 'B'))
		H3.add_widget(self.btn_B)
		
		self.btn_1=Button(text='1')
		self.btn_1.bind(on_press = partial(self.press_btn, digit = '1'))
		H3.add_widget(self.btn_1)
		
		self.btn_2=Button(text='2')
		self.btn_2.bind(on_press = partial(self.press_btn, digit = '2'))
		H3.add_widget(self.btn_2)
		
		self.btn_3=Button(text='3')
		self.btn_3.bind(on_press = partial(self.press_btn, digit = '3'))
		H3.add_widget(self.btn_3)
		
		self.btn_mnog=Button(text='*')
		self.btn_mnog.bind(on_press = self.pres_mnog)
		H3.add_widget(self.btn_mnog)
		
		H4=BoxLayout(orientation='horizontal')

		self.btn_A=Button(text='A')
		self.btn_A.bind(on_press = partial(self.press_btn, digit = 'A'))
		H4.add_widget(self.btn_A)
		
		self.btn_toch=Button(text='.')
		self.btn_toch.bind(on_press = self.pres_toch)
		H4.add_widget(self.btn_toch)
		
		self.btn_nul=Button(text='0')
		self.btn_nul.bind(on_press = partial(self.press_btn, digit = '0'))
		H4.add_widget(self.btn_nul)
		
		self.btn_delit=Button(text='<<')
		self.btn_delit.bind(on_press = self.pres_delit)
		H4.add_widget(self.btn_delit)
		
		self.btn_delim=Button(text='/')
		self.btn_delim.bind(on_press = self.pres_delim)
		H4.add_widget(self.btn_delim)
		
		H5=BoxLayout(orientation='horizontal')
		
		self.btn_ochist=Button(text='[b]Del[/b]', size_hint = (.485, 1), color = (.95, .78, .14, 1), markup=True)
		self.btn_ochist.bind(on_press = self.pres_ochist)
		H5.add_widget(self.btn_ochist)

		self.btn_What=Button(text='?', size_hint = (.485, 1))
		self.btn_What.bind(on_press = self.pres_What)
		H5.add_widget(self.btn_What)
		
		self.btn_rezult=Button(text='=')
		self.btn_rezult.bind(on_press = self.pres_rezult)
		H5.add_widget(self.btn_rezult)
		
		self.btn_skob=Button(text='( )', size_hint = (.485, 1))
		self.btn_skob.bind(on_press = self.pres_skob)
		H5.add_widget(self.btn_skob)

# изначально неактивные кнопки

		self.btn_A.disabled = True
		self.btn_B.disabled = True
		self.btn_C.disabled = True
		self.btn_D.disabled = True
		self.btn_E.disabled = True
		self.btn_F.disabled = True
		
# упорядочивание конструкторов в супер-конструкторе
		
		super_layout.add_widget(ver1)
		super_layout.add_widget(ver_dop)
		super_layout.add_widget(ver2)
		super_layout.add_widget(ver3)
		super_layout.add_widget(ver4)
		super_layout.add_widget(ver5)
		super_layout.add_widget(H0)
		super_layout.add_widget(H1)
		super_layout.add_widget(H2)
		super_layout.add_widget(H3)
		super_layout.add_widget(H4)
		super_layout.add_widget(H5)
		
#  запуск супер-конструктора
		
		return super_layout
		
# создание отдельных методов для кнопок
	
	def pres_x10(self, btn_x10):
		self.flag = 10
		self.flag_rezult = 0
		self.lbl_10ss.color = (.95, .78, .14, 1)
		self.lbl_10ss_dop.color = (.95, .78, .14, 1) 
		self.lbl_16ss.color = (1, 1, 1, 1)
		self.lbl_16ss_dop.color = (1, 1, 1, 1)
		self.lbl_2ss.color = (1, 1, 1, 1)
		self.lbl_2ss_dop.color = (1, 1, 1, 1)
		self.btn_x10.color = (.95, .78, .14, 1)
		self.btn_x16.color = (1, 1, 1, 1)
		self.btn_x2.color = (1, 1, 1, 1)
		self.btn_2.disabled = False
		self.btn_3.disabled = False
		self.btn_4.disabled = False
		self.btn_5.disabled = False
		self.btn_6.disabled = False
		self.btn_7.disabled = False
		self.btn_8.disabled = False
		self.btn_9.disabled = False
		self.btn_A.disabled = True
		self.btn_B.disabled = True
		self.btn_C.disabled = True
		self.btn_D.disabled = True
		self.btn_E.disabled = True
		self.btn_F.disabled = True
		self.btn_toch.disabled = False
		self.lbl_primer.text = 'x + y = й'
		self.lbl_2ss.text = ''
		self.lbl_16ss.text = ''
		self.lbl_10ss.text = ''
		self.lbl_rezult.text = '0'

	def pres_x16(self, btn_x16):
		self.flag_rezult = 0
		self.flag = 16
		self.lbl_10ss.color = (1, 1, 1, 1)
		self.lbl_10ss_dop.color = (1, 1, 1, 1) 
		self.lbl_16ss.color = (.95, .78, .14, 1)
		self.lbl_16ss_dop.color = (.95, .78, .14, 1)
		self.lbl_2ss.color = (1, 1, 1, 1)
		self.lbl_2ss_dop.color = (1, 1, 1, 1)
		self.btn_x10.color = (1, 1, 1, 1)
		self.btn_x16.color = (.95, .78, .14, 1)
		self.btn_x2.color = (1, 1, 1, 1)
		self.btn_2.disabled = False
		self.btn_3.disabled = False
		self.btn_4.disabled = False
		self.btn_5.disabled = False
		self.btn_6.disabled = False
		self.btn_7.disabled = False
		self.btn_8.disabled = False
		self.btn_9.disabled = False
		self.btn_A.disabled = False
		self.btn_B.disabled = False
		self.btn_C.disabled = False
		self.btn_D.disabled = False
		self.btn_E.disabled = False
		self.btn_F.disabled = False
		self.btn_toch.disabled = False
		self.lbl_primer.text = 'x + y = й'
		self.lbl_2ss.text = ''
		self.lbl_16ss.text = ''
		self.lbl_10ss.text = ''
		self.lbl_rezult.text = '0'

	def pres_x2(self, btn_x2):
		self.flag_rezult = 0
		self.flag = 2
		self.lbl_10ss.color = (1, 1, 1, 1)
		self.lbl_10ss_dop.color = (1, 1, 1, 1) 
		self.lbl_16ss.color = (1, 1, 1, 1)
		self.lbl_16ss_dop.color = (1, 1, 1, 1)
		self.lbl_2ss.color = (.95, .78, .14, 1)
		self.lbl_2ss_dop.color = (.95, .78, .14, 1)
		self.btn_x10.color = (1, 1, 1, 1)
		self.btn_x16.color = (1, 1, 1, 1)
		self.btn_x2.color = (.95, .78, .14, 1)
		self.btn_2.disabled = True
		self.btn_3.disabled = True
		self.btn_4.disabled = True
		self.btn_5.disabled = True
		self.btn_6.disabled = True
		self.btn_7.disabled = True
		self.btn_8.disabled = True
		self.btn_9.disabled = True
		self.btn_A.disabled = True
		self.btn_B.disabled = True
		self.btn_C.disabled = True
		self.btn_D.disabled = True
		self.btn_E.disabled = True
		self.btn_F.disabled = True
		self.btn_toch.disabled = False
		self.lbl_primer.text = 'x + y = й'
		self.lbl_2ss.text = ''
		self.lbl_16ss.text = ''
		self.lbl_10ss.text = ''
		self.lbl_rezult.text = '0'
	
	def pres_plus(self, btn_plus):
		self.flag_rezult = 0
		self.lbl_rezult.text = self.lbl_rezult.text + '+'
		
	def pres_minus(self, btn_minus):
		self.flag_rezult = 0
		if self.lbl_rezult.text == '0':
			self.lbl_rezult.text = '-'
		else:
			self.lbl_rezult.text = self.lbl_rezult.text + '-'
		
	def pres_mnog(self, btn_mnog):
		self.flag_rezult = 0
		self.lbl_rezult.text = self.lbl_rezult.text + '*'
			
	def pres_toch(self, btn_toch):
		self.flag_rezult = 0
		self.lbl_rezult.text = self.lbl_rezult.text + '.'
			
	def pres_delim(self, btn_delim):
		self.flag_rezult = 0
		self.lbl_rezult.text = self.lbl_rezult.text + '/'
			
	def pres_ochist(self, btn_ochist):
		self.flag_rezult = 0
		self.lbl_primer.text = 'x + y = й'
		self.lbl_2ss.text = ''
		self.lbl_16ss.text = ''
		self.lbl_10ss.text = ''
		self.lbl_rezult.text = '0'

	def press_btn(self, button, digit):
		a = self.lbl_rezult.text
		if a == '0' or a == '':
			self.lbl_rezult.text = digit
			self.lbl_2ss.text = ''
			self.lbl_16ss.text = ''
			self.lbl_10ss.text = ''
			self.flag_rezult = 0
		elif self.flag_rezult == 1:
			self.lbl_rezult.text = digit
			self.lbl_2ss.text = ''
			self.lbl_16ss.text = ''
			self.lbl_10ss.text = ''
			self.lbl_primer.text = ''
			self.flag_rezult = 0
		else:
			self.lbl_rezult.text = self.lbl_rezult.text + digit
			self.flag_rezult = 0
		
	def pres_skob(self, btn_skob):
		if self.flag_rezult == 1:
			self.flag_rezult = 0
			self.lbl_rezult.text = '('
			self.lbl_primer.text = 'x + y = й'
			self.lbl_10ss.text = ''
			self.lbl_16ss.text = ''
			self.lbl_2ss.text = ''
		else:
			self.flag_rezult = 0
			stroka = self.lbl_rezult.text
			dlina = len(stroka)
			spisok = list(stroka)
			if len(spisok) == 0:
				znak = ''
			else:
				znak = spisok[-1]
			mylist = set(znak)
			chars = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'A', 'B', 'C', 'D', 'E', 'F'}
			if stroka == '' or dlina == 1:
				self.lbl_rezult.text = '('
			elif znak == '+' or znak == '-' or znak == '*' or znak == '/':
				self.lbl_rezult.text = self.lbl_rezult.text + '('
			elif mylist.issubset(chars) and dlina > 1 and stroka.find('x') != 0:
				self.lbl_rezult.text = self.lbl_rezult.text + ')'
			else:
				layout = BoxLayout(orientation='vertical')
				layout.add_widget(Label(text='Куда тут скобку-то ставить???'))
				button = Button (text = 'Океюшки!', size_hint = (.5,  .3), pos_hint = {'center_x': .5, 'center_y': .2})
				layout.add_widget(button)
				popup = Popup(title='ОшибочкА', content=layout, size_hint = (1, .4))
				button.bind(on_press = popup.dismiss)
				popup.open()

# создание метода кнопки "<<" с проверкой на ошибки
			
	def pres_delit(self, btn_delit):
		self.flag_rezult = 0
		if self.lbl_rezult.text == '0':
			self.lbl_primer.text = 'x + y = й'
			self.lbl_2ss.text = ''
			self.lbl_16ss.text = ''
			self.lbl_rezult.text = '0'
		elif self.lbl_rezult.text == '':
			layout = BoxLayout(orientation='vertical')
			layout.add_widget(Label(text='Там уже удалять нечего!!!'))
			button = Button (text = 'Океюшки!', size_hint = (.5,  .3), pos_hint = {'center_x': .5, 'center_y': .2})
			layout.add_widget(button)
			popup = Popup(title='ОшибочкА', content=layout, size_hint = (1, .4))
			button.bind(on_press = popup.dismiss)
			self.lbl_rezult.text = '0'
			self.lbl_primer.text = 'x + y = й'
			self.lbl_10ss.text = ''
			self.lbl_16ss.text = ''
			self.lbl_2ss.text = ''
			popup.open()
		else:
			a = self.lbl_rezult.text
			a = list(a)
			del a[-1]
			a = ''.join(a)
			self.lbl_rezult.text = a

# создание метода подсказки "?"

	def pres_What(self, btn_What):
		self.flag_rezult = 0
		layout = BoxLayout(orientation='vertical')
		layout_0 = BoxLayout(orientation='vertical', size_hint = (1, .1))
		layout_1 = BoxLayout(orientation='vertical', size_hint = (1,  .8))
		self.my_lbl_0 = Label(text = '[b]\n\nПоДсКаЗкИ\n[/b]', color = (.95, .78, .14, 1), markup=True)
		self.my_lbl = Label(text = '\n1. Для возведения числа в некоторую степень\nиспользуйте двойное умножение «**».\nНапример, чтобы возвести 33 в квадрат,\nнужно ввести: 33**2.\n\n2. Для извлечения квадратного корня\nиспользуйте двойное умножение на 0,5.\nНапример, чтобы извлечь квадратный\nкорень из 25, нужно ввести: 25**0,5.\n\n3. Чтобы просто перевести некоторое число\nв другую систему счисления,\nнужно выбрать систему счисления,\nв которой представлено это число,\nнабрать его и нажать «=».\n\n\n')
		layout_0.add_widget(self.my_lbl_0)
		layout_1.add_widget(self.my_lbl)
		layout_2 = BoxLayout(orientation='horizontal', size_hint = (1,  .1))
		self.button_zakr = Button (text = 'Закрыть')
		layout_2.add_widget(self.button_zakr)
		layout.add_widget(layout_0)
		layout.add_widget(layout_1)
		layout.add_widget(layout_2)
		self.dop_view = ModalView()
		self.dop_view.add_widget(layout)
		self.button_zakr.bind(on_press = self.dop_view.dismiss)
		self.dop_view.open()
			
# создание метода кнопки "=" с проверкой на ошибки
		
	def pres_rezult(self, btn_rezult):
		self.flag_rezult = 1
		my_primer = self.lbl_rezult.text
		self.rez = my_primer
		if self.flag == 16:
			self.rez = summary(self.rez, from_base=16)
		elif self.flag == 2:
			self.rez = summary(self.rez, from_base=2)
		try:
			self.rez = str(eval(self.rez))
		except(ZeroDivisionError, SyntaxError):
			layout = BoxLayout(orientation='vertical')
			layout.add_widget(Label(text='Вы ввели какую-то херню или поделили на 0!!!'))
			button = Button (text = 'Океюшки!', size_hint = (.5,  .3), pos_hint = {'center_x': .5, 'center_y': .2})
			layout.add_widget(button)
			popup = Popup(title='ОшибочкА', content=layout, size_hint = (1, .4))
			button.bind(on_press = popup.dismiss)
			self.lbl_rezult.text = '0'
			self.lbl_primer.text = 'x + y = й'
			self.lbl_10ss.text = ''
			self.lbl_16ss.text = ''
			self.lbl_2ss.text = ''
			popup.open()
		else:
			if self.rez[-1] == '0' and self.rez[-2] == '.':
				self.rez = self.rez[:-2]
			self.rez_16 = float_convert(self.rez, to_base=16)
			self.rez_2 = float_convert(self.rez, to_base=2)
			if self.rez.find('.') != -1:
				tochka = self.rez.find('.')
				while tochka > 0:
					tochka = tochka - 3
					if tochka <= 0:
						break
					self.rez = self.rez[:tochka] + ' ' + self.rez[tochka:]
			else:
				tochka = len(self.rez)
				if tochka > 3:
					while tochka > 0:
						tochka = tochka - 3
						if tochka <= 0:
							break
						self.rez = self.rez[:tochka] + ' ' + self.rez[tochka:]
			if self.rez_2.find('.') != -1:
				tochka = self.rez_2.find('.')
				while tochka > 0:
					tochka = tochka - 4
					if tochka <= 0:
						break
					self.rez_2 = self.rez_2[:tochka] + ' ' + self.rez_2[tochka:]
			else:
				tochka = len(self.rez_2)
				if tochka > 4:
					while tochka > 0:
						tochka = tochka - 4
						if tochka <= 0:
							break
						self.rez_2 = self.rez_2[:tochka] + ' ' + self.rez_2[tochka:]
			if self.rez_16.find('.') != -1:
				tochka = self.rez_16.find('.')
				while tochka > 0:
					tochka = tochka - 2
					if tochka <= 0:
						break
					self.rez_16 = self.rez_16[:tochka] + ' ' + self.rez_16[tochka:]
			else:
				tochka = len(self.rez_16)
				if tochka > 2:
					while tochka > 0:
						tochka = tochka - 2
						if tochka <= 0:
							break
						self.rez_16 = self.rez_16[:tochka] + ' ' + self.rez_16[tochka:]
			if self.flag == 16:
				self.lbl_rezult.text = self.rez_16
			elif self.flag == 2:
				self.lbl_rezult.text = self.rez_2
			else:
				self.lbl_rezult.text = self.rez
			self.lbl_primer.text = my_primer
			self.lbl_10ss.text = self.rez
			self.lbl_16ss.text = self.rez_16
			self.lbl_2ss.text = self.rez_2

# ПРОГА ДЛЯ КОНВЕРТАЦИИ

def int_convert(num, from_base=10, to_base=10):
    if num == '0':
        return str(num)
    elif to_base == 10:
        my_int = int(num, from_base)
        return str(my_int)
    else:
        alphabet ='0123456789ABCDEF'
        my_int = ''
        num = int(num, from_base)
        while num != 0:
            a = num % to_base
            a = alphabet[a]
            num = num // to_base
            my_int = a + my_int
        return str(my_int)
		
def drob(num, from_base=10, to_base=10):
    if to_base == 10:
        if from_base == 2:
            s = 0
            sum = 0
            for n in num:
                n = int(n)
                s = s - 1
                sum = sum + n*(2 ** s)
            sum = str(sum)
            sum = sum.split('.')
            return sum[1]
        elif from_base == 16:
            chars = 'ABCDEF'
            no_chars = [10, 11, 12, 13, 14, 15]
            s = 0
            sum = 0
            for n in num:
                no = chars.find(n)
                if no != -1:
                    n = no_chars[no]
                n = int(n)
                s = s - 1
                sum = sum + n*(16**s)
            sum = str(sum)
            sum = sum.split('.')
            return sum[1]
    else:
        my_num = float('0.' + num)
        num = int(num)
        sum = ''
        s = 0
        alphabet ='0123456789ABCDEF'
        while num != 0:
            s = s + 1
            x = my_num * to_base
            x = str(x)
            x = x.split('.')
            my_num = x[1]
            num = int(my_num)
            my_num = float('0.' + my_num)
            x = int(x[0])
            x = alphabet[x]
            sum = sum + x
            if s == 10:
                break
        return str(sum)

def float_convert(num, from_base=10, to_base=10):
    f = 0
    num = str(num)
    if num[0] == '-':
        num = num[1:]
        f = 1
    s = num.split(".")
    try:
        a = s[1]
    except IndexError:
        my_float = int_convert(s[0], from_base=from_base, to_base=to_base)
        if f == 1:
            my_float = '-' + my_float
            f = 0
        return my_float
    else:
        if s[1] == "0":
            my_float = int_convert(s[0], from_base=from_base, to_base=to_base)
            if f == 1:
                my_float = '-' + my_float
                f = 0
            return my_float
        else:
            first = int_convert(s[0], from_base=from_base, to_base=to_base)
            second = drob(s[1], from_base=from_base, to_base=to_base)
            if f == 1:
                first = '-' + first
                f = 0
            s = first + '.' + second
            return s
            
def summary(a, from_base=10, cifr='', znak='', itog=''):
    mass = '0123456789ABCDEF.'
    fl = 1
    if a[-1] in mass:
        a = a + ' '
    else:
        a = a + '.'
    for n in a:
        if mass.find(n) != -1: 
            fl = 0
            itog = itog + znak
            znak = ''
            cifr = cifr + n
        else:
            if fl == 0:
                cifr = str(float_convert(cifr, from_base=from_base, to_base=10))
            fl = 1
            itog = itog + cifr
            cifr = ''
            znak = znak + n
    return itog

# КОНЕЦ ПРОГИ ДЛЯ КОНВЕРТАЦИИ
		
# создание экземпляра класса приложения и его запуск, если приложение вызвано
		
#if _name_ == '_main_':
root = MainApp()
root.run()