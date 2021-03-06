"""
This code is run to show end product of using different systems to maximize gains using low risk- low reward and high risk-high reward stock. 

Author: Vikram Melchizedec

"""

import random
import sys
import csv
import matplotlib.pyplot as plt

# Input: Amount(Monetary) , preferred system, Iterations amount
# Output: Ending amount for x amount of trials
def main():
    print("Hello, welcome to the Stock simulator")
    Capital = float(input("Pleae enter your starting capital $$$: "))
    Iterations = 50
    Scenarios = float(input("How many scenarios should you run? "))
    print("Starting capital $$$ ",  Capital,"$")
    print("Iterations: ", Iterations)
    print("# of runs: ", Scenarios )
    #LowValues = loloValue()
    i = 0
    x = list()
    while i < Iterations:
        x.append(i)
        i = i+1
    j = 0
    ReturnsList = List()
    while j < Scenarios:	
        HighValues = hihiValue(Iterations)
        ReturnsList.append(MelSystemOne(Capital,Scenarios, Iterations,HighValues))
        plt.plot(x,HighValues)
        plt.show()
        print(*HighValues, sep = "\n")

# low risk low reward simulator for all iterations
def loloValue():
	Value = 1
	LowValue = list.append(Value)
	return LowValue

# high risk high reward simulator for all iterations
def hihiValue(n):
	Value = 1
	HighValue = list()
	HighValue.append(Value)
	i = 1
	multiplier = [50,66,80,100,100, 125,150,200]
	#While loop to generate stock values for all iterations
	while (i < n):
	    randMult = random.choice(multiplier)
	    randMult = randMult  / 100
	    Value = Value * randMult
	    HighValue.append(Value)
	    i = i + 1
	    #Safeguards from Extremes... Coming soon

	
	return HighValue

def AllOnLow():
	return print("function run")
#returns value of investment/capital after x amount of iterations if user let it ride. 
def AllOnHigh():
	return print("function run")

#returns value of investmennt/capital if investor used the Mel system of investing.
def MelSystemOne(Capital,TimesRun, Iterations, HighValues ):
	Returns = capital
    
	return Returns

def StockBroker(amountIN, Iteration ):
	return Value

if __name__ == "__main__":
    main()