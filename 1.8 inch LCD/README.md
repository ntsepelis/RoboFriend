# 1.8 inch LCD Module
 
## ΕΙΣΑΓΩΓΗ
Στο παρόν αρχείο περιγράφονται τα βήματα που πρέπει να ακολουθηθούν για να ενεργοποιηθεί η οθόνη αλλά και να χρησιμοποιηθεί.

### ΧΑΡΑΚΤΗΡΙΣΤΙΚΑ
-	Τάση Λειτουργίας: 3.3V/5V (Όταν χρησιμοποιούνται τα 5V, το λογικό "1" είναι τα 5V, ενώ για τάση λειτουργίας 3.3V, το λογικό "1" είναι τα 3.3V)
-	Διεπαφή: SPI
-	Τύπος LCD: TFT
-	Οδηγός: ST7735S
-	Ανάλυση: 128 x 160 (Pixel)
-	Μέγεθος Οθόνης: 35.04mm(Πλάτος) x 28.03mm(Ύψος)
-	Μέγεθος Εικονοστοιχείου: 0.219mm(Πλάτος) * 0.219xx(Ύψος)
-	Διαστάσεις: 56.5mm x 34mm

## ΔΙΕΠΑΦΗ

### RASPBERRY PI :: ΣΥΝΔΕΣΕΙΣ
Συνδέστε την οθόνη με το Raspberry Pi σύμφωνα με τον ακόλουθο πίνακα.\
Περιγράφονται δύο τρόποι σύνδεσης ανάλογα με το αν το πρόγραμμα χρησιμοποιεί τη την απεικόνιση BCM2835 ή την κλασική (Board).

![Πίνακας Συνδέσεων](./LCD1.png) 

> Οι τρόποι απεικόνισης των pin του Raspberry Pi αναθέτουν δε κάθε pin έναν αριθμό ή ένα όνομα.
 
## RASPBERRY PI :: ΛΕΙΤΟΥΡΓΙΑ

### ΕΝΕΡΓΟΠΟΙΗΣΗ SPI INTERFACE

1.	Στη γραμμή ενοτλών πληκτρολογείστε\
**`sudo raspi-config`**
2.	Επιλέξτε διαδοχικά: **Interfacing Options -> SPI -> Yes to enable SPI interface**
3.	Επνακκινήστε το Raspberry Pi

### ΜΕΤΑΦΟΡΤΩΣΗ ΠΑΡΑΔΕΙΓΜΑΤΩΝ
Από τη διεύθυνση 

https://files.waveshare.com/upload/8/8d/LCD_Module_RPI_code.zip

μεταφορτώστε τα παραδείγματα και αποσυμπιέστε τα.

Μέσα στον φάκελο υπάρχουν τα ακόλουθα αρχεία

![Αρχεία Φακέλου](./LCD-Programs.png)

### ΕΛΕΓΧΟΣ ΛΕΙΤΟΥΡΓΙΑΣ 
Για να ελεγχθεί η σωστή εγκατάσταση και λειτουργία της οθόνης θα πρέπει διαδοχικά να εκτελέσετε τα ακόλουθα προγράμματα και να πάρετε ένδειξη σωστής λειτουργίας.
1. `lcdconfig.py`
2. `LCD_1inch8.py`

### ΣΥΝΑΡΤΗΣΕΙΣ ΟΘΟΝΗΣ

#### Προσανατολισμός Οθόνης

Αν θέλετε να αλλάξετε τον προσανατολισμό της οθόνης, χρησιμοποιήστε την εντολή\
**`im_r= image1.rotate(270)`** \
για να στρεφεί η οθόνη κατά 270°.\
Οι δυνατές τιμές είναι: 0°, 90°, 180°, 270°
 
#### Συναρτήσεις Γραφικών (GUI Functions)

Python has an image library PIL official library link, it does not need to write code from the logical layer like C and can directly call to the image library for image processing. The following will take a 1.54-inch LCD as an example, we provide a brief description of the demo. 

•	It needs to use the image library and install the library.
sudo apt-get install python3-pil  
And then import the library
from PIL import Image,ImageDraw,ImageFont.
Among them, Image is the basic library, ImageDraw is the drawing function, and ImageFont is the text function. 

•	Define an image cache to facilitate drawing, writing, and other functions on the picture.
image1 = Image.new("RGB", (disp.width, disp.height), "WHITE")
The first parameter defines the color depth of the image, which is defined as "1" to indicate the bitmap of one-bit depth. The second parameter is a tuple that defines the width and height of the image. The third parameter defines the default color of the buffer, which is defined as "WHITE". 

