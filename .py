
import sys

#Collecting input and setting days/weeks rented variables 
rentalCode = input("(B)udget, (D)aily, or (W)eekly rental?\n")
rentalPeriod = 0

#allocating input message for rentalPeriod depending on rentalCode
if rentalCode == 'B' or rentalCode == 'D':
  rentalPeriod = int(input("Number of Days Rented:\n"))
else:
  rentalPeriod = int(input("Number of Weeks Rented:\n"))





#Taking rental Period and budget_charge to find baseCharge
budget_charge = 40.00
daily_charge = 60.00
weekly_charge = 190.00

if rentalCode == 'B':
  baseCharge = rentalPeriod * budget_charge
elif rentalCode == 'D':
  baseCharge = rentalPeriod * daily_charge
else:
  baseCharge = rentalPeriod * weekly_charge
  



odoStart = int(input("Starting Odometer Reading:\n"))
odoEnd = int(input("Ending Odometer Reading:\n"))
totalMiles = odoEnd - odoStart



#Calculating Mile Charge

if rentalCode == 'B':
  mileCharge = totalMiles * 0.25

# Added rentalPeriod of 1 to test following code  
averageDayMiles = totalMiles / rentalPeriod
averageWeekMiles = totalMiles/ rentalPeriod
extraMiles = averageDayMiles - 100
mileCharge = totalMiles * .25

# If average day miles is under 100, no charge. After 100, charge $0.25 per additional mile.
if rentalCode == 'D':
  if averageDayMiles <= 100:
    extraMiles = 0
  else: 
    extramiles = averageDayMiles - 100
    mileCharge = extraMiles * .25
    
# If average week miles exceed 900, charge and additional $100 per week rented.

if rentalCode == 'W':
  if averageWeekMiles <= 900:
    mileCharge = 0
  else:
    mileCharge = rentalPeriod * 100
    




#Rental Summary *Note the formatting on 'Amount Due' to convert to dollars, cents

amtDue = baseCharge + mileCharge


print('Rental Summary')
print('Rental Code:' + rentalCode)
print('Rental Period: ' + str(rentalPeriod))
print('Starting Odometer:' + str(odoStart))
print('Ending Odometer: ' + str(odoEnd))
print('Miles Driven: ' + str(totalMiles))
print('Amount Due: ' + '${:,.2f}'.format(amtDue))
