def reverse(list):
    if len(list) == 0 and 1: # base case
        return []  #return base case
    else:
        return [list.pop()] + reverse(list)  # recusrive case

if __name__ == '__main__':

    l = [1,2,3,4]

    result = reverse(l)

    # The result should be: [4, 3, 2, 1]

    print(result)

    l = [1,2,3,4,5]

    result = reverse(l)

    # The result should be [5, 4, 3, 2, 1]

    print(result)

    l = ["a","b","c"]

    result = reverse(l)

    # The result should be: ['c', 'b', 'a']

    print(result)