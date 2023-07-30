def main():
    extensions('file')

def extensions(file):
    file = input('File name: ').strip().lower()
    file = file.rpartition('.')[2]

    extensions_dict = {'image':['gif', 'jpg', 'jpeg', 'png'],
                       'application':['pdf', 'zip'],
                       'text':['txt']
    }
    
    if file not in str(extensions_dict.items()) or file == '':
        print('application/octet-stream')
        exit()
        
    for k, v in extensions_dict.items():
        if file == 'txt' in v:
            print(k, 'plain', sep='/')
        elif file == 'jpg' in v:
            print(k, 'jpeg', sep='/')
        elif file in v:
            print(k, file, sep='/')
        else:
            None

    return


main()