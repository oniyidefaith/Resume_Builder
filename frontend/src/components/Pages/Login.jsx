import React, { useState } from 'react'
import LoginForm from './LoginForm'

const Login = (props) => {
  const [display, set_display] = useState(true)

  
  const style = {
    width: "30px",
    height: "30px",
    weight: "600",
    cursor: "pointer",
    border: "none",
  }
 
  const login_content ={  
    display: display? 'initial' : 'none',
    backgroundColor: "var(--login-box-color) !important",
    borderRadius: "0.5rem",
    height: "fit-content",
    fontSize: ".875rem",
    lineHeight: "1.25rem",
    padding: "2rem"
  }
  return (
    <>
    <React.Fragment>
    <div className='Login'>
      <div  className="login_content" style={login_content}>
        <div className="login_contents" >
       
          <div className="login_top d-flex">
            <div className="sub_login">
              <span> 
                <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" class="bi bi-box-arrow-in-right" viewBox="0 0 16 16">
                  <path fill-rule="evenodd" d="M6 3.5a.5.5 0 0 1 .5-.5h8a.5.5 0 0 1 .5.5v9a.5.5 0 0 1-.5.5h-8a.5.5 0 0 1-.5-.5v-2a.5.5 0 0 0-1 0v2A1.5 1.5 0 0 0 6.5 14h8a1.5 1.5 0 0 0 1.5-1.5v-9A1.5 1.5 0 0 0 14.5 2h-8A1.5 1.5 0 0 0 5 3.5v2a.5.5 0 0 0 1 0v-2z" />
                  <path fill-rule="evenodd" d="M11.854 8.354a.5.5 0 0 0 0-.708l-3-3a.5.5 0 1 0-.708.708L10.293 7.5H1.5a.5.5 0 0 0 0 1h8.793l-2.147 2.146a.5.5 0 0 0 .708.708l3-3z" />
                </svg>
              </span>
              <span>/</span>
              <span>Login to Your account</span>
            </div>
            <div className="animated_close_button" 
            >
              
              <lord-icon
                 onClick={() => set_display(false)}
                src="https://cdn.lordicon.com/nhfyhmlt.json"
                trigger="hover"
                colors="primary:#e4e4e4"
                style={style} 
              />
            
            </div>
          </div>
          <hr />
          <div className="summary_container">
            <p className='register_text'>Please enter your username and password associated with your account to login and access, manage and share your resumes.</p></div>
          <div className="login_form">  <LoginForm /></div>
        </div>
      </div>
    </div>
    </React.Fragment>
    </>
  )
}

export default Login