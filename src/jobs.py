from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path) as file:
        file_content = csv.DictReader(file)
        print(file_content)
        return list(file_content)
