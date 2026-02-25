import Navbar from '@/components/Navbar'
import { AuthProvider } from '@/context/AuthContext'
import React from 'react'

const layout = ({children}) => {
  return (
    <div>
      <AuthProvider>
        <Navbar />
        {children}
      </AuthProvider>

        </div>
  )
}

export default layout