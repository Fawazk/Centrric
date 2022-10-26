from ast import Delete
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from . serializers import UserSerializer, UserFollowSerializer,UserDetailsSerializer
from .models import Account, UserFollow


class Register(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.validated_data)
        else:
            return Response(serializer.errors)

# To follow
class UserFollowViews(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserFollowSerializer
    queryset = UserFollow.objects.all()

    def post(self, request):
        if request.GET.get('followid'):
            data = {}
            follow = request.GET.get('followid')
            data = {
                'user_id': request.user.id,
                'following_user_id': follow,
            }
            serializer = self.get_serializer(data=data)
            serializer.is_valid(raise_exception=True)
            c = serializer.save()
            return Response({
                "cource": UserFollowSerializer(c, context=self.get_serializer_context()).data,
                'message': 'Follow successfully'
            })
        else:
            return Response({
                'error':'follow id is required'
            })

# To get current user details and any other user details
class userDetails(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        if request.GET.get('uid'):
            uid = request.GET.get('uid')
            details = Account.objects.filter(id=uid)
        else:
            details=Account.objects.filter(id=request.user.id)
            print(details)
        serializer = UserDetailsSerializer(details,many=True)
        return Response({'details':serializer.data})



# To get all the following related to user
class Getfollowing(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        user = request.user
        following= user.following.all()
        serializer = UserFollowSerializer(following,many=True)
        return Response({'following':serializer.data})

# To get all the followers related to user
class GetFollowers(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        user = request.user
        followers = user.followers.all()
        serializer = UserFollowSerializer(followers,many=True)
        return Response({'followers':serializer.data})

# to unfollow 
class UnFollow(APIView):
    permission_classes = [IsAuthenticated]
    def delete(self, request,uid):
        user = request.user
        follow = UserFollow.objects.get(user_id=user.id,following_user_id=uid)
        follow.delete()
        return Response({'message':'Unfollowed Successfully'})