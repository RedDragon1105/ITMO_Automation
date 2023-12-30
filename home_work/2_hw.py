def task_1(p: int, f:float, x:str, a:list, b:bool): # переменные и их аннотации
    return
p = 2 # переменные и их значения
f = 0.002
x = "oppo"
a = [1, 2, 3, 4]
b = True
task_1 # вызов функции
print("Тип p", type(p)) # вывод
print("Тип f", type(f))
print("Тип x", type(x))
print("Тип a", type(a))
print("Тип b", type(b))

def task_2(a:list): # переменная и аннотация
    return
a = [1, 2, 3, 5, 8, 13, 21] # значения переменной
task_2 # вызов функции
print("a[0:3] = ", a[0:3]) # вывод
# эта последовательность называется "список"


def task_3(num: int) -> int:
    return
num= int(input())**2
print(num)