import json
import xml.etree.ElementTree as ET

tree = ET.parse('src/masters/recursive-prop_xprn_weight_slnt_ital.designspace')
root = tree.getroot()


# xml.etree.ElementTree.Element(tag,


print(root.findall('instances'))

for child in root.findall('instances/instance'):
    print(child.tag)
    print(child.attrib)
    print(child.text)
    print(type(json.loads(child.text)))
    print('------------------')
    print(child.text.get('familyname'), child.text.get('stylename'))

    # for thing in child.findall('location/dimension'):
    #     print(thing.tag)
    #     print(thing.attrib)
    #     print(thing.text)
    #     print('------------------')