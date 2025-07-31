# Displacement calculator in Python

u = float(input("Enter initial velocity (u) in m/s: "))
t = float(input("Enter time (t) in seconds: "))
a = float(input("Enter acceleration (a) in m/s²: "))

# Calculate displacement
s = u * t + 0.5 * a * t * t

print("Displacement is:", s, "meters")
