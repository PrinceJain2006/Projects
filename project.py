class CarNode: 
    def __init__(self, car_number):   
        self.car_number = car_number
        self.next = None

class ParkingLot:
    def __init__(self, capacity):   
        self.capacity = capacity
        self.size = 0
        self.head = None

    def park_car(self, car_number):
        if self.size >= self.capacity:
            print("🚫 Parking lot is full!")
            return
        new_car = CarNode(car_number)
        new_car.next = self.head
        self.head = new_car
        self.size += 1
        print(f"✅ Car {car_number} parked.")

    def remove_car(self, car_number):
        prev, curr = None, self.head
        while curr:
            if curr.car_number == car_number:
                if prev:
                    prev.next = curr.next
                else:
                    self.head = curr.next
                self.size -= 1
                print(f"🚗 Car {car_number} exited.")
                return
            prev, curr = curr, curr.next
        print("❌ Car not found in lot.")

    def display_parking(self):
        curr = self.head
        print("🅿 Current parked cars:")
        while curr:
            print(curr.car_number, end=" -> ")
            curr = curr.next
        print("None")

lot = ParkingLot(3)
lot.park_car("KA-01-AA-1234")
lot.park_car("KA-02-BB-5678")
lot.park_car("KA-03-CC-9999")
lot.park_car("KA-04-DD-0000") 
lot.display_parking()
lot.remove_car("KA-02-BB-5678")
lot.display_parking()
