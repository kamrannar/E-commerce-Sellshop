from modeltranslation.translator import translator, TranslationOptions
from .models import Category

class CategoryTranslationOptions(TranslationOptions):
    fields = ('categories', 'subcategories')

translator.register(Category, CategoryTranslationOptions)