from flask import Blueprint, request, jsonify
import stripe
import os

webhook_bp = Blueprint('webhook', __name__)

endpoint_secret = os.getenv('STRIPE_WEBHOOK_SECRET')

@webhook_bp.route('/webhook', methods=['POST'])
def stripe_webhook():
    payload = request.data
    sig_header = request.headers.get('Stripe-Signature')
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        return 'Invalid payload', 400
    except stripe.error.SignatureVerificationError as e:
        return 'Invalid signature', 400

    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        print(f"✅ Payment successful for session: {session['id']}")

    return '', 200
