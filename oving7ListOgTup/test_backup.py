def separate(numbers, treshold):
    """""
    TODO: Funksjonen tar inn en liste (numbers) og et heltall (treshold). Den skal så sortere alle tallene som er lavere enn treshold i en ny liste,
    og legge alle tall lik eller større enn treshold, inkludert treshold, hvis det eksisterer i numbers, i en annen liste, for å så returnere begge listene.
    """""
    less = []
    more = []
    for i in numbers:
        if i < treshold:
            less.append(i)
        if i >= treshold:
            more.append(i)
    return sorted(less), sorted(more)

def multiplication_table(number):
    """""
    TODO: Funksjonen tar inn et heltall, og skal returnere en matrise med de n første elementene i de n første gangetabellene.
    Et tips er å lage matrisen først, før man fyller inn tallene
    """""
    Matrix = [[0 for x in range(number)] for y in range(number)]
    for i in range(1,number + 1):
        for j in range(1,number + 1):
            Matrix [i - 1][j - 1] = i * j
    return Matrix