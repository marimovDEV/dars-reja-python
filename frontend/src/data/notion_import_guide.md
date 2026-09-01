# Notion orqali Dars Rejalari Import qilish Qo'llanmasi

Ilovangizga dars rejalarini Notion'dan eksport qilingan `CSV` yoki `Markdown` formatlarida muvaffaqiyatli yuklash uchun quyidagi yo'riqnomaga amal qiling.

---

## 1. Notion Database sxemasi (CSV uchun)

Notion'da darslar jadvalini yaratayotganda quyidagi ustunlar (ustun nomlari) va turlardan foydalaning. Ustun nomlari o'zbekcha yoki inglizcha bo'lishi mumkin:

| Ustun nomi (Uzbek) | Ustun nomi (English) | Notion ustun turi (Property Type) | Misol qiymat |
| :--- | :--- | :--- | :--- |
| **Dars raqami** | **Lesson Number** or **#** | Number | `1` |
| **Sarlavha** | **Title** or **Name** | Title (Text) | `O'zgaruvchilar va turlar` |
| **Sana** | **Date** | Date | `2026-09-01` yoki `2026-09-01 -> 2026-09-02` |
| **Tavsif** | **Description** or **Mavzu** | Text | `O'zgaruvchi turlari (str, int, float, bool)` |
| **Uyga vazifa** | **Homework** or **Vazifa** | Text | `10 xil turdagi o'zgaruvchi yaratish` |
| **Holat** | **Status** | Status or Select | `completed` (O'tildi) yoki `planned` (Reja) |
| **Vaqt** | **Time** | Text | `14:00 - 16:00` |

> [!TIP]
> **Sana oralig'i (Date ranges):** Notion sana oralig'ini eksport qilganda (masalan, `2026-09-01 -> 2026-09-02`) tizim boshlanish sanasini (`2026-09-01`) avtomatik ravishda dars sanasi qilib oladi. Agar sana ustuni bo'sh bo'lsa, tizim darsni jadvalda sanasiz ko'rsatadi.

---

## 2. Markdown Formati (MD uchun)

Agar dars rejalarni bitta yaxlit Markdown fayli sifatida yuklamoqchi bo'lsangiz, har bir dars sarlavhasi va tarkibini quyidagi formatda yozing:

```markdown
### 1-dars — Sarlavha nomi
**Mavzu:** Algoritm va kompyuter tushunchasi.
**Amaliyot:** Terminalda darslarni boshlash.
**Uyga vazifa:** 7 qatorli "Men haqimda" dasturi.

### 2-dars — O'zgaruvchilar va turlar
**Mavzu:** str, int, float, bool turlari.
**Amaliyot:** Talaba profilini o'zgaruvchilarga saqlash.
**Uyga vazifa:** O'zgaruvchilar yaratish.
```

---

## 3. Notion'dan Eksport qilish tartibi

1. Notion'dagi dars rejalari database'iga kiring.
2. Sahifaning yuqori o'ng burchagidagi uchta nuqta (**...**) tugmasini bosing.
3. Ochilgan menyudan **Export** buyrug'ini tanlang.
4. **Export format** maydonidan **Markdown & CSV** variantini belgilang.
5. **Export** tugmasini bosing. Notion sizga ZIP fayl beradi.
6. ZIP faylni ochib, ichidagi `.csv` yoki `.md` faylini ushbu ilovaga yuklang.
