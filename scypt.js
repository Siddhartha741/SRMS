document.addEventListener('DOMContentLoaded', function () {
    const products = [
        {
            name: 'Surgical Mask',
            description: 'A high-quality surgical mask for protection.',
            price: '$1.50'
        },
        {
            name: 'Hand Sanitizer',
            description: 'Alcohol-based hand sanitizer for hygiene.',
            price: '$3.00'
        },
        {
            name: 'Gloves',
            description: 'Disposable gloves for medical use.',
            price: '$5.00 per box'
        },
        {
            name: 'Thermometer',
            description: 'Digital thermometer for accurate temperature measurement.',
            price: '$10.00'
        },
        {
            name: 'Blood Pressure Monitor',
            description: 'Digital blood pressure monitor for home use.',
            price: '$25.00'
        }
    ];

    const productContainer = document.getElementById('product-list');
    products.forEach(product => {
        const productElement = document.createElement('div');
        productElement.classList.add('product-item');
        productElement.innerHTML = `
            <h3>${product.name}</h3>
            <p>${product.description}</p>
            <strong>${product.price}</strong>
        `;
        productContainer.appendChild(productElement);
    });

    const contactForm = document.getElementById('contact-form');
    contactForm.addEventListener('submit', function (event) {
        event.preventDefault();
        alert('Message sent!');
        contactForm.reset();
    });
});
