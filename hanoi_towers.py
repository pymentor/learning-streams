class Stack:
    def __init__(self, name):
        self._name = name
        self._container = list()

    def push(self, element):
        self._container.append(element)

    def pop(self):
        return self._container.pop()

    @property
    def is_empty(self):
        return bool(self._container)

    def __repr__(self):
        return f"Stack {self._name}"


class Ring:
    def __init__(self, size):
        self._size = size

    def __str__(self):
        return f"Ring {self._size}"

    def __repr__(self):
        return self.__str__()


def hanoi(start_tower, end_tower, temp_tower, n):
    global number_of_calls
    number_of_calls += 1
    if n == 1:
        elem = start_tower.pop()
        print(f"{elem}: {start_tower} -> {end_tower}")
        end_tower.push(elem)
    else:
        hanoi(start_tower, temp_tower, end_tower, n-1)
        hanoi(start_tower, end_tower, temp_tower, 1)
        hanoi(temp_tower, end_tower, start_tower, n-1)


number_of_calls = 0
N = 3

green_tower = Stack("green")  # initial start tower
red_tower = Stack("red")  # initial temp tower
blue_tower = Stack("blue")  # initial finish tower

for i in range(N):
    green_tower.push(Ring(i))


# 1) перемещаем верхние n-1 колец из green в red используя blue в качестве промежуточной
# 2) перемещаем нижнее кольцо из green в blue
# 3) перемещаем n-1 колец из red в blue используя башню green как промежуточную


hanoi(green_tower, blue_tower, red_tower, N)
print(number_of_calls)
