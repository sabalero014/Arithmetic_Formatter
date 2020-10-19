# example string
string = 'cat'
nombres = ['marcelo','lionel','nico','Lau']
los_nombres =""
width = 8

# print right justified string
print(string.rjust(width))
for i in nombres:
    print(i.rjust(width))
    los_nombres += "    " + i.rjust(width)
print(los_nombres)
print(f'Largo: {len(los_nombres)} debe ser igual a {4+ width * len(nombres)}')
