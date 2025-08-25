list = list(range(1,11))
extracted_list = list[:5]
reversed_list = extracted_list[::-1]

print(f"Original List : {list}")
print(f"Extracted first five elements: {extracted_list}")
print(f"Reversed extracted elements: {reversed_list}")



#Here I have used [::-1] instead of reverse() method because reverse() method was giving None as it just directly changes the list, whereas [::-1] creates a new list
