class member:
    def __init__(self, name, visits, months, monthly_fee):
        self.name = name
        self.visits = visits
        self.months = months
        self.monthly_fee = monthly_fee
    
    def is_at_risk(self):
        return self.visits < 4 and self.months > 6
    
    def total_paid(self):
        return self.months*self.monthly_fee
    
#object    
m1 = member("Athabol Ritphad", 2, 10, 900)
m2 = member("Steven Gerrard", 8, 10, 900)
m3 = member("Cristiano Ronaldo", 15, 4, 900)
m4 = member("Leonel Messi", 15, 12, 900)

for m in [m1, m2, m3, m4]:
    print(f"ชื่อสมาชิก : {m.name}")
    print(f"เสี่ยงเลิกใช้บริการ : {m.is_at_risk()}")
    print(f"ยอดชำระรวม : {m.total_paid()} บาท")
    print("--------------------")
