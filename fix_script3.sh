sed -i '2694,2723c\
                            }\
                            setApEditId('"'"''"'"');\
                            setApName('"'"''"'"');\
                            setApDesc('"'"''"'"');\
                            setApDuration(60);\
                            setApPricesList([{ keterangan: '"'"'Dewasa'"'"', harga: 100000 }]);\
                            setApUnit('"'"'/ Pax'"'"');\
                          }}\
                          disabled={isTranslating}\
                          className="flex-grow bg-pink-600 hover:bg-pink-700 disabled:opacity-50 text-white font-extrabold py-2 rounded-xl text-[10px] uppercase tracking-wider flex items-center justify-center gap-1.5"\
                        >\
                          {isTranslating ? <Loader2 size={12} className="animate-spin" /> : null}\
                          {apEditId \
                            ? (language === '"'"'zh'"'"' ? '"'"'保存更改'"'"' : language === '"'"'en'"'"' ? '"'"'Save Changes'"'"' : '"'"'Simpan Perubahan'"'"') \
                            : (language === '"'"'zh'"'"' ? '"'"'添加套餐'"'"' : language === '"'"'en'"'"' ? '"'"'Add Package'"'"' : '"'"'Tambah Paket'"'"')}\
                        </button>\
                        {apEditId && (\
                          <button\
                            type="button"\
                            onClick={() => {\
                              setApEditId('"'"''"'"');\
                              setApName('"'"''"'"');\
                              setApDesc('"'"''"'"');\
                              setApDuration(60);\
                              setApPricesList([{ keterangan: '"'"'Dewasa'"'"', harga: 100000 }]);\
                              setApUnit('"'"'/ Pax'"'"');\
                            }}\
                            className="border border-slate-200 text-slate-500 font-extrabold py-2 px-3 rounded-xl text-[10px] uppercase"\
                          >\
                            {language === '"'"'zh'"'"' ? '"'"'取消'"'"' : language === '"'"'en'"'"' ? '"'"'Cancel'"'"' : '"'"'Batal'"'"'}\
                          </button>\
                        )}\
                      </div>\
                    </div>\
                  </div>\
                </div>' src/views/AdminView.tsx
