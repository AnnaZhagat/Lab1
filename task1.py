import doctest


class Socks:
    def __init__(self, colour: str, size: (int, float)):
        """
        Создание и подготовка к работе объекта "Носки"

        :param colour: Цвет пары носков
        :param size: Размер носков по Российскому стандарту

        Примеры:
            socks = Socks('Красные', 23)  # инициализация экземпляра класса
        """
        self.colour = None
        if not isinstance(colour, str):  #
            raise TypeError("Цвет указывается в текстовом виде")
        self.colour = colour

        self.size = None
        if size <= 0:
            raise ValueError("Размер носков долже быть положительным числом")
        if not isinstance(size, (int, float)):
            raise TypeError("Размер является целым или десятичным числом")
        if size < 16 or size > 48 or (size * 2) % 1 != 0:
            raise ValueError("Размер носков должен быть в промежутке от 16 до 48, а также быть кратным 0.5")
        self.size = size

    def stirka(self) -> None:
        """
        Функция отвечает за "усадку" носков при стирке. Размер уменьшается на 1.

        Примеры:
             socks = Socks('Красные', 23.5)
             socks.stirka()  -- Носки сели, размер уменьшился на 1
        """
        self.size -= 1

    def syshka(self) -> None:
        """
         Функция отвечает за "выцветание" носков при сушке под палящим солнцем. Цвет становится бледнее.

        Примеры:
                socks = Socks('Красные', 23.5)
                socks.syshka()  -- Носки сушились на сонце, цвет стал бледнее
        """
        self.colour = 'Бледно-' + self.colour.lower()

    def __str__(self) -> str:
        """
            Функция возвращает строку с характеристиками экземлпяра в удобном для польхователя формате
        """
        return f'{self.colour} носки {self.size} размера'


class Kopilka:
    def __init__(self, max_capacity: int, coins: dict):
        """
         Создание и подготовка к работе объекта "Копилка"

        :param max_capacity: Максимальное колличество монет, которое поместится в копилку
        :param  coins: Словарь, ключами которого является номинал монеты, а значением - колличество монет
        Примеры:
             kopilka = Kopilka(100,{1: 5, 2: 7, 5: 3, 10: 2})  # инициализация экземпляра класса
        """

        self.amount_coins = 0
        self.summ = 0

        self.max_capacity = None
        self.init_max_capacity(max_capacity)
        self.coins = None
        self.init_coins(coins)

    def init_max_capacity(self, max_capacity: int) -> None:
        """
        Функция проверяет правильность ввода атрибута "вместимость копилки" (монеты, штуки).
        Введенное значение должно быть ЦЕЛЫМ и ПОЛОЖИТЕЛЬНЫМ числом

        :param max_capacity: Максимально колличество монет, которые могут поместиться в копилку (Вместимость)
        :return: None
        """
        if not isinstance(max_capacity, int):
            raise TypeError("Колличество монет, помещающихся в копилку, должно быть целым числом")
        if max_capacity <= 0:
            raise ValueError("Колличество монет, помещающихся в копилку,должно быть положительным числом")
        self.max_capacity = max_capacity

    def init_coins(self, coins: dict):
        """
        Функция проверяет правильность ввода атрибута "содержимое копилки " (номинал монеты, их кол-во).
        Введенное переменная должна быть СЛОВАРЕМ.
        Общее число монет не должно превышать вместимость копилки.
        Ключами словаря должны быть монеты номиналом (1,2,5,10) - других монет не существует

        :param coins: словарь, ключами которого являются номинал монет, а значением - колличество монет данного номинала
        :return: None
        """
        if not isinstance(coins, dict):
            raise TypeError("Переменная должна быть представленны в виде словаря")
        for i in coins.values():
            self.amount_coins += i
        if self.amount_coins > self.max_capacity:
            raise ValueError(
                f"Суммарное колличество монет в словаре превышает его вместимость ({self.amount_coins}) > {self.max_capacity}")
        for j in coins.keys():
            if j not in (1, 2, 5, 10):
                raise ValueError(f'Значение {j} не является допустимым номиналом монеты (1, 2, 5, 10)')
        self.coins = coins

    def count_summ(self) -> str:
        """
        Функция подсчитывает суммарное колличество денег, лежащих в копилке (рубли)

        :return: сумма значений всех монет
        """
        self.summ = 0
        for i in list(self.coins):
            self.summ += i * self.coins[i]
        return f'Сумма монет, лежащих в копилке - {self.summ} ₽'

    def count_amount_coins(self) -> str:
        """
        Функция подсчитывает колличество лежащих в копилке монет(штуки)
        :return: кол-во монет
        """
        return f'Суммарное колличество монет в копилке - {self.amount_coins} шт.'

    def add_coin(self, coin: int, count_coin=1) -> dict:
        """
        Функция добавляет в копилку еще одну (значение по умолчанию =1) или несколько монет


        :param coin: Вводится номинал монеты
        :param count_coin: Вводится колличество положенных монет, по умолчанию = 1
        :raise ValueError: Если введен несуществующий номинал монеты (например - 11,"3а0")
        :return: Обновленный словарь, содержащий новое колличество монет указанного номинала
        Если до этого в копилке не было таких монет (в словаре не было ключа) - он добавляется.
        """
        if coin not in (1, 2, 5, 10):
            raise ValueError("Монеты с таким номиналом не существует")

        self.coins[coin] = self.coins.get(coin, 0) + count_coin
        self.amount_coins += count_coin
        return self.coins


