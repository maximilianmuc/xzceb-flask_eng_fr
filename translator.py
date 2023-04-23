"""Translation English to French and back"""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2023-04-23',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.eu-de.language-translator.watson.cloud.ibm.com')



def english_to_french(english_text):
    '''translation from english to french'''
    french_text = language_translator.translate(text=english_text,model_id='en-fr').get_result()
    #print(json.dumps(french_text, indent=2, ensure_ascii=False))
    return french_text["translations"][0]["translation"]

def french_to_english(french_text):
    '''translation from french to english'''
    english_text = language_translator.translate(text=french_text,model_id='fr-en').get_result()
    #print(json.dumps(english_text, indent=2, ensure_ascii=False))
    return english_text["translations"][0]["translation"]
