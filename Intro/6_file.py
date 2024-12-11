
def create_file() -> None:
    try:
        file = open('file.txt', 'w', encoding='utf-8')
        file.write('Latin content\r\n')
        file.write('Кирилічний контент')
    except OSError as err:
        print('Error writing file', err)
    else:
        file.flush()
        print('Write file OK')
    finally:
        file.close()

def read_file() -> None :
    try :
        with open( "file.txt", "r", encoding='utf-8') as file :
            print(file.read())
    except OSError as err:
        print('Error reading file', err)

def read_file2() -> None :
    try :
        with open( "file.txt", "r", encoding='utf-8') as file :
           for line in file :
               print(line)
    except OSError as err:
        print('Error reading file', err)

def create_http():
    try:
        with open("file2.txt", "w", encoding='utf-8') as file:
            file.write ("Host: localhost\r\n")
            file.write ("Connection: close\r\n")
            file.write ("Connection-Type: text/html\r\n")
            file.write ("Content-Length: 100500\r\n")
            file.write ("Accept: *.*\r\n")
            file.write ("\r\n")
            file.write ("<html></html>\r\n")
    except OSError as err:
        print("Error reading file: ", err)

# def parse_http_imp() -> dict:
#     d = {}
#     with open("file2.txt", "r", encoding='utf-8') as file:
#         for line in file:
#             if ':'


def parse_http() -> dict:
    return {k: v
        for k, v in (map(str.strip, line.split(':') )
            for line in open("file2.txt", "r", encoding='utf-8') if ':' in line)}

def main():
    try:
        # create_http()
        # parse_http_imp()
        for k, v in parse_http().items():
            print(k, v)
        d = {}
        print(type(d))
        d["a"] = 1
        d["b"] = 2
        print(d)
        d2 = {k: str(k) for k in range(10)}
    except OSError as err:
        print("Error reading file: ", err)

if __name__ == "__main__":
    main()

