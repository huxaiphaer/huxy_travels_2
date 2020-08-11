from .serializers import AvailableDatesSerializer, TourPackageSerializer


class FilterAvailableDateSerializer(AvailableDatesSerializer):
    tour_package = TourPackageSerializer()
