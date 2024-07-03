// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
import { getAuth } from "firebase/auth"; 
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyBXHtc3agkwQ5IHPo2tY2hnLAafB315aEM",
  authDomain: "authentication-b4eb1.firebaseapp.com",
  projectId: "authentication-b4eb1",
  storageBucket: "authentication-b4eb1.appspot.com",
  messagingSenderId: "20509267302",
  appId: "1:20509267302:web:81b1686a05dbac5cd6a4a7",
  measurementId: "G-BHEDXHNM1P"
};


// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);

// Initialize Firebase Authentication and get a reference to the service
const auth = getAuth(app);

// Export the initialized Firebase app and authentication
export { app, analytics, auth };
