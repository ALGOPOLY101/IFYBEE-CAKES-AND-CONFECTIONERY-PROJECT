from django.contrib import admin
from django.utils.html import mark_safe
from .models import (
    SiteSetting,
    HeroSlide,
    GalleryItem,
    AcademyClass,
    ClassMedia,
    AcademyCurriculumModule,
    AcademyAnnouncement,
)

# Customize Admin Site branding
admin.site.site_header = "Ifybee's Cakes & Confectionery — Administration"
admin.site.site_title = "Ifybee's Admin Portal"
admin.site.index_title = "Bakery & Academy Website Content Management"


@admin.register(SiteSetting)
class SiteSettingAdmin(admin.ModelAdmin):
    list_display = ('site_name', 'phone_display', 'whatsapp_number', 'address')
    fieldsets = (
        ('Branding & Contact Information', {
            'fields': (
                'site_name',
                'hero_label',
                'whatsapp_number',
                'phone_display',
                'address',
                'footer_tagline',
            ),
            'description': 'Main business information, contact details, and footer summary.',
        }),
        ('Social Media Profiles', {
            'fields': ('instagram_url', 'tiktok_url', 'facebook_url'),
            'description': 'Direct links to official social profiles.',
        }),
        ('Homepage Welcome Section', {
            'fields': ('welcome_label', 'welcome_title', 'welcome_text_1', 'welcome_text_2'),
            'description': 'Introduction text shown directly below the hero section on the homepage.',
        }),
        ('About Page Story Section', {
            'fields': ('about_heading', 'about_story_1', 'about_story_2', 'about_story_3'),
            'description': 'Story text shown on the About page.',
        }),
    )

    def has_add_permission(self, request):
        # Only allow 1 site configuration row
        if self.model.objects.exists():
            return False
        return super().has_add_permission(request)


