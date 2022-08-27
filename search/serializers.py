from asyncore import read
from rest_framework import serializers

from search.models import Unit, Variable, Sector, SatModel

class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = ('id', 'unit')

class SectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sector
        fields = ('id', 'sector')

class VariableSerializer(serializers.ModelSerializer):

    sector = serializers.SlugRelatedField(slug_field="sector", queryset=Sector.objects.all())
    unit = serializers.SlugRelatedField(slug_field="unit", queryset=Unit.objects.all())

    class Meta:
        model = Variable
        fields = ('id', 'shortname', 'longname', 'description', 'sector', 'unit')


# class SatModelSerializer(serializers.ModelSerializer):

#     variable = serializers.SlugRelatedField(slug_field="shortname", queryset=Variable.objects.all())
    
#     class Meta:
#         model = SatModel
#         fields = ('id', 'satellite_or_model_long', 'satellite_or_model_short', 'sensor', 'product', 'variable', 'start_date', 'end_date', 'reference')

class WriteSatModelSerializer(serializers.ModelSerializer):

    variable = serializers.SlugRelatedField(slug_field="shortname", queryset=Variable.objects.all())
    
    class Meta:
        model = SatModel
        fields = ('satellite_or_model_long', 'satellite_or_model_short', 'sensor', 'product', 'variable', 'start_date', 'end_date', 'reference')

class ReadSatModelSerializer(serializers.ModelSerializer):

    variable = VariableSerializer()
    
    class Meta:
        model = SatModel
        fields = ('id', 'satellite_or_model_long', 'satellite_or_model_short', 'sensor', 'product', 'variable', 'start_date', 'end_date', 'reference')

        read_only_fields = fields