def top_n(items, n):
    '''
    returns top n items in an array in descending order

    args:
        items(array): list or array like object
        n(int): num of items to return

    output:
        array top n items in descending order

    Egs:
        >>>top_n([7,4,6,3,9], 3)
        [9,7,6 ]
    '''

    for i in range(n): #keep sorting until we have top n items
        for j in range(len(items) - 1 - i):

            if items[j] > items[j + 1]: #if this item is bigger than next item
                items[j], items[j+1] = items[j+1], items[j] #swap the two

    #get the last 2 items
    top_n = items[-n:]

    #return in descending order
    return top_n[::-1]