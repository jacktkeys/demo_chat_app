export * from './string-to-color';
export * from './timestamp-to-time-ago';

export const getUser = () => {
    const userStr = sessionStorage.getItem('user');
    if (userStr) return JSON.parse(userStr);
    else return null;
}

export const removeUserSession = () => {
    sessionStorage.removeItem('user');
}

export const setUserSession = (user: {}) => {
    sessionStorage.setItem('user', JSON.stringify(user));
}