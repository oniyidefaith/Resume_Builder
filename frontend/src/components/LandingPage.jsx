import React from 'react'
import NavBar from './NavBar'
import LandingLeft from './Pages/LandingLeft'

const LandingPage = () => {
  return (
    <div className='Home'>
        <div className='Navbar'>
            <NavBar/>
        </div>
        <div className='home_left_page'>
          <LandingLeft/>
        </div>
    </div>
  )
}

export default LandingPage