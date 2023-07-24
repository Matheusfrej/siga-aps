import { useEffect, useState } from 'react';
import { deletarCadeiraRequest, getCadeiras } from '../../services/cadeiraService';
import { Header } from '../Header';
import styles from './styles.module.css'
import { NavLink } from 'react-router-dom';
import { Trash } from '@phosphor-icons/react';

interface CadeiraInterface{
  id: number;
  nome: string;
  plano_ensino: string;
  centro_universitario: string;
  horarios: any[];
}

export function ListagemCadeiras() {
  const [cadeiras, setCadeiras] = useState<CadeiraInterface[]>([]);

  useEffect(() => {
    fetchCadeiras();
  }, []);

  const fetchCadeiras = async () => {
    try {
      const response = await getCadeiras();
      setCadeiras(response);
    } catch (error) {
    }
  };

  const handleDeleteCadeira = async (cadeiraId: number) => {
    try {
      await deletarCadeiraRequest(cadeiraId);
      fetchCadeiras();
    } catch (error) {
    }
  };

  return (
    <>
      <Header />
      <div className={styles.listagemContainer}>
        <div className={styles.listagemContent}>
          <div style={{display: 'flex', gap: "2rem", justifyContent: "center", alignItems: "center"}}>
            <h1>Listagem de Cadeiras</h1>
            <button className='btn'>
              <NavLink to={'/cadastrar-cadeira'} className={styles.linkContainer}>
                <strong>Cadastrar uma nova cadeira</strong>
              </NavLink>
            </button>
          </div>
          <table className={styles.customTable}>
            <thead>
              <tr>
                <th>Nome</th>
                <th>Plano de Ensino</th>
                <th>Centro Universitário</th>
                <th>Ação</th>
              </tr>
            </thead>
            <tbody>
              {cadeiras.map((cadeira) => (
                <tr key={cadeira.id}>
                  <td>{cadeira.nome}</td>
                  <td>{cadeira.plano_ensino}</td>
                  <td>{cadeira.centro_universitario}</td>
                  <td><div style={{display: 'flex', alignItems: 'center', justifyContent: 'center'}}><button className='btn' onClick={() => handleDeleteCadeira(cadeira.id)}><Trash/></button></div></td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </>
  );
}
