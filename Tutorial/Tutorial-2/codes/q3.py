# FULL MARKS
a, b, c = "east", "easter", "easy"
a, b, c = c, a, b #easy , east, easter

if a < b:
    a, b = b, a
else:
    if b < c:
        a += b # a = easyeast
b = a + c # b = easyeasteaster

print(a[:-1])  #easyeas 
print(b[1:]) #asyeasteaster
print(c[::-1]) #retsae