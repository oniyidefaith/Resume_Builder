import React,{useState,useEffect} from 'react'
import BarLoader from "react-spinners/BarLoader";
import AboutPage from './Pages/AboutPage';

const About = () => {
let [loading, setLoading] = useState(false);
    useEffect(()=>{
        setLoading(true)
        setTimeout(()=>{
          setLoading(false)
        },8000)
      },[])
  return (
		<div className='About'>
			{
				loading ?
        <div className="center_loader">
				<BarLoader className='bar_loader' color={"#86E7D4"} loading={loading} size={30}/></div>
				:

			<AboutPage/>
			}
		</div>
  )
}

export default About