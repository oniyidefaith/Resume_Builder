import React from 'react'
import hero_img from '../../images/hero_img.svg'
import {Link} from 'react-router-dom'
import Fade from 'react-reveal/Fade';

const LandingLeft = () => {
    let mark = "fa fa-check-circle fs-4"
  return (
    <div className='home_body'>
      <Fade left>
      <div className="home_left">
       <p className='headed_color'>Make a free resume online using ready made templates</p>
       <h3 className='big_header fs-1 fw-bold'>The Reactive Resume <br /> Builder</h3>
       <div className="marked_lists">
        <ul className='home_lists'>
           <li><i className={mark}></i> Access our entire collection of HR-approved resume designs</li>
           <li><i className={mark}></i>Automatic formatting saves time and helps bypass ATS software</li>
           <li><i className={mark}></i>Export your resume to JSON or PDF format</li>
        </ul>
       </div>
       <div className="home_btn">
       <Link className='btn btn-success' to="/About">Build My Resume Now</Link>
       </div>
</div>
</Fade>
<Fade right>
<div className="home_img">
        <img src={hero_img} className='online_resume' alt="Hiring" />
       </div>
       </Fade>
    </div>
  )
}

export default LandingLeft