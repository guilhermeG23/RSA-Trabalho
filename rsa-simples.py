entrada = int(input("Entrada:"))
p = int(input("p:"))
q = int(input("q:"))
n = int(input("n:"))
e = int(input("e:"))
d = int(input("d:"))

c = (entrada ** e) % n
print(entrada ** e)
print("RSA: {}".format(c))

d = (c ** d) % n
print(c ** d)
print("Des-RSA: {}".format(d))
