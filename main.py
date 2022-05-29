import requests, threading, random


class Checker:
    def __init__(self):
        self.threads = 10
        self.hits    = 0
        self.fails   = 0
        self.file    = open('hits.txt', 'a')
        
        while True:
            if threading.active_count() < self.threads:
                threading.Thread(target=self.check_email)

    def check_email(self):
        email = f"{''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=5))}@gmail.com"
        r = requests.get(f"https://mail.google.com/mail/gxlu?email={email}")
        try:
            if r.headers["Set-Cookie"]:
                self.fails += 1
    
            else:
                self.hits += 1
                print(email); print(email, file=self.file)
        except:
            self.hits += 1
            print(email, file=self.file)


Checker()
