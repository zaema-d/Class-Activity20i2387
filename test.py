import unittest
from main import StudentsInMLOps

class TestStudentsInMLOps(unittest.TestCase):
    def setUp(self):
        """Create a StudentsInMLOps object before each test."""
        self.class_obj = StudentsInMLOps()

    def test_enrollStudents(self):
        """Test enrolling students."""
        self.class_obj.enrollStudents(5)
        self.assertEqual(self.class_obj.getTotalStrength(), 5)

    def test_dropStudents(self):
        """Test dropping students."""
        self.class_obj.enrollStudents(5)
        self.class_obj.dropStudents(2)
        self.assertEqual(self.class_obj.getTotalStrength(), 3)

    def test_getTotalStrength(self):
        """Test getting total strength."""
        self.class_obj.enrollStudents(3)
        self.assertEqual(self.class_obj.getTotalStrength(), 3)

    def test_getClassName(self):
        """Test getting class name."""
        self.assertEqual(self.class_obj.getClassName(), "StudentsInMLOps")

if __name__ == '__main__':
    unittest.main()
