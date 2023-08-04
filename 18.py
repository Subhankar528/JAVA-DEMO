count=0
a=input("Enter here something : ")
print("so" in a or "So" in a)
print("length of",a,"is",len(a))
for letters in a :
    count=count+1
    print(letters,count)
print(a[1:2])#index starts from 0
if a=="sonu"  :
    print(a.startswith("s"))
    print(a.endswith("p"))
    print(a.find("u"))
    print(a.find("n"))
    print(a.find("o"))
    print(a.find("s"))
    print("done")
    a.startswith("so")
print(a.lower())#String library creates a copy of original String
print(a.upper())
y="          Hello          "
print(y)
print(y.replace("l","p"))
print(y.lstrip())
print(y.rstrip())
print(y.strip())
print("Thank You")
