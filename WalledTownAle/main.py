import datetime
import math

print("Welcome to Walled Town Ale Order Platform\n".center(100))
print("Please, complete the following fields for delivery:\n")

# --- User Name and Address Inputs--- #
companyName = input("Company Name:    ").strip()
companyPhoneNumber = input("Phone Number:    ").strip()
street = input("Street Address:  ")
town = input("Town/City:       ")
county = input("County:          ")
actualDate = datetime.datetime.today().strftime('%d-%m-%Y')
companyInvoiceNo = ("WTA" + companyPhoneNumber.lstrip("0")[0:2] + companyPhoneNumber[-2:] + companyName[-2]).upper()

print("\nPlease, complete the following fields to make your order:\n")
# --- User Barrels Order --- #
butchersUnits = int(input("Butcher's Pale Ale Barrels Units:   "))
farriersUnits = int(input("Farriers' IPA Barrels Units:        "))
gatehouseUnits = int(input("Gatehouse Brown Ale Barrels Units:  "))

# -- Check how many spaces left in a Rack -- #
# 1 Rack = 15 spaces
checkRackSpaces = 15 - ((butchersUnits + farriersUnits + gatehouseUnits) % 15)
surcharge = 0

if checkRackSpaces < 15:
    surcharge = checkRackSpaces * 2

# -- Check discount Butchers' Pale Ale-- #
butchersBarrelPriceTotal = round(butchersUnits * 125.50, 3)
butchersBarrelUnitsDiscount = math.floor(butchersUnits / 10) * 10
butchersBarrelDiscountPrice = round(butchersBarrelUnitsDiscount * 10, 2)
butchersBarrelTotalAfterDiscount = round(butchersBarrelPriceTotal - butchersBarrelDiscountPrice, 2)

# -- Check discount Farriers' IPA-- #
farriersBarrelPriceTotal = round(farriersUnits * 105.90, 2)
farriersBarrelUnitsDiscount = math.floor(farriersUnits / 12) * 12
farriersBarrelDiscountPrice = round(farriersBarrelUnitsDiscount * 8.40, 2)
farriersBarrelTotalAfterDiscount = round(farriersBarrelPriceTotal - farriersBarrelDiscountPrice, 2)

# -- Check discount Gatehouse Brown Ale-- #
gatehouseBarrelPriceTotal = round(gatehouseUnits * 132.35, 2)
gatehouseBarrelUnitsDiscount = math.floor(gatehouseUnits / 9) * 9
gatehouseBarrelDiscountPrice = round(gatehouseBarrelUnitsDiscount * 11.65, 2)
gatehouseBarrelTotalAfterDiscount = round(gatehouseBarrelPriceTotal - gatehouseBarrelDiscountPrice, 2)


subtotal = round(butchersBarrelPriceTotal + farriersBarrelPriceTotal + gatehouseBarrelPriceTotal, 2)
totalDiscount = round(butchersBarrelDiscountPrice + farriersBarrelDiscountPrice + gatehouseBarrelDiscountPrice, 2)


# --- PRINT RECEIPT --- #
boldLine = "\u2501" * 18

print(f"{'':>50}{'Walled Town Ale'}")
print(f"{'':>70}{'Invoice No:':<20}{companyInvoiceNo}")
print(f"{'':>70}{'Date:':<20}{actualDate}")
print("")
print(f"{'Company Name:':<15}{companyName}")
print(f"{'Address:':<15}{street}\n{'':<15}{town}\n{'':<15}{county}")
print("\nSales Details:\n")
butchersPaleAleName = "Butchers' Pale Ale:"
farriersIpaName = "Farriers' Ipa:"
gatehouseBrownAleName = "Gatehouse Brown Ale:"
print(f"{butchersPaleAleName:<50}{butchersUnits:<40}{butchersBarrelPriceTotal:.2f}")
print(f"{farriersIpaName:<50}{farriersUnits:<40}{farriersBarrelPriceTotal:.2f}")
print(f"{gatehouseBrownAleName:<50}{gatehouseUnits:<40}{gatehouseBarrelPriceTotal:.2f}\n")

print(boldLine.rjust(100))
print(f"{'':<70}{'Subtotal:':<20}{subtotal:.2f}")


if checkRackSpaces < 15:
    print("\nSurcharge:")
    print(f"{'Rack spaces unused:':<50}{checkRackSpaces:<40}{surcharge:.2f}")

if totalDiscount > 0:
    print("\nDiscount:")

if butchersBarrelDiscountPrice > 0:
    print(f"{butchersPaleAleName:<50}{butchersBarrelUnitsDiscount:<40}{butchersBarrelDiscountPrice:.2f}")

if farriersBarrelDiscountPrice > 0:
    print(f"{farriersIpaName:<50}{farriersBarrelUnitsDiscount:<40}{farriersBarrelDiscountPrice:.2f}")

if gatehouseBarrelDiscountPrice > 0:
    print(f"{gatehouseBrownAleName:<50}{gatehouseBarrelUnitsDiscount:<40}{gatehouseBarrelDiscountPrice:.2f}")


print(boldLine.rjust(100))
print(f"{'':<70}{'Total:':<20}{(subtotal - totalDiscount + surcharge):.2f}")
