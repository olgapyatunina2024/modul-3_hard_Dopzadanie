summa_all = 0
sum_int = 0
sum_str = 0
def calculate_structure_sum(*data_):

    for element in data_:
        global summa_all, sum_int, sum_str

        if isinstance(element, int):
            sum_int += element
            summa_all += element

        elif isinstance(element, str):
            sum_str += len(element)
            summa_all += len(element)

        elif isinstance(element, list):
            calculate_structure_sum(*element)
        elif isinstance(element, tuple):
            calculate_structure_sum(*element)
        elif isinstance(element, set):
            calculate_structure_sum(*element)
        elif isinstance(element, dict):
            for k in element:
                key = (k, element[k])
                calculate_structure_sum(*key)
    return summa_all

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])]

result = calculate_structure_sum(data_structure)
print('Result :', result)

print('Сумма всех чисел', sum_int)

print('Сумма длин всех строк', sum_str)

#sum_int = calculate_structure_sum(data_structure)
#print('Int :', sum_int)

#summa_all = 0
#sum_chisl = calculate_structure_sum(data_structure)
#print ("Сумма всех чисел:", sum_chisl[0])

#summa_all = 0
#sum_len = calculate_structure_sum(data_structure)
#print("Сумма длин всех строк:", sum_len[0])
