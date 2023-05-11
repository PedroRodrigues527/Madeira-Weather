def saveToFile(content, file):
    try:
        with open(file, 'w') as f:
            for strings in content:
                f.write(strings)
            print("Content saved with success")
    except FileExistsError as e:
        print("Error opening the file\n"+e)
    except FileNotFoundError as e:
        print("File not Found\n"+e)