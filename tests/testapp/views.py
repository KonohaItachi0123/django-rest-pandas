from rest_pandas import (
    PandasSimpleView, PandasView, PandasViewSet,
    PandasUnstackedSerializer, PandasScatterSerializer, PandasBoxplotSerializer
)
from .models import TimeSeries, MultiTimeSeries, ComplexTimeSeries
from .serializers import (
    TimeSeriesSerializer, MultiTimeSeriesSerializer,
    ComplexTimeSeriesSerializer, ComplexScatterSerializer,
    ComplexBoxplotSerializer,
)


class NoModelView(PandasSimpleView):
    def get_data(self, request, *args, **kwargs):
        return [
            {'x': 5, 'y': 7},
            {'x': 3, 'y': 2},
            {'x': 8, 'y': 6},
            {'x': 5, 'y': 4},
        ]


class TimeSeriesView(PandasView):
    queryset = TimeSeries.objects.all()
    serializer_class = TimeSeriesSerializer

    def transform_dataframe(self, df):
        df['date'] = df['date'].astype('datetime64[D]')
        return df


class TimeSeriesViewSet(PandasViewSet):
    queryset = TimeSeries.objects.all()
    serializer_class = TimeSeriesSerializer


class MultiTimeSeriesView(PandasView):
    queryset = MultiTimeSeries.objects.all()
    serializer_class = MultiTimeSeriesSerializer
    pandas_serializer_class = PandasUnstackedSerializer


class MultiScatterView(PandasView):
    queryset = MultiTimeSeries.objects.all()
    serializer_class = MultiTimeSeriesSerializer
    pandas_serializer_class = PandasScatterSerializer


class MultiBoxplotView(PandasView):
    queryset = MultiTimeSeries.objects.all()
    serializer_class = MultiTimeSeriesSerializer
    pandas_serializer_class = PandasBoxplotSerializer


class ComplexTimeSeriesView(PandasView):
    queryset = ComplexTimeSeries.objects.all()
    serializer_class = ComplexTimeSeriesSerializer
    pandas_serializer_class = PandasUnstackedSerializer


class ComplexScatterView(PandasView):
    queryset = ComplexTimeSeries.objects.all()
    serializer_class = ComplexScatterSerializer
    pandas_serializer_class = PandasScatterSerializer


class ComplexBoxplotView(PandasView):
    queryset = ComplexTimeSeries.objects.all()
    serializer_class = ComplexBoxplotSerializer
    pandas_serializer_class = PandasBoxplotSerializer
