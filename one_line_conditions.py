power = False

if power:
    voltage = 220
else:
    voltage = 0
print("полная запись:", voltage)

voltage = 220 if power else 0
print("короткая запись:", voltage)
