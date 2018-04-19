from django.core import serializers
from django.http import HttpResponse


def export_as_json(modeladmin, request, queryset):
    response = HttpResponse(content_type="application/json")
    model_name = modeladmin.model._meta.model_name
    response["Content-Disposition"] = "attachment;filename={model_name}.json".format(model_name=model_name)
    serializers.serialize("json", queryset, stream=response, indent=2, use_natural_primary_keys=True)
    return response
