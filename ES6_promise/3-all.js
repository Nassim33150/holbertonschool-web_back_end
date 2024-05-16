import { uploadPhoto, createUser } from './utils';

export function handleProfileSignup() {
    Promise.all([uploadPhoto(), createUser()])
        .then(([photoData, userData]) => {
            console.log(`body ${userData.firstName} ${userData.lastName}`);
        })
        .catch(error => {
            console.log('Signup system offline');
        });
}
