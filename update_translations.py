with open('src/data/translations.ts', 'r') as f:
    content = f.read()

insert = """
  view_more_activities: {
    id: 'Lihat Lebih Banyak Aktivitas',
    en: 'View More Activities',
    zh: '查看更多活动'
  },
  select_language_desc: {
    id: 'Sentuh opsi di bawah untuk mengubah bahasa aplikasi',
    en: 'Select an option to switch the application language',
    zh: '选择一个选项以切换应用程序语言'
  },
"""

content = content.replace("export const translations: Record<string, { id: string; en: string; zh: string }> = {", "export const translations: Record<string, { id: string; en: string; zh: string }> = {" + insert)

with open('src/data/translations.ts', 'w') as f:
    f.write(content)
