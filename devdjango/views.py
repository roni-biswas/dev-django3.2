"""
To render HTML web pages
---------------------------------
"""

from django.http import HttpResponse
import random


def home_page(request):

    ranNum = random.randint(10, 9999)

    num1 = 25
    num2 = 75
    name = "Roni Biswas"
    cuntry = "Bangladesh"

    HTML_CONTENT = f"""
    <h1>Hi! I'm {name} from {cuntry}.</h1>
    <h3> Random Number is : roni@{ranNum}</h3>
    <p>Total number of ______ {num1} + {num2} = {num1+num2}</p>

    """
    return HttpResponse(HTML_CONTENT)