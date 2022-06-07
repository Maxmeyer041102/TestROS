#!/usr/bin/env python
import random




class Agent4 :
    def __init__(self, valence_table):
        """ Creating our agent """
        self.valence_table = valence_table
        self._action = 0
        self.anticipated_outcome = None
        self.compteur_lignes = 0
        self.prediction0 = 0
        self.prediction1 = 0
        self.prediction2 = 0

    def action(self, outcome):
        """ tracing the previous cycle """
        if self._action is not None:
            print(str(self.compteur_lignes) + " " +
                  ("Action: " + str(self._action) +
                   ", Anticipation: " + str(self.anticipated_outcome) +
                   ", Outcome: " + str(outcome) +
                   ", Satisfaction: (anticipation: " + str(self.anticipated_outcome == outcome) +
                   ", valence: " + str(self.valence_table[self._action][outcome]) + ")"))

        """ Computing the next action to enact """
        self.compteur_lignes = self.compteur_lignes + 1


        if self.compteur_lignes <= 1 :
            self._action = 1

        elif self.compteur_lignes == 16:
            self._action = 2

        elif self.compteur_lignes == 34 :
            self._action = 1

        elif self.compteur_lignes == 55 :
            self._action = 0

        elif self.compteur_lignes == 57 :
            self._action = 2

        elif self.compteur_lignes == 72 :
            self._action = 1

        elif self.compteur_lignes == 86:
            self._action = 2

        elif self.compteur_lignes == 100 :
            self._action = None


        return self._action

