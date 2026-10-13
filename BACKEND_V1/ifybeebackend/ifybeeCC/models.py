from django.db import models
from django.core.exceptions import ValidationError
from django.templatetags.static import static
import urllib.parse


class SiteSetting(models.Model):
    """
    General site configuration, business contact details, and core text.
    Managed by the owner through Django Admin.
    """
    site_name = models.CharField(
        max_length=200,
        default="Ifybee's Cakes & Confectionery",
        help_text="Business name displayed across the website."
    )
    hero_label = models.CharField(
        max_length=200,
        default="IFYBEE'S CAKES & CONFECTIONERY",
        help_text="Top eyebrow tagline on the hero."
    )
    whatsapp_number = models.CharField(
        max_length=50,
        blank=True,
        default="2348121402824",
        help_text="WhatsApp phone number in international format without '+' or spaces (e.g. 2348121402824)."
    )
    phone_display = models.CharField(
        max_length=50,
        blank=True,
        default="+234 812 140 2824",
        help_text="Public phone display label (e.g. +234 812 140 2824)."
    )
    address = models.CharField(
        max_length=255,
        blank=True,
        default="No. 18 Umuodu Ihitte Isi Mbieri, Opposite Mmesoma Building, Mbaitoli LGA, Owerri, Imo State, Nigeria",
        help_text="Bakery physical address or city."
    )
    instagram_url = models.URLField(
        blank=True,
        default="https://www.instagram.com/ifybeescakesandevents?dlrf=NmtrNG05b2NtMGFi",
        help_text="Link to official Instagram profile."
    )
    tiktok_url = models.URLField(
        blank=True,
        default="https://www.tiktok.com/@ifybeescakes001?_r=1&_t=ZS-9AV1gxz7m4N",
        help_text="Link to official TikTok profile."
    )
    facebook_url = models.URLField(
        blank=True,
        default="https://www.facebook.com/IfybeesCakesAndEvents",
        help_text="Link to official Facebook page."
    )
    
    # Homepage Intro text
    welcome_label = models.CharField(
        max_length=100,
        default="WELCOME TO IFYBEE'S",
        help_text="Small heading above welcome title."
    )
    welcome_title = models.CharField(
        max_length=200,
        default="Where every creation matters."
    )
    welcome_text_1 = models.TextField(
        default="At Ifybee's Cakes & Confectionery, we believe food should be more than something you eat. It should become part of the memory."
    )
    welcome_text_2 = models.TextField(
        default="From beautifully designed celebration cakes to freshly baked pastries and practical baking classes, every creation is made to bring something special to your day."
    )

    # About Page Story text
    about_heading = models.CharField(
        max_length=200,
        default="Built around creativity and care."
    )
    about_story_1 = models.TextField(
        default="Ifybee's Cakes & Confectionery was born from a deep love for baking, thoughtful artistic detail, and the simple joy of seeing people smile when they taste something made with genuine care."
    )
    about_story_2 = models.TextField(
        default="What began as a passionate pursuit baking bespoke cakes for family birthdays and close celebrations gradually expanded into a dedicated confectionery brand. Word-of-mouth recommendations from satisfied clients helped Ifybee's grow into a recognized kitchen known for dependable taste and beautiful aesthetics."
    )
    about_story_3 = models.TextField(
        default="Today, Ifybee's is not only a home for delectable celebration cakes and oven-fresh pastries, but also a nurturing learning hub where eager students master the craft of professional baking."
    )

    # Shared footer summary
    footer_tagline = models.TextField(
        default="Beautiful cakes, artisanal pastries, and practical baking education. Bringing joy to every celebration."
    )

    class Meta:
        verbose_name = "Site Configuration"
        verbose_name_plural = "Site Configuration"

    def __str__(self):
        return self.site_name

    def get_whatsapp_url(self, default_text="Hello Ifybee's, I would like to make an enquiry."):
        """Constructs an active WhatsApp click-to-chat URL or fallback."""
        if not self.whatsapp_number:
            return "https://wa.me/?text=" + urllib.parse.quote(default_text)
        return f"https://wa.me/{self.whatsapp_number}?text={urllib.parse.quote(default_text)}"


