from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from .models import Movie, Seat, Booking
from .serializers import MovieSerializer, SeatSerializer, BookingSerializer

# 🎬 API ViewSets (unchanged)
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=['post'])
    def book_seat(self, request, pk=None):
        seat = get_object_or_404(Seat, pk=pk)
        if seat.is_booked:
            return Response({"error": "Seat is already booked."}, status=400)

        movie_id = request.data.get('movie_id')
        if not movie_id:
            return Response({"error": "Movie ID is required."}, status=400)

        movie = get_object_or_404(Movie, id=movie_id)
        booking = Booking.objects.create(user=request.user, movie=movie, seat=seat)
        seat.is_booked = True
        seat.save()

        return Response({"message": "Seat booked successfully!", "booking_id": booking.id})


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)

    @action(detail=False, methods=['get'])
    def my_bookings(self, request):
        bookings = self.get_queryset()
        serializer = self.get_serializer(bookings, many=True)
        return Response(serializer.data)


# 🖥️ Template-based views for HTML pages
def movie_list_view(request):
    return render(request, "movie_list.html")


def seat_booking_view(request):
    return render(request, "seat_booking.html")


def booking_history_view(request):
    return render(request, "booking_history.html")
