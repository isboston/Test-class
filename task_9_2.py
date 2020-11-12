func_key = lambda **kwargs: {key * 2: value for key, value in kwargs.items()}
print(func_key(abc=5, fff=4))
