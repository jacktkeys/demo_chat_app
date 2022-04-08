import './sign-up.scss';
import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { APIService } from '../../services';
import { setUserSession } from '../../utils';

interface SignUpProps {
}

export const SignUpPage: React.FunctionComponent<SignUpProps> = () => {
    const navigate = useNavigate();
    const [username, setUsername] = useState('');
    const [errorMessage, setErrorMessage] = useState(false);

    const signUp = () => {
        APIService.createUser(username).then(function(res){
            if (typeof(res) == 'boolean') {
                setErrorMessage(true);
            } else {
                setUserSession(res);
                navigate('/chat')
            }
        });
    };

    return (
        <div id='container'>
            <div className='sign-up'>
                <div className='welcome-card'>
                    <h1>
                        welcome to <span className='app-name'>the chat site</span>
                    </h1>
                    <h2>Create your account or <Link to='/login'>back to login</Link></h2>
                    {errorMessage ? <label className="error">Pick another name. This one already exists.</label> : <label></label> }
                    <label>
                        Username
                        <input type='text' value={username} onChange={(e) => { setErrorMessage(false); setUsername(e.target.value.toLowerCase()); } } />
                    </label>
                    <button onClick={() => signUp()} type='submit' >
                        Submit
                    </button>
                </div>
            </div>
        </div>
    );
};
