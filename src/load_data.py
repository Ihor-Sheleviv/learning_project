def load_data(path,file):
    """ завантаження даних про товар """
    f = open(path+file, "r")
    goods_str = f.readline()
    f.close()
    goods = eval(goods_str)
    return goods
