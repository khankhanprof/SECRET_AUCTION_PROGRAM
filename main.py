from replit import clear
from art import logo
print(logo)
#HINT: You can call clear() to clear the output in the console.
def final(new_dict):
  max=0
  for i in new_dict:
    amt=new_dict[i]
    
    if amt>max:
      max=amt
      winner=i
  print(f"the winner is {winner} with the highest bid of {max}")    
  
def auction(new_dict):
  name=input("enter name:\t")
  bid=int(input("enter bid amount: $\t"))
  option=input("type \"yes\" if next bidder is available else type \"no\" ")
  
  new_dict[name]=bid
  if option=="yes":
    clear()
    auction(new_dict)
  return new_dict


new_dict={}
auction(new_dict)
final(new_dict)






