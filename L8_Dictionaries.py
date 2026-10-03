
family = {"Mom":46,"Dad":48,"Sister":16,"Brother":15}

print(type(family))
family["Bob"] = 14
print(family)
family["Mom"] = 47
print(family)
family.pop("Bob")
print(family)
print(len(family))

print(family.keys())
print(family.values())
print(family.items())

for i in family:
    print(i)

for i,j in family.items():
    print(i,j)

print("Sister" in family)
print("Sister" not in family)
