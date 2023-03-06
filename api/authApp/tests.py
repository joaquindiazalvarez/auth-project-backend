from django.test import TestCase
from .models import User

class ModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        """
        Set a data for testing it on the DB
        """
        cls.model = User.objects.create(name='testname', password=123456, email='test@test.com', birthdate='2000-1-1')

    def test_model_data(self):
        """
        Test that the data was saved correctly in DB
        """
        self.assertEqual(self.model.name, 'testname')
        self.assertEqual(self.model.password, 123456)
        self.assertEqual(self.model.email, 'test@test.com')
        self.assertEqual(self.model.birthdate, '2000-1-1')

    def test_model_validation(self):
        """
        Test that the model's validation works as expected. It must fail
        """
        # This model has no birthdate, and birthdate is a not null field on User model
        invalid_model = User(name='', password=123, email='')
        with self.assertRaises(ValueError):
            invalid_model.full_clean()

    def test_model_delete(self):
        # Test that the model can be deleted
        self.model.delete()
        self.assertFalse(User.objects.filter(name='testname').exists())

