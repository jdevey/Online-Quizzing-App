import React from 'react'
import ReactDOM from 'react-dom'

class GameIDForm extends React.Component {
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
    alert('A pin was submitted: ' + this.state.value);
    event.preventDefault();
  }

  render() {
    return (
    	<div className="gameIDForm">
      		<form onSubmit={this.handleSubmit}>
        		<label>
          			<h2>Enter a Game ID to Play!</h2> 
                <div/>
          		<input type="text" value={this.state.value} onChange={this.handleChange} />
              <div/>
              <div/>
        		</label>
        		<input type="submit" value="Submit" />
      		</form>
      	</div>
    );
  }
}

ReactDOM.render(
	<GameIDForm />,
  	document.getElementById('notauthindex')
);

