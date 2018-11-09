import React from 'react'
import ReactDOM from 'react-dom'
import {browserHistory} from 'react-router'

class QuizViews extends React.Component {
  handleClick() {
    browserHistory.push('/quiz-creation');
  }

  render() {
    // This syntax ensures `this` is bound within handleClick
    return (
      <div className="CreateQuiz">
          <a href="quiz-creation"><button>Create New Quiz</button></a>
        <h2>My Quiznos Subs</h2>
      </div>
    );
  }
}


ReactDOM.render(
  <QuizViews />,
  	document.getElementById('authindex')
);

