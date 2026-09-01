import { Lesson } from '../types';

export const initialLessonsData: Lesson[] = [
  {
    id: 'les-1',
    lessonNumber: 1,
    title: "Dasturlash asoslari va Algoritm tushunchasi",
    date: '2024-09-04',
    time: '08:30 - 10:00',
    status: 'completed',
    description: "Algoritm tushunchasi, uning xossalari, turlari va ifodalanish usullari bilan tanishish.",
    content: `### 1. Algoritm tushunchasi va tarixi
"Algoritm" so'zi buyuk o'zbek qomusiy olimi **Muhammad ibn Muso al-Xorazmiy** (783–850) nomining lotincha ifodasi *"Algorithmi"* so'zidan kelib chiqqan.

> **Ta'rif:** Berilgan boshlang'ich ma'lumotlar asosida ko'zlangan natijaga erishish uchun bajaruvchiga yo'naltirilgan aniq, tushunarli va chekli buyruqlar ketma-ketligi **algoritm** deb ataladi.

---

### 2. Algoritmning asosiy xossalari
Har qanday buyruqlar ketma-ketligi algoritm bo'la olmaydi. Algoritm quyidagi 5 ta muhim xossaga ega bo'lishi shart:
1. **Diskretlik:** Algoritm qadam-baqadam, bo'laklarga bo'lingan holda bajarilishi lozim.
2. **Aniqlik:** Har bir buyruq bajaruvchi uchun bir ma'noli bo'lishi kerak.
3. **Tushunarlilik:** Buyruqlar faqat bajaruvchining buyruqlar tizimiga kiruvchi amallardan iborat bo'lishi kerak.
4. **Ommaviylik:** Tuzilgan algoritm bir turdagi barcha masalalar to'plamini yechishga yaroqli bo'lishi lozim.
5. **Natijaviylik (Cheklilik):** Algoritm chekli sondagi qadamlardan so'ng aniq natija bilan tugashi shart.`,
    homework: "Darslikning 12-betidagi 1-5 topshiriqlarni bajarish. Uchta son orasidan eng kattasini topuvchi algoritmning blok-sxemasini daftarga chizib kelish.",
    materials: [
      { id: 'm-1', name: '1-Dars_Taqdimot_Algoritmlar.pptx', type: 'pptx', size: '3.4 MB' },
      { id: 'm-2', name: 'Algoritmlash_Konspekt_va_Korsatmalar.pdf', type: 'pdf', size: '1.2 MB' }
    ],
    tasks: [
      {
        id: 't-1',
        title: "Kvadrat tenglama diskriminantini hisoblash",
        type: 'practical',
        question: "ax² + bx + c = 0 kvadrat tenglama uchun D = b² - 4ac diskriminantni hisoblash va ildizlar sonini aniqlash algoritmini tuzing.",
        answer: "1. a, b, c ni kiritish\n2. D = b*b - 4*a*c\n3. Agar D > 0 bo'lsa: '2 ta ildiz bor'\n4. Agar D == 0 bo'lsa: '1 ta ildiz bor'\n5. Aks holda: 'Haqiqiy ildiz yo'q'"
      },
      {
        id: 't-2',
        title: "Algoritm xossalari testi",
        type: 'test',
        question: "Quyidagilardan qaysi biri algoritm의 chekli qadamdan so'ng tugashini ifodalovchi xossasi?",
        answer: "Natijaviylik (Cheklilik) xossasi."
      }
    ]
  },
  {
    id: 'les-2',
    lessonNumber: 2,
    title: "Python dasturlash tili sintaksisi va o'zgaruvchilar",
    date: '2024-09-11',
    time: '08:30 - 10:00',
    status: 'completed',
    description: "Python tiliga kirish, ma'lumotlar turlari (int, float, str, bool), o'zgaruvchilarni e'lon qilish va arifmetik amallar.",
    content: `### 1. Python tiliga kirish
Python — bu yuqori darajali, talqin qilinadigan (interpreted), o'qilishi oson va qat'iy sintaksisga ega zamonaviy dasturlash tili. U 1991-yilda **Gvido van Rossum** tomonidan yaratilgan.

### 2. O'zgaruvchilar va ma'lumot turlari
Python tilida o'zgaruvchilar dinamik tiplashtiriladi. Ya'ni, o'zgaruvchining turi unga qiymat berilganda avtomatik aniqlanadi.

* **int:** Butun sonlar (masalan, \`x = 10\`)
* **float:** Haqiqiy/o'nli sonlar (\`y = 3.14\`)
* **str:** Satrli/matnli qiymatlar (\`name = "Ali"\`)
* **bool:** Mantiqiy qiymat (\`is_active = True\`)`,
    homework: "O'zgaruvchilar nomi qoidalarini yozib kelish. Kiritilgan ikki sonning ko'paytmasini hisoblovchi kod yozish.",
    materials: [
      { id: 'm-4', name: 'Python_Ozgaruvchilar_Sintaksis.pdf', type: 'pdf', size: '2.1 MB' },
      { id: 'm-5', name: 'Amaliy_kod_namunalari.zip', type: 'zip', size: '1.8 MB' }
    ],
    tasks: [
      {
        id: 't-3',
        title: "Kalkulyator dasturi",
        type: 'practical',
        question: "Foydalanuvchidan ikkita son qabul qilib, ularning yig'indisi va ko'paytmasini chiqaruvchi Python kodini yozing.",
        answer: "a = float(input('Birinchi sonni kiriting: '))\nb = float(input('Ikkinchi sonni kiriting: '))\nprint('Yig\\'indi:', a + b)\nprint('Ko\\'paytma:', a * b)"
      }
    ]
  },
  {
    id: 'les-3',
    lessonNumber: 3,
    title: "Shart operatorlari (if, elif, else)",
    date: '2024-09-18',
    time: '08:30 - 10:00',
    status: 'completed',
    description: "Tarmoqlanuvchi algoritmlarni Python tilida amalga oshirish: taqqoslash va mantiqiy amallar.",
    content: `### 1. Shart operatorining tuzilishi
Tarmoqlanish jarayonlarini boshqarish uchun \`if\`, \`elif\` (else if) va \`else\` kalit so'zlaridan foydalaniladi.

\`\`\`python
yosh = int(input("Yoshingizni kiriting: "))
if yosh >= 18:
    print("Siz ovoz bera olasiz!")
else:
    print("Siz hali voyaga yetmagansiz.")
\`\`\`

---

### 2. Mantiqiy operatorlar
* \`and\`: Ikkala shart ham to'g'ri bo'lsa True
* \`or\`: Kamida bitta shart to'g'ri bo'lsa True
* \`not\`: Shartni teskarisiga o'zgartiradi`,
    homework: "Kiritilgan sonning juft yoki toq ekanligini aniqlovchi dastur yozish.",
    materials: [
      { id: 'm-6', name: 'If_Shart_Operatorlari.pdf', type: 'pdf', size: '1.5 MB' }
    ],
    tasks: [
      {
        id: 't-4',
        title: "Katta sonni topish",
        type: 'practical',
        question: "Uchta son kiritilganda, ularning eng kattasini topuvchi Python dasturini yozing.",
        answer: "a = float(input())\nb = float(input())\nc = float(input())\n\nmax_val = a\nif b > max_val:\n    max_val = b\nif c > max_val:\n    max_val = c\nprint('Eng katta son:', max_val)"
      }
    ]
  },
  {
    id: 'les-4',
    lessonNumber: 4,
    title: "Sikllar va takrorlanish operatorlari (for, while)",
    date: '2024-09-25',
    time: '08:30 - 10:00',
    status: 'pending',
    description: "Takrorlanuvchi jarayonlar bilan ishlash. range() funksiyasi va siklni boshqarish.",
    content: `### 1. 'for' sikli va range()
\`for\` sikli ma'lum bir ketma-ketlik elementlari bo'ylab takrorlash uchun qo'llaniladi.

\`\`\`python
# 1 dan 5 gacha sonlarni chop etish
for i in range(1, 6):
    print(i)
\`\`\`

---

### 2. 'while' sikli
\`while\` sikli berilgan shart to'g'ri (True) bo'lib turgan vaqtda takrorlanadi.

\`\`\`python
sanoq = 0
while sanoq < 3:
    print("Salom")
    sanoq += 1
\`\`\``,
    homework: "1 dan 100 gacha bo'lgan toq sonlarning yig'indisini hisoblovchi dastur tuzish.",
    materials: [
      { id: 'm-7', name: 'Sikllar_Takrorlanish.pptx', type: 'pptx', size: '2.8 MB' }
    ],
    tasks: [
      {
        id: 't-5',
        title: "Kopaytirish jadvali",
        type: 'practical',
        question: "Berilgan sonning 1 dan 10 gacha bo'lgan karrali jadvalini chiqaruvchi kod yozing.",
        answer: "n = int(input())\nfor i in range(1, 11):\n    print(f'{n} x {i} = {n * i}')"
      }
    ]
  },
  {
    id: 'les-5',
    lessonNumber: 5,
    title: "Funksiyalar bilan ishlash (def)",
    date: '2024-10-02',
    time: '08:30 - 10:00',
    status: 'planned',
    description: "Kodning qayta ishlatilishini ta'minlash. Funksiyani e'lon qilish, parametrlar va return.",
    content: `### 1. Funksiya tushunchasi
Funksiya — bu faqat chaqirilganda ishlaydigan va ma'lum bir vazifani bajaradigan kodlar bloki.

\`\`\`python
def salomlash(ism):
    return f"Salom, {ism}!"

print(salomlash("Ogabek"))
\`\`\`

---

### 2. Return qiymati
\`return\` operatori funksiyadan natija qaytarish va uning ishini tugatish uchun ishlatiladi.`,
    homework: "Berilgan sonning kvadratini hisoblovchi funksiya yozish va oliy darslarda tekshirish.",
    materials: [
      { id: 'm-8', name: 'Python_Funksiyalar.pdf', type: 'pdf', size: '1.9 MB' }
    ],
    tasks: [
      {
        id: 't-6',
        title: "Juft sonni tekshirish funksiyasi",
        type: 'practical',
        question: "Son qabul qilib, u juft bo'lsa True, toq bo'lsa False qaytaruvchi juft_mi(n) funksiyasini yozing.",
        answer: "def juft_mi(n):\n    return n % 2 == 0"
      }
    ]
  }
];
