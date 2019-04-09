def get_even_list(l):
    """ l is argument of a list """
    menu = []
    for i in l:
        if i % 2 == 0:
            menu.append(i)
    return(menu)

print(get_even_list([1,2,3,4,5,8]))
