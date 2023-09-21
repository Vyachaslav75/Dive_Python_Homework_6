from sys import argv


def check_date(date_input):
    ch_dt=[int(x) for x in date_input.split('.')] #date_input.split('.')
    print(ch_dt)
    if ch_dt[1]<1 or ch_dt[1]>12:
        return False
    if 1>ch_dt[2] or ch_dt[2]>9999:
        return False
    if 0<ch_dt[0]<32:
        if ch_dt[1] in [4, 6, 9, 11] and ch_dt[0]>30:
            return False
        elif ch_dt[1]==2:
            if check_vis(ch_dt[2]) and ch_dt[0]>29:
                return False
            elif not check_vis(ch_dt[2]) and ch_dt[0]>28:
                return False
    else:
        return False
    return True


def check_vis(ch_year):
    if ch_year%4==0:
        if ch_year%100==0:
            if ch_year%400==0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    
if __name__ == "__main__":
    if len(argv)==1:
        dt='30.2.2024'
    else:
        dt=argv[1]
    print(check_date(dt))