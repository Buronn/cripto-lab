import random
def randomNumberGenerator():
    phone = "9"
    for i in range(8):
        phone += str(random.randint(0, 9))
    return phone
def randomNameGenerator():
    name = ""
    for i in range(random.randint(3, 10)):
        name += chr(random.randint(65, 90))
    return name
def randomPasswordGenerator():
    password = ""
    for i in range(random.randint(6, 10)):
        password += chr(random.randint(65, 90))
    for i in range(random.randint(6, 10)):
        password += chr(random.randint(97, 122))
    for i in range(random.randint(6, 10)):
        password += str(random.randint(0, 9))
    for i in range(random.randint(6, 7)):
        password += chr(random.randint(45, 47))
    return password
def randomPasswordGeneratorLength(length):
    password = ""
    for i in range(length):
        password += chr(random.randint(33, 126))
    return password
def randomPasswordEmojiGenerator(length):
    emojis = ["🤓", "😎", "😍", "😘", "😚", "😋", "😛", "😜", "😝", "😁", "😂", "😃", "😄", "😅", "😆", "😉", "😊", "😋", "😌", "😍", "😏", "😒", "😓", "😔", "😖", "😘", "😚", "😜", "😝", "😞", "😟", "😠", "😡", "😢", "😣", "😤", "😥", "😦", "😧", "😨", "😩", "😪", "😫", "😬", "😭", "😮", "😯", "😰", "😱", "😲", "😳", "😴", "😵", "😶", "😷", "😸", "😹", "😺", "😻", "😼", "😽", "😾", "😿", "🙀", "🙅", "🙆", "🙇", "🙈", "🙉", "🙊", "🙋", "🙌", "🙍", "🙎", "🙏", "🚀", "🚁", "🚂", "🚃", "🚄", "🚅", "🚆", "🚇", "🚈", "🚉", "🚊", "🚋", "🚌", "🚍", "🚎", "🚏", "🚐", "🚑", "🚒", "🚓", "🚔", "🚕", "🚖", "🚗", "🚘", "🚙", "🚚", "🚛", "🚜", "🚝", "🚞", "🚟", "🚠", "🚡", "🚢", "🚣", "🚤"]
    password = ""
    for i in range(length):
        password += random.choice(emojis)
    return password
def randomPasswordLatinGenerator(length):
    latin_chars = ["¡", "¢", "£", "¤", "¥", "¦", "§", "¨", "©", "ª", "«", "¬", "®", "¯", "°", "±", "²", "³", "´", "µ", "¶", "·", "¸", "¹", "º", "»", "¼", "½", "¾", "¿", "À", "Á", "Â", "Ã", "Ä", "Å", "Æ", "Ç", "È", "É", "Ê", "Ë", "Ì", "Í", "Î", "Ï", "Ð", "Ñ", "Ò", "Ó", "Ô", "Õ", "Ö", "×", "Ø", "Ù", "Ú", "Û", "Ü", "Ý", "Þ", "ß", "à", "á", "â", "ã", "ä", "å", "æ", "ç", "è", "é", "ê", "ë", "ì", "í", "î", "ï", "ð", "ñ", "ò", "ó", "ô", "õ", "ö", "÷", "ø", "ù", "ú", "û", "ü", "ý", "þ", "ÿ", "Ā", "ā", "Ă", "ă", "Ą", "ą", "Ć", "ć", "Ĉ", "ĉ", "Ċ", "ċ", "Č", "č", "Ď", "ď", "Đ", "đ", "Ē", "ē", "Ĕ", "ĕ", "Ė", "ė", "Ę", "ę", "Ě", "ě", "Ĝ", "ĝ", "Ğ", "ğ", "Ġ", "ġ", "Ģ", "ģ", "Ĥ", "ĥ", "Ħ", "ħ", "Ĩ", "ĩ", "Ī", "ī", "Ĭ"]
    password = ""
    for i in range(length):
        password += random.choice(latin_chars)
    return password
def randomPasswordLatinExtendedGenerator(length):
    latin_chars = ["ƀ", "Ɓ", "Ƃ", "ƃ", "Ƅ", "ƅ", "Ɔ", "Ƈ", "ƈ", "Ɖ", "Ɗ", "Ƌ", "ƌ", "ƍ", "Ǝ", "Ə", "Ɛ", "Ƒ", "ƒ", "Ɠ", "Ɣ", "ƕ", "Ɩ", "Ɨ", "Ƙ", "ƙ", "ƚ", "ƛ", "Ɯ", "Ɲ", "ƞ", "Ɵ", "Ơ", "ơ", "Ƣ", "ƣ", "Ƥ", "ƥ", "Ʀ", "Ƨ", "ƨ", "Ʃ", "ƪ", "ƫ", "Ƭ", "ƭ", "Ʈ", "Ư", "ư", "Ʊ", "Ʋ", "Ƴ", "ƴ", "Ƶ", "ƶ", "Ʒ", "Ƹ", "ƹ", "ƺ", "ƻ", "Ƽ", "ƽ", "ƾ", "ƿ", "ǀ", "ǁ", "ǂ", "ǃ", "Ǆ", "ǅ", "ǆ", "Ǉ", "ǈ", "ǉ", "Ǌ", "ǋ", "ǌ", "Ǎ", "ǎ", "Ǐ", "ǐ", "Ǒ", "ǒ", "Ǔ", "ǔ", "Ǖ", "ǖ", "Ǘ", "ǘ", "Ǚ", "ǚ", "Ǜ", "ǜ", "ǝ", "Ǟ", "ǟ", "Ǡ", "ǡ", "Ǣ", "ǣ", "Ǥ", "ǥ", "Ǧ", "ǧ", "Ǩ", "ǩ", "Ǫ", "ǫ", "Ǭ", "ǭ", "Ǯ", "ǯ", "ǰ", "Ǳ", "ǲ", "ǳ", "Ǵ", "ǵ", "Ƕ", "Ƿ", "Ǹ", "ǹ", "Ǻ", "ǻ", "Ǽ", "ǽ"]
    password = ""
    for i in range(length):
        password += random.choice(latin_chars)
    return password
