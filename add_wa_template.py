with open('src/views/AdminView.tsx', 'r') as f:
    content = f.read()

wa_block = """
        {/* TAB 10: WA TEMPLATE (wa-template) */}
        {activeTab === 'wa-template' && (
          <div className="flex flex-col gap-4 text-left">
            <div className="bg-white rounded-3xl border border-slate-100 p-5 shadow-sm">
              <h3 className="text-slate-800 font-extrabold text-xs mb-1 flex items-center gap-1.5">
                <MessageCircle size={15} className="text-fuchsia-600" />
                Template Pesan WhatsApp
              </h3>
              <p className="text-slate-400 text-[10px] font-bold leading-relaxed mb-4">
                Atur format pesan WhatsApp yang akan dikirim oleh pelanggan saat melakukan pemesanan.
              </p>
              
              <div className="flex flex-col gap-4">
                {/* Template Tour Package */}
                <div className="flex flex-col gap-1.5 border border-slate-100 p-4 rounded-2xl bg-slate-50/50">
                  <label className="text-[10px] font-black text-slate-700 uppercase tracking-widest ml-1">Template Pemesanan Paket Tour</label>
                  <p className="text-[9px] text-slate-500 mb-2 leading-relaxed">
                    Gunakan placeholder berikut: <br/>
                    <code className="text-fuchsia-600 font-bold bg-fuchsia-50 px-1 py-0.5 rounded">[NAMA_PAKET]</code> untuk nama paket<br/>
                    <code className="text-fuchsia-600 font-bold bg-fuchsia-50 px-1 py-0.5 rounded">[OPSI]</code> untuk opsi harga yang dipilih (jika ada)<br/>
                    <code className="text-fuchsia-600 font-bold bg-fuchsia-50 px-1 py-0.5 rounded">[HARGA]</code> untuk harga total
                  </p>
                  <textarea
                    value={settings.wa_template_package || 'Halo, saya ingin memesan:\nPaket: [NAMA_PAKET]\nOpsi: [OPSI]\nHarga: [HARGA]'}
                    onChange={(e) => updateSettings({ ...settings, wa_template_package: e.target.value })}
                    rows={4}
                    className="w-full bg-white border border-slate-200 outline-none text-xs font-medium text-slate-800 rounded-xl py-2 px-3 resize-none focus:border-fuchsia-300 focus:ring-4 focus:ring-fuchsia-100 transition-all"
                  />
                  
                  {/* Preview Tour Package */}
                  <div className="mt-2 bg-green-50 border border-green-100 rounded-xl p-3">
                    <span className="text-[9px] font-bold text-green-700 uppercase mb-1 block">Preview Pesan:</span>
                    <p className="text-[10px] text-green-800 whitespace-pre-wrap font-medium">
                      {(settings.wa_template_package || 'Halo, saya ingin memesan:\\nPaket: [NAMA_PAKET]\\nOpsi: [OPSI]\\nHarga: [HARGA]')
                        .replace('\\[NAMA_PAKET\\]', 'Nusa Penida Tour')
                        .replace('\\[OPSI\\]', 'Private Car')
                        .replace('\\[HARGA\\]', 'Rp 1.500.000')}
                    </p>
                  </div>
                </div>

                {/* Template Activity */}
                <div className="flex flex-col gap-1.5 border border-slate-100 p-4 rounded-2xl bg-slate-50/50">
                  <label className="text-[10px] font-black text-slate-700 uppercase tracking-widest ml-1">Template Pemesanan Aktivitas</label>
                  <p className="text-[9px] text-slate-500 mb-2 leading-relaxed">
                    Gunakan placeholder berikut: <br/>
                    <code className="text-fuchsia-600 font-bold bg-fuchsia-50 px-1 py-0.5 rounded">[NAMA_AKTIVITAS]</code> untuk nama aktivitas<br/>
                    <code className="text-fuchsia-600 font-bold bg-fuchsia-50 px-1 py-0.5 rounded">[PAKET]</code> untuk paket yang dipilih (opsional)<br/>
                    <code className="text-fuchsia-600 font-bold bg-fuchsia-50 px-1 py-0.5 rounded">[OPSI]</code> untuk harga/opsi khusus (opsional)<br/>
                    <code className="text-fuchsia-600 font-bold bg-fuchsia-50 px-1 py-0.5 rounded">[HARGA]</code> untuk harga total
                  </p>
                  <textarea
                    value={settings.wa_template_activity || 'Halo, saya tertarik dengan aktivitas:\nAktivitas: [NAMA_AKTIVITAS]\nPaket: [PAKET]\nOpsi: [OPSI]\nHarga: [HARGA]'}
                    onChange={(e) => updateSettings({ ...settings, wa_template_activity: e.target.value })}
                    rows={4}
                    className="w-full bg-white border border-slate-200 outline-none text-xs font-medium text-slate-800 rounded-xl py-2 px-3 resize-none focus:border-fuchsia-300 focus:ring-4 focus:ring-fuchsia-100 transition-all"
                  />
                  
                  {/* Preview Activity */}
                  <div className="mt-2 bg-green-50 border border-green-100 rounded-xl p-3">
                    <span className="text-[9px] font-bold text-green-700 uppercase mb-1 block">Preview Pesan:</span>
                    <p className="text-[10px] text-green-800 whitespace-pre-wrap font-medium">
                      {(settings.wa_template_activity || 'Halo, saya tertarik dengan aktivitas:\\nAktivitas: [NAMA_AKTIVITAS]\\nPaket: [PAKET]\\nOpsi: [OPSI]\\nHarga: [HARGA]')
                        .replace('\\[NAMA_AKTIVITAS\\]', 'Water Sports Tanjung Benoa')
                        .replace('\\[PAKET\\]', 'Paket A (Parasailing, Banana Boat)')
                        .replace('\\[OPSI\\]', 'WNI / KTP')
                        .replace('\\[HARGA\\]', 'Rp 250.000')}
                    </p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        )}
"""

target = "      </div>\n    </div>\n  );\n}"

if target in content:
    content = content.replace(target, wa_block + "\n" + target)
else:
    print("Could not find target block")

with open('src/views/AdminView.tsx', 'w') as f:
    f.write(content)
