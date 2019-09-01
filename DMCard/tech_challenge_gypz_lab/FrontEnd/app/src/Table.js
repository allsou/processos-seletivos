import React, { Component } from 'react'
import axios from 'axios';

function validateReq(value){
  if(value){
    return 'Aprovado'
  }else{
    return 'Reprovado'
  }
}

function deleteReq(req_id){
  const API_URL = 'http://127.0.0.1:5000/cardrequest/';
  console.log(API_URL+req_id)
  axios.delete(API_URL+req_id).then(
    res =>{
      alert(res.data.message)
    }
  )
  window.location.reload()
}

const TableHeader = () => {
  return (
    <thead>
      <tr>
        <th>ID</th>
        <th>Nome</th>
        <th>Renda</th>
        <th>Score</th>
        <th>Status</th>
        <th>Crédito</th>
        <th>Eliminação (DELETE)</th>
      </tr>
    </thead>
  )
}
const TableBody = props => {
  console.log(props.requestsData);
  const rows = props.requestsData.map((row, index) => {
    return (
      <tr key={index}>
        <td>{row.req_id}</td>
        <td>{row.data.user.name}</td>
        <td>R${row.data.user.income}</td>
        <td>{row.data.user.score}</td>
        <td>{validateReq(row.data.status)}</td>
        <td>R${row.data.credit}</td>
        <td>
          <button onClick={() => deleteReq(row.req_id)}>Eliminar</button>
         </td>
      </tr>
    )
  })

  return <tbody>{rows}</tbody>
}

class Table extends Component {
  render() {
    const {requestsData} = this.props
    return (
      <table>
        <TableHeader />
        <TableBody requestsData={requestsData}/>
      </table>
    )
  }
}

export default Table