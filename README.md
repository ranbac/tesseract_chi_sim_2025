I. Tesseract OCR langdata for Simplified Chinese (China)

This is another trained tesseract data pack for Chinese OCR.
The training fonts includes commonly used fonts:

1. SimSun  
2. SimHei  
3. KaiTi  
4. DengXian  
5. Microsoft YaHei  
6. Noto Serif SC  
7. Source Han Serif SC  
8. FangSong  
9. PingFang SC  
10. Noto Sans SC  
11. Source Han Sans SC  
12. WenQuanYi Zen Hei Medium  

II. HOW TO PREPARE Training tools:

Download from: https://github.com/tesseract-ocr/tesstrain, then extract, you have tesstrain folder. Then read Installation.

III. HOW TO PREPARE for ground truth data
1. Install fonts and check fonts.
2. Prepare training text
3. Copy text from articles of www.thepaper.cn. (100-200 articles), then save as: First_chi_sim_trainingtext.txt
4. Use optimize_training_text.py to optimize training text (one line has 50-55 characters). You will have chi_sim_trainingtext.txt. Copy all content from chi_sim_trainingtext.txt to chi_sim.training_text (in  langdata folder)
5. You can add content to my file chi_sim.training_text (7.87 MB) (Use Notepad)
6. Use split_training_textmultifont.py to create .gt.txt, .tif, .box for ground truth data. You can place them in folder: tesstrain/data/ranbac-ground-truth.

IV. HOW TO TRAINING

At tesstrain folder, open Git Bash

$ make training MODEL_NAME=ranbac START_MODEL=chi_sim TESSDATA=../tessdata/ MAX_ITERATIONS=20000.

You can increase MAX_ITERATIONS to 80000 or larger, to achieve best BCER ~ 1%, BWER ~ 5%.

Drink a coffee, play games or sleep.

After training finish, you will receiver ranbac.traineddata in folder: tesstrain\data. 

Example: 

At iteration 6776/10000/10000, mean rms=0.477%, delta=1.299%, BCER train=4.644%, BWER train=45.050%, skip ratio=0.000%, New worst BCER = 4.644 wrote checkpoint.

Finished! Selected model with minimal training error rate (BCER) = 3.795

VI. TEST WITH REAL DATA:

1. Create an folder: REAL DATA
2. Prepare some image file: 001.png, 002.jpg...
3. At REAL DATA folder, Example: C:\Users\ASUS\Downloads\REAL_DATA>, type cmd
4.  use command:
 tesseract 001.png 001 -l ranbac
5. You will have 001.txt. Check content in image and txt.

 You can experience my service for free (Chinese, Vietnamese, English) at: https://tiengtrungquoc.net/ocr/
