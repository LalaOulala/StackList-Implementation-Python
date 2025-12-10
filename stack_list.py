#!/usr/bin/env python3
# -*- coding: utf-8 -*-
        
from sys import setswitchinterval


class Cell():
    """ Creates an instance of class Cell
    input   -- self : instance of class Cell
    """
    def __init__(self):
        self.value = object
        self.next = None
        
    def __str__(self):
        """ Returns a string representing Cell self
        input   -- self : instance of class Cell
        output  -- string
        """
        result = str(self.value) + ', next:'
        if self.next == None:
            result += 'None'
        else:
            result += str(self.next.value)
        return '{ ' + result + ' }'

      
class StackList:
           
    """
    The class StackList allows to represent a stack implemented by a linked list
    """
    def __init__(self, capacity=100):

        """ Creates an instance of StackList
        input    -- self
        output   -- self is an empty stack
        """
        self.mtop = None            # element at the top of the stack
        self.size = 0               # size of 
        self.capacity = capacity    # size MAX of the stack = 100 by default
        
    def __str__(self):
        """ Returns a string representing the StackList self
        input   -- self : instance of class StackList
        output  -- string
        """
        affichage = "\n"
        current = self.mtop
        while current is not None:
            affichage += "| " + str(current.value) + " |\n"
            current = current.next
        affichage += "------"
        return affichage

            
    def empty_stack(self):
        """ Returns True if the stack self is empty and False otherwise
        input   -- self : instance of class StackList
        output  -- bool
        """
        return self.mtop == None

    def full_stack(self):
        """ Return True if the stack self is full and False otherwise
        In this version implemented by a list, we don't give the maximum size of the stack
        input   -- self : instance of class StackList
        output  -- bool
        """
        #print(f"dans full_stack - capacity : {self.capacity}")
        #print(f"dans full_stack - size : {self.size}")
        return self.capacity == self.size
    
    def size_stack(self):
        """ Returns the size of the stack
        input   -- self : instance of class StackList
        output  -- size, the size of self
        """
        return self.size

    def push(self, v):
        """ Stacks an element at the top of StackList
        The stack is modified by adding the Cell of value v at the top of the stack
        input    -- self: instance of class StackList
                 -- v : object, value of the Cell to push
                    pre-cond: self is not full
        output   -- self which has been modified
                 post-cond: the size of the stack is incremented
        """
        assert self.full_stack() == False, "La pile est pleine."
        new_cell = Cell()
        new_cell.value = v
        if self.mtop == None: # Cas 1 : La pile est vide
            new_cell.next = None
        else: # Cas 2 : La pile n'est pas vide
            new_cell.next = self.mtop
        # Dans tous les cas
        self.mtop = new_cell
        self.size += 1

    def top(self):
        """ Returns the element at the top of the stack self
        input   -- self : instance of class StackList
        output  -- t: Cell element 
        """
        assert self.empty_stack() == False, "La pile est vide." 
        return self.mtop
        
    def top_value(self):
        """ Returns the value of the element at the top of the stack self
        input   -- self : instance of class StackList
        output  -- s: object (type of value, attribute of class Cell) 
        """
        assert self.empty_stack() == False, "La pile est vide." 
        return self.mtop.value

    def pop(self):
        """ Unstacks the element at the top of the stack self
        input    -- self : instance of class PileList
                    pre-cond: self is not empty
        output   -- self in which the element at the top of the stack has been unstacked
                  post-cond: the size of the stack is decremented
        """
        assert self.empty_stack() == False, "La pile est vide." 
        if self.mtop.next == None: # La pile est de taille 1 (un élément)
            self.mtop = None
            self.size -= 1
        else: # La pile est au moins de taille 2 (deux éléments)
            self.mtop = self.mtop.next
            self.size -= 1


class EvalExp():
    def __init__(self):
        """ Create an instance of EvalExp
        """
        self.exp = ""
    
    def evaluate(self, exp):
        """ Evalue la valeur d'une expression arithmétique
        input   -- self : instance de la classe EvalExp
                -- exp : chaine de caractère contenant l'expression a évaluer
        output  -- result : valeur réelle de l'expression calculée
        """
        maPile = StackList()
        exp_list = exp.split(" ") # transforme la chaine exp en liste de tous les éléments
        for element in exp_list:
            if element in ["+", "-", "*", "/"]:
                operande1 = maPile.top_value() # on extrait la valeur de la première cellule de la pile
                maPile.pop() # on dépile le premier élément de la pile
                operande2 = maPile.top_value()
                maPile.pop()
                if element == "+": # disjonction de cas pour les différents opérateurs
                    maPile.push(float(operande1) + float(operande2))
                elif element == "-":
                    maPile.push(float(operande1) - float(operande2))
                elif element == "*":
                    maPile.push(float(operande1) * float(operande2))
                elif element == "/":
                    maPile.push(float(operande1) / float(operande2))
            else: # si l'élément n'est pas un opérateur, alors 
                maPile.push(element)
        print(maPile)
        return maPile.top_value()


# EXERCICE 1

#Test pile representee par une liste
if __name__ == "__main__":
    print("Hello StackList !")