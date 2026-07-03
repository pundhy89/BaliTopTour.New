sed -i '3485,3500c\
                  {settings.receipt_footer && (\
                    <p className="text-[9px] mt-4 whitespace-pre-wrap">{settings.receipt_footer}</p>\
                  )}\
                </div>\
              </div>\
            </div>\
          </div>\
        )}\
      </div>\
    </div>\
  );\
}' src/views/AdminView.tsx
