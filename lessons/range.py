"""Demonstrate range in a loop."""

names: list[str] = ["Alyssa", "Vrinda", "Janet"]

for index in range(0, len(names)):
    print(f"{index}:{names[index]}")