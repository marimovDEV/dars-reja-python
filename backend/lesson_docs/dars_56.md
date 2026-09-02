# 🖼 56. Django Static Files & Media Fayllar — Dars dokumentatsiyasi

Django loyihalarda CSS, JavaScript va fayllar **Static**, foydalanuvchilar yuklaydigan rasmlar esa **Media** fayllar deb yuritiladi.

---

## settings.py Sozlamalari

```python
# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

# Media files (Foydalanuvchi rasmlari)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

Keyingi **57-dars: Django Forms va Validatsiya** da formalarni tekshirishni o'rganamiz.
