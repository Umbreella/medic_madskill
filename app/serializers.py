from rest_framework import serializers
from drf_extra_fields.fields import Base64ImageField, Base64FileField

from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = (
            'email', 'password',
        )


class NewSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='analysis.name')
    description = serializers.CharField(source='analysis.description')
    price = serializers.DecimalField(source='analysis.price',
                                     max_digits=10, decimal_places=2)

    class Meta:
        model = New
        fields = (
            'id', 'name', 'description', 'price', 'image',
        )


class AnalysisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Analysis
        fields = (
            'id', 'category', 'name', 'description', 'price', 'time_result',
            'preparation', 'bio',
        )


class PatientSerializer(serializers.ModelSerializer):
    image = Base64ImageField(required=False)

    class Meta:
        model = Patient
        fields = (
            'id', 'first_name', 'last_name', 'middle_name', 'date_of_birth',
            'pol', 'image',
        )

    def create(self, validated_data):
        return Patient.objects.create(**{
            **validated_data,
            **self.context,
        })


class AnalysisInPatientSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='analysis.name', read_only=True)
    price = serializers.DecimalField(source='analysis.price',
                                     max_digits=10, decimal_places=2,
                                     read_only=True)

    class Meta:
        model = AnalysisInPatient
        fields = (
            'analysis', 'name', 'price',
        )


class PatientInOrderSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source='patient.first_name',
                                       read_only=True)
    last_name = serializers.CharField(source='patient.last_name',
                                      read_only=True)
    middle_name = serializers.CharField(source='patient.middle_name',
                                        read_only=True)
    image = serializers.ImageField(source='patient.image', read_only=True)
    analysises = AnalysisInPatientSerializer(many=True)

    class Meta:
        model = PatientInOrder
        fields = (
            'patient', 'first_name', 'last_name', 'middle_name', 'image',
            'analysises',
        )


class OrderSerializer(serializers.ModelSerializer):
    patients = PatientInOrderSerializer(many=True)
    audio_comment = Base64FileField(required=False)

    class Meta:
        model = Order
        fields = (
            'id', 'address', 'date_time', 'phone', 'comment', 'patients',
        )

    def create(self, validated_data):
        patients = validated_data.pop('patients')

        order = Order.objects.create(**{
            **validated_data,
            **self.context,
        })

        for patient in patients:
            analysises = patient.pop('analysises')

            patient_in_order = PatientInOrder.objects.create(**{
                **patient,
                'order': order,
            })

            for analysis in analysises:
                AnalysisInPatient.objects.create(**{
                    **analysis,
                    'patient_in_order': patient_in_order,
                })

        return order
