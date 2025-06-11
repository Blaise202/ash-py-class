inventory = 200
week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
for day in week:
    print(f"{day} - Starting inventory: {inventory} books")

    if day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
        inventory -= 30  # books sold
        inventory += 25  # books restocked
    elif day == "Saturday":
        inventory -= 45  # books sold, no restock
    print(f"{day} - Ending inventory: {inventory} books\n")

print(f"Final inventory on Sunday night: {inventory} books")
