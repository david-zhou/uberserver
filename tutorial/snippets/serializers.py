from django.forms import widgets
from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES, User, Credit_Card, Driver, Pending_Ride, User_Ride

'''
class SnippetSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    code = serializers.CharField(style={'base_template': 'textarea.html'})
    linenos = serializers.BooleanField(required=False)
    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
    style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance
'''	
		
class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style')
        
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'name', 'last_name','password','phone','country','home','home_lat','home_long','work','work_lat','work_long')

class CreditCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Credit_Card
        fields = ('credit_card_number','email','mm','yy','cvv','postal_code','mail')
        
class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ('driver_id','name','last_name','vehicle','available','pos_lat','pos_long','gcm_id', 'license_plate')
        
class PendingRideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pending_Ride
        fields = ('pending_ride_id','user_id','user_lat','user_lon', 'user_destination_lat', 'user_destination_lon')
        
class UserRideSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Ride
        fields = ('ride_id', 'user_id', 'driver_id', 'credit_card_number', 'date', 'initial_pos', 'initial_lat', 'initial_long', 'final_pos', 'final_lat', 'final_long', 'distance', 'time', 'fee', 'final_fee', 'user_rating', 'driver_rating', 'pending_ride_id')