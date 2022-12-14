import React, { useState } from 'react'
import axios from 'axios'

const LoginForm = () => {
  const [data, setData] = useState(null)
 const login_api = `http://localhost:8000/api/login/`
  function submit(e){
    e.preventDefault();
    axios.get(login_api)
    .then(res=>
      res.json())
      .then(res=>{console.log(res)
      setData(res)})
    .catch(err=>{
      console.log(err)
    })

  }



  return (
    <div>
      <form onSubmit={(e)=>submit(e)}>
        <div>
          <input type="text"  id='username' value={data.username} placeholder='username' />
          <label htmlFor="">{data.err}</label>
        </div>
        <div>
          <input type="password"  id='password' value={data.password} placeholder='Password' />
          <label htmlFor=""></label>
        </div>
        <button className='login_about'>Login</button>
      </form>
    </div>
  )
}

export default LoginForm