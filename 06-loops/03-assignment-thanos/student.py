# write your code here
def thanos(queue_size, target_size):
    counter=0
    while queue_size>target_size:
        queue_size=queue_size//2
        counter+=1
    return counter

print(thanos(8,4))