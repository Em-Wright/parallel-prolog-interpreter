import csv

f = open("output2.txt", "r")

arr = []
c = 0
for h in f:
    if c > 100000:
        break
    c += 1
    arr.append(int(h.rstrip()))

print(c)

with open("stackheight.csv", "w") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([])
    for r in arr:
        writer.writerow([r])
