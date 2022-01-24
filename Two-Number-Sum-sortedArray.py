#sort array - O(nlog(n)) Time, O(1) Space -> best for space

def twoNumberSort(array, targetSum):
    # (.sort) of the array does exactly that, is sorts the array from smallest to largest. This is an automatic function built in for lists.
    # left is set to 0 to start from the left
    # right is set to the length of the list that can be iterated -1, meaning it doesn't want iterate the last number. Why? because left has taken care of one integer, meaning that if the -1 is not there, it's going to error, as the while loop will try to iterate 1 too many times.
    # a while loop will keep running until it is directed to stop.
    # this while loop says, if the current sum is equal to the target sum (10), return the two integers
    # otherwise if the currentSum is less than the targetSum, iterate the left iterable(pointer) up one.
    # Also, if the current sum is more than the target sum, iterate the right pointer back down.
    # once it has gone through the list and fails all the if statements in the while loop.
    # no dice grandma!! it reachees the return statement.
    array.sort()
    left = 0
    right = len(array) -1
    while left < right:
        currentSum = array[left] + array[right]
        if currentSum == targetSum:
            return [array[left], array[right]]
        elif currentSum < targetSum:
            left += 1
        elif currentSum > targetSum:
            right -= 1
    return("No dice grandma!!\nthe list doesn't include two numbers that equal to your secret number.")

result = twoNumberSort([3,5,-4,8,11,-1,6], 10)
print(result)