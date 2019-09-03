import React, { Component } from 'react'
import Table from './Table'
import Form from './Form'
import axios from 'axios'
const API_URL = 'http://127.0.0.1:5000'

class App extends Component {
    state = {
        reqs: []
      }
      componentDidMount() {
        const url = `${API_URL}/cardrequest/`;
        axios.get(url, { crossdomain: true }).then(response => response.data)
        .then((data) => {
          this.setState({ reqs: data })
         })
      }

  render() {
    return (
    <div className="container">
        <Table requestsData = {this.state.reqs}/>
        <Form />
    </div>
    )
  }
}

export default App