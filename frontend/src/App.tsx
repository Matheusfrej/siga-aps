import { BrowserRouter } from 'react-router-dom'
import { Router } from './Router'
import { SigabContextProvider } from './contexts/sigabContext'
import { ToastContainer } from 'react-toastify'
import 'react-toastify/dist/ReactToastify.css'

function App() {
  return (
    <SigabContextProvider>
      <BrowserRouter>
        <Router />
      </BrowserRouter>
      <ToastContainer />
    </SigabContextProvider>
  )
}

export default App
