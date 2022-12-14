import React,{useState} from 'react'
import { Link } from 'react-router-dom'
import Summary from './Summary'
import Fade from 'react-reveal/Fade';
import "animate.css/animate.min.css";
import Testimonial from './Testimonial';
import Login from './Login';

const AboutPage = () => {
  const [link,setLink] = useState()
 
  const handle_click = () => {
    setLink(<Login/>)
  }
  return (
    <div className='About'>
      <div className='flexed_top'>
        <div className="flexed_img">
          <div className="flexed_top_content">
            <img src={require('../../images/resume builder logo.png'
            )} className='about_logo' alt="logo" />
            <div className="flexed_text">
              <h2 className='project_name'>Resume Builder</h2>
              <p className="small_text">A free resume builder web application</p>
              <div className="reg_flex">
                <Link  onClick={handle_click} className='login_about'>{link}Login</Link>
                <Link to="#" className='register_about'>Register</Link>
              </div>
            </div>
          </div>
        </div>

      </div>
      <Fade bottom>
        <Summary />
      </Fade>

      <Testimonial />
    </div>
  )
}

export default AboutPage