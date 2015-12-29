i = input("How many bottles of beer you wanna throw: ")
#i = 99
j=i
while i != 1:
        print "%s bottles of beer on the wall, %s bottles of beer." %(i,i)
        i-=1
        print "Take one down and pass it around, %s bottles of beer on the wall.\n"%(i)

if i==1:
    print "%s bottle of beer on the wall, %s bottle of beer.\nTake one down and pass it around, no more bottles of beer on the wall."%(i,i)

print "\nNo more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, %s bottles of beer on the wall."%(j)
