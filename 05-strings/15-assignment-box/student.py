# write your code here
def box(string):
    lengte = len(string)
    hori = f"+-{lengte*"-"}-+"
    return f"{hori}\n| {string} |\n{hori}"