
class Horse:
    def __init__(self):
        self.x_distance = 0
        self.sound = 'Frrr'

    def run(self, dx):
        """Метод для передвижения на dx по земле"""
        self.x_distance += dx



class Eagle:
    def __init__(self):
        self.y_distance = 0
        self.sound = 'I train, eat, sleep, and repeat'

    def fly(self, dy):
        """Метод для полёта на dy по высоте"""
        self.y_distance += dy


class Pegasus(Horse, Eagle):
    def __init__(self):
        Horse.__init__(self)
        Eagle.__init__(self)

    def move(self, dx, dy):
        """Метод для передвижения: вызывает run для перемещения по земле и fly для полёта"""
        self.run(dx)
        self.fly(dy)

    def get_pos(self):
        """Возвращает текущее положение Pegasus как кортеж (x_distance, y_distance)"""
        return self.x_distance, self.y_distance

    def voice(self):
        """Выводит звук, который издаёт Pegasus (звук наследуется от Eagle)"""
        print(self.sound)



p1 = Pegasus()
print(p1.get_pos())  # (0, 0)
p1.move(10, 15)
print(p1.get_pos())  # (10, 15)
p1.move(-5, 20)
print(p1.get_pos())  # (5, 35)
p1.voice() 
