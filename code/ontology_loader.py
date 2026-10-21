from pathlib import Path
from rdflib import Graph, Namespace, RDF, RDFS, Literal

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
OSS_SOM = Namespace(namespace_uri)

# Создаем новый репозиторий (экземпляр класса SoftwareProduct)
repo1_uri = OSS_SOM.Repo1
g.add((repo1_uri, RDF.type, OSS_SOM.SoftwareProduct))
g.add((repo1_uri, RDFS.label, Literal("Repo1")))

# Проверяем, что данные добавлены
print("\nДобавленные данные для Repo1:")
nm = g.namespace_manager
for s, p, o in g.triples((repo1_uri, None, None)):
    print(f"  {s.n3(nm)} -> {p.n3(nm)} -> {o.n3(nm)}")