@admin.register(HeroSlide)
class HeroSlideAdmin(admin.ModelAdmin):
    list_display = ('slide_thumbnail', 'heading', 'subheading', 'order', 'is_active')
    list_display_links = ('heading', 'subheading')
    list_editable = ('order', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('heading', 'subheading', 'description')
    ordering = ('order', 'id')

    fieldsets = (
        ('Slide Content', {
            'fields': ('heading', 'subheading', 'description'),
            'description': 'Headlines and short description displayed on the slide.',
        }),
        ('Slide Background Image', {
            'fields': ('image', 'fallback_image_path'),
            'description': 'Upload a custom photo or specify a static fallback path.',
        }),
        ('Primary Action Button', {
            'fields': ('button_text', 'button_link'),
        }),
        ('Secondary Action Button', {
            'fields': ('secondary_button_text', 'secondary_button_link'),
        }),
        ('Display Settings', {
            'fields': ('order', 'is_active'),
        }),
    )

    def slide_thumbnail(self, obj):
        url = obj.get_image_url()
        if url:
            return mark_safe(f'<img src="{url}" style="height: 50px; width: 80px; object-fit: cover; border-radius: 4px;" />')
        return "No Image"
    slide_thumbnail.short_description = "Preview"


@admin.register(GalleryItem)
class GalleryItemAdmin(admin.ModelAdmin):
    list_display = ('media_thumbnail', 'title', 'category', 'media_kind', 'order', 'is_active', 'date_added')
    list_display_links = ('title',)
    list_editable = ('order', 'is_active')
    list_filter = ('category', 'is_active', 'date_added')
    search_fields = ('title', 'caption', 'source_credit')
    ordering = ('order', '-date_added')

    fieldsets = (
        ('Item Information', {
            'fields': ('title', 'category', 'caption', 'source_credit'),
        }),
        ('Photo (Upload or Static Path)', {
            'fields': ('image', 'static_image_path'),
            'description': 'Provide an uploaded photo or static image path.',
        }),
        ('Video (File, Local Static Path, or URL)', {
            'fields': ('video', 'static_video_path', 'video_url'),
            'description': 'If this item is a video, upload an MP4, specify a local static path, or provide a video URL.',
        }),
        ('Display & Visibility', {
            'fields': ('order', 'is_active'),
        }),
    )

    def media_thumbnail(self, obj):
        url = obj.get_image_url()
        if url:
            return mark_safe(f'<img src="{url}" style="height: 50px; width: 65px; object-fit: cover; border-radius: 4px;" />')
        elif obj.video or obj.video_url or obj.static_video_path:
            return mark_safe('<span style="font-size: 20px;">🎥 Video</span>')
        return "No Media"
    media_thumbnail.short_description = "Preview"

    def media_kind(self, obj):
        return "Video" if obj.is_video else "Photo"
    media_kind.short_description = "Media Type"


@admin.register(AcademyClass)
class AcademyClassAdmin(admin.ModelAdmin):
    list_display = ('class_thumbnail', 'title', 'status', 'date_info', 'is_featured', 'order', 'is_active')
    list_display_links = ('title',)
    list_editable = ('is_featured', 'order', 'is_active')
    list_filter = ('status', 'is_featured', 'is_active')
    search_fields = ('title', 'description', 'location')
    ordering = ('order', 'id')

    fieldsets = (
        ('Class Overview', {
            'fields': ('title', 'subtitle', 'description', 'status', 'is_featured'),
        }),
        ('Class Schedule & Venue', {
            'fields': ('date_info', 'schedule_info', 'location', 'skill_level', 'materials_note', 'certificate_note'),
        }),
        ('Class Media & Registration', {
            'fields': ('image', 'static_image_path', 'whatsapp_message'),
        }),
        ('Display & Visibility', {
            'fields': ('order', 'is_active'),
        }),
    )

    def class_thumbnail(self, obj):
        url = obj.get_image_url()
        if url:
            return mark_safe(f'<img src="{url}" style="height: 50px; width: 75px; object-fit: cover; border-radius: 4px;" />')
        return "No Image"
    class_thumbnail.short_description = "Photo"


@admin.register(ClassMedia)
class ClassMediaAdmin(admin.ModelAdmin):
    list_display = ('media_thumbnail', 'title', 'academy_class', 'media_type', 'order', 'is_active')
    list_display_links = ('title',)
    list_editable = ('order', 'is_active')
    list_filter = ('media_type', 'is_active', 'academy_class')
    search_fields = ('title', 'caption')
    ordering = ('order', 'id')

    fieldsets = (
        ('Class Media Information', {
            'fields': ('title', 'academy_class', 'caption', 'media_type'),
        }),
        ('Photo (Upload or Static Path)', {
            'fields': ('image', 'static_image_path'),
        }),
        ('Video (Upload, Local Static Path, or URL)', {
            'fields': ('video', 'static_video_path', 'video_url'),
        }),
        ('Display & Visibility', {
            'fields': ('order', 'is_active'),
        }),
    )

    def media_thumbnail(self, obj):
        url = obj.get_image_url()
        if url:
            return mark_safe(f'<img src="{url}" style="height: 45px; width: 65px; object-fit: cover; border-radius: 4px;" />')
        elif obj.video or obj.video_url or obj.static_video_path:
            return mark_safe('<span>🎥 Video</span>')
        return "No Media"
    media_thumbnail.short_description = "Preview"


@admin.register(AcademyCurriculumModule)
class AcademyCurriculumModuleAdmin(admin.ModelAdmin):
    list_display = ('module_number', 'title', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    ordering = ('order', 'id')


@admin.register(AcademyAnnouncement)
class AcademyAnnouncementAdmin(admin.ModelAdmin):
    list_display = ('title', 'badge_text', 'is_gold_border', 'order', 'is_active')
    list_editable = ('is_gold_border', 'order', 'is_active')
    ordering = ('order', 'id')
