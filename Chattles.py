from Chattler import checker
import re
from NER import show_ents
class Rulebot():
    neg = ("no",
    "nope",
    "not really",
    "nah",
    "i don't think so", "n")
    Neutr = ("i'm not sure", "I don't know","idk")
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
        will_help = input(f"Hi {self.name}, This is MKT-B's Fake News Detection Chatbot where we apply NLP concepts into a real workl use\n Do you want to use us?\n ")
        if will_help.lower() in self.neg:
            print("I see...")
        elif will_help.lower in self.posi:
            self.chat()
        elif will_help.lower() in self.exits:
            self.exiting(will_help)
        else:
            print("please give a positive or negative response")
            self.greet()

    def exiting(self,reply):
        for command in self.exits:
            if reply == command:
                print("see you next time")
                quit()

    def chat(self):
        print("Let's get started")
        starter = input("Do you want to look at newws\n")
        if starter in self.posi:
            news = input("Give me the news snippet.\n")
            if news.lower() in self.neg:
                print("oh...\n Well then...\n Do you want to quit?")
                quiter = input()
                if quiter.lower() in self.posi:
                    self.exiting("quit")
            elif news.lower() in self.exits:
                self.exiting(news)
            else:
                if checker(news) == 1:
                    print("This Headlines seems to be legit")
                else:
                    print("This seems not to be true")

                conti = input("do you want to Know more?")
                if conti in self.posi:
                    print("Your doc talks about some things:")
                    show_ents(news)
                elif conti.lower() in self.exits:
                    self.exiting(conti)
                elif conti in self.neg:
                    print("Okay then, do you want to continue?")
                    checks = input()
                    if checks in self.neg:
                        print("oh...\n Well then...\n Do you want to quit?")
                    quiter = input()
                    if quiter.lower() in self.posi:
                        self.exiting("quit")
        elif starter in self.neg:
            print("oh...\n Well then...\n Do you want to quit?")
            quiter = input()
            if quiter.lower() in self.posi:
                self.exiting("quit")
            if quiter.lower() in self.exits:
                self.exiting(quiter)


    def match_reply(self, reply):
        for key, value in self.babble.items():
            intent = key
            pattern = value
            match  = re.match(pattern, reply)
            if reply.lower() in self.exits:
                self.exiting(reply)
            if match and intent == 'about_MKT-B':
                return self.about()
            elif match and intent =='why':
                return self.why()
            else:
                return self.no_match()
            
    def about(self):
        print("We are a group of data scientists and NLP students looking to apply our abilities")
    
    def why(self):
        print("We wnat to make an easy and convenient way to debunk problematic newsheadlines as thye are bad for society")
    def no_match(self):
        print("I'm not quite sure how to handle that, meet with the team to help us solve this issue\n")


Clat = Rulebot()
Clat.greet()