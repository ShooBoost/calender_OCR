"""
import PIL
print(PIL)

import sys
print(sys.path)
"""
# import _imaging


from PIL import Image
import pytesseract

# 找出 tesseract 安裝的地方
# 將 pytesseract 指向該位子，這樣才能讓 pytesseract 可以使用 tesseract
pytesseract.pytesseract.tesseract_cmd = r'/usr/local/Cellar/tesseract/4.1.1/bin/tesseract'

# chi_sim.traineddata 要放在跟剛剛的 tesseract 旗下的 tessdata 資料夾耶
# eng.traineddata
# chi_tra.traineddata
# 各種語言的 traineddata 都是喔喔喔
img = Image.open('test_sim.jpeg')
text = pytesseract.image_to_string(img, lang='chi_sim')
print(text)

img_tra = Image.open('test2.PNG')
text_tra = pytesseract.image_to_string(img_tra, lang='chi_tra')
print(text_tra)
