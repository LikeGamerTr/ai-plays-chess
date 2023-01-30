import pyscreenshot
from paddleocr import PaddleOCR

ocr = PaddleOCR(use_angle_cls=True, lang='en')
for i in range(0,6):
    img_path = 'testRun\\imgs\\img_'+str(i)+".png"
    ss = pyscreenshot.grab(bbox=(1200, 580, 1800, 910))
    ss.save(img_path)
    result = ocr.ocr(img_path, cls=True)
    print(result)
