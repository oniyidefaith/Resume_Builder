import React from 'react'
import Review from './Review'

const Testimonial = () => {
  return (
    <>
    <div>
        <h3 className='summary_head'>testimonial</h3>
        <p className='summary_text'>Good or bad, I would love to hear your opinion on Reactive Resume and how the experience has been for you. <br />
Here are some of the messages sent in by users across the world. <br />

You can reach out to me through my email or through the contact form on my website.</p>
    </div>
    <div className="responses"> 
     <Review Ezra='Hi Faith, Let me congratulate you on the awesome RxResume. After long and extensive searches on the internet for a good and clean CV generator, Resume Builder is truly a gem. Ive been using it to create all my CVs.'
     Caption='-Ezra'
     />
    </div>

</>
  )
}

export default Testimonial