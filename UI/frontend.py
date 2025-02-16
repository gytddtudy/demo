from kivymd.uix.backdrop.backdrop import MDBoxLayout
from kivymd.uix.backdrop.backdrop import MDTopAppBar
from kivymd.uix.bottomnavigation.bottomnavigation import MDScreen
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import MDList, OneLineAvatarListItem
from kivymd.uix.button import MDIconButton
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager, NoTransition
from kivy.metrics import dp
from kivy.clock import Clock
import sys
from kivymd.uix.label import MDLabel

sys.path.append('/home/salamat/ratingsays_offline/rs')


class Demo(MDApp):

    def build(self):
        self.theme_cls.primary_palette = 'Red'

        return Builder.load_file('frontend.kv')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.root = ScreenManager()
        self.last_touch_time = 0
        self.favorites_screens = set()

        self.default_changer = MDIconButton(
            icon = 'format-align-center',
            icon_size = '20sp',
            icon_color = (1, 1, 1, 1),
            theme_text_color = 'Custom',
            text_color = (1, 1, 1, 1),
            on_release = lambda x: self.main_random_list()
        )

        self.abc_changer = MDIconButton(
            icon = 'alphabet-latin',
            icon_size = '20sp',
            icon_color = (1, 1, 1, 1),
            theme_text_color = 'Custom',
            text_color = (1, 1, 1, 1),
            on_release = lambda x: self.main_abc_list()
        )




    def on_start(self): 

        self.favorite_list = []
        print(self.favorite_list)

        self.light_theme()

        self.main = self.root.get_screen('main')
        self.mother_list = self.main.ids.mother_lists
        self.top_list = self.main.ids.top_list

        self.characters = OneLineAvatarListItem(
            text='Hasiyet psihologiyasy',
            on_release=lambda x: self.go_characters()
            )

        self.child = OneLineAvatarListItem(
            text='Caga psiholohiyasy',
            on_release=lambda x: self.go_child()
        )

        self.acne = OneLineAvatarListItem(
            text='Yetginjek psihologiyasy',
            on_release=lambda x: self.go_acne()
        )

        self.women = OneLineAvatarListItem(
            text='Ayal psiholohiyasy',
            on_release=lambda x: self.go_women()
        )

        self.man = OneLineAvatarListItem(
            text='Erkek psiholohiyasy',
            on_release=lambda x: self.go_man()
        )

        self.learn = OneLineAvatarListItem(
            text='Owrenme psiholohiyasy',
            on_release=lambda x: self.go_learn()
        )

        self.battle = OneLineAvatarListItem(
            text='Sowes psiholohiyasy',
            on_release=lambda x: self.go_battle()
        )

        self.widgets = [self.characters, self.child, self.acne, self.women, self.man, self.learn, self.battle]

        self.main_random_list()


    def main_random_list(self):
        
        self.top_list.remove_widget(self.default_changer)
        self.remove_widgets()

        self.top_list.add_widget(self.abc_changer)
        self.add_widget_default()

    def main_abc_list(self):

        self.top_list.remove_widget(self.abc_changer)
        self.remove_widgets()

        self.top_list.add_widget(self.default_changer)
        self.add_widget_abc()

    def add_widget_abc(self):

        self.mother_list.add_widget(self.women)
        self.mother_list.add_widget(self.child)
        self.mother_list.add_widget(self.man)
        self.mother_list.add_widget(self.characters)
        self.mother_list.add_widget(self.battle)
        self.mother_list.add_widget(self.learn)
        self.mother_list.add_widget(self.acne)
            
    def add_widget_default(self):
        for item in self.widgets:
            self.mother_list.add_widget(item)

    def remove_widgets(self):
        for item in self.widgets:
            self.mother_list.remove_widget(item)

    def characters_default_list(self):
        pass


    def add_favorite(self, *args):
        screen_name = self.root.current

        self.delete_fav_btn = MDIconButton( 
            icon='star',
            theme_text_color= 'Custom',
            text_color= (1, 1, 1, 1),
            on_release= lambda x: self.delete_fav()
        )

        self.parent_widget = args[0]

        while self.parent_widget and not isinstance(self.parent_widget, MDBoxLayout):
            self.parent_widget = self.parent_widget.parent
            self.parent_id = self.parent_widget.id

        self.parent_widget.remove_widget(args[0])
        self.parent_widget.add_widget(self.delete_fav_btn)

        
        self.favorites_screens.add(screen_name)

        print(self.favorites_screens)

    def delete_fav(self):
        
        self.add_fav = MDIconButton(
            icon= 'star-outline',
            theme_text_color= 'Custom',
            text_color= (1, 1, 1, 1),
            on_release= lambda x: self.add_fav()
        )

        for child in self.parent_widget.children:
            if isinstance(child, MDIconButton) and child.icon == 'star':
                self.parent_widget.remove_widget(child)
        
        self.parent_widget.add_widget(self.add_fav)

    def add_fav(self):

        for child in self.parent_widget.children:
            if isinstance(child, MDIconButton) and child.icon == 'star-outline':
                self.parent_widget.remove_widget(child)

            self.parent_widget.add_widget(self.delete_fav_btn)

    def set_color(self, color):

        rgb = color.text_color

        if rgb == [1.0, 0.6470588235294118, 0.0, 1.0]:
            main_color = 'Orange'

        elif rgb == [0.0, 0.5019607843137255, 0.0, 1.0]:
            main_color = 'Green'

        elif rgb == [1.0, 0.0, 0.0, 1.0]:
            main_color = 'Red'

        elif rgb == [0.5019607843137255, 0.0, 0.5019607843137255, 1.0]:
            main_color = 'Purple'

        elif rgb == [0.0, 0.0, 1.0, 1.0]:
            main_color = 'Blue'

        self.theme_cls.primary_palette = main_color

        if self.theme_cls.theme_style == 'Light':
            self.posibility_calc_screen.ids.calc_bottom_app_bar.md_bg_color = (.96, .96, .96, .5)

        else: 
            self.posibility_calc_screen.ids.calc_bottom_app_bar.md_bg_color = (.04, .04, .04, .5)


    def theme(self, dt):

        if self.theme_cls.theme_style == 'Dark':
            self.light_theme()

        else: 
            self.dark_theme()        

    def light_theme(self):

        self.theme_cls.theme_style = 'Light'

        self.posibility_calc_screen = self.root.get_screen('posibility_calc_screen')
        main_screen = self.root.get_screen('main')
        self.theme_cls.theme_style_switch_animation = True
        main_screen.ids.top_app_bar.use_primary_color = False

        drawers_main = [
            main_screen.ids.main_drawer_id_0, 
            main_screen.ids.main_drawer_id_1, 
            main_screen.ids.main_drawer_id_2,
            main_screen.ids.main_drawer_id_3,
        ]

        drawers_posibility_calc = [
            self.posibility_calc_screen.ids.calc_drawer_id_0, 
            self.posibility_calc_screen.ids.calc_drawer_id_1, 
            self.posibility_calc_screen.ids.calc_drawer_id_2,
            self.posibility_calc_screen.ids.calc_drawer_id_3,
        ]

        self.posibility_calc_screen.ids.posibility_calc_md.md_bg_color = (.96, .96, .96, 1)
        main_screen.ids.main_md.md_bg_color = (.96, .96, .96, 1)
        main_screen.ids.nav_drawer_0.md_bg_color = (.88, .88, .88, .9)
        self.posibility_calc_screen.ids.nav_drawer_1.md_bg_color = (.88, .88, .88, .9) 
        self.posibility_calc_screen.ids.user_input_card_c.md_bg_color = (.90, .90, .90, 1)
        self.posibility_calc_screen.ids.user_input_card_d.md_bg_color = (.90, .90, .90, 1)
        self.posibility_calc_screen.ids.user_input_card_e.md_bg_color = (.90, .90, .90, 1)
        self.posibility_calc_screen.ids.user_input_card_f.md_bg_color = (.90, .90, .90, 1)

        self.posibility_calc_screen.ids.user_input_text_c.foreground_color = (0, 0, 0, 1)
        self.posibility_calc_screen.ids.user_input_text_d.foreground_color = (0, 0, 0, 1)
        self.posibility_calc_screen.ids.user_input_text_e.foreground_color = (0, 0, 0, 1)
        self.posibility_calc_screen.ids.user_input_text_f.foreground_color = (0, 0, 0, 1)

        main_screen.ids.top_app_bar.specific_text_color = (.5, .5, .5, 1)
        self.posibility_calc_screen.ids.calc_bottom_app_bar.md_bg_color = (.96, .96, .96, .5)
        self.posibility_calc_screen.ids.calc_bottom_app_bar.icon_color = (0, 0, 0, 1)

        for drawer in drawers_main:
            drawer.text_color = (0, 0, 0, 1)
            drawer.icon_color = (0, 0, 0, 1)

        for drawer in drawers_posibility_calc:
            drawer.text_color = (0, 0, 0, 1)
            drawer.icon_color = (0, 0, 0, 1)

    def dark_theme(self):

        self.theme_cls.theme_style = 'Dark'

        main_screen = self.root.get_screen('main')
        self.theme_cls.theme_style_switch_animation = True
        main_screen.ids.top_app_bar.use_primary_color = False

        drawers_main = [
            main_screen.ids.main_drawer_id_0, 
            main_screen.ids.main_drawer_id_1, 
            main_screen.ids.main_drawer_id_2,
            main_screen.ids.main_drawer_id_3,
        ]

        drawers_posibility_calc = [
            self.posibility_calc_screen.ids.calc_drawer_id_0, 
            self.posibility_calc_screen.ids.calc_drawer_id_1, 
            self.posibility_calc_screen.ids.calc_drawer_id_2,
            self.posibility_calc_screen.ids.calc_drawer_id_3,
        ]

        self.posibility_calc_screen.ids.posibility_calc_md.md_bg_color = (.04, .04, .04, 1)
        main_screen.ids.main_md.md_bg_color = (.04, .04, .04, 1)
        main_screen.ids.nav_drawer_0.md_bg_color = (.05, .05, .05, .9)
        self.posibility_calc_screen.ids.nav_drawer_1.md_bg_color = (.05, .05, .05, .9) 
        
        self.posibility_calc_screen.ids.user_input_card_c.md_bg_color = (.2, .2, .2, 1)
        self.posibility_calc_screen.ids.user_input_card_d.md_bg_color = (.2, .2, .2, 1)
        self.posibility_calc_screen.ids.user_input_card_e.md_bg_color = (.2, .2, .2, 1)
        self.posibility_calc_screen.ids.user_input_card_f.md_bg_color = (.2, .2, .2, 1)

        self.posibility_calc_screen.ids.user_input_text_c.foreground_color = (1, 1, 1, 1)
        self.posibility_calc_screen.ids.user_input_text_d.foreground_color = (1, 1, 1, 1)
        self.posibility_calc_screen.ids.user_input_text_e.foreground_color = (1, 1, 1, 1)
        self.posibility_calc_screen.ids.user_input_text_f.foreground_color = (1, 1, 1, 1)

        main_screen.ids.top_app_bar.specific_text_color = (.7, .7, .7, 1)
        self.posibility_calc_screen.ids.calc_bottom_app_bar.md_bg_color = (.04, .04, .04, .5)
        self.posibility_calc_screen.ids.calc_top_app_bar.specific_text_color = (.7, .7, .7, 1)
        

        for drawer in drawers_main:

            drawer.text_color = (.9, .9, .9, 1)
            drawer.icon_color = (.9, .9, .9, 1)

        for drawer in drawers_posibility_calc:
            drawer.text_color = (.9, .9, .9, 1)
            drawer.icon_color = (.9, .9, .9, 1)

    def is_dark_theme(self):

        return self.theme_cls.theme_style == 'Dark'


    def enter_hover(self, instance):

        if not self.is_dark_theme():

            instance.md_bg_color = [.3, .3, .3, .9]
            instance.text_color = [.15, .15, .15, 1]
            instance.icon_color = [.15, .15, .15, 1]

        else:
            instance.md_bg_color = [0.9, 0.9, 0.9, 1]
            instance.text_color = [.8, .8, .8 ,1]
            instance.icon_color = [.8, .8, .8 ,1]

    def leave_hover(self, instance):

        if not self.is_dark_theme():
            
            instance.md_bg_color = (.2, .2 , .2, 1)
            instance.text_color = (0, 0, 0, 1)
            instance.icon_color = (0, 0, 0, 1)
        
        else:

            instance.text_color = (.9, .9, .9, 1)
            instance.icon_color = (.9, .9, .9, 1)

    def set_theme(self, instance, touch):

        self.green_balloon = self.main.ids.green_balloon
        self.touch = touch

        if instance.collide_point(*touch.pos):    
            self.fly = Clock.schedule_once(self.fly_balloon, 1)

    def on_touch_down(self, instance, touch):

        if instance.collide_point(*touch.pos):
            self.touch_time = Clock.schedule_once(self.theme, .99)


        screens = [ 
                    self.root.get_screen('main').ids.main_md,
                    self.root.get_screen('posibility_calc_screen').ids.posibility_calc_md
        ]

        for screen in screens :
            if instance == screen:
                current_time = Clock.get_time()
                time_diff = current_time - self.last_touch_time
            
                if time_diff < .3:
                    self.toggle_nav_menu()
                self.last_touch_time = current_time

    def on_touch_up(self, instance, touch):

        if instance.collide_point(*touch.pos):
            if hasattr(self, 'touch_time'):
                self.touch_time.cancel()
    

    def toggle_nav_menu(self):

        nav_drawer= [self.root.get_screen('main').ids.nav_drawer_0,
                    self.root.get_screen('posibility_calc_screen').ids.nav_drawer_1           
        ]

        for drawer in nav_drawer:
            if drawer == 'open':
                drawer.set_state('close')

            else: drawer.set_state('open')

    def back_main(self):
        main = self.root.get_screen('main')
        self.root.current = 'main'

    def back_characters(self):
        characters = self.root.get_screen('characters')
        self.root.current = 'characters'

    def find_word(self):
        print('1')
        instance_word = self.root.get_screen('main').ids.main_search.text

        if len(instance_word) > 0:
            self.get_words(instance_word)

    def get_words(self, word):
        print('2')
        hint_text = self.root.get_screen('main').ids.main_search.hint_text
        words = ['Cekinjenlik', 'Otizm', 'Asperger sendromy', 'Sizoid hasiyet', 'Pasiw agresiwlik', 'Paranoid hasiyet', 'Histriyoniki hasiyet', 'Narsistlik', 'Mazosizm', 'Depresif hasiyet', 'Antisosyal hasiyet', 'Borderline hasiyet', 'Bakna hasiyet', 'Obesiw kompulsif hasiyet']

        if len(word) > 0:
            hint_text = ''

        word_len = len(word)

        for i in words:
            if word == i[0 : word_len]:
                print(i)


    def go_characters(self):
        self.root.current = 'characters'

    def go_child(self):
        self.root.current = 'child'
    
    def go_acne(self):
        self.root.current = 'acne'
    
    def go_women(self):
        self.root.current = 'women'
    
    def go_man(self):
        self.root.current = ('man')
    
    def go_learn(self):
        self.root.current = 'learn'
    
    def go_battle(self):
        self.root.current = 'battle'

