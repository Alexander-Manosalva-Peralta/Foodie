/** @type {import('tailwindcss').Config} */
module.exports = {
  // Le decimos a Tailwind dónde buscar clases en tu proyecto Flask
  content: [
    "./templates/**/*.html",
    "./static/js/**/*.js"
  ],
  theme: {
    extend: {
      colors: {
        'primary-bg': '#F9F7F1',
        'text-dark': '#1A1A1A',
        'accent-gold': '#BFA36F',
        'card-bg': '#FFFFFF',
      },
      fontFamily: {
        serif: ['Garamond', 'serif'],
      },
    },
  },
  plugins: [],
};
