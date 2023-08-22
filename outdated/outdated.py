def main():
    int_date_conversion()
    
months_in_year = {
    "January": '01',
    "February": '02',
    "March": '03',
    "April": '04',
    "May": '05',
    "June": '06',
    "July": '07',
    "August": '08',
    "September": '09',
    "October": '10',
    "November": '11',
    "December": '12'
}

def int_date_conversion():
    while True:
        mdy = input('Date: ')
        if mdy.split()[0] in months_in_year and ',' in mdy.split()[1]:
            mdy = mdy.split()
            for word in mdy:
                if word in months_in_year:
                    mdy[0] = months_in_year[word]
                    mdy[1] = mdy[1].replace(',', '')
        elif '/' in mdy:
                mdy = mdy.split('/')
        else:
            continue
        
        try:
            month, date, year = map(int, mdy)
            if month not in range(1, 13) or date not in range(1, 32):
                continue
        except (IndexError, ValueError):
            continue
        else:
            break

    conversion = f'{year:04}-{month:02}-{date:02}'
    print(conversion)

main()