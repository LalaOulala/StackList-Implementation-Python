# TP8 - Piles (StackList en Python)

Cours/TP de structures de donnees (2024-2025) sur l'implementation d'une pile (LIFO) avec une liste chainee et l'evaluation d'expressions arithmetiques en notation postfixee (polonaise inverse). Ce README sert de fiche de revision pour rejouer le TP et retrouver les notions clefs du PDF `TP8-Piles.pdf`.

## Objectifs du TP
- Comprendre le type abstrait pile : insertion/retrait en tete uniquement (Last-In-First-Out).
- Implementer une pile avec une liste chainee simple (`StackList`).
- Utiliser la pile pour evaluer des expressions arithmetiques postfixees (sans parentheses).
- Optionnel (ex. 3 du PDF) : re-implementer la pile avec un tableau et gerer l'accroissement de capacite.

## Structure du projet
- `stack_list.py` : definition de `Cell`, `StackList` (pile chainee) et `EvalExp` (evaluation postfixee).
- `stack_list_tests.py` : petits essais interactifs des operations de pile et de l'evaluation.
- `TP8-Piles.pdf` : sujet complet du TP.
- `.gitignore` : ignore la venv, les caches et fichiers temporaires.

## Rappels sur les piles
- Principe : LIFO (dernier entre, premier sorti).
- Operations de base (toutes en O(1) avec la liste chainee) :
  - `push(v)` : empile `v`.
  - `pop()` : depile le sommet.
  - `top()` : renvoie la cellule en sommet (utilise `top().value` pour la valeur).
  - `top_value()` : renvoie directement la valeur du sommet.
  - `empty_stack()` / `full_stack()` : tests d'etat (la capacite est configurable, 100 par defaut).
  - `size_stack()` : taille courante.
- Implementation : chaque `Cell` porte `value` et `next`. Le sommet `mtop` pointe vers la premiere cellule; empiler/deempiler revient a deplacer ce pointeur.

### Pourquoi une pile ?
- Gestion naturelle d'un historique (undo/redo).
- Parcours de graphes/arbres sans recursion.
- Evaluation d'expressions postfixees (cf. ci-dessous).

## Notation postfixee (polonaise inverse)
On ecrit d'abord les operandes, puis l'operateur. Avantages : pas de parentheses, seule l'ordre des operations compte.

Exemples du sujet :
- `2 3 +` -> 5
- `1 3 + 2 *` -> (1 + 3) * 2 = 8
- `4 3 * 2 5 + +` -> (4 * 3) + (2 + 5) = 19

Algorithme avec une pile :
1. Parcourir les tokens (ici separes par des espaces).
2. Si token = nombre, l'empiler.
3. Si token = operateur `+, -, *, /`, depiler deux operandes (op2 puis op1), appliquer l'operation, empiler le resultat.
4. En fin de parcours, le sommet contient le resultat.

Dans `EvalExp.evaluate`, on transforme l'expression avec `exp.split(" ")`, puis on applique l'algorithme ci-dessus en utilisant la pile chainee.

## S'en servir rapidement

### Empiler/depiler
```bash
python3 -q
>>> from stack_list import StackList
>>> p = StackList(capacity=10)
>>> p.push(1); p.push(2); p.push(3)
>>> print(p)
| 3 |
| 2 |
| 1 |
------
>>> p.top_value()
3
>>> p.pop(); p.top_value()
2
```

### Evaluation postfixee
```bash
python3 -q
>>> from stack_list import EvalExp
>>> ev = EvalExp()
>>> ev.evaluate("2 10 * 10 2 / - 3 +")
```
Dans le code fourni, `evaluate` empile le resultat sur une pile locale et ne le renvoie pas. Pour exploiter la valeur, modifiez la methode pour retourner le sommet (ex. `return maPile.top_value()`) ou exposez le resultat a travers un attribut.

## Lancer les tests fournis
Un petit script de test/illustration est fourni :
```bash
python3 stack_list_tests.py
```
Il construit plusieurs piles, affiche l'etat du sommet, puis joue un exemple d'evaluation postfixee (`"1 2 * 3 +"`).

## Aller plus loin (ex. 3 du PDF)
- Reprendre la meme interface mais avec un tableau de taille MAX.
- Gerer l'agrandissement du tableau quand la pile est pleine.
- Comparer complexites et contraintes par rapport a la version chainee.

Bonnes revisions ! Rouvrez `TP8-Piles.pdf` si vous voulez le detail des consignes et des exemples traces pas a pas.
