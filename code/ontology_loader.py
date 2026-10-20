from pathlib import Path
from rdflib import Graph

file_path = Path("./model/oss-som.ttl")

# Создаем пустой граф
g = Graph()

# Проверяем, существует ли файл
if file_path.exists():
    print(f"Загрузка локальной онтологии из файла: {file_path.resolve()}...")
    g.parse(file_path, format="turtle")
else:
    print(f"Ошибка: Файл {file_path} не найден!")
    exit()

# находим namespace
detected_uri = None
for prefix, namespace_uri in g.namespaces():
    if prefix == "":
        detected_uri = namespace_uri
        break

print(f"Найдена namespace: {namespace_uri}")
