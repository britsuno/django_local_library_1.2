from django.contrib import admin

# Register your models here.

from .models import Author, Language, Genre, Book, BookInstance

class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre', 'language')

    inlines = [BooksInstanceInline]

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'borrower', 'due_back', 'id')
    list_filter = ('status', 'due_back')
    
    fieldsets = (
        (None, {'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {'fields':('status', 'due_back', 'borrower')
        }),
        )   

class AuthorInline(admin.TabularInline):
    model = Book
    extra = 0

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')

    fields = ['first_name', 'last_name', ('date_of_birth')]    

    exclude = ['date_of_death']
   
    inlines = [AuthorInline] 

# admin.site.register(Book)
# admin.site.register(Author)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre)
# admin.site.register(BookInstance)
admin.site.register(Language)
