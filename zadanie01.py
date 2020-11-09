#Przemysław Iskra
#nr almumu: 145863
#grupa: L6

def klucz(list_el):
    return list_el[1], list_el[2]

list_to_sort = [[3, 2, 3], [2, 0, 2], [3, 0, 1]];

list_to_sort_2 = [[3, 2, 3], [2, 0, 2], [3, 0, 1], [3, 1, 0]];

print("Listy niesortowane");

print(list_to_sort);
print(list_to_sort_2);

print("Listy posortowane");

list_to_sort.sort(key=klucz);
list_to_sort_2.sort(key=klucz);

print(list_to_sort);
print(list_to_sort_2);