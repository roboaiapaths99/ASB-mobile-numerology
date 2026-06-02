# ASB Numerology Theme Configuration

## Color Palette

### Primary Colors
- **Purple**: `#6b5bff` (Main brand color)
- **Navy**: `#1a1a3e` (Dark text/headings)
- **Cream**: `#f5f1e8` (Background)

### Accent Colors
- **Text**: `#1a1a3e` (Primary text)
- **Text Light**: `#5a5a7a` (Secondary text)
- **Surface**: `#ffffff` (White background)
- **Border**: `#e8e4db` (Light borders)

### Gradients
- **Main Gradient**: `linear-gradient(90deg, #1a1a3e, #6b5bff)`
- **Accent Gradient**: `linear-gradient(90deg, #7c3aed, #d946ef)`

---

## Typography

### Font Families
1. **Playfair Display** - Headings (h1-h6)
   - Weights: 500, 600, 700
   - Used for: All heading tags

2. **Cinzel** - Special/Numerology Text
   - Weights: 400, 700
   - Used for: Numbers, special emphasis, metric boxes

3. **Inter** - Body Text
   - Weights: 400, 500, 600, 700
   - Used for: All body text, buttons, inputs

### Font Sizes
- **h1**: `3rem` (line-height: 1.2)
- **h2**: `2rem` (line-height: 1.3)
- **h3**: `1.5rem` (line-height: 1.5)
- **h4**: `1.25rem`
- **p**: Default (line-height: 1.6)

### Google Fonts Import
```html
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Playfair+Display:wght@500;600;700&family=Cinzel:wght@400;700&display=swap" rel="stylesheet">
```

---

## Components

### 1. ASB Button (`.asb-button`)
```css
Background: linear-gradient(90deg, #7c3aed, #d946ef)
Padding: 1rem 2.5rem
Font Size: 1.05rem
Font Weight: 600
Border Radius: 0.75rem
Box Shadow: 0 8px 16px -4px rgba(124, 58, 237, 0.4)
Color: #fff
Letter Spacing: 0.5px

Hover Effects:
- Box Shadow: 0 15px 30px -10px rgba(124, 58, 237, 0.5)
- Transform: translateY(-3px)

Disabled:
- Opacity: 0.5
- Cursor: not-allowed
```

### 2. ASB Card (`.asb-card`)
```css
Background: #ffffff
Border: 1px solid #e8e4db
Border Radius: 0.5rem
Padding: 1.5rem
Box Shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05)
Transition: all 0.3s ease

Hover Effects:
- Box Shadow: 0 10px 20px -10px rgba(107, 91, 255, 0.2)
- Transform: translateY(-2px)
- Border Color: #6b5bff
```

### 3. Result Card (`.result-card`)
```css
Background: #ffffff
Border: 1px solid #e8e4db
Border Radius: 0.5rem
Padding: 1.5rem
Margin Bottom: 1rem
Box Shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05)
Transition: all 0.3s ease

h4 Styling:
- Font Family: Cinzel, serif
- Font Size: 1.25rem
- Color: #1a1a3e
- Margin Bottom: 0.5rem

p Styling:
- Color: #5a5a7a

Hover Effects:
- Same as .asb-card
```

### 4. Metric Box (`.metric-box`)
```css
Background: #ffffff
Border: 2px solid #e8e4db
Border Radius: 1rem
Padding: 2rem 1.5rem
Text Align: center
Box Shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05)
Transition: all 0.3s ease

h3 Styling (Metric Value):
- Font Family: Cinzel, serif
- Font Size: 3rem
- Font Weight: 700
- Color: #6b5bff
- Margin: 0 0 0.75rem 0

p Styling (Metric Label):
- Opacity: 0.8
- Font Weight: 500
- Color: #5a5a7a
- Font Size: 1rem

Hover Effects:
- Box Shadow: 0 12px 24px -10px rgba(107, 91, 255, 0.15)
- Transform: translateY(-4px)
- Border Color: #6b5bff

Variants:
- .metric-box.gold: Border #7c3aed, h3 color #7c3aed
- .metric-box.green: Border #6b5bff, h3 color #6b5bff
```

### 5. Form Inputs
```css
Input Fields (text, date, textarea):
- Background: #ffffff
- Border: 1px solid #e8e4db
- Border Radius: 0.5rem
- Padding: 0.75rem 1rem
- Font Family: Inter, system-ui, sans-serif
- Font Size: 1rem
- Width: 100%
- Transition: all 0.3s ease
- Color: #1a1a3e

Focus State:
- Border Color: #6b5bff
- Box Shadow: 0 0 0 3px rgba(107, 91, 255, 0.1)
- Outline: none

Placeholder:
- Color: #5a5a7a
```

