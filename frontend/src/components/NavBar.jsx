import React from 'react'
import {Link} from 'react-router-dom'


const NavBar = () => {

  return (
    <div className='Nav'>
     
        <div className='Logo'>
            <h3 className='logo'>ResumeBuilder</h3>
        </div>
        <div className='Nav_list'>
            <Link className='btn btn-success' to="/About">Build My Resume Now</Link>
            <Link className='fs-4 link' to='#'>Login</Link>
        </div>
    </div>
  )
}

export default NavBar