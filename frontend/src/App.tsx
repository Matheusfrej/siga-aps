import { BrowserRouter } from 'react-router-dom'
import { Router } from './Router'
import { Header } from './pages/Header'

function App() {
  return (
    <BrowserRouter>
      <Header />
      <Router />
    </BrowserRouter>
  )
}

export default App
