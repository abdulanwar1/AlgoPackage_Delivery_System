# AlgoPackage_Delivery_System
🚚 Package Delivery System Simulation 🚚

This project simulates a package delivery system using a greedy algorithm for route optimization. The system reads data from CSV files, assigns packages to trucks, and computes the most efficient route for each truck based on proximity using a Nearest Neighbor Algorithm. The goal is to ensure that all packages are delivered on time while tracking truck mileage and delivery statuses at any given time.
🔑 Key Features:

    Greedy Nearest Neighbor Algorithm: Optimizes the delivery route by always selecting the closest undelivered package.
    Dynamic Package Tracking: View the status of any package at any time (at hub, en route, delivered).
    User Interaction: Real-time command-line interface for querying delivery status, total mileage, and package deadlines.
    Chaining Hash Table: Efficient package lookup by ID for quick access to package details.
    CSV Data Input: Reads package, address, and distance data from CSV files, making it easy to update or modify inputs.

🚀 How It Works:

    Package Management:
        The system reads from package.csv, converts "End of Day" to a proper time format, and stores the packages in a hash table.
        Each package contains details like delivery deadline, address, and status.

    Truck Scheduling:
        Three trucks are initialized with start times and assigned package IDs.
        The trucks navigate through the city based on distance.csv and address.csv files, using the Nearest Neighbor Algorithm to select the shortest available delivery path.

⚠️ Constraints:

    Package Delivery Time Windows:
        Some packages have specific time constraints and cannot be delivered before a certain time. For example:
            Package #6, 25, 28, 32: These packages cannot be delivered before 9:05 AM.
            Package #9: This package cannot be delivered before 10:20 AM.

    Truck Load and Departure:
        Truck 1 starts at 8:00 AM and is assigned specific packages.
        Truck 2 starts at 9:05 AM, carrying another set of packages.
        Truck 3 also starts at 9:05 AM, and its package load is optimized based on delivery constraints.

    End of Day (EOD) Deadlines:
        Some packages must be delivered by End of Day, which is converted to a time representation of 11:59 PM.

    Maximum Package Load:
        Each truck has a predefined list of package IDs that cannot exceed a reasonable limit.

🛠️ User Commands:

    Option A: Check the status of a specific package at a given time.
    Option B: View the statuses of all packages at a specified time.
    Option C: Get the total mileage of each truck and the combined mileage for all trucks.
    Option D: Exit the program.

📂 Data Input:

    package.csv: Contains package details such as ID, address, deadline, and weight.
    distances.csv: Provides the distances between all delivery addresses.
    address.csv: Stores address data with corresponding indices used to calculate distances.

🎮 How to Run:

    Clone the repository.
    Ensure the required CSV files (package.csv, distances.csv, address.csv) are in the same directory.
    Run the program:

    bash

    python package_delivery.py

    Follow the on-screen prompts to interact with the package delivery system.

This simulation provides an efficient way to manage package deliveries while adhering to time constraints and route optimization.
