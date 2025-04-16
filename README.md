I. Tesseract OCR langdata for Simplified Chinese (China)

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

II. HOW TO PREPARE for ground truth data
1. Install fonts and check fonts.
2. Prepare training text
3. Copy text from www.thepaper.cn. (100-200 articles), then save as: First_chi_sim_trainingtext.txt
4. Use optimize_training_text.py to optimize training text (one line has 50-55 characters). You will have chi_sim_trainingtext.txt. Copy all content from chi_sim_trainingtext.txt to chi_sim.training_text. Place file chi_sim.training_text in folder: /langdata
5. Use split_training_textmultifont.py to create .gt.txt, .tif, .box for ground truth data. You can place them in folder: tesstrain/data/ranbac-ground-truth.

III. HOW TO PREPARE for data

Copy all file from langdata folder: ranbac.numbers, ranbac.punc, ranbac.traineddata, ranbac.unicharset, ranbac.wordlist, then place them in folder: tesstrain\data\ranbac

HOW TO PREPARE Training tools:

Download from: https://github.com/tesseract-ocr/tesstrain, then extract, you have tesstrain folder. Then read Installation.

IV. HOW TO TRAINING:

At tesstrain folder, open Git Bash

$ make training MODEL_NAME=ranbac START_MODEL=chi_sim TESSDATA=../tessdata/ MAX_ITERATIONS=20000.

You can increase MAX_ITERATIONS to 80000 or larger, to achieve best BCER ~ 1%, BWER ~ 5%.

Drink a coffee, play games or sleep.

After training finish, you will receiver ranbac.traineddata in folder: tesstrain\data. 

Example: 

At iteration 6776/10000/10000, mean rms=0.477%, delta=1.299%, BCER train=4.644%, BWER train=45.050%, skip ratio=0.000%, New worst BCER = 4.644 wrote checkpoint.

Finished! Selected model with minimal training error rate (BCER) = 3.795


