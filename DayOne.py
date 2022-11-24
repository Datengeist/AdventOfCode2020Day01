j: int =0
content: list[str]

with open("./input.txt", "r", encoding="UTF-16") as f:
    content = f.readlines()

for line in content:
    j+=1
    verarbeitung: int= 2020 - int(line)
    ausgabe: int= int(line) * verarbeitung
    for i in range(0,j):
        if (int(content[i])+int(line)) == 2020:
            print(str(i) + " " + str(j) + " " + str(int(content[i])*int(line)))

j = 0
    
