import re
with open('src/views/ActivityDetailView.tsx', 'r') as f:
    content = f.read()

target = re.compile(r'            <div className="flex flex-col gap-2">\n              \{activePrices\.map\(\(pr, idx\) =\> \{\n                const isSelected = selectedPriceIdx === idx;\n.*?\n              \}\)\}\n            \</div\>', re.DOTALL)

replacement = """            <div className="flex flex-col gap-2">
              {activePrices.map((pr) => {
                const q = quantities[pr.id] || 0;
                return (
                  <div
                    key={pr.id}
                    className="w-full p-4 rounded-2xl text-left border border-slate-50 bg-slate-50/40 flex justify-between items-center transition-all"
                  >
                    <div className="flex items-center gap-2.5">
                      <span className="text-slate-800 text-xs font-bold">
                        {language === 'zh' ? (pr.label_zh || pr.label) : language === 'en' ? (pr.label_en || pr.label) : (pr.label_id || pr.label)}
                      </span>
                    </div>
                    <div className="flex flex-col items-end gap-2">
                      <span className="font-bold text-xs" style={primaryText}>
                        Rp {pr.price_idr.toLocaleString('id-ID')}
                      </span>
                      <div className="flex items-center gap-3">
                        <button 
                          onClick={() => setQuantities(prev => ({...prev, [pr.id]: Math.max(0, (prev[pr.id] || 0) - 1)}))}
                          className="w-6 h-6 rounded-full bg-slate-200 text-slate-600 flex items-center justify-center font-bold active:scale-95"
                        >
                          -
                        </button>
                        <span className="text-xs font-bold w-4 text-center">{q}</span>
                        <button 
                          onClick={() => setQuantities(prev => ({...prev, [pr.id]: (prev[pr.id] || 0) + 1}))}
                          className="w-6 h-6 rounded-full text-white flex items-center justify-center font-bold active:scale-95"
                          style={primaryBg}
                        >
                          +
                        </button>
                      </div>
                    </div>
                  </div>
                );
              })}
            </div>"""

content = target.sub(replacement, content)

# Remove the state declaration
content = content.replace("const [selectedPriceIdx, setSelectedPriceIdx] = useState(0);", "")

with open('src/views/ActivityDetailView.tsx', 'w') as f:
    f.write(content)
