# This is the package class that contains all the necessary attributes from the package.csv and that will be used
# all throughout the project
class Package:
    def __init__(self, package_id, address, city, state, zip_code, delivery_deadline, weight, status):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.delivery_deadline = delivery_deadline
        self.weight = weight
        self.status = status
        self.departure_time = None
        self.delivery_time = None
    def __str__(self):
        return f"Package ID: {self.package_id}," \
               f" Address: {self.address}, City: {self.city}," \
               f" State: {self.state}, Zipcode: {self.zip_code}," \
               f" Delivery_Deadline: {self.delivery_deadline}," \
               f" Weight: {self.weight}, Status: {self.status}"