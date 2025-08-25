content = input("Please enter the content for the file :")

try:
    with open('output.txt', 'w') as file:
        file.write(content)
        file.close()
    print("File has been created successfully")
    
    with open('output.txt', 'r') as file:
        file_content = file.read()
        print(file_content)
        file.close()
        
    with open('output.txt', 'a+') as file:
        added_content = input("Add something to append to file :")
        file.write("\n"+added_content)
        updated_content = file.read()
        file.close()
    
    with open('output.txt', 'r') as file:
        file_content = file.read()
        print(f"updated content : {file_content}")
        file.close()
        
        
except IOError as e:
    print(f"An Error occurred while writing the content to the file: {e}")
    
finally:
    print("Program Completed")
