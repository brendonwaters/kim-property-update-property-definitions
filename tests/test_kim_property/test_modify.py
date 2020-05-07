import os
from os.path import join, isfile

import kim_edn

from tests.test_kim_property import PyTest


class TestModifyModule:
    """Test kim_property utility module (modify)."""

    def test_modify(self):
        """Test the modify functionality."""
        # Create the property instance with the property name
        str_obj = self.kim_property.kim_property_create(
            1, 'cohesive-energy-relation-cubic-crystal')

        str_obj = self.kim_property.kim_property_modify(
            str_obj, 1,
            "key", "short-name",
            "source-value", "1", "fcc",
            "key", "species",
            "source-value", "1:4", "Al", "Al", "Al", "Al",
            "key", "a",
            "source-value",
            "1:5", "3.9149", "4.0000", "4.032", "4.0817", "4.1602",
            "source-unit", "angstrom", "digits", "5",
            "key", "basis-atom-coordinates",
            "source-value", "2", "1:2", "0.5", "0.5",
            "key", "basis-atom-coordinates",
            "source-value", "3", "1:3", "0.5", "0.0", "0.5",
            "key", "basis-atom-coordinates",
            "source-value", "4", "2:3", "0.5", "0.5",
            "key", "cohesive-potential-energy",
            "source-value",
            "1:5", "3.324", "3.3576", "3.3600", "3.3550", "3.3260",
            "source-std-uncert-value",
            "1:5", "0.002", "0.0001", "0.00001", "0.0012", "0.00015",
            "source-unit", "eV",
            "digits", "5")

        kim_obj = kim_edn.load(str_obj)[0]

        Property_Instance = '{"property-id" "tag:staff@noreply.openkim.org,2014-04-15:property/cohesive-energy-relation-cubic-crystal" "instance-id" 1 "short-name" {"source-value" ["fcc"]} "species" {"source-value" ["Al" "Al" "Al" "Al"]} "a" {"source-value" [3.9149 4.0 4.032 4.0817 4.1602] "source-unit" "angstrom" "digits" 5} "basis-atom-coordinates" {"source-value" [[0.0 0.0 0.0] [0.5 0.5 0.0] [0.5 0.0 0.5] [0.0 0.5 0.5]]} "cohesive-potential-energy" {"source-value" [3.324 3.3576 3.36 3.355 3.326] "source-std-uncert-value" [0.002 0.0001 1e-05 0.0012 0.00015] "source-unit" "eV" "digits" 5}}'

        self.assertTrue(Property_Instance == kim_edn.dumps(kim_obj))

        # Create the property instance with the property name
        str_obj = self.kim_property.kim_property_create(
            1, 'cohesive-energy-relation-cubic-crystal')

        str_obj = self.kim_property.kim_property_modify(
            str_obj, 1,
            "key", "short-name",
            "source-value", "1", "fcc",
            "key", "species",
            "source-value", "1:4", "Al", "Al", "Al", "Al")

        str_obj = self.kim_property.kim_property_modify(
            str_obj, 1,
            "key", "a",
            "source-value",
            "1:5", "3.9149", "4.0000", "4.032", "4.0817", "4.1602")

        str_obj = self.kim_property.kim_property_modify(
            str_obj, 1,
            "key", "a",
            "source-unit", "angstrom", "digits", "5")

        str_obj = self.kim_property.kim_property_modify(
            str_obj, 1,
            "key", "basis-atom-coordinates",
            "source-value", "4", "2:3", "0.5", "0.5",
            "key", "basis-atom-coordinates",
            "source-value", "3", "3", "0.5",
            "key", "basis-atom-coordinates",
            "source-value", "2", "1:2", "0.5", "0.5")

        str_obj = self.kim_property.kim_property_modify(
            str_obj, 1,
            "key", "basis-atom-coordinates",
            "source-value", "3", "1", "0.5")

        str_obj = self.kim_property.kim_property_modify(
            str_obj, 1,
            "key", "cohesive-potential-energy",
            "source-value",
            "1:5", "3.324", "3.3576", "3.3600", "3.3550", "3.3260",
            "source-std-uncert-value",
            "1:5", "0.002", "0.0001", "0.00001", "0.0012", "0.00015",
            "source-unit", "eV",
            "digits", "5")

        kim_obj = kim_edn.load(str_obj)[0]

        self.assertTrue(Property_Instance == kim_edn.dumps(kim_obj))

        # Test for scalar values
        str_obj = self.kim_property.kim_property_modify(
            str_obj, 1,
            "key", "space-group",
            "source-value", "Immm")

        kim_obj = kim_edn.load(str_obj)[0]

        self.assertTrue(kim_obj["space-group"]["source-value"] == "Immm")

        str_obj = self.kim_property.kim_property_modify(
            str_obj, 1,
            "key", "space-group",
            "source-value", "Fm-3m")

        kim_obj = kim_edn.load(str_obj)[0]

        self.assertTrue(kim_obj["space-group"]["source-value"] == "Fm-3m")

    def test_modify_exception(self):
        """Test the modify functionality on exceptions."""
        # Fails when the input is none or not created
        for str_obj in [None, '', 'None', '[]']:
            self.assertRaises(self.KIMPropertyError,
                              self.kim_property.kim_property_modify, str_obj, 1)

        # Fails when there is a different instance id
        str_obj = '[{"property-id" "tag:staff@noreply.openkim.org,2014-04-15:property/cohesive-energy-relation-cubic-crystal" "instance-id" 1}]'
        self.assertRaises(self.KIMPropertyError,
                          self.kim_property.kim_property_modify, str_obj, 2)

        # Fails when not having the instance id
        str_obj = '[{"property-id" "tag:staff@noreply.openkim.org,2014-04-15:property/cohesive-energy-relation-cubic-crystal"}]'
        self.assertRaises(self.KIMPropertyError,
                          self.kim_property.kim_property_modify, str_obj, 1)

        # Fails when not having the property id
        str_obj = '[{"instance-id" 1}]'
        self.assertRaises(self.KIMPropertyError,
                          self.kim_property.kim_property_modify, str_obj, 1)

        # Create the property instance with the property name
        str_obj = self.kim_property.kim_property_create(
            1, 'cohesive-energy-relation-cubic-crystal')

        # Fails when the instance id is not an integer
        self.assertRaises(self.KIMPropertyError,
                          self.kim_property.kim_property_modify, str_obj,
                          1.0)

        self.assertRaises(self.KIMPropertyError,
                          self.kim_property.kim_property_modify, str_obj,
                          "1")

        self.assertRaises(self.KIMPropertyError,
                          self.kim_property.kim_property_modify, str_obj,
                          "id")

        # Fails when one forgts to put the comma between inputs
        self.assertRaises(self.KIMPropertyError,
                          self.kim_property.kim_property_modify,
                          str_obj, 1,
                          "key", "a" "source-value", 1, 3.9149)

        self.assertRaises(self.KIMPropertyError,
                          self.kim_property.kim_property_modify,
                          str_obj, 1,
                          "key" "a", "source-value", 1, 3.9149)

        # Fails when value passed instead of index
        self.assertRaises(self.KIMPropertyError,
                          self.kim_property.kim_property_modify,
                          str_obj, 1,
                          "key", "a", "source-value", 3.9149)

        self.assertRaises(self.KIMPropertyError,
                          self.kim_property.kim_property_modify,
                          str_obj, 1,
                          "key", "a", "source-value", 2.5)

        self.assertRaises(self.KIMPropertyError,
                          self.kim_property.kim_property_modify,
                          str_obj, 1,
                          "key", "short-name", "source-value", "fcc")

        msg = 'input value '
        msg += '"{}" doesn\'t meet the '.format("fcc")
        msg += 'format specification. An integer '
        msg += 'equal to or greater than 1 '
        msg += 'or integer indices range of '
        msg += '"start:stop".'

        self.assertRaisesRegex(self.KIMPropertyError, msg,
                               self.kim_property.kim_property_modify,
                               str_obj, 1,
                               "key", "short-name", "source-value", "fcc")

        str_obj = self.kim_property.kim_property_modify(
            str_obj, 1,
            "key", "basis-atom-coordinates",
            "source-value", "4", "2:3", "0.5", "0.5",
            "key", "basis-atom-coordinates",
            "source-value", "3", "3", "0.5",
            "key", "basis-atom-coordinates",
            "source-value", "2", "1:2", "0.5", "0.5")

        # Fails when not in the standard key-value pairs
        self.assertRaises(self.KIMPropertyError,
                          self.kim_property.kim_property_modify,
                          str_obj, 1,
                          "key", "basis-atom-coordinates",
                          "source-unknown", 2.5)

        # Fails when not enough input
        self.assertRaises(self.KIMPropertyError,
                          self.kim_property.kim_property_modify,
                          str_obj, 1,
                          "key", "basis-atom-coordinates",
                          "source-value", 3)

        msg = 'there is not enough input arguments '
        msg += 'to use.\n Processing the {"basis-atom-coordinates"}:'
        msg += '{"source-value"} input arguments failed.\n The second '
        msg += 'index is missing from the input arguments.'

        self.assertRaisesRegex(self.KIMPropertyError, msg,
                               self.kim_property.kim_property_modify,
                               str_obj, 1,
                               "key", "basis-atom-coordinates",
                               "source-value", 3)

        self.assertRaises(self.KIMPropertyError,
                          self.kim_property.kim_property_modify,
                          str_obj, 1,
                          "key", "basis-atom-coordinates",
                          "source-value", "1", "1:3", 0.0, 0.0)

        self.assertRaises(self.KIMPropertyError,
                          self.kim_property.kim_property_modify,
                          str_obj, 1,
                          "key", "basis-atom-coordinates",
                          "source-value", "2", "1:3", 0.0, 0.5)

        self.assertRaises(self.KIMPropertyError,
                          self.kim_property.kim_property_modify,
                          str_obj, 1,
                          "key", "basis-atom-coordinates",
                          "source-value", "2", "2:3", 0.5)

        self.assertRaises(self.KIMPropertyError,
                          self.kim_property.kim_property_modify,
                          str_obj, 1,
                          "key", "basis-atom-coordinates",
                          "source-value", 3, 3)

        msg = 'there is not enough input arguments '
        msg += 'to use.\n Processing the {"basis-atom-coordinates"}:'
        msg += '{"source-value"} input arguments failed.\n '
        msg += 'At least we need one further input.'

        self.assertRaisesRegex(self.KIMPropertyError, msg,
                               self.kim_property.kim_property_modify,
                               str_obj, 1,
                               "key", "basis-atom-coordinates",
                               "source-value", 3, 3)

        self.assertRaises(self.KIMPropertyError,
                          self.kim_property.kim_property_modify,
                          str_obj, 1,
                          "key", "basis-atom-coordinates",
                          "source-value", 3, 4)

        msg = 'this dimension has a fixed length = 3, while, '
        msg += 'wrong index = 4 is requested.\n Processing the '
        msg += '{"basis-atom-coordinates"}:{"source-value"} input arguments,'
        msg += ' wrong index at the second dimension is requested.'

        self.assertRaisesRegex(self.KIMPropertyError, msg,
                               self.kim_property.kim_property_modify,
                               str_obj, 1,
                               "key", "basis-atom-coordinates",
                               "source-value", 3, 4)

        # Create the property instance with the property name
        str_obj = self.kim_property.kim_property_create(
            1, 'cohesive-potential-energy-cubic-crystal')

        # Fails paasing the wrong type
        self.assertRaises(ValueError,
                          self.kim_property.kim_property_modify,
                          str_obj, 1,
                          "key", "a", "source-value", "True")

        self.assertRaises(ValueError,
                          self.kim_property.kim_property_modify,
                          str_obj, 1,
                          "key", "a", "source-value", "false")

        self.assertRaises(ValueError,
                          self.kim_property.kim_property_modify,
                          str_obj, 1,
                          "key", "a", "digits", "false")

        self.assertRaises(ValueError,
                          self.kim_property.kim_property_modify,
                          str_obj, 1,
                          "key", "a", "digits", "true")

        self.assertRaises(self.KIMPropertyError,
                          self.kim_property.kim_property_modify,
                          str_obj, 1,
                          "key", "a", "digits", 3.14)


    # Extra check for the scalar values
    # see https://github.com/openkim/kim-property/issues/1
    def test_modify_exception_issue1(self):
        """Test the modify functionality on exceptions."""
        # Create the property instance with the property name
        str_obj = self.kim_property.kim_property_create(
            1, 'cohesive-energy-relation-cubic-crystal')

        str_obj = self.kim_property.kim_property_modify(
            str_obj, 1,
            "key", "short-name",
            "source-value", "1", "fcc",
            "key", "species",
            "source-value", "1:4", "Al", "Al", "Al", "Al",
            "key", "a",
            "source-value",
            "1:5", "3.9149", "4.0000", "4.032", "4.0817", "4.1602")

        # index for scalar key
        self.assertRaises(self.KIMPropertyError,
                          self.kim_property.kim_property_modify, str_obj, 1,
                          "key", "space-group", "source-value", 1, "Fm-3m")

        # index for keys with no extent
        self.assertRaises(self.KIMPropertyError,
                          self.kim_property.kim_property_modify, str_obj, 1,
                          "key", "a", "source-unit", 1, "angstrom")

        self.assertRaises(self.KIMPropertyError,
                          self.kim_property.kim_property_modify, str_obj, 1,
                          "key", "a", "source-unit", "angstrom",
                          "digits", 1, 5)

        self.assertRaises(self.KIMPropertyError,
                          self.kim_property.kim_property_modify, str_obj, 1,
                          "key", "cohesive-potential-energy",
                          "source-unit", 1, "eV", "digits", 1, "5")

        self.assertRaises(self.KIMPropertyError,
                          self.kim_property.kim_property_modify, str_obj, 1,
                          "key", "cohesive-potential-energy",
                          "source-value", "1:5", "3.324", "3.3576",
                          "3.3600", "3.3550", "3.3260",
                          "source-unit", 1, "eV", "digits", 1, "5")


class TestPyTestModifyModule(TestModifyModule, PyTest):
    pass
