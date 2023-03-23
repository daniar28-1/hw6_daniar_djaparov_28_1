
ten = list(range(1,11))

def gen_object(sequence=ten):
    while True:
        ind = input('enter index: (or "exit)')
        if ind == 'exit':
            print('finished...')
            break
        try:
            print(sequence[int(ind)])
        except:
            print('enter index from 0 to {len(sequence)-1}')

gen_object(list(range(1 , 101)))













