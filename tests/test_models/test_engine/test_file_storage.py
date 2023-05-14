    def test_5_save_state(self):
        """Tests save() method for State."""
        self.help_test_save("State")

    def test_5_save_city(self):
        """Tests save() method for City."""
        self.help_test_save("City")

    def test_5_save_amenity(self):
        """Tests save() method for Amenity."""
        self.help_test_save("Amenity")

    def test_5_save_place(self):
        """Tests save() method for Place."""
        self.help_test_save("Place")

    def test_5_save_review(self):
        """Tests save() method for Review."""
        self.help_test_save("Review")

    def test_5_save_no_args(self):
        """Tests save() with no arguments."""
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            FileStorage.save()
        msg = "save() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), msg)

    def test_5_save_excess_args(self):
        """Tests save() with too many arguments."""
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            FileStorage.save(self, 98)
        msg = "save() takes 1 positional argument but 2 were given"
        self.assertEqual(str(e.exception), msg)

    def help_test_reload(self, classname):
        """Helps test reload() method for classname."""
        self.resetStorage()
        storage.reload()
        self.assertEqual(FileStorage._FileStorage__objects, {})
        cls = storage.classes()[classname]
        o = cls()
        storage.new(o)
        key = "{}.{}".format(type(o).__name__, o.id)
        storage.save()
        storage.reload()
        self.assertEqual(o.to_dict(), storage.all()[key].to_dict())

    def test_5_reload_base_model(self):
        """Tests reload() method for BaseModel."""
        self.help_test_reload("BaseModel")

    def test_5_reload_user(self):
        """Tests reload() method for User."""
        self.help_test_reload("User")

    def test_5_reload_state(self):
        """Tests reload() method for State."""
        self.help_test_reload("State")

    def test_5_reload_city(self):
        """Tests reload() method for City."""
        self.help_test_reload("City")

    def test_5_reload_amenity(self):
        """Tests reload() method for Amenity."""
        self.help_test_reload("Amenity")

    def test_5_reload_place(self):
        """Tests reload() method for Place."""
        self.help_test_reload("Place")

    def test_5_reload_review(self):
        """Tests reload() method for Review."""
        self.help_test_reload("Review")

    def help_test_reload_mismatch(self, classname):
        """Helps test reload() method for classname."""
        self.resetStorage()
        storage.reload()
        self.assertEqual(FileStorage._FileStorage__objects, {})

        cls = storage.classes()[classname]
        o = cls()
        storage.new(o)
        key = "{}.{}".format(type(o).__name__, o.id)
        storage.save()
        o.name = "Laura"
        storage.reload()
        self.assertNotEqual(o.to_dict(), storage.all()[key].to_dict())

    def test_5_reload_mismatch_base_model(self):
        """Tests reload() method mismatch for BaseModel."""
        self.help_test_reload_mismatch("BaseModel")

    def test_5_reload_mismatch_user(self):
        """Tests reload_mismatch() method for User."""
        self.help_test_reload_mismatch("User")

    def test_5_reload_mismatch_state(self):
        """Tests reload_mismatch() method for State."""
        self.help_test_reload_mismatch("State")

    def test_5_reload_mismatch_city(self):
        """Tests reload_mismatch() method for City."""
        self.help_test_reload_mismatch("City")

    def test_5_reload_mismatch_amenity(self):
        """Tests reload_mismatch() method for Amenity."""
        self.help_test_reload_mismatch("Amenity")

    def test_5_reload_mismatch_place(self):
        """Tests reload_mismatch() method for Place."""
        self.help_test_reload_mismatch("Place")

    def test_5_reload_mismatch_review(self):
        """Tests reload_mismatch() method for Review."""
        self.help_test_reload_mismatch("Review")

    def test_5_reload_no_args(self):
        """Tests reload() with no arguments."""
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            FileStorage.reload()
        msg = "reload() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), msg)

    def test_5_reload_excess_args(self):
        """Tests reload() with too many arguments."""
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            FileStorage.reload(self, 98)
        msg = "reload() takes 1 positional argument but 2 were given"
        self.assertEqual(str(e.exception), msg)


if __name__ == '__main__':
    unittest.main()
