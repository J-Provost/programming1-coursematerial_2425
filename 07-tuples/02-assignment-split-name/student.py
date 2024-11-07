# write your code here
def split_name(full_name):
    index = full_name.find(" ")
    names = (full_name[:index], full_name[index+1:])
    return names