import React, { Component } from 'react';
import axios from 'axios';
const API_URL = 'http://localhost:5000';

class ListCardRequest extends Component {
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
        <div className="col-xs-8">
        <h1>React Axios Example</h1>
        {this.state.reqs.forEach(function(req){
          console.log(req.data.user.name)
        }
        )}
        </div>
       </div>
    );
  }

}


export default ListCardRequest;
