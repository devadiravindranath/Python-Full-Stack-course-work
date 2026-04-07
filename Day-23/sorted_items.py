data = {
    'soap': 65,
    'bread' : 45,
    'butter':102,
    'salt': 10
}

print(dict(sorted(data.items(),key=lambda i : i [1], reverse = True)))
print(dict(sorted(data.items(),key=lambda i : i [1])))
print(dict(sorted(data.items(),key=lambda i : i [0], reverse = True)))
print(dict(sorted(data.items(),key=lambda i : i [0])))