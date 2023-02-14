from modeltranslation.translator import translator, TranslationOptions

from .models import Setting, AboutUs

class SettingTranslationOptions(TranslationOptions):
    fields = ('address',)


class AboutUsTranslationOptions(TranslationOptions):
    fields = ('title', 'text')

translator.register(Setting, SettingTranslationOptions)
translator.register(AboutUs, AboutUsTranslationOptions)
