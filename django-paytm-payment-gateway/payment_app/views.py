# payment_app/views.py

import logging
import requests
import json
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from paytmpg import EnumCurrency, EChannelId, UserSubWalletType
from paytmpg import ExtendInfo, ShippingInfo, GoodsInfo, UserInfo, PaymentMode, Money
from paytmpg import PaymentDetailsBuilder, PaymentStatusDetailBuilder
from paytmpg import RefundDetailBuilder, RefundStatusDetailBuilder
from paytmpg import MerchantProperty, LibraryConstants
from paytmpg import Payment, Refund
from paytmchecksum import PaytmChecksum

logger = logging.getLogger(__name__)

def initiate_payment(request):
    # Your initialization code here

    # Create a dictionary with payment parameters
    paytmParams = {
        "MID": settings.PAYTM_MID,
        "ORDERID": "UNIQUE_ORDER_ID",  # Replace with your unique order ID
        "TXN_AMOUNT": "1.00",          # Replace with the transaction amount
        "CUST_ID": "CUSTOMER_ID",      # Replace with the customer's ID
        "MOBILE_NO": "CUSTOMER_MOBILE_NO",
        "EMAIL": "CUSTOMER_EMAIL_ID",
        "INDUSTRY_TYPE_ID": "Retail",
        "WEBSITE": settings.PAYTM_WEBSITE,
        "CHANNEL_ID": "WEB",
        "CALLBACK_URL": settings.PAYTM_CALLBACK_URL,
    }

    # Generate the checksum using PaytmChecksum library
    paytmChecksum = PaytmChecksum.generateSignature(paytmParams, settings.PAYTM_KEY)

    # Add the checksum to the parameters
    paytmParams["CHECKSUMHASH"] = paytmChecksum

    # Redirect the user to the Paytm payment gateway
    paytm_url = "https://securegw.paytm.in/theia/processTransaction"
    response = requests.post(paytm_url, json=paytmParams)
    response_dict = response.json()
    return render(request, 'payment_app/payment_form.html', {'paytm_dict': response_dict})


def payment_status(request):
    if request.method == 'POST':
        # Get the payment status from Paytm using the provided SDK code
        order_id = request.POST['ORDERID']
        read_timeout = 30 * 1000
        payment_status_detail = PaymentStatusDetailBuilder(order_id).set_read_timeout(read_timeout).build()
        response = Payment.getPaymentStatus(payment_status_detail)
        return render(request, 'payment_app/payment_status.html', {'payment_status': response})
    return HttpResponse("Invalid Request Method")

def payment_response(request):
    # Handle the payment response from Paytm here
    # This view will be called by Paytm after payment is completed

    # You can extract payment details from the request and update your database accordingly
    # Be sure to validate the response for security
    return HttpResponse("Payment Response Received")
