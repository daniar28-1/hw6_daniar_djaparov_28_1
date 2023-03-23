class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    def __eq__(self, other):
        return self.__memory == other.__memory

    def __ne__(self, other):
        return self.__memory != other.__memory

    def __lt__(self, other):
        return self.__memory < other.__memory

    def __gt__(self, other):
        return self.__memory > other.__memory

    def __le__(self, other):
        return self.__memory <= other.__memory

    def __ge__(self, other):
        return self.__memory >= other.__memory

    def __str__(self):
        return f'cpu: {self.__cpu}, memory: {self.__memory}'
    @property
    def cpu(self):
        return self.__cpu

    @cpu.setter
    def cpu(self, value):
        self.__cpu = value

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, value):
        self.__memory = value

    def make_computations(self):
        return self.__cpu + self.__memory

class Phone:
    __sim_card_list = ['Beeline', 'O!', 'MegaCom']

    def __str__(self):
        return f'sim_card_list: {self.__sim_card_list}'

    @property
    def sim_card_list(self):
        return self.__sim_card_list

    @sim_card_list.setter
    def sim_card_list(self, value):
        self.__sim_card_list = value

    def call(self, sim_card_number, call_to_number):
        if sim_card_number == 1:
            print(f'Идет звонок на номер {call_to_number} с сим - карты {sim_card_number}{self.__sim_card_list[0]}')
        elif sim_card_number == 2:
            print(f'Идет звонок на номер {call_to_number} с сим - карты {sim_card_number}{self.__sim_card_list[1]}')
        elif sim_card_number == 3:
            print(f'Идет звонок на номер {call_to_number} с сим - карты {sim_card_number}{self.__sim_card_list[2]}')

class Smart_Phone(Computer,Phone):
    def __init__(self, cpu, memory):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self)

    def __str__(self):
        return super().__str__()


    def use_gps(self, location):
        print(f'Маршрут проложен до {location}')

computer = Computer(123, 256)
telephone = Phone()
smartphone1 = Smart_Phone(456, 126)
smartphone2 = Smart_Phone(34, 123)

print(computer)
print(telephone)
print(smartphone1)
print(smartphone2)

print(computer.make_computations())
print(telephone.call(1, 9965555555))
print(smartphone1.use_gps('Bishkek'))

print(computer == smartphone1)
print(smartphone1 != smartphone2)
print(computer < smartphone1)
print(computer > smartphone2)
print(smartphone1 >= smartphone2)
print(smartphone2 <= computer)































