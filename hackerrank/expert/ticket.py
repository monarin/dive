# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
destinationPrices = {}
destinationPassengers = []
for line in sys.stdin:
  cols = line.strip().split()
  if len(cols)==3:
    n,m,k = map(int, cols)
  elif len(cols)==2:
    destinationPrices[cols[0]]=float(cols[1])
  elif len(cols)==1:
    destinationPassengers.append(cols[0])
    
# Cost is calculated as * price if the previous passenger shares the same destination
# otherwise, * 0.8 price
passengerSaleWindows = [0] * n 
passengerCosts = [0] * n
prevPassengers = [[]] * m
nextSaleWindow = 1
for passenger, passengerCount in zip(destinationPassengers, range(n)):
  #go through each sale window and queue up if previous passenger share the same destination
  #if none, choose [] or one with the lowest order
  flagDone = False
  freeSaleWindow = []
  for prevPassenger, saleWindow in zip(prevPassengers, range(1,m+1)):
    if prevPassenger == passenger:
      passengerSaleWindows[passengerCount] = saleWindow
      passengerCosts[passengerCount] = 0.8 * destinationPrices[passenger]
      prevPassengers[saleWindow-1] = passenger + ''
      flagDone = True
      break
    if not freeSaleWindow and not prevPassenger: freeSaleWindow = saleWindow 
  if not flagDone:
    if freeSaleWindow:
      passengerSaleWindows[passengerCount] = freeSaleWindow
      prevPassengers[freeSaleWindow-1] = passenger + ''
    else:
      passengerSaleWindows[passengerCount] = nextSaleWindow
      prevPassengers[nextSaleWindow-1] = passenger + ''
      nextSaleWindow += 1
      if nextSaleWindow > m:
        nextSaleWindow = 1
    passengerCosts[passengerCount] = 1.0 * destinationPrices[passenger]
  print passenger, passengerSaleWindows[passengerCount], passengerCosts[passengerCount], prevPassengers

# Print output
print sum(passengerCosts)                      