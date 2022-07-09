import itertools

def get_factors(x):
    ret_list = []
    for i in range(1, x):
        if x % i == 0:
            ret_list.append(i)
    return ret_list

print(get_factors(20))

candidate_list = list(range(1, 100))
filtered_list = list(itertools.filterfalse(lambda x: x != sum(get_factors(x)), candidate_list))

for i in filtered_list:
    print(f"perfect number is: {i}, {get_factors(i)}")