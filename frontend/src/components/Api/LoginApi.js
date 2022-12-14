import React from 'react'
import axios from 'axios'


const LoginApi = () => {
    const login_api = `http://localhost:8000/api/login/`
    function submit(e){
      e.preventDefault();
      axios.get(login_api)
      .then(res=>
        res.json())
      .catch(err=>{
        console.log(err)
      })
  
    }
  return (
    <div>
      
    </div>
  )
}

export default LoginApi
