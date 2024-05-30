from Chattler import checker
import re

class Rulebot():
    neg = ("no",
    "nope",
    "not really",
    "nah",
    "i don't think so", "n")
    Neutr = ("i'm not sure, I don't know,idk, ¯\_(ツ)_/¯")
    posi = (    "yes",
    "sure",
    "of course",
    "absolutely",
    "you got it",
    "sounds good", "n")
    exits = ("bye",
            "goodbye",
            "exit",
    "quit",
    "see you later")

    def __init__(self):
        self.babble = {'why': r'.*\s*why*',
                       'about_MKT-B': r'*\s*about MKT-B',
                       }
        
    def greet(self):
        self.name = input("what is your name?\n")
        will_help = input(f"Hi {self.name}, This is MKT-B's Fake News Detection Chatbot where we apply NLP concepts into a real workl use\n Do you want to use us?")
        if will_help in self.neg:
            print("I see...")
            self.exiting("Goodbye")
        else:
            self.chat()

    def exiting(self,reply):
        for command in self.exits:
            if reply == command:
                print("see you next time")
                quit()

    def chat(self):
        news = input("Give me the news snippet.\n")
        if news.lower() in self.neg:
            print("oh...")
            self.exiting
        else:
            if checker(news) == 1:
                if checker.checkles == True:
                    restarter = input("That seems pretty short do you want to continue\n")
                    if restarter in self.neg:
                        
                print("This Headlines seems to be legit")
            else:
                print("seems pretty sus")

            conti = input("do you want to Know more?")
            if conti in self.neg:
                print("Okay then")
                conters = ("do you want to quit the bot?")
                if conters in self.neg:
                    print("Travis")
                    self.exiting()

    def match_reply(self, reply):
        for key, value in self.babble.items():
            intent = key
            pattern = value
            match  = re.match(pattern, reply)
            if match and intent == 'about_MKT-B':
                return self.about()
            elif match and intent =='why':
                return self.why()
            else:
                return self.no_match()
            
    def about(self):
        return "We are a group of data scientists and NLP students looking to apply our abilities"
    
    def why(self):
        return "We wnat to make an easy and convenient way to debunk problematic newsheadlines as thye are bad for society"
    def no_match(self):
        input("I'm not quite sure how to handle that, meet with the team to help us solve this issue\n")

Clat = Rulebot()
Clat.greet()