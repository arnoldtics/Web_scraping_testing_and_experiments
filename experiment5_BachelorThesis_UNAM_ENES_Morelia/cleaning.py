input = open("tesisTotal2.txt", "r", encoding="utf-8")
output = open("tesisTotal3.txt", "w", encoding="utf-8")

text = input.readlines()
for line in text:
    line = line.strip()
    line = line.replace("Licenciatura en ", "")
    i, j = line.find("/"), line.find(" presenta ")
    line = line[:i] + line[j:]

    output.write(line + "\n")

input.close()
output.close()