def get_price(fruit):
    fruit = fruit.lower();
    if fruit in ["banana", "orange", "apple", "lemon", "grapes"]:
        return 5;
    elif fruit in ["avocado", "strawberry", "mango"]:
        return 7;
    else:
        return 9;

def mix_fruit(arr):
    return round(sum(list(map(get_price, arr))) / len(arr));