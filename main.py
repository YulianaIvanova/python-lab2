import json
import re
import argparse
from tqdm import tqdm

class Data:
    '''
        Объект класса Data содержит характеристики одного человека

        Attributes
        -----------------------------------------------------------------
            __telephone: str
                Номер телефона – строка, объектное свойство класса Data.
            __height: str
                Рост – строка, объектное свойство класса Data.
            __snils: str
                Номер СНИЛСа – строка, объектное свойство класса Data.
            __passport_series: str
                Серия паспорта – строка, объектное свойство класса Data.
            __occupation: str
                Название работы – строка, объектное свойство класса Data.
            __age: str
                Возраст – строка, объектное свойство класса Data.
            __political_views: str
                Политические взгляды – строка, объектное свойство класса Data.
            __worldview: str
                Мировоззрение – строка, объектное свойство класса Data.
            __address: str
                Адрес проживания – строка, объектное свойство класса Data.
    '''
    def __init__(self, telephone: str, height: str or float, snils: str, passport_series: str, occupation: str,
                 age: int, political_views: str, worldview: str,
                 address: str) -> None:
        '''
        Инициализирует экземпляр класса Data.

        Parameters
        -------------------------------------------
        telephone: str
        Строка; номер телефона

        height: str or int
        Строка/число с плавающей точкой; рост

        snils: str
        Строка; номер СНИЛСа

        passport_series: str
        Строка; серии паспорта

        occupation: str
        Строка; название работы

        age: int
        Целое число; возраст

        political_views: str
        Строка; политические взгляды

        worldview: str
        Строка; мировоззрение

        address: str
        Строка; адресс
        '''
        self.__telephone = telephone
        self.__height = str(height)
        self.__snils = snils
        self.__passport_series = passport_series
        self.__occupation = occupation
        self.__age = str(age)
        self.__political_views = political_views
        self.__worldview = worldview
        self.__address = address



    @property
    def telephone(self) -> str:
       '''
       Возвращает __telephone – объектное свойство класса Data.
       Returns
       --------------------------
       str:
          Строка __telephone.
       '''
       return self.__telephone

    @property
    def height(self) -> str:
        '''
        Возвращает __height – объектное свойство класса Data.
        Returns
        --------------------------
        str:
            Строка __height.
        '''
        return self.__height

    @property
    def snils(self) -> str:
        '''
        Возвращает __snils – объектное свойство класса Data.
        Returns
        --------------------------
        str:
           Строка __snils.
        '''
        return self.__snils

    @property
    def passport_series(self) -> str:
        '''
        Возвращает __passport_series – объектное свойство класса Data.
        Returns
        --------------------------
        str:
            Строка __passport_series.
        '''
        return self.__passport_series

    @property
    def occupation(self) -> str:
        '''
        Возвращает __occupation – объектное свойство класса Data.
        Returns
        --------------------------
        str:
            Строка __occupation.
        '''
        return self.__occupation

    @property
    def age(self) -> str:
        '''
        Возвращает __age – объектное свойство класса Data.
        Returns
        --------------------------
        str:
            Строка __age.
        '''
        return self.__age

    @property
    def political_views(self) -> str:
        '''
        Возвращает __political_views – объектное свойство класса Data.
        Returns
        --------------------------
        str:
            Строка __political_views.
        '''
        return self.__political_views

    @property
    def worldview(self) -> str:
        '''
        Возвращает __worldview – объектное свойство класса Data.
        Returns
        --------------------------
        str:
            Строка __worldview.
        '''
        return self.__worldview

    @property
    def address(self) -> str:
        '''
        Возвращает __address – объектное свойство класса Data.
        Returns
        --------------------------
        str:
            Строка __address.
        '''
        return self.__address

    def all_data(self) -> dict:
        '''
        Возвращает словарь со всеми объектными свойствами класса Data.
        Returns
        ---------------------------------------------------------
        dict:
            Словарь вида:
                       {'telephone':self.__telephone, 'height': self.__height, 'snils': self.__snils ...'.}

        '''
        key = ["telephone", "height", "snils", "passport_series", "occupation", "age", "political_views", "worldview",
               "address"]
        data_list = [self.__telephone, self.__height, self.__snils, self.__passport_series, self.__occupation,
                     self.__age, self.__political_views, self.__worldview, self.__address]
        return dict(zip(key, data_list))

