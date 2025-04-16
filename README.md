Tesseract OCR langdata for Simplified Chinese (China)

This is another trained tesseract data pack for Chinese OCR, more accurate than the https://github.com/tesseract-ocr/tessdata_best
The training fonts includes commonly used fonts:
SimSun 
SimHei 
KaiTi 
DengXian 
DengXian Light 
Microsoft YaHei 
Noto Sans CJK SC
Noto Sans SC
Noto Sans SC Bold 
Noto Serif SC
Source Han Sans SC
Source Han Serif SC
FangSong
PingFang SC
LiGuoFu (Handwriting Chinese Font)

and more.
How to train: 
First, you need need prepare training text www.thepaper.cn. Copy 200-500 articles.
Second, you use optimize_training_text.py to optimize training text (one line has 50-55 characters).
Third, you use split_training_textmultifont.py to create .gt.txt, .tif, .box for ground truth data. You can place them in folder: tesstrain/data/ranbac-ground-truth.
Now, you use:  make training MODEL_NAME=ranbac START_MODEL=chi_sim TESSDATA=../tessdata/ MAX_ITERATIONS=20000.
Drink a coffee, play games or sleep.
You can increase MAX_ITERATIONS to 80000 or larger, to achieve best BCER ~ 1%, BWER ~ 5%.
After training finish, you will receiver ranbac.traineddata in folder: tesstrain\data. 
Example: At iteration 6776/10000/10000, mean rms=0.477%, delta=1.299%, BCER train=4.644%, BWER train=45.050%, skip ratio=0.000%, New worst BCER = 4.644 wrote checkpoint.
Finished! Selected model with minimal training error rate (BCER) = 3.795


