#ітератор
lst=[1,2,3,4,5,6,6]
"""
print(iter(lst))


class My_iterator:
    def __init__(self, data):
        self.data=data
        self.index=0
    def __iter__(self):
        return self
    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        value = self.data[self.index]
        self.index+=1
        return value
for num in My_iterator(lst):
    print(num)

"""
"""
def my_generator(data):
    for item in data:
        yield item

for num in  my_generator(lst):
    print(num)

"""

def calc():
    def add(a,b):
        return a+b
    def sub(a,b):
        return a-b
    def mult(a, b):
        return a*b
    def div(a,b):
        if b!=0:
            return a/b
        else:
            raise ValueError('Помилка ділення на 0')
    return add, sub,mult,div
add, sub,mult,div=calc()#відбувається замикання

print(div(3, 1))

