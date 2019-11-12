'''
Ex 2
Tom Goldenberg
Question 7
'''

class Agent:
    def __init__(self, opt_num, val_list):
        self.value_list = val_list
        # for _ in range(opt_num):
        #     self.va

    def value(self, option:int)->float:
        return self.value_list[option]
"""
 INPUT: the index of an option.
 OUTPUT: the value of the option to the agent.
"""
# def isParetoImprovement(agents:List[Agent], option1:int, option2:int)->bool:
def isParetoImprovement(agents, option1, option2):
    for agent in agents:
        if (option1 != option2):
            val1 = agent.value(option1)
            val2 = agent.value(option2)
            if (val1 < val2):
                return False
    return True


# def isParetoOptimal(agents:List[Agent], option:int, allOptions:List[int])->bool:
def isParetoOptimal(agents, option, allOptions):
    for option2 in allOptions:
        if (option != option2):
            if not (isParetoImprovement(agents, option, option2)):
                return False
    return True

ami = Agent(5, [1,2,3,4,5])
tami = Agent(5, [3,1,2,5,4])
rami = Agent(5, [3,5,5,1,1])

agents = []
agents.append(ami)
agents.append(tami)
agents.append(rami)

allopt = [0,1,2,3,4]

for _ in range(5):
    for __ in range(5):
        res = isParetoImprovement(agents, _, __)
        # print('option 1: {_}, option 2: {__}, is Pareto Improvment: {res}')
        # print('option 1: {}, option 2: {}, is Pareto Improvment: {}', _, __, res)
        print('option 1: {}, option 2: {}, is Pareto Improvment: {}'.format(_, __, res))

    res = isParetoOptimal(agents, _, allopt)
    print('option 1: {}, is Pareto Optimal: {}'.format(_, res))