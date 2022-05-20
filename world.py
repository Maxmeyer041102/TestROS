#!/usr/bin/env python
# Olivier Georgeon, 2021.
# This code is used to teach Developmental AI.
# from turtlesim_enacter import TurtleSimEnacter # requires ROS
import random

from turtlepy_enacter import TurtlePyEnacter
# from Agent5 import Agent5
# from OsoyooCarEnacter import OsoyooCarEnacter


class Agent:
    def __init__(self, _hedonist_table):
        """ Creating our agent """
        self.hedonist_table = _hedonist_table
        self._action = 0
        self.anticipated_outcome = None
        self.CmtrVariables = 0
        self.previous_outcome = None
        self.compteur_lignes = 0

    def action(self, outcome):
        """ tracing the previous cycle """
        #self._action = 0
        if self._action is not None:
            print(str(self.compteur_lignes) + " "
                  "Action: " + str(self._action) +
                  #", Anticipation: " + str(self.anticipated_outcome) +
                  ", Outcome: " + str(outcome) +
                  #", Satisfaction: (anticipation: " + str(self.anticipated_outcome == outcome) +
                  #", valence: " + str(self.hedonist_table[self._action][outcome]) + ")" +
                  ", compteur de la variable: " + str(self.CmtrVariables))



        self.compteur_lignes = self.compteur_lignes +1



        if self.CmtrVariables >= 3:
            self.CmtrVariables = 0
            if self._action == 1:
                self._action = 0
            else:
                self._action = 1

        if self.previous_outcome == outcome:
            self.CmtrVariables = self.CmtrVariables +1

        self.previous_outcome = outcome
                
        """ Computing the next action to enact """
        # TODO: Implement the agent's decision mechanism
        #self._action = 0
        # TODO: Implement the agent's anticipation mechanism
        self.anticipated_outcome = 0
        return self._action


class Environment1:
    """ In Environment 1, action 0 yields outcome 0, action 1 yields outcome 1 """
    def outcome(self, action):
        # return int(input("entre 0 1 ou 2"))
        if action == 0:
            return 0
        else:
            return 1


class Environment2:
    """ In Environment 2, action 0 yields outcome 1, action 1 yields outcome 0 """
    def outcome(self, action):
        if action == 0:
            return 1
        else:
            return 0


class Environment3:
    """ Environment 3 yields outcome 1 only when the agent alternates actions 0 and 1 """
    def __init__(self):
        """ Initializing Environment3 """
        self.previous_action = 0

    def outcome(self, action):
        _outcome = 1
        if action == self.previous_action:
            _outcome = 0
        self.previous_action = action
        return _outcome

class Environment4 :
    def outcome (self, action):
        _outcome = random.randint(0,1)



        return _outcome
# TODO Define the hedonist valance of interactions (action, outcome)
hedonist_table = [[-1, 1], [-1, 1]]
# TODO Choose an agent
a = Agent(hedonist_table)
# a = Agent5(hedonist_table)
# TODO Choose an environment
e = Environment1()
# e = Environment2()
# e = Environment3()
# e = Environment4()
# e = TurtleSimEnacter()
# e = TurtlePyEnacter()
# e = OsoyooCarEnacter()

if __name__ == '__main__':
    """ The main loop controlling the interaction of the agent with the environment """
    outcome = 0
    for i in range(41):
        action = a.action(outcome)
        outcome = e.outcome(action)


