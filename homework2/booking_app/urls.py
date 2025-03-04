from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, SeatViewSet, BookingViewSet, movie_list_view, seat_booking_view, booking_history_view
from django.conf import settings
from django.conf.urls.static import static


# DRF API Router
router = DefaultRouter()
router.register(r'movies', MovieViewSet, basename='movie')
router.register(r'seats', SeatViewSet, basename='seat')
router.register(r'bookings', BookingViewSet, basename='booking')

# URL Patterns for API and HTML templates
urlpatterns = [
    path('api/', include(router.urls)),  # ✅ DRF API Endpoints
    path('/home/student/cs4300/homework2', movie_list_view, name='movie_list'),  # ✅ Serves movie_list.html
    path('/home/student/cs4300/homework2/book-seat/', seat_booking_view, name='seat_booking'),  # ✅ Serves seat_booking.html
    path('/home/student/cs4300/homework2/booking-history/', booking_history_view, name='booking_history'),  # ✅ Serves booking_history.html


    path('accounts/', include('django.contrib.auth.urls')),  # Includes login, logout, password reset, etc.

]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)  
