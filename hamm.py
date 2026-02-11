with open("rosalind_hamm.txt", "r") as file:
    dna1, dna2 = file.read().strip().split("\n")

count = 0

for i in range(len(dna1)):
    if dna1[i] != dna2[i]:
        count += 1

print(count)
