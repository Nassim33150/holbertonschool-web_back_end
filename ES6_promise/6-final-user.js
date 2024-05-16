import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, fileName) {
    const promises = [];

    promises.push(signUpUser(firstName, lastName).then(value => {
        return { status: 'fulfilled', value };
    }).catch(error => {
        return { status: 'rejected', value: error };
    }));
    
    promises.push(uploadPhoto(fileName).then(value => {
        return { status: 'fulfilled', value };
    }).catch(error => {
        return { status: 'rejected', value: error };
    }));
    
    return Promise.all(promises);
}

