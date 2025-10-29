from django.http import HttpResponse
from django.template import loader
from .models import Member

def members(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))
  
def details(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))
  
def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def testing(request):
  mydata = Member.objects.all().values() # return specific columns Members.objects.values_list, return a specific name Member.objects.filter(firstname='Emil').values
  '''
  mydata = Member.objects.filter(firstname='Emil').values()
  mydata = Member.objects.filter(lastname='Refsnes', id=2).values()
  mydata = Member.objects.filter(firstname='Emil').values() | Member.objects.filter(firstname='Tobias').values()
  mydata = Member.objects.filter(firstname_startwith='L').values()
  And there are my other field Lookups keywords (refer for more)

  # Order by 
  mydata = Member.objects.all().order_by('firstname').values()
  mydata = Member.objects.all().order_by('firstname').values()
  mydata = Member.objects.all().order_by('lastname', 'id').values()
  '''
  mymembers = Member.objects.all().values()
  template = loader.get_template('template.html')
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],
    'firstname': 'Linus',
    'mymembers' : mydata,
    'x' : ['Apple', 'Banana', 'Cherry' ],
    'y' : ['Apple', 'Banana', 'Cherry' ],
  }
  return HttpResponse(template.render(context, request))

'''
# Commented out a section in the view


from django.http import HttpResponse
from django.template import loader

def testing(request):
  template = loader.get_template('template.html')
  #context = {
  # 'var1': 'John',
  #}
  return HttpResponse(template.render())


  
  '''


'''
# Comment of how to use the q operations 

from django.http import HttpResponse
from django.template import loader
from .models import Member
from django.db.models import Q

def testing(request):
  mydata = Member.objects.filter(Q(firstname='Emil') | Q(firstname='Tobias')).values()
  template = loader.get_template('template.html')
  context = {
    'mymembers': mydata,
  }
  return HttpResponse(template.render(context, request))

'''