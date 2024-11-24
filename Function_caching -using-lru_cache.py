from functools import lru_cache
import time


@lru_cache(maxsize=None)
def fx(n):
    time.sleep(3)
    return n*5


# Below 2 statements will take time delay to perform
print(fx(2))
print("terminated after 2 seconds")

print(fx(3))
print("Terminated after 3 seconds")

# Below same 2 statements will run without delay as it is saved in the cache memory
print(fx(2))
print("terminated after 2 seconds")

print(fx(3))
print("Terminated after 3 seconds")
