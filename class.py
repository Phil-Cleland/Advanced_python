class Person:
    def __init__(self,name,Dob,age):
        self.name = name
        self.Dob = Dob
        self.age = age
        
    def speak(self):
        print ("hello")
    def walk(self):
        print ("walking away")
    def get_Dob(self):
        return self.Dob
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age


the_name= Person(input("Enter your name: "),input("Enter your Date of birth: "), int(input("Enter your age: ")))
print("Your name is ", the_name.name)
print("And you are " , the_name.age , "years old")

the_name.speak()
the_name.walk()
