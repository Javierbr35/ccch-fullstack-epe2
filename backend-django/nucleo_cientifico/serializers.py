from rest_framework import serializers

from .models import ProyectoInvestigacion


class ProyectoSerializer(serializers.ModelSerializer):
    area_display = serializers.CharField(
        source="get_area_cientifica_display",
        read_only=True,
    )

    estado_display = serializers.CharField(
        source="get_estado_display",
        read_only=True,
    )

    investigador_principal_nombre = serializers.CharField(
        source="investigador_principal.nombre_completo",
        read_only=True,
    )

    class Meta:
        model = ProyectoInvestigacion
        fields = [
            "id",
            "codigo",
            "titulo",
            "area_cientifica",
            "area_display",
            "resumen",
            "investigador_principal",
            "investigador_principal_nombre",
            "estado",
            "estado_display",
            "presupuesto_clp",
            "fecha_inicio",
            "fecha_termino",
        ]

    def validate_codigo(self, value):
        value = value.strip().upper()

        if not value:
            raise serializers.ValidationError(
                "El código del proyecto es obligatorio."
            )

        return value

    def validate_titulo(self, value):
        value = value.strip()

        if len(value) < 5:
            raise serializers.ValidationError(
                "El título debe tener al menos 5 caracteres."
            )

        return value

    def validate_resumen(self, value):
        value = value.strip()

        if len(value) < 20:
            raise serializers.ValidationError(
                "El resumen debe tener al menos 20 caracteres."
            )

        return value

    def validate_presupuesto_clp(self, value):
        if value < 0:
            raise serializers.ValidationError(
                "El presupuesto no puede ser negativo."
            )

        return value

    def validate(self, attrs):
        fecha_inicio = attrs.get(
            "fecha_inicio",
            getattr(self.instance, "fecha_inicio", None),
        )

        fecha_termino = attrs.get(
            "fecha_termino",
            getattr(self.instance, "fecha_termino", None),
        )

        if fecha_inicio and fecha_termino:
            if fecha_termino < fecha_inicio:
                raise serializers.ValidationError(
                    {
                        "fecha_termino": (
                            "La fecha de término no puede ser anterior "
                            "a la fecha de inicio."
                        )
                    }
                )

        return attrs