# import numpy as np
#
#
# def creating_array():
#     a = np.arange(15).reshape(3, 5)
#     print(a)
#     print(a.shape)
#     print(a.ndim)
#     print(a.dtype.name)
#
#
# if __name__ == '__main__':
#     creating_array()


def combination_task(input_list):
    for ind, val in enumerate(input_list):
        for ele in range(ind+1 , len(input_list)):
            yield (val, input_list[ele], input_list[ele - (len(input_list)-1)])


if __name__ == '__main__':
    result = list(combination_task(['Anish', 'Panish', 'Monish', 'Danish']))
    print(result)
