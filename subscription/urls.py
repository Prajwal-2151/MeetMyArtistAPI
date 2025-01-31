from django.urls import path

from subscription.views import SubscriptionAPI, CreateRazorpayOrder, VerifyRazorpayPayment

# router=routers.DefaultRouter()
# router.register('',subscriptionAPI)

urlpatterns = [
          # path('',include(router.urls)),
          path('allSubscriptions/', SubscriptionAPI.as_view({'get': 'list'})),
          path('userSubscriptions/', SubscriptionAPI.as_view({'get': 'user_subscriptions'})),
          path('organizerSubscriptions/', SubscriptionAPI.as_view({'get': 'organizer_subscriptions'})),
          path('artistSubscription/', SubscriptionAPI.as_view({'get': 'artist_subscriptions'})),
          path('subscriptionDetails/<int:pk>', SubscriptionAPI.as_view({'get': 'retrieve'})),
          path('createSubscription/', SubscriptionAPI.as_view({'post': 'create'})),
          path('updateSubscription/<int:pk>/', SubscriptionAPI.as_view({'put': 'update'})),
          path('partialupdateSubscription/<int:pk>/', SubscriptionAPI.as_view({'patch': 'partial_update'})),
          path('deleteSubscription/<int:pk>', SubscriptionAPI.as_view({'delete': 'destroy'})),

          path('createOrder/<int:subscription_id>/', CreateRazorpayOrder.as_view(), name='create_razorpay_order'),
          path('verifyPayment/', VerifyRazorpayPayment.as_view(), name='verify_payment'),

]
