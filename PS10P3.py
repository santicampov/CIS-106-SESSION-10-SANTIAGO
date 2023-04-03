summsrp = 0
sumtotal=0

#run
response = str(input("Enter 'Yes' if you want to run this program, otherwise, enter 'No'"))

#function
def price(msrp,make,model,evcode):
  if make.lower() in "honda" and model.lower() in "accord":
    poff = 0.1
  elif make.lower() in "toyota" and model.lower() in "rav4":
    poff = 0.15
  elif evcode.lower() in "yes":
    poff = 0.3
  else:
    poff=0.05
  discount=poff*msrp
  newmsrp = msrp - discount
  msrptax = newmsrp*1.07
  return float(msrptax)

#input
while response.lower() in "yes":
  make = str(input("Enter the make of the car "))
  model = str(input("Enter the model of the car "))
  evcode = str(input("Is the car electric? "))
  msrp = float(input("Enter the msrp of the vehicle "))
  summsrp = summsrp + msrp
  float(summsrp)
  msrptax=price(msrp,make,model,evcode)
  float(msrptax)
  sumtotal = sumtotal+msrptax
  print(f"The final MSRP is ${msrptax:.2f}.")
  response = str(input("Enter 'Yes' if you want to run this program, otherwise, enter 'No'"))

#output
print(f"The total of MSRP ${summsrp:.2f} and the total of MSRP after discount and tax is ${sumtotal:.2f}.")