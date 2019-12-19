from hashlib import sha256

# class Human:
#     def __init__(self, first_name):
#         self.first_name = first_name
#
#     def __hash__(self):
#         return 1
#
# h1 = Human('Dima')
# h2 = Human('Alex')
#
# print(h1.first_name)
# print(h1.__hash__())
#
# d = {
#     h1: 1,
#     h2: 1
# }
# print(d)

print(sha256(b'password').hexdigest())