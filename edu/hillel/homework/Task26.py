# def primes(rang=100):
#     lst=[1]
#     for num in range(rang):
#         if num > 1:
#             for i in range(2, num):
#                 if (num % i) == 0:
#                     break
#             else:
#                 lst.append(num)
#     return lst
#
# print(primes(200))


primes = lambda rang: [num for num in range(2, rang) if not 0 in map(lambda z: num % z, range(2,num))]
print("""1,""",", ".join(map(str, primes(200))))

