import requests
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Payment

@api_view(['POST'])
def initiate_payment(request):
    data = request.data
    booking_reference = data.get('booking_reference')
    amount = data.get('amount')
    email = data.get('email')

    payload = {
        "amount": amount,
        "currency": "ETB",
        "email": email,
        "tx_ref": booking_reference,
        "callback_url": "https://yourdomain.com/verify-payment",
        "return_url": "https://yourdomain.com/payment-success"
    }

    headers = {
        "Authorization": f"Bearer {settings.CHAPA_SECRET_KEY}"
    }

    chapa_url = "https://api.chapa.co/v1/transaction/initialize"
    res = requests.post(chapa_url, json=payload, headers=headers)
    res_data = res.json()

    if res.status_code == 200 and res_data.get("status") == "success":
        checkout_url = res_data["data"]["checkout_url"]
        Payment.objects.create(
            booking_reference=booking_reference,
            amount=amount,
            transaction_id=res_data["data"]["tx_ref"],
            status="Pending"
        )
        return Response({"checkout_url": checkout_url})
    return Response({"error": res_data.get("message", "Failed to initiate payment")}, status=400)

@api_view(['GET'])
def verify_payment(request):
    tx_ref = request.GET.get('tx_ref')

    headers = {
        "Authorization": f"Bearer {settings.CHAPA_SECRET_KEY}"
    }

    res = requests.get(f"https://api.chapa.co/v1/transaction/verify/{tx_ref}", headers=headers)
    res_data = res.json()

    try:
        payment = Payment.objects.get(transaction_id=tx_ref)
    except Payment.DoesNotExist:
        return Response({"error": "Payment record not found"}, status=404)

    if res.status_code == 200 and res_data["data"]["status"] == "success":
        payment.status = "Completed"
        payment.save()
        return Response({"status": "Payment successful"})
    else:
        payment.status = "Failed"
        payment.save()
        return Response({"status": "Payment failed"}, status=400)
