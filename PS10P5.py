summ=0
suma=0

#runprogram
response=str(input("Enter 'Yes' if you want to run this program, otherwise, enter 'No'"))

#function
def avalue(mv,county):
  if county.lower() in "cook":
    avp = 0.9
  elif county.lower() in "dupage":
    avp = 0.8
  elif county.lower() in "mchenry":
    avp = 0.75
  elif county.lower() in "kane":
    avp = 0.6
  else:
    avp = 0.7
  avalue = avp*mv
  return avalue

#process
while response.lower() in "yes":
  county = str(input("Please enter the county in which the house is located. "))
  mv = float(input("Please enter the market value of the house. "))
  avalue = avalue(mv,county)
  print(f"The assessed value of the home is ${avalue:.2f}.")
  response = str(input("Enter 'Yes' if you want to run this program, otherwise, enter 'No'"))

#output
summv = summ + mv
suma = suma + avalue
print(f"The sum is ${summ:.2f} and the sum of all the assessed values is ${suma:.2f}.")