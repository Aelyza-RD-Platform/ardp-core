{% if cookiecutter.use_typescript == "y" %}
import React from 'react'
import './App.css'

function App(): JSX.Element {
  return (
    <div className="App">
      <header className="App-header">
        <h1>{{ cookiecutter.project_name }}</h1>
        <p>{{ cookiecutter.description }}</p>
      </header>
    </div>
  )
}

export default App
{% else %}
import React from 'react'
import './App.css'

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>{{ cookiecutter.project_name }}</h1>
        <p>{{ cookiecutter.description }}</p>
      </header>
    </div>
  )
}

export default App
{% endif %}
