scores = {"Alex":97, "Dom":87, "Kim":99}
scores["sam"]=94

print(scores)

print(scores.keys())
print(scores.values())
print(scores.items())

print(sorted(list(scores)))

print("Alex" in scores)

s = iter(scores)
for k in s:
    print(k)

si = scores.items()
for k,v in si:
    print(k,v)