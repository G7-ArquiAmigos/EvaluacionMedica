from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse(<head>
  <meta charset="UTF-8">
  <title>Hola Mundo</title>
</head>
<body>
  <h1>Hola Mundo</h1>
</body>)
