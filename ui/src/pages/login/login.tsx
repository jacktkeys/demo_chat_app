import './login.scss';
import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { APIService } from '../../services';
import { setUserSession } from '../../utils';

export interface LoginProps { }

export const LoginPage: React.FunctionComponent<LoginProps> = () => {
    var loggedIn = false;
    const [username, setUsername] = useState('');
    const [loginError, setLoginError] = useState(false)
    const navigate = useNavigate();

    const login = () => {
        APIService.login(username).then(
            function(res) {
                if ('id' in res) {
                    setUserSession(res);
                    navigate("/chat");
                } else {
                    setLoginError(true)
                }
            }
        );
    }

    return (
        <div id='container'>
            <div className='login'>
                <div className='welcome-card'>
                    <h1>
                        welcome to <span className='app-name'>the chat site</span>
                    </h1>
                    <h2>Please login or <Link to='/sign-up'>sign up</Link></h2>
                    {loginError ? (<label className="error">There was an error logging in</label>) : <label></label>}
                    <label>
                        Username
                        <input type='text' value={username} onChange={(e) => setUsername(e.target.value.toLowerCase())} />
                    </label>
                    <button type='submit' onClick={() => login()}>
                        Submit
                    </button>
                </div>
            </div>
        </div>
    );
};
