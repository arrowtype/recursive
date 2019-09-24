from drawBot import * # requires drawbot to be installed as module
import datetime
from fontTools.misc.bezierTools import splitCubicAtT
newDrawing() # for drawbot module


export = True
autoOpen = True
exportFormat = "pdf" # pdf, gif, mp4, or bmp
W,H = 11, 8.5 # inches
DPI = 300

pageW, pageH = W * DPI, H * DPI

now = datetime.datetime.now().strftime("%Y_%m_%d-%H_%M")
parentDir = "/Users/stephennixon/type-repos/recursive/src/proofs/vietnamese-diacritics"
docTitle="recursive-vietnamese-diacritics"

fontFam = "/Users/stephennixon/type-repos/recursive/src/proofs/vietnamese-diacritics/recursive-mono--xprn_wght_slnt_ital--2019_09_23.ttf"

variations = [
    {"wght": 300.01, "XPRN":0.01},
    {"wght": 400.01, "XPRN":0.01},
    {"wght": 800.01, "XPRN":0.01},
    {"wght": 899.99, "XPRN":0.01},
    {"wght": 300.01, "XPRN":0.999},
    {"wght": 400.01, "XPRN":0.999},
    {"wght": 800.01, "XPRN":0.999},
    {"wght": 899.99, "XPRN":0.999}
    ]

# top, right, bottom, left
padding = [0.5, 0.5, 0.5, 0.5] # in inches

pad = [i * DPI for i in padding]

def newPagePlz(w,h):
    newPage(w,h)
    font(fontFam)
    fontSize(10 * DPI/72)
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d, %H:%M")
    text(f"Recursive Mono – Vietnamese Diacritics; {timestamp}", (pad[3], pad[2]*0.75))


def printVariations(string, size, variations):
    for i,var in enumerate(variations):

        text = FormattedString()
        text.font(fontFam)
        text.fontSize(12 * DPI/72)
        text.fontVariations(**var)
        text.append(string)

        textPath = BezierPath()

        textPath.textBox(text, (pad[3],-pad[1]-64*DPI/72*i, pageW-pad[1]*2, pageH))
        drawPath(textPath)

def serialPrint(string, size, variations):
    testText = FormattedString()
    testText.font(fontFam)
    for glyph in string:
        for var in variations:
            fSize = size * DPI/72
            testText.fontSize(fSize)
            testText.lineHeight(fSize * 1.625)
            testText.fontVariations(**var)
            testText.append(glyph)

    textPath = BezierPath()
    textPath.textBox(testText, (pad[3],0-pad[0],pageW-pad[1]*2, pageH))
    drawPath(textPath)

# ---------------------------------------------------------------
# PAGE 1 --------------------------------------------------------
newPagePlz(pageW, pageH)

testString="Trương, trường, thương, tương, trước, sương, chương, phương hướng, xương sường, tưởng tượng"

printVariations(testString, size, variations)

# ---------------------------------------------------------------
# PAGE 2 --------------------------------------------------------



newPagePlz(pageW, pageH)

diacriticsUpper="ẢẤẦẨẪẬẮẰẲẴẶẺẾỀỂỄỆỈƠỎỐỒỔỖỘỚỜỞỠỢƯỦỨỪỬỮỰ"
# diacritics="ẢẤẦẨẪẬẮẰẲẴẶẺẾỀỂỄỆ"


serialPrint(diacriticsUpper, 36, variations)

# ---------------------------------------------------------------
# PAGE 3 --------------------------------------------------------

newPagePlz(pageW, pageH)
diacriticsLower = "ảấầẩẫậắằẳẵặẻếềểễệỉơỏốồổỗộớờởỡợưủứừửữự"
serialPrint(diacriticsLower, 36, variations)

# ---------------------------------------------------------------
# PAGE 4 --------------------------------------------------------

newPagePlz(pageW, pageH)
mainDiacritics = "ƠỎƯỦơỏưủ"
serialPrint(mainDiacritics,72, variations)

# ---------------------------------------------------------------
# PAGE 5 --------------------------------------------------------

newPagePlz(pageW, pageH)
randomText = "Giải đua xe mô-tô quốc tế  (trước kia còn được gọi là MotoGP) là giải thể thao tốc độ số một thế giới về mảng đua môtô được tổ chức ở các trường đua đường nhựa. Các cuộc đua xe moto riêng lẻ đã được tổ chức từ đầu thế kỷ 20 và những cuộc đua lớn nhất trong số đó được gọi là các  Grand Prix, Tổ chức được thành lập để điều hành các giải đua xe moto quốc tế là Liên đoàn đua xe moto quốc tế, viết tắt là FIM trong năm 1949 đã thống nhất các quy định và tổ chức giải đua MotoGP vòng quanh thế giới đầu tiên, tên chính thức tiếng Anh là FIM Road Racing World Championship Grand Prix. Nó chính là giải đua xe vô địch thế giới.lâu đời nhất thế giới"

printVariations(randomText, 12, variations)


# ------------------------------------------------
# save result ------------------------------------

endDrawing()

if export and exportFormat is not "bmp":

    path = f"{parentDir}/exports/{docTitle}-{now}.{exportFormat}"

    print("saved to ", path)

    saveImage(path)

    if autoOpen:
        import os
        # os.system(f"open --background -a Preview {path}")
        os.system(f"open -a Preview {path}")