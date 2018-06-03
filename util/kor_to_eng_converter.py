import math
import re
ENG_KEY = "rRseEfaqQtTdwWczxvgkoiOjpuPhynbml";
KOR_KEY = "ㄱㄲㄴㄷㄸㄹㅁㅂㅃㅅㅆㅇㅈㅉㅊㅋㅌㅍㅎㅏㅐㅑㅒㅓㅔㅕㅖㅗㅛㅜㅠㅡㅣ";
CHO_DATA = "ㄱㄲㄴㄷㄸㄹㅁㅂㅃㅅㅆㅇㅈㅉㅊㅋㅌㅍㅎ";
JUNG_DATA = "ㅏㅐㅑㅒㅓㅔㅕㅖㅗㅘㅙㅚㅛㅜㅝㅞㅟㅠㅡㅢㅣ";
JONG_DATA = "ㄱㄲㄳㄴㄵㄶㄷㄹㄺㄻㄼㄽㄾㄿㅀㅁㅂㅄㅅㅆㅇㅈㅊㅋㅌㅍㅎ";

def flatten_kor(ss):
    CHOSUNG_LIST = [u'ㄱ', u'ㄲ', u'ㄴ', u'ㄷ', u'ㄸ', u'ㄹ', u'ㅁ', u'ㅂ', u'ㅃ', u'ㅅ', u'ㅆ', u'ㅇ', u'ㅈ', u'ㅉ', u'ㅊ', u'ㅋ', u'ㅌ', u'ㅍ', u'ㅎ']
    JUNGSUNG_LIST = [u'ㅏ', u'ㅐ', u'ㅑ', u'ㅒ', u'ㅓ', u'ㅔ', u'ㅕ', u'ㅖ', u'ㅗ', u'ㅘ', u'ㅙ', u'ㅚ', u'ㅛ', u'ㅜ', u'ㅝ', u'ㅞ', u'ㅟ', u'ㅠ', u'ㅡ', u'ㅢ', u'ㅣ']
    JONGSUNG_LIST = [u' ', u'ㄱ', u'ㄲ', u'ㄳ', u'ㄴ', u'ㄵ', u'ㄶ', u'ㄷ', u'ㄹ', u'ㄺ', u'ㄻ', u'ㄼ', u'ㄽ', u'ㄾ', u'ㄿ', u'ㅀ', u'ㅁ', u'ㅂ', u'ㅄ', u'ㅅ', u'ㅆ', u'ㅇ', u'ㅈ', u'ㅊ', u'ㅋ', u'ㅌ', u'ㅍ', u'ㅎ']
    BASE_CODE, CHOSUNG, JUNGSUNG = 44032, 588, 28
    res = ''
    for charTemp in ss:
        cBase = ord(charTemp) - BASE_CODE
        c1 = int(cBase / CHOSUNG)
        c2 = int((cBase - (CHOSUNG * c1)) / JUNGSUNG)
        c3 = int((cBase - (CHOSUNG * c1) - (JUNGSUNG * c2)))
        s = CHOSUNG_LIST[c1] + JUNGSUNG_LIST[c2] + JONGSUNG_LIST[c3]
        res += s
    return res

def isHanguel(s):
    h = re.compile('[ㄱ-힣]+')
    if len(h.findall(s)) == 0:
        return False
    return True

def korTypeToEng(src):
    res = ""
    if len(src) == 0:
        return res

    for i in range(len(src)):
        ch = src[i]
        nCode = ord(ch)
        ch = flatten_kor(ch)
        nCho = CHO_DATA.find(ch[0])
        nJung = JUNG_DATA.find(ch[1])
        nJong = JONG_DATA.find(ch[2])
        arrKeyIndex = [-1, -1, -1, -1, -1]
        if 0xac00 <= nCode and nCode <= 0xd7a3:
            nCode -= 0xac00
            arrKeyIndex[0] = math.floor(nCode / (21 * 28)) #초성
            arrKeyIndex[1] = math.floor(nCode / 28) % 21  #중성
            arrKeyIndex[3] = nCode % 28 - 1               #종성
        elif nCho != -1: # 초성 자음
            arrKeyIndex[0] = nCho
        elif nJung != -1: #중성
            arrKeyIndex[1] = nJung
        elif nJong != -1: #종성 자음
            arrKeyIndex[3] = nJong
        else: #한글이 아님
            res += ch;
        # 실제 Key Index로 변경. 초성은 순서 동일
        if arrKeyIndex[1] != -1:
            if arrKeyIndex[1] == 9: #ㅘ
                arrKeyIndex[1] = 27
                arrKeyIndex[2] = 19
            elif (arrKeyIndex[1] == 10): #ㅙ
                arrKeyIndex[1] = 27
                arrKeyIndex[2] = 20
            elif arrKeyIndex[1] == 11: #ㅚ
                arrKeyIndex[1] = 27
                arrKeyIndex[2] = 32
            elif arrKeyIndex[1] == 14: #ㅝ
                arrKeyIndex[1] = 29
                arrKeyIndex[2] = 23
            elif arrKeyIndex[1] == 15: #ㅞ
                arrKeyIndex[1] = 29
                arrKeyIndex[2] = 24
            elif arrKeyIndex[1] == 16: #ㅟ
                arrKeyIndex[1] = 29
                arrKeyIndex[2] = 32
            elif arrKeyIndex[1] == 19: #ㅢ
                arrKeyIndex[1] = 31
                arrKeyIndex[2] = 32
            else:
                arrKeyIndex[1] = KOR_KEY.index(JUNG_DATA[(arrKeyIndex[1])])
                arrKeyIndex[2] = -1
        
        if arrKeyIndex[3] != -1:
            if arrKeyIndex[3] == 2: #ㄳ
                arrKeyIndex[3] = 0
                arrKeyIndex[4] = 9
            elif arrKeyIndex[3] == 4: #ㄵ
                arrKeyIndex[3] = 2
                arrKeyIndex[4] = 12
            elif arrKeyIndex[3] == 5: #ㄶ
                arrKeyIndex[3] = 2
                arrKeyIndex[4] = 18
            elif arrKeyIndex[3] == 8: #ㄺ
                arrKeyIndex[3] = 5
                arrKeyIndex[4] = 0
            elif arrKeyIndex[3] == 9: #ㄻ
                arrKeyIndex[3] = 5
                arrKeyIndex[4] = 6
            elif arrKeyIndex[3] == 10: #ㄼ
                arrKeyIndex[3] = 5
                arrKeyIndex[4] = 7
            elif arrKeyIndex[3] == 11: #ㄽ
                arrKeyIndex[3] = 5
                arrKeyIndex[4] = 9
            elif arrKeyIndex[3] == 12: #ㄾ
                arrKeyIndex[3] = 5
                arrKeyIndex[4] = 16
            elif arrKeyIndex[3] == 13: #ㄿ
                arrKeyIndex[3] = 5
                arrKeyIndex[4] = 17
            elif arrKeyIndex[3] == 14: #ㅀ
                arrKeyIndex[3] = 5
                arrKeyIndex[4] = 18
            elif arrKeyIndex[3] == 17: #ㅄ
                arrKeyIndex[3] = 7
                arrKeyIndex[4] = 9
            else:
                arrKeyIndex[3] = KOR_KEY.index(JONG_DATA[arrKeyIndex[3]])
                arrKeyIndex[4] = -1;

        for j in range(5):
            if arrKeyIndex[j] != -1:
                res += ENG_KEY[arrKeyIndex[j]];
    return res
