/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./app/**/*.{js,ts,jsx,tsx}",
    "./pages/**/*.{js,ts,jsx,tsx}",
    "./components/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      fontFamily: {
        main: ["VT323", "monospace"],
      },
      colors: {
        bgPrimary: "#16213E",
        bgSecondary: "#0F3460",
        secondary: "#533483",
        primary: "#E94560",
      },
    },
  },
  plugins: [],
};
