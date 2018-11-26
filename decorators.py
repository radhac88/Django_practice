def my_decorator(fn):
	def wrapper(name):
		print("Before the function")
		fn(name)
		print("After the function")
	return wrapper

@my_decorator
def my_func(name):
	print(name)

my_func("Ryan")
my_func("Todd")