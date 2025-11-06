# Python Labs

____
## Условие задачи:
Задание 5. 

Рациональные числа являются счетным множеством.
Реализовать генератор, выдающий все рациональные числа по одному разу.

Таким образом, генератор должен проходить все рациональные числа, пропуская те, что могут быть сокращены до уже пройденных, например:

$$\frac{1}{2} \rightarrow \frac{1}{3} \rightarrow \frac{2}{3} \rightarrow \frac{1}{4} \rightarrow  \frac{3}{4} \rightarrow ... $$

____
## Установка виртуального окружения и запуск
### 1. Клонируйте репозиторий
```bash
git clone git@github.com:Python-Team-25-26/rational-numbers.git
cd rational-numbers
```
### 2. Создайте виртуальное окружение
```bash
python -m venv venv
```
### 3. Активируйте виртуальное окружение
- **Windows CMD**
```bash
.\venv\Scripts\activate
```
- **macOS/Linux**
```bash
source venv/bin/activate
```
После активации виртуального окружения в командной строке появится префикс venv.
### 4. Запустите программу
```bash
python rational-numbers.py
```