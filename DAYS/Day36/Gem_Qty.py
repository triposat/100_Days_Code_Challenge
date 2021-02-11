Gem_Qty = {"ruby": 25, "diamond": 30,
           "emrald": 15, "topaz": 18, "sapphire": 20}
Gem_Price = {"ruby": 2000, "diamond": 4000,
             "emrald": 1900, "topaz": 500, "sapphire": 2500}
Gem_Name = input("Enter Gem Names: ").split(",")
Gem_Num = input("Enter Gem Quantities: ").split(",")
Total_Cost = 0
for items in range(len(Gem_Name)):
    Total_Cost = Total_Cost+int(Gem_Num[items])*Gem_Price[Gem_Name[items]]
    Gem_Qty[Gem_Name[items]] = Gem_Qty[Gem_Name[items]]-int(Gem_Num[items])

print(f"Total Cost: {Total_Cost}")
print(f"Gem_Qty: {Gem_Qty}")
