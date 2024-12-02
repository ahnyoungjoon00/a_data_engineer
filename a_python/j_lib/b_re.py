"""
정규표현식
"""
import re
from util import check_re

def reg_exp1() :
    # 정규표현식
    # r'', re.compile()
    exp = r'python'
    text = 'easy python lib python regular expression'

    # search : 문자열 전체 탐색
    res = re.search(exp, text)
    if (res) :
        print("search complete : ", res, res.group()) # group : 위치값이 아닌 일치하는 문자열 자체를 출력
    else :
        print("not exist")
    print("===============================")

    # match : 문자열 시작부분을 탐색
    res = re.match(exp, text)
    if (res) :
        print("match : ", res, res.group())
    else :
        print("match : ", "not exist")
    print("===============================")

    # split : 구분자로 사용하여 문자열 분리
    res = re.split(exp, text)
    print(res)
    print("===============================")

    # findall : 문자열 내 존재하는 패턴(exp)을 모두 찾아 출력
    res = re.findall(exp, text)
    print(res)
    print("===============================")
# reg_exp1()

def reg_exp2() :
    """
    앵커문자
    ^ : ^ 뒤에 오는 패턴으로 시작하는 문자열 줄 인가?
    $ : $ 앞에 오는 패턴으로 종료되는 문자열 줄 인가?
    """
    text1 = "python script is a module"
    text2 = "is script a module in python"

    exp1 = r"^python"
    exp2 = r"python$"

    # 문자열이 python으로 시작하는가?
    check_re(exp1, text1)
    check_re(exp1, text2)

    # 문자열이 python으로 끝나는가?
    check_re(exp2, text1)
    check_re(exp2, text2)
# reg_exp2()

def reg_exp3() :
    """
    flag 문자
    정규표현식이 탐색할 범위를 지정
    i : 대소문자를 구분하지 않고 검색
    m : 모든 행에 대해 패턴을 검색
    """
    text = """PYTHON, javajscript
    html, css, matplotlib python
    database, pandas"""

    exp1 = r"^python"
    exp_f = r"(?i)^python"
    exp2 = r"python$"
    exp2_f = r"(?m)python$"
    exp3_f = r"(?im)python$"
    exp4_f = r"(?mi)python$"

    check_re(exp1, text)
    check_re(exp1, text, re.IGNORECASE)
    check_re(exp_f, text)
    print("===============================")
    check_re(exp2, text)
    check_re(exp2, text, re.MULTILINE)
    check_re(exp2, text, re.IGNORECASE | re.MULTILINE)
    check_re(exp2_f, text)
    print("===============================")
    check_re(exp3_f, text)
    check_re(exp4_f, text)
# reg_exp3()

def reg_exp4() :
    """
    문자셋
    []로 묶어준다. [] 안에서 "^"는 not의 의미를 가진다.
    문자셋 안의 패턴은 or 연산으로 수행된다.
    
    1. 숫자 : [0-9]
    2. 알파벳 소문자 : [a-z]
    3. 알파벳 대문자 : [A-Z]
    4. 알파벳 :[a-zA-Z]
    5. 한글 : [ㄱ-힣]
    6. 특수문자 : [^a-zA-Z0-9ㄱ-힣]
                영어, 숫자, 한글이 아닌 문자 -> 특수문자
    7. escape 문자 : 즐비꿈 등, 문자열로 표현하고 싶은데 방법이 없는 것들
    \n, \r\n : 줄바꿈
    \b : backspace
    \t, \' 
    '\'' == "'"
    """
    print("a\ta\nb")
    
    text = """1. PYTHON, 2.javajscript
    3.html, 4.css, 5.matplotlib 6.파이썬
    7.database, 10.판다스"""
    
    exp_num = r'[0-9]'
    exp_lowwe_alp = r'[a-z]'
    exp_upper_alp = r'[A-Z]'
    exp_alp = r'[a-zA-Z]'
    exp_kor = r'[ㄱ-힣]'
    exp_etc = r'[^a-zA-Z0-9ㄱ-힣\n]'

    print(re.sub(exp_num, "*", text))
    print("===============================")
    print(re.sub(exp_lowwe_alp, "*", text))
    print("===============================")
    print(re.sub(exp_upper_alp, "*", text))
    print("===============================")
    print(re.sub(exp_alp, "*", text))
    print("===============================")
    print(re.sub(exp_kor, "*", text))
    print("===============================")
    print(re.sub(exp_etc, "*", text))
