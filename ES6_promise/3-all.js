import { uploadPhoto, createUser } from './utils';

export function handleProfileSignup() {
    Promise.all([uploadPhoto(), createUser()]) // Attend que toutes les promesses soient résolues ou qu'au moins une soit rejetée
        .then(([photoData, userData]) => {
            console.log(`${res[0].body} ${res[1].firstName} ${res[1].lastName}`);
        })
        .catch(error => {
            console.log('Signup system offline');
        });
}

