import re
with open('src/views/ActivityDetailView.tsx', 'r') as f:
    content = f.read()

target = """            <div className="flex flex-col gap-2">
              {activePrices.map((pr, idx) => {
                const isSelected = selectedPriceIdx === idx;
                return (
                  <button
                    key={pr.id}
                    onClick={() => setSelectedPriceIdx(idx)}
                    className={`w-full p-4 rounded-2xl text-left border flex justify-between items-center transition-all ${
                      isSelected
                        ? 'border-indigo-100 bg-indigo-50/40'
                        : 'border-slate-50 bg-slate-50/40 hover:bg-slate-50 text-slate-700'
                    }`}
                  >
                    <div className="flex items-center gap-2.5">
                      <div 
                        className={`w-5 h-5 rounded-full border-2 flex items-center justify-center ${
                          isSelected ? 'border-transparent text-white' : 'border-slate-300'
                        }`}
                        style={isSelected ? primaryBg : {}}
                      >
                        {isSelected && <div className="w-2 h-2 rounded-full bg-white" />}
                      </div>
                      <span className="text-slate-800 text-xs font-bold">
                        {language === 'zh' ? (pr.label_zh || pr.label) : language === 'en' ? (pr.label_en || pr.label) : (pr.label_id || pr.label)}
                      </span>
                    </div>
                    <span className="font-bold text-xs" style={primaryText}>
                      Rp {pr.price_idr.toLocaleString('id-ID')}
                    </span>
                  </button>
                );
              })}
            </div>"""

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

content = content.replace(target, replacement)

# Fix the total price calculation in the bottom bar
bottom_bar_target = """            Rp {(activePrices[selectedPriceIdx]?.price_idr || activity.price_per_person_idr)?.toLocaleString('id-ID')}
            <span className="text-[9px] font-medium text-white/80 block uppercase tracking-wider mt-0.5">
              {activePrices.length > 0 ? (
                (() => {
                  const pr = activePrices[selectedPriceIdx];
                  return language === 'zh' ? (pr.label_zh || pr.label) : language === 'en' ? (pr.label_en || pr.label) : (pr.label_id || pr.label);
                })()
              ) : (
                translate('per_person', language)
              )}
            </span>"""

bottom_bar_replacement = """            Rp {(() => {
              if (activePrices.length > 0) {
                let t = 0;
                activePrices.forEach(pr => { t += (quantities[pr.id] || 0) * pr.price_idr; });
                return t.toLocaleString('id-ID');
              }
              const q = quantities['default'] || 1;
              return (q * (activity.price_per_person_idr || 0)).toLocaleString('id-ID');
            })()}
            <span className="text-[9px] font-medium text-white/80 block uppercase tracking-wider mt-0.5">
              {activePrices.length > 0 ? 'Total' : translate('per_person', language)}
            </span>"""

content = content.replace(bottom_bar_target, bottom_bar_replacement)

with open('src/views/ActivityDetailView.tsx', 'w') as f:
    f.write(content)
