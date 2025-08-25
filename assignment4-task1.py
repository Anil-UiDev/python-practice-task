try:
    file1 = open("sample.txt", 'r')
    read_file = file1.readlines()

    for idx, line in enumerate(read_file):
        print(f"Line {idx+1}: {line}")
    file1.close()
except FileNotFoundError:
    print("Error: file not found")
finally:
    print("\nProgram completed")
