Tesseract OCR langdata for Simplified Chinese (China)

This is another trained tesseract data pack for Chinese OCR.
The training fonts includes commonly used fonts:

1. SimSun 
2. SimHei 
3. KaiTi 
4. DengXian 
5. DengXian Light 
6. Microsoft YaHei 
7. Noto Sans CJK SC
8. Noto Sans SC
9. Noto Sans SC Bold 
10. Noto Serif SC
11. Source Han Sans SC
12. Source Han Serif SC
13. FangSong
14. PingFang SC
15. LiGuoFu (Handwriting Chinese Font)

and more.

HOW TO TRAINING:

First, you need need prepare training text www.thepaper.cn. Copy text from 200-500 articles, then save as: chi_sim.training_text file.

Second, you use optimize_training_text.py to optimize training text (one line has 50-55 characters).

Third, you use split_training_textmultifont.py to create .gt.txt, .tif, .box for ground truth data. You can place them in folder: tesstrain/data/ranbac-ground-truth.

Now, you use:  make training MODEL_NAME=ranbac START_MODEL=chi_sim TESSDATA=../tessdata/ MAX_ITERATIONS=20000.

You can increase MAX_ITERATIONS to 80000 or larger, to achieve best BCER ~ 1%, BWER ~ 5%.

Drink a coffee, play games or sleep.

After training finish, you will receiver ranbac.traineddata in folder: tesstrain\data. 

Example: 

At iteration 6776/10000/10000, mean rms=0.477%, delta=1.299%, BCER train=4.644%, BWER train=45.050%, skip ratio=0.000%, New worst BCER = 4.644 wrote checkpoint.

Finished! Selected model with minimal training error rate (BCER) = 3.795


