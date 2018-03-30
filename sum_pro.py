"""This class inp takes input from the user related to the bayesian belief networks and
stores it for future processing of creating sum-product graph"""
data = []
class inp:

    def __init__(self, var_name = None, dependencies = None, prob = None):
        self.var_name = var_name
        self.dependencies = dependencies
        self.prob = prob

class node:
    def __init__(self, dataval= None, type = None,children=[]):
        self.dataval = dataval
        self.type = type
        self.children = []

head = node(None)

def traverse(temp):
    if (temp.children == []):
        print temp.dataval.var_name
    else:
       # if temp.children.:
        for each in temp.children:
                traverse(each)

def createGraph():
    i=0
    for item in data:
        if(item.dependencies <> []):
            for each in item.dependencies:
                head.children.append(node(inp(each,[],-1),'V'))
            #Create a factor node for the above dependency nodes
            (head.children[-1]).children.append((node(inp("f"+str(i),[],1),'F')))
            (head.children[-1]).children.append((node(item,'V')))
            i+=1
    temp = head
    traverse(temp)

def main():
    print("Enter the Bayesian Belief Network with dependencies")
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
    createGraph()
if __name__ == "__main__": main()