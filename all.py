'''  
Probability Bag

You have been tasked with creating a lab that demonstrates the basics of probability by simulating a bag filled with colored balls. The bag is represented using a dictionary called "bag", where the key represents the color of the ball and the value represents the no of balls. The skeleton code has been made for you, do not add or remove any functions. Complete the following functions -

fillBag - A function that packs it's arguments into a global dictionary "bag".
totalBalls - returns the total no of balls in the bucket
probOf - takes a color (string) as argument and returns probability of drawing the selected ball. Assume total balls are not zero and the color given is a valid key.
probAll - returns a dictionary of all colors and their corresponding probability

'''

def fillBag(**balls):
    global bag
    bag = balls

def totalBalls():
    total = 0
    for color in bag:
        total += bag[color]
    return total
    # alternatively,
    # return sum(bag.values())

def probOf(color):
    return bag[color]/totalBalls()

def probAll():
    probDict = {}
    for color in bag:
        probDict[color] = probOf(color)
    return probDict