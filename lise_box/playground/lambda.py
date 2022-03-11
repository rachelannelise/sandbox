# %%
def identity(x):
    return x

# ^ is equivalent to:
lambda x: x

# %% because it is an expression it can be given a name
add_one = lambda x: x + 1

test = add_one(2)
test

# %% lambdas with multiple arguments, separated by a comma
full_name = lambda first, last: f'Full name: {first.title()} {last.title()}'
full_name('guido', 'van rossum')

# %%
portfolio = [
  {'name': 'MSFT', 'price': 65.1, 'shares': 50},
  {'name': 'AA', 'price': 32.2, 'shares': 100},
  {'name': 'CAT', 'price': 83.44, 'shares': 150},
  {'name': 'GE', 'price': 40.37, 'shares': 95},
  {'name': 'IBM', 'price': 91.1, 'shares': 50},
  {'name': 'IBM', 'price': 70.44, 'shares': 100},
  {'name': 'MSFT', 'price': 51.23, 'shares': 200},

]

portfolio.sort()

# %%
def stock_name(s):
    return s['name']

portfolio.sort(key=stock_name)

# %%
# vs lambda
portfolio.sort(key=lambda s: s['name'])