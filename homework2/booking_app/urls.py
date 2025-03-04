from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, SeatViewSet, BookingViewSet, movie_list_view, seat_booking_view, booking_history_view

# DRF API Router
router = DefaultRouter()
router.register(r'movies', MovieViewSet, basename='movie')
router.register(r'seats', SeatViewSet, basename='seat')
router.register(r'bookings', BookingViewSet, basename='booking')

# URL Patterns for API and HTML templates
urlpatterns = [
    path('api/', include(router.urls)),  # ✅ DRF API Endpoints
    path('', movie_list_view, name='movie_list'),  # ✅ Serves movie_list.html
    path('book-seat/', seat_booking_view, name='seat_booking'),  # ✅ Serves seat_booking.html
    path('booking-history/', booking_history_view, name='booking_history'),  # ✅ Serves booking_history.html
]
