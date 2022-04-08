import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { models } from '../../models';
import { APIService } from '../../services';
import { getUser } from '../../utils';
import './new-chatroom.scss';

export interface NewChatroomProps {
}

export const NewChatroom: React.FunctionComponent<NewChatroomProps> = () => {
    const [name, setName] = useState('');
    const [errorMessage, setErrorMessage] = useState(false);
    const navigate = useNavigate();
    const creatingRoom = false;
    const user = getUser();

    const create = () => {
        APIService.createRoom(name, user.id).then(
            function(res) {
                if (typeof(res) == 'boolean') {
                    setErrorMessage(true);
                } else {
                    navigate('/chat');
                }
            }
        )
    };

    return (
        <div className='new-chatroom'>
            <div className='card'>
                <h2>Choose a name for the new room</h2>
                {errorMessage ? <label className="error">Pick another name. This one already exists.</label> : <label></label> }
                <label>
                    Room name
                    <input disabled={creatingRoom} value={name} onChange={(e) => setName(e.target.value)} />
                </label>
                <button disabled={creatingRoom} onClick={() => create()}>
                    Create Room
                </button>
            </div>
        </div>
    );
};
