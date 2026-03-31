from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from .models import Member
from .serializers import MemberSerializer

from django.shortcuts import render



def frontend(request):
       return render(request, 'members/index.html')

@method_decorator(csrf_exempt, name='dispatch')
class MemberListCreateView(APIView):





 class MemberListCreateView(APIView):
    """
    GET  /api/members/   — list all members (newest first)
    POST /api/members/   — register a new member
    """

    def get(self, request):
        members = Member.objects.select_related('invited_by').all()
        serializer = MemberSerializer(members, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = MemberSerializer(data=request.data)
        if serializer.is_valid():
            member = serializer.save()
            return Response(
                MemberSerializer(member).data,
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MemberDetailView(APIView):

    def get_object(self, pk):
        return get_object_or_404(Member, pk=pk)

    def get(self, request, pk):
        member = self.get_object(pk)
        serializer = MemberSerializer(member)
        return Response(serializer.data)

    def put(self, request, pk):
        member = self.get_object(pk)
        serializer = MemberSerializer(member, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        member = self.get_object(pk)
        member.delete()
        return Response(status=204)
    
    