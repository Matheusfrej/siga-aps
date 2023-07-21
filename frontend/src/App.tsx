import { BrowserRouter } from 'react-router-dom'
import { Router } from './Router'
import { SigabContextProvider } from './contexts/sigabContext'

function App() {
  return (
    <SigabContextProvider>
      <BrowserRouter>
        <Router />
      </BrowserRouter>
    </SigabContextProvider>
  )
}

export default App
