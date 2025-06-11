original_people = 8
flour_grams = 300
eggs = 4
bake_minutes = 45
temperature_celsius = 180
new_people = 20
scale_factor = new_people / original_people
new_flour = flour_grams * scale_factor
new_eggs = eggs * scale_factor
temperature_fahrenheit = (temperature_celsius * 9/5) + 32

print("New Cookie Recipe for Happy Holdings")
print(f"Flour: {new_flour:.0f} grams")
print(f"Eggs: {new_eggs:.1f} eggs")
print(f"Bake Time: {bake_minutes} minutes")
print(f"Temperature: {temperature_fahrenheit:.1f}°F")
