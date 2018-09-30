from django.test import TestCase
from .models import Subject


# Create your tests here.

class SubjectModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Subject.objects.create(name='first subject')
        Subject.objects.create(description='a description here')

    def test_name_content(self):
        subject = Subject.objects.get(id=1)
        expected_object_name = f'{subject.name}'
        self.assertEquals(expected_object_name, 'first subject')

    def test_description_content(self):
        subject = Subject.objects.get(id=2)
        expected_object_name = f'{subject.description}'
        self.assertEquals(expected_object_name, 'a description here')
