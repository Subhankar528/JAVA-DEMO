fhand=open('mbox.txt')
pl=fhand.read()
count=0
for lines in fhand :
    count=count+1
print(count)
print(len(pl))
