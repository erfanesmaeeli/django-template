from django.core.management.base import BaseCommand, no_translations
import requests
import json
from main.models import ReserveData
import datetime
from core.settings import RESERVATION_API_BASE_URL, RESERVATION_API_KEY


class Command(BaseCommand):

    @no_translations
    def handle(self, *args, **options):
        url = RESERVATION_API_BASE_URL + '/api/occ'
        
        headers = {
        'Content-Type': 'application/json',
        'apiKey': RESERVATION_API_KEY
        }

        data = {
            "startDate": "2023/03/6",
            "endDate": "2023/03/10", 
            "guestNum":2,
            "iata": "1245", 
            "mpeHotel": 1
        }

        response = requests.post(url, headers=headers, json=data)