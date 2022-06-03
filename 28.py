# Polymorphism in Python.
print(5+5)
print("5" + "5" )
print("--------\n")


# Function caching in Python.
import time
from functools import lru_cache

@lru_cache(maxsize=3)
def some_work(n):
    # Some task taking n seconds.
    time.sleep(n)
    return n

if __name__ == "__main__":
    print("Now running some work")
    some_work(3)
    print("Done, calling again")
    some_work(3)
    print("called again")