class Posibilyty_calc(Screen):
    
    def open_x_menu(self):

        menu_items = [
            {
                'text': 'Pes',
                'height': dp(40),
                "on_release": lambda x="Pes": self.x_callback(x),
            },
            {
                'text': 'Erbet dal',
                'height': dp(40),
                "on_release": lambda x="Erbet dal": self.x_callback(x),
            },
            {
                'text': 'Onat',
                'height': dp(40),
                "on_release": lambda x="Onat": self.x_callback(x),
            },
            {
                'text': 'Yokary',
                'height': dp(40),
                "on_release": lambda x="Yokary": self.x_callback(x),
            },
            {
                'text': 'Mejbur',
                'height': dp(40),
                "on_release": lambda x="Mejbur": self.x_callback(x),
            }
        ]

        self.x_menu = MDDropdownMenu(
            caller=self.x_info,
            items=menu_items,
        )

        self.x_menu.open()

    def open_y_menu(self):

        menu_items = [
            {
                'text': 'Pes',
                'height': dp(40),
                "on_release": lambda x="Pes": self.y_callback(x),
            },
            {
                'text': 'Erbet dal',
                'height': dp(40),
                "on_release": lambda x="Erbet dal": self.y_callback(x),
            },
            {
                'text': 'Onat',
                'height': dp(40),
                "on_release": lambda x="Onat": self.y_callback(x),
            },
            {
                'text': 'Yokary',
                'height': dp(40),
                "on_release": lambda x="Yokary": self.y_callback(x),
            },
            {
                'text': 'Mejbur',
                'height': dp(40),
                "on_release": lambda x="Mejbur": self.y_callback(x),
            }
        ]

        self.y_menu = MDDropdownMenu(
            caller=self.y_info,
            items=menu_items,
        )

        self.y_menu.open()

    def open_z_menu(self):

        menu_items = [
            {
                'text': '0%',
                'height': dp(40),
                "on_release": lambda x="0%": self.z_callback(x),
            },
            {
                'text': '10%',
                'height': dp(40),
                "on_release": lambda x="10%": self.z_callback(x),
            },
            {
                'text': '20%',
                'height': dp(40),
                "on_release": lambda x="20%": self.z_callback(x),
            },
            {
                'text': '30%',
                'height': dp(40),
                "on_release": lambda x="30%": self.z_callback(x),
            },
            {
                'text': '40%',
                'height': dp(40),
                "on_release": lambda x="40%": self.z_callback(x),
            },
            {
                'text': '50%',
                'height': dp(40),
                "on_release": lambda x="50%": self.z_callback(x),
            },
            {
                'text': '60%',
                'height': dp(40),
                "on_release": lambda x="60%": self.z_callback(x),
            },
            {
                'text': '70%',
                'height': dp(40),
                "on_release": lambda x="70%": self.z_callback(x),
            },
            {
                'text': '80%',
                'height': dp(40),
                "on_release": lambda x="80%": self.z_callback(x),
            },
            {
                'text': '90%',
                'height': dp(40),
                "on_release": lambda x="90%": self.z_callback(x),
            },
            {
                'text': '99%',
                'height': dp(40),
                "on_release": lambda x="99%": self.z_callback(x),
            }
        ]

        self.z_menu = MDDropdownMenu(
            caller=self.z_info,
            items=menu_items,
        )

        self.z_menu.open()

    def head(self):

        menu_items = [
            {
                'text': 'Yeterlik dal',
                'height': dp(40),
                "on_release": lambda x="Yeterlik dal": self.head_callback(x),
            },
            {
                'text': 'Onat',
                'height': dp(40),
                "on_release": lambda x="Onat": self.head_callback(x),
            },
            {
                'text': 'Yeterlik',
                'height': dp(40),
                "on_release": lambda x="Yeterlik": self.head_callback(x),
            }
        ]
        self.head_menu = MDDropdownMenu(
            caller=self.head_info,
            items=menu_items,
        )

        self.head_menu.open()

    def body(self):

        menu_items = [
            {
                'text': 'Yeterli dal',
                'height': dp(40),
                "on_release": lambda x="Yeterli dal": self.body_callback(x),
            },
            {
                'text': 'Onat',
                'height': dp(40),
                "on_release": lambda x="Onat": self.body_callback(x),
            },
            {
                'text': 'Yeterlik',
                'height': dp(40),
                "on_release": lambda x="Yeterlik": self.body_callback(x),
            }
        ]
        self.body_menu = MDDropdownMenu(
            caller=self.body_info,
            items=menu_items,
        )

        self.body_menu.open()

    def on_enter(self):

        from utils.probability import Calc_probality
        self.probability_calc = Calc_probality()

        self.c_info = self.ids.user_input_text_c
        self.d_info = self.ids.user_input_text_d
        self.e_info = self.ids.user_input_text_e
        self.f_info = self.ids.user_input_text_f
        self.e_info_alpha = self.ids.second_text_input_e
        self.f_info_alpha = self.ids.second_text_input_f
        self.x_info = self.ids.x_info
        self.y_info = self.ids.y_info
        self.z_info = self.ids.z_info
        self.head_info = self.ids.head_info
        self.body_info = self.ids.body_info

    def reset_button(self, instance):

        if instance: 
            self.c_info.text = ''
            self.d_info.text = ''
            self.e_info.text = ''
            self.f_info.text = ''
            self.e_info_alpha.text = ''
            self.f_info_alpha.text = ''

    def control(self, instance):

        if instance:
            self.probability_calc.control_input(self.c_info.text, self.d_info.text, self.e_info.text, self.f_info.text, self.e_info_alpha, self.f_info_alpha, self.x_info, self.y_info, self.z_info, self.head_info, self.body_info)

   
    def x_callback(self, text_item):
        self.x_info.text = text_item

    def y_callback(self, text_items):
        self.y_info.text = text_items

    def z_callback(self, text_items):
        self.z_info.text = text_items

    def head_callback(self, text_items):
        self.head_info.text = text_items 
        
    def body_callback(self, text_items):
        self.body_info.text = text_items


    def get_result(self, result):

        rounded_result = round(result)
        str_result = str(rounded_result)
        print(str_result)
        
        dialog = MDDialog(
            text=f'Isin yerine yetme mumkinciligi {str_result}%'
            )
        dialog.open()


