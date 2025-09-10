from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from service.models import Stud
from Profile.models import photo

def myinsert(request):
	data1={}
	try:
		s1=Stud.objects.all();
		data1={
			'data1':s1,
			'id':'',
			'name':'',
			'city':''
		}

		if request.method=='GET':
			roll=request.GET['id']
			name=request.GET['name']
			city=request.GET['city']

			print(roll,name,city)


			s1=Stud.objects.all();

			data1={

				'data1':s1,
				'id':roll,
				'name':name,
				'city':city

			}


		if request.method=='POST':
			roll=request.POST['roll']
			name=request.POST['name']
			city=request.POST['city']
			print(roll,name,city)

			s2=Stud(id=roll,name=name,city=city)
			s2.save();
			print("Record is Save")
	except:
		pass

	return render(request,'index.html',data1)

def mydelete(request):
	id1=request.GET['id']
	s2=Stud.objects.get(id=id1)
	s2.delete()
	print("Record is Delete")
	return HttpResponseRedirect('/myinsert')
def myview(request):
	return render(request,'ajax.html')

def mysave(request):
	if request.method=='GET':
		roll=request.GET['roll']
		name=request.GET['name']
		city=request.GET['city']

		print("Roll",roll)
		print("Name",name)
		print("City",city)

	return JsonResponse({'data':'data success'})

#CRUD APPLICATION


def myajax(request):
	return render(request,'fetchdata.html')

def myfetch(request):
	s2=Stud.objects.values()
	data=list(s2)
	print("Hello ajax call")
	return JsonResponse({'key':data})


def mydel(request):
	id1=request.GET['id']
	s2=Stud.objects.get(id=id1)
	s2.delete()
	print("Record is Delete")
	return JsonResponse({'data':'Record is Delete'})

def myadd(request):
	if request.method=='GET':

		roll=request.GET['roll']
		name=request.GET['name']
		city=request.GET['city']
		print("Roll",roll)
		print("Name",name)
		print("City",city)
		s1=Stud(id=roll,name=name,city=city)
		s1.save()
	return JsonResponse({'data':'Record is Save'})
	
def myup(request):
	id=request.GET['id']
	s2=Stud.objects.get(id=id)
	data={

		'id':s2.id,
		'name':s2.name,
		'city':s2.city

	}

	return JsonResponse({'key':data})

def pic(request):
	try:
		if(request.method=='POST'):
			name=request.POST['name']
			
			img=request.FILES['img']
		
			s1=photo(name=name,image=img)
			s1.save()
			
	except Exception as e1:
		print("Error user=",e1)
	return render(request,"pic.html")
