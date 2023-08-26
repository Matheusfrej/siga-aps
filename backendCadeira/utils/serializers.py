from entidades import Cadeira, OfertaCadeira

class BaseSerializer:
    def __init__(self, content, many=False) -> None:
        self.content = content
        self.many = many

    def _to_representation(self, instance):
        data = dict()
        for field in self.Meta.fields:
            if hasattr(instance, field):
                data[field] = getattr(instance, field)

        if hasattr(self.Meta, 'sub_serializers'):
            for field, sub_serializer in self.Meta.sub_serializers.items():
                try:
                    if hasattr(instance, field):
                        data[field] = sub_serializer(getattr(instance, field)).get_data()
                except:
                    pass

        if hasattr(self.Meta, 'many_sub_serializers'):
            for field, sub_serializer in self.Meta.many_sub_serializers.items():
                try:
                    if hasattr(instance, field):
                        data[field] = sub_serializer(getattr(instance, field), many=True).get_data()
                except:
                    pass

        return data

    def get_data(self):
        if self.many == True:
            obj_list = []
            for instance in self.content:
                obj_list.append(self._to_representation(instance))
            return obj_list
        else:
            return self._to_representation(self.content)

class CadeiraSimpleSerializer(BaseSerializer):
    class Meta:
        model = Cadeira
        fields = (
            'id',
            'nome',
            'ementa',
        )

class CadeiraSerializer(BaseSerializer):
    class Meta:
        model = Cadeira
        fields = (
            'id',
            'nome',
            'ementa',
        )
        many_sub_serializers = {
            'prerequisitos': CadeiraSimpleSerializer,
            'corequisitos': CadeiraSimpleSerializer,
            'equivalencias': CadeiraSimpleSerializer
        }


class OfertaCadeiraSerializer(BaseSerializer):
    class Meta:
        medel = OfertaCadeira
        fields = (
            'id',
            'ementa',
            'horario',
            'plano_ensino',
            'centro_universitario',
            'periodo',
            'professor_id'
        )
        sub_serializers = {
            'cadeira': CadeiraSerializer,
        }