class Main(Screen):    

    def on_enter(self):
        pass        
    
    def abc_list(self):
        pass

    def random_list(self):
        pass

    def get_favorites(self):


        if len(self.favorite_list) < 1:
            Demo.remove_widgets()

            not_favorite = 'Halananlar tapylmady'
            label = MDLabel(
                text=not_favorite,
                size_hint_x=.5
            )

        self.main.add_widget(label)

    
class Setting(Screen):
    pass


class Characters(Screen):
    def back_main(self):
        self.manager.current = 'main'

    def go_shy(self):
        self.manager.current = 'shy'

    def go_otism(self):
        self.manager.current = 'otism'

    def go_asperger(self):
        self.manager.current = 'asperger'

    def go_schizoid(self):
        self.manager.current = 'schizoid'

    def go_agresive(self):
        self.manager.current = 'agresive'

    def go_paranoid(self):
        self.manager.current = 'paranoid'

    def go_histrionic(self):
        self.manager.current = 'histrionic'

    def go_narcissism(self):
        self.manager.current = 'narcissism'

    def go_mazochism(self):
        self.manager.current = 'mazochism'

    def go_depresive(self):
        self.manager.current = 'depresive'

    def go_antisocial(self):
        self.manager.current = 'antisocial'

    def go_compulsive(self):
        self.manager.current = 'compulsive'

    def go_borderline(self):
        self.manager.current = 'borderline'

    def go_dependent(self):
        self.manager.current = 'dependent'

    

class Child(Screen):
    pass

class Acne(Screen):
    pass


class Women(Screen):
    pass


class Man(Screen):
    pass


class Learn(Screen):
    pass



class Battle(Screen):

    pass


class Shy(Screen):
    
    def on_enter(self):
        pass
    


class Otism(Screen):
    pass

class Asperger(Screen):
    pass


class Schizoid(Screen):
    pass


class Agresive(Screen):
    pass


class Paranoid(Screen):
    pass


class Histrionic(Screen):
    pass


class Narcissism(Screen):
    pass


class Mazochism(Screen):
    pass


class Depresive(Screen):
    pass


class Antisocial(Screen):
    pass

class Compulsive(Screen):
    pass


class Borderline(Screen):
    pass


class Dependent(Screen):
    pass


if __name__ == '__main__':
    Demo().run()