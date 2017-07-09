# Simple programs, takes a final string, creates a random intial one
# and mutates until it matches fina;

import random
import datetime


# Generic set of letters for genes, and a target string


geneSet = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!."
target = "Hello World!"


# Generate a random string of letters from the gene set
# This implementation allows us to generate a long string with
# a small set of genes using as many unique genes as possible


def generate_parent(length):
    genes = []
    while len(genes) < length:
        sampleSize = min(length - len(genes), len(geneSet))
        # random.sample takes sampleSize amound of values from the input
        # without replacement there will be no duplicates in the generated
        # parent unless geneSet contains duplicates or
        # length is greater than len(geneSet)
        genes.extend(random.sample(geneSet, sampleSize))
    return ''.join(genes)


# Fitness is the only feedback the engine gets to guide towards the solution
# Here, fitness value is the total number of letters in the guess that match
# the letter in the same position of the target


def get_fitness(guess):
    return sum(1 for expected, actual in zip(target, guess)
               if expected == actual)


# Produce new guess by mutating the current one
# Convert parent string to array
# Replace 1 letter with a randomly selected one for geneSet
# join into string


def mutate(parent):
    index = random.randrange(0, len(parent))
    childGenes = list(parent)
    newGene, alternate = random.sample(geneSet, 2)
    # if newGene is the same as the one being replaced
    # an alternate gene is used
    childGenes[index] = alternate \
        if newGene == childGenes[index] \
        else newGene
    return ''.join(childGenes)

# Important to monitor what is happening, to stop the engine if it gets stuck
# Allows us to learn what does and doesn't work, so we can improve
# Display a visual representation of the gene sequence
# guess, fitness and time elapsed


def display(guess):
    timeDiff = datetime.datetime.now() - startTime
    fitness = get_fitness(guess)
    print("{0}\t{1}\t{2}".format(guess, fitness, str(timeDiff)))

# Main
# Initialise bestParent to a random sequence of letters


random.seed()
startTime = datetime.datetime.now()
bestParent = generate_parent(len(target))
bestFitness = get_fitness(bestParent)
display(bestParent)

# Loop that generates a guess, requests the fitness and compares to previous
# best guess keeping the better of the two
# Repeats until all letters match the target
while True:
    child = mutate(bestParent)
    childFitness = get_fitness(child)

    if bestFitness >= childFitness:
        continue
    display(child)
    if childFitness >= len(bestParent):
        break
    bestFitness = childFitness
    bestParent = child