class HeroSlide(models.Model):
    """
    Homepage full-screen hero slideshow slides.
    Editable, reorderable, and toggleable through Django Admin.
    """
    heading = models.CharField(
        max_length=200,
        default="A Taste.",
        help_text="First line of the hero title."
    )
    subheading = models.CharField(
        max_length=200,
        default="A Lifetime Delight.",
        blank=True,
        help_text="Second line of the hero title (highlighted in gold)."
    )
    description = models.TextField(
        default="Beautiful cakes, delicious pastries and unforgettable experiences, crafted with care for every occasion."
    )
    image = models.ImageField(
        upload_to="hero_slides/",
        blank=True,
        null=True,
        help_text="Upload a hero image (recommended: 1920x1080)."
    )
    fallback_image_path = models.CharField(
        max_length=255,
        blank=True,
        default="IMAGES/cakes/cake image 3.jpg",
        help_text="Static image path used if no custom image is uploaded."
    )
    button_text = models.CharField(
        max_length=100,
        default="Explore Gallery",
        blank=True
    )
    button_link = models.CharField(
        max_length=200,
        default="/gallery/",
        blank=True
    )
    secondary_button_text = models.CharField(
        max_length=100,
        default="Baking Academy",
        blank=True
    )
    secondary_button_link = models.CharField(
        max_length=200,
        default="/academy/",
        blank=True
    )
    order = models.PositiveIntegerField(
        default=0,
        help_text="Display order (slides are shown from lowest to highest)."
    )
    is_active = models.BooleanField(
        default=True,
        help_text="Only active slides appear on the homepage."
    )

    class Meta:
        ordering = ['order', 'id']
        verbose_name = "Hero Slide"
        verbose_name_plural = "Hero Slides"

    def __str__(self):
        return f"{self.heading} {self.subheading}".strip()

    def get_image_url(self):
        if self.image:
            return self.image.url
        if self.fallback_image_path:
            return static(self.fallback_image_path)
        return static("IMAGES/cakes/cake image 3.jpg")


class GalleryItem(models.Model):
    """
    Portfolio gallery media (cakes, pastries, academy training).
    Supports uploaded photos, static fallbacks, uploaded videos, and video URLs.
    """
    CATEGORY_CHOICES = [
        ('cakes', 'Cakes'),
        ('pastries', 'Pastries'),
        ('academy', 'Academy & Training'),
    ]

    title = models.CharField(
        max_length=200,
        help_text="Display title for the gallery item."
    )
    caption = models.TextField(
        blank=True,
        help_text="Short description or caption."
    )
    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default='cakes'
    )
    image = models.ImageField(
        upload_to="gallery/images/",
        blank=True,
        null=True,
        help_text="Upload high-quality photograph."
    )
    static_image_path = models.CharField(
        max_length=255,
        blank=True,
        help_text="Static image path (e.g. IMAGES/cakes/cake image 3.jpg)."
    )
    video = models.FileField(
        upload_to="gallery/videos/",
        blank=True,
        null=True,
        help_text="Upload MP4 video file if this is a video item."
    )
    video_url = models.URLField(
        blank=True,
        help_text="Or provide a direct MP4 URL."
    )
    static_video_path = models.CharField(
        max_length=255,
        blank=True,
        help_text="Static video path fallback (e.g. VIDEOS/VID-20260528-WA0023.mp4)."
    )
    source_credit = models.CharField(
        max_length=255,
        blank=True,
        help_text="Optional attribution note (e.g., 'Demonstration sample' or 'Ifybee Kitchen')."
    )
    date_added = models.DateTimeField(auto_now_add=True)
    order = models.PositiveIntegerField(
        default=0,
        help_text="Display order (lower numbers appear first)."
    )
    is_active = models.BooleanField(
        default=True,
        help_text="Toggle visibility in the gallery."
    )

    class Meta:
        ordering = ['order', '-date_added']
        verbose_name = "Gallery Item"
        verbose_name_plural = "Gallery Items"

    def __str__(self):
        return f"{self.title} ({self.get_category_display()})"

    def clean(self):
        super().clean()
        has_media = bool(self.image or self.static_image_path or self.video or self.video_url or self.static_video_path)
        if not has_media:
            raise ValidationError("Please provide an image, static image path, video file, video URL, or static video path.")

    @property
    def is_video(self):
        return bool(self.video or self.video_url or self.static_video_path)

    def get_image_url(self):
        if self.image:
            return self.image.url
        if self.static_image_path:
            return static(self.static_image_path)
        return ""

    def get_video_url(self):
        if self.video:
            return self.video.url
        if self.static_video_path:
            return static(self.static_video_path)
        return self.video_url or ""


