# Напишите программу для. проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z  для всех значений предикат.

i =0
for x in range(2):
    for y in range(2):
        for z in range(2):
            if not(not(x or y or z) == (not x and not y and not z)):
                i+=1
if i:
    print("False")
else:
    print("All True")
    

