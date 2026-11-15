name="Athabol Ritphad"
visits=2
months=10

#ฟังชั่นตรวจสอบความเสี่ยง
def is_at_risk(visits,months):
    return visits < 4 and months > 6

#แสดงผลลัพธ์
print(f"ชื่อสมาชิก : {name}")
print(f"จำนวนครั้งที่ใช้งาน : {visits} ครั้ง") 
print(f"อายุสมาชิก : {months} เดือน")
print(f"เสี่ยงเลิกใช้บริการ : {is_at_risk(visits,months)}")