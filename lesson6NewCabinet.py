# def sum_two_or_three(a,b,c=0):
#     return a + b + c
#
# print(sum_two_or_three(2,3))
# print(sum_two_or_three(b=2,c=3,a=4))
# print('Hello', 'World', sep='***', end='')
# print('Good bye!')


# def sum_all_of_them(*args):
#     return sum(args)
#
# print(sum_all_of_them(1,2,3,4,5,6,6,7))
#
# def concat_all(*args):
#     # res = ''
#     # for word in args:
#     #     res += word
#     # return res
#     res = ''
#     for word in args:
#         res.append({
#             'word': word,
#             'lenght': len(word),
#         })
#
#         return res
#
# print(concat_all('Hello', 'people', 'of', 'earth'))


def tester(a,b,c=0, *args, **kwargs):
    print(a,b)
    print(c)
    print(args)
    print(kwargs)


tester(2,3, 1,1,2,'1,', True, None, [1,2,3], {'name': 'Jack'}, name='Jack', surname='Smith', age=20,)

