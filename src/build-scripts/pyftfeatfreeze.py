
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, print_function, unicode_literals
from builtins import range
from builtins import object

VERSION = "1.23"
"""pyftfeatfreeze.py
Version %(version)s
Copyright (c) 2015 by Adam Twardoch <adam@twardoch.com>
Licensed under the Apache 2 license.
""" % {"version": VERSION}

# 1.23 (2015-09-29 by adam):
#      minor
# 1.22 (2015-08-06 by adam):
#      added -z option to zap TT glyph names
# 1.21 (2015-08-06 by adam):
#      added -i option to control version string update
#      fixed issues with suffix and name replacing
# 1.20 (2015-08-05 by adam):
#      added -r option to report available scripts and features
#      made outpath optional
#      fixed a bug reported by Eric Muller that made the -s and -l options non-functional
# 1.10 (2015-07-18 by adam):
#      first version

import os
import os.path
import argparse
import sys
import tempfile
import fontTools.ttLib

LOGNAME = "featfreeze"


def getTempFilename(suffix=""):
    tmpf = tempfile.NamedTemporaryFile(suffix=suffix)
    tmpfn = tmpf.name
    tmpf.close()
    return tmpfn


def log(message, category="info"):
    sys.stdout.write("[%s][%s] %s\n" % (LOGNAME, category, message))
    sys.stdout.flush()


def warn(message, category="WARN", exit=False):
    sys.stderr.write("[%s][%s] %s\n" % (LOGNAME, category, message))
    sys.stderr.flush()
    if exit:
        sys.exit(2)


def parseOptions():
    USAGE = "%(prog)s [options] inpath [outpath]"
    EXAMPLE = "Example: %(prog)s -f 'c2sc,smcp' -S -U SC OpenSans.ttf OpenSansSC.ttf"
    parser = argparse.ArgumentParser(usage=USAGE, 
                                   epilog=EXAMPLE, add_help=True)
    parser.description = """
    With %(prog)s you can "freeze" some OpenType features into a font. 
    These features are then "on by default", even in apps that don't support OpenType features. 
    This tool actually remaps the "cmap" table of the font by applying the specified GSUB features.
    Only single and alternate substitutions are supported. Homepage: https://github.com/twardoch/fonttools-utils/
    """
    parser.add_argument("inpath", help="input .otf or .ttf font file")
    parser.add_argument("outpath", nargs='?', default=None, help="output .otf or .ttf font file (optional)")
    group1 = parser.add_argument_group("options to control feature freezing")
    group1.add_argument("-f", "--features",
                      action="store", dest="features", type=str, default="",
                      help="comma-separated list of OpenType feature tags, e.g. 'smcp,c2sc,onum'")
    group1.add_argument("-s", "--script",
                      action="store", dest="script", type=str, default="latn",
                      help="OpenType script tag, e.g. 'cyrl' (default: '%(default)s')")
    group1.add_argument("-l", "--lang",
                      action="store", dest="lang", type=str, default=None,
                      help="OpenType language tag, e.g. 'SRB ' (optional)")
    group1.add_argument("-z", "--zapnames",
                      action="store_true", dest="zapnames", default=False,
                      help="zap glyphnames from the font ('post' table version 3, .ttf only)")
    group2 = parser.add_argument_group("options to control font renaming")
    group2.add_argument("-S", "--suffix",
                      action="store_true", dest="rename", default=False,
                      help="add a suffix to the font menu names (by default, the suffix will be constructed from the OpenType feature tags)")
    group2.add_argument("-U", "--usesuffix",
                      action="store", dest="usesuffix", default="",
                      help="use a custom suffix when -S is provided")
    group2.add_argument("-R", "--replacenames", action="store", dest="replacenames", default="", 
                      help="search for strings in the font naming tables and replace them, format is 'search1/replace1,search2/replace2,...'")
    group2.add_argument("-i", "--info",
                      action="store_true", dest="info", default=False,
                      help="update font version string")
    group3 = parser.add_argument_group("reporting options")
    group3.add_argument("-r", "--report",
                      action="store_true", dest="report", default=False,
                      help="report languages, scripts and features in font")
    group3.add_argument("-n", "--names",
                      action="store_true", dest="names", default=False,
                      help="output names of remapped glyphs during processing")
    group3.add_argument("-v", "--verbose",
                      action="store_true", dest="verbose", default=False,
                      help="print additional information during processing")
    group3.add_argument("-V", "--version", action="version", version="%s" % VERSION)

    return parser.parse_args()


