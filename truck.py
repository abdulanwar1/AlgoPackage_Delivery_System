# This is the truck class that contains attributs that we will use throughout the project.
# For instance, the total miles and total delivery attributes will calculate the total mileage of the trucks and the time.
#
class Truck:
    def __init__(self, truck_id, start_time, packages=[]):
        self.truck_id = truck_id
        self.start_time = start_time
        self.packages = packages
        self.total_miles = 0
        self.total_delivery_time = 0
        self.starting_address = "4001 South 700 East"
    def add_package(self, package):
        self.packages.append(package.package_id)

    def __str__(self):
        return f"Truck ID: {self.truck_id}, Start Time: {self.start_time}, Total miles: {self.total_miles}, Total delivery time: {self.total_delivery_time}, Packages: {self.packages}"
