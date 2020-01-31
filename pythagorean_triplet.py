a=1
b=2
c=3

for c in range(3,1000):
    for b in range(2,c):
        for a in range(1,b):
            if a*a+b*b==c*c and a+b+c==1000:
                print(f"a is {a}, b is {b}, c is {c}")

            