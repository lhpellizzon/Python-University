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
checkRackSpaces = (butchersUnits + farriersUnits + gatehouseUnits) % 15
surcharge = 0

if checkRackSpaces > 0:
    surcharge = checkRackSpaces * 2

print(surcharge)

# -- Check discount Butchers' Pale Ale-- #
butchersBarrelPriceTotal = round(butchersUnits * 125.50, 2)
butchersBarrelDiscount = round(math.floor(butchersUnits / 10) * 10 * 10, 2)
butchersBarrelTotalAfterDiscount = round(butchersBarrelPriceTotal - butchersBarrelDiscount, 2)

# -- Check discount Farriers' IPA-- #
farriersBarrelPriceTotal = round(farriersUnits * 105.90, 2)
farriersBarrelDiscount = round(math.floor(farriersUnits / 12) * 12 * 8.40, 2)
farriersBarrelTotalAfterDiscount = round(farriersBarrelPriceTotal - farriersBarrelDiscount, 2)

# # -- Check discount Gatehouse Brown Ale-- #
gatehouseBarrelPriceTotal = round(gatehouseUnits * 132.35, 2)
gatehouseBarrelDiscount = round(math.floor(gatehouseUnits / 9) * 9 * 11.65, 2)
gatehouseBarrelTotalAfterDiscount = round(gatehouseBarrelPriceTotal - gatehouseBarrelDiscount, 2)

