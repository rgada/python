import itertools

# ******** itertools.count ********
counter = itertools.count() # will keep on returning next count starting from 0 to infinite until stopped.
for i in (counter):
    print(i)
    if i == 10:
        break

counter = itertools.count(5,5) #keep counting starting from 5 and increment by 5

# ******** itertools.cycle ********
# cycle through on and off state
cyl = itertools.cycle(['On', 'Off']) # It will keep cycling through given arguments. If its string link 'AB' it will keep returning A B A B
for i in range(6):  # instead of using cyl as iterator running loop in range and using next to fetch next value from iterator
    print(next(cyl))

# ******** itertools.repeat ********
# using repeat() to repeatedly print number
print ("Printing the numbers repeatedly : ")
print (list(itertools.repeat(25, 4))) # will print 25 four times


# ******** itertools.product ********
# This tool computes the cartesian product of input iterables.
# To compute the product of an iterable with itself, we use the optional repeat keyword argument to specify the number of repetitions.
# The output of this function is tuples in sorted order

print("The cartesian product using repeat:")
print(list(itertools.product([1, 2], repeat = 2))) # [(1, 1), (1, 2), (2, 1), (2, 2)] It same as itertools.product([1,2],[1,2])
print()

print("The cartesian product of the containers:")
print(list(itertools.product(['geeks', 'for', 'geeks'], '2')))
print()

print("The cartesian product of the containers:")
print(list(itertools.product('AB', [3, 4])))
print()


# ******** combinations ********
print("All the combination of list in sorted order(without replacement) is:")
print(list(itertools.combinations(['A', 2], 2)))
print()

print("All the combination of string in sorted order(without replacement) is:")
print(list(itertools.combinations('AB', 2)))
print()

print("All the combination of list in sorted order(without replacement) is:")
print(list(itertools.combinations(range(2), 1)))

# ******** combination with replacement ********
# with replacement elements can be repeated but in unique combinations only. position of elements does not matter
print("All the combination of string in sorted order(with replacement) is:")
print(list(itertools.combinations_with_replacement("AB", 2)))
print()

print("All the combination of list in sorted order(with replacement) is:")
print(list(itertools.combinations_with_replacement([1, 2], 2)))
print()

print("All the combination of container in sorted order(with replacement) is:")
print(list(itertools.combinations_with_replacement(range(2), 1)))

# ******** Permutations ********
print("All the permutations of the given list is:")
print(list(itertools.permutations([1, 'geeks'], 2)))
print()

print("All the permutations of the given string is:")
print(list(itertools.permutations('AB')))
print()

print("All the permutations of the given container is:")
print(list(itertools.permutations(range(3), 2)))


