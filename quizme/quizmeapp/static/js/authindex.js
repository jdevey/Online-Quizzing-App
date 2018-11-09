import React from 'react'
import ReactDOM from 'react-dom'

class QuizViews extends React.Component {
  handleClick() {
    console.log('this is:', this);
  }

  render() {
    // This syntax ensures `this` is bound within handleClick
    return (
      <div className="CreateQuiz">
        <button onClick={(e) => this.handleClick(e)}>
          Create New Quiz
        </button>
        <h2>My Quiznos Subs</h2>
      </div>
    );
  }
}


ReactDOM.render(
  <QuizViews />,
  	document.getElementById('authindex')
);

