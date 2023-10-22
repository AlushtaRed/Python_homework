points ={1:"AEIOULNSTRАВЕИНОРСТ", 2:"DGДКЛМПУ", 3:"BCMPБГЁЬЯ", 4:"FHVWYЙЫ", 5:"KЖЗХЦЧ", 8:"JXШЭЮ", 10:"QZФЩЪ"}
k  = "ноутzбук"
res = 0
for i in k.upper():
    for j in points:
        if i in points[j]:
            res += j
print(res)
