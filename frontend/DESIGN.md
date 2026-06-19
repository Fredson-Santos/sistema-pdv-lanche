---
name: Lanche MVP
description: A modern, dark-themed, sleek frontend design for Lanche MVP.

colors:
  primary: "#F97316"
  primary-dark: "#EA6C06"
  bg: "#0F172A"
  bg-card: "#1E293B"
  bg-sidebar: "#0B1120"
  text-primary: "#F8FAFC"
  text-secondary: "#94A3B8"
  text-muted: "#475569"
  success: "#22C55E"
  danger: "#EF4444"
  warning: "#EAB308"
  info: "#3B82F6"

typography:
  body:
    fontFamily: "Inter, -apple-system, sans-serif"
    fontSize: "16px"
  text-xs:
    fontSize: "0.75rem"
  text-sm:
    fontSize: "0.875rem"
  text-md:
    fontSize: "1rem"
  text-lg:
    fontSize: "1.125rem"
  text-xl:
    fontSize: "1.25rem"
  text-2xl:
    fontSize: "1.5rem"
  text-3xl:
    fontSize: "1.875rem"

rounded:
  sm: "6px"
  md: "10px"
  lg: "14px"
  xl: "20px"
  full: "9999px"

spacing:
  "1": "4px"
  "2": "8px"
  "3": "12px"
  "4": "16px"
  "5": "20px"
  "6": "24px"
  "8": "32px"
  "10": "40px"
  "12": "48px"

components:
  btn-primary:
    backgroundColor: "{colors.primary}"
    textColor: "#ffffff"
    rounded: "{rounded.md}"
  card:
    backgroundColor: "{colors.bg-card}"
    rounded: "{rounded.lg}"
    padding: "{spacing.6}"
---

## Overview

The Lanche MVP interface is built on a dark slate foundation, using a vibrant orange as its primary brand color. The aesthetic aims for a premium, developer-focused, and modern look, emphasizing readability and depth.

## Colors

The palette relies heavily on dark slate backgrounds to create depth, contrasted with a bright, energetic orange for primary interactions.

- **Background (#0F172A):** The deep dark canvas for the application.
- **Card Background (#1E293B):** A slightly lighter slate for elevated elements like cards and forms.
- **Primary (#F97316):** A vibrant orange used for primary actions, active states, and glowing effects.
- **Text Primary (#F8FAFC):** Near-white text for high contrast and readability on dark backgrounds.
- **Text Secondary (#94A3B8):** Soft slate text for supporting content and metadata.

## Typography

The typography relies entirely on the `Inter` font family, providing a clean, geometric, and highly legible sans-serif experience. 
Weights range from regular (400) for body text to bold (700) for headings and important values.

## Components

### Buttons
Buttons feature a gradient orange background and subtle hover glows (`0 6px 24px rgba(249, 115, 22, 0.45)`) that make them feel alive and responsive. They use medium rounding (`10px`).

### Cards
Cards and stat cards use a slightly elevated background (`#1E293B`) with large rounding (`14px`) and ample padding (`24px`). Stat cards feature a subtle top border gradient that reinforces the brand color.

### Form Inputs
Form elements use an elevated background with subtle border transitions. On focus, inputs show a distinct orange border and a glowing box-shadow (`rgba(249, 115, 22, 0.25)`), providing clear interaction feedback.
