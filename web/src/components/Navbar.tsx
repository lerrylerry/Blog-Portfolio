import Link from 'next/link'
import { useState } from 'react'

export default function Navbar() {
  const [open, setOpen] = useState(false)
  const nav = [
    { name: 'HOME', href: '/' },
    { name: 'ABOUT', href: '/about' },
    { name: 'BLOG', href: '/blog' },
    { name: 'PROJECTS', href: '/projects' },
    { name: 'RESUME', href: '/contact' }
  ]

  return (
    <header className="bg-[#DAE5E6] dark:bg-gray-900 shadow-sm">
      <div className="container mx-auto py-1 md:py-2 lg:py-3 px-3 md:px-4 lg:px-8">
        <div className="flex items-center justify-between h-16 p-0 mx-4">
          {/* Logo */}
          <Link href="/" className="flex items-center gap-3">
            <span className="inline-block w-8 h-8 rounded-full bg-gradient-to-r from-indigo-500 to-pink-500" />
            <span className="font-semibold text-2xl text-gray-800 dark:text-gray-100">LERRY</span>
          </Link>

          {/* Desktop nav */}
          <nav className="hidden lg:flex lg:items-center lg:space-x-6">
            {nav.map((item) => (
              <Link
                key={item.name}
                href={item.href}
                className="p-3 text-gray-700 dark:text-gray-300 hover:text-indigo-600 hover:underline dark:hover:text-indigo-400 dark:hover:underline transition"
              >
                {item.name}
              </Link>
            ))}
          </nav>

          {/* Actions / CTA */}
          <div className="hidden lg:flex lg:items-center lg:space-x-4 flex-shrink-0">
            <Link
              href="#"
              className="px-4 py-2 rounded-md border border-indigo-500 text-indigo-600 hover:bg-indigo-50 dark:hover:bg-indigo-900/20 transition"
              target="_blank"
            >
              LOG IN
            </Link>
            <Link
              href="#"
              className="px-4 py-2 bg-indigo-600 text-white rounded-md hover:opacity-95 transition"
            >
              SIGN UP
            </Link>
          </div>

          {/* Mobile menu button */}
          <div className="lg:hidden">
            <button
              aria-label="Toggle menu"
              aria-expanded={open}
              onClick={() => setOpen((v) => !v)}
              className="inline-flex items-center justify-center p-2 rounded-md text-gray-700 dark:text-gray-200 hover:bg-gray-100 dark:hover:bg-gray-800 focus:outline-none focus:ring-2 focus:ring-indigo-500"
            >
              <svg className={`w-6 h-6 transition-transform ${open ? 'rotate-90' : ''}`} fill="none" viewBox="0 0 24 24" stroke="currentColor">
                {open ? (
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
                ) : (
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 6h16M4 12h16M4 18h16" />
                )}
              </svg>
            </button>
          </div>
        </div>
      </div>

      {/* Mobile drawer */}
      <div className={`md:hidden ${open ? 'block' : 'hidden'}`}>
        <div className="px-2 pt-2 pb-3 space-y-1 sm:px-3 bg-white dark:bg-gray-900">
          {nav.map((item) => (
            <Link
              key={item.name}
              href={item.href}
              className="block px-3 py-2 rounded-md text-base font-medium text-gray-700 dark:text-gray-200 hover:bg-gray-100 dark:hover:bg-gray-800 transition"
              onClick={() => setOpen(false)}
            >
              {item.name}
            </Link>
          ))}

          <div className="mt-2 border-t border-gray-200 dark:border-gray-800 pt-3 px-3 space-y-2">
            <Link href="#" className="block px-3 py-2 rounded-md border border-indigo-500 text-indigo-600 text-center" target="_blank">LOG IN</Link>
            <Link href="#" className="block px-3 py-2 rounded-md bg-indigo-600 text-white text-center">SIGN UP</Link>
          </div>
        </div>
      </div>
    </header>
  )
}
