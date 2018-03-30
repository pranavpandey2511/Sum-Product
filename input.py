"""This class inp takes input from the user related to the bayesian belief networks and
stores it for future processing of creating sum-product graph"""
data = []
class inp:

    def __init__(self, var_name = None, dependencies = None, prob = None):
        self.var_name = var_name
        self.dependencies = dependencies
        self.prob = prob

def main():
    print("Enter the vayesian Belief Network with dependencies")
    print("Enter the total number of variables involved")
    num = input()
    for token in range(num):
        print("Enter the variable name")
        name = raw_input()
        print("Enter the dependencies seperated by space")
        dpndnc = raw_input().split(" ")
        print("Enter the probability of the variable")
        prob = float(raw_input())
        data.append(inp(name,dpndnc, prob))
    print("The dependencies entered are as follows")
    for each in data:
        print each.var_name
        print each.dependencies
        print each.prob
if __name__ == "__main__": main()