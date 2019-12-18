from django.http import HttpResponse
from django.shortcuts import render
from operator import itemgetter


def homepage(request):
   # return HttpResponse('Hello, u in homepage') # this syntax is good when we dont use html
   return render(request, 'home.html')

def count_words(request):
   full_text= request.GET['fulltext']   # This is taken from home.html. Must be same in both place
   #print(full_text)  # This is for testing.Full text will be dispayed in terminal

   # for printing in website
   word_list= full_text.split()
   word_dictionary= {}

   for word in word_list:
       if word in word_dictionary:
           # need to add
           word_dictionary[word]+=1
       else:
           word_dictionary[word]=1
   dict_to_list= list(word_dictionary.items())     # converting dict to 2d list
   

   #sorted_words= dict_to_list1.sort(reverse= True)
   sorted_words = sorted(dict_to_list, key=itemgetter(1), reverse=True) # To sort in descending order

   return render(request, 'count_result.html', {'full':full_text,'counting_words':len(word_list), 'sorted':sorted_words,'counting':word_dictionary, 'counting2':word_dictionary.items()})  # Dictionay is used to display in web

def about_me(request):
       # return HttpResponse('Hello, u in homepage') # this syntax is good when we dont use html
   return render(request, 'about.html')

