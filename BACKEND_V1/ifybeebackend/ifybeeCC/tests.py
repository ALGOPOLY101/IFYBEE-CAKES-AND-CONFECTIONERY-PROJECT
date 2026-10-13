from django.test import TestCase, Client
from django.urls import reverse
from django.contrib import admin
from ifybeeCC.models import (
    SiteSetting,
    HeroSlide,
    GalleryItem,
    AcademyClass,
    ClassMedia,
    AcademyCurriculumModule,
    AcademyAnnouncement,
)


class PageResolutionTests(TestCase):
    """Verify all 4 public website pages and Django Admin resolve with HTTP 200."""

    def setUp(self):
        self.client = Client()

    def test_homepage_resolves(self):
        response = self.client.get(reverse('ifybeeCC:home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ifybeeCC/index.html')
        self.assertTemplateUsed(response, 'ifybeeCC/base.html')

    def test_gallery_page_resolves(self):
        response = self.client.get(reverse('ifybeeCC:gallery'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ifybeeCC/gallery.html')

    def test_academy_page_resolves(self):
        response = self.client.get(reverse('ifybeeCC:academy'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ifybeeCC/academy.html')

    def test_about_page_resolves(self):
        response = self.client.get(reverse('ifybeeCC:about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ifybeeCC/about.html')

    def test_admin_portal_accessible(self):
        response = self.client.get('/admin/login/?next=/admin/')
        self.assertEqual(response.status_code, 200)


class NavigationExclusionTests(TestCase):
    """
    Ensure each page excludes its own link from the main header navigation:
    - Home: Gallery, Academy, About
    - Gallery: Home, Academy, About
    - Academy: Home, Gallery, About
    - About: Home, Gallery, Academy
    """

    def setUp(self):
        self.client = Client()

    def test_homepage_nav_excludes_home(self):
        response = self.client.get(reverse('ifybeeCC:home'))
        content = response.content.decode('utf-8')
        # Desktop nav checks
        nav_slice = content[content.find('<nav class="nav">'):content.find('</nav>')]
        self.assertNotIn('>Home<', nav_slice)
        self.assertIn('>Gallery<', nav_slice)
        self.assertIn('>Academy<', nav_slice)
        self.assertIn('>About<', nav_slice)

    def test_gallery_nav_excludes_gallery(self):
        response = self.client.get(reverse('ifybeeCC:gallery'))
        content = response.content.decode('utf-8')
        nav_slice = content[content.find('<nav class="nav">'):content.find('</nav>')]
        self.assertIn('>Home<', nav_slice)
        self.assertNotIn('>Gallery<', nav_slice)
        self.assertIn('>Academy<', nav_slice)
        self.assertIn('>About<', nav_slice)

    def test_academy_nav_excludes_academy(self):
        response = self.client.get(reverse('ifybeeCC:academy'))
        content = response.content.decode('utf-8')
        nav_slice = content[content.find('<nav class="nav">'):content.find('</nav>')]
        self.assertIn('>Home<', nav_slice)
        self.assertIn('>Gallery<', nav_slice)
        self.assertNotIn('>Academy<', nav_slice)
        self.assertIn('>About<', nav_slice)

    def test_about_nav_excludes_about(self):
        response = self.client.get(reverse('ifybeeCC:about'))
        content = response.content.decode('utf-8')
        nav_slice = content[content.find('<nav class="nav">'):content.find('</nav>')]
        self.assertIn('>Home<', nav_slice)
        self.assertIn('>Gallery<', nav_slice)
        self.assertIn('>Academy<', nav_slice)
        self.assertNotIn('>About<', nav_slice)


class EmptyDatabaseFallbackTests(TestCase):
    """
    Ensure that even when the database contains zero records,
    all 4 pages render gracefully with default fallbacks and no 500 errors.
    """

    def setUp(self):
        self.client = Client()
        # Verify completely empty tables in test database
        SiteSetting.objects.all().delete()
        HeroSlide.objects.all().delete()
        GalleryItem.objects.all().delete()
        AcademyClass.objects.all().delete()
        ClassMedia.objects.all().delete()
        AcademyCurriculumModule.objects.all().delete()
        AcademyAnnouncement.objects.all().delete()

    def test_empty_database_homepage(self):
        response = self.client.get(reverse('ifybeeCC:home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "A Taste.")
        self.assertContains(response, "Explore Gallery")

    def test_empty_database_gallery(self):
        response = self.client.get(reverse('ifybeeCC:gallery'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Inspiration Gallery")
        self.assertContains(response, "All Media")

    def test_empty_database_academy(self):
        response = self.client.get(reverse('ifybeeCC:academy'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Ifybee's Baking")
        self.assertContains(response, "Cake Baking & Fondant")

    def test_empty_database_about(self):
        response = self.client.get(reverse('ifybeeCC:about'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Built around creativity and care.")


class ModelBehaviorTests(TestCase):
    """Test model methods, string representations, and properties."""

    def test_site_setting_whatsapp_url(self):
        setting = SiteSetting.objects.create(whatsapp_number="2348121402824")
        url = setting.get_whatsapp_url("Hello from test")
        self.assertIn("https://wa.me/2348121402824", url)
        self.assertIn("Hello%20from%20test", url)

    def test_hero_slide_methods(self):
        slide = HeroSlide.objects.create(
            heading="Special Cake",
            subheading="Delight",
            fallback_image_path="IMAGES/cakes/cake image 3.jpg"
        )
        self.assertEqual(str(slide), "Special Cake Delight")
        self.assertTrue(slide.get_image_url().endswith("cake%20image%203.jpg"))

    def test_gallery_item_video_property(self):
        photo_item = GalleryItem.objects.create(
            title="Birthday Cake",
            category="cakes",
            static_image_path="IMAGES/cakes/cake image 3.jpg"
        )
        self.assertFalse(photo_item.is_video)

        video_item = GalleryItem.objects.create(
            title="Baking Demo",
            category="pastries",
            static_video_path="VIDEOS/VID-20260528-WA0023.mp4"
        )
        self.assertTrue(video_item.is_video)
        self.assertTrue(video_item.get_video_url().endswith("VID-20260528-WA0023.mp4"))


class AdminRegistrationTests(TestCase):
    """Ensure all required business models are registered in Django Admin."""

    def test_all_models_registered_in_admin(self):
        registered_models = admin.site._registry
        models_to_check = [
            SiteSetting,
            HeroSlide,
            GalleryItem,
            AcademyClass,
            ClassMedia,
            AcademyCurriculumModule,
            AcademyAnnouncement,
        ]
        for model in models_to_check:
            self.assertIn(model, registered_models, f"{model.__name__} must be registered in Django Admin")


class VideoMediaTests(TestCase):
    # Verify videos render with proper HTML video tags and working sources

    def setUp(self):
        self.client = Client()

    def test_gallery_renders_video_element(self):
        GalleryItem.objects.create(
            title="Turntable Cake Reveal",
            category="cakes",
            static_image_path="IMAGES/cakes/cake image 3.jpg",
            static_video_path="VIDEOS/VID-20261010-WA0055.mp4"
        )
        response = self.client.get(reverse('ifybeeCC:gallery'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "<video controls")
        self.assertContains(response, "VID-20261010-WA0055.mp4")

    def test_academy_renders_video_element(self):
        ClassMedia.objects.create(
            title="Practical Mentorship",
            media_type="video",
            static_image_path="IMAGES/academy/acade.webp",
            static_video_path="VIDEOS/VID_20260926_144544.mp4"
        )
        response = self.client.get(reverse('ifybeeCC:academy'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "<video controls")
        self.assertContains(response, "VID_20260926_144544.mp4")
