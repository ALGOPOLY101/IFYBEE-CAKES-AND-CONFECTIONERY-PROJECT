from django.shortcuts import render
from .models import (
    HeroSlide,
    GalleryItem,
    AcademyClass,
    ClassMedia,
    AcademyCurriculumModule,
    AcademyAnnouncement,
    SiteSetting,
)


def home_view(request):
    # Homepage view with slides, featured items, and academy spotlight
    slides = HeroSlide.objects.filter(is_active=True).order_by('order', 'id')
    
    # 3 distinct featured products: Cakes, Small Chops, and Fresh Pastries
    product_paths = [
        'IMAGES/cakes/IMG_20250924_105701.jpg',
        'IMAGES/pastries/IMG-20260528-WA0018.jpg',
        'IMAGES/pastries/meatpie.webp',
    ]
    featured_products = [
        item for p in product_paths
        if (item := GalleryItem.objects.filter(is_active=True, static_image_path=p).first())
    ] or list(GalleryItem.objects.filter(is_active=True).exclude(category='academy')[:3])

    # 8 distinct gallery preview items across cakes, pastries, and academy
    preview_paths = [
        'IMAGES/cakes/IMG_20261010_130340.jpg',
        'IMAGES/cakes/IMG_20260801_111223.jpg',
        'IMAGES/pastries/IMG-20260528-WA0016.jpg',
        'IMAGES/pastries/IMG-20260527-WA0038(1).jpg',
        'IMAGES/cakes/IMG_20251215_114912.jpg',
        'IMAGES/pastries/IMG-20260720-WA0073.jpg',
        'IMAGES/cakes/IMG_20260926_233223.jpg',
        'IMAGES/academy/acsa.webp',
    ]
    gallery_preview = [
        item for p in preview_paths
        if (item := GalleryItem.objects.filter(is_active=True, static_image_path=p).first())
    ] or list(GalleryItem.objects.filter(is_active=True)[:8])

    featured_class = (
        AcademyClass.objects.filter(is_active=True, is_featured=True).first()
        or AcademyClass.objects.filter(is_active=True).first()
    )

    context = {
        'active_page': 'home',
        'slides': slides,
        'featured_products': featured_products,
        'gallery_preview': gallery_preview,
        'featured_class': featured_class,
    }
    return render(request, 'ifybeeCC/index.html', context)


def gallery_view(request):
    # Gallery view with all active items
    items = GalleryItem.objects.filter(is_active=True).order_by('order', '-date_added')

    context = {
        'active_page': 'gallery',
        'items': items,
    }
    return render(request, 'ifybeeCC/gallery.html', context)


def academy_view(request):
    # Academy view with workshop details and media
    current_class = (
        AcademyClass.objects.filter(is_active=True, is_featured=True).first()
        or AcademyClass.objects.filter(is_active=True, status='upcoming').first()
        or AcademyClass.objects.filter(is_active=True).first()
    )
    
    curriculum_modules = AcademyCurriculumModule.objects.filter(is_active=True).order_by('order', 'id')
    class_media = ClassMedia.objects.filter(is_active=True).order_by('order', 'id')
    announcements = AcademyAnnouncement.objects.filter(is_active=True).order_by('order', 'id')

    context = {
        'active_page': 'academy',
        'current_class': current_class,
        'curriculum_modules': curriculum_modules,
        'class_media': class_media,
        'announcements': announcements,
    }
    return render(request, 'ifybeeCC/academy.html', context)


def about_view(request):
    # About page view
    context = {
        'active_page': 'about',
    }
    return render(request, 'ifybeeCC/about.html', context)
