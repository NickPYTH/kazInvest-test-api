import json

import requests
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def ask_ai(request):
    question = request.GET.get('question')
    url = 'https://api.pawan.krd/cosmosrp/v1'
    payload = {
        "model": "gpt-3.5-turbo",
        "max_tokens": 100,
        "messages": [
            {"role": "system", "content":  "You are an helpful assistant."},
            {"role": "user", "content": question}
        ]
    }
    headers = {
        'Authorization': 'pk-DrZJDAKvKSmAcFwxkFiyusEVaJoEHSIkBdKbWQxQZrSBXANM',
        'Content-Type': 'application/json'
    }
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    if response.status_code != 200:
        return Response({'error': response.json()['error']['message']}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'answer': response.json()['choices'][0]['message']['content']}, status=status.HTTP_200_OK)