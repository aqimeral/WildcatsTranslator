from src.translator import query_llm_robust
from mock import patch

@patch('vertexai.preview.language_models._PreviewChatSession.send_message')
def test_unexpected_language(mocker):
  default_res = (True, '')
  # we mock the model's response to return a random message
  mocker.return_value.text = "I don't understand your request"
  assert query_llm_robust("Aquí está su primer ejemplo.") == default_res


@patch('vertexai.preview.language_models._PreviewChatSession.send_message')
def test_non_string_result(mocker):
  default_res = (True, '')
  mocker.return_value.text = 123
  assert query_llm_robust("Aquí está su primer ejemplo.") == default_res


@patch('vertexai.preview.language_models._PreviewChatSession.send_message')
def test_empty_string(mocker):
  default_res = (True, '')
  mocker.return_value.text = ''
  assert query_llm_robust("Aquí está su primer ejemplo.") == default_res

@patch('vertexai.preview.language_models._PreviewChatSession.send_message')
def test_non_english_result(mocker):
  default_res = (True, '')
  mocker.return_value.text = '随机文本'
  assert query_llm_robust("Aquí está su primer ejemplo.") == default_res