rivers = [
    {"name": "Nile", "length": 4157},
    {"name": "Yangtze", "length": 3434},
    {"name": "Murray-Darling", "length": 2310},
    {"name": "Volga", "length": 2290},
    {"name": "Mississippi", "length": 2540},
    {"name": "Amazon", "length": 3915}
]

# Task 1: Print out each river's name
print("Task 1:")
for river in rivers:
    print(river["name"])

# Task 2: Calculate and print the total length of all rivers
total_length = sum(river["length"] for river in rivers)
print("\nTask 2:")
print(f"Total length of all rivers: {total_length} miles")

# Extension 1: Print out river names that begin with the letter M
print("\nExtension 1:")
for river in rivers:
    if river["name"].startswith("M"):
        print(river["name"])

# Extension 2: Convert river lengths from miles to kilometers and print
print("\nExtension 2:")
for river in rivers:
    length_km = river["length"] * 1.6
    print(f"{river['name']} - Length: {length_km:.2f} km")