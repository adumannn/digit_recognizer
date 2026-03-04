def delete(D,N):
    for x in D.keys():
        if x>N:
            del D[x]
    return D
my_dict = {101: 'ICP', 102: 'AST'}
delete(my_dict,101)