

#Task1

class CellPackage:
    def __init__(self, price, data, talk_time, messages, cashback, validity):
          self.price=price
          self.data = data
          self.talk_time=talk_time
          self.messages=messages
          self.cashback=int(cashback.strip('%'))
          self.cash_back=int((self.cashback/100)*price)
          self.validity=validity
          gb_data= data.split()
          self.mb_data= int((gb_data[0]))*1024


pkg = CellPackage(150, '6 GB', 99, 20, '7%', 7)
print('============= Package 1 =============')
if pkg.mb_data>0:
  print(f"Data = {pkg.mb_data} MB")
if pkg.talk_time > 0:
        print(f"Talktime = {pkg.talk_time} Minutes")
if pkg.messages > 0:
          print(f"SMS/MMS = {pkg.messages}")
print(f"Validity = {pkg.validity} Days")
print(f"--> Price = {pkg.price} tk")
if pkg.cash_back > 0:
              print(f"Buy now to get {pkg.cash_back} tk cashback.")

pkg2 = CellPackage(700, '35 GB', 700, 0, '10%', 30)
print('============= Package 2 =============')
if pkg2.mb_data>0:
  print(f"Data = {pkg2.mb_data} MB")
if pkg2.talk_time > 0:
        print(f"Talktime = {pkg2.talk_time} Minutes")
if pkg2.messages > 0:
          print(f"SMS/MMS = {pkg2.messages}")
print(f"Validity = {pkg2.validity} Days")
print(f"--> Price = {pkg2.price} tk")
if pkg2.cash_back > 0:
              print(f"Buy now to get {pkg2.cash_back} tk cashback.")

pkg4 = CellPackage(120, '0 GB', 190, 0, '0%', 10)
print('============= Package 3 =============')
if pkg4.mb_data>0:
  print(f"Data = {pkg4.mb_data} MB")
if pkg4.talk_time > 0:
        print(f"Talktime = {pkg4.talk_time} Minutes")
if pkg4.messages > 0:
          print(f"SMS/MMS = {pkg4.messages}")
print(f"Validity = {pkg4.validity} Days")
print(f"--> Price = {pkg4.price} tk")
if pkg4.cash_back > 0:
              print(f"Buy now to get {pkg4.cash_back} tk cashback.")