Create a drawing object based on Image1 on which all drawing operations will be performed on here.
draw = ImageDraw.Draw(image1)

Draw a line.
draw.line([(20, 10),(70, 60)], fill = "RED", width = 1)
The first parameter is a four-element tuple starting at (0, 0) and ending at (127,0). Draw a line. Fill ="0" means the color of the line is white. 

Draw a rectangle.
draw.rectangle([(20,10),(70,60)],fill = "WHITE", outline="BLACK")
Η πρώτη παράμετρος είναι ένα tuple τεσσάρων (4) στοιχείων.
•	(20,10). Οι συντεταγμένες της πάνω αριστερά γωνίας του ορθογωνίου
•	(70,60). Οι συντεταγμένες της κάτω δεξιά γωνίας του του ορθογωνίου
•	Fill =" WHITE". Το εσωτερικό του ορθογωνίου θα είναι λευκό.
•	outline="BLACK". Το χρώμα του περιγράμματος θα είναι μαύρο.

Σχεδιασμός Κύκλου.
Υπάρχουν δύο τρόποι για να σχεδιαστεί ένας κύκλος.

α. Χρησιμοποιώντας τη συνάρτηση draw.arc
draw.arc((150,15,190,55),0, 360, fill =(0,255,0)
Η συνάρτηση σχεδιάζει ένα τόξο που περιέχεται σε ένα τετράγωνο! 
Η πρώτη παράμετρος είναι ένα tuple τεσσάρων (4) στοιχείων.
•	(150,15). Οι συντεταγμένες της πάνω αριστερά γωνίας του περιγεγραμμένου τετραγώνου.
•	(190,55). Οι συντεταγμένες της κάτω δεξιά γωνίας του περιγεγραμμένου τετραγώνου.
•	0. Η γωνία εκκίνησης του τόξου.
•	360. Τελική γωνία του τόξου. Το 360 αντιστοιχεί σε πλήρη κύκλο.
•	fill =(0,255,0). R=0,G=255,B=0. Το εσωτερικό του κύκλου θα έχει χρώμα πράσινο.
Αν το περιγεγραμμένο τετράπλευρο δεν είναι τετράγωνο, τότε η καμπύλη θα είναι έλλειψη.

β. Χρησιμοποιώντας τη συνάρτηση draw.ellipse
draw.ellipse((150,65,190,105), fill = 0)
Η πρώτη παράμετρος είναι ένα tuple τεσσάρων (4) στοιχείων.
•	(150,65). Οι συντεταγμένες της πάνω αριστερά γωνίας του περιγεγραμμένου ορθογωνίου.
•	(190,105). Οι συντεταγμένες της κάτω δεξιά γωνίας του περιγεγραμμένου ορθογωνίου.
•	fill = 0. Το εσωτερικό του κύκλου θα έχει χρώμα μαύρο.
Αν το περιγεγραμμένο τετράπλευρο δεν είναι τετράγωνο, τότε η καμπύλη θα είναι έλλειψη.

Character.
The ImageFont module needs to be imported and instantiated: 
Font1 = ImageFont.truetype("../Font/Font01.ttf",25)
Font2 = ImageFont.truetype("../Font/Font01.ttf",35)
Font3 = ImageFont.truetype("../Font/Font02.ttf",32)
You can use the fonts of Windows or other fonts which is in ttc format..
Note: Each character library contains different characters; If some characters cannot be displayed, it is recommended that you can refer to the encoding set ro used. To draw English characters, you can directly use the fonts; for Chinese characters, you need to add a symbol u: 
draw.text((40, 50), 'WaveShare', fill = (128,255,128),font=Font2)
text= u"微雪电子"
draw.text((74, 150),text, fill = "WHITE",font=Font3)
The first parameter is a tuple of 2 elements, with (40, 50) as the left vertex, the font is Font2, and the fill is the font color. You can directly make fill = "WHITE", because the regular color value is already defined Well, of course, you can also use fill = (128,255,128), the parentheses correspond to the values of the three RGB colors so that you can precisely control the color you want. The second sentence shows Waveshare Electronics, using Font3, the font color is white.

•	read local image
image = Image.open('../pic/LCD_1inch28.jpg')
The parameter is the image path. 

•	Other functions.
For more information, you can refer to http://effbot.org/imagingbook pil 


