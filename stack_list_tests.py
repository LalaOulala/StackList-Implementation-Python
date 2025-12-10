#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import stack_list as stl

#%% Test des méthodes __str__, empty_stack, push, size_stack, full_stack
p1 = stl.StackList(100)
print("p1.empty_stack()", p1.empty_stack())
#print(f"test de full_stack : {p1.full_stack()}")
#assert p1.full_stack == False, "La condition est fausse"
p1.push(1)
p1.push(2)
p1.push(3)
p1.push(4)
p1.push(5)
print("p1:", p1)
print("p1.size_stack() : ", p1.size_stack())

# %% Tests des méthodes top_value, top
print("""
- - - - - Nouvelle pile ! - - - - - 
""")
p2 = stl.StackList(100)
p2.push(1)
p2.push(2)
p2.push(3)
p2.push(4)
p2.push(5)
print(p2)
print("p2.top_value():", p2.top_value())
print("p2.top():", p2.top())

# %% Tests de la méthode pop
p3 = stl.StackList(100)
p3.push(1)
p3.push(2)
p3.push(3)
p3.push(4)
p3.push(5)
print("p3:", p3)
p3.pop()
print("p3.pop()", p3)

# %% EXERCICE 2
print("""
exercice 2 evaluate
""")
eval1 = stl.EvalExp()
eval1.evaluate("1 2 * 3 +")