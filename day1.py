# find the 2 numbers that add up to 2020
# and return their product

with open("input.txt", "r") as numbers:
    input = numbers.read().splitlines()
    input = [int(i) for i in input]

for nb1 in input:
    for nb2 in input:
        if nb1 + nb2 + nb3 == 2020:
            print(nb1*nb2*nb3)

'''
#solved pt1 this way, not scaleable for pt2 though...
winners = []

for nb1 in input:
    nb2 = 2020-nb1
    if nb2 in input:
        winners.append(nb2)
print(winners)

def multiply(winners):
    product = 1
    for i in winners:
        product = product * i
    return product

print(multiply(winners))'''
