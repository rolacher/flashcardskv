# -*- coding: iso-8859-1 -*-

from kivy.app import App
from kivy.lang import Builder 
from kivy.uix.screenmanager import ScreenManager, Screen, SwapTransition, ObjectProperty
from kivy.uix.widget import Widget
from kivy.properties import StringProperty
from Flashcards import Flashcards, FlashcardsFile

# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.


testfile='''"FRONTSIDE";"BACKSIDE";"LASTSHOWNDATE";"NEXTSHOWDATE"
ad�quat;angemessen,richtig
After;Darmausgang
Agglutination;Zusammenballung,Verklumpung,hier von Blutzellen
allergisch (-e Reaktion);"�berreaktion" des K�rpers auf k�rperfremde,eigentlich unsch�dliche Substanzen
Alveolen (pulmonis);Lungenbl�schen
Anamnese;Krankengeschichte (Vorgeschichte oder Unfallhergang)
anaphylaktische (-e Reaktion);�berempfindliche (allergische) Reaktion des K�rpers
Antibiotika;Gruppe von Medikamenten zur Behandlung von bakteriellen Infektionskrankheiten
Aorta;gro�e K�rperschlagader
Aorta abdominalis;Bauchschlagader
apoplektischer Insult;kurz: Apoplex,(umgangssprachlich:Schlaganfall,Gehirnschlag)
Appendix;Wurmfortsatz des Blinddarmes
Appendizitis;Entz�ndung des Wurmfortsatzes
applizieren;verabreichen,anwenden
Apnoe;Atemstillstand
Ampulle;Glasbeh�ltnis f�r (in der Regel fl�ssige) Medikamente
A(r)rhythmie;unregelm��ige Herzfrequenz
a(r)rhythmisch;unregelm��ig
Arteriolen;kleine Arterien
Aspiration;Einatmung von festen oder fl�ssigen Stoffen in die Luftwege (die Lunge)
'''


Builder.load_string("""
<FrontsideScreen>:
    id: screen_frontside

    BoxLayout:
        orientation: 'vertical' 

        Label:
            text: self.parent.parent.text
            size_hint: 1, 0.8

        Button:
            text: 'Umdrehen'
            size_hint: 1, 0.2
            on_press: root.manager.current = 'backside'

<BacksideScreen>:
    id: screen_backside

    BoxLayout:
        orientation: 'vertical' 

        Label:
            text: self.parent.parent.text
            size_hint: 1, 0.8

        BoxLayout:
            orientation: 'horizontal' 
            size_hint: 1, 0.2

            Button:
                text: 'Richtig'
                on_press: root.do_update()

            Button:
                text: 'Falsch'
                on_press: root.manager.current = 'frontside'
""")

fc = FlashcardsFile(open("Flashcards.csv")).read()

# Declare both screens
class FrontsideScreen(Screen):
    global fc
    fc.toFirstCard()
    text = StringProperty(fc.front())

class BacksideScreen(Screen):
    global fc
    fc.toFirstCard()
    text = StringProperty(fc.back())

    def do_update(self):
        global fc
        fc.nextCard()
        self.manager.get_screen('frontside').text = fc.front()
        self.manager.get_screen('backside').text = fc.back()
        self.manager.current = 'frontside'

# Create the screen manager
sm = ScreenManager(transition=SwapTransition())
sm.add_widget(FrontsideScreen(name='frontside'))
sm.add_widget(BacksideScreen(name='backside'))

class TestApp(App):

    def build(self):
        return sm

if __name__ == '__main__':
    TestApp().run()

