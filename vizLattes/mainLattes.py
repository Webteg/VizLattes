import xml.dom.minidom

x = xml.dom.minidom.parse('input/curriculo.xml')
nos = x.documentElement
print("%s" % nos.nodeName)
filhos1 = [no for no in nos.childNodes if no.nodeType == x.ELEMENT_NODE]
for pai in filhos1:
    puta =
       print ("|--> %s" % pai.nodeName)

       filhos2 = [no for no in pai.childNodes if no.nodeType == x.ELEMENT_NODE]
       for filho in filhos2:
           if filho.nodeName == 'PREMIOS-TITULOS':
               print('teste')
               elida = filho.getElementsByTagName('PREMIO-TITULO')
               for item in elida:
                   print(item.getAttribute('NOME-DO-PREMIO-OU-TITULO'))
           print ("|---> %s" % filho.nodeName)
           print ("|-----> %s" % filho.getAttribute('atributo1'))
           print ("|-----> %s" % filho.getAttribute('atributo2'))


           for node in nos.getElementsByTagName('PREMIOS-TITULOS'):  # visit every node <bar />
               #print (node.toxml())
               print (node.getAttribute('NOME-DO-PREMIO-OU-TITULO'))