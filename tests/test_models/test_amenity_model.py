#!/usr/bin/python3

"""
Test for the Amenity model.
"""

import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """
    Testing Amenity class.
    """

    def test_Amenity_inheritence(self):
        """
        Test that the Amenity class inherits from BaseModel.
        """
        new_amenity = Amenity()
        self.assertIsInstance(new_amenity, BaseModel)

    def test_Amenity_attributes(self):
        """
        Test that the Amenity class has a 'name' attribute.
        """
        new_amenity = Amenity()
        self.assertTrue("name" in new_amenity.__dir__())

    def test_Amenity_attribute_type(self):
        """
        Test that the Amenity class's 'name' attribute is of type str.
        """
        new_amenity = Amenity()
        name_value = getattr(new_amenity, "name")
        self.assertIsInstance(name_value, str)

if __name__ == "__main__":
    unittest.main()
