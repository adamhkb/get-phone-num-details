import phonenumbers
from phonenumbers import carrier, geocoder, timezone

mobileNo = input("Enter Mobile Number with Country Code: ")
mobileNo = phonenumbers.parse(mobileNo)

# Get Timezone of the phone number
print(timezone.time_zones_for_number(mobileNo))

# Get carrier of the phone number
print(carrier.name_for_number(mobileNo, "en"))

# Getting region information
print(geocoder.description_for_number(mobileNo, "en"))

# Validating a phone number
print("Valid Mobile Number: ", phonenumbers.is_valid_number(mobileNo))

# Checking possibility of the phone number
print("Checking possibility of phone number: ", phonenumbers.is_possible_number(mobileNo))