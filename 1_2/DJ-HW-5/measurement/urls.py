from django.urls import path

from measurement.views import CreateSensorView, SensorChange, MeasurmentCreate, MeasurementAddSerializer

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', CreateSensorView.as_view()),
    path('sensors/<pk>/', SensorChange.as_view()),
    path('measurements/', MeasurmentCreate.as_view()),
]

