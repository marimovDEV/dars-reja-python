# 📱 52. Responsive Web Design va Mobile Layout — Dars dokumentatsiyasi

Mobil moslashuvchanlik (**Responsive Design**) — foydalanuvchi qaysi qurilmadan kirmasin (telefon, planshet yoki monitor) sayt ko'rinishining qulay saqlanishidir.

---

## CSS Media Queries Misoli

```css
/* Mobil qurilmalar uchun (max-width: 768px) */
@media (max-width: 768px) {
    .sidebar {
        display: none;
    }
    .main-content {
        width: 100%;
        padding: 15px;
    }
}
```

Keyingi **53-dars: Django Frameworkga Kirish** da ushbu HTML/CSS shablonlarni Django freymvorkiga ulashni boshlaymiz.
