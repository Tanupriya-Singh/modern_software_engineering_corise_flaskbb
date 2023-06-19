import pytest
from flaskbb.forum.forms import SpecialTopicForm, TopicForm
from unittest.mock import patch
pytestmark = pytest.mark.usefixtures("post_request_context", "default_settings")

###################################################################
# CoRise TODO done: add unit tests below that test the functionality of
# the `SpecialTopicForm`

class TestSpecialTopicForm(object):
    
    @patch('builtins.print')
    def test_class(self, mock_print):
        c = SpecialTopicForm()
        mock_print.assert_called_once_with("Initialized")

###################################################################