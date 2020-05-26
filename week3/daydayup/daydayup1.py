#每天进步1% 每天退步1%
#daydayup1.py
df = 1/100
dayup = pow(1.001,365)

daydown = pow(0.999, 365)

print("if use 0.99---up is",pow(0.99,365))
print("everyday up->{:.2f}, everyday down-->{:.2f}".format(dayup,daydown))