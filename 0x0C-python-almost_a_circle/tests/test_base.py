import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    """Test cases for the Base class"""

    def test_id_incrementation(self):
        """Test that IDs are incremented properly"""

        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

        b3 = Base()
        self.assertEqual(b3.id, 3)

    def test_id_with_argument(self):
        """Test that ID is set with argument"""

        b = Base(10)
        self.assertEqual(b.id, 10)

    def test_id_without_argument(self):
        """Test that ID is auto-assigned when no argument is provided"""

        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

if __name__ == "__main__":
    unittest.main()

