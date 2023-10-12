/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/*"],
  theme: {
    extend: {
      colors:{
        primary: '#1e3a8a',
        second: '#d1d5db'
      },
      fontFamily:{
        display: ['Iceberg']
      }
    },
  },
  plugins: [],
}

