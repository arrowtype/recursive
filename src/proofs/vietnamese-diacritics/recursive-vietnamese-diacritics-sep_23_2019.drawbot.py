from drawBot import * # requires drawbot to be installed as module
import datetime
from fontTools.misc.bezierTools import splitCubicAtT
from fontTools.ttLib import TTFont
import os
import shutil

newDrawing() # for drawbot module

export = True
autoOpen = True
exportFormat = "pdf" # pdf, gif, mp4, or bmp
W,H = 11, 8.5 # inches
DPI = 300

pageW, pageH = W * DPI, H * DPI

now = datetime.datetime.now().strftime("%Y_%m_%d-%H_%M")
timestamp = datetime.datetime.now().strftime("%Y-%m-%d, %H:%M")
parentDir = "/Users/stephennixon/type-repos/recursive/src/proofs/vietnamese-diacritics"
docTitle="recursive-vietnamese-diacritics"

fontFam = "/Users/stephennixon/type-repos/recursive/src/proofs/vietnamese-diacritics/recursive-mono--xprn_wght_slnt_ital--2019_09_26.ttf"

# hack to avoid font cache: update nameID 6 (https://github.com/typemytype/drawbot/issues/112)
ttfont = TTFont(fontFam)
oldName6 = ttfont['name'].getName(6, 3, 1)
tempName6 = f"tempFont-{now}"
print(f"{oldName6} updated to {tempName6} to avoid cache")
ttfont['name'].setName(tempName6, 6, 3, 1, 0x409)

oldName3 = ttfont['name'].getName(3, 3, 1)
tempName3 = str(oldName3).replace(str(oldName3).split(';')[-1],tempName6)
print(f"{oldName3} updated to {tempName3} to avoid cache")
ttfont['name'].setName(tempName3, 3, 3, 1, 0x409)

tempFolder = os.path.split(fontFam)[0] + "/temp"

if not os.path.exists(tempFolder):
    os.makedirs(tempFolder)

tempFile = tempFolder + "/" + os.path.split(fontFam)[1].replace(".ttf",f".temp.ttf")
ttfont.save(tempFile)

fontFam = tempFile

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

def newPagePlz(w,h, footer=True):
    newPage(w,h)
    if footer:
        font(fontFam)
        fontSize(10 * DPI/72)
        text(f"Recursive Mono – Vietnamese Diacritics; {timestamp}", (pad[3], pad[2]*0.75))


def printVariations(string, size, variations):
    text = FormattedString()
    text.font(fontFam)
    fSize = size * DPI/72
    text.fontSize(fSize)
    text.lineHeight(fSize * 1.625)

    for var in variations:

        text.fontVariations(**var)
        text.append(string)

    textPath = BezierPath()

    textPath.textBox(text, (pad[3],-pad[1], pageW-pad[1]*2, pageH))
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
# COVER PAGE ----------------------------------------------------
newPagePlz(pageW, pageH, footer=False)

coverText = FormattedString()
coverText.font(fontFam)
fSize = 16 * DPI/72
coverText.fontSize(fSize)
coverText.lineHeight(fSize * 1.625)

coverText.fontVariations(wght=899.99, XPRN=0.001)
coverText.append(f"Recursive Mono\n")
coverText.fontVariations(wght=399.99, XPRN=0.999)
coverText.append(f"Vietnamese Diacritics\n")
coverText.append(f"{timestamp} \n\n")
coverText.append(f"Instances in proof: \n")

varStrings = [
    "Expression: 0, Weight: 300 // Linear Light      (master)",
    "Expression: 0, Weight: 400 // Linear Regular    (interpolated)",
    "Expression: 0, Weight: 800 // Linear ExtraBold  (master)",
    "Expression: 0, Weight: 900 // Linear Black      (master)",
    "Expression: 1, Weight: 300 // Casual Light      (master) ",
    "Expression: 1, Weight: 400 // Casual Regular    (interpolated) ",
    "Expression: 1, Weight: 800 // Casual ExtraBold  (master) ",
    "Expression: 1, Weight: 900 // Casual Black      (master) "
]

for i, var in enumerate(variations):
    coverText.fontVariations(**var)
    coverText.append(f"  → {varStrings[i]} \n")

textPath = BezierPath()
textPath.textBox(coverText, (pad[3],-pad[1], pageW-pad[1]*2, pageH))
drawPath(textPath)

