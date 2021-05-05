# game-of-life

An implementation of John Conway's [Game of Life](https://en.wikipedia.org/wiki/Conway's_Game_of_Life), which provided me a good opportunity to learn to use classes in Python 3.

## How to use

It's best to run game-of-life.py in interactive mode. If your shell is set up like mine, the command will be something like:

`python3 -i game-of-life.py`

Let's set up a gameboard and start playing!

```
>>> # start a new game board, with dimensions 12 by 8
>>> my_gameboard = Board(12, 8)
>>> # let's see how it looks!
>>> my_gameboard 

 - - - - - - - - - - - -
 - - - - - - - - - - - -
 - - - - - - - - - - - -
 - - - - - - - - - - - -
 - - - - - - - - - - - -
 - - - - - - - - - - - -
 - - - - - - - - - - - -
 - - - - - - - - - - - -

>>> # switch individual cells from dead to alive and back using .toggle()
>>> my_gameboard.toggle((2, 2), (2, 3), (3, 3), (4, 2), (3, 4))
>>> my_gameboard

 - - - - - - - - - - - -
 - - - - - - - - - - - -
 - - O O - - - - - - - -
 - - - O O - - - - - - -
 - - O - - - - - - - - -
 - - - - - - - - - - - -
 - - - - - - - - - - - -
 - - - - - - - - - - - -

>>> # simulate one generation using .step()
>>> my_gameboard.step()

 - - - - - - - - - - - -
 - - - - - - - - - - - -
 - - O O O - - - - - - -
 - - - - O - - - - - - -
 - - - O - - - - - - - -
 - - - - - - - - - - - -
 - - - - - - - - - - - -
 - - - - - - - - - - - -

>>> # clear the board using .reset()
>>> my_gameboard.reset()
>>> my_gameboard

 - - - - - - - - - - - -
 - - - - - - - - - - - -
 - - - - - - - - - - - -
 - - - - - - - - - - - -
 - - - - - - - - - - - -
 - - - - - - - - - - - -
 - - - - - - - - - - - -
 - - - - - - - - - - - -

>>>  # you can generate a random starting position using .soup() . Here, each cell has a 30 percent chance of being alive.
>>> my_gameboard.soup(0.3)
>>> my_gameboard

 - - - O - O - O O - - -
 - - - - - O O - - O O -
 O - - - - O - - O - O -
 - - - O - - - - - - O -
 - O - - - O - - - - - O
 - O - O O - - O O O - -
 - - - - O - O O - - - -
 O - - - - - O - O - O -

>>> # finally, simulate multiple generations using .steps()
>>> my_gameboard.steps(3)
Generation 1:

 - - - - O O - O O O - -
 - - - - - O - - - - O -
 - - - - O O O - - - O O
 - - - - O - - - - O O O
 - - - O - - - - O O O -
 - - O O O - - O O - - -
 - - - O O - O - - - - -
 - - - - - O O - - - - -

Generation 2:

 - - - - O O O - O O - -
 - - - - - - - O O - O O
 - - - - O - O - - - - -
 - - - O O - - - O - - -
 - - O - - - - O - - - O
 - - O - - O - O O - - -
 - - O - - - O - - - - -
 - - - - O O O - - - - -

Generation 3:

 - - - - - O O - O O O -
 - - - - O - - - O - O -
 - - - O O O - - O O - -
 - - - O O O - O - - - -
 - - O - O - O O - - - -
 - O O O - - - O O - - -
 - - - O O - - - - - - -
 - - - - - O O - - - - -

>>> 


```

