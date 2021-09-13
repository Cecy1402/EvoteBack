from rest_framework import routers
from .views import *

router = routers.SimpleRouter()
#router.register('Candidates', CandidatesViewSet)
router.register('ListInfo', ListInfoViewSet)
router.register('Parameter', ParameterViewSet)
router.register('Period', PeriodViewSet)
router.register('Students', VoteStudentViewSet)
router.register('voteInfo', VoteInfoViewSet)


urlpatterns = router.urls