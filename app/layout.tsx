// =============================================================================
// ROOT LAYOUT COMPONENT
// =============================================================================
// This is the root layout that wraps all pages in the application.
// Defines the basic HTML structure and metadata for the entire app.
// Includes global styles and sets up the document structure.

import type { Metadata } from 'next'
import './globals.css'

// Metadata configuration for the application
export const metadata: Metadata = {
  title: 'CodeTech', // Application title
  description: 'Created by CodeTech Team', // Application description

}

// Root layout component that wraps all pages
export default function RootLayout({
  children, // React components to be rendered inside the layout
}: Readonly<{
  children: React.ReactNode
}>) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  )
}
