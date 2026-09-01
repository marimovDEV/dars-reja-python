# 📘 DARS DOKUMENTATSIYASI SHABLONI — Ichki Qo'llanma

Bu hujjat har bir dars uchun professional dokumentatsiya yozishda **majburiy** qo'llaniladigan shablon va qoidalar to'plamidir. Hech bir bo'lim tushirib qoldirilmasligi kerak.

---

## FORMAT QOIDALARI

- Til: O'zbek tilida tushuntirishlar, inglizcha texnik atamalar.
- Kod bloklari: faqat ` ```python ` ichida.
- Kod oldidan `python`, `Nusxalash`, satr raqamlari kabi oddiy text YOZILMASIN.
- Kodlar sintaktik jihatdan to'g'ri va ishga tushadigan bo'lsin.
- O'zgaruvchi nomlari tushunarli, o'zbekcha yoki inglizcha (mos kelgani).
- "va hokazo", "shu kabi" deb qoldirmaslik; har narsani to'liq tushuntirish.
- Har bo'limda sarlavha va bo'sh joy ishlatish, uzun oddiy matn yozmaslik.
- Mavzuga aloqasi bo'lmagan narsalarni yozmaslik.
- Minimal hajm: 4000–8000 belgi (kichik mavzular uchun kamida 4000, katta mavzular uchun 8000+).

---

## SHABLON TUZILISHI (19 bo'lim)

Quyida har bir bo'limning aniq formati va minimal talablari keltirilgan.

---

### 1-BO'LIM: Sarlavha

```
# [emoji] [dars_raqami]. [Mavzu nomi] — Dars dokumentatsiyasi
```

Emoji mavzuga mos tanlanadi. Masalan: 🏗️ (models), 🔐 (auth), 🧪 (testing), 🐳 (docker).

---

### 2-BO'LIM: Kirish tushuntirish (2–4 paragraf)

Mavzu nima ekanini sodda tilda, ammo to'liq tushuntirish. Har bir paragraf alohida fikrni bildiradi:

- 1-paragraf: Bu nima va nima uchun kerak?
- 2-paragraf: Qanday ishlaydi (mexanizmi)?
- 3-paragraf: Qayerda va qachon ishlatiladi (real kontekst)?
- 4-paragraf (ixtiyoriy): Boshqa usullardan farqi yoki afzalligi.

**Minimal:** 2 paragraf, **Tavsiya:** 3–4 paragraf.

---

### 3-BO'LIM: Bu mavzu orqali nimalar qilish mumkin

```
## Bu mavzu orqali nimalar qilish mumkin

- [1-imkoniyat];
- [2-imkoniyat];
- [3-imkoniyat];
- ...
```

**Minimal:** 4 ta band, **Tavsiya:** 5–6 ta.

---

### 4-BO'LIM: Dars maqsadi

```
## Dars maqsadi

Bu dars oxirida o'quvchi:

