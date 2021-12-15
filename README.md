# iut-dt-cw

Теория принятия решений (Курсовая работа)

Для работы с большими знаменателями у дробей нужны изменения в fractions, т.к. numpy пихает свои int64 и может произойти
переполнение

```python
    na, da = a.numerator, a.denominator
nb, db = b.numerator, b.denominator
```

```python
    na, da = int(a.numerator), int(a.denominator)
nb, db = int(b.numerator), int(b.denominator)
```
