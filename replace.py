list_en_up = ["Q","W","E","R","T","Y","U","I","O","P","{","}","A","S","D","F","G","H","J","K","L",":",'"',"|","Z","X","C","V","B","N","M","<",">","?"]
list_en_low = ["q","w","e","r","t","y","u","i","o","p","[","]","a","s","d","f","g","h","j","k","l",";","'","\\","z","x","c","v","b","n","m",",",".","/"]

list_ru_up =  ["Й","Ц","У","К","Е","Н","Г","Ш","Щ","З","Х","Ъ","Ф","Ы","В","А","П","Р","О","Л","Д","Ж","Э","/","Я","Ч","С","М","И","Т","Ь","Б","Ю",","]
list_ru_low = ["й","ц","у","к","е","н","г","ш","щ","з","х","ъ","ф","ы","в","а","п","р","о","л","д","ж","э","\\","я","ч","с","м","и","т","ь","б","ю","."]

list_ua_up = ["Й","Ц","У","К","Е","Н","Г","Ш","Щ","З","Х","Ї","Ф","І","В","А","П","Р","О","Л","Д","Ж","Є","Ґ","Я","Ч","С","М","И","Т","Ь","Б","Ю",","]
list_ua_low = ["й","ц","у","к","е","н","г","ш","щ","з","х","ї","ф","і","в","а","п","р","о","л","д","ж","є","ґ","я","ч","с","м","и","т","ь","б","ю","."]

list_en = list_en_up + list_en_low
list_ua = list_ua_up + list_ua_low

REPLACE = {}    
for key, value in zip(list_en, list_ua):
    REPLACE[ord(key)] = value


def abc_replace(message_text):
    if len(message_text) > 2:
        for i in message_text:
            if i in list_ru_up or i in list_ru_low or i in list_ua_up or i in list_ua_low:
                return message_text
        return message_text.translate(REPLACE)
    else:
        return message_text