from django.contrib import admin
from blog.models import Post,CustomUser,Comments

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','body','date_pub','author')
    list_display_links = ('title','body')



from .models import User
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import ugettext_lazy as _


# Указываем наши форма для создания и редактирования пользователя.
# Добавляем новые поля в fieldsets, и поле email в add_fieldsets.
class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': (
            'first_name',
            'last_name',
            'email',
            'avatar',
            'birthday'
        )}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2','birthday')}
        ),
    )

class CommentsAdmin(admin.ModelAdmin):
    list_display = ('body', 'comment_author','post')
    list_filter = ('comment_author','body')
    search_fields = ('comment_author','body')
admin.site.register(Comments, CommentsAdmin)
admin.site.register(CustomUser, UserAdmin)

admin.site.register(Post,PostAdmin)

