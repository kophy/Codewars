def cakes(recipe, available):
    return min([available[k] / recipe[k] if k in available else 0 for k in recipe]);