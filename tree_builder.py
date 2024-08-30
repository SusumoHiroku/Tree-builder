from collections import defaultdict


def to_tree(source):
    # Создаем словарь для хранения потомков каждого узла
    tree = defaultdict(dict)
    # Словарь для родительских ссылок
    nodes = {}

    # Инициализация узлов в дереве
    for parent, child in source:
        # Если узел не существует в nodes, создаем его
        if child not in nodes:
            nodes[child] = tree[child]

        # Если родитель не None, связываем с родителем
        if parent is not None:
            if parent not in nodes:
                nodes[parent] = tree[parent]
            nodes[parent][child] = nodes[child]

    # Выделяем только корневые узлы (с parent == None)
    result = {child: nodes[child] for parent, child in source if parent is None}

    return result


# Пример использования
source = [
    (None, 'a'),
    (None, 'b'),
    (None, 'c'),
    ('a', 'a1'),
    ('a', 'a2'),
    ('a2', 'a21'),
    ('a2', 'a22'),
    ('b', 'b1'),
    ('b1', 'b11'),
    ('b11', 'b111'),
    ('b', 'b2'),
    ('c', 'c1'),
]

expected = {
    'a': {'a1': {}, 'a2': {'a21': {}, 'a22': {}}},
    'b': {'b1': {'b11': {'b111': {}}}, 'b2': {}},
    'c': {'c1': {}},
}


assert to_tree(source) == expected
print("Функция работает корректно")


def run_tests():
    # Тест 1: Простой случай с одним корнем и несколькими потомками
    source_1 = [
        (None, 'root'),
        ('root', 'child1'),
        ('root', 'child2'),
    ]
    expected_1 = {
        'root': {'child1': {}, 'child2': {}}
    }
    assert to_tree(source_1) == expected_1

    # Тест 2: Случай с несколькими уровнями вложенности
    source_2 = [
        (None, 'root'),
        ('root', 'child1'),
        ('child1', 'child1_1'),
        ('child1_1', 'child1_1_1'),
    ]
    expected_2 = {
        'root': {'child1': {'child1_1': {'child1_1_1': {}}}}
    }
    assert to_tree(source_2) == expected_2

    # Тест 3: Случай с несколькими корневыми узлами и разной глубиной
    source_3 = [
        (None, 'a'),
        (None, 'b'),
        ('a', 'a1'),
        ('a', 'a2'),
        ('a2', 'a21'),
        ('b', 'b1'),
        ('b1', 'b11'),
    ]
    expected_3 = {
        'a': {'a1': {}, 'a2': {'a21': {}}},
        'b': {'b1': {'b11': {}}}
    }
    assert to_tree(source_3) == expected_3

    # Тест 4: Случай без корневых узлов (неправильные данные)
    source_4 = [
        ('x', 'y'),
        ('y', 'z'),
    ]
    expected_4 = {}  # Нет корневых узлов, должно быть пустое дерево
    assert to_tree(source_4) == expected_4

    # Тест 5: Случай с несколькими независимыми деревьями
    source_5 = [
        (None, 'root1'),
        ('root1', 'child1'),
        (None, 'root2'),
        ('root2', 'child2'),
    ]
    expected_5 = {
        'root1': {'child1': {}},
        'root2': {'child2': {}}
    }
    assert to_tree(source_5) == expected_5

    print("Все тесты пройдены успешно!")

run_tests()