class RemapByOTL(object):

    def __init__(self, options):
        self.success = True
        self.inpath = options.inpath
        self.outpath = options.outpath
        if not self.outpath: 
            self.outpath = self.inpath + ".featfreeze.otf"
        self.options = options
        self.names = []
        self.reportLangSys = []
        self.reportFeature = []
        self.ttx = None
        if self.options.verbose:
            log("[RemapByOTL] Running with options: %s" % self.options)

    def openFont(self):
        self.success = True
        self._openFontTTX()
        if (not self.ttx):
            self.success = False
        if self.options.verbose and self.success:
            log("[openFont] Opened font: %s" % self.inpath)

    def _openFontTTX(self):
        self.success = True
        if self.inpath:
            try:
                self.ttx = fontTools.ttLib.TTFont(
                    self.inpath, 0, verbose=False, recalcBBoxes=False)
            except:
                warn("[_openFontTTX] TTX cannot open %s" % self.inpath, "ERRR")
                self.success = False
                self.ttx = None

    def saveFont(self):
        if self.options.report: 
            self._reportFont()
        else: 
            if self.options.zapnames: 
                self.ttx["post"].formatType = 3.0
            self._saveFontTTX()
            if self.options.verbose and self.success:
                log("[saveFont] Saved font: %s" % self.outpath)

    def _reportFont(self): 
        self.success = True
        print("# Scripts and languages:\n%s" % ("\n".join(sorted(list(set(self.reportLangSys))))))
        print("# Features:\n-f %s" % (",".join(sorted(list(set(self.reportFeature))))))

    def _saveFontTTX(self):
        self.success = True
        outpath = self.outpath
        try:
            self.ttx.save(outpath)
        except:
            warn("[_saveFontTTX] TTX cannot save %s" % outpath, "ERRR")
            self.success = False

    def closeFont(self):
        self.success = True
        self._closeFontTTX()

    def _closeFontTTX(self):
        self.success = True
        if self.ttx:
            self.ttx.close()

    def initSubs(self):
        self.success = True
        self.subs0 = list(self.ttx.getGlyphOrder())
        self.subs1 = list(self.ttx.getGlyphOrder())

    def filterFeatureIndex(self):
        self.success = True
        self.filterByScript = self.options.script
        self.filterByLangSys = self.options.lang
        if not "GSUB" in self.ttx:
            warn("No 'GSUB' table found in %s, nothing to do!" % self.inpath, "ERRR")
            self.success = True
            return None
        gsub = self.ttx["GSUB"].table
        self.FeatureIndex = []
        for ScriptRecord in gsub.ScriptList.ScriptRecord:
            if self.options.report: 
                self.reportLangSys.append("-s '%s'" % (ScriptRecord.ScriptTag))
                for LangSysRecord in ScriptRecord.Script.LangSysRecord:
                    self.reportLangSys.append("-s '%s' -l '%s'" % (ScriptRecord.ScriptTag, LangSysRecord.LangSysTag))
            if ScriptRecord.ScriptTag == self.filterByScript:
                if self.filterByLangSys:
                    for LangSysRecord in ScriptRecord.Script.LangSysRecord:
                        if LangSysRecord.LangSysTag == self.filterByLangSys:
                            self.FeatureIndex += LangSysRecord.LangSys.FeatureIndex
                else:
                    self.FeatureIndex += ScriptRecord.Script.DefaultLangSys.FeatureIndex
        self.FeatureIndex = sorted(list(set(self.FeatureIndex)))
        if self.options.verbose:
            log("[filterFeatureIndex] FeatureIndex: %s" % (self.FeatureIndex))

    def filterLookupList(self):
        self.success = True
        self.filterByFeatures = self.options.features.split(",")
        if self.options.verbose:
            log("[filterLookupList] Features to apply: %s" %
                (self.filterByFeatures))
        if not "GSUB" in self.ttx:
            self.success = True
            return None
        gsub = self.ttx["GSUB"].table
        self.LookupList = []
        if self.options.report: 
            for FeatureRecord in gsub.FeatureList.FeatureRecord:
                self.reportFeature.append(FeatureRecord.FeatureTag)
        for fi in self.FeatureIndex:
            if gsub.FeatureList.FeatureRecord[fi].FeatureTag in self.filterByFeatures:
                self.LookupList += gsub.FeatureList.FeatureRecord[fi].Feature.LookupListIndex
        self.LookupList = sorted(list(set(self.LookupList)))
        if self.options.verbose:
            log("[filterLookupList] Lookups: %s" % (self.LookupList))

    def applySubstitutions(self):
        self.success = True
        if not "GSUB" in self.ttx:
            self.success = True
            return None
        gsub = self.ttx["GSUB"].table
        for LookupID in self.LookupList:
            Lookup = gsub.LookupList.Lookup[LookupID]
            for Subtable in Lookup.SubTable:
                mapping = None
                alternates = None
                if Subtable.LookupType == 1:
                    mapping = Subtable.mapping
                elif Subtable.LookupType == 3:
                    alternates = Subtable.alternates
                elif Subtable.LookupType == 7:
                    ExtSubTable = Subtable.ExtSubTable
                    if ExtSubTable.LookupType == 1:
                        mapping = ExtSubTable.mapping
                    elif ExtSubTable.LookupType == 3:
                        alternates = ExtSubTable.alternates
                if mapping:
                    for gn0 in mapping:
                        gn1 = mapping[gn0]
                        for i in range(len(self.subs1)):
                            if self.subs1[i] == gn0:
                                self.subs1[i] = gn1
                if alternates:
                    for gn0 in alternates:
                        if len(alternates[gn0]):
                            gn1 = alternates[gn0][0]
                            for i in range(len(self.subs1)):
                                if self.subs1[i] == gn0:
                                    self.subs1[i] = gn1
        self.subd = {}
        for gi in range(len(self.subs0)):
            self.subd[self.subs0[gi]] = self.subs1[gi]
            if self.options.verbose:
                if self.subs0[gi] != self.subs1[gi]:
                    log("[applySubstitutions] Remap: '%s' -> '%s'	" %
                        (self.subs0[gi], self.subs1[gi]))
            if self.options.names:
                if self.subs0[gi] != self.subs1[gi]:
                    self.names.append(self.subs1[gi])

    def remapCmaps(self):
        self.success = True
        cmap = self.ttx["cmap"]
        for cmaptable in cmap.tables:
            for u in cmaptable.cmap:
                cmaptable.cmap[u] = self.subd[cmaptable.cmap[u]]

    def renameFont(self):
        self.success = True
        if not self.options.rename and not self.options.replacenames:
            return self.success
        suffix = " " + self.options.usesuffix
        if suffix == " ":
            suffix = " ".join(sorted(self.filterByFeatures))
        if suffix == " ": 
            suffix = ""
        pssuffix = suffix.replace(" ", "")
        replacenames = False
        replacetable = [s.split("/") for s in self.options.replacenames.split(",")]
        if len(replacetable[0]) > 1: 
            replacenames = True
        name = self.ttx["name"]
        utf8familyname = None
        utf8fullname = None
        utf8psname = None
        for nr in name.names:
            # Family name
            if nr.nameID in [1, 16, 18, 21]:
                if nr.platformID in [0, 3]:
                    oldname = nr.string.decode("utf_16_be")
                else:
                    oldname = nr.string
                newname = u"%s%s" % (oldname, suffix)
                if replacenames: 
                    for repl in replacetable: 
                        newname = newname.replace(repl[0],repl[1])
                if nr.platformID in [0, 3]:
                    nr.string = newname.encode("utf_16_be")
                    if not utf8familyname:
                        utf8familyname = newname.encode("utf_8")
                else:
                    nr.string = newname.encode("utf_8")
            if self.options.info: 
                # Version string
                if nr.nameID in [5]:
                    if nr.platformID in [0, 3]:
                        oldname = nr.string.decode("utf_16_be")
                    else:
                        oldname = nr.string
                    newname = u"%s; featfreeze: %s" % (oldname, self.options.features)
                    if nr.platformID in [0, 3]:
                        nr.string = newname.encode("utf_16_be")
                    else:
                        nr.string = newname.encode("utf_8")
            # PS name
            newpsname = None
            if nr.nameID in [6]:
                if nr.platformID in [0, 3]:
                    oldname = nr.string.decode("utf_16_be")
                else:
                    oldname = nr.string
                parts = oldname.split("-")
                psfamily = parts[0]
                psstyle = "".join(parts[1:])
                if len(psstyle):
                    psstyle = u"-%s" % (psstyle)
                newpsname = u"%s%s%s" % (psfamily, pssuffix, psstyle)
                if replacenames: 
                    for repl in replacetable: 
                        newpsname = newpsname.replace(repl[0],repl[1])
                if nr.platformID in [0, 3]:
                    nr.string = newpsname.encode("utf_16_be")
                    if not utf8psname:
                        utf8psname = newpsname.encode("utf_8")
                else:
                    nr.string = newpsname.encode("utf_8")
        for nr in name.names:
            # Full name
            if nr.nameID == 4:
                nrfam = name.getName(1, nr.platformID, nr.platEncID, nr.langID)
                nrsty = name.getName(2, nr.platformID, nr.platEncID, nr.langID)
                if nr.platformID in [0, 3]:
                    nfam = nrfam.string.decode("utf_16_be")
                    nsty = nrsty.string.decode("utf_16_be")
                else:
                    nfam = nrfam.string
                    nsty = nrsty.string
                newname = u"%s %s" % (nfam, nsty)
                if nr.platformID in [0, 3]:
                    nr.string = newname.encode("utf_16_be")
                    utf8fullname = newname.encode("utf_8")
                else:
                    nr.string = newname.encode("utf_8")
                if "CFF " in self.ttx:
                    if nr.platformID == 3 and nr.platEncID == 1:
                        nrpsn = name.getName(6, 3, 1, nr.langID)
                        if nrpsn:
                            nr.string = nrpsn.string
        if "CFF " in self.ttx:
            cff = self.ttx["CFF "]
            rawDict = cff.cff[list(cff.cff.keys())[0]].rawDict
            if utf8familyname:
                rawDict["FamilyName"] = utf8familyname
            else:
                warn("Cannot change CFF FamilyName", exit=True)
            if utf8fullname:
                rawDict["FullName"] = utf8fullname
            else:
                warn("Cannot change CFF FullName", exit=True)
            if len(cff.cff.fontNames) == 1:
                if utf8psname:
                    cff.cff.fontNames[0] = utf8psname
                else:
                    warn("Cannot change CFF FontName", exit=True)
            else:
                warn(
                    "Cannot properly rename font with multiple CFF font entries", exit=True)
                self.success = False
        if self.options.verbose:
            log("[renameFont] New family name: '%s'" % (utf8familyname))
            log("[renameFont] New full name: '%s'" % (utf8fullname))
            log("[renameFont] New PostScript name: '%s'" % (utf8psname))

    def remapByOTL(self):
        self.success = True
        self.initSubs()
        if self.success:
            self.filterFeatureIndex()
        if self.success:
            self.filterLookupList()
        if self.success:
            self.applySubstitutions()
        if self.success:
            self.remapCmaps()
        if self.success:
            if self.options.names:
                print(" ".join(self.names))

    def run(self):
        self.openFont()
        if self.success:
            self.remapByOTL()
        if self.success:
            self.renameFont()
        if self.success:
            self.saveFont()
        self.closeFont()


def main():
    args = parseOptions()
    if args:
        if not os.path.exists(args.inpath):
            warn("Input file does not exist.", "ERRR", exit=True)
        p = RemapByOTL(args)
        p.run()
        if p.success:
            if p.options.verbose:
                log("Finished processing.", "good")
            return 0
        else:
            warn("Errors during processing.", "FAIL", exit=True)
    else:
        print("Add -h for help")

if __name__ == "__main__":
    finish = main()
    sys.exit(finish)