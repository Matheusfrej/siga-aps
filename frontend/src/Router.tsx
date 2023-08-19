import { Routes, Route } from 'react-router-dom'
import { Home } from './pages/Home'
import { Login } from './pages/Login'
import { Horarios } from './pages/Horarios'
import { CadastrarCadeira } from './pages/CadastrarCadeira'
import { ListagemCadeiras } from './pages/ListagemCadeiras'
import { Matricula } from './pages/Matricula'

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
      <Route path="/matricula" element={<Matricula />} />
    </Routes>
  )
}
