class member:
    def __init__(self, name, visits, months):
        self.name = name
        self.visits = visits
        self.months = months
    
    def is_at_risk(self):
        return self.visits < 4 and self.months > 6
#object    
m1 = member("Athabol Ritphad", 2, 10)
m2 = member("Steven Gerrard", 8, 10)
m3 = member("Cristiano Ronaldo", 15, 4)
m4 = member("Leonel Messi", 15, 12)

for m in [m1, m2, m3, m4]:
    print(f"ชื่อสมาชิก : {m.name}")
    print(f"เสี่ยงเลิกใช้บริการ : {m.is_at_risk()}")
    print("--------------------")
