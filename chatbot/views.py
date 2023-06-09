from django.shortcuts import render
from django.http import JsonResponse
import openai
import os


print(os.environ)

openai_api_key = os.environ.get("OPENAI_API_KEY")
openai.api_key = openai_api_key


def ask_openai(message):

    
    
    response = openai.Completion.create(
        model= "text-davinci-003",
        prompt = message,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7,
    ) 
    answer = response.choices[0].text.strip()
    return answer
    





# Create your views here.
def chatbot(request):

    # If receiving or sending
    if request.method == 'POST':
            message = request.POST.get('message') # message from body of fetch post
            response = ask_openai(message)
            return JsonResponse({'message': message, 'response': response})
    return render(request, 'chatbot.html')