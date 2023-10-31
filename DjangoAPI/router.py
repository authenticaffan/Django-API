from API.viewsets import DetailsViewset
from rest_framework import routers

router=routers.DefaultRouter()
router.register('info',DetailsViewset)