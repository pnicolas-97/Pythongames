# Invertir palabra
n = input('Ingresar palabra: ')
v_n = list(n)
v = []
for i in range(len(v_n),0,-1):
    if v_n[i - 1] == ' ':
        continue
    v.append(v_n[i - 1])
print(v)