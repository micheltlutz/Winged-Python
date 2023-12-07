import unittest
from winged.core.tag import Tag


class TagTest(unittest.TestCase):
    def test_get_tag(self):
        tag = Tag()
        tag._tag = "div"
        self.assertEqual(tag.get_tag(), "div")

    def test_get_attributes(self):
        tag = Tag(("id", "my_div"))
        self.assertEqual(tag.get_attributes().get_string(), 'id="my_div"')

    def test_add_attributes(self):
        tag = Tag()
        tag.add_attributes(("class", "my-class"), ("data-toggle", "modal"))
        self.assertEqual(tag.get_attributes().get_string(), 'class="my-class" data-toggle="modal"')


if __name__ == '__main__':
    unittest.main()
