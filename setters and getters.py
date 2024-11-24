class Harry:
    def set(self, nm):  # setter
        self.name = nm

    def get(self):  # getter
        print(f"The name is {self.name}")


a = Harry()
a.set(input("enter the name = "))
a.get()
