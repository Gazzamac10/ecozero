
def flatten_list(nested_list):
    flattened = []
    for item in nested_list:
        if isinstance(item, list):
            flattened.extend(flatten_list(item))
        else:
            flattened.append(item)
    return flattened

def save_list_to_txt(filename, input_list):
    try:
        with open(filename, 'w') as file:
            for item in input_list:
                file.write(str(item) + '\n')
        print(f"List saved to {filename}")
    except IOError:
        print("An error occurred while saving the list to the file.")
        

def readtext(path):
    # Initialize an empty list to store the lines from the file
    lines = []

    # Open the 'headers.txt' file for reading
    with open(path, 'r') as file:
        for line in file:
            # Append each line (as a string) to the list
            lines.append(line.strip())
    return lines

h = readtext('header1.txt')

l = h[3:]



listofprefix = ['RC Flat Slab','PT RC Flat Slab','RC Rib Slab','Two-way RC Slab',\
'One-Way Spanning RC','Precast Hollowcore with In-situ RC Beams',\
'Non-Composite Rolled Steel with PCC Planks','Composite Rolled Steel with Metal Decking',\
'Composite Cell Beams with Metal Decking','Steel Frame with CLT Slabs',\
'CLT Glulam and Steel Column Hybrid']


def concat(pre,list):
    out = []
    for item in list:
        out.append(pre+"_"+item)
    return out

new =  h[:3]+flatten_list([concat(listofprefix[i],l)for i in range(len(listofprefix))])
old = readtext('headers.txt')

print(len(new))
print (len(old))

save_list_to_txt('new.txt',new)
