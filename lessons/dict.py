"""Practice with dictionary"""

ice_cream: dict[str, int] = {"chocolate": 12, "vanilla": 8, "strawberry": 5}
ice_cream["mint"] = 3
print("After adding mint:")
print(ice_cream)


ice_cream.pop("mint")
print("after removing mint")
print(ice_cream)

# accessing
print(f"Number of vanilla orders: {ice_cream['vanilla']}")


#updating a value
ice_cream["vanilla"] += 1
print(ice_cream)   

#check if key is in dictionary
print("chocolate" in ice_cream)
print("mint" in ice_cream)

print(ice_cream["pecan"])
