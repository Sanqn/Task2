import pandas

from django.core.files.storage import FileSystemStorage

from rest_framework import viewsets
from rest_framework.response import Response
import os

from .serializers import WbDataSerializer, WbDataFileSerializer

from .models import WbData, WbDataFile
from .parser import tr


class WbDataViews(viewsets.ModelViewSet):
    queryset = WbDataFile.objects.all()
    serializer_class = WbDataFileSerializer

    # file extension check
    def check_name(self, name):
        name = str(name)
        if name.endswith('.xlsx'):
            return True
        else:
            return False

    # If no data in db, save
    def save_db(self, url):
        serializer = WbDataSerializer(data=url)
        serializer.is_valid()
        serializer.save()

    def create(self, request):
        article = request.data['article']

        if article:
            list_link = [f'https://www.wildberries.ru/catalog/{article}/detail.aspx']
            list_json = tr(list_link)
            for i in list_json:
                article_in_db = WbData.objects.filter(article=i['article'])
                if not article_in_db:
                    self.save_db(i)
            return Response({'data': list_json})

        else:
            up_file = request.FILES['file']
            name_file = self.check_name(up_file)
            if not name_file:
                return Response({'error': 'Ошибка: неверное расширение файла. Ожидалось .xlsx'})
            else:
                fs = FileSystemStorage()
                # Save file in folder
                filename = fs.save(up_file.name, up_file)
                fs.url(filename)
                # Take file and open
                excel_data_df = pandas.read_excel(f'media/{up_file}')
                list_articles = list(excel_data_df['articles'])
                list_links = []
                for i in list_articles:
                    list_links.append(f'https://www.wildberries.ru/catalog/{i}/detail.aspx')
                # Delete file
                os.remove(f'media/{up_file}')
                list_jsons = tr(list_links)
                for i in list_jsons:
                    article_in_db = WbData.objects.filter(article=i['article'])
                    if not article_in_db:
                        self.save_db(i)
                return Response({'data': list_jsons})
