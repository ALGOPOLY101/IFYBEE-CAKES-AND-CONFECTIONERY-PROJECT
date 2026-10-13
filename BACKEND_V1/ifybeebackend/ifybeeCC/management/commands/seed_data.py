from django.core.management.base import BaseCommand
from ifybeeCC.models import (
    SiteSetting,
    HeroSlide,
    GalleryItem,
    AcademyClass,
    ClassMedia,
    AcademyCurriculumModule,
    AcademyAnnouncement,
)


class Command(BaseCommand):
    help = "Populate initial data for Ifybee's Cakes & Confectionery website."

    def handle(self, *args, **kwargs):
        self.stdout.write("Seeding database with Ifybee's Cakes & Confectionery initial data...")

        # 1. Site Configuration with real business details
        setting, _ = SiteSetting.objects.update_or_create(
            id=1,
            defaults={
                'site_name': "Ifybee's Cakes & Confectionery",
                'hero_label': "IFYBEE'S CAKES & CONFECTIONERY",
                'whatsapp_number': "2348121402824",
                'phone_display': "+234 812 140 2824",
                'address': "No. 18 Umuodu Ihitte Isi Mbieri, Opposite Mmesoma Building, Mbaitoli LGA, Owerri, Imo State, Nigeria",
                'instagram_url': "https://www.instagram.com/ifybeescakesandevents?dlrf=NmtrNG05b2NtMGFi",
                'tiktok_url': "https://www.tiktok.com/@ifybeescakes001?_r=1&_t=ZS-9AV1gxz7m4N",
                'facebook_url': "https://www.facebook.com/IfybeesCakesAndEvents",
                'welcome_label': "WELCOME TO IFYBEE'S",
                'welcome_title': "Where every creation matters.",
                'welcome_text_1': "At Ifybee's Cakes & Confectionery, we believe food should be more than something you eat. It should become part of the memory.",
                'welcome_text_2': "From beautifully designed celebration cakes to freshly baked pastries and practical baking classes, every creation is made to bring something special to your day.",
                'about_heading': "Built around creativity and care.",
                'about_story_1': "Ifybee's Cakes & Confectionery was born from a deep love for baking, thoughtful artistic detail, and the simple joy of seeing people smile when they taste something made with genuine care.",
                'about_story_2': "What began as a passionate pursuit baking bespoke cakes for family birthdays and close celebrations gradually expanded into a dedicated confectionery brand. Word-of-mouth recommendations from satisfied clients helped Ifybee's grow into a recognized kitchen known for dependable taste and beautiful aesthetics.",
                'about_story_3': "Today, Ifybee's is not only a home for delectable celebration cakes and oven-fresh pastries, but also a nurturing learning hub where eager students master the craft of professional baking.",
                'footer_tagline': "Beautiful cakes, artisanal pastries, and practical baking education. Bringing joy to every celebration.",
            }
        )
        self.stdout.write(self.style.SUCCESS(f"[OK] Updated Site Configuration with real contact details ({setting.whatsapp_number})"))

        # 2. Hero Slides
        slides_data = [
            {
                'heading': "A Taste.",
                'subheading': "A Lifetime Delight.",
                'description': "Beautiful cakes, delicious pastries and unforgettable experiences, crafted with care for every occasion.",
                'fallback_image_path': "IMAGES/cakes/cake image 3.jpg",
                'button_text': "Explore Gallery",
                'button_link': "/gallery/",
                'secondary_button_text': "Baking Academy",
                'secondary_button_link': "/academy/",
                'order': 1,
            },
            {
                'heading': "Oven-Fresh Pastries.",
                'subheading': "Baked To Perfection.",
                'description': "Golden flaky meat pies, gourmet glazed doughnuts, and savory snack boxes prepared fresh daily.",
                'fallback_image_path': "IMAGES/pastries/IMG-20260528-WA0016.jpg",
                'button_text': "Explore Gallery",
                'button_link': "/gallery/",
                'secondary_button_text': "Baking Academy",
                'secondary_button_link': "/academy/",
                'order': 2,
            },
            {
                'heading': "Artisanal Celebrations.",
                'subheading': "Crafted With Passion.",
                'description': "From majestic tiered wedding cakes to bespoke birthday designs, every tier tells your story.",
                'fallback_image_path': "IMAGES/cakes/IMG_20250726_065808.jpg",
                'button_text': "Explore Gallery",
                'button_link': "/gallery/",
                'secondary_button_text': "Baking Academy",
                'secondary_button_link': "/academy/",
                'order': 3,
            },
            {
                'heading': "Gourmet Confectionery.",
                'subheading': "Sweet Moments.",
                'description': "Handcrafted pastries and celebration treats created with the finest natural ingredients.",
                'fallback_image_path': "IMAGES/pastries/IMG-20260527-WA0038(1).jpg",
                'button_text': "Explore Gallery",
                'button_link': "/gallery/",
                'secondary_button_text': "Baking Academy",
                'secondary_button_link': "/academy/",
                'order': 4,
            },
            {
                'heading': "Bespoke Anniversary Cakes.",
                'subheading': "Unforgettable Flavours.",
                'description': "Tailored celebration cakes crafted with intricate fondant designs and handcrafted sugar flowers.",
                'fallback_image_path': "IMAGES/cakes/IMG_20251216_083501.jpg",
                'button_text': "Explore Gallery",
                'button_link': "/gallery/",
                'secondary_button_text': "Baking Academy",
                'secondary_button_link': "/academy/",
                'order': 5,
            },
            {
                'heading': "Artisanal Catering Platters.",
                'subheading': "Crisp & Savory.",
                'description': "Deluxe party snack boxes, freshly rolled meat pies, and gourmet bites for special gatherings.",
                'fallback_image_path': "IMAGES/pastries/IMG-20260528-WA0022.jpg",
                'button_text': "Explore Gallery",
                'button_link': "/gallery/",
                'secondary_button_text': "Baking Academy",
                'secondary_button_link': "/academy/",
                'order': 6,
            },
            {
                'heading': "Luxury Velvet Designs.",
                'subheading': "Modern Elegance.",
                'description': "Contemporary textured celebration cakes designed to be the centerpiece of your special day.",
                'fallback_image_path': "IMAGES/cakes/IMG_20260721_201640.jpg",
                'button_text': "Explore Gallery",
                'button_link': "/gallery/",
                'secondary_button_text': "Baking Academy",
                'secondary_button_link': "/academy/",
                'order': 7,
            },
            {
                'heading': "Signature Golden Meatpies.",
                'subheading': "Flaky Crust Perfection.",
                'description': "Our iconic richly seasoned minced meat and vegetable pies, oven-baked to golden perfection.",
                'fallback_image_path': "IMAGES/pastries/meatpie.webp",
                'button_text': "Explore Gallery",
                'button_link': "/gallery/",
                'secondary_button_text': "Baking Academy",
                'secondary_button_link': "/academy/",
                'order': 8,
            },
        ]
        # Clean up older slide entries to ensure clean 8-slide set
        HeroSlide.objects.exclude(heading__in=[s['heading'] for s in slides_data]).delete()
        for s in slides_data:
            HeroSlide.objects.update_or_create(
                heading=s['heading'],
                defaults=s
            )
        self.stdout.write(self.style.SUCCESS(f"[OK] Configured {len(slides_data)} Hero Slides"))

        # 3. Gallery Items (Cakes, Pastries, Academy, Photos & Local Videos)
        gallery_data = [
            # --- CAKES ---
            {
                'title': "Signature Celebration Cake",
                'category': 'cakes',
                'caption': "Artisanal celebration cake decorated with handmade floral accents and delicate piping.",
                'static_image_path': "IMAGES/cakes/cake image 3.jpg",
                'order': 1,
            },
            {
                'title': "Cake Finishing Touches Demo",
                'category': 'cakes',
                'caption': "Studio demonstration showing turntable finishing, border piping, and delicate decorating.",
                'static_video_path': "VIDEOS/VID-20261010-WA0055.mp4",
                'static_image_path': "IMAGES/cakes/cake image 3.jpg",
                'source_credit': "Ifybee Studio recording.",
                'order': 2,
            },
            {
                'title': "Milestone Celebration Cake",
                'category': 'cakes',
                'caption': "High-tier custom occasion cake crafted with sharp buttercream edges.",
                'static_image_path': "IMAGES/cakes/IMG_20250330_071915.jpg",
                'order': 3,
            },
            {
                'title': "Royal Buttercream Tiered Cake",
                'category': 'cakes',
                'caption': "Regal tiered celebration design for weddings, banquets, and major milestones.",
                'static_image_path': "IMAGES/cakes/IMG_20250726_065808.jpg",
                'order': 4,
            },
            {
                'title': "Grand Wedding Tier Showcase",
                'category': 'cakes',
                'caption': "Video reveal of an exquisite multi-tier celebration masterpiece.",
                'static_video_path': "VIDEOS/VID_20261005_111416.mp4",
                'static_image_path': "IMAGES/cakes/IMG_20261005_111518.jpg",
                'source_credit': "Ifybee Celebration portfolio.",
                'order': 5,
            },
            {
                'title': "Artistic Floral Birthday Cake",
                'category': 'cakes',
                'caption': "Vibrant celebratory cake with handcrafted floral arrangements and gold accents.",
                'static_image_path': "IMAGES/cakes/IMG_20251216_083501.jpg",
                'order': 6,
            },
            {
                'title': "Golden Accent Celebration Cake",
                'category': 'cakes',
                'caption': "Bespoke birthday cake adorned with elegant golden details.",
                'static_image_path': "IMAGES/cakes/IMG_20250420_070917.jpg",
                'order': 7,
            },
            {
                'title': "Luxe Tiered Celebration Cake",
                'category': 'cakes',
                'caption': "Tall celebration tower finished with delicate modern textures.",
                'static_image_path': "IMAGES/cakes/IMG_20260721_201640.jpg",
                'order': 8,
            },
            {
                'title': "Contemporary Drip & Topper Cake",
                'category': 'cakes',
                'caption': "Modern drip styling combined with decorative celebration toppers.",
                'static_image_path': "IMAGES/cakes/IMG_20251026_105754.jpg",
                'order': 9,
            },
            {
                'title': "Deluxe Holiday Tiered Cake",
                'category': 'cakes',
                'caption': "Festive holiday celebration cake baked with rich sponge layers.",
                'static_image_path': "IMAGES/cakes/IMG-20251203-WA0226.jpeg",
                'order': 10,
            },

            # --- PASTRIES ---
            {
                'title': "Golden Flaky Meat Pies",
                'category': 'pastries',
                'caption': "Richly spiced minced meat and vegetable filling encased in buttery, flaky pastry crust.",
                'static_image_path': "IMAGES/pastries/meatpie.webp",
                'order': 11,
            },
            {
                'title': "Fresh Pastry Baking Process",
                'category': 'pastries',
                'caption': "Real kitchen footage of baking oven-fresh pastries to a golden crisp tan.",
                'static_video_path': "VIDEOS/VID-20260528-WA0023.mp4",
                'static_image_path': "IMAGES/pastries/meatpie.webp",
                'source_credit': "Ifybee Kitchen recording.",
                'order': 12,
            },
            {
                'title': "Oven Fresh Meat Pies Batch",
                'category': 'pastries',
                'caption': "Trays of golden meat pies resting on cooling racks straight from the bakery oven.",
                'static_image_path': "IMAGES/pastries/IMG-20260528-WA0016.jpg",
                'order': 13,
            },
            {
                'title': "Glazed Ring Doughnuts",
                'category': 'pastries',
                'caption': "Fluffy yeast-raised doughnuts fried to a golden tan and finished with sweet glaze.",
                'static_image_path': "IMAGES/pastries/donughts.webp",
                'order': 14,
            },
            {
                'title': "Confectionery Craft Demo",
                'category': 'pastries',
                'caption': "Short video demo showing delicate pastry handling and oven readiness.",
                'static_video_path': "VIDEOS/VID-20260602-WA0045.mp4",
                'static_image_path': "IMAGES/pastries/donughts.webp",
                'source_credit': "Ifybee Kitchen recording.",
                'order': 15,
            },
            {
                'title': "Fresh Snack Box Assortment",
                'category': 'pastries',
                'caption': "Assorted confectionery snack pack combination prepared for event catering.",
                'static_image_path': "IMAGES/pastries/IMG-20260527-WA0038(1).jpg",
                'order': 16,
            },
            {
                'title': "Deluxe Pastry Display",
                'category': 'pastries',
                'caption': "Signature pastry craftsmanship ready for orders and special deliveries.",
                'static_image_path': "IMAGES/pastries/IMG-20260720-WA0073.jpg",
                'order': 17,
            },
            {
                'title': "Confectionery Party Tray",
                'category': 'pastries',
                'caption': "Crisp and flavorful bite-sized confectionery treats ideal for celebrations.",
                'static_image_path': "IMAGES/pastries/IMG-20260528-WA0022.jpg",
                'order': 18,
            },

            # --- ACADEMY & TRAINING ---
            {
                'title': "Hands-on Decorating Workshop",
                'category': 'academy',
                'caption': "Students engaged in hands-on fondant draping and cake structure practicals.",
                'static_image_path': "IMAGES/academy/A.webp",
                'order': 19,
            },
            {
                'title': "Academy Studio in Action",
                'category': 'academy',
                'caption': "Watch students master cake leveling, frosting, and styling under mentor guidance.",
                'static_video_path': "VIDEOS/VID_20260926_105441.mp4",
                'static_image_path': "IMAGES/academy/acade.webp",
                'source_credit': "Ifybee Academy classroom recording.",
                'order': 20,
            },
            {
                'title': "Interactive Mentorship Session",
                'category': 'academy',
                'caption': "One-on-one demonstration illustrating precise piping pressure and consistency.",
                'static_video_path': "VIDEOS/VID_20260926_144544.mp4",
                'static_image_path': "IMAGES/academy/acsa.webp",
                'source_credit': "Ifybee Academy classroom recording.",
                'order': 21,
            },
            {
                'title': "Cake Science & Batter Mixing",
                'category': 'academy',
                'caption': "Baking students learning step-by-step recipe blending, leaveners, and temperature control.",
                'static_image_path': "IMAGES/academy/acade.webp",
                'order': 22,
            },
            {
                'title': "Collaborative Fondant Art",
                'category': 'academy',
                'caption': "Group session sharing pastry-making secrets, sugar crafts, and presentation methods.",
                'static_image_path': "IMAGES/academy/acsa.webp",
                'order': 23,
            },
            {
                'title': "Official Masterclass Syllabus",
                'category': 'academy',
                'caption': "Official promotional curriculum and enrollment details for the upcoming masterclass.",
                'static_image_path': "IMAGES/academy/file_000000003fd08246ad0846f3a525e5c6.png",
                'order': 24,
            },
        ]
        for g in gallery_data:
            GalleryItem.objects.update_or_create(
                title=g['title'],
                defaults=g
            )
        self.stdout.write(self.style.SUCCESS(f"[OK] Configured {len(gallery_data)} Gallery Items (Photos & Local Videos)"))

        # 4. Academy Featured Class
        featured_class, _ = AcademyClass.objects.update_or_create(
            title="Cake Baking & Fondant",
            defaults={
                'subtitle': "Masterclass",
                'description': "A comprehensive practical bootcamp for aspiring bakers and enthusiasts. Learn how to bake delicious sponge cakes from scratch, achieve sharp buttercream edges, sculpt fondant decorations, and bake commercial pastries.",
                'date_info': "Next Cohort: 15th – 20th Next Month",
                'schedule_info': "10:00 AM – 3:00 PM Daily",
                'location': "Ifybee Studio, No. 18 Umuodu Ihitte Isi Mbieri, Mbaitoli LGA, Owerri, Imo State",
                'skill_level': "Beginner to Intermediate",
                'materials_note': "Provided in class",
                'certificate_note': "Issued upon completion",
                'status': 'upcoming',
                'is_featured': True,
                'static_image_path': "IMAGES/academy/A.webp",
                'whatsapp_message': "Hello Ifybee's, I would like to register for the upcoming Baking Masterclass.",
                'order': 1,
            }
        )
        self.stdout.write(self.style.SUCCESS("[OK] Configured Academy Featured Class"))

        # 5. Class Media (Moments with Photos and Local Videos)
        media_data = [
            {
                'title': "Hands-on Practice",
                'caption': "Learners measuring ingredients and mastering mixing techniques.",
                'static_image_path': "IMAGES/academy/acade.webp",
                'media_type': 'photo',
                'order': 1,
            },
            {
                'title': "Academy Studio in Action",
                'caption': "Students practicing real-time cake crumb-coating and buttercream smoothing.",
                'static_video_path': "VIDEOS/VID_20260926_105441.mp4",
                'static_image_path': "IMAGES/academy/acade.webp",
                'media_type': 'video',
                'order': 2,
            },
            {
                'title': "Interactive Decorating",
                'caption': "Students practicing precise piping and fondant application.",
                'static_image_path': "IMAGES/academy/acsa.webp",
                'media_type': 'photo',
                'order': 3,
            },
            {
                'title': "One-on-One Practical Mentorship",
                'caption': "Instructor coaching on turntable precision and fondant draping.",
                'static_video_path': "VIDEOS/VID_20260926_144544.mp4",
                'static_image_path': "IMAGES/academy/acsa.webp",
                'media_type': 'video',
                'order': 4,
            },
            {
                'title': "Class Syllabus & Announcements",
                'caption': "Official promotional updates and syllabus overviews for upcoming classes.",
                'static_image_path': "IMAGES/academy/file_000000003fd08246ad0846f3a525e5c6.png",
                'media_type': 'photo',
                'order': 5,
            },
        ]
        for m in media_data:
            ClassMedia.objects.update_or_create(
                title=m['title'],
                defaults={
                    'academy_class': featured_class,
                    **m
                }
            )
        self.stdout.write(self.style.SUCCESS(f"[OK] Configured {len(media_data)} Class Media Moments"))

        # 6. Curriculum Modules
        modules_data = [
            {
                'module_number': "01",
                'title': "Cake Science & Sponges",
                'description': "Master recipes for vanilla sponge, moist chocolate, and velvety red velvet. Understand ingredient functions, leaveners, and oven temperature control.",
                'order': 1,
            },
            {
                'module_number': "02",
                'title': "Buttercream & Sharp Edges",
                'description': "Whip silky American and Swiss meringue buttercreams. Learn leveling, crumb coating, smooth acrylic disk finishes, and textured comb techniques.",
                'order': 2,
            },
            {
                'module_number': "03",
                'title': "Fondant & Sugar Art",
                'description': "Roll, drape, and smooth fondant without tears. Create delicate sugar blossoms, borders, bows, and silicone mold design accents.",
                'order': 3,
            },
            {
                'module_number': "04",
                'title': "Commercial Pastry & Costing",
                'description': "Bake flaky golden meat pies, roll sausage snacks, and fry glazed doughnuts. Learn recipe costing, cake pricing formulas, and bakery management basics.",
                'order': 4,
            },
        ]
        for mod in modules_data:
            AcademyCurriculumModule.objects.update_or_create(
                module_number=mod['module_number'],
                defaults=mod
            )
        self.stdout.write(self.style.SUCCESS(f"[OK] Configured {len(modules_data)} Curriculum Modules"))

        # 7. Announcements
        announcements_data = [
            {
                'badge_text': "Upcoming Schedule",
                'title': "Weekend Intensive Workshop",
                'description': "Designed specifically for busy working professionals and students who cannot attend weekday bootcamps. Covers complete cake baking and frosting over two intensive Saturdays.",
                'whatsapp_query': "Hello Ifybee's, I am interested in the Weekend Intensive Workshop.",
                'is_gold_border': False,
                'order': 1,
            },
            {
                'badge_text': "Private Mentorship",
                'title': "One-on-One Practical Sessions",
                'description': "Want dedicated individual coaching on custom sugar flowers, tiered wedding cake construction, or advanced pastry craft? Personalized private sessions can be scheduled.",
                'whatsapp_query': "Hello Ifybee's, I would like to inquire about One-on-One Private Mentorship.",
                'is_gold_border': True,
                'order': 2,
            },
        ]
        for ann in announcements_data:
            AcademyAnnouncement.objects.update_or_create(
                title=ann['title'],
                defaults=ann
            )
        self.stdout.write(self.style.SUCCESS(f"[OK] Configured {len(announcements_data)} Announcements"))

        self.stdout.write(self.style.SUCCESS("All Ifybee Cakes & Confectionery initial data successfully populated!"))
