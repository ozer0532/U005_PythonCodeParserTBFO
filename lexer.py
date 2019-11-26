symbol = ['{', '}', '(', ')', '[', ']', '.', '"', ',', "'"]
operator = ['+','-',':','*','/','=','>','<','?','|','&','^','%','$','#','!', '~', '`', '\\', '@', '_']
KEY= symbol+operator

keywords = ['True', 'False', 'None', 'and', 'or', 'not', 'is', 'class', 'def', 'return', 'if', 'elif', 'else', 'while', 'for', 'in', 'break', 'continue', 'import', 'as', 'from', 'raise', 'with', 'pass']

def ReadFile () -> list:
    space = ' '
    conc = ''
    out = []
    fin = ""

    fileFound = False
    while not fileFound:
        try:
            fin = open(input("Read from file: "))
        except FileNotFoundError:
            print("File is not found. Check to see if you typed in the correct file and try again.")
            fileFound = False
        else:
            fileFound = True

    for y in fin.read(1):
        if y != '\n' and y != space :
            conc += y
        if (y != ""): 
            print(conc)
            if y == space or y in KEY or conc in KEY: # if next y == ' '
                if conc != '':
                    if (conc in keywords or conc in KEY):
                        out.append(conc)
                    else:
                        out.append('Abjad')
                    conc = ''

    return out

if __name__ == "__main__":
    out = ReadFile()
    print(out)