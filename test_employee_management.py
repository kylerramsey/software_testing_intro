import unittest
from employee_management import Employee, Post, Manager

class TestManagementSystem(unittest.TestCase):
    def test_employee_init(self):
        employee = Employee("Kyler", "Ramsey")
        self.assertIn(employee, employee.all_)
        # self.assertIn(employee.email, employee.all_)

    def test_create_post(self):
        # testing if the created post reads out the correct body
        employee = Employee("Kyler", "Ramsey")
        post_body = "This is a test."
        new_post = Post(post_body, employee.email)
        self.assertIn(new_post.body, "This is a test.")

        # testing if creating a post attaches it to the correct employees post list
        employee.create_post()
        self.assertTrue(employee.posts)
        
    def test_create_manager(self):
        employee = Employee("Derek", "Hawkins")
        manager = Manager("Ripal", "Coding_Temple")
        self.assertFalse(manager.employees)

    def test_add_employee(self):
        # testing an unsucessful addition of an employee
        employee1 = Employee("Kyler", "Ramsey")
        manager = Manager("Lucas", "Lang")
        self.assertNotIn(employee1 ,manager.employees)

    def test_show_post(self):
        # testing if an uploaded post is added to the company post feed
        employee = Employee("Kyler", "Ramsey")
        post_body = "This is a test."
        new_post = Post(post_body, employee.email)
        self.assertIn(new_post, Post.all_)

if __name__ == '__main__':
        unittest.main()