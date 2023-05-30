""" Write a Python script to check whether a given key already exists in a dictionary. """


d={"name" : "John", "age":"34","gender":"male", 101 :"brad", 23:"sub"}

if 'age' in d.keys():
    print('present')
else:
    print('not present')