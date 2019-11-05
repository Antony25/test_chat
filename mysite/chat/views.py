from django.shortcuts import render, redirect
from django.utils.safestring import mark_safe
import json
from pdb import set_trace
from django.http import JsonResponse
# Create your views here.

def index(request):
    return render(request, 'chat/index.html', {})

def room(request, room_name):
    if request.method == 'POST':
      success =  False
      message = ''
      try:
        request.session['name'] = request.POST.get('name')
        success = True
      except Exception as e:
        print('Exception to save name ={}'.format(str(e)))
        message =  str(e)
      return JsonResponse({'success': success, 'message':message})

    else:
      if 'name' not in request.session:
        return redirect('index')
        
      return render(request, 'chat/room.html', {
          'room_name_json': mark_safe(json.dumps(room_name))
      })
