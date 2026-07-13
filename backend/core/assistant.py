class Huginn:

    def __init__(self, name = "Huginn"):
        self.name = name
        self.version = "0.1.0"
        self.interests = []

    def speak(self):
        print(f"🐦 Bonjour, je suis {self.name}.")
        
    def add_interest(self, interest):
        self.interests.append(interest)