# reg_exp4()

def reg_stack() :
    exp_kor2 = r'[ㄱ-힣][ㄱ-힣]' # 한글로 이루어진 2글자 문자를 검사
    exp_kor3 = r'[ㄱ-힣][ㄱ-힣][ㄱ-힣]' # 한글로 이루어진 3글자 문자를 검사
    exp_kor4 = r'[ㄱ-힣][ㄱ-힣][ㄱ-힣][ㄱ-힣]' # 한글로 이루어진 4글자 문자를 검사
    text = """1. PYTHON, 2.javajscript
    3.html, 4.css, 5.matplotlib 6.파이썬
    7.database, 10.판다스"""

    print(re.sub(exp_kor2, "*", text))
    print("===============================")
    print(re.sub(exp_kor3, "*", text))
    print("===============================")
    print(re.sub(exp_kor4, "*", text))
    print("===============================")
# reg_stack()

def reg_national_id() :
    """
    주민등록번호를 검증하는 정규표현식을 만드시오
    숫자 6자리 - 숫자 7자리
    주민등록번호의 - 뒤 첫 숫자는 1-4사이의 숫자만 올 수 있다.
    """
    exp = r'[0-9][0-9][0-9][0-9][0-9][0-9]-[1-4][0-9][0-9][0-9][0-9][0-9][0-9]'
    text = "name, 19, pro, 000000-1000000, 경기도"
    check_re(exp, text)
    # id = input("주민등록번호 :").split(sep = "-")
    # if not((len(id[0]) == 6) and (len(id[1]) == 7)) :
    #     print("잘못된 번호입니다.")
    #     return
    # exp = r"[1-4]"
    # elif re.search(exp, id[1]) == False :
# reg_national_id()

def reg_exp5() :
    """
    특수문자
    . : 줄바꿈문자를 제외한 모든 단일 문자
    \d : 숫자 == [0-9]
    \D : 숫자가 아닌 [^0-9]
    \w : 밑줄 문자를 포함한 숫자와 문자 [a-zA-z0-9_]
    \W : 밑줄 문자를 포함한 숫자와 문자가 아닌 [^a-zA-z0-9_]
    
    수량문자
    + 패턴이 1개 이상
    * 패턴이 0개 이상
    ? 패턴이 0개 또는 1개 존재
    {n} 패턴이 n개 존재
    {n, m} 패턴이 n~m개 존재
    {n, } 패턴이 n개 이상 존재
    """
    text = """1. PYTHON, 2.java___script
    3.html, 4.css, 5.matplotlib 6.파이썬
    7.database, 8.판다스 
    """

    print(re.sub(r'.', "*", text))
    print("===============================")
    print(re.sub(r'\d', "*", text))
    print("===============================")
    print(re.sub(r'\D', "*", text))
    print("===============================")
    print(re.sub(r'\w', "*", text))
    print("===============================")
    print(re.sub(r'\W', "*", text))
    print("===============================")
    exp = r'\d{6}-[1-4]\d{6}'
    text = "name, 19, pro, 000000-1000000, 경기도"
    check_re(exp, text)
# reg_exp5()

def reg_exp6() :
    """
    () : 그룹
    | : 그룹 안에서 패턴을 or 로 묶어줄 수 있음
    
    주민등록번호 최종
    연도 : 숫자2자리    -> \d{2}
    월 : 01-09 | 11-12 -> (0[1-9]|1[0-2])
    일 : 01-31         -> (0[1-9]|[1-2]\d|3[0-1])
    """
    exp = r'\d{2}(0[1-9]|1[0-2])(0[1-9]|[1-2]\d|3[0-1])-[1-4]\d{6}'
    text = "name, 19, pro, 000000-1000000, 경기도"
    check_re(exp, text)
reg_exp6()