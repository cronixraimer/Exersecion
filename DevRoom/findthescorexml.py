import sys
import xml.etree.ElemenTree as etree

def get_att_number(node):
    count = 0
    count += len(node.attrib)
    for i in node:
        count += get_att_number(i)
    return count

if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElemenTree(etree.formstring(xml))
    root = tree.getroot()
    print(get_att_number(root))
