import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# 이미지 파일 로드
image = cv2.imread('2023SPRING_TICKET_INFO.jpg') #이미지 파일 입력

# 이미지 전처리를 위해 흑백으로 변환
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 이미지에서 텍스트 추출
text = pytesseract.image_to_string(gray, lang='kor')

# 추출한 텍스트 출력
print(text)