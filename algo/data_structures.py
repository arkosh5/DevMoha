"""def foo(numbers):
    result = []
    num = 0
    i = 0
    found = False
    while i < len(numbers):
        if i == 0:
            num = numbers[i]
            i += 1
        if numbers[i] < num:
            result.append(numbers[i])
            num = numbers[i]
            if result[-1] < result[0]:
                result[-1], result[0] = result[0], result[-1]
                result.pop()
                result.pop()
                found = True
                i = 0
        if found:
            numbers.pop(0)
        i += 1
    return result


print(foo([10, 5, 2, 3, 4, 1, 6, 7, 8, 9]))"""

"""def concat_list(strings):
    if len(strings) == 0:
        return ""
    else:
        return strings[0] + concat_list(strings[1:])


def product(data):
    if len(data) == 0:
        return 1
    else:
        return data[0] * product(data[1:])


def backwards(s):
    if len(s) == 0:
        return ""
    else:
        return backwards(s[1:]) + s[0]


def odds(data):
    if len(data) == 0:
        return []
    elif data[0] % 2 == 0:
        return odds(data[1:])
   """

'''def num_rushes(slope_height, rush_height_gain, back_sliding, rushes=0):
    if slope_height == 0:
        return 0
    else:
        if back_sliding < slope_height > 0:
            total_rush = rush_height_gain - back_sliding
            gain = 0.95

            if rushes >= 1:
                for i in range(rushes):
                    if i >0:
                        gain *= 0.95

                back_sliding = back_sliding * gain
                rush_height_gain = rush_height_gain * gain
                return num_rushes(slope_height - total_rush, rush_height_gain, back_sliding, rushes + 1)
            else:
                return num_rushes(slope_height - total_rush, rush_height_gain, back_sliding, rushes + 1)
    return rushes


ans = num_rushes(100, 15, 9)
print(ans)'''

"""
def dumbo_func(data):
  
    count = 0
    if len(data) == 0:
        return 0
    else:
        if (data[0] // 100) % 3 != 0:
            data.remove(data[0])
            return 1 + dumbo_func(data)
        else:
            data.remove(data[0])
            return dumbo_func(data)


'''data = [677, 90, 785, 875, 7, 90393, 10707]
print(dumbo_func(data))'''

MAX = 10000000

# Create an array for memoization
f = [0] * MAX


def fib(n):
    # Base cases
    if (n == 0):
        return 0
    if (n == 1 or n == 2):
        f[n] = 1
        return (f[n])

    # If fib(n) is already computed
    if (f[n]):
        return f[n]

    if (n & 1):
        k = (n + 1) // 2
    else:
        k = n // 2

    # Applying above formula [Note value n&1 is 1
    # if n is odd, else 0.
    if ((n & 1)):
        f[n] = (fib(k) * fib(k) + fib(k - 1) * fib(k - 1))
    else:
        f[n] = (2 * fib(k - 1) + fib(k)) * fib(k)

    return f[n]


print(fib(10**6) % 10**10)"""
"""Write a recursive function all_odds(numbers) that takes a list of integers and returns True if (and only if) all the elements of the list are odd numbers, otherwise it returns False.

Your code must not use for or while and must not import anything.

The focus of this question is on recursion. O(n2)
solutions are acceptable; that is, you can use slicing if you wish.
def foo(numbers, start=None):
    if start is None:
        start = 0
    if start >= len(numbers):
        return 0
    x = numbers[start]
    p = x * x * x
    if p >= 0:
        return foo(numbers, start + 1) + 1
    else:
        return foo(numbers, start + 1) - 1
print(foo([1, 2,2,2,2,2,2]))"""

"""Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0."""

"""def three_sum(nums):
    nums.sort()
    result = []
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        j = i + 1
        k = len(nums) - 1
        while j < k:
            if nums[i] + nums[j] + nums[k] == 0:
                result.append([nums[i], nums[j], nums[k]])
                j += 1
                k -= 1
                while j < k and nums[j] == nums[j - 1]:
                    j += 1
                while j < k and nums[k] == nums[k + 1]:
                    k -= 1
            elif nums[i] + nums[j] + nums[k] < 0:
                j += 1
            else:
                k -= 1
    return result"""

"""Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity."""

'''def searchRange(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    result = []
    found = False
    for index, value in enumerate(nums):
        if value == target:
            result.append(index)
            found = True
        if len(result) <= 1 and index == len(nums) - 1 and found is True:
            result.append(result[0])

    if not found:
        return [-1, -1]

    return [result[0], result[-1]]


print(searchRange([1, 2, 3, 3, 3, 3, 4, 5, 9], 3))'''

'''def countCharacters(words, chars):
    """
    :type words: List[str]
    :type chars: str
    :rtype: int
    """
    ans = ''
    for word in words:
        for letter in word:
            if chars.count(letter) < word.count(letter):
                break
        else:
            ans += word
    return len(ans)


print(countCharacters(["cat", "bt", "hat", "tree"], "atach"))'''

"""The LinkedList code from before is provided below.
Add three functions to the LinkedList.
"get_position" returns the element at a certain position.
The "insert" function will add an element to a particular
spot in the list.
"delete" will delete the first element with that
particular value.
Then, use "Test Run" and "Submit" to run the test cases
at the bottom."""


'''class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        if position < 1:  # Just in case the position is too small
            return
        current = self.head
        while current and position > 1:
            position -= 1
            current = current.next
        return current

    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        if position == 1:
            new_element.next = self.head
            self.head = new_element
        else:
            before = self.get_position(position - 1)
            if before is None:
                raise ValueError("invalid position")
            new_element.next = before.next
            before.next = new_element

    def delete(self, value):
        """Delete the first node with a given value."""
        # Store head node
        temp = self.head

        # If head node itself holds the key to be deleted
        if (temp is not None):
            if (temp.value == value):
                self.head = temp.next
                temp = None
                return

        # Search for the key to be deleted, keep track of the
        # previous node as we need to change 'prev.next'
        while (temp is not None):
            if temp.data == value:
                break
            prev = temp
            temp = temp.next

        # if key was not present in linked list
        if (temp == None):
            return

        # Unlink the node from linked list
        prev.next = temp.next

        temp = None



# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

# Test get_position
# Should print 3
print(ll.head.next.next.value)
# Should also print 3
print(ll.get_position(3).value)

# Test insert
ll.insert(e4, 3)
# Should print 4 now
print(ll.get_position(3).value)

# Test delete
ll.delete(1)
# Should print 2 now
print(ll.get_position(1).value)
# Should print 4 now
print(ll.get_position(2).value)
# Should print 3 now
print(ll.get_position(3).value)
'''
'''
import pyautogui as pg
import time

time.sleep(7)
txt = open("animals.txt", "r")
name = "don't challenge me sarah"
# make name a large string
pg.typewrite(name)


for j in range(40):
    if j %2 == 0:
        pg.typewrite("i love you")
    if j %2 == 1:
        pg.typewrite("i love you more")

    pg.press('Enter')'''

def function(input):
    """"""