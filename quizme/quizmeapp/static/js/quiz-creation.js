import React from 'react'
import ReactDOM from 'react-dom'

class QCreateForm extends React.Component {
  constructor(props) {
    super(props);
    this.state = {value: ''};
    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {
    this.setState({value: event.target.value});
  }

  handleSubmit(event) {
    //TODO
  }

  render() {
    return (
    	<div className="quiz-creation-form">
        <form onSubmit={this.handleSubmit}>
          <label>
            <h2> Quiz Creation </h2> 
            Quiz title: <input type="text" value={this.state.value} onChange={this.handleChange} />
            <p/>
            <p/>
          </label>
          <input type="submit" value="Start adding questions" />
        </form>
      </div>
    );
  }
}

ReactDOM.render(
	<QCreateForm />,
  	document.getElementById('quiz-creation')
);
