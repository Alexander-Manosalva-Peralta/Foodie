// Foodie_ECommerce_V1.0/static/js/customizer_visualizer.js

/**
 * Lógica del Personalizador de Platos:
 * Maneja la interacción, el cálculo de precios y la visualización.
 */

document.addEventListener('DOMContentLoaded', () => {
    const customizerForm = document.querySelector('.lg\\:col-span-1');
    const finalPriceElement = document.getElementById('final-price');
    const extraCostElement = document.getElementById('extra-cost');
    const visualizerArea = document.getElementById('visualizer-area');
    const addButton = document.getElementById('add-custom-to-cart');

    // Precio base del plato (hardcodeado para el ejemplo, en un real vendría de la DB)
    const BASE_PRICE = 25.00;

    /**
     * Recalcula el precio total y actualiza la UI.
     */
    function recalculatePriceAndVisualize() {
        let totalExtraCost = 0.00;
        let selectedIngredients = [];

        // Limpia el visualizador para la actualización
        visualizerArea.innerHTML = '<p class="text-gray-500">Aquí se visualizarán los ingredientes seleccionados.</p>';

        // Itera sobre todos los inputs del formulario
        customizerForm.querySelectorAll('input:checked').forEach(input => {
            const price = parseFloat(input.getAttribute('data-price'));
            const value = input.value;
            const name = input.parentNode.textContent.trim().split('(+S/')[0].trim();
            const category = input.name;

            if (price > 0) {
                totalExtraCost += price;
            }

            // Simulación de visualización de ingredientes
            const icon = document.createElement('span');
            icon.className = absolute text-2xl p-2 rounded-full bg-opacity-70;
            icon.style.left = ${Math.random() * 70 + 10}%; // Posición aleatoria
            icon.style.top = ${Math.random() * 70 + 10}%;

            let emoji = '🍽'; // Default
            if (category === 'base') emoji = '🍚';
            if (category === 'protein') emoji = '🍗';

            icon.textContent = emoji;
            visualizerArea.appendChild(icon);

            selectedIngredients.push({
                id: value,
                name: name,
                price: price,
                category: category
            });
        });

        const finalPrice = BASE_PRICE + totalExtraCost;
        finalPriceElement.textContent = finalPrice.toFixed(2);
        extraCostElement.textContent = totalExtraCost.toFixed(2);

        // Almacenar temporalmente los ingredientes seleccionados
        customizerForm.ingredients = selectedIngredients;

        // Habilita/Deshabilita el botón (Ejemplo: Base es obligatoria)
        const baseSelected = customizerForm.querySelector('input[name="base"]:checked');
        addButton.disabled = !baseSelected;
    }

    // Escucha cambios en todos los inputs (radio y checkbox)
    customizerForm.addEventListener('change', recalculatePriceAndVisualize);

    // Inicializa el estado
    recalculatePriceAndVisualize();


    // Evento de Añadir al Carrito Personalizado
    addButton.addEventListener('click', () => {
        const selectedIngredients = customizerForm.ingredients;
        if (!selectedIngredients || selectedIngredients.length === 0) {
            alert('Por favor, selecciona al menos una base.');
            return;
        }

        const itemData = {
            product_id: 'custom_dish_base_001', // ID genérico para plato personalizado
            quantity: 1,
            // Solo envía los datos esenciales de personalización
            customization: selectedIngredients
        };

        // Llama a la función global del carrito (cart_store.js)
        if (typeof addToCart === 'function') {
            addToCart(itemData);
            alert(Plato personalizado (S/${finalPriceElement.textContent}) añadido al carrito!);
        } else {
            console.error('El script cart_store.js no se cargó correctamente.');
        }
    });

});