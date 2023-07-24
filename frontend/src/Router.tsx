import { Routes, Route } from 'react-router-dom'
import { Home } from './pages/Home'
import { Login } from './pages/Login'
import { Horarios } from './pages/Horarios'
import { CadastrarCadeira } from './pages/CadastrarCadeira'
import { ListagemCadeiras } from './components/ListagemCadeiras'

export function Router() {
  return (
    <Routes>
      <Route path="/login" element={<Login />} />
      <Route path="/" element={<Home />} />
      <Route path="/horarios" element={<Horarios />} />
      <Route
        path="/visualizar-minhas-cadeiras"
        element={<ListagemCadeiras />}
      />
      <Route path="/cadastrar-cadeira" element={<CadastrarCadeira />} />
    </Routes>
  )
}
