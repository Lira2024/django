from django.shortcuts import render

def index(request):
    #PAGINA PRINCIPAL LEARNING_LOG
    return render(request, 'learnig_logs/index.html')