- [1-ko'nikma];
- [2-ko'nikma];
- [3-ko'nikma];
- ...

ni mustaqil bajara oladi.
```

**Minimal:** 4 ta ko'nikma, **Tavsiya:** 5–6 ta.

---

### 5-BO'LIM: Kerakli oldingi bilimlar

```
## Kerakli oldingi bilimlar

Bu darsni tushunish uchun:

- [oldingi dars/mavzu va raqami];
- [oldingi dars/mavzu va raqami];
- [kerakli modul yoki tushuncha]

bilinishi kerak.
```

**Minimal:** 3 ta, o'quvchi darajasiga mos. Aniq dars raqamlarini ko'rsatish.

---

### 6-BO'LIM: Asosiy tushunchalar va atamalar

Har bir atama uchun:

```
## [Atama] nima?

> **[Atama]** — bu [aniq va sodda ta'rif]. [Qayerda va nima uchun ishlatiladi].
```

Har bir tushuncha blockquote ichida, qisqa va aniq.

**Minimal:** 4 ta atama, **Tavsiya:** 5–8 ta.

---

### 7-BO'LIM: Sintaksis va uning izohi

Mavzuning umumiy yozilish strukturasini ko'rsatish:

```python
# umumiy sintaksis
```

Har bir qator ostida izoh berish.

---

### 8-BO'LIM: Jadvallar (metodlar, klasslar, parametrlar, fieldlar)

Mavzuga qarab bir yoki bir nechta jadval.

| Nomi | Vazifasi | Parametrlari | Misol | Ko'p uchraydigan xatosi |
|---|---|---|---|---|

Yoki field/parametr jadvali:

| Parametr | Turi | Vazifasi | Default | Misol |
|---|---|---|---|---|

**Minimal:** 1 ta jadval kamida 8 qatordan, **Tavsiya:** 2–3 ta jadval.

---

### 9-BO'LIM: Kod misollari (kamida 8 ta)

Har bir misol uchun:

```
## Misol [N] — [Nomi]
```

Keyin:

1. **Kod bloki** — to'liq ishlaydigan Python kodi
2. **Natija** — `Natija:` sarlavhasi bilan kutilgan chiqish
3. **Qatorma-qator izoh** — har bir muhim qator uchun izoh
4. **Qachon ishlatiladi** — real kontekst

Misollar osondan murakkabga qarab tartiblangan bo'lsin.

**Minimal:** 8 ta misol, **Tavsiya:** 8–12 ta.

Misollar progressiyasi:
- Misol 1–2: Eng sodda, birinchi tanishuv
- Misol 3–4: Asosiy parametrlar va konfiguratsiyalar
- Misol 5–6: O'rta murakkablik, kombinatsiyalar
- Misol 7–8: Murakkab, real loyihaga yaqin

---

### 10-BO'LIM: Real loyiha misoli

To'liq, real loyiha kontekstida ishlaydigan kod. Masalan:
- Blog tizimi
- Onlayn do'kon
- Kurs platformasi
- Chat ilovasi

**Minimal:** 1 ta loyiha, 30+ qator kod, izohi bilan.

---

### 11-BO'LIM: Ko'p uchraydigan xatolar

Har bir xato uchun:

```
## Xato [N]: [Xato sarlavhasi]

Noto'g'ri:

\```python
# xato kod
\```

Nima uchun xato: [sabab]

To'g'ri:

\```python
# to'g'ri kod
\```

Qanday oldini olish: [maslahat]
```

**Minimal:** 4 ta xato, **Tavsiya:** 5–6 ta.

---

### 12-BO'LIM: 3 darajali amaliy topshiriqlar

```
## 1-topshiriq — Oson
**Vazifa:** [aniq vazifa tavsifi]
[Kutilgan natija yoki izoh]

## 2-topshiriq — O'rta
**Vazifa:** [aniq vazifa tavsifi]

## 3-topshiriq — Murakkab
**Vazifa:** [aniq vazifa tavsifi]
```

Har bir topshiriq aniq va bajarsa bo'ladigan bo'lsin.

---

### 13-BO'LIM: Uyga vazifa

```
## Uyga vazifa

1. [vazifa 1];
2. [vazifa 2];
3. [vazifa 3];
4. [vazifa 4];
5. [vazifa 5].
```

**Minimal:** 5 ta, har biri o'quvchini mustaqil fikrlashga undaydigan.

---

### 14-BO'LIM: Test savollari

```
## Test savollari

1. [savol]?
2. [savol]?
...
10. [savol]?
```

**Minimal:** 10 ta savol. Har xil qiyinlikda — oddiy ta'rifdan tortib amaliy savolga qadar.

---

### 15-BO'LIM: Test javoblari

```
## Javoblar

**1.** [to'liq javob]

**2.** [to'liq javob]

...
```

Har bir javob 2–4 jumla. Qisqa emas, to'liq tushuntirish.

---

### 16-BO'LIM: Qisqa xulosa

```
## Qisqa xulosa

Bu darsda:

- [1-o'rganilgan narsa];
- [2-o'rganilgan narsa];
- [3-o'rganilgan narsa];
- ...

o'rganildi.
```

**Minimal:** 4 ta band.

---

### 17-BO'LIM: Keyingi darsga bog'lanish

```
Keyingi **[N]-dars: [Mavzu nomi]** da [qisqa tushuntirish: nima o'rganiladi va bu dars bilan qanday bog'liq].
```

1–2 jumla, aniq va motivatsiya beruvchi.

---

### 18-BO'LIM: Qo'shimcha resurslar

```
## Qo'shimcha resurslar

- 📄 Rasmiy hujjat: [link]
- 📄 Qo'shimcha hujjat: [link]
- 💻 Kodlar: `github.com/dars-reja/[N]-dars`
- 🎬 Video dars: `youtube.com/watch?v=dars[N]`
```

**Minimal:** 4 ta resurs.

---

## SIFAT MEZONLARI

Tayyor dokumentatsiya quyidagi mezonlarga javob berishi SHART:

| Mezon | Talab |
|---|---|
| Hajm | Kamida 4000 belgi (katta mavzular 6000–8000) |
| Kod misollari | Kamida 8 ta, barchasi ishlaydigan |
| Jadvallar | Kamida 1 ta, 8+ qator |
| Xatolar | Kamida 4 ta, sabab + yechim bilan |
| Test savollari | Kamida 10 ta + javoblari |
| Uyga vazifa | Kamida 5 ta |
| Topshiriqlar | 3 daraja: oson, o'rta, murakkab |
| Atamalar | Kamida 4 ta, izohli |
| Real loyiha | Kamida 1 ta, 30+ qator kod |
| Format | Markdown, kod bloklari to'g'ri |

---

## QANDAY ISHLATILADI

Men (agent) har bir dars uchun dokumentatsiya yozganimda:

1. Ushbu shablonni o'qiyman;
2. 19 bo'limning har birini to'liq yozaman;
3. Sifat mezonlarini tekshiraman;
4. Tayyor hujjatni foydalanuvchiga taqdim etaman.

Foydalanuvchi faqat quyidagilarni beradi:
- Dars raqami
- Mavzu nomi
- Keyingi dars mavzusi
- O'quvchi darajasi
- Qamrab olishi kerak bo'lgan atamalar/tushunchalar ro'yxati

Men qolgan hamma narsani shu shablon asosida yozaman.
