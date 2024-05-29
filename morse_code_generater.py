# 모스코드 변환기

# 소개
lang = input("Welcome to the morse code coverter! Type your local language in capital letter. ex) ENG, KOR : ")

#  모스 부호 매핑 // ENG 예시
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 
    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', 
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', 
    '9': '----.', '0': '-----', '.': '.-.-.-', ' ': ' '
}             

# 모스 부호를 ENG 언어로 변환하는 딕셔너리 생성
MORSE_TO_TEXT_DICT = {morse: letter for letter, morse in MORSE_CODE_DICT.items()}

# ENG 언어를 모스 부호로 변환하는 함수
def text_to_morse(text):
    morse_code = ' '.join(MORSE_CODE_DICT.get(char.upper(), '') for char in text)
    return morse_code.strip()

# 모스 부호를 ENG 언어로 변환하는 함수 (공백 처리 포함)
def morse_to_text(morse_code):
    # 모스 부호에서 단어 사이는 3개의 공백으로, 글자 사이는 1개의 공백으로 구분
    words = morse_code.split('   ')  # 단어 사이의 공백(3개)을 기준으로 분리
    decoded_text = ''
    for word in words:
        letters = word.split(' ')  # 글자 사이의 공백(1개)을 기준으로 분리
        decoded_word = ''.join(MORSE_TO_TEXT_DICT.get(letter, '') for letter in letters)
        decoded_text += decoded_word + ' '  # 단어를 더할 때 단어 사이 공백 추가
    return decoded_text.strip()  # 양 끝의 불필요한 공백 제거

# 입력 언어가 영어일 시 처리 코드
if lang == "ENG":
    # 사용자 입력 처리 (텍스트 -> 모스 부호)
    input_text = input("Enter text to convert to Morse code: ")
    output_morse = text_to_morse(input_text)
    print("You typed: ", input_text)
    print("Here is Morse Code: ", output_morse)

# 모스부호 변환할 지 사용자 확인   
    response = input("Do you want to covert the morse code to your local language too? : (Y/N) ")
    if response == "Y":
        # 사용자 입력 처리 (모스 부호 -> 텍스트)
        input_morse = input("Enter Morse to convert to text: ")
        output_text = morse_to_text(input_morse)
        print("You typed: ", input_morse)
        print("Here is text: ", output_text)
    else :
        print("OK")
# 예외처리 구문, 딕셔너리와 함수상에 없는 언어를 타이핑 시 출력됨
# (언어 추가는 딕셔너리에 로컬 언어의 모스 코드를 추가한 후, else if문 사용하여 원하는 언어 추가하여 해결)
# 만약 언어별로 서로 다른 딕셔너리 구축을 요할시엔 변환 함수 별도로 재지정 필요
else :
    print("Sorry, We are not support the language what you typed yet. Please wait for us!")
