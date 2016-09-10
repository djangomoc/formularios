from django.shortcuts import render

def form_manual(request):
    data = {}
    if request.method == 'POST':
    	data['name'] = request.POST.get('name', 'name not found')
    	data['active'] = request.POST.get('active', 'off')
    	data['week'] = request.POST.get('week', 'week not found')
    	data['month'] = request.POST.get('month', 'month not found')

    return render(request, 'core/index.html', data)