class Validator(Data):
    '''
    Объект класса содержит объект класса Data.

    Attributes
    -------------------------------------------
            __obj: Data
                Объект класса Data.
    '''
    def __init__(self, obj: Data) -> None:
        '''
        Инициализирует экземпляр класса validator.

        Parameters
        --------------------------------------
            obj: Data
                Объект класса Data.
        '''
        self.__obj = obj

    def check_telephone(self, obj) -> bool:
        '''
            Выполняет проверку корректности записи __telephone – объектного свойства объекта класса Data.

            Если строка __telephone соответствует типу '+7-(xxx)-xxx-xx-xx',
            где x – число от 0 до 9, будет возвращено True, иначе – False.

            Returns
            ---------------------------------------------------
                    bool:
                        Булевый результат проверки на корректность.
        '''
        pattern = r"^\+7\D*\d{3}\D*\d{3}\D*\d{2}\D*\d{2}"
        if re.match(pattern, obj.telephone):
            return True
        return False

    def check_height(self, obj) -> bool:
        '''
            Выполняет проверку корректности записи __height – объектного свойства объекта класса Data.

            Если __height - число с плавающей точкой, начинается с 1 или с 2, будет возвращено True, иначе – False.

            Returns
            ---------------------------------------------------
                    bool:
                         Булевый результат проверки на корректность.
        '''
        pattern = r"[1-2]\.\d{2}"
        if re.match(pattern, obj.height):
            return True
        return False

    def check_snils(self, obj) -> bool:
        '''
           Выполняет проверку корректности записи __snils – объектного свойства объекта класса Data.

           Если строка __snils состоит из 11 цифр от 0 до 9, будет возвращено True, иначе – False.

           Returns
           ---------------------------------------------------
                    bool:
                        Булевый результат проверки на корректность.
        '''
        pattern = r"\d{11}"
        if re.match(pattern, obj.snils):
            return True
        return False

    def check_passport_series(self, obj) -> bool:
        '''
            Выполняет проверку корректности записи __passport_series – объектного свойства объекта класса Data.

            Если строка __passport_series соответствует типу хх хх, где х - цифра от 0 до 9,
             будет возвращено True, иначе – False.

            Returns
            ---------------------------------------------------
                    bool:
                        Булевый результат проверки на корректность.
        '''
        pattern = r"\d{2}\ \d{2}"
        if re.match(pattern, obj.passport_series):
            return True
        return False

    def check_occupation(self, obj) -> bool:
        '''
            Выполняет проверку корректности записи __occupation – объектного свойства объекта класса Data.

            Если строка __occupation соответствует типу {x}, где х - слово/а(если в названии профессии есть тире и пробел)
            состоящие/я из букв английского или русского алфавитов,будет возвращено True, иначе – False.

            Returns
            ---------------------------------------------------
                     bool:
                         Булевый результат проверки на корректность.
        '''
        pattern = r"[A-Za-z\ А-Яа-я-ё]+"
        if re.match(pattern, obj.occupation):
            return True
        return False

    def check_age(self, obj) -> bool:
        '''
            Выполняет проверку корректности записи __age – объектного свойства объекта класса Data.

            Если __age - целое число, удовлетворяющее виду xy, где x - цифра от 1 до 9, y - цифра от 0 до 9,
            будет возвращено True, иначе – False.

            Returns
            ---------------------------------------------------
                  bool:
                        Булевый результат проверки на корректность.
        '''
        pattern = r"[1-9]+[0-9]"
        if re.match(pattern, obj.age):
            return True
        return False

    def check_political_views(self, obj) -> bool:
        '''
            Выполняет проверку корректности записи __political_views – объектного свойства объекта класса Data.

            Если строка __political_views - удовлетворяет одному из допустмых значений,будет возвращено True, иначе – False.
            Допустимые значения для __political_views:
            -Либертарианские
            -Социалистические
            -Умеренные
            -Анархистские
            -Либеральные
            -Консервативные
            -Индифферентные
            -Коммунистические

            Returns
            ---------------------------------------------------
                    bool:
                        Булевый результат проверки на корректность.
        '''
        pattern = r"Либертарианские|Социалистические|Умеренные|Анархистские|Либеральные|Консервативные|Индифферентные|Коммунистические"
        if re.match(pattern, obj.political_views):
            return True
        return False

    def check_worldview(self, obj) -> bool:
        '''
            Выполняет проверку корректности записи __worldview – объектного свойства объекта класса Data.

            Если строка __worldview - удовлетворяет одному из допустмых значений,будет возвращено True, иначе – False.
            Допустимы значения для __worldview:
            -Пантеизм
            -Конфуцианство
            -Секулярный гуманизм
            -Иудаизм
            -Деизм
            -Агностицизм
            -Буддизм
            -Католицизм
            -Атеизм
            -Культ пророка Лебеды
            -Культ богини Мелитэле

            Returns
            ---------------------------------------------------
                    bool:
                        Булевый результат проверки на корректность.
        '''
        pattern = r"Пантеизм|Конфуцианство|Секулярный гуманизм|Иудаизм|Деизм|Агностицизм|Буддизм|Католицизм|Атеизм|Культ пророка Лебеды|Культ богини Мелитэле"
        if re.match(pattern, obj.worldview):
            return True
        return False

    def check_address(self, obj) -> bool:
        '''
            Выполняет проверку корректности записи __worldview – объектного свойства объекта класса Data.

            Если строка __worldview соответстувет типу  a b сd
            где:
            a - Аллея или ул.
            b - название аллеи или улицы,состоящие из одного или двух слов,также может начинаться с цифры
            с - d-я или dбуква или d км,где в d - цифра от 0 до 9
            d - целое число, номер дома
            будет возвращено True, иначе – False.


            Returns
            ---------------------------------------------------
                    bool:
                        Булевый результат проверки на корректность.
        '''
        pattern = r"(?:Аллея |ул\. ){1}[0-9]*\D+(?:[1-9]*-я |[0-9]+[а-я] |[0-9]* км )?[0-9]*$"
        if re.match(pattern, obj.address):
            return True
        return False



