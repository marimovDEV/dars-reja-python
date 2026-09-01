# 🐙 38. Git va GitHub — Dars dokumentatsiyasi

**Git** — bu dastur kodingizning barcha o'zgarishlar tarixini kuzatib boruvchi va saqlovchi dunyodagi eng mashhur **Versiyalarni Boshqarish Tizimi (VCS - Version Control System)** dir. U dasturchiga istalgan vaqtda kodning avvalgi holatiga qaytish yoki bir vaqtning o'zida bir nechta versiya (branches) ustida ishlash imkoniyatini beradi.

**GitHub** — bu Git repozitoriylarini bulutda saqlash, boshqa dasturchilar bilan birgalikda (teamwork) loyiha ustida ishlash va kodlarni ulashish uchun mo'ljallangan veb-platformadir.

---

## Bu mavzu orqali nimalar qilish mumkin

- Kompyuterda yangi Git repozitoriysi yaratish (`git init`);
- Kod o'zgarishlarini kuzatish (`git status`, `git add`, `git commit`);
- Tarmoqlar (`branches`) yaratish va ularni birlashtirish (`git merge`);
- Loyihani GitHub bulutli omboriga yuklash (`git push`) va u yerdan yuklab olish (`git clone`, `git pull`).

---

## Dars maqsadi

Bu dars oxirida o'quvchi:

- Git va GitHub o'rtasidagi farqni bilish;
- Asosiy Git buyruqlarini terminalda ishlatish;
- `.gitignore` fayli orqali keraksiz fayllarni (masalan `venv`, `.env`) berkitish;
- Loyihani GitHub platformasiga joylay olish

ni mustaqil bajara oladi.

---

## Kerakli oldingi bilimlar

- 1-dars: Terminal va dasturlash muhiti.

---

# 1. Asosiy Git Buyruqlari Jadvali

| Buyruq | Vazifasi |
|---|---|
| `git init` | Joriy papkada yangi local Git repozitoriy yaratadi |
| `git status` | O'zgartirilgan va kuzatuvdagi fayllar holatini ko'rsatadi |
| `git add .` | Barcha o'zgarishlarni keshga (staging area) qo'shadi |
| `git commit -m "msg"` | O'zgarishlarni izoh bilan xotiraga muhrlaydi |
| `git branch` | Mavjud tarmoqlarni ko'rsatadi |
| `git checkout -b name`| Yangi tarmoq yaratib unga o'tadi |
| `git push origin main` | Kodni GitHub omboriga yuklaydi |
| `git pull origin main` | GitHub dan so'nggi o'zgarishlarni yuklab oladi |

---

# 2. Amaliy Ish Ketma-ketligi (Workflow)

```bash
# 1. Repozitoriy yaratish
git init

# 2. Fayllarni belgilash va commit qilish
git add .
git commit -m "Initial commit: Project setup"

# 3. GitHub repozitoriyasiga ulash
git remote add origin https://github.com/username/project.git

# 4. Kodni GitHub ga push qilish
git branch -M main
git push -u origin main
```

---

# 10. Qisqa xulosa

Bu darsda Git versiyalar boshqaruvi tizimi, asosiy buyruqlar va GitHub bilan ishlash o'rganildi.
