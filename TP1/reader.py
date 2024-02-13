import io
import sys


sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')

sports = []
count = -1.0
ables = 0.0
athletes = {}

for line in sys.stdin:
    if count >= 0:
        splited_line = line.split(',')
        if splited_line[8] not in sports:
            sports.append(splited_line[8])

        if splited_line[12] == "true\n":
            ables += 1
        
        age = int(splited_line[5])
        if age not in athletes:
            athletes[age] = 1
        else:
            athletes[age] += 1
    count += 1

sports.sort()
print("### Modalidades Desportivas:")
for sport in sports:
    print(sport)

print("### Percentagem de atletas aptos:", ables / count * 100, "%")
print("### Percentagem de atletas inaptos:", (count - ables) / count * 100, "%")
print("### Distribuição de atletas por escalão:")

max = max(athletes.keys())
min = min(athletes.keys())

print(f"FR count: {count}")
for i in range(0, max+1, 5):
    age_counter = 0
    for j in range(i, i+5):
        if j in athletes:
            age_counter += athletes[j]
    if age_counter != 0:
        print(f"\tEscalão de {i} até {i+4} anos: {age_counter} atletas.")

