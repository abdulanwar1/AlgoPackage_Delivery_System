# Mohammad Haji
# ID #009453651

import csv
from datetime import datetime, timedelta
from package import Package
from truck import Truck
# WGU code repository W-2_ChainingHashTable_zyBooks_Key-Value_CSV_Greedy.py
# This is the chainingHashTable I will be using throughout the project, it has all necessary functions I need
class ChainingHashTable:
    def __init__(self, initial_capacity=20):
        self.list = []
        for i in range(initial_capacity):
            self.list.append([])

    def insert(self, key, item):
        bucket = hash(key) % len(self.list)
        bucket_list = self.list[bucket]

        for kv in bucket_list:
            if kv[0] == key:
                kv[1] = item
                return True

        key_value = [key, item]
        bucket_list.append(key_value)
        return True

    def remove(self, key):
        bucket = hash(key) % len(self.list)
        for i, kv in enumerate(self.list[bucket]):
            if kv[0] == key:
                del self.list[bucket][i]
                break

    def lookup(self, key):
        bucket = hash(key) % len(self.list)
        for kv in self.list[bucket]:
            if kv[0] == key:
                return kv[1]
        return None

    def get_keys(self):
        keys = []
        for bucket in self.list:
            for kv in bucket:
                keys.append(kv[0])
                return keys
        return None
HashTable = ChainingHashTable()





# Package object that will read from the package.csv
# It will the string EOD to timedelta
# It will then create package with all the attributes from the Package class
# It will then insert it into the HashTable
# It will then append package into package_list
package_list = []

with open('package.csv', mode='r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        package_id = int(row[0])
        address = row[1]
        city = row[2]
        state = row[3]
        zip_code = row[4]
        if row[5] == 'EOD':
            delivery_deadline = timedelta(hours = 23, minutes = 59)
        else:
            h,m = row[5].split(':')

            delivery_deadline = timedelta(hours = int(h),minutes = int(m))
        weight = int(row[6])
        status = row[7]

        package = Package(package_id, address, city, state, zip_code, delivery_deadline, weight, status)
        HashTable.insert(package_id, package)
        package_list.append(package)

print(package_list)

# these are the truck object

truck1 = Truck(1, timedelta(hours=8), [15, 1, 13, 14, 16, 20, 29, 30, 31, 34, 37, 40])
truck2 = Truck(2, timedelta(hours=9, minutes=5), [3, 6, 12, 17, 18, 19, 21, 22, 23, 24, 26, 27, 35, 36, 38, 39])
truck3 = Truck(3, timedelta(hours=9, minutes=5), [2, 4, 5, 7, 8, 9, 10, 11, 25, 28, 32, 33, 10])







# This will read from the distance.csv and create distanceData []
distanceData = []
def loadDistanceData(distanceData):
    with open("distances.csv", "r") as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            distanceData.append(row)
loadDistanceData(distanceData)


# This will read from the address.csv and create addressData []
addressData = []
def loadAddressData(addressData):
    with open('address.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            addressData.append(row)
loadAddressData(addressData)






# This is the algorithm I will be using
def nearest_neighbor(truck):

    # Store the starting address of the truck
    current_address = truck.starting_address
    # Store the current time
    current_time = truck.start_time
    # Store the current mileage
    current_mileage = 0
    while True:
        # This while statement will be the main algorithm
        # I have created a few variables that we will compare throughout the code
        winnerAddress = None
        winnerDistance = 10000
        winnerPackage = None
        for package_id in truck.packages:
        # This for loop checks for package id in truck.packages
        # It will use the Hashtable to lookup by package id
        # It will help accomodate some of the special circumstances for the packages
        # it will then use the addressData and distance Data to see the distance between addresses
        # It will assign that distance to the distance variable
        # It will compare the distance to the variables we created initially and assign accordingly
        # It will then calculate the time, mileage, and distance appropriately




            package = HashTable.lookup(package_id)
            if package.delivery_time != None:
                continue
            if package_id in [6,25,28,32]:
                if current_time < timedelta(hours=9, minutes=5):
                    continue
            if package_id in [9]:
                if current_time < timedelta(hours=10, minutes=20):
                    continue

            package_address = package.address
            package_address_index = None
            for address in addressData:

                if address[2] == package_address:
                    package_address_index = int(address[0])
                    break

            if package_address_index is None:
                print(f"Address {package_address} not found in addressData")
                continue
            current_address_index = None
            for add in addressData:
                if add[2] == current_address:
                    current_address_index = int(add[0])
                    break

            if current_address_index is None:
                print(f"Address {current_address} not found in addressData")
                continue
            try:
                distance = float(distanceData[current_address_index][package_address_index])
            except:

                distance = float(distanceData[package_address_index][current_address_index])
            if distance< winnerDistance:
                winnerDistance = distance
                winnerAddress = package_address
                winnerPackage = package
        if winnerAddress == None:
            break

        current_address = winnerAddress
        current_mileage += winnerDistance
        current_time += timedelta(hours= winnerDistance/ 18)
        winnerPackage.delivery_time = current_time
        winnerPackage.departure_time = truck.start_time

        truck.total_miles = current_mileage


# These are the instances of the nearest_neighbor that take in all three trucks
nearest_neighbor(truck1)
nearest_neighbor(truck2)
nearest_neighbor(truck3)


while True:
# This is my user interface
# It takes in four options to accommodate each request
# For option A and B, I have created an if else statement that gives the proper status
# Option C gives you the total mileage and D exits

    user_input = input("Enter command "
                       "\n(A: to get a status for given time)"
                       "\n(B: to get all statuses for a given time) "
                       "\n(C: to get the total mileage for the trucks) "
                       "\n(D: to exit) ")
    if user_input == "A":
        package_id = int(input("Enter package ID: "))
        package = HashTable.lookup(package_id)
        h,m = input("Enter a time in format HH:MM").split(":")
        time = timedelta(hours = int(h),minutes = int(m))
        if time < package.departure_time:
            package.status = "at hub"
        elif time < package.delivery_time:
            package.status = "en route"
        else:
            package.status = f"delivered {package.delivery_time}"
            if package.delivery_time > package.delivery_deadline:
                print("Missed deadline")
        print(str(package))

    elif user_input == "B":
        h, m = input("Enter a time in format HH:MM").split(":")
        time = timedelta(hours = int(h),minutes = int(m))
        packages = []
        try:
            for package_id in range(1,41):
                package = HashTable.lookup(package_id)


                if time < package.departure_time:

                    package.status = "at hub"
                elif time < package.delivery_time:
                    package.status = "en route"
                else:
                    package.status = f"delivered {package.delivery_time}"
                print(str(package))
        except ValueError:
            print("Incorrect input")



    elif user_input == "C":
        print(f"Truck 1 total miles: {truck1.total_miles}")
        print(f"Truck 2 total miles: {truck2.total_miles}")
        print(f"Truck 3 total miles: {truck3.total_miles}")
        print(truck1.total_miles + truck2.total_miles + truck3.total_miles)
    elif user_input == "D":
        print("Exiting program.")
        break
    else:
        print("Invalid command.")
