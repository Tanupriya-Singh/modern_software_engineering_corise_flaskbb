###################################################################
# CoRise TODO done: add an integration test that uses the test client to
# load the home page ('/'). Make sure the response code is 200 and
# that the response data contains something you expect to see on the
# home page.
#
# Hint: you can get the test client by calling `application.test_client()`
# when using the application test fixture.

# ADD CODE HERE

###################################################################
import pytest
import flask

class TestClient:
    def test_home(self, application, default_groups,default_settings, translations):
        with application.test_client() as test_client:
            response = test_client.get('/')
        assert response.status_code == 200
        assert flask.session is not None

# Good page for various flask testing- https://stackoverflow.com/questions/52028124/why-use-flasks-app-test-client-over-requests-session-for-testing
