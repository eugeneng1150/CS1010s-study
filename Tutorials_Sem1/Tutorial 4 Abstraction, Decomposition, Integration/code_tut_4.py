def symmetric_grid(n):
    string = ""
    for i in range(n):
        for j in range(n):
            if i == j:
                string += "*"
            else:
                string += "_"
        string += "\n"
    return string
print(symmetric_grid(6))