sed -i '3382,3419c\
        {/* TAB 9: PRINTER & RECEIPT (receipt) */}\
        {activeTab === '"'"'receipt'"'"' && (\
          <div className="flex flex-col gap-4 text-left">\
            <div className="bg-white rounded-3xl border border-slate-100 p-5 shadow-sm">\
              <h3 className="text-slate-800 font-extrabold text-xs mb-1 flex items-center gap-1.5">\
                <Printer size={15} className="text-teal-600" />\
                Pengaturan Struk & Printer Thermal\
              </h3>\
              <p className="text-slate-400 text-[10px] font-bold leading-relaxed mb-4">\
                Atur tata letak, logo, dan footer struk. Hubungkan printer bluetooth untuk mencetak.\
              </p>\
              \
              <div className="flex flex-col gap-4 mb-6">\
                <div className="grid grid-cols-2 gap-4">\
                  <div className="flex flex-col gap-1.5">\
                    <label className="text-[10px] font-black text-slate-500 uppercase tracking-widest ml-1">Tata Letak (Layout)</label>\
                    <select \
                      value={settings.receipt_layout || '"'"'center'"'"'}\
                      onChange={(e) => updateSettings({ ...settings, receipt_layout: e.target.value as '"'"'left'"'"' | '"'"'center'"'"' })}\
                      className="bg-slate-50 border border-slate-200 text-slate-800 text-xs font-bold rounded-xl px-4 py-2.5 focus:border-teal-300 outline-none"\
                    >\
                      <option value="center">Tengah (Center)</option>\
                      <option value="left">Kiri (Left)</option>\
                    </select>\
                  </div>\
                  <div className="flex flex-col gap-1.5">\
                    <label className="text-[10px] font-black text-slate-500 uppercase tracking-widest ml-1">Ukuran Kertas</label>\
                    <select \
                      value={settings.receipt_paper_size || '"'"'58mm'"'"'}\
                      onChange={(e) => updateSettings({ ...settings, receipt_paper_size: e.target.value as '"'"'58mm'"'"' | '"'"'80mm'"'"' })}\
                      className="bg-slate-50 border border-slate-200 text-slate-800 text-xs font-bold rounded-xl px-4 py-2.5 focus:border-teal-300 outline-none"\
                    >\
                      <option value="58mm">58mm (Kecil)</option>\
                      <option value="80mm">80mm (Besar)</option>\
                    </select>\
                  </div>\
                </div>\
\
                <ImageUploadOrUrl\
                  value={settings.receipt_logo_url || '"'"''"'"'}\
                  onChange={(val) => updateSettings({ ...settings, receipt_logo_url: val })}\
                  label="Logo Struk"\
                  placeholder="URL logo atau unggah"\
                />\
\
                <div className="flex flex-col gap-1.5">\
                  <label className="text-[10px] font-black text-slate-500 uppercase tracking-widest ml-1">Nama Perusahaan (Header Struk)</label>\
                  <input\
                    type="text"\
                    value={settings.receipt_company_name || '"'"''"'"'}\
                    onChange={(e) => updateSettings({ ...settings, receipt_company_name: e.target.value })}\
                    placeholder="Contoh: Bali Top Tour"\
                    className="bg-slate-50 border border-slate-200 text-slate-800 text-xs font-bold rounded-xl px-4 py-2.5 focus:border-teal-300 focus:bg-white focus:ring-4 focus:ring-teal-100 transition-all outline-none"\
                  />\
                </div>\
\
                <div className="flex flex-col gap-1.5">\
                  <label className="text-[10px] font-black text-slate-500 uppercase tracking-widest ml-1">Teks Footer Struk</label>\
                  <textarea\
                    value={settings.receipt_footer || '"'"''"'"'}\
                    onChange={(e) => updateSettings({ ...settings, receipt_footer: e.target.value })}\
                    placeholder="Contoh: Terima kasih atas pesanan Anda. Semoga liburan Anda menyenangkan!"\
                    rows={2}\
                    className="bg-slate-50 border border-slate-200 text-slate-800 text-xs font-bold rounded-xl px-4 py-2.5 focus:border-teal-300 focus:bg-white focus:ring-4 focus:ring-teal-100 transition-all outline-none resize-none"\
                  />\
                </div>\
              </div>\
              \
              <div className="border-t border-slate-100 pt-5">\
                <h4 className="text-[10px] font-black text-slate-500 uppercase tracking-widest mb-3 flex justify-between items-center">\
                  Preview Struk\
                  <button onClick={() => {\
                    if (navigator.bluetooth) {\
                      navigator.bluetooth.requestDevice({ acceptAllDevices: true, optionalServices: ['"'"'000018f0-0000-1000-8000-00805f9b34fb'"'"'] }).then(device => { alert('"'"'Terhubung ke: '"'"' + device.name); }).catch(err => { console.error(err); alert('"'"'Koneksi gagal atau dibatalkan.'"'"'); });\
                    } else {\
                      alert('"'"'Web Bluetooth API tidak didukung di browser ini.'"'"');\
                    }\
                  }} className="text-teal-600 bg-teal-50 px-2 py-1 rounded flex items-center gap-1 active:scale-95 transition-all"><Printer size={12} /> Hubungkan Printer</button>\
                </h4>\
                \
                <div className={`bg-white border border-slate-200 shadow-sm mx-auto p-4 font-mono text-slate-800 \${settings.receipt_paper_size === '"'"'80mm'"'"' ? '"'"'max-w-[320px]'"'"' : '"'"'max-w-[240px]'"'"'} \${settings.receipt_layout === '"'"'left'"'"' ? '"'"'text-left'"'"' : '"'"'text-center'"'"'}`}>\
                  {settings.receipt_logo_url && (\
                    <img src={settings.receipt_logo_url} className={`h-12 mb-2 grayscale \${settings.receipt_layout === '"'"'left'"'"' ? '"'"'mr-auto'"'"' : '"'"'mx-auto'"'"'}`} alt="Logo" />\
                  )}\
                  <h4 className="font-bold text-sm mb-1">{settings.receipt_company_name || '"'"'BALI TOP TOUR'"'"'}</h4>\
                  <div className="text-[10px] border-b border-dashed border-slate-300 pb-2 mb-2">\
                    <p>Waktu: {new Date().toLocaleString()}</p>\
                    <p>Kasir: Admin</p>\
                  </div>\
                  <div className="text-[11px] mb-2 text-left">\
                    <p className="font-bold">Paket Wisata Bali 3 Hari</p>\
                    <div className="flex justify-between">\
                      <span>1x</span>\
                      <span>Rp 1.500.000</span>\
                    </div>\
                  </div>\
                  <div className="text-[11px] border-t border-dashed border-slate-300 pt-2 mb-3 text-left">\
                    <div className="flex justify-between font-bold">\
                      <span>TOTAL</span>\
                      <span>Rp 1.500.000</span>\
                    </div>\
                  </div>\
                  {settings.receipt_footer && (\
                    <p className="text-[9px] mt-4 whitespace-pre-wrap">{settings.receipt_footer}</p>\
                  )}\
                </div>\
              </div>\
            </div>\
          </div>\
        )}' src/views/AdminView.tsx
