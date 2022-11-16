import datetime

print("Welcome to Walled Town Ale Order Platform\n".center(100))
print("Please, complete the following fields:\n")

# --- User Name and Address Inputs--- #
companyName = input("Company Name:").strip()
companyPhoneNumber = input("Phone Number:").strip()
street = input("Street Address:")
town = input("Town/City:")
county = input("County:")
actualDate = datetime.datetime.today().strftime('%d-%m-%Y')
companyInvoiceNo = ("WTA" + companyPhoneNumber.lstrip("0")[0:2] + companyPhoneNumber[-2:] + companyName[-2]).upper()


