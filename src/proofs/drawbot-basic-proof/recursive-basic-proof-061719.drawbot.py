
from drawBot import *
import datetime

now = datetime.datetime.now()
W, H = 792, 612


txt = FormattedString()

# # adding some text with some formatting
# txt.append("hello", font="Helvetica", fontSize=100, fill=(1, 0, 0))
# # adding more text
# txt.append("world", font="Times-Italic", fontSize=50, fill=(0, 1, 0))

fontSize = 18
padding = 40

# setting a font
txt.fontSize(fontSize)
# txt += "abcdefghijklmnopqrstuvwxyz\n"

# txt += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"



lower = "\
nnannooaoo nnbnnooboo nncnnoocoo nndnnoodoo nnennooeoo nnfnnoofoo\n\
nngnnoogoo nnhnnoohoo nninnooioo nnjnnoojoo nnknnookoo nnlnnooloo\n\
nnmnnoomoo nnpnnoopoo nnqnnooqoo nnrnnooroo nnsnnoosoo nntnnootoo\n\
nnunnoouoo nnvnnoovoo nnwnnoowoo nnxnnooxoo nnynnooyoo nnznnoozoo\n\
\n"

upper = "\
HHAHHOOAOO HHBHHOOBOO HHCHHOOCOO HHDHHOODOO HHEHHOOEOO HHFHHOOFOO\n\
HHGHHOOGOO HHIHHOOIOO HHJHHOOJOO HHKHHOOKOO HHLHHOOLOO HHMHHOOMOO\n\
HHNHHOONOO HHPHHOOPOO HHQHHOOQOO HHRHHOOROO HHSHHOOSOO HHTHHOOTOO\n\
HHUHHOOUOO HHVHHOOVOO HHWHHOOWOO HHXHHOOXOO HHYHHOOYOO HHZHHOOZOO\n\
\n"

nums = "\
0080088088 0010088188 0020088288 0030088388 0040088488\n\
0050088588 0060088688 0070088788 0090088988\n"


# drawing the formatted string
# txt.font("Recursive Mono Test 061719-Casual C Italic")
# txt.font("Recursive Mono Test 061719")
# txt += lower 
# txt += upper.replace("HHGHHOOGOO ","")
# text(txt, (10, H-fontSize*2))


newPage('LetterLandscape')
txt.font("Recursive Mono Test 061719")
txt += lower 
txt += upper
txt.openTypeFeatures(ss01=True)
txt += lower
txt += nums
text(txt, (padding, H-padding))

font("Recur Mono")
fontSize= 12
text("Recursive Mono Casual Heavy – " + now.strftime("%Y.%m.%d – %H:%M"), padding, padding)



# ========================================

newPage('LetterLandscape')

txt.clear()

txt.font("Recursive Mono Test 061719")
txt += lower 
txt += upper
txt.openTypeFeatures(ss01=True)
txt += lower
txt += nums
text(txt, (padding, H-padding))

font("Recur Mono")
fontSize= 12
text("Recursive Mono Casual Heavy – " + now.strftime("%Y.%m.%d – %H:%M"), padding, padding)


# ========================================
# Save ==================================-

print("saving")
# path = "/Users/stephennixon/type-repos/recursive/src/proofs/drawbot-basic-proof/exports/" + now.strftime("%Y_%m_%d-%H_%M_%S") + ".pdf"
path = "/Users/stephennixon/type-repos/recursive/src/proofs/drawbot-basic-proof/exports/temp.pdf"
saveImage(path) #imageResolution=300
