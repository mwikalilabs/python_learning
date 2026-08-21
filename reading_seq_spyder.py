# %%
file1=open("F:/dna1.fasta.txt","r")
file2=open("F:/results.txt","w")
# %%


# %%
count=0
seq=""
# %%


# %%
for line in file1:
    line = line.rstrip("\n")
    count +=1
    if count == 1:
        file2.write(line)
    else:
        seq=seq.upper()

        seq=seq+line
# %%

        
        
        
length1 = len(seq)
file2.write("\n" +"Length of the sequence is " + str(length1)
+"/n")



# %%
nucleotide=("A","T","C","G","N")
gc=0

for x in nucleotide:
    n_count = seq.count(x)
    file2.write(str(x)+str(n_count)+"\t")
    if x=="G" or x=="C":
        gc = gc+n_count
    print(x,n_count)
# %%
    
percentage_gc=(gc/length1)*100
file2.write("\n"+"GC content="+ str(percentage_gc))


# %%

# %%
file1.close()
file2.close()
# %%
