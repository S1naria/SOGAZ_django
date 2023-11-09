from django.shortcuts import render
from .models import Data
from django.db.models import Q
import matplotlib.pyplot as plt
import os


def index(request):
    unique_countries = Data.objects.values_list('country', flat=True).distinct()
    districts = Data.objects.values_list('district', flat=True).distinct()
    years = Data.objects.values_list('year', flat=True).distinct()
    str_years = map(str, years)
    industry = Data.objects.values_list('industry', flat=True).distinct()
    MKB_name = Data.objects.values_list('MKB_name', flat=True).distinct()
    values = {'country': unique_countries, 'district': districts, 'year': str_years, 'industry':industry, 'MKB_name':MKB_name}
    user_value = {key: [] for key in values}
    if request.method == 'POST':
        for param_name, param_value in values.items():
            for param in param_value:
                if request.POST.getlist(param):
                    user_value[param_name].append(param)
        filtered_data = filter_data(user_value, Data.objects)
        graph_path = create_graph(request, filtered_data)
        return render(request, 'main/index.html', {'countries': unique_countries, 'states': districts, 'years': years,
                                                'industries': industry, 'mkb_names': MKB_name, 'graph_path':graph_path})
    
    return render(request, 'main/index.html', {'countries': unique_countries, 'states': districts, 'years': years,
                                            'industries': industry, 'mkb_names': MKB_name})


def filter_data(user_value, data_objects):
    filters = Q()

    for key, values in user_value.items():
        if values:
            q = Q()
            for value in values:
                q |= Q(**{key: value})
            filters &= q

    if not filters:
        return data_objects.none()

    filtered_data = data_objects.filter(filters)
    return filtered_data


def create_graph(request, filtered_objects):
    Y = []
    X = []
    for row in filtered_objects:
        Y.append(row.country + ' ' + row.district + ' ' + str(row.year) + ' ' + row.industry + ' ' + row.MKB_name)
        X.append(row.morbidity)

    left_values = [0] * len(X)

    plt.figure(figsize=(15, 7))
    plt.barh(Y, X, left=left_values)
    plt.xlabel('Значения')
    plt.title('Горизонтальный столбчатый график')
    plt.subplots_adjust(left=0.3)

    script_dir = os.path.dirname(os.path.abspath(__file__))
    static_dir = os.path.join(script_dir, '..', 'static', 'graph')
    media_dir = os.path.join(script_dir, '..', 'media', 'graph')  # Путь к каталогу медиа

    os.makedirs(static_dir, exist_ok=True)
    os.makedirs(media_dir, exist_ok=True)

    file_name = 'horizontal_bar_chart.png'
    file_path = os.path.join(media_dir, file_name)  # Полный путь к файлу

    plt.savefig(file_path)

    return os.path.join('media', 'graph', file_name) 

