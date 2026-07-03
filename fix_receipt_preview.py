with open('src/views/AdminView.tsx', 'r') as f:
    content = f.read()

target = """                  <div className="text-[10px] border-b border-dashed border-slate-300 pb-2 mb-2">
                    <p>Waktu: {new Date().toLocaleString()}</p>
                    <p>Kasir: Admin</p>
                  </div>"""

replacement = """                  <div className="text-[10px] border-b border-dashed border-slate-300 pb-2 mb-2">
                    <p>Waktu: {new Date().toLocaleString()}</p>
                    <p>Kasir: Admin</p>
                    <p>Pemesan: Budi</p>
                  </div>"""

content = content.replace(target, replacement)

with open('src/views/AdminView.tsx', 'w') as f:
    f.write(content)
