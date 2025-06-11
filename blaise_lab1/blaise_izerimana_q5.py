energy = 50
week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
for day in week:
    print(f"{day} - Starting energy: {energy} units")

    if day != "Sunday":
        energy += 8    # Dawn
        energy -= 3    # Noon
        energy += 5    # Dusk

    print(f"{day} - Ending energy: {energy} units\n")

print(f"Final energy balance at the end of Sunday: {energy} units")
