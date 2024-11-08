from django.shortcuts import render
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
blogs=[{
"id":1,
"title":"python",
"description":"python is high level programming language"    
},
{
"id":1,
"title":"python",
"description":"python is high level programming language"   
}
]
@csrf_exempt
def creatAndGetAllBlogs(request):
    if(request.method=="GET"):
        return JsonResponse({"blogs":blogs},safe=False)
    elif(request.method=="POST"):
        data=json.loads(request.body)
        print(data)
        type(data)
        new_blog={
            "id":len(blogs)+1,
            "title":data.get("title"),
            "description":data.get("description"),
            
        }
        blogs.append(new_blog)
        return JsonResponse({"message":"Blog Created Successfully","blog":new_blog},status=201)
        
        
    
# Create your views here.
