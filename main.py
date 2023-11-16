from HTML.span import Span
from HTML.string import String
from HTML.p import P
from HTML.div import Div


#mainDiv = Div(("id","mainDiv"))
# mainDiv = Div()
mainDiv = Div(("id","mainDiv"))
paragraph = P(("id","paragraph"))
span_test = Span(("id","teste"))
span_test.addAttributes(("class","teste2"),("style","color:red"))
span_test.addElement(String("Teste"))

paragraph.addElement(span_test)
# print(span_test.getString())

# span_test.generate()

mainDiv.addElement(paragraph)


mainDiv.generate()