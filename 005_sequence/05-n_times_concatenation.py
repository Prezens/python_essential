"""
Используя операцию умножения на целое число, можно сконкатенировать вместе
заданное количество копий последовательности. Однако следует иметь в виду,
что эти копии являются так называемыми неполными копиями (shallow copies),
то есть копирование происходит нерекурсивно и если внутри объекта были
ссылки на другие объекты, то они будут указывать на те же объекты.
"""

print('*' * 80)
print([2, 3] * 10)
