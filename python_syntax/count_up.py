def count_up(start, stop):
    """Print all numbers from start up to and including stop.

    For example:

        count_up(5, 7)

   should print:

        5
        6
        7
    """

    # YOUR CODE HERE
    for num in range(start, stop + 1): #+1 to include the stop number
        print(num)


count_up(5, 7)        
count_up(78,104)