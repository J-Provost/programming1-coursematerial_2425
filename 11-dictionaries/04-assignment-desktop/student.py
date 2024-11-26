catalog = {
    'Intel Core i7 13700K': 439,
    'Intel Core i5 13600K': 331,
    'Gigabyte Z790 AORUS ELITE AX': 261,
    'MSI MAG Z790 TOMAHAWK WIFI': 279,
    'Corsair DDR5 Vengeance 2x16GB 5600': 95,
    'Corsair DDR5 Vengeance 2x32GB 5600': 165,
    'MSI GeForce RTX 4070 VENTUS 3X 12G OC GPU': 659,
    'Gigabyte GeForce RTX 4090 GAMING OC 24G GPU': 1849,
}
def desktop(catalog, components):
    """
    Calculates the total cost of the specified components using the given catalog.

    Parameters:
        catalog (dict): A dictionary where keys are component names and values are their prices.
        components (list): A list of component names to calculate the total cost for.

    Returns:
        int: The total cost of the specified components.
    """
    return sum(catalog.get(component, 0) for component in components)
