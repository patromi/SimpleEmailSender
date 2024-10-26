# Z podanego zbioru danych wyselekcjonuj 5 o największej wartości na jednostkę, znając kategorię obiektu
# Dane znajdują się w folderze "dane" w pliku "zbiór_wejściowy.json" oraz "kategorie.json"
# Wynik przedstaw w czytelnej formie na standardowym wyjściu

import json

def find_closest_purity(type, purity):
    available_purities = list(categories.get(type, {}).keys())
    if purity in available_purities:
        return purity

    if not purity.isnumeric():
        return None

    # Fallback to the closest match or None
    closest = min(available_purities, key=lambda x: abs(int(x) - int(purity)), default=None)
    return closest


#read categories from file
categories = {}
with open('kategorie.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
    for item in data:

        if item["Typ"] not in categories:
            categories[item["Typ"]] = {}
        categories[item["Typ"]][item["Czystość"]] = item['Wartość za uncję (USD)']

#print(categories)


#read and process valueables from file
ct_to_ounce = 0.00705479239
g_to_ounce = 0.0352739619
items = []
with open('zbiór_wejściowy.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
    for item in data:

        weight = item["Masa"].replace(',', '.')
        purity = item["Czystość"]
        type = item["Typ"]

        #convert gem's weight to ounces
        if weight[-2:] == 'ct':
            weight = float(weight[:-2]) * ct_to_ounce
        else:
            if weight[-1:] == 'g':
                weight = float(weight[:-1]) * g_to_ounce
            else:
                print(f"Error, unknown unit in {item}")

        # Find the closest available purity for the given type
        matched_purity = find_closest_purity(type, purity)
        if matched_purity is None:
            print(f"Warning: No matching purity found for {item}")
            continue

        unit_price = categories[type][matched_purity]
        item["Cena"] = weight * unit_price
        items.append(item)


#sort the items and output the 5 priciest ones in a readable format
items_sorted = sorted(items, key=lambda x: x.get("Cena", 0), reverse=True)
i = 1
print("\n")
for item in items_sorted[:5]:
    print(f"{i}:")
    for key in item:
        print(f"\t{key}: {item[key]}")

    print("\n")
    i+=1