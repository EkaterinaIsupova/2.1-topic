from typing import Union


class Student:
    def __init__(self, name: str, age: int, assessment: Union[int, float]):
        """
        Создание и подготовка к работе объекта "Студент"

        :param name: имя студента
        :param age: возраст студента
        :param assessment: сумма всех баллов студента

        Примеры:
        >>> student = Student("Ivan", 21, 34.2)  # инициализация экземпляра класса
        """
        self.name = name

        if not isinstance(age, int):
            raise TypeError("Возраст студента должен быть типа int или float")
        if age < 0:
            raise ValueError("Возраст студента должен быть положительным числом")
        self.age = age

        if not isinstance(assessment, (int, float)):
            raise TypeError("Общий балл студента должен быть типа int или float")
        if assessment < 0:
            raise ValueError("Общий балл студента должен быть положительным числом")
        self.assessment = assessment

    def increase_the_age(self) -> None:
        """
        Функция, которая прибавляет возраст студента в день его рождения

        Примеры:
        >>> student = Student("Ivan", 21, 34.2)
        >>> student.increase_the_age()
        """
        self.age += 1

    def increase_the_assessment(self, add: Union[int, float]) -> None:
        """
        Функция, которая прибавляет к общему баллу студента балл за, например, реферат

        Примеры:
        >>> student = Student("Ivan", 21, 34.2)
        >>> student.increase_the_assessment(7.6)
        """
        if not isinstance(add, (int, float)):
            raise TypeError("Добавляемое количество баллов должно быть типа int или float")
        if add < 0:
            raise ValueError("Добавляемое количество баллов должно быть положительным числом")
        self.assessment += add


class Country:
    def __init__(self, name: str, square: Union[int, float], population: int):
        """
        Создание и подготовка к работе объекта "Страна"

        :param name: название страны
        :param square: площадь страны
        :param population: население страны

        Примеры:
        >>> сountry = Country("Russia", 17098246, 146980061)  # инициализация экземпляра класса
        """
        self.name = name

        if not isinstance(square, (int, float)):
            raise TypeError("Площадь страны должна быть типа int или float")
        if square < 0:
            raise ValueError("Площадь страны должен быть положительным числом")
        self.square = square

        if not isinstance(population, int):
            raise TypeError("Население страны должно быть только типа int")
        if square < 0:
            raise ValueError("Население страны должно быть положительным числом")
        self.population = population

    def change_the_square(self, add: Union[int, float]) -> None:
        """
        Функция, которая изменяет площадь страны, может увеличивать, может уменьшать

        Примеры:
        >>> сountry = Country("Russia", 17098246, 146980061)
        >>> сountry.change_the_square(-1245.3)
        """
        if not isinstance(add, (int, float)):
            raise TypeError("Добавочная площадь страны должна быть типа int или float")
        if abs(add) > self.square:
            raise ValueError("Добавочная площадь страны не должна превышать текущую площадь")
        self.square += add

    def change_the_population(self, add: int) -> None:
        """
        Функция, которая изменяет население страны, может увеличивать, может уменьшать

        Примеры:
        >>> сountry = Country("Russia", 17098246, 146980061)
        >>> сountry.change_the_population(155545)
        """
        if not isinstance(add, int):
            raise TypeError("Добавочное население страны должно быть только типа int")
        if abs(add) > self.population:
            raise ValueError("Добавочное население страны не должно превышать текущее население")
        self.population += add


class Square:
    def __init__(self, side_length: Union[int, float], color: str):
        """
        Создание и подготовка к работе объекта "Страна"

        :param side_length: длина стороны квадрата
        :param color: цвет квадрата

        Примеры:
        >>> square = Square(12, "red")  # инициализация экземпляра класса
        """
        if not isinstance(side_length, (int, float)):
            raise TypeError("Длина стороны квадрата должна быть типа int или float")
        if side_length < 0:
            raise ValueError("Длина стороны квадрата должна быть положительным числом")
        self.side_length = side_length

        self.color = color

    def increase_side_length(self, side_length_add: Union[int, float]) -> None:
        """
        Функция, которая увеличивает длину стороны квадрата

        Примеры:
        >>> square = Square(12, "red")
        >>> square.increase_side_length(15)
        """
        if not isinstance(side_length_add, (int, float)):
            raise TypeError("Добавочная длина стороны квадрата должна быть типа int или float")
        if side_length_add < 0:
            raise ValueError("Добавочная длина стороны квадрата должна быть положительным числом")
        self.side_length += side_length_add

    def reduce_the_length(self, side_length_reduction: Union[int, float]) -> None:
        """
        Функция, которая уменьшает длину стороны квадрата

        Примеры:
        >>> square = Square(12, "red")
        >>> square.reduce_the_length(5)
        """
        if not isinstance(side_length_reduction, (int, float)):
            raise TypeError("Убавочная длина стороны квадрата должна быть типа int или float")
        if side_length_reduction < 0:
            raise ValueError("Убавочная длина стороны квадрата должна быть положительным числом")
        if side_length_reduction > self.side_length:
            raise ValueError("Убавочная длина стороны квадрата не должна быть больше текущей длины стороны")
        self.side_length -= side_length_reduction


if __name__ == "__main__":
    import doctest
    doctest.testmod()
