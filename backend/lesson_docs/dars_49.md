# 🌐 49. HTML5 Asoslari va Semantik Teglar — Dars dokumentatsiyasi

Veb ilovalar va saytlarning ko'rinishi hamda strukturasi **HTML5 (HyperText Markup Language)** yordamida hosil qilinadi. Har bir backend dasturchi Django yoki boshqa freymvorklarda ishlashdan oldin frontendning asosiy skeletini mukammal tushunishi shart.

---

## Bu mavzu orqali nimalar qilish mumkin

- Veb sahifa tayanch HTML strukturasi (`<!DOCTYPE html>`, `<html>`, `<head>`, `<body>`) ni tuzish;
- Semantik teglar (`<header>`, `<nav>`, `<main>`, `<article>`, `<aside>`, `<footer>`) bilan ishlash;
- Matnlar, sarlavhalar (`<h1>`-`<h6>`), ro'yxatlar (`<ul>`, `<ol>`) va havolalar (`<a>`) yaratish;
- HTML formalari (`<form>`, `<input>`, `<select>`, `<button>`) orqali foydalanuvchidan ma'lumot qabul qilish.

---

## Asosiy HTML5 Teglar

```html
<!DOCTYPE html>
<html lang="uz">
<head>
    <meta charset="UTF-8">
    <title>Mening Birinchi Veb Saytim</title>
</head>
<body>
    <header>
        <h1>Veb Dasturlash Kursi</h1>
        <nav>
            <a href="#home">Bosh sahifa</a> |
            <a href="#about">Biz haqimizda</a>
        </nav>
    </header>

    <main>
        <section>
            <h2>HTML5 Nima?</h2>
            <p>HTML — bu veb sahifalarning strukturaviy karkasidir.</p>
        </section>

        <section>
            <h2>Ro'yxatdan O'tish Formasi</h2>
            <form action="/submit" method="POST">
                <label for="username">Ismingiz:</label>
                <input type="text" id="username" name="username" required>
                <button type="submit">Yuborish</button>
            </form>
        </section>
    </main>

    <footer>
        <p>© 2026 MarimovDev. Barcha huquqlar himoyalangan.</p>
    </footer>
</body>
</html>
```

Keyingi **50-dars: CSS3 Styling, Flexbox va Grid Layout** da saytga chiroyli visual bezak berishni o'rganamiz.
