#Given an array of integers and a value, determine if there are any two integers in the array whose sum is equal to the given value. 
#Return true if the sum exists and return false if it does not. Consider this array and the target sums:
# | 5 | 7 | 1 | 2 | 8 | 4 | 3 |
# | Target Sum 10 | 7+3=10, 2+8=10
# | Target Sum 19 | No 2 values sum up to 19

def find_sum_of_two(A, val):
    valorEncontrado = set()
    for value in A: #percorrer toda a lista
        if val - value in valorEncontrado: #se a subtração do valor menos elemento atual da lista tiver um valorEncontrado
            return True #significa q encontrou
        valorEncontrado.add(value) #inserir o valor atual no valorEncontrado
    return False

find_sum_of_two([5, 7, 1, 2, 8, 4, 3],2)