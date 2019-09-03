import React, { Component } from 'react'
import axios from 'axios';

function createReq(state){
    const API_URL = ' http://127.0.0.1:5000/cardrequest/'
    axios.post(API_URL, state).then(
        res =>{
            alert(res.data.message)
            location.reload(true)
        }
        
    ).catch(
      res =>{
          alert(res.data.message)
          location.reload(true)
      }
    )
}

class Form extends Component {
  constructor(props) {
    super(props)

    this.initialState = {
      name: '',
      income: '',
    }

    this.state = this.initialState
  }

  handleChange = event => {
    const { name, value } = event.target
  
    this.setState({
      [name]: value,
    })
  }
  submitForm = () => {
    createReq(this.state)
  }

  render() {
    const { name, income } = this.state;
  
    return (
        <div>
            <h1>Nova Requisição (POST)</h1>
            <form>
                <label>Name</label>
                <input
                type="text"
                name="name"
                value={name}
                onChange={this.handleChange} />
                <label>Renda R$</label>
                <input
                type="number"
                name="income"
                value={income}
                onChange={this.handleChange} />
                <input type="button" value="Enviar Requisição" onClick={this.submitForm} />
            </form>
      </div>
    );
  }
}

export default Form;