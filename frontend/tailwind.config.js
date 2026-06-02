/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        'asb-purple': '#6b5bff',
        'asb-navy': '#1a1a3e',
        'asb-cream': '#f5f1e8',
        'asb-text': '#1a1a3e',
        'asb-text-light': '#5a5a7a',
        'asb-surface': '#ffffff',
        'asb-border': '#e8e4db',
      },
      fontFamily: {
        'numerology': ['Cinzel', 'serif'],
        'heading': ['Playfair Display', 'serif'],
        'body': ['Inter', 'system-ui', 'sans-serif'],
      },
      backgroundImage: {
        'asb-gradient': 'linear-gradient(90deg, #1a1a3e, #6b5bff)',
        'asb-gradient-text': 'linear-gradient(to right, #1a1a3e, #6b5bff)',
      },
      boxShadow: {
        'asb-light': '0 4px 6px -1px rgba(0, 0, 0, 0.05)',
        'asb-card': '0 10px 15px -3px rgba(0, 0, 0, 0.08)',
        'asb-card-hover': '0 20px 40px -20px rgba(107, 91, 255, 0.2)',
      },
      animation: {
        'cosmic-float': 'cosmic-float 6s ease-in-out infinite',
        'ping-slow': 'ping 8s cubic-bezier(0, 0, 0.2, 1) infinite',
      },
      keyframes: {
        'cosmic-float': {
          '0%, 100%': { transform: 'translateY(0) rotate(0)' },
          '50%': { transform: 'translateY(-15px) rotate(2deg)' },
        },
      },
    },
  },
  plugins: [],
}
