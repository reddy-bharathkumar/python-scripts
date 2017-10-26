import paragraphs
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textInput import TextInput

class TypingScreen(Label):
  def __init__(self, **kwargs):
    super(TypingScreen, self).__init__(**kwargs)
  
  @staticmethod
  def retrieveParagraph(mode):
    para_key=str(randint(1,11))
    paragraph=paragraphs.paradict(mode,para_key)
    
    print("Press Enter once your typing is completed!")
    
    self.cols=1
    self.add_widget(Label(text=paragraph, font_size='20sp'))
    self.add_widget(TextInput(multiline=True, font_size='20sp', focus=True))
    
 class typingScreen(App):
  def build(self):
    return TypingScreen()
 
 if __name__=="__main__":
  typingScreen().run()
