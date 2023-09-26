class Vehicle:
    def __init__(self, make="", model=""):
        self.VehicleMake = make
        self.VehicleModel = model

    def SetVehicleMake(self, make):
        self.VehicleMake = make

    def SetVehicleModel(self, model):
        self.VehicleModel = model

    def GetVehicleMake(self):
        return self.VehicleMake

    def GetVehicleModel(self):
        return self.VehicleModel


class Car(Vehicle):
    def __init__(self, make="", model="", doors=""):
        self.CarDoor = doors
        self.VehicleMake = make  # Initialize Vehicle attributes directly
        self.VehicleModel = model

    def SetCarDoor(self, doors):
        self.CarDoor = doors

    def GetCarDoor(self):
        return self.CarDoor


class Truck(Vehicle):
    def __init__(self, make="", model="", bed_length=""):
        self.BedLength = bed_length
        self.VehicleMake = make  # Initialize Vehicle attributes directly
        self.VehicleModel = model

    def SetBedLength(self, length):
        self.BedLength = length

    def GetBedLength(self):
        return self.BedLength


while True:
  input_vehicle = input("\nEnter 1 to make a car, 2 for a truck or 3 to quit: ")
  
  if input_vehicle == '3':
    break
  
  elif input_vehicle == '1':
    new_car = Car()
    
    make = input("Enter car make: ")
    new_car.SetVehicleMake(make)
    
    model = input("Enter car model: ")
    new_car.SetVehicleModel(model)
    
    doors = input("Enter number of doors: ")
    new_car.SetCarDoor(doors)

    print(f"\nThe car make is: {new_car.GetVehicleMake()}.")
    print(f"The car model is: {new_car.GetVehicleModel()}.")
    print(f"The car has: {new_car.GetCarDoor()} doors.")

  elif input_vehicle == '2':
    new_truck = Truck()
    
    make = input("Enter truck make: ")
    new_truck.SetVehicleMake(make)
    
    model = input("Enter truck model: ")
    new_truck.SetVehicleModel(model)
    
    bed_length = input("Enter bed length: ")
    new_truck.SetBedLength(bed_length)

    print(f"\nThe truck make is: {new_truck.GetVehicleMake()}.")
    print(f"The truck model is: {new_truck.GetVehicleModel()}.")
    print(f"The bed length is: {new_truck.GetBedLength()} inches.")

    
  