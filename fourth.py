#for table
print("\t\t\t\t\t\t Multiplication Table\n")
for i in range(1,21):
    print(i,end="\t")#end=' ' use for the horizontal line and \t for tab
print()
print("-----------------------------------------------------------------------------\n")
for j in range(1,11): #i for vartical nos
    for k in range(1,21): # j for horizonatal nos
        print(j*k,end="\t")
    print("\n")
