grams_per_lots = 13.3
lots_per_pounds = 32
pounds_per_talents = 20

talents = float(input("enter talents: \n"))
pounds = float(input("enter pounds: \n"))
lots = float(input("enter lots: \n"))

grams_from_talents = talents * pounds_per_talents * lots_per_pounds * grams_per_lots
grams_from_pounds = pounds * lots_per_pounds * grams_per_lots
grams_from_lots = lots * grams_per_lots
total_grams = grams_from_talents + grams_from_pounds + grams_from_lots

kilograms = int(total_grams // 1000)
grams = total_grams % 1000

print("\nthe weight in modern units")
print(f"{kilograms} kilograms and {grams:.2f} grams.")

