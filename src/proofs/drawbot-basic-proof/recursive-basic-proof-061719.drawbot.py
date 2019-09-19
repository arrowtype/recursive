
from drawBot import *
from datetime import datetime
import subprocess

timestamp = datetime.now().strftime("%Y-%m-%d")

print(timestamp)
W, H = 792, 612




mainFontSize = 16
padding = 40

# setting a font



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

kernKing = """\
lynx tuft frogs, dolphins abduct by proxy the ever awkward klutz, dud, dummkopf, jinx snubnose filmgoer, orphan sgt. renfruw grudgek reyfus, md. sikh psych if halt tympany jewelry sri heh! twyer vs jojo pneu fylfot alcaaba son of nonplussed halfbreed bubbly playboy guggenheim daddy coccyx sgraffito effect, vacuum dirndle impossible attempt to disvalue, muzzle the afghan czech czar and exninja, bob bixby dvorak wood dhurrie savvy, dizzy eye aeon circumcision uvula scrungy picnic luxurious special type carbohydrate ovoid adzuki kumquat bomb? afterglows gold girl pygmy gnome lb. ankhs acme aggroupment akmed brouhha tv wt. ujjain ms. oz abacus mnemonics bhikku khaki bwana aorta embolism vivid owls often kvetch otherwise, wysiwyg densfort wright you’ve absorbed rhythm, put obstacle kyaks krieg kern wurst subject enmity equity coquet quorum pique tzetse hepzibah sulfhydryl briefcase ajax ehler kafka fjord elfship halfdressed jugful eggcup hummingbirds swingdevil bagpipe legwork reproachful hunchback archknave baghdad wejh rijswijk rajbansi rajput ajdir okay weekday obfuscate subpoena liebknecht marcgravia ecbolic arcticward dickcissel pincpinc boldface maidkin adjective adcraft adman dwarfness applejack darkbrown kiln palzy always farmland flimflam unbossy nonlineal stepbrother lapdog stopgap sx countdown basketball beaujolais vb. flowchart aztec lazy bozo syrup tarzan annoying dyke yucky hawg gagzhukz cuzco squire when hiho mayhem nietzsche szasz gumdrop milk emplotment ambidextrously lacquer byway ecclesiastes stubchen hobgoblins crabmill aqua hawaii blvd. subquality byzantine empire debt obvious cervantes jekabzeel anecdote flicflac mechanicville bedbug couldn’t i’ve it’s they’ll they’d dpt. headquarter burkhardt xerxes atkins govt. ebenezer lg. lhama amtrak amway fixity axmen quumbabda upjohn hrumpf

LYNX TUFT FROGS, DOLPHINS ABDUCT BY PROXY THE EVER AWKWARD KLUTZ, DUD, DUMMKOPF, JINX SNUBNOSE FILMGOER, ORPHAN SGT. RENFRUW GRUDGEK REYFUS, MD. SIKH PSYCH IF HALT TYMPANY JEWELRY SRI HEH! TWYER VS JOJO PNEU FYLFOT ALCAABA SON OF NONPLUSSED HALFBREED BUBBLY PLAYBOY GUGGENHEIM DADDY COCCYX SGRAFFITO EFFECT, VACUUM DIRNDLE IMPOSSIBLE ATTEMPT TO DISVALUE, MUZZLE THE AFGHAN CZECH CZAR AND EXNINJA, BOB BIXBY DVORAK WOOD DHURRIE SAVVY, DIZZY EYE AEON CIRCUMCISION UVULA SCRUNGY PICNIC LUXURIOUS SPECIAL TYPE CARBOHYDRATE OVOID ADZUKI KUMQUAT BOMB? AFTERGLOWS GOLD GIRL PYGMY GNOME LB. ANKHS ACME AGGROUPMENT AKMED BROUHHA TV WT. UJJAIN MS. OZ ABACUS MNEMONICS BHIKKU KHAKI BWANA AORTA EMBOLISM VIVID OWLS OFTEN KVETCH OTHERWISE, WYSIWYG DENSFORT WRIGHT YOU’VE ABSORBED RHYTHM, PUT OBSTACLE KYAKS KRIEG KERN WURST SUBJECT ENMITY EQUITY COQUET QUORUM PIQUE TZETSE HEPZIBAH SULFHYDRYL BRIEFCASE AJAX EHLER KAFKA FJORD ELFSHIP HALFDRESSED JUGFUL EGGCUP HUMMINGBIRDS SWINGDEVIL BAGPIPE LEGWORK REPROACHFUL HUNCHBACK ARCHKNAVE BAGHDAD WEJH RIJSWIJK RAJBANSI RAJPUT AJDIR OKAY WEEKDAY OBFUSCATE SUBPOENA LIEBKNECHT MARCGRAVIA ECBOLIC ARCTICWARD DICKCISSEL PINCPINC BOLDFACE MAIDKIN ADJECTIVE ADCRAFT ADMAN DWARFNESS APPLEJACK DARKBROWN KILN PALZY ALWAYS FARMLAND FLIMFLAM UNBOSSY NONLINEAL STEPBROTHER LAPDOG STOPGAP SX COUNTDOWN BASKETBALL BEAUJOLAIS VB. FLOWCHART AZTEC LAZY BOZO SYRUP TARZAN ANNOYING DYKE YUCKY HAWG GAGZHUKZ CUZCO SQUIRE WHEN HIHO MAYHEM NIETZSCHE SZASZ GUMDROP MILK EMPLOTMENT AMBIDEXTROUSLY LACQUER BYWAY ECCLESIASTES STUBCHEN HOBGOBLINS CRABMILL AQUA HAWAII BLVD. SUBQUALITY BYZANTINE EMPIRE DEBT OBVIOUS CERVANTES JEKABZEEL ANECDOTE FLICFLAC MECHANICVILLE BEDBUG COULDN’T I’VE IT’S THEY’LL THEY’D DPT. HEADQUARTER BURKHARDT XERXES ATKINS GOVT. EBENEZER LG. LHAMA AMTRAK AMWAY FIXITY AXMEN QUUMBABDA UPJOHN HRUMPF

Aaron Abraham Adam Aeneas Agfa Ahoy Aileen Akbar Alanon Americanism Anglican Aorta April Fool’s Day Aqua Lung (Tm.) Arabic Ash Wednesday Authorized Version Ave Maria Away Axel Ay Aztec Bhutan Bill Bjorn Bk Btu. Bvart Bzonga California Cb Cd Cervantes Chicago Clute City, Tx. Cmdr. Cnossus Coco Cracker State, Georgia Cs Ct. Cwacker Cyrano David Debra Dharma Diane Djakarta Dm Dnepr Doris Dudley Dwayne Dylan Dzerzhinsk Eames Ectomorph Eden Eerie Effingham, Il. Egypt Eiffel Tower Eject Ekland Elmore Entreaty Eolian Epstein Equine Erasmus Eskimo Ethiopia Europe Eva Ewan Exodus Jan van Eyck Ezra Fabian February Fhara Fifi Fjord Florida Fm France Fs Ft. Fury Fyn Gabriel Gc Gdynia Gehrig Ghana Gilligan Karl Gjellerup Gk. Glen Gm Gnosis Gp.E. Gregory Gs Gt. Br. Guinevere Gwathmey Gypsy Gzags Hebrew Hf Hg Hileah Horace Hrdlicka Hsia Hts. Hubert Hwang Hai Hyacinth Hz. Iaccoca Ibsen Iceland Idaho If Iggy Ihre Ijit Ike Iliad Immediate Innocent Ione Ipswitch Iquarus Ireland Island It Iud Ivert Iwerks Ixnay Iy Jasper Jenks Jherry Jill Jm Jn Jorge Jr. Julie Kerry Kharma Kiki Klear Koko Kruse Kusack Kylie Laboe Lb. Leslie Lhihane Llama Lorrie Lt. Lucy Lyle Madeira Mechanic Mg. Minnie Morrie Mr. Ms. Mt. Music My Nanny Nellie Nillie Novocane Null Nyack Oak Oblique Occarina Odd Oedipus Off Ogmane Ohio Oil Oj Oklahoma Olio Omni Only Oops Opera Oqu Order Ostra Ottmar Out Ovum Ow Ox Oyster Oz Parade Pd. Pepe Pfister Pg. Phil Pippi Pj Please Pneumonia Porridge Price Psalm Pt. Purple Pv Pw Pyre Qt. Quincy Radio Rd. Red Rhea Right Rj Roche Rr Rs Rt. Rural Rwanda Ryder Sacrifice Series Sgraffito Shirt Sister Skeet Slow Smore Snoop Soon Special Squire Sr St. Suzy Svelte Swiss Sy Szach Td Teach There Title Total Trust Tsena Tulip Twice Tyler Tzean Ua Udder Ue Uf Ugh Uh Ui Uk Ul Um Unkempt Uo Up Uq Ursula Use Utmost Uvula Uw Uxurious Uzßai Valerie Velour Vh Vicky Volvo Vs Water Were Where With World Wt. Wulk Wyler Xavier Xerox Xi Xylophone Yaboe Year Yipes Yo Ypsilant Ys Yu Zabar’s Zero Zhane Zizi Zorro Zu Zy Don’t I’ll I’m I’se
"""

