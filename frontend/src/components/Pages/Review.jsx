import React from 'react'

const Review = (props) => {
  return (
    <div className='response'>
        <p>{props.Ezra}</p>
        <figcaption>{props.Caption}</figcaption>
    </div>
  )
}

export default Review