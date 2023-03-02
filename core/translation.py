from modeltranslation.translator import translator, TranslationOptions

from .models import FAQ, PrivacyPolicy, Setting, AboutUs, SecureShopping, DeliveryInfo, OurServices

class SettingTranslationOptions(TranslationOptions):
    fields = ('address',)


class SecureShoppingTranslationOptions(TranslationOptions):
    fields = ('title', 'text')


class DeliveryInfoTranslationOptions(TranslationOptions):
    fields = ('title', 'text')


class OurServicesTranslationOptions(TranslationOptions):
    fields = ('title', 'text')


class AboutUsTranslationOptions(TranslationOptions):
    fields = ('title', 'text')


class PrivacyPolicyTranslationOptions(TranslationOptions):
    fields = ('title', 'text')


class FAQTranslationOptions(TranslationOptions):
    fields = ('title', 'text')


translator.register(Setting, SettingTranslationOptions)
translator.register(AboutUs, AboutUsTranslationOptions)
translator.register(SecureShopping, SecureShoppingTranslationOptions)
translator.register(DeliveryInfo, DeliveryInfoTranslationOptions)
translator.register(OurServices, OurServicesTranslationOptions)
translator.register(PrivacyPolicy, PrivacyPolicyTranslationOptions)
translator.register(FAQ, FAQTranslationOptions)





