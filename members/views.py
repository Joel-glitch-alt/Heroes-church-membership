from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from .models import Member
from .serializers import MemberSerializer


def frontend(request):
    return render(request, 'members/index.html')


class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        return  # skip CSRF check


@method_decorator(csrf_exempt, name='dispatch')
class MemberListCreateView(APIView):
    """
    GET  /api/members/   — list all members (newest first)
    POST /api/members/   — register a new member
    """
    authentication_classes = [CsrfExemptSessionAuthentication]

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


@method_decorator(csrf_exempt, name='dispatch')
class MemberDetailView(APIView):
    """
    GET    /api/members/<id>/  — retrieve a single member
    PUT    /api/members/<id>/  — update a member
    DELETE /api/members/<id>/  — remove a member
    """
    authentication_classes = [CsrfExemptSessionAuthentication]

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
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        member = self.get_object(pk)
        member.delete()
        return Response(
            {'message': 'Member deleted successfully.'},
            status=status.HTTP_204_NO_CONTENT,
        )
