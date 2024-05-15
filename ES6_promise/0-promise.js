export default function getResponseFromAPI() {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
	    resolve(true);
	    const error = new Error("Une erreur s'est produite.");
	    reject(error);
    }, 1000);
  });
}
