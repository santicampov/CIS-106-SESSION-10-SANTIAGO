#input
response = str(input("Enter 'Yes' if you want to run this program, otherwise, enter 'No'"))

#function
def comppercent(month,sales):
  if month.lower() in ["jan","feb","mar"]:
    percent = 0.1
  elif month.lower() in ["apr","may","june"]:
    percent = 0.15
  elif month.lower() in ["jul","aug","sept"]:
    percent = 0.2
  elif month.lower() in ["oct","nov","dec"]:
    percent = 0.25
  else:
    print("Please enter a month abreviation" )
    exit()
  
  nmsales=(percent+1)*sales
  return nmsales

  #process
while response.lower() == "yes":
  lname = str(input("Please enter your last name. "))
  month = str(input("Please enter the month."))
  sales = float(input("Please enter the current sales."))
  nmsales = comppercent(month,sales)

  #output  
  print(f"For the month of {month} the forecasted sales are ${nmsales:.2f}.")
  response = str(input("Enter 'Yes' if you want to run this program, otherwise, enter 'No'"))

print("Thank you for using the program.")