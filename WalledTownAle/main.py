import datetime
import math

print("Welcome to Walled Town Ale Order Platform\n".center(100))
print("Please, complete the following fields for delivery:\n")

# --- User Name and Address Inputs--- #
companyName = input("Company Name:    ").strip()
companyPhoneNumber = input("Phone Number:    ").strip()
address1 = input("Address Line 1:  ")
address2 = input("Address Line 2:  ")
address3 = input("Address Line 3:  ")
actualDate = datetime.datetime.today().strftime('%d-%m-%Y')
companyInvoiceNo = ("WTA" + companyPhoneNumber.lstrip("0")[0:2] + companyPhoneNumber[-2:] + companyName[-2]).upper()

print("\nPlease, complete the following fields to make your order:\n")
# --- User Barrels Order --- #
butchersUnits = int(input("Butcher's Pale Ale Barrels Units:    "))
farriersUnits = int(input("Farriers' IPA Barrels Units:         "))
gatehouseUnits = int(input("Gatehouse Brown Ale Barrels Units:   "))

# -- Check how many spaces left in a Rack -- #
# 1 Rack = 15 spaces
checkRackSpaces = 15 - ((butchersUnits + farriersUnits + gatehouseUnits) % 15)
surcharge = 0

if checkRackSpaces < 15:
    surcharge = checkRackSpaces * 2

# -- Check discount Butchers' Pale Ale-- #
butchersBarrelPriceTotal = round(butchersUnits * 125.50, 2)
butchersBarrelUnitsDiscount = math.floor(butchersUnits / 10)
butchersBarrelDiscountPrice = round(butchersBarrelUnitsDiscount * 10, 2)

# -- Check discount Farriers' IPA-- #
farriersBarrelPriceTotal = round(farriersUnits * 105.90, 2)
farriersBarrelUnitsDiscount = math.floor(farriersUnits / 12)
farriersBarrelDiscountPrice = round(farriersBarrelUnitsDiscount * 8.40, 2)

# -- Check discount Gatehouse Brown Ale-- #
gatehouseBarrelPriceTotal = round(gatehouseUnits * 132.35, 2)
gatehouseBarrelUnitsDiscount = math.floor(gatehouseUnits / 9)
gatehouseBarrelDiscountPrice = round(gatehouseBarrelUnitsDiscount * 11.65, 2)

subtotal = round(butchersBarrelPriceTotal + farriersBarrelPriceTotal + gatehouseBarrelPriceTotal, 2)
totalDiscount = round(butchersBarrelDiscountPrice + farriersBarrelDiscountPrice + gatehouseBarrelDiscountPrice, 2)

# --- PRINT RECEIPT --- #
boldLine = "\u2501" * 18
butchersPaleAleName = "Butchers' Pale Ale:"
farriersIpaName = "Farriers' Ipa:"
gatehouseBrownAleName = "Gatehouse Brown Ale:"

# --- Receipt Title --- #
print(f"{'':>50}{'Walled Town Ale'}")

# --- Invoice No and Date --- #
print(f"{'':>70}{'Invoice No:':<20}{companyInvoiceNo}")
print(f"{'':>70}{'Date:':<20}{actualDate}\n")

# --- Company Name & Address --- #
print(f"{'Company Name:':<20}{companyName}")
print(f"{'Address:':<20}{address1}\n{'':<20}{address2}\n{'':<20}{address3}")

# --- Sales Details --- #
# --- Formatting the prices (numbers) to Euro currency --- #
butcherTotal = "€{:,.2f}".format(butchersBarrelPriceTotal)
farriersTotal = "€{:,.2f}".format(farriersBarrelPriceTotal)
gatehouseTotal = "€{:,.2f}".format(gatehouseBarrelPriceTotal)
subtotalCharge = "€{:,.2f}".format(subtotal)

# --- Each Barrel / Each Barrel Units / Each Barrel Full Price --- #
print("\nSales Details:\n")
print(f"{butchersPaleAleName}{butchersUnits:>36}{butcherTotal:>45}")
print(f"{farriersIpaName}{farriersUnits:>41}{farriersTotal:>45}")
print(f"{gatehouseBrownAleName}{gatehouseUnits:>35}{gatehouseTotal:>45}\n")
print(boldLine.rjust(100))
print(f"{'':<70}{'Subtotal:'}{subtotalCharge:>21}")

# --- Surcharge --- #
# --- Print Space Racks Unused if there is some / Surcharge Price --- #
if checkRackSpaces < 15:
    surchargePrice = "€{:,.2f}".format(surcharge)
    print("\nSurcharge:")
    print(f"{'Rack spaces unused:'}{checkRackSpaces:>36}{surchargePrice:>45}")

# --- Barrels Discount --- #
# --- Display Each Barrel Unit For Total Discount / Display Discount Price Per Barrel Type  --- #
if totalDiscount > 0:
    print("\nDiscount:")

if butchersBarrelDiscountPrice > 0:
    butchersBarrelDiscountPriceTotal = "€{:,.2f}".format(butchersBarrelDiscountPrice)
    print(f"{butchersPaleAleName}{butchersBarrelUnitsDiscount:>36}{butchersBarrelDiscountPriceTotal:>45}")

if farriersBarrelDiscountPrice > 0:
    farriersBarrelDiscountPriceTotal = "€{:,.2f}".format(farriersBarrelDiscountPrice)
    print(f"{farriersIpaName}{farriersBarrelUnitsDiscount:>41}{farriersBarrelDiscountPriceTotal:>45}")

if gatehouseBarrelDiscountPrice > 0:
    gatehouseBarrelDiscountPriceTotal = "€{:,.2f}".format(gatehouseBarrelDiscountPrice)
    print(f"{gatehouseBrownAleName}{gatehouseBarrelUnitsDiscount:>35}{gatehouseBarrelDiscountPriceTotal:>45}")

# --- Total --- #
print(boldLine.rjust(100))
# --- Formatting the total order price to Euro currency --- #
orderTotal = "€{:,.2f}".format((subtotal - totalDiscount + surcharge))
print(f"{'':<70}{'Total:'}{orderTotal:>24}")
