with open('src/data/translations.ts', 'r') as f:
    content = f.read()

content = content.replace(
    "id: 'View More Tour Packages',\n    en: 'View More Tour Packages',\n    zh: '查看更多旅游套餐'",
    "id: 'Lihat Lebih Banyak Paket Wisata',\n    en: 'View More Tour Packages',\n    zh: '查看更多旅游套餐'"
)

with open('src/data/translations.ts', 'w') as f:
    f.write(content)


with open('src/views/HomeView.tsx', 'r') as f:
    content2 = f.read()

content2 = content2.replace(
    "{language === 'id' ? 'Lihat Selengkapnya' : 'View More Tour Packages'}",
    "{translate('view_more_tour', language)}"
)

with open('src/views/HomeView.tsx', 'w') as f:
    f.write(content2)