### 6. Header Section (`.header-section`)
```css
Text Align: center
Margin Bottom: 3rem
Padding: 2rem 1rem

h1:
- Background: linear-gradient(90deg, #1a1a3e, #6b5bff)
- -webkit-background-clip: text
- -webkit-text-fill-color: transparent
- background-clip: text
- Margin Bottom: 0.5rem

p:
- Font Size: 1.1rem
- Color: #5a5a7a
```

### 7. Table Container (`.table-container`)
```css
Background: #ffffff
Border Radius: 0.5rem
Border: 1px solid #e8e4db
Overflow: hidden
Box Shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05)

Table:
- Width: 100%
- Border Collapse: collapse

Table Header (.table-header):
- Background: #6b5bff
- Color: white
- Font Family: Cinzel, serif
- Font Weight: 600
- Text Align: center
- Padding: 1rem

Table Rows:
- .table-row-good: Background #e6f7ed, Color #2d5a3d
- .table-row-bad: Background #ffe8e0, Color #8b4513
- .table-row-neutral: Background #f9fafb, Color #374151

Table Data Cell:
- Padding: 0.75rem 1rem
- Text Align: center
- Border Bottom: 1px solid #e8e4db
```

### 8. Loading Spinner
```css
Animation: spin 1s linear infinite
Border Radius: 9999px
Height: 2rem
Width: 2rem
Border: 2px solid #6b5bff (bottom + top transparent)
```

### 9. Error Message (`.error-message`)
```css
Background: #fef2f2
Border: 1px solid #fecaca
Border Radius: 0.5rem
Padding: 1rem
Color: #dc2626
Margin Bottom: 1.5rem
```

---

## Animations

### Cosmic Float
```css
@keyframes cosmic-float {
  0%, 100% {
    transform: translateY(0) rotate(0);
  }
  50% {
    transform: translateY(-15px) rotate(2deg);
  }
}

Duration: 6s
Timing: ease-in-out
Iteration: infinite
```

### Spin
```css
@keyframes spin {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}

Duration: 1s
Timing: linear
Iteration: infinite
```

---

## Spacing System

### Margin
- `mb-2`: 0.5rem
- `mb-4`: 1rem
- `mb-6`: 1.5rem
- `mb-8`: 2rem
- `mt-1`: 0.25rem
- `mt-2`: 0.5rem
- `mt-4`: 1rem
- `mt-6`: 1.5rem

### Padding
- `p-4`: 1rem
- `p-6`: 1.5rem
- `px-4`: 1rem left/right
- `px-8`: 2rem left/right
- `py-3`: 0.75rem top/bottom
- `py-4`: 1rem top/bottom
- `py-12`: 3rem top/bottom

### Gap
- `gap-4`: 1rem
- `gap-6`: 1.5rem

---

## Grid System

```css
.grid-cols-1: 1 column
.grid-cols-2: 2 columns
.grid-cols-3: 3 columns

Responsive:
@media (min-width: 768px) {
  .md\:grid-cols-2: 2 columns
  .md\:grid-cols-3: 3 columns
}
```

---

## CSS Variables

```css
:root {
  --asb-purple: #6b5bff;
  --asb-navy: #1a1a3e;
  --asb-cream: #f5f1e8;
  --asb-text: #1a1a3e;
  --asb-text-light: #5a5a7a;
  --asb-surface: #ffffff;
  --asb-border: #e8e4db;
  --gradient-accent: linear-gradient(90deg, #1a1a3e, #6b5bff);
}
```

---

## Scrollbar Styling

```css
::-webkit-scrollbar {
  width: 6px;
}

::-webkit-scrollbar-track {
  background-color: #f5f1e8;
}

::-webkit-scrollbar-thumb {
  background-color: #6b5bff;
  border-radius: 9999px;
}

::-webkit-scrollbar-thumb:hover {
  background-color: #5a4aee;
}
```

---

## Text Utilities

- `.text-sm`: 0.875rem
- `.text-lg`: 1.125rem
- `.text-xl`: 1.25rem
- `.text-2xl`: 1.5rem
- `.text-4xl`: 2.25rem
- `.text-asb-purple`: Color #6b5bff
- `.text-asb-navy`: Color #1a1a3e
- `.text-gray-500`: Color #6b7280
- `.text-gray-600`: Color #4b5563
- `.text-gray-700`: Color #374151

## Font Weight Utilities

- `.font-medium`: 500
- `.font-semibold`: 600
- `.font-bold`: 700

---

## Tailwind Configuration

See `tailwind.config.js` for extended theme configuration including custom colors, fonts, shadows, and animations.
can you change the whole theme of frontend according to this -