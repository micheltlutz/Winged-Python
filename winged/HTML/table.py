from winged.HTML.string import String
from winged.core.generic_element import GenericElement
from winged.core.tag import Tag
from winged.HTML.thead import THead
from winged.HTML.tbody import TBody
from winged.HTML.tr import Tr
from winged.HTML.th import Th
from winged.HTML.td import Td


class Table(Tag):
    """
    The Table class is a specific implementation of the HTML 'table' tag in the Winged-Python library.
    It provides helper methods to generate table structures.

    Table creation involves creating headers (th), rows (tr), and data cells (td).

    Example Usage:
        ```
        table = Table()
        table.add_table_headers(["Name", "Age", "Height", "Location"])  # Define headers
        table.add_row()
        table.add_in_row(String("John"))
        table.add_in_row(String("25"))
        table.add_in_row(String("1.80"))
        table.add_in_row(String("New York"))
        ```

    This would generate a table with mentioned headers and one row of data.
    """

    _tag = "table"
    _container = True
    _form_element = False

    def __init__(self):
        super().__init__()
        self.tbody = TBody()
        self.thead = None
        self.rows = []

    def add_table_headers(self, titles, aligns=None, classes=None):
        self.thead = THead()
        for index, title in enumerate(titles):
            th = Th()
            th.add(String(title))
            if aligns:
                th.add_attributes(('align', aligns[index]))
            if classes:
                th.add_attributes(('class', classes[index]))
            self.thead.add(th)
        self.add(self.thead)

    def add_row(self):
        tr = Tr()
        self.rows.append(tr)
        return tr

    def add_in_row(self, data: GenericElement, *args):
        td = Td(*args)
        td.add(data)
        try:
            self.rows[-1].add(td)
        except IndexError:
            raise Exception("[Wrong usage for add_in_row] Use add_row first to create a new row")

        return self.rows[-1]

    def get_string(self):
        for row in self.rows:
            self.tbody.add(row)
        self.add(self.tbody)

        return super().get_string()
