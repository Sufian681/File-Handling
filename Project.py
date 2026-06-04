print("Creating your initial shoppig list...")
initial_items = ["Apples", "Milk", "Bread", "Eggs"]

with open("shopping_list.txt", "w") as file:
    for item in initial_items:
        file.write(item + "\n")
print("Initial list saved successfully.\n")

print("--- Reading Complete File ---")
with open("shopping_list.txt", "r") as file:
    content = file.read()
    print(content)

print("Adding new items to your list...")
new_items = ["Chicken", "Eggs"]

with open("shopping_list.txt", "a") as file:
    for item in new_items:
        file.write(item + "\n")
print("New items added successfully.\n")
print("--- Reading Updated File Line by Line ---")
with open("shopping_list.txt", "r") as file:
    for line in file:
        print(f"- {line.strip()}")


