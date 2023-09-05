from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_yaml.renderers import YAMLRenderer
from rest_framework_xml.renderers import XMLRenderer

class YAMLView(APIView):
    renderer_classes = [YAMLRenderer]

    def get(self, request):
        data = {'message': 'This response is in YAML format!'}
        return Response(data)

class XMLView(APIView):
    renderer_classes = [XMLRenderer]

    def get(self, request):
        data = {'message': 'This response is in XML format!'}
        return Response(data)

class JSONView(APIView):

    def get(self, request):
        data = {'message': 'This response is in JSON format!'}
        return Response(data)