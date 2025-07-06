// =============================================================================
// THEME PROVIDER COMPONENT
// =============================================================================
// This component provides theme management functionality for the application.
// Wraps the next-themes provider to enable dark/light mode switching.
// Currently not actively used but available for future theme implementation.

'use client'

import * as React from 'react'
import {
  ThemeProvider as NextThemesProvider,
  type ThemeProviderProps,
} from 'next-themes'

/**
 * Theme provider component that wraps the next-themes provider
 * Enables theme switching functionality throughout the application
 * 
 * @param children - React components to be wrapped with theme context
 * @param props - Additional props to pass to the theme provider
 * @returns Theme provider wrapper component
 */
export function ThemeProvider({ children, ...props }: ThemeProviderProps) {
  return <NextThemesProvider {...props}>{children}</NextThemesProvider>
}
