# L-System package
import numpy as np
import logging


class Axiom(object):
    """ Дескриптор для определения аксиомы """
    def __init__():
        self.value = Null
    def __get__(self, obj, type):
        return self.value

    def __set__(self, obj, value):
        self.value = value

class Productions(object):
    """ Дескриптор для определения произведения """
    def __init__():
        self.value = Null
    def __get__(self, obj, type):
        return self.value

    def __set__(self, obj, value):
        self.value = value


class LSystem2D(object):
    axiom = Axiom()
    productions = Productions()
    def __init__(self, axiom, productions, iterations, angel):
        self.axiom = axiom
        self.productions = productions
        self.iterations = iterations
        self.grad = angel
        self.angel = self.__ang_to_rad(angel)
        self.__make_rule()
    
    def __repr__(self):
        string = "axiom: " + str(self.axiom) + '\n' +\
        "productions: " + str(self.productions) + '\n' +\
        "iterations: " + str(self.iterations) + '\n' +\
        "angel: " + str(self.grad) + '°'
        return string
        
    def __ang_to_rad(self, deg):
        return np.pi/180*deg
    
    def __make_rule(self):
        rule = self.axiom
        productions = self.productions.copy()
        productions['+'] = '+
'        productions['-'] = '-'
        productions['['] = '['
        productions[']'] = ']'
        for i in range(self.iterations):
            rule = ''.join([productions[s] for s in rule])
        self.rule = rule


if __name__ == "__main__":
    pass