fontStyle = "Recursive Beta 1.016 – PROP=1, XPRN=1, wght=400, slnt=0, ital=0.5"

newPage('LetterLandscape')

txt = FormattedString()

txt.fontSize(mainFontSize)

txt.font("Recursive Beta 1.016")
txt.fontVariations(PROP=1, XPRN=1, wght=400, slnt=0, ital=0.5)
txt += lower
txt += upper
# txt.openTypeFeatures(ss01=True)
txt += lower
txt += nums
text(txt, (padding, H-padding))

font("Recursive Beta 1.016")
fontSize(8)
text(fontStyle + " // " + timestamp, (padding, padding))


# ----------------------------------------
# Next Page ------------------------------

# TODO: figure out how to call a fresh instance of txt, but keep the formatting

newPage('LetterLandscape')

txtB = FormattedString()


# txt.font("Recursive Mono Test 061719 Casual C Italic")
# txt.font("Times New Roman")
txtB.font("Recursive Beta 1.016")
txtB.fontVariations(PROP=1, XPRN=1, wght=400, slnt=0, ital=0.5)

txtB += kernKing
textBox(txtB, (padding, H-H+padding*2, W-padding*2, H-padding*3))

font("Recursive Beta 1.016")
fontSize(8)
text(fontStyle + " // " + timestamp, (padding, padding))



# -----------------
# temp ------------

newPage('LetterLandscape')

font("Recursive Beta 1.016")
fontSize(32)
text("more pages to come", (padding, padding))

# ----------------------------------------
# Save -----------------------------------

print("saving")
# path = "/Users/stephennixon/type-repos/recursive/src/proofs/drawbot-basic-proof/exports/" + now.strftime("%Y_%m_%d-%H_%M_%S") + ".pdf"
path = f"/Users/stephennixon/type-repos/recursive/src/proofs/drawbot-basic-proof/exports/temp-{timestamp}.pdf"
saveImage(path)  # imageResolution=300

# open(path)
# subprocess.call(['open', path])
