from rest_framework import serializers
from .models import Member


class MemberSerializer(serializers.ModelSerializer):
    invited_by_name = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model  = Member
        fields = [
            'id',
            'first_name',
            'last_name',
            'contact',
            'invited_by',
            'invited_by_name',
            'location',
            'date_joined',
            'created_at',
        ]
        read_only_fields = ['id', 'created_at', 'invited_by_name']

    def get_invited_by_name(self, obj):
        if obj.invited_by:
            return obj.invited_by.full_name
        return None
    
        # FIRST NAME VALIDATION
    def validate_first_name(self, value):
        if not value.strip():
            raise serializers.ValidationError('First name cannot be blank.')
        return value.strip().title()
     

     # LAST NAME VALIDATION
    def validate_last_name(self, value):
        if not value.strip():
            raise serializers.ValidationError('Last name cannot be blank.')
        return value.strip().title()


       # LOCATION VALIDATION
    def validate_location(self, value):
        if not value.strip():
            raise serializers.ValidationError('Location cannot be blank.')
        return value.strip()
    

    # INVITED BY VALIDATION
    def validate_invited_by(self, value):
        return value or None

    # CONTACT VALIDATION
    def validate_contact(self, value):
        value = value.strip().replace(" ", "").replace("+", "")

        if value.startswith("0"):
            value = "233" + value[1:]

        if not value.isdigit():
            raise serializers.ValidationError('Contact must contain only numbers.')

        if len(value) < 10:
            raise serializers.ValidationError('Contact must be valid.')

        return value