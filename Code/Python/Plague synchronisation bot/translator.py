# -*- coding: utf-8 -*-
from deep_translator import GoogleTranslator


def translate(message: str, source_lang: str, target_lang: str):
    translator = GoogleTranslator(source=source_lang, target=target_lang)
    return translator.translate(message)