def randomPasswordSubscriptsGenerator(length):
    subscripts = ["₀", "₁", "₂", "₃", "₄", "₅", "₆", "₇", "₈", "₉", "₊", "₋", "₌", "₍", "₎", "ₐ", "ₑ", "ₒ", "ₓ", "ₔ", "ₕ", "ₖ", "ₗ", "ₘ", "ₙ", "ₚ", "ₛ", "ₜ", "₝", "₞", "₟", "₠", "₡", "₢", "₣", "₤", "₥", "₦", "₧", "₨", "₩", "₪", "₫", "₭", "₮", "₯", "₰", "₱", "₲", "₳", "₴", "₵", "₶", "₷", "₸", "₹", "₺", "₻", "₼", "₽", "₾", "₿", "⃀", "⃁", "⃂", "⃃", "⃄", "⃅", "⃆", "⃇", "⃈", "⃉", "⃊", "⃋", "⃌", "⃍", "⃎", "⃏", "⃐", "⃑", "⃒", "⃓", "⃔", "⃕", "⃖", "⃗", "⃘", "⃙", "⃚", "⃛", "⃜", "⃝", "⃞", "⃟", "⃠", "⃡", "⃢", "⃣", "⃤"]
    password = ""
    for i in range(length):
        password += random.choice(subscripts)
    return password
def randomPasswordSuperscriptsGenerator(length):
    superscripts = ["⁰", "ⁱ", "⁲", "⁳", "⁴", "⁵", "⁶", "⁷", "⁸", "⁹", "⁺", "⁻", "⁼", "⁽", "⁾", "ⁿ", "₀", "₁", "₂", "₃", "₄", "₅", "₆", "₇", "₈", "₉", "₊", "₋", "₌", "₍", "₎", "ₐ", "ₑ", "ₒ", "ₓ", "ₔ", "ₕ", "ₖ", "ₗ", "ₘ", "ₙ", "ₚ", "ₛ", "ₜ", "₝", "₞", "₟", "₠", "₡", "₢", "₣", "₤", "₥", "₦", "₧", "₨", "₩", "₪", "₫", "₭", "₮", "₯", "₰", "₱", "₲", "₳", "₴", "₵", "₶", "₷", "₸", "₹", "₺", "₻", "₼", "₽", "₾", "₿", "⃀", "⃁", "⃂", "⃃", "⃄", "⃅", "⃆", "⃇", "⃈", "⃉", "⃊", "⃋", "⃌", "⃍", "⃎", "⃏", "⃐", "⃑", "⃒", "⃓", "⃔", "⃕", "⃖", "⃗"]
    password = ""
    for i in range(length):
        password += random.choice(superscripts)
    return password
def randomPasswordASCIIGenerator(length):
    password = ""
    for i in range(length):
        password += chr(random.randint(0,255))
    return password
def randomPasswordOneLetterPerAlphabetGenerator(length):
    chars = ["a", "ﺏ", "b", "ﺐ", "c", "ﺑ", "d", "ﺒ", "e", "ﺓ", "f", "ﺔ", "g", "ﺕ", "h", "ﺖ", "i", "ﺗ", "j", "ﺘ", "k", "ﺙ", "l", "ﺚ", "m", "ﺛ", "n", "ﺜ", "o", "ﺝ", "p", "ﺞ", "q", "ﺟ", "r", "ﺠ", "s", "ﺡ", "t", "ﺢ", "u", "ﺣ", "v", "ﺤ", "w", "ﺥ", "x", "ﺦ", "y", "ﺧ", "z", "ﺨ", "A", "ﺩ", "B", "ﺪ", "C", "ﺫ", "D", "ﺬ", "E", "ﺭ", "F", "ﺮ", "G", "ﺯ", "H", "ﺰ", "I", "ﺱ", "J", "ﺲ", "K", "ﺳ", "L", "ﺴ", "M", "ﺵ", "N", "ﺶ", "O", "ﺷ", "P", "ﺸ", "Q", "ﺹ", "R", "ﺺ", "S", "ﺻ", "T", "ﺼ", "U", "ﺽ", "V", "ﺾ", "W", "ﺿ", "X", "ﻀ", "Y", "ﻁ", "Z", "ﻂ", "0", "ﻃ", "1", "ﻄ", "2", "ﻅ", "3", "ﻆ", "4", "ﻇ", "5", "ﻈ", "6", "ﻉ", "7", "ﻊ", "8", "ﻋ", "9", "ﻌ", "!", "ﻍ", "\""]
    password = ""
    for i in range(length):
        password += random.choice(chars)
    return password
