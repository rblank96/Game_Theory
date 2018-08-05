# Prize Model

Prize model is structured as follows. There is a certain amount of money to be won: the value. There is a step to which each player can bet on increments: the step. The winning bet gets the value minus whatever they bet. If the winning bet is a tie, those members split the value equally. I wrote a program to find the Game Theory equilibria in any three person prize model, with any value and any chose step.

## Usage

#test cases

```
print("equilibriums for value 30, step 15: " + str(prize_model(30, 15)))
print("equilibriums for value 100, step 25: " + str(prize_model(100, 25)))
print("equilibriums for value 100, step 50: " + str(prize_model(100, 50)))
print("equilibriums for value 3, step 1: " + str(prize_model(3, 1)))
```
