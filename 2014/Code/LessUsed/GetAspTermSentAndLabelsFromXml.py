import sys,json
from pprint import pprint
from xml.etree import ElementTree
from collections import OrderedDict

def Main ():
    FName = sys.argv[1]
    # FName = '../../Data/Restaurants_Train.xml'

    with open(FName, 'rt') as f:
        tree = ElementTree.parse(f)

    print 'File: {} loaded using python xml parser'.format(FName)

    Sents = OrderedDict()
    for node in tree.iter():
        # print node, node.tag, node.attrib
        if node.tag == 'sentence':
            Id = node.attrib['id']
            Sents[Id] = OrderedDict ()
            Sents[Id]['Sentence'] = ''
            Sents[Id]['TermAndPolarity'] = OrderedDict()
            Sents[Id]['TermAndPolarity']['Term'] = []
            Sents[Id]['TermAndPolarity']['Polarity'] = []
        if 'text' == node.tag:
            Sentence = "".join(node.itertext())
            Sents[Id]['Sentence'] = Sentence
        if 'aspectTerm' == node.tag:
            Sents[Id]['TermAndPolarity']['Term'].append(node.attrib['term'])
            Sents[Id]['TermAndPolarity']['Polarity'].append(node.attrib['polarity'])

    OPFName = FName + '.term-polarity.json'
    with open (OPFName,'w') as FH:
        json.dump(Sents,FH,indent=4)

    print 'All sentences, asp categories and their polarity saved python dict in file ', OPFName


if __name__ == '__main__':
    Main()