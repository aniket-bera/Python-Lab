class Demo:
    string = ""

    def Get_String(self):
        self.string = input()
    
    def Print_String(self):
        print(self.string.upper())

ob1 = Demo()
ob1.Get_String()
ob1.Print_String()