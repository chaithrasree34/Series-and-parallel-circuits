# Series-and-parallel-circuits
# Series and Parallel Circuit Calculator

print("Series and Parallel Circuit Calculator")
print("1. Series Circuit")
print("2. Parallel Circuit")

choice = int(input("Enter your choice (1 or 2): "))

n = int(input("Enter the number of resistors: "))

resistors = []

for i in range(n):
    r = float(input(f"Enter resistance R{i + 1} (Ohm): "))
    resistors.append(r)

voltage = float(input("Enter supply voltage (V): "))

if choice == 1:
    # Series: Rt = R1 + R2 + R3 + ...
    total_resistance = sum(resistors)

    current = voltage / total_resistance

    print("\n--- Series Circuit ---")
    print("Total Resistance =", total_resistance, "Ohm")
    print("Total Current =", current, "A")

elif choice == 2:
    # Parallel: 1/Rt = 1/R1 + 1/R2 + 1/R3 + ...
    reciprocal = sum(1 / r for r in resistors)
    total_resistance = 1 / reciprocal

    total_current = voltage / total_resistance

    print("\n--- Parallel Circuit ---")
    print("Total Resistance =", total_resistance, "Ohm")
    print("Total Current =", total_current, "A")

else:
    print("Invalid choice!")
