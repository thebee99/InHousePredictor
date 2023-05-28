from django.shortcuts import render, redirect
from myapp.models import UserChoice

def submit(request):
    if request.method == 'POST':
        selected_info = request.POST.get('info_1')
        return render(request, 'myapp/prediction.html')
    return render(request, 'myapp/Ai.html')

def prediction_view(request):
    if request.method == 'POST':
        # POST 요청에서 입력된 데이터 가져오기
        location = request.POST.get('location')
        certificate = request.POST.get('certificate')
        listing_area = request.POST.get('listing_area')
        bedroom_count = request.POST.get('bedroom_count')
        bathroom_count = request.POST.get('bathroom_count')
        jakarta_division = request.POST.get('Division_info')
        
        # 필요한 다른 정보들도 가져오기
        
        context = {
            'location': location,
            'certificate': certificate,
            'listing_area': listing_area,
            'bedroom_count': bedroom_count,
            'bathroom_count': bathroom_count,
            'jakarta_division': jakarta_division,
            # 필요한 다른 정보들도 context에 추가
        }
        
        # 결과 페이지로 이동하기 위해 render 함수를 사용하여 result.html 렌더링
        return render(request, 'myapp/result.html', context)
    
    # GET 요청일 경우 prediction.html을 렌더링
    return render(request, 'myapp/prediction.html')

# def result_view(request):
#     # 결과 페이지에 입력된 정보 전달하기
#     location = request.POST.get('location')
#     room_count = request.POST.get('room_count')
#     # 필요한 다른 정보들도 가져오기
    
#     context = {
#         'location': location,
#         'room_count': room_count,
#         # 필요한 다른 정보들도 context에 추가
#     }
#     return render(request, 'app_name/result.html', context)