from django.test import TestCase
from .models import Task
from datetime import date
from datetime import timedelta
from django.core.exceptions import ValidationError
from .models import Task
from django.urls import reverse

class TaskModelTest(TestCase):
    def setUp(self):
        """Set up test data"""
        self.task = Task.objects.create(
            title="Task1",
            description="Description1",
            deadline=date.today() + timedelta(days=1),
            is_completed=False,
        )

    def test_task_creation(self):
        """Test if a task object is created correctly"""
        self.assertEqual(self.task.title, "Task1")
        self.assertEqual(self.task.description, "Description1")
        self.assertEqual(self.task.deadline, date.today()+timedelta(days=1))
        self.assertEqual(self.task.is_completed, False)

    def test_task_str(self):
        """Test the string representation of the task"""
        self.assertEqual(str(self.task), "Task1")
    

class TaskModelOrderingTest(TestCase):
    def setUp(self):
        """Set up tasks with varying deadlines"""
        now = date.today()
        self.task1 = Task.objects.create(title="Task 1", deadline=now + timedelta(days=3))
        self.task2 = Task.objects.create(title="Task 2", deadline=now + timedelta(days=1))
        self.task3 = Task.objects.create(title="Task 3", deadline=now + timedelta(days=2))

    def test_default_ordering(self):
        """Ensure tasks are ordered by deadline in ascending order by default"""
        tasks = Task.objects.all()
        self.assertEqual(list(tasks), [self.task2, self.task3, self.task1])

    def test_explicit_ordering(self):
        """Ensure explicit ordering with `order_by` works"""
        tasks_desc = Task.objects.all().order_by('-deadline')
        self.assertEqual(list(tasks_desc), [self.task1, self.task3, self.task2])


class TaskDeadlineValidationTest(TestCase):
    def test_valid_deadline(self):
        """Test that a future deadline is accepted"""
        future_time = date.today() + timedelta(days=1)
        task = Task(title="Future Task", deadline=future_time)
        try:
            task.full_clean()  # Trigger model validation
        except ValidationError:
            self.fail("ValidationError raised for a valid deadline")

    def test_invalid_deadline(self):
        """Test that a past or present deadline raises ValidationError"""
        past_time = date.today() - timedelta(days=3)
        task = Task(title="Past Task", deadline=past_time)
        with self.assertRaises(ValidationError):
            task.full_clean()



class TaskListViewTest(TestCase):
    def setUp(self):
        # Create some test tasks
        Task.objects.create(title="Task 1", deadline=date.today() + timedelta(days=1))
        Task.objects.create(title="Task 2", deadline=date.today() + timedelta(days=2))

    def test_task_list_view(self):
        """Test the task list view"""
        response = self.client.get(reverse('todo:task_list'))  # `home` refers to the root URL view
        self.assertEqual(response.status_code, 200)  # Check if the response is OK
        self.assertTemplateUsed(response, 'todo/task_list.html')  # Verify the correct template is used
        self.assertContains(response, "Task 1")  # Check if the content is in the response
        self.assertContains(response, "Task 2")
