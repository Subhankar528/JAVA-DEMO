def computepay(h, r):
    if h<=40 :
        return(h*r)
    else :
        return((40*r)+((h-40)*1.5*r))
h =float(input("Enter Hours:"))
r=float(input("Enter Rate :"))
p = computepay(h, r)
print("Pay", p)
hjsdfjbhjdvbhjbvbhjdsvbhj
