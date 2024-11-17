#lista
do_kupienia = ['marchew', 'chleb', 'maslo', 'mleko']

for i in range(5):
    print(i)
    
for i in range(len(do_kupienia)):
    print(do_kupienia) #nie ma iteratora

# jak moge wyświetlic to mozna zrobić cos innego   
for i in range(len(do_kupienia)): # to daje wi\eksza możliwości modyfikacji np i+1
    print(do_kupienia[i])
    

print('------kod ten sam bardziej paitonicznie-----')
    
for product in do_kupienia: #i jest elementem listy, a dla czytelności zmieniamy nazwę na product
    print(product)