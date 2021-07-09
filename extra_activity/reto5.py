""" Challenge """

# Stantdard lybraris
from math import ceil, sqrt


def read_file(path):
    """ Open up the file and clean the data, each row is casted into a list

    """
    data = []
    with open(path, 'r') as f:

        i = 0
        for line in f.readlines():

            if i != 0:

                line = line.split(",")  
                line[0], line[2], line[3], line[4] = int(line[0]), float(line[2]), int(line[3]), line[4][0]
                data.append(line)  

            i += 1

    return data


def filter_by_id(data, id_):
    """ Only takes the lists that have the id named
    """
    filter_data = []

    for d in data:

        if d[0] == id_:
            filter_data.append(d)

    return filter_data


def mean(data):
    """ Retrives the mean
    """
    return sum(data) /  len(data) 


def std(data):
    """ Retrives the stantdard
    """
    mean = sum(data) /  len(data)
    return sqrt((sum(list(map(lambda x: (x - mean) ** 2, data)))) / (len(data) - 1))


def main():
    data = read_file("data.csv")  
    ids = list(set(list(map(lambda x: int(x), input().split(' ')))))
    ids.sort()

    area_old = 4653  # Aqui debes asignar el valor del rango de las antenas previamente instaladas
    
    for id_ in ids:
        depart_data = filter_by_id(data, id_)
        
        acum_type_ant = {
            'a': 0,
            'b': 0,
            'c': 0,
            'd': 0,
            'e': 0
        }
        
        varea, vant_old, vtype_new = [d[2] for d in depart_data], [d[3] for d in depart_data], [d[4] for d in depart_data]

        for i in range(len(varea)):  

            area, ant_old, type_new = varea[i], vant_old[i], vtype_new[i]

            if type_new == "a" :

                acum_type_ant[type_new] += max(0, ceil((area - area_old * ant_old) / 11400)) 

            elif type_new == "b" : 

                acum_type_ant[type_new] += max(0, ceil((area - area_old * ant_old) / 12600))
                
            elif type_new == "c" :

                acum_type_ant[type_new] += max(0, ceil((area - area_old * ant_old) / 41100))  

            elif type_new == "d" : 
                
                acum_type_ant[type_new] += max(0, ceil((area - area_old * ant_old) / 14700)) 

            elif type_new == "e" : 

                acum_type_ant[type_new] += max(0, ceil((area - area_old * ant_old) /38000))  

        
        # The output 

                
        print(id_, depart_data[0][1])
        print('terrain area')
        print('mean {:.2f}'.format(mean(varea)))
        print('std {:.2f}'.format(std(varea)))
        print('min {:.2f}'.format(min(varea))) 
        print('max {:.2f}'.format(max(varea)))
        print('total {:.2f}'.format(sum(varea)))
        
        print('old antenna')
        print('mean {:.2f}'.format(mean(vant_old)))
        print('std {:.2f}'.format(std(vant_old)))
        print('min {:.0f}'.format(min(vant_old)))
        print('max {:.0f}'.format(max(vant_old)))  
        print('total {:.0f}'.format(sum(vant_old))) 
        
        print('new antenna')
        for i in acum_type_ant.items():
            print(f"{i[0]} {i[1]}")


if __name__ == "__main__":
    main()