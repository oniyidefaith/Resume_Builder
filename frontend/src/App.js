import './App.css';
import LandingPage from './components/LandingPage';
import {BrowserRouter as Router, Route, Routes} from 'react-router-dom'
import About from './components/About';
import Login from './components/Pages/Login';

function App() {
  return (
<Router>
    <div className="content">
      <Routes>
      <Route path="/" element={<LandingPage/>} />
      </Routes>
      <Routes>
      <Route path="/About" element={<About/>} />
      </Routes>
      <Routes>
      <Route path="/Login" element={<Login/>} />
      </Routes>
    </div>
</Router>
  );
}

export default App;
