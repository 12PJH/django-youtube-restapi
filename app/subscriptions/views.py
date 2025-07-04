from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Subscription
from .serializers import SubscriptionSerializer
from rest_framework.exceptions import ValidationError
from django.db.models import Q
from users.models import User


class SubscriptionList(APIView):
    def post(self, request):
        subscriber = request.user # 구독을 요청하는 자
        subscribed_to_id = request.data.get('subscribed_to')

        data = {'subscriber':subscriber.id, 'subscribed_to' : subscribed_to_id}

        serializer = SubscriptionSerializer(data=data)

        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except ValidationError as e:
            return Response(e.detail, status=status.HTTP_400_BAD_REQUEST)


class SubscriptionDetail(APIView):
    def delete(self, request, pk):
        subscriber = request.user
        subscription = get_object_or_404(
            Subscription,
            subscriber=subscriber,
            subscribed_to=pk
        )
        subscription.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)