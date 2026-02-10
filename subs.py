with open("rosalind_subs.txt", "r") as file:
    dna, motif = file.read().strip().split("\n")


locations = []

for i in range(len(dna)):
    if dna[i : i + len(motif)] == motif:
        locations.append(i + 1)

print(" ".join(str(x) for x in locations))
