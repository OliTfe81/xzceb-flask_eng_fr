"""
Module for translating text between English and French using MyMemoryTranslator.
"""

from deep_translator import MyMemoryTranslator

english_to_french_translator = MyMemoryTranslator(source='english', target='french')
french_to_english_translator = MyMemoryTranslator(source='french', target='english')

def english_to_french(english_text):
    """
    Translate English text to French.
    
    Args:
        english_text (str): Text in English to translate.
        
    Returns:
        str: Translated text in French.
    """
    french_text = english_to_french_translator.translate(english_text)
    return french_text

def french_to_english(french_text):
    """
    Translate French text to English.
    
    Args:
        french_text (str): Text in French to translate.
        
    Returns:
        str: Translated text in English.
    """
    english_text = french_to_english_translator.translate(french_text)
    return english_text
