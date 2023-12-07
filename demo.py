from winged.HTML.div import Div
from winged.HTML.h import H
from winged.HTML.table import Table
from winged.HTML.string import String

divC = Div(("class", "container"))
# divC.add(H("1").add(String("Hello World")))  # Add header text
h = H("1")
h.add(String("Hello World"))
divC.add(h)

table = Table()
table.add_table_headers(["Name", "Age", "Height", "Location"])  # Define headers
table.add_row()
table.add_in_row(String("John"))
table.add_in_row(String("25"))
table.add_in_row(String("1.80"))
table.add_in_row(String("New York"))
# table.add_row()
# table.add_in_row(String("Maria"))
# table.add_in_row(String("23"))
# table.add_in_row(String("1.50"))
# table.add_in_row(String("New Jersey"))

# table.add_in_row(String("John")).add_in_row(String("25")).add_in_row(String("1.80")).add_in_row(String("New York"))
# table.add_row().add(String("25")).add(String("1.80")).add(String("New York"))
# table.add_in_row("John").add_in_row("25").add_in_row("1.80").add_in_row("New York")
divC.add(table)

print(divC.generate())
