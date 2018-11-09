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
    	<div className="question-creationn-form">
        <form onSubmit={this.handleSubmit}>
          <label>
            <h2> Question Creation </h2> 
            Question text: <input type="text" value={this.state.value} onChange={this.handleChange} /><p/>
            Answer 1 text: <input type="text" id="1"/><p/>
            Answer 2 text: <input type="text" id="2"/><p/>
            Answer 3 text: <input type="text" id="3"/><p/>
            Answer 4 text: <input type="text" id="4"/><p/>
            Correct answer: <p/>
            <input type="radio" name="correct" id="correct1" value="1" /><label>Option 1</label><p/>
            <input type="radio" name="correct" id="correct2" value="2" /><label>Option 2</label><p/>
            <input type="radio" name="correct" id="correct3" value="3" /><label>Option 3</label><p/>
            <input type="radio" name="correct" id="correct4" value="4" /><label>Option 4</label><p/>
          </label>
          <input type="submit" value="Add another question" /><p/>
          <input type="submit" value="Done creating quiz" /> 
        </form>
      </div>
    ); 
  }
}
            //<input type="radio" id="correct" value="0"><label for="correct">Option 1</label>
          //<input type="submit" value="Done creating quiz" /> 

ReactDOM.render(
	<QCreateForm />,
  	document.getElementById('question-creation')
);
