import React from 'react'
import ReactDOM from 'react-dom'

export class HelloWorld extends React.Component {
	render() {
		return(
			<div className="helloWorld">
				this is a text test.
			</div>
		);
	}
}

ReactDOM.render(
	<HelloWorld />,
  	document.getElementById('react')
);