parser = argparse.ArgumentParser(description="main")
parser.add_argument(
    "-input",
    type=str,
    help="Это обязательный строковый позиционный аргумент, который указывает, с какого файла будут считаны данные",
    dest="file_input")
parser.add_argument(
    "-output",
    type=str,
    help="Это необязательный позиционный аргумент, который указывает, куда будут сохранены валидные данные",
    dest="file_output")
args = parser.parse_args()
save_data = []
file = json.load(open(args.file_input, encoding='windows-1251'))
output = open(args.file_output, 'w', encoding='windows-1251')

counter_valid = 0
counter_invalid = 0
invalid_data = {'telephone': 0,
                'height': 0,
                'snils': 0,
                'passport_series': 0,
                'occupation': 0,
                'age': 0,
                'political_views': 0,
                'worldview': 0,
                'address': 0}


with tqdm(file, desc='Валидация записей') as progressbar:
    for _file in file:
        d = Data(_file['telephone'], _file['height'], _file['snils'],
                 _file['passport_series'], _file['occupation'], _file['age'],
                 _file['political_views'], _file['worldview'], _file['address'])
        v = Validator(d)
        tmp_valid_data = 0

        if (v.check_telephone(d) == True):
           tmp_valid_data += 1
        else:
            invalid_data['telephone'] += 1

        if (v.check_height(d) == True):
           tmp_valid_data += 1
        else:
           invalid_data['height'] += 1

        if (v.check_snils(d) == True):
           tmp_valid_data += 1
        else:
           invalid_data['snils'] += 1

        if (v.check_passport_series(d) == True):
           tmp_valid_data += 1
        else:
            invalid_data['passport_series'] += 1

        if (v.check_occupation(d) == True):
            tmp_valid_data += 1
        else:
            invalid_data['occupation'] += 1

        if (v.check_age(d) == True):
           tmp_valid_data += 1
        else:
            invalid_data['age'] += 1

        if (v.check_political_views(d) == True):
            tmp_valid_data += 1
        else:
            invalid_data['political_views'] += 1

        if (v.check_worldview(d) == True):
            tmp_valid_data += 1
        else:
            invalid_data['worldview'] += 1

        if (v.check_address(d) == True):
            tmp_valid_data += 1
        else:
            invalid_data['address'] += 1

        if (tmp_valid_data == 9):
            save_data.append(d.all_data())
            counter_valid += 1
        else:
            counter_invalid += 1
        progressbar.update(1)
improved_data = json.dumps(save_data, ensure_ascii=False, indent=4)
output.write(improved_data)
output.close()

print("Статистика обработанных данных: \n1.Число валидных записей: " + str(counter_valid) +
      "\n2.Общее число невалидных записей: " + str(counter_invalid))
print("Число невалидных записей по типам ошибок: \n1.Число невалидных номеров телефона: " +
      str(invalid_data['telephone']) + "\n2.Число невалидных ростов: " + str(invalid_data['height']) +
      "\n3.Число невалидных записей СНИЛС: " + str(invalid_data['snils']) + "\n4.Число невалидных серий паспорта: " +
      str(invalid_data['passport_series']) + "\n5.Число невалидных записей профессий: " + str(invalid_data['occupation']) +
      "\n6.Число невалидных записей возраста: " + str(invalid_data['age']) + "\n7.Число невалидных записей политических взглядов:" +
      str(invalid_data['political_views']) + "\n8.Число невалидных записей мировоззрений: " + str(invalid_data['worldview']) +
      "\n9.Число невалидных адрессов: " + str(invalid_data['address']))
