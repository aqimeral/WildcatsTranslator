from google.auth.credentials import Credentials
from google.oauth2 import service_account
from google.cloud import aiplatform
from vertexai.preview.language_models import ChatModel, InputOutputTextPair

credentials = service_account.Credentials.from_service_account_file("/translator-419005-544a54bab75b.json")
aiplatform.init(project='translator-419005', credentials=credentials)


chat_model = ChatModel.from_pretrained("chat-bison@001")

def get_translation(post: str) -> str:
    # ----------------- DO NOT MODIFY ------------------ #

    parameters = {
        "temperature": 0.7,  # Temperature controls the degree of randomness in token selection.
        "max_output_tokens": 256,  # Token limit determines the maximum amount of text output.
    }

     # ---------------- YOUR CODE HERE ---------------- #
    context = "You are a professional translator. Please translate the following text to English." # TODO: Insert context
    chat = chat_model.start_chat(context=context)
    response = chat.send_message(post, **parameters)
    return response.text


def get_language(post: str) -> str:
    # ----------------- DO NOT MODIFY ------------------ #
    context = "Which language is the following text? Answer in one word." # TODO: Insert context
    parameters = {
        "temperature": 0.7,  # Temperature controls the degree of randomness in token selection.
        "max_output_tokens": 256,  # Token limit determines the maximum amount of text output.
    }

     # ---------------- YOUR CODE HERE ---------------- #
    chat = chat_model.start_chat(context=context)
    response = chat.send_message(post, **parameters)
    return response.text



def query_llm_robust(post: str) -> tuple[bool, str]:
  default_res = (True, '')
  try:
    language = get_language(post)
    assert(type(language) == str)
  except:
    print("LLM Failed to get the language of the Post.")
    return default_res

  try:
    translation = get_translation(post)
    assert(type(translation) == str)
  except:
    print("LLM Failed to get the translation of the Post.")
    return default_res

  language = language.lower()
  language = language.replace('.', '')

  # One word language
  if (" " in language):
    print("LLM provided poorly formatted language")
    return default_res

  # Not translated
  if language != 'english':
    translation_language = get_language(translation)
    translation_language = translation_language.lower().replace('.', '')
    if (language == translation_language):
      print("LLM failed to translate post")
      return default_res

  return (language == 'english', get_translation(post))
