import string as st
import random as r

alphabet = st.digits + st.ascii_uppercase[:6]
colors = []
amount = int(input('Сколько цветов вам нужно?'))
for i in range(0, amount):
    hex_color = ''
    for num in range(0, 6):
        index = r.randint(0, len(alphabet) - 1)
        hex_color += alphabet[index]
    colors.append(hex_color)

print(colors)





