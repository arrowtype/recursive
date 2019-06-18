
from drawBot import *
import datetime
import subprocess

timestamp = datetime.datetime.now().strftime("%Y.%m.%d – %H:%M")
W, H = 792, 612


txt = FormattedString()

fontSize = 18
padding = 40

# setting a font
txt.fontSize(fontSize)


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


newPage('LetterLandscape')
# txt.font("Recursive Mono Test 061719")
txt.font("Helvetica")
txt += lower
txt += upper
txt.openTypeFeatures(ss01=True)
txt += lower
txt += nums
text(txt, (padding, H-padding))

font("Courier")
fontSize = 12
text("Helvetica – " +
     timestamp, padding, padding)


# ----------------------------------------
# Next Page ------------------------------

# TODO: figure out how to call a fresh instance of txt, but keep the formatting

newPage('LetterLandscape')


# txt.font("Recursive Mono Test 061719 Casual C Italic")
txt.font("Times New Roman")
text(txt, (padding, H-padding))

text("Times New Roman – " +
     timestamp, padding, padding)


# ----------------------------------------
# Save -----------------------------------

print("saving")
# path = "/Users/stephennixon/type-repos/recursive/src/proofs/drawbot-basic-proof/exports/" + now.strftime("%Y_%m_%d-%H_%M_%S") + ".pdf"
path = "/Users/stephennixon/type-repos/recursive/src/proofs/drawbot-basic-proof/exports/temp.pdf"
saveImage(path)  # imageResolution=300

# open(path)
# subprocess.call(['open', path])
