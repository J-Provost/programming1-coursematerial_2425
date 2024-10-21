# write your code here
def earlier(h1, m1, h2, m2):
    hour_earlier=h1<h2
    hour_same= h1==h2
    minutes= hour_same and (m1<m2)
    return hour_earlier or minutes or False