from google.auth.credentials import Credentials
from google.oauth2 import service_account
from google.cloud import aiplatform
from vertexai.preview.language_models import ChatModel, InputOutputTextPair

credentials = service_account.Credentials.from_service_account_info({
  "type": "service_account",
  "project_id": "translator-419005",
  "private_key_id": "544a54bab75b33446616750c167b64ec0d63a992",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQCnzRyIvQ1ZTq0m\n7CxNx3ubiAUBUZCqXFsIcp83e3taKuM6nReviyCYzr2hWTo1b+QbQLBIf7pXjch2\nT8dxsmpMd8QiGZXzd5/UVuXmVoPZ1ZpvBwc4+tgHEdpGu7Q7TpCwo6oIueCZI4hY\naYBjknHfN3+0CYlI7dsDXDOZLpCeTAv5BzVqYgCMZIf3oZyEqDCAfFjMjsdO8v1S\n4KYuT7huBrdGeDltCVd2iyUjn1NKbBq31E4jf89cSZzpq00SXilonP5mHUcCYn0f\n7i58Z5uSgCuQ2S5vTJE5JhyNczdQuP75Abk8JYNNBhFQAHAgqVIYtf73/WwzajKA\nzTXjpMPlAgMBAAECggEABcDFmOw5uYVgmzbvLkEn3CqobfBk4EEM2kgLFzz2UHPW\neQ4QP74/y/AQoSgc6QlGSJHp8/5fE5KNRtMlkHYbE2FAJKF8b427JC2mMa9nKLAx\nsdtLlIOd0EuSJdPYfM0M2brZa6BV0ozyPIJs0AfMvCgGtT6Qyfg6W/iMs1SHnvRd\nsQrOk8WmhTX4+VHK4jjjwqE9gIAWafoVNbKOmW+q/RKQS+PuGR074kIfWLb2R+Ua\nTnVmjN6CX4EiLby0OdJQu8V0yQ/6nnlZGzHqbSwf/lWacusu0+9G4KHW5bD55Zf6\njvkAak1dfOXozv8XNNkO3SxDWQuyie0n4Dvf99V6mQKBgQDqIwL+aLXuPxiGqJ+Q\n/WXe62YGS1aNB9G/R4SK6TNuI31REWM0se+LpiJSuxWh+7EgAyilbt+uA+/VMA3P\npQU+t/49dAdim7hyu4GG0rW3kBw+wgzAk4GsGMqBCzYJmP2E2T4U/gyUl8DI6NBJ\nHh978Yp++j/+Bimq+yDqm2KYqQKBgQC3eFzq9MWMxKmXG6Gkrq1ycMopVAZwVQe4\nCSBtpRt7dGk1d8YrBGEg5Sd6dd72kTITA59EhuSsAEndk77bmZ/8e3LHOpfjm92Y\nlh25DmWo00bxrQyyn46bf1qgTMo3/gZVUciq3RRGjLPvw4O4Ad9FtyiN50VVnCKT\n6mGKN2lq3QKBgBldial+NpeFBmcwRXkzuqGX5wmvh8Tnn/WVDerusL+x4JWzyIeg\n7061xOopkoJl/h51uSWTCXCUxJrYBecE/bh5vnVx6IrqS+VCIxo0IbOtTSIPa8pB\nML8wQGASktwfUvfdgThM/ZfriNs7PbVuKgMHe/WdrukaSdFYO4yvINNhAoGAcsYD\nKqCxLJyikvsgJct4iczxSuVbmc43o/Nhq/XLuXFbl60z9RkqQc/Y4Iz4TDsMnkR3\n0ACq8MbFbq3MicgTA3mele+bsTGCcMAIHApboj95dBqThPK33aLP6NPg9SIeiCU/\naVQgKPpAXk9rCSNyr0QjRJJXF3UzVGEdX7/GXKkCgYAu6X7BsqIHd9aC2siWe8KX\noCBTJMDdiyTfz2a8axL+us8TZn17VE6/d/8yt5qZanLEpq/molWLn0fzITsdjMWl\n3pJdbUBZ4KrDlocEDAhSkCXynJhI2YFF7+qv77gn6jGn2pSVcAp7cEeeoQSlS89A\ndYfwUimcyFGDyZIwt6Nn8w==\n-----END PRIVATE KEY-----\n",
  "client_email": "820387500890-compute@developer.gserviceaccount.com",
  "client_id": "106903921378560974208",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/820387500890-compute%40developer.gserviceaccount.com",
  "universe_domain": "googleapis.com"
})
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
    assert(language != '')
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
    try:
      translation.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
      print("LLM failed to translate post")
      return default_res

  return (language == 'english', get_translation(post))
