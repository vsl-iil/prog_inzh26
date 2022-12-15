# === Задание 1 ===
def f0(n):
	return lambda x: x + n 

# Проверка работы функции по пользовательским данным
arg1 = int(input("n: "))
arg2 = int(input("x: "))
a = f0(arg1)
print(a(arg2))


# === Задание 2 ===
print("\nЗадание 2:")
def f1(x):
	return lambda: x**x

def f2(fnc):
	print(fnc)
	return fnc() + 5

# Проверка работы
n = int(input("n = "))
print(f2(f1(n)))