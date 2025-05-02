from django.shortcuts import render
from .model import predict_cost

def estimator_form(request):
    result = None
    if request.method == 'POST':
        site_type = request.POST['site_type']
        pages = int(request.POST['pages'])
        features_selected = request.POST.getlist('features')
        features = len(features_selected)
        design = request.POST['design']
        urgency = request.POST['urgency']
        result = predict_cost(site_type, pages, features, design, urgency)
    return render(request, 'estimator.html', {'result': result})