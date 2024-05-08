from django.shortcuts import render
from blog.models import Product, ProductSpec
from django.http import HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
# def compare(request):
#     ProductSpec = {'Products': Product.objects.all().order_by('-product_id')}
#     return render(request, 'prototype.html')

def search(request):
    if request.method == 'GET':
        search_text = request.GET.get('search_text', '')
        products = Product.objects.filter(product_name__icontains=search_text)
        return render(request, 'search_results.html', {'products': products})

@csrf_exempt
def compare(request):
    test_string = 'Chua co gi ca!!!!'  # Khởi tạo test_string trước
    if request.method == 'POST':
        searchpr1 = request.POST.get('searchpr1')
        searchpr2 = request.POST.get('searchpr2')

        try:
            product1 = Product.objects.get(product_name=searchpr1)
            product2 = Product.objects.get(product_name=searchpr2)

            product1_specs = ProductSpec.objects.filter(product=product1)
            product2_specs = ProductSpec.objects.filter(product=product2)

            context = {
                'product1': product1,
                'product2': product2,
                'product1_specs': product1_specs,
                'product2_specs': product2_specs,
                'test_string': 'Hello World',
            }

            return render(request, 'prototype.html', context)
        
        except Product.DoesNotExist:
            # Xử lý khi sản phẩm không tồn tại
            test_string = 'Sản phẩm không tồn tại'  # Gán giá trị cho test_string

    # Trả về template và truyền test_string vào context
    return render(request, 'prototype.html', {'test_string': test_string})


from django.http import HttpResponse

def test(request):
    if request.method == 'POST':
        return render(request, 'test_fe_be.html', {'test_string': 'Hello World'})
    return render(request, 'test_fe_be.html', {'test_string': 'Chua co du lieu'})

def testapi(request):
    # Xử lý yêu cầu POST
    if request.method == 'POST':
        test_string = 'Hello World'
        return render(request, 'test_fe_be.html', {'test_string': test_string})
    
    # Xử lý yêu cầu GET hoặc các phương thức khác
    return render(request, 'test_fe_be.html', {'test_string': 'Chua co gi ca'})