# ---------------------------------------------------------------
# PAGE 1 --------------------------------------------------------
newPagePlz(pageW, pageH)

testString="Trương, trường, thương, tương, trước, sương, chương, phương hướng, xương sường, tưởng tượng\n"

printVariations(testString, 20, variations)

# ---------------------------------------------------------------
# PAGE 2 --------------------------------------------------------

newPagePlz(pageW, pageH)
diacriticsUpper="ẢẤẦẨẪẬẮẰẲẴẶẺẾỀỂỄỆỈƠỎỐỒỔỖỘỚỜỞỠỢƯỦỨỪỬỮỰ"
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

newPagePlz(pageW, pageH)
# mainDiacritics = "ẢẤẦẨẪẮẰẲẴ ấầẩẫẩẫắằẳẵ"
mainDiacritics = "ỐỒỔỖỘỚỜỞỠ ốồổỗộớờởỡợ"
serialPrint(mainDiacritics,44, variations)

newPagePlz(pageW, pageH)
# mainDiacritics = "ẢẤẦẨẪẮẰẲẴ ấầẩẫẩẫắằẳẵ"
mainDiacritics = "ƯỦỨỪỬỮỰ ưủứừửữự"
serialPrint(mainDiacritics,44, variations)

# ---------------------------------------------------------------
# PAGE 5 --------------------------------------------------------

newPagePlz(pageW, pageH)

variations = [
    {"wght": 300.01, "XPRN":0.01},
    {"wght": 400.01, "XPRN":0.01},
    {"wght": 800.01, "XPRN":0.01},
    {"wght": 899.99, "XPRN":0.01},
    ]

# wikiText = "Giải đua xe mô-tô quốc tế  (trước kia còn được gọi là MotoGP) là giải thể thao tốc độ số một thế giới về mảng đua môtô được tổ chức ở các trường đua đường nhựa. Các cuộc đua xe moto riêng lẻ đã được tổ chức từ đầu thế kỷ 20 và những cuộc đua lớn nhất trong số đó được gọi là các  Grand Prix, Tổ chức được thành lập để điều hành các giải đua xe moto quốc tế là Liên đoàn đua xe moto quốc tế, viết tắt là FIM trong năm 1949 đã thống nhất các quy định và tổ chức giải đua MotoGP vòng quanh thế giới đầu tiên, tên chính thức tiếng Anh là FIM Road Racing World Championship Grand Prix. Nó chính là giải đua xe vô địch thế giới.lâu đời nhất thế giới"


wikiText = 'Đồng (VND) là đơn vị tiền tệ chính thức của nước Cộng hòa Xã hội Chủ nghĩa Việt Nam, do Ngân hàng Nhà nước Việt Nam phát hành. Đồng có ký hiệu là ₫, mã quốc tế theo ISO 4217 là "VND". Một đồng có giá trị bằng 100 xu hay 10 hào. Hai đơn vị xu và hào vì quá nhỏ nên không còn được phát hành nữa. Tiền giấy được phát hành hiện nay có giá trị 100₫, 200₫ … Đồng thời cũng có tiền kim loại trị giá 200₫, 500₫, … Loại tiền này lúc trước còn được gọi một cách dân dã là Tiền cụ Hồ [cần dẫn nguồn] vì hầu hết mặt trước tiền giấy đều in hình của chủ tịch Hồ Chí Minh và đặc biệt khi dùng để phân biệt với các loại tiền khác đã từng lưu hành tại Việt Nam có cùng tên gọi là "đồng". Theo luật pháp hiện hành của Việt Nam, tiền giấy và tiền kim loại là phương tiện thanh toán pháp quy không giới hạn nghĩa là người ta bắt buộc phải chấp nhận khi nó được dùng để thanh toán cho một khoản nợ xác lập bằng đồng Việt Nam với mọi số lượng, mệnh giá kỷ.\n'

printVariations(wikiText, 10, variations)

# ---------------------------------------------------------------
# PAGE 5 --------------------------------------------------------

newPagePlz(pageW, pageH)

variations = [
    {"wght": 300.01, "XPRN":0.999},
    {"wght": 400.01, "XPRN":0.999},
    {"wght": 800.01, "XPRN":0.999},
    {"wght": 899.99, "XPRN":0.999}
    ]

printVariations(wikiText, 10, variations)

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

# remove earlier font hack
shutil.rmtree(tempFolder)
