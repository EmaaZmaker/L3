class bird:
    def __init__(self):
        print("bird is ready :p")
    def who_is_this(self):
        print("bird")
    def swim(self):
        print("SWIM FASTER")
class penguin(bird):
    def __init__(self):
        print("penguin is ready")
        super().__init__()
    def who_is_this():
        print("penguin")
    def run(self):
        print("RUN FASTER!")
obj=penguin()
obj.run()
obj.swim()
