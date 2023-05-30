""" Write a Python script to sort (ascending and descending) a dictionary by value. """


d={"name" : "John", "age":"34","gender":"male", 101 :"brad", 23:"sub"}
print(sorted(d.values()))
print(sorted(d.values(),reverse=True))