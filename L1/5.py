class StackClass:
    def __init__(self):
        self.plates = [[]]

    def is_empty(self):
        return self.plates == [[]]

    def push_in(self, el):
        if len(self.plates[0]) // 5 == 1:
            self.plates.insert(0, [])
        self.plates[0].insert(0, el)

    def pop_out(self):
        return self.plates[0].pop(0)

    def get_val(self):
        return self.plates[0][0]

    def stack_size(self):
        return len(self.plates[0])


stack_plates = StackClass()
print(stack_plates.is_empty())  # проверяем на пустоту
# кладем тарелки с делением на стопки по 5 тарелок
stack_plates.push_in(1)
stack_plates.push_in(2)
stack_plates.push_in(3)
stack_plates.push_in(4)
stack_plates.push_in(5)
stack_plates.push_in(6)
stack_plates.push_in(7)
print(stack_plates.get_val())  # получаем номер первой тарелки с вершины стопки
print(stack_plates.stack_size())  # узнаем размер последней стопки
print(stack_plates.is_empty())  # снова проверяем на пустоту
stack_plates.push_in(8)  # кладем еще одну тарелку в стопку
print(stack_plates.pop_out())  # убираем тарелку с вершины стопки и возвращаем ее номер
print(stack_plates.stack_size())  # узнаем размер последней стопки
print(stack_plates.plates)  # получаем все стопки