class AcademyClass(models.Model):
    """
    Baking Academy classes and bootcamps.
    Supports upcoming, ongoing, and past workshops.
    """
    STATUS_CHOICES = [
        ('upcoming', 'Upcoming Workshop (Open for Registration)'),
        ('ongoing', 'Currently Ongoing'),
        ('completed', 'Past Workshop'),
    ]

    title = models.CharField(
        max_length=200,
        help_text="Class name (e.g., 'Cake Baking & Fondant Masterclass')."
    )
    subtitle = models.CharField(
        max_length=200,
        blank=True,
        default="Masterclass",
        help_text="Highlighted secondary title word."
    )
    description = models.TextField(
        help_text="Detailed overview of what the class covers."
    )
    date_info = models.CharField(
        max_length=150,
        help_text="Dates or cohort timing (e.g., 'Next Cohort: 15th – 20th Next Month')."
    )
    schedule_info = models.CharField(
        max_length=150,
        blank=True,
        default="10:00 AM – 3:00 PM Daily",
        help_text="Daily hours."
    )
    location = models.CharField(
        max_length=200,
        blank=True,
        default="Ifybee Studio, No. 18 Umuodu Ihitte Isi Mbieri, Mbaitoli LGA, Owerri, Imo State",
        help_text="Classroom or studio location."
    )
    skill_level = models.CharField(
        max_length=100,
        blank=True,
        default="Beginner to Intermediate"
    )
    materials_note = models.CharField(
        max_length=150,
        blank=True,
        default="Provided in class"
    )
    certificate_note = models.CharField(
        max_length=150,
        blank=True,
        default="Issued upon completion"
    )
    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default='upcoming'
    )
    is_featured = models.BooleanField(
        default=False,
        help_text="Set to True to highlight this class as the main featured workshop."
    )
    image = models.ImageField(
        upload_to="academy/classes/",
        blank=True,
        null=True,
        help_text="Main photograph for this class."
    )
    static_image_path = models.CharField(
        max_length=255,
        blank=True,
        default="IMAGES/academy/A.webp",
        help_text="Static image path used as fallback."
    )
    whatsapp_message = models.CharField(
        max_length=255,
        blank=True,
        default="Hello Ifybee's, I would like to register for the upcoming Baking Masterclass.",
        help_text="Custom prefilled message sent when a student taps Register on WhatsApp."
    )
    order = models.PositiveIntegerField(
        default=0,
        help_text="Display order."
    )
    is_active = models.BooleanField(
        default=True,
        help_text="Toggle visibility."
    )

    class Meta:
        ordering = ['order', 'id']
        verbose_name = "Academy Class"
        verbose_name_plural = "Academy Classes"

    def __str__(self):
        return f"{self.title} ({self.get_status_display()})"

    def get_image_url(self):
        if self.image:
            return self.image.url
        if self.static_image_path:
            return static(self.static_image_path)
        return static("IMAGES/academy/A.webp")


class ClassMedia(models.Model):
    """
    Photographs and video clips from classes, workshops, and student practicals.
    """
    MEDIA_TYPE_CHOICES = [
        ('photo', 'Photo'),
        ('video', 'Video'),
    ]

    academy_class = models.ForeignKey(
        AcademyClass,
        on_delete=models.CASCADE,
        related_name="media_items",
        blank=True,
        null=True,
        help_text="Optionally link this photo/video to a specific academy class."
    )
    title = models.CharField(
        max_length=200,
        help_text="Caption or title (e.g. 'Hands-on Practice', 'Decorating Workshop')."
    )
    caption = models.TextField(
        blank=True,
        help_text="Short description of what students are doing."
    )
    media_type = models.CharField(
        max_length=10,
        choices=MEDIA_TYPE_CHOICES,
        default='photo'
    )
    image = models.ImageField(
        upload_to="academy/media/",
        blank=True,
        null=True
    )
    static_image_path = models.CharField(
        max_length=255,
        blank=True,
        help_text="Static image path fallback."
    )
    video = models.FileField(
        upload_to="academy/media/videos/",
        blank=True,
        null=True
    )
    video_url = models.URLField(
        blank=True,
        help_text="Or direct video URL (e.g. MP4 demo)."
    )
    static_video_path = models.CharField(
        max_length=255,
        blank=True,
        help_text="Static video path fallback (e.g. VIDEOS/VID_20260926_105441.mp4)."
    )
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order', 'id']
        verbose_name = "Academy Media Item"
        verbose_name_plural = "Academy Media Items"

    def __str__(self):
        return f"{self.title} ({self.get_media_type_display()})"

    def get_image_url(self):
        if self.image:
            return self.image.url
        if self.static_image_path:
            return static(self.static_image_path)
        return ""

    def get_video_url(self):
        if self.video:
            return self.video.url
        if self.static_video_path:
            return static(self.static_video_path)
        return self.video_url or ""


class AcademyCurriculumModule(models.Model):
    """
    Structured syllabus modules shown on the Academy page.
    """
    module_number = models.CharField(max_length=10, default="01")
    title = models.CharField(max_length=200)
    description = models.TextField()
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order', 'id']
        verbose_name = "Curriculum Module"
        verbose_name_plural = "Curriculum Modules"

    def __str__(self):
        return f"Module {self.module_number}: {self.title}"


class AcademyAnnouncement(models.Model):
    """
    Notices, weekend workshops, and one-on-one mentorship announcements.
    """
    badge_text = models.CharField(max_length=100, default="Upcoming Schedule")
    title = models.CharField(max_length=200)
    description = models.TextField()
    whatsapp_query = models.CharField(
        max_length=255,
        blank=True,
        default="Hello Ifybee's, I am interested in this workshop."
    )
    is_gold_border = models.BooleanField(
        default=False,
        help_text="Gives this card an accent gold border."
    )
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order', 'id']
        verbose_name = "Academy Announcement"
        verbose_name_plural = "Academy Announcements"

    def __str__(self):
        return self.title
