# class Talaba:
# def __init__(self, ism, familiya, tyil):
#     self.ism = ism
# self.familiya = familiya
# self.tyil = tyil

# def tanishtir(self):
# print(f"Ismim {self.ism} {self.familiya}. {self.tyil} yilda tugilganman")

# def get_name(self):
# return self.ism

# def get_lastname(self):
# return self.familiya

# def full_name(self):
#     return f"{self.ism} {self.familiya}"

# def get_age(self, yil):
#     return yil - self.tyil


# class User:
#     def __init__(self, name, username, email):
#         self.name = name
#         self.uname = username
#         self.mail = email
#
#     def get_name(self):
#         return f"Mening ismim {self.name}"
#
#     def get_user(self):
#         return f"Mening usernamemim {self.uname}"
#
#     def get_email(self):
#         return f"Mening emailim {self.mail}"
#
#
# malumot = User("Anvar", "Anvarovich", "anvar@gmail.com")
# print(malumot.name)
# print(malumot.uname)
# print(malumot.mail)


class Shaxs:
    def __init__(self, ism, familiya, passport, tyil):
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil
    def get_inf0(self):
        info = f"{self.ism} {self.familiya}."
        info += f"Passport:{self.passport}, {self.tyil} - yilda tug'ilgan"
        return info

    def get_age(self,yil):
        return yil -self.tyil

inson = Shaxs("Hasan", "Alimov", "FB001122", 1995)
print(f"{inson.get_inf0()}. {inson.get_age(2023)} yoshda")