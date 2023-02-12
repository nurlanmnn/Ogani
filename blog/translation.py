from modeltranslation.translator import translator, TranslationOptions

from .models import Blog, News

class BlogTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

translator.register(Blog, BlogTranslationOptions)
translator.register(News, NewsTranslationOptions)