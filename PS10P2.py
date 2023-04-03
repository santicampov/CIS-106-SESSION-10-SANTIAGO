#run
answer = str(input("Enter 'Yes' if you want to run this program, otherwise, enter 'No'"))

#function
def sqft(l,w,h):
  sqft=(2*l*w)+(2*l*h)+(2*w*h)
  return sqft

#process
while answer.lower() == "yes":
  l = int(input("Please enter the length."))
  w = int(input("Please enter the width"))
  h = int(input("Please enter the height" ))
  paint = (sqft(l,w,h))//50

  #output
  print(f"You need {paint} gallons to paint the room.")
  answer = str(input("Enter 'Yes' if you want to run this program, otherwise, enter 'No'"))

print("Thank you for using the program.")