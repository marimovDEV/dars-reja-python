# 🎨 50. CSS3 Styling, Flexbox va Grid Layout — Dars dokumentatsiyasi

**CSS3 (Cascading Style Sheets)** — bu HTML teglarga ko'rinish, rang, shrift va joylashuv tartibini (layout) berish uchun ishlatiladigan uslublar tilidir.

---

## Asosiy CSS va Flexbox Misoli

```css
/* Asosiy uslublar */
body {
    font-family: 'Inter', sans-serif;
    background-color: #f8fafc;
    color: #0f172a;
    margin: 0;
    padding: 0;
}

/* Flexbox Konteyner */
.card-container {
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 20px;
    padding: 40px;
}

.card {
    background: #ffffff;
    border-radius: 12px;
    padding: 24px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
    flex: 1;
}
```

Keyingi **51-dars: Bootstrap 5 Framework** da tayyor dizayn komponentlari bilan ishlashni o'rganamiz.
