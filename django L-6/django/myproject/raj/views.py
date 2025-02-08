from django.shortcuts import render
 
#add 
from .models import rajvarity
from django.shortcuts import get_object_or_404

#  #create your views here
# def raj(request):
#     return render(request,'raj/all.html')




# database se request le kr all  value ko forword 
def raj(request):
    fetch_data_to_backend= rajvarity.objects.all()
    return render(request,'raj/all.html', {'fetch_data_to_backend':fetch_data_to_backend})


# def raj_detail(request, raj_id):       wrong
#     rajId=get_object_or_404(rajvarity, raj_id, pk=raj_id)
#     return render(request, 'raj/raj_detail.html', {'rajId':rajId})

# currect
def raj_detail(request, raj_id):
    rajId = get_object_or_404(rajvarity, pk=raj_id)  # Correct lookup
    return render(request, 'raj/raj_detail.html', {'rajId': rajId})