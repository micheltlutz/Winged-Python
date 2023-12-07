import unittest
from winged.HTML.table import Table
from winged.HTML.string import String


class TestTable(unittest.TestCase):
    def test_table(self):
        # Create a table
        table = Table()

        # Add headers to the table
        table.add_table_headers(["Name", "Age", "Height", "Location"])

        # Add a row to the table
        table.add_row()

        # Add data to the row
        table.add_in_row(String("John"))
        table.add_in_row(String("25"))
        table.add_in_row(String("1.80"))
        table.add_in_row(String("New York"))

        # Get the HTML string for the table
        html = table.get_string()

        correct_html = ("<table><thead><th>Name</th><th>Age</th><th>Height</th><th>Location</th></thead><tbody><tr"
                        "><td>John</td><td>25</td><td>1.80</td><td>New York</td></tr></tbody></table>")

        # Test if the generated HTML is correct
        self.assertEqual(html, correct_html)


if __name__ == "__main__":
    unittest.main()