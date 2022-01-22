from rest_framework import serializers



class SubmitGearSerializer(serializers.Serializer):
    name = serializers.CharField(required=True, allow_null=False, allow_blank=False, max_length=128)
    description1 = serializers.CharField(required=True, allow_null=True, allow_blank=True, max_length=256)
    description2 = serializers.CharField(required=True, allow_null=True, allow_blank=True, max_length=256)
    description3 = serializers.CharField(required=True, allow_null=True, allow_blank=True, max_length=256)
    description4 = serializers.CharField(required=True, allow_null=True, allow_blank=True, max_length=256)
    description5 = serializers.CharField(required=True, allow_null=True, allow_blank=True, max_length=256)
    description6 = serializers.CharField(required=True, allow_null=True, allow_blank=True, max_length=256)
    description7 = serializers.CharField(required=True, allow_null=True, allow_blank=True, max_length=256)
    description8 = serializers.CharField(required=True, allow_null=True, allow_blank=True, max_length=256)
    description9 = serializers.CharField(required=True, allow_null=True, allow_blank=True, max_length=256)
    description10 = serializers.CharField(required=True, allow_null=True, allow_blank=True, max_length=256)
    category_id = serializers.IntegerField(required=True, allow_null=False)


class DeleteGearSerializer(serializers.Serializer):
    gear_id = serializers.IntegerField(required=True, allow_null=False)
