import pyttsx3

class speech:
    def convert(self,text,speed,gender):
        engine= pyttsx3.init()
        try:
            if speed == 2:
                engine.setProperty('rate',200)
            elif speed == 0:
                engine.setProperty('rate',50)
            else:
                engine.setProperty('rate',100)
            voices = engine.getProperty('voices')
            engine.setProperty('voice',voices[gender].id)
            engine.say(text)
            engine.runAndWait()
            
        except:
            print("we have some error")