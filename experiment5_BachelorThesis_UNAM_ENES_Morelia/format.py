input = open("tesisTotal1.txt", "r", encoding="utf-8")
output = open("tesisTotal2.txt", "w", encoding="utf-8")

text, register = input.readlines(), ""
for line in text:
    if line.startswith("Licenciatura"): 
        if register != "": output.write(register.replace("\n", "") + "\n")
        register = line
    else: register += line

output.close()
input.close()