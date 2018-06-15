import os
import fontmake
from fontmake.font_project import FontProject

DS_PATH = 'Recursive-sans-core.designspace'

def getRunArguments():
    u"""Arguments to be passed to a fontmake project run. The values below
    make Decovar build without errors. See also fontmake.__main__.py."""

    args = {
        'subset': None,
        'use_production_names': False,
        #'mark_writer_class': None,
        'reverse_direction': False,
        #'kern_writer_class': None,
        'interpolate_binary_layout': False,
        'remove_overlaps': True,
        'autohint': None,
        'conversion_error': None,
        #'no_round': False,
        'masters_as_instances': False,
        'interpolate': True,
        'use_afdko': False,
        'subroutinize': True,
        'output':['ttf'],
    }
    return args

project = FontProject()

args = getRunArguments()

print(project.run_from_designspace(designspace_path=DS_PATH, **args))

# fontPath = 'otf/' + DS_PATH.replace('.designspace', '.otf')
# os.system('open %s' % fontPath)