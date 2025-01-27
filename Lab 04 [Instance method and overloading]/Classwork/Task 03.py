 

#task 3
class TaxiLagbe:
    def __init__(self, taxi_number, area):
        self.taxi_number = taxi_number
        self.area = area
        self.passengers = []
        self.total_fare = 0

    def addPassenger(self, *passenger_info):
        if len(self.passengers) < 4:
            for info in passenger_info:
                last_name, fare = info.split('_')
                self.passengers.append(last_name)
                self.total_fare += int(fare)
                print(f"Dear {last_name}! Welcome to TaxiLagbe.")
        else:
            print("Taxi Full! No more passengers can be added.")

    def printDetails(self):
        print(f"Trip info for Taxi number: {self.taxi_number}")
        print(f"This taxi can only cover the {self.area} area.")
        print(f"Total passengers: {len(self.passengers)}")
        print("Passenger lists:")
        print(', '.join(self.passengers))
        print(f"Total collected fare: {self.total_fare} Taka")

# Driver Code
taxi1 = TaxiLagbe('1010-01', 'Dhaka')
print('-------------------------------')
taxi1.addPassenger('Walker_100', 'Wood_200', 'Matt_100')
taxi1.addPassenger('Wilson_105')
print('-------------------------------')
taxi1.printDetails()
print('-------------------------------')
taxi1.addPassenger('Karen_200')
print('-------------------------------')
taxi1.printDetails()
print('-------------------------------')
taxi2 = TaxiLagbe('1010-02', 'Khulna')
taxi2.addPassenger('Ronald_115', 'Parker_215')
print('-------------------------------')
taxi2.printDetails()