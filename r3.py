
lines = []
with open('dryu.txt', 'r', encoding = 'utf-8-sig') as f:
    for line in f:
        lines.append(line.strip()) #將line加進lines清單


for line in lines:
    s = line.split(' ')
    time = s[0][:5]
    name = s[0][5:]
    #print(time)
    print(name)
    #print(s)