sed -i '2581,2703c\
                          </div>\
                        ))}\
                        <button\
                          type="button"\
                          onClick={() => setApPricesList([...apPricesList, { keterangan: '"'"''"'"', harga: 0 }])}\
                          className="mt-1 text-[10px] font-bold text-indigo-600 hover:text-indigo-700 flex items-center justify-center gap-1 py-1.5 border border-dashed border-indigo-200 rounded-lg bg-indigo-50/50 hover:bg-indigo-100 transition-colors"\
                        >\
                          + Tambah Harga\
                        </button>\
                      </div>\
                      <div className="flex gap-2.5 mt-1">\
                        <button\
                          type="button"\
                          onClick={async () => {\
                            if (!apName.trim()) return;\
                            setIsTranslating(true);\
                            const textToTranslate = [apName, apDesc, ...apPricesList.map(p => p.keterangan || '"'"''"'"')];\
                            let trans = { en: textToTranslate, zh: textToTranslate, id: textToTranslate };\
                            try {\
                              trans = await translateTexts(textToTranslate);\
                            } catch (e) {\
                              console.error(e);\
                            } finally {\
                              setIsTranslating(false);\
                            }\
                            const pkgId = apEditId || '"'"'ap-'"'"' + Date.now();\
                            if (apEditId) {\
                              const existing = activityPackages.find(p => p.id === apEditId);\
                              updateActivityPackage({\
                                ...existing,\
                                id: apEditId,\
                                activity_id: editingAct.id,\
                                name: apName.trim(),\
                                name_id: apName.trim(),\
                                name_en: trans.en[0] || apName.trim(),\
                                name_zh: trans.zh[0] || apName.trim(),\
                                description: apDesc.trim(),\
                                description_id: apDesc.trim(),\
                                description_en: trans.en[1] || apDesc.trim(),\
                                description_zh: trans.zh[1] || apDesc.trim(),\
                                duration_minutes: apDuration || 60,\
                                sort_order: existing?.sort_order || 0\
                              });\
                              const existingPrices = activityPackagePrices.filter(pr => pr.activity_package_id === apEditId);\
                              for (let i = 0; i < apPricesList.length; i++) {\
                                const item = apPricesList[i];\
                                const labelFull = item.keterangan ? `${item.keterangan} ${apUnit}` : apUnit;\
                                const enLabelFull = trans.en[i + 2] ? `${trans.en[i + 2]} ${apUnit}` : labelFull;\
                                const zhLabelFull = trans.zh[i + 2] ? `${trans.zh[i + 2]} ${apUnit}` : labelFull;\
                                if (item.id) {\
                                  updateActivityPackagePrice({\
                                    id: item.id,\
                                    activity_package_id: apEditId,\
                                    price_idr: item.harga,\
                                    label: labelFull,\
                                    label_id: item.keterangan,\
                                    label_en: enLabelFull,\
                                    label_zh: zhLabelFull,\
                                    sort_order: i\
                                  });\
                                } else {\
                                  addActivityPackagePrice({\
                                    id: '"'"'app-'"'"' + Date.now() + i,\
                                    activity_package_id: apEditId,\
                                    label: labelFull,\
                                    label_id: item.keterangan,\
                                    label_en: enLabelFull,\
                                    label_zh: zhLabelFull,\
                                    price_idr: item.harga,\
                                    sort_order: i\
                                  });\
                                }\
                              }\
                              for (const exPr of existingPrices) {\
                                if (!apPricesList.find(p => p.id === exPr.id)) {\
                                  deleteActivityPackagePrice(exPr.id);\
                                }\
                              }\
                            } else {\
                              addActivityPackage({\
                                id: pkgId,\
                                activity_id: editingAct.id,\
                                name: apName.trim(),\
                                name_id: apName.trim(),\
                                name_en: trans.en[0] || apName.trim(),\
                                name_zh: trans.zh[0] || apName.trim(),\
                                description: apDesc.trim(),\
                                description_id: apDesc.trim(),\
                                description_en: trans.en[1] || apDesc.trim(),\
                                description_zh: trans.zh[1] || apDesc.trim(),\
                                duration_minutes: apDuration || 60,\
                                sort_order: activityPackages.filter(p => p.activity_id === editingAct.id).length\
                              });\
                              for (let i = 0; i < apPricesList.length; i++) {\
                                const item = apPricesList[i];\
                                const labelFull = item.keterangan ? `${item.keterangan} ${apUnit}` : apUnit;\
                                const enLabelFull = trans.en[i + 2] ? `${trans.en[i + 2]} ${apUnit}` : labelFull;\
                                const zhLabelFull = trans.zh[i + 2] ? `${trans.zh[i + 2]} ${apUnit}` : labelFull;\
                                addActivityPackagePrice({\
                                  id: '"'"'app-'"'"' + Date.now() + i,\
                                  activity_package_id: pkgId,\
                                  label: labelFull,\
                                  label_id: item.keterangan,\
                                  label_en: enLabelFull,\
                                  label_zh: zhLabelFull,\
                                  price_idr: item.harga,\
                                  sort_order: i\
                                });\
                              }\
                            }\
' src/views/AdminView.tsx
