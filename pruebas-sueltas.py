# Python program to iterate 
# over 3 lists using zip function 

num = [10, 22, 34]
color = ['red', 'while', 'black'] 
value = [255, 256,664]

# iterates over 3 lists and excutes 
# 2 times as len(value)= 2 which is the 
# minimum among all the three 
for (n,c,v) in (num, color, value):
    print(n,c,v)
    print(f'renglon{n}')