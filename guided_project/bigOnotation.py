
# tim's notes

def find_name(name, phone_book):
    a = 2
    b = 10**a
    c = 3 + 4
    for person in phone_book:
        if name == person:
            return True


name = 'kim'
phone_book = ['tim', 'dan', 'oliver', 'kim']

O(1 + 1 + 4)

# sean chen

O(1)  # same thing as 0(c)
# number of operations does not scale with input
# -- doesn't matter how how big an input is, this operation is going to take the same amount of time
# -- takes the same amount of time (number of operations) if there's a single element or a million elements

# example 1: accessing something in an array via it's index
arr[1]

# example 2: grabbing a key in value from a dictionary, assuming the key is in there
dict['key']

0(n)
# number of operations does depend on the input size

# example: search function that takes in an array and target


def search(arr, target):
    # loop through array
    for x in arr:
        # if an x matches the target, return True
        if x == target:
            return True
    return false


# -- if we imagine this function with just two elements:
[1, 2]  # <- and searching for a target of 2
# we're going to expect everything from the array until the target is found (more time/number of operations)

# -- if we imagine the function with 1 - 1,000,000
[1, 2, ..., 10000000]  # <- and target is 1,000,000
# we would be checking every statement (for, if) for each element

# in the worst case, with list 1 we had to do 2 inspections in the worst case,
# in the case of list 2, we had to do 1,000,000


0(1)  # 0(c)
# considered 'the best' because the function executes in constant time
# c = constant (could be some huge value)
0(1000000000)  # <- is still constant time

# ----------


def do_x_to_first_ten_arr(arr):
    # loop over first 10 elements
    for i in range(10):
        print(arr[i])


def foo(arr):
    # loop and skip through every other element
    for i in range(len(arr), step=2):  # n: 1000/2 = 500
        print(arr[i])


# linked lists

# arrays & linked lists store things in order
# -- arrays: allow you to index to fetch particular elements
