
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from bag.contexts import bag_contents

import stripe
 
def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Oops...There's nothing in your bag!")
        return redirect(reverse('products'))

    current_bag = bag_contents(request)
    total_sum = current_bag['grand_total']
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51LYBaOEqAJbeRep0mf1bdGQvOvm0XYUeT32IRVBgDR8aDISffJaYN8Wnq7rsATTwvba2NMItSOZuhfUKAugNSb5Z00ytpMiMYe',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)