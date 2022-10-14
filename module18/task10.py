print('Задача 10. Истина\n')

ENCRYPTED_TEXT = 'vujgvmCfb tj ufscfu ouib z/vhm jdjuFyqm jt fscfuu uibo jdju/jnqm fTjnqm tj scfuuf ibou fy/dpnqm ' \
                 'yDpnqmf jt cfuufs boui dbufe/dpnqmj uGmb tj fuufsc ouib oftufe/ bstfTq jt uufscf uibo otf/ef ' \
                 'uzSfbebcjmj vout/dp djbmTqf dbtft (ubsfo djbmtqf hifopv up csfbl ifu t/svmf ipvhiBmu zqsbdujdbmju ' \
                 'fbutc uz/qvsj Fsspst tipvme wfsof qbtt foumz/tjm omfttV mjdjumzfyq odfe/tjmf Jo fui dfgb pg ' \
                 'hvjuz-bncj gvtfsf fui ubujpoufnq up ftt/hv Uifsf vmetip fc pof.. boe sbcmzqsfgf zpom pof pvt..pcwj ' \
                 'xbz pu pe ju/ Bmuipvhi uibu bzx bzn puo cf wjpvtpc bu jstug ttvomf sfzpv( i/Evud xOp tj scfuuf ibou ' \
                 '/ofwfs uipvhiBm fsofw jt fopgu cfuufs boui iu++sjh x/op gJ ifu nfoubujpojnqmf tj eibs pu mbjo-fyq ' \
                 'tju( b bec /jefb Jg fui foubujpojnqmfn jt fbtz up bjo-fyqm ju znb cf b hppe jefb/ bnftqbdftO bsf ' \
                 'pof ipoljoh sfbuh efbj .. fu(tm pe psfn gp tf"uip'


def cesar_decrypt(text: str, shift: int):
    return ''.join([
        chr(ord(symbol) - shift) if 32 < ord(symbol) < 127
        else symbol
        for symbol in text
    ])


def decrypt_word_shift(text: str, shift: int):
    result = []
    for word in text.split(' '):
        word_shift = -shift % len(word)
        decrypted_word = ''.join([word[word_shift:], word[:word_shift]])

        if decrypted_word.endswith('.'):
            shift += 1

        result.append(decrypted_word)

    return ' '.join(result).replace('. ', '.\n')


decrypted = decrypt_word_shift(cesar_decrypt(ENCRYPTED_TEXT, 1), 3)
print(decrypted)
