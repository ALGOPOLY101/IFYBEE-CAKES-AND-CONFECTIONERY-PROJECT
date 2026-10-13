from .models import SiteSetting


def site_settings(request):
    """
    Makes site configuration, contact information, and business details
    available across all templates.
    """
    setting = SiteSetting.objects.first()
    if not setting:
        # Fallback in-memory object if no row exists yet
        setting = SiteSetting(
            site_name="Ifybee's Cakes & Confectionery",
            hero_label="IFYBEE'S CAKES & CONFECTIONERY",
            whatsapp_number="2348121402824",
            phone_display="+234 812 140 2824",
            address="No. 18 Umuodu Ihitte Isi Mbieri, Opposite Mmesoma Building, Mbaitoli LGA, Owerri, Imo State, Nigeria",
            instagram_url="https://www.instagram.com/ifybeescakesandevents?dlrf=NmtrNG05b2NtMGFi",
            tiktok_url="https://www.tiktok.com/@ifybeescakes001?_r=1&_t=ZS-9AV1gxz7m4N",
            facebook_url="https://www.facebook.com/IfybeesCakesAndEvents",
            welcome_label="WELCOME TO IFYBEE'S",
            welcome_title="Where every creation matters.",
            welcome_text_1="At Ifybee's Cakes & Confectionery, we believe food should be more than something you eat. It should become part of the memory.",
            welcome_text_2="From beautifully designed celebration cakes to freshly baked pastries and practical baking classes, every creation is made to bring something special to your day.",
            about_heading="Built around creativity and care.",
            about_story_1="Ifybee's Cakes & Confectionery was born from a deep love for baking, thoughtful artistic detail, and the simple joy of seeing people smile when they taste something made with genuine care.",
            about_story_2="What began as a passionate pursuit baking bespoke cakes for family birthdays and close celebrations gradually expanded into a dedicated confectionery brand. Word-of-mouth recommendations from satisfied clients helped Ifybee's grow into a recognized kitchen known for dependable taste and beautiful aesthetics.",
            about_story_3="Today, Ifybee's is not only a home for delectable celebration cakes and oven-fresh pastries, but also a nurturing learning hub where eager students master the craft of professional baking.",
            footer_tagline="Beautiful cakes, artisanal pastries, and practical baking education. Bringing joy to every celebration.",
        )
    return {
        'site_setting': setting,
    }

