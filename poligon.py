def basket(name, quantity):
    f = open('static/dist/basket.txt', 'r')
    basket = ''
    for i in f:
        basket += i
    f.close()
    if name in basket:
        if ((name + ' - ' + quantity) in basket) == False:
            start = basket.find(name)
            end = basket.find("\n", start)
            f = open('static/dist/basket.txt', 'w')
            f.write(basket[:start])
            f.write(basket[end+1:])
            f.write(name + ' ' + quantity + ' шт\n')
        else:
            f = open('static/dist/basket.txt', 'r')
    else:
        f = open('static/dist/basket.txt', 'a')
        f.write(name + ' ' + quantity + ' шт\n')
    f.close()
    basket = ''
    return 0



def main():
    while(True):
        cmd = input().split()
        basket(cmd[0], cmd[1])
        f = open('static/dist/basket.txt', 'r')
        for i in f:
            print(i)
        print('*' * 15)







if __name__ == "__main__":
    main()