class SpisokPokupok:
    def __init__(self, spisok: list):
        """
        Создание и подготовка к работе объекта "Список покупок"
        :param spisok: список товаров (строки), без колличества

        :raise TypeError: Если переданный аргумент не является списком, вполучается ошибка
        """
        if not isinstance(spisok, list):
            raise TypeError('Параметр должен быть списком')
        self.spisok = spisok

    def add_item(self, item: str) -> list:
        """
        Функция добавляет ещё один товар в список покупок (проверка на дублирование не проводится)
        :param item: наименование товара (строка)
        :return: обновленный список покупок
        """
        self.spisok.append(item)
        return self.spisok

    def delete_item(self, item: str) -> list:
        """
        Функция ищет в списке покупок введенное наимнование товара
        Если такого наименование нет - выводится строка с предупреждением
        Если наименование входило в список более, чем 1 раз, удаляется первое включение его в список (наименьший индекс)

        :param item: наименование товара (строка)
        :return: обновленный список покупок
        """
        if item not in self.spisok:
            print(f'Товара "{item}" не было в списке')
        else:
            for i in self.spisok:
                if i == item:
                    self.spisok.pop(self.spisok.index(i))
        return self.spisok


if __name__ == "__main__":
    socks1 = Socks('Красные', 23.5)
    print(socks1)
    socks1.stirka()
    print(socks1)
    socks1.syshka()
    print(socks1)

    print()
    print('-' * 40)
    print()

    kopilka1 = Kopilka(100, {1: 5, 2: 10, 5: 2, 10: 3})
    print(f'Монеты, лежащие в копилке {kopilka1.coins}')
    print(kopilka1.count_summ())
    print(kopilka1.count_amount_coins())
    print('..' * 20)
    kopilka1.add_coin(5, 10)
    print(f'Монеты, лежащие в копилке {kopilka1.coins}')
    print(kopilka1.count_summ())
    print(kopilka1.count_amount_coins())

    print()
    print('-' * 40)
    print()

    spisok1 = SpisokPokupok(['огурцы', 'помидоры', 'кока-кола', 'творог', 'яйца'])
    print(spisok1.spisok)
    print(f"Новый список: {spisok1.add_item('вино')}")
    print(f"Новый список: {spisok1.delete_item('кокакола')}")

    doctest.testmod()  # тестирование примеров, которые находятся в документации

    pass
