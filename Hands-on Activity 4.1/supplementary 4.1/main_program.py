import projectilemotion

speed = 11.0
angle = 20.0

r, h = projectilemotion.projectilemotion_solver(speed, angle)

print(f"Horizontal Distance (Range): {r:.2f} m")
print(f"Maximum Height: {h:.2f} m")

