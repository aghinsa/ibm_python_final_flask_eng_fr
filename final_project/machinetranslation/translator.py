import os

from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']


authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    authenticator=authenticator,
    version = "2018-05-01"
)

language_translator.set_service_url(url)

def englishToFrench(englishText):
    """
        Translates text in English to French
        Params:
            englishText:string: Text in English to be translated
        Return:string
            french translation
    """
    if len(englishText) == 0:
        return ""

    translation = language_translator.translate(
    text=englishText,
    model_id='en-fr').get_result()

    # list of translations
    translations = translation["translations"]
    return translations[0]["translation"]

def frenchToEnglish(frenchText):
    """
        Translates text in French to English
        Params:
            frenchText:string: Text in French to be translated
        Return:string
            English translation
    """
    if len(frenchText) == 0:
        return ""

    translation = language_translator.translate(
    text=frenchText,
    model_id='fr-en').get_result()

    # list of translations
    translations = translation["translations"]
    return translations[0]["translation"]
