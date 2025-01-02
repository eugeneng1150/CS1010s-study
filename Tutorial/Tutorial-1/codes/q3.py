x = 10
def ping(x):
    return pong(x + 4)
def pong(x):
    x += 1
    return x**2
  
print(ping(3)) # 64
#since the funciton of ping returns pong, it will call the funciton pong

print(pong(x)) # 121
ping(2) # nothing is printed