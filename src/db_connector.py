from abc import ABC, abstractmethod
from os import path, mkdir
import json

from config import ROOT_DIR


class AbstractDBConnector(ABC):
    @abstractmethod
    def add_vacancy(self, vacancy):
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy):
        pass

    @abstractmethod
    def get_vacancies(self, selections: tuple):
        pass


class DBConnector(AbstractDBConnector):
    """
    Класс добавляет в json вакансии
    получает данные из файла по указанным критериям,
    удаляет вакансии по URL
    """

    def __init__(self, file_json: str):
        self.file_json = path.join(ROOT_DIR, "data", file_json)

    def read(self) -> list:
        """Читает json и возвращает данные"""

        data_folder = path.join(ROOT_DIR, "data")
        if not path.exists(data_folder):
            mkdir(data_folder)

        try:
            with open(self.file_json, "r", encoding="UTF-8") as file:
                try:
                    data = json.load(file)
                except json.JSONDecodeError:
                    return []  # Если файл пустой, возвращаем пустой список
        except FileNotFoundError:
            with open(self.file_json, "w", encoding="UTF-8") as file:
                file.write("[]")
            return []  # Если файл отсутствует, создаем его и возвращаем пустой список
        else:
            return data

    def save(self, data: list):
        """Записывает данные в файл json"""
        json_data = json.dumps(data, ensure_ascii=False)
        with open(self.file_json, "w", encoding="UTF-8") as file:
            file.write(json_data)

    def add_vacancy(self, vacancy):
        """
        Принимает экземпляр класса vacancy,
        дописывает все атрибуты __slots__ с их значениями в json-файл
        """

        data = self.read()
        item = {attr: vacancy.__getattribute__(attr) for attr in vacancy.__slots__}
        data.append(item)
        self.save(data)

    def delete_vacancy(self, vacancy):
        """
        Принимает экземпляр класса vacancy,
        удаляет первую попавшуюся запись, которая соответствует вакансии по ключу URL
        """

        data = self.read()
        item = None
        for vac in data:
            if vac["url"] == vacancy.url:
                item = vac
                break
        if item:
            data.remove(item)
        self.save(data)

    def get_vacancies(self, keys: list) -> list:
        """
        Принимает список ключевых слов, по которым нужно отобрать вакансии из файла.
        Возвращает данные в виде списка словарей
        """

        def is_valid_from_key(item: dict, key: str):
            """Определяет, проходит ли вакансия по заданному ключу"""
            for value in item.values():
                if isinstance(value, str) and key.lower() in value.lower():
                    return True
            return False

        def is_valid_from_keys(item: dict, keys: list):
            """Определяет, проходится ли вакансия по НАБОРУ ключей"""
            for key in keys:
                if not is_valid_from_key(item, key):
                    return False
            return True

        data = self.read()

        new_data = []
        for vac in data:
            if is_valid_from_keys(vac, keys):
                new_data.append(vac)

        return new_data