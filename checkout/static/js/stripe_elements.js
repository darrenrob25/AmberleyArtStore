/*
    Core logic/payment flow for this comes from here:
    https://stripe.com/docs/payments/accept-a-payment

    CSS from here: 
    https://stripe.com/docs/stripe-js
*/

var stripe_public_key = $('#id_stripe_public_key').text().slice(1, -1);
var client_secret = $('#id_client_secret').text().slice(1, -1);

// Debugging: Log the raw HTML elements
console.log("Raw Public Key Element:", $('#id_stripe_public_key').text());
console.log("Raw Client Secret Element:", $('#id_client_secret').text());

// Debugging: Check if the keys are correct
console.log("Stripe Public Key:", stripe_public_key);
console.log("Client Secret:", client_secret);

// Initialize Stripe
var stripe = Stripe(stripe_public_key);
var elements = stripe.elements();
var style = {
    base: {
        color: '#000',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};

// Create the card element
var card = elements.create('card', {style: style});
card.mount('#card-element');