class Shit:
    def __init__(self):
        self.string = "this is the new shit"

    def __access(self):
        return self.string


shit = Shit()
shit.shit = "wtf"
print(shit.__attr__)