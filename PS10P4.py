sum=0
#runprogram
response=str(input("Enter 'Yes' if you want to run this program, otherwise, enter 'No'"))

#function
def ticketprice(miles):
  if miles >=30:
    tprice=12
  elif miles>=20:
    tprice=10
  elif miles>=10:
    tprice=8
  else:
    tprice=5
  return tprice

#input
while response.lower() in "yes":
  name = str(input("Please enter your last name. "))
  miles = int(input("Please enter the distance in miles. "))
  tprice=ticketprice(miles)
  sum=sum+tprice
  #output
  print(f"The train ticket price is ${tprice:.2f} to get to Chicago.")
  response= str(input("Enter 'Yes' if you want to run this program, otherwise, enter 'No'"))

print(f"The sum of all train tickets is ${sum:.2f}.")