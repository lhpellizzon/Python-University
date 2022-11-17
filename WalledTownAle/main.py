import datetime
import math

print("Welcome to Walled Town Ale Order Platform\n".center(100))
print("Please, complete the following fields for delivery:\n")
#
# # --- User Name and Address Inputs--- #
# companyName = input("Company Name:    ").strip()
# companyPhoneNumber = input("Phone Number:    ").strip()
# street = input("Street Address:  ")
# town = input("Town/City:       ")
# county = input("County:          ")
# actualDate = datetime.datetime.today().strftime('%d-%m-%Y')
# companyInvoiceNo = ("WTA" + companyPhoneNumber.lstrip("0")[0:2] + companyPhoneNumber[-2:] + companyName[-2]).upper()
#
# print("\nPlease, complete the following fields to make your order:\n")
# # --- User Barrels Order --- #
# butchersUnits = int(input("Butcher's Pale Ale Barrels Units:   "))
# farriersUnits = int(input("Farriers' IPA Barrels Units:        "))
# gatehouseUnits = int(input("Gatehouse Brown Ale Barrels Units:  "))
#
# # -- Check how many spaces left in a Rack -- #
# # 1 Rack = 15 spaces
# checkRackSpaces = (butchersUnits + farriersUnits + gatehouseUnits) % 15
# surcharge = 0
#
# if checkRackSpaces > 0:
#     surcharge = checkRackSpaces * 2
#
# print(surcharge)
#
# # -- Check discount Butchers' Pale Ale-- #
# butchersBarrelPriceTotal = round(butchersUnits * 125.50, 2)
# butchersBarrelDiscount = round(math.floor(butchersUnits / 10) * 10 * 10, 2)
# butchersBarrelTotalAfterDiscount = round(butchersBarrelPriceTotal - butchersBarrelDiscount, 2)
#
# # -- Check discount Farriers' IPA-- #
# farriersBarrelPriceTotal = round(farriersUnits * 105.90, 2)
# farriersBarrelDiscount = round(math.floor(farriersUnits / 12) * 12 * 8.40, 2)
# farriersBarrelTotalAfterDiscount = round(farriersBarrelPriceTotal - farriersBarrelDiscount, 2)
#
# # -- Check discount Gatehouse Brown Ale-- #
# gatehouseBarrelPriceTotal = round(gatehouseUnits * 132.35, 2)
# gatehouseBarrelDiscount = round(math.floor(gatehouseUnits / 9) * 9 * 11.65, 2)
# gatehouseBarrelTotalAfterDiscount = round(gatehouseBarrelPriceTotal - gatehouseBarrelDiscount, 2)

# --- PRINT RECEIPT --- #
invoice = "WTA22212S"
date = "12-02-1998"
name = "JJ Odriscoll Superstore"
street = "4, Elderwood Park, Borrenmanna Road"
town = "Ballintemple"
county = "Cork"
print(f"{'':>50}{'Walled Town Ale'}")
print(f"{'':>70}{'Invoice No:':<20}{invoice}")
print(f"{'':>70}{'Date:':<20}{date}")
print("")
print(f"{'Company Name:':<15}{name}")
print(f"{'Address:':<15}{street}\n{'':<15}{town}\n{'':<15}{county}")
print("\nSales Details:\n")
butchersPaleAleName = "Butchers' Pale Ale:"
farriersIpaName = "Farriers' Ipa:"
gatehouseBrownAleName = "Gatehouse Brown Ale:"
print(f"{butchersPaleAleName:<50}{9:<40}{11}")
print(f"{farriersIpaName:<50}{9:<40}{12}")
print(f"{gatehouseBrownAleName:<50}{9:<40}{12}\n")
boldLine = "\u2501" * 18
print(boldLine.rjust(100))
print(f"{'':<70}{'Subtotal:':<20}{12}")

spaceRacks = 1
if spaceRacks > 0:
    print("\nSurcharge:")
    print(f"{'Rack spaces unused:':<50}{spaceRacks:<40}{'120'}")

discount = 1
if discount > 0:
    print("\nDiscount:")
    print(f"{butchersPaleAleName:<50}{discount}")
    print(f"{farriersIpaName:<50}{discount}")
    print(f"{gatehouseBrownAleName:<50}{discount}")
