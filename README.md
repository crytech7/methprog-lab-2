# methprog-3-year
```
  #  =====================================================================================================
  # 	 ﾞ☆ﾞ            ﾞ☆ﾞ            ﾞ☆ﾞ            ﾞ☆ﾞ            ﾞ☆ﾞ            ﾞ☆ﾞ
  #   ／|、         ﾞ☆ﾞ            ﾞ☆ﾞ            ﾞ☆ﾞ            ﾞ☆ﾞ            ﾞ☆ﾞ            ﾞ☆ﾞ
  # （ﾟ､ ｡ つ               ﾞ☆ﾞ             ﾞ☆ﾞ               ﾞ☆ﾞ            ﾞ☆ﾞ              ﾞ☆ﾞ              ﾞ☆ﾞ
  #  |、ﾞ  ヽ        ﾞ☆ﾞ            ﾞ☆ﾞ            ﾞ☆ﾞ            ﾞ☆ﾞ            ﾞ☆ﾞ            ﾞ☆ﾞ
  #  じーし__ )つ            ﾞ☆ﾞ            ﾞ☆ﾞ            ﾞ☆ﾞ            ﾞ☆ﾞ            ﾞ☆ﾞ            ﾞ☆ﾞ
  #  =====================================================================================================
  #  МЕТОДЫ ПРОГРАММИРОВАНИЯ | LAB 2 01.04.2023 | ВАРИАНТ 12
  #  by crytech7
  #  =====================================================================================================
  #  > ВАРИАНТ 12:
  # 	Массив данных о командах, принимающих участие в  чемпионате страны по футболу:
  # 	страна, название клуба,  город, год, ФИО главного тренера
  # 	(сравнение по полям – год, страна, количество набранных очков (по убыванию), название клуба):

  #       Country,Club Name,City,Year,Coach Name,Points

  #  > СОРТИРОВКИ:
  # 	г) Шейкер-сортировка
  # 	д) Пирамидальная сортировка
  # 	е) Быстрая сортировка
  #  ====================================================================================================
```
1) Реализовать прямой и бинарный поиск заданного элемента в массиве объектов по ключу в соответствии с вариантом (ключом является первое НЕ числовое поле объекта). 

2) Входные данные для поиска обязательно считывать из  внешних источников: текстовый файл, файл MS Excel, данные из СУБД (любое на выбор).

3) Выполнить поиск 7-10 раз на массивах разных размерностей от 100 и более. Засечь (программно) время поиска для следующих способов: прямой поиск, бинарный поиск в заранее отсортированном массиве, сортировка массива (наиболее эффективным методом из работы 1) и бинарный поиск в нем. По полученным точкам построить графики зависимости времени поиска от размерности массива.

4) Записать входные данные в ассоциативный массив multimap<key, object> и сравнить время поиска по ключу в нем с временем поиска из п.3. Добавить данные по времени поиска в ассоциативном массиве в общее сравнение с остальными способами и построить график зависимости времени поиска от размерности массива.

## Visual

![Alt text](https://github.com/crytech7/methprog-lab-2/blob/main/bin_lin_presorted.png "Presorted bin search")

## Usage
```
  git clone https://github.com/crytech7/methprog-lab-2
  cd methprog-lab-2
  python3 generate.py
  python3 main.py
  python3 do_graphs.py
```
## Note
Multimap search was done in C++, thus python implementations are bad. To get results:
```
  g++ main.cpp
  ./a.out
```

HTML Report was generated using pdoc. Index page was manually edited to place images and links
```
  pip3 install pdoc3
  pdoc --html .
```
