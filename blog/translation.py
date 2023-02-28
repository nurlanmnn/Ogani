from modeltranslation.translator import translator, TranslationOptions
from .models import Blog, News, BlogCategory

class BlogTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


class BlogCategoryTranslationOptions(TranslationOptions):
    fileds = ('name')


class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


translator.register(Blog, BlogTranslationOptions)
translator.register(BlogCategory, BlogCategoryTranslationOptions)
translator.register(News, NewsTranslationOptions)



