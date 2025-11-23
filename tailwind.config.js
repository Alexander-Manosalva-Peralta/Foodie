// Foodie_ECommerce_V1.0/tailwind.config.js
/** @type {import('tailwindcss').Config} */
module.exports = {
  // CRÍTICO: Rutas para que Tailwind escanee tus clases
  content: [
    "./templates//*.html", // Escanea todos los archivos HTML en la carpeta templates
    "./app/static/js/*.js", // Escanea si usas clases dinámicas en JS
  ],
  theme: {
    // Extiende el tema por defecto de Tailwind
    extend: {
      colors: {
        // Paleta de la plantilla 'Uptown' (Oscuro y Dorado)
        'primary-dark': '#0A0A0A',      // Negro principal (Fondo)
        'secondary-gold': '#C8A97E',    // Dorado/Ocre (Acentos, Links, Títulos)
        'dark-gray': '#1A1A1A',         // Gris Oscuro (Tarjetas, Formularios, Componentes)
        'light-text': '#EAEAEA',        // Texto claro
      },
      fontFamily: {
        // Fuente de ejemplo elegante (si usas una fuente específica)
        sans: ['Garamond', 'serif'],
      },
    },
  },
  plugins: [],
}