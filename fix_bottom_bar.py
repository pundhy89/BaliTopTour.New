import re
with open('src/views/ActivityDetailView.tsx', 'r') as f:
    content = f.read()

bottom_bar_regex = re.compile(r'Rp \{\(activePrices\[selectedPriceIdx\]\?\.price_idr \|\| activity\.price_per_person_idr\)\?\.toLocaleString\(\'id-ID\'\)\}.*?\n.*?\n.*?\n.*?\n.*?\n.*?\n.*?\n.*?\n.*?\n.*?</span\>', re.DOTALL)

bottom_bar_new = """Rp {(() => {
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

content = bottom_bar_regex.sub(bottom_bar_new, content)

with open('src/views/ActivityDetailView.tsx', 'w') as f:
    f.write(content)
