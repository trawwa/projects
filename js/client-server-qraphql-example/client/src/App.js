import logo from './logo.svg';
import './App.css';
import { useEffect, useState } from 'react';
import { useMutation, useQuery } from '@apollo/client';
import { GET_ALL_USERS } from './query/user';
import { GET_ONE_USER } from './query/user';
import { CREATE_USER } from './mutations/user';

function App() {
  const {data, loading, error, refetch} = useQuery(GET_ALL_USERS)
  const {data:oneUser, loading: loadingOneUser} = useQuery(GET_ONE_USER, {
    variables: {
      id: 1
    }
  })
  const [newUser] = useMutation(CREATE_USER)
  const [users, setUsers] = useState([])
  const [username, setUsername] = useState('')
  const [age, setAge] = useState(0)
  
  console.log(oneUser)
  
  useEffect(() => {
    if (!loading) {
      setUsers(data.getAllUsers)
    }
  }, [data])

  const addUser = e => {
    e.preventDefault()
    newUser({
      variables: {
        input: {
          username, age
        }
      }
    }).then(({data}) => {
      console.log(data)
      setUsername('')
      setAge()
      
    })
  }
  const getAll = e => {
    e.preventDefault()
    refetch()
  }

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Developing...
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
        <form>
          <input value={username} onChange={e => setUsername(e.target.value)} type="text"/>
          <input value={age} onChange={e => setAge(e.target.value)} type="number"/>
          <div className='btns'>
            <button onClick={e => addUser(e)}>Создать</button>
            <button onClick={e => getAll(e)}>Получить</button>
          </div>
      </form>
      <div>
        {users.map(user =>
          <div className='user'>{user.id}. {user.username}. {user.age}</div>
        )}
      </div>
      </header>
    </div>
  );
};

export default App;
