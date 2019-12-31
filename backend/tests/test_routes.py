# tests/test_routes.py (to do)
import unittest

class FlaskTestCase:

    # Ensure that Flask was set up correctly
    def test_index(self):
        response = self.client.get('/login', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # Ensure that main page requires user login
    def test_main_route_requires_login(self):
        response = self.client.get('/users/profile', follow_redirects=True)
        self.assertIn(b'Token is missing!', response.data)

    # Ensure that posts show up on the main page
    def test_posts_show_up_on_main_page(self):
        response = self.client.post(
            '/login',
            data=dict(username="admin", password="admin"),
            follow_redirects=True
        )
        self.assertIn("ok : True", response.data)


if __name__ == '__main__':
    unittest.main()
