sed -i '3330,3362c\
              <div className="flex flex-col gap-4">\
                <div className="p-4 bg-slate-50 border border-slate-100 rounded-2xl flex flex-col gap-3">\
                  <h4 className="font-extrabold text-[11px] text-slate-700 uppercase tracking-wider flex items-center gap-2"><div className="w-2 h-2 rounded-full bg-blue-500"></div>BCA</h4>\
                  <div className="grid grid-cols-2 gap-3">\
                    <div className="flex flex-col gap-1.5">\
                      <label className="text-[10px] font-bold text-slate-500">Nomor Rekening</label>\
                      <input type="text" value={settings.bank_bca_number || '"'"''"'"'} onChange={e => updateSettings({ ...settings, bank_bca_number: e.target.value })} placeholder="Contoh: 1234567890" className="bg-white border border-slate-200 text-slate-800 text-xs font-bold rounded-xl px-3 py-2 outline-none" />\
                    </div>\
                    <div className="flex flex-col gap-1.5">\
                      <label className="text-[10px] font-bold text-slate-500">Atas Nama</label>\
                      <input type="text" value={settings.bank_bca_name || '"'"''"'"'} onChange={e => updateSettings({ ...settings, bank_bca_name: e.target.value })} placeholder="Contoh: John Doe" className="bg-white border border-slate-200 text-slate-800 text-xs font-bold rounded-xl px-3 py-2 outline-none" />\
                    </div>\
                  </div>\
                  <ImageUploadOrUrl value={settings.bank_bca_logo || '"'"''"'"'} onChange={val => updateSettings({ ...settings, bank_bca_logo: val })} label="Logo Bank BCA" placeholder="URL logo atau unggah" />\
                </div>\
                \
                <div className="p-4 bg-slate-50 border border-slate-100 rounded-2xl flex flex-col gap-3">\
                  <h4 className="font-extrabold text-[11px] text-slate-700 uppercase tracking-wider flex items-center gap-2"><div className="w-2 h-2 rounded-full bg-orange-500"></div>SeaBank</h4>\
                  <div className="grid grid-cols-2 gap-3">\
                    <div className="flex flex-col gap-1.5">\
                      <label className="text-[10px] font-bold text-slate-500">Nomor Rekening</label>\
                      <input type="text" value={settings.bank_seabank_number || '"'"''"'"'} onChange={e => updateSettings({ ...settings, bank_seabank_number: e.target.value })} placeholder="Contoh: 9012345678" className="bg-white border border-slate-200 text-slate-800 text-xs font-bold rounded-xl px-3 py-2 outline-none" />\
                    </div>\
                    <div className="flex flex-col gap-1.5">\
                      <label className="text-[10px] font-bold text-slate-500">Atas Nama</label>\
                      <input type="text" value={settings.bank_seabank_name || '"'"''"'"'} onChange={e => updateSettings({ ...settings, bank_seabank_name: e.target.value })} placeholder="Contoh: John Doe" className="bg-white border border-slate-200 text-slate-800 text-xs font-bold rounded-xl px-3 py-2 outline-none" />\
                    </div>\
                  </div>\
                  <ImageUploadOrUrl value={settings.bank_seabank_logo || '"'"''"'"'} onChange={val => updateSettings({ ...settings, bank_seabank_logo: val })} label="Logo Bank SeaBank" placeholder="URL logo atau unggah" />\
                </div>\
                \
                <div className="p-4 bg-slate-50 border border-slate-100 rounded-2xl flex flex-col gap-3">\
                  <h4 className="font-extrabold text-[11px] text-slate-700 uppercase tracking-wider flex items-center gap-2"><div className="w-2 h-2 rounded-full bg-sky-500"></div>PayPal</h4>\
                  <div className="grid grid-cols-2 gap-3">\
                    <div className="flex flex-col gap-1.5">\
                      <label className="text-[10px] font-bold text-slate-500">Akun / Email</label>\
                      <input type="text" value={settings.bank_paypal_number || '"'"''"'"'} onChange={e => updateSettings({ ...settings, bank_paypal_number: e.target.value })} placeholder="Contoh: email@example.com" className="bg-white border border-slate-200 text-slate-800 text-xs font-bold rounded-xl px-3 py-2 outline-none" />\
                    </div>\
                    <div className="flex flex-col gap-1.5">\
                      <label className="text-[10px] font-bold text-slate-500">Atas Nama</label>\
                      <input type="text" value={settings.bank_paypal_name || '"'"''"'"'} onChange={e => updateSettings({ ...settings, bank_paypal_name: e.target.value })} placeholder="Contoh: John Doe" className="bg-white border border-slate-200 text-slate-800 text-xs font-bold rounded-xl px-3 py-2 outline-none" />\
                    </div>\
                  </div>\
                  <ImageUploadOrUrl value={settings.bank_paypal_logo || '"'"''"'"'} onChange={val => updateSettings({ ...settings, bank_paypal_logo: val })} label="Logo Bank PayPal" placeholder="URL logo atau unggah" />\
                </div>\
              </div>' src/views/AdminView.tsx
