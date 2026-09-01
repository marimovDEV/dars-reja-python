# 🏆 30. OOP Mini-Loyiha — Dars dokumentatsiyasi

Ushbu dars OOP modulidagi barcha bilimlarni (Class, Object, `__init__`, Inkapsulyatsiya, Vorislik, Polimorfizm, Magic Methods) amaliyotda birlashtiruvchi **Mini-Loyiha: Bank Boshqaruvi va Foydalanuvchilar Tizimi**ga bag'ishlanadi.

Loyiha arxitekturasi bir-biri bilan bog'langan klasslardan tashkil topadi.

---

## Loyiha Arxitekturasi

1. **`User` (Ota Klass)**: Barcha foydalanuvchilar uchun umumiy (ism, email).
2. **`Customer` (Bola Klass)**: Bank mijozlari, shaxsiy bank hisobiga (`BankAccount`) ega.
3. **`BankAccount`**: Balansni inkapsulyatsiya qiladi (Private `__balance`), depozit va pul yechish amallari.
4. **`BankSystem`**: Barcha mijozlar va hisoblarni boshqaruvchi asosiy tizim.

---

# Kod Implementatsiyasi

```python
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.__balance = balance # Private

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return True
        return False

    def __str__(self):
        return f"Hisob [{self.account_number}]: Balans = ${self.__balance}"

class Customer(User):
    def __init__(self, name, email, account_number, initial_balance=0):
        super().__init__(name, email)
        self.account = BankAccount(account_number, initial_balance)

    def __str__(self):
        return f"Mijoz: {self.name} | {self.account}"

# Test qilish
c1 = Customer("Ali Valiyev", "ali@mail.com", "ACC1001", 500)
c1.account.deposit(200)
c1.account.withdraw(100)

print(c1)
print("Haqiqiy balans:", c1.account.get_balance())
```

---

# 10. Qisqa xulosa

Ushbu mini-loyiha orqali OOP ning barcha 4 ustuni va amaliy qo'llanilishi to'liq mustahkamlandi.
