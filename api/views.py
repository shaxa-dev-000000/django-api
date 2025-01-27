from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Passport

def get_passport(request, passport_id):
    try:
        # Modeldan pasport ma'lumotlarini olish
        passport = Passport.objects.get(passport_id=passport_id)
        
        # Ma'lumotni JSON formatiga aylantirish va qaytarish
        return JsonResponse({
            "name": passport.name,
            "surname": passport.surname,
            "phone_number": passport.phone_number,
            "birth_day": passport.birth_day,
            "passport_id": passport.passport_id,
            "address": passport.address
        })
    except Passport.DoesNotExist:
        # Agar pasport topilmasa, xatolik xabarini qaytarish
        return JsonResponse({"error": "Passport not found